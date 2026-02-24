#!/bin/bash
#
# Unified NetFlow & sFlow Stack Deployment Script
# Managed by Viktor Petrov (TeleHouse/TelePoint)
#

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

log_info() { echo -e "${BLUE}[INFO]${NC} $1"; }
log_success() { echo -e "${GREEN}[OK]${NC}   $1"; }
log_warn() { echo -e "${YELLOW}[WARN]${NC}  $1"; }
log_error() { echo -e "${RED}[ERROR]${NC} $1"; }

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONFIG_FILE="${SCRIPT_DIR}/deploy.conf"

# Detect Docker Compose
if command -v docker-compose &> /dev/null; then
    DC="docker-compose"
else
    DC="docker compose"
fi

create_example_config() {
    cat > "$CONFIG_FILE" << EOF
# Deployment Configuration
CLUSTER_NAME="netflow-cluster"
STACK_VERSION="9.2.4"
ELASTIC_PASSWORD="telehouse"
KIBANA_PASSWORD="telehouse"

# Generated encryption keys: openssl rand -base64 32
KIBANA_ENCRYPTION_KEY="$(openssl rand -base64 32)"
KIBANA_SECURITY_KEY="$(openssl rand -base64 32)"
KIBANA_REPORTING_KEY="$(openssl rand -base64 32)"

FRONTEND_IP="192.168.1.10"
BACKEND_IPS="192.168.1.21,192.168.1.90"
EOF
    log_info "Example config created at: $CONFIG_FILE"
}

load_config() {
    if [ ! -f "$CONFIG_FILE" ]; then
        log_error "Config file not found. Run $0 --generate first."
        exit 1
    fi
    source "$CONFIG_FILE"
}

create_env_file() {
    cat > "$SCRIPT_DIR/.env" << EOF
CLUSTER_NAME=$CLUSTER_NAME
STACK_VERSION=$STACK_VERSION
ELASTIC_PASSWORD=$ELASTIC_PASSWORD
KIBANA_PASSWORD=$KIBANA_PASSWORD
KIBANA_ENCRYPTION_KEY=$KIBANA_ENCRYPTION_KEY
KIBANA_SECURITY_KEY=$KIBANA_SECURITY_KEY
KIBANA_REPORTING_KEY=$KIBANA_REPORTING_KEY
FRONTEND_IP=$FRONTEND_IP
EOF
    log_info "Created .env file"
}

deploy_frontend() {
    log_info "Deploying Frontend (ES + Kibana)..."
    create_env_file
    $DC -f docker-compose-frontend.yml up -d
}

deploy_backend() {
    log_info "Deploying Backend (Collector)..."
    local current_ip=$(hostname -I | awk '{print \$1}')
    
    # Check if we're on a backend server or if user forces it
    # For automated scripts, we just assume this is a backend if called with --backend
    
    cat > "$SCRIPT_DIR/.env" << EOF
CLUSTER_NAME=$CLUSTER_NAME
STACK_VERSION=$STACK_VERSION
ELASTIC_PASSWORD=$ELASTIC_PASSWORD
FRONTEND_IP=$FRONTEND_IP
BACKEND_IP=$current_ip
EOF

    $DC -f docker-compose-backend.yml up -d
}

apply_templates() {
    log_info "Applying ILM Policy and Index Templates from templates/ folder..."
    
    # 1. ILM Policy
    curl -s -k -u "elastic:$ELASTIC_PASSWORD" -X PUT "https://$FRONTEND_IP:9200/_ilm/policy/logstash-flow-policy" \
        -H "Content-Type: application/json" -d @templates/logstash-flow-policy.json
    
    # 2. Index Template
    curl -s -k -u "elastic:$ELASTIC_PASSWORD" -X PUT "https://$FRONTEND_IP:9200/_index_template/logstash-flow" \
        -H "Content-Type: application/json" -d @templates/logstash-flow-template.json
        
    # 3. Bootstrap initial index
    log_info "Bootstrapping initial serialized index..."
    curl -s -k -u "elastic:$ELASTIC_PASSWORD" -X PUT "https://$FRONTEND_IP:9200/%3Clogstash-flow-%7Bnow%2Fd%7D-000001%3E" \
        -H "Content-Type: application/json" -d '{"aliases": {"logstash-flow-write": {"is_write_index": true}}}'
    
    log_success "Templates and bootstrap applied to https://$FRONTEND_IP:9200"
}

setup_cron() {
    log_info "Setting up hourly maintenance cron job..."
    (crontab -l 2>/dev/null | grep -v "prune_indices.sh"; echo "0 * * * * $SCRIPT_DIR/scripts/prune_indices.sh $ELASTIC_PASSWORD >> $SCRIPT_DIR/maintenance.log 2>&1") | crontab -
    log_success "Cron job established."
}

import_dashboards() {
    log_info "Importing Dashboards from dashboards/ folder..."
    for f in dashboards/*.ndjson; do
        log_info "Importing $f..."
        curl -s -k -u "elastic:$ELASTIC_PASSWORD" \
            -X POST "http://$FRONTEND_IP:5601/api/saved_objects/_import?overwrite=true" \
            -H "kbn-xsrf: true" --form file=@"$f"
    done
    log_success "Dashboard import process complete."
}

case "$1" in
    --generate) create_example_config ;;
    --frontend) load_config; deploy_frontend; apply_templates; setup_cron ;;
    --backend)  load_config; deploy_backend ;;
    --import)   load_config; import_dashboards ;;
    *) echo "Usage: $0 {--generate|--frontend|--backend|--import}" ;;
esac

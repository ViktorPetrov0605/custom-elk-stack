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
    cat > "$CONFIG_FILE" << 'EOF'
# Deployment Configuration
CLUSTER_NAME="netflow-cluster"
STACK_VERSION="9.2.4"
ELASTIC_PASSWORD="CHANGEME"
FRONTEND_IP="10.4.4.87"
BACKEND_IPS="10.4.4.21,10.4.4.90"
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

deploy_frontend() {
    log_info "Deploying Frontend (ES + Kibana)..."
    $DC -f docker-compose-frontend.yml up -d
}

deploy_backend() {
    log_info "Deploying Backend (Collector)..."
    $DC -f docker-compose-backend.yml up -d
}

apply_templates() {
    log_info "Applying ILM Policy and Index Templates from templates/ folder..."
    
    # 1. ILM Policy
    curl -s -k -u "elastic:$ELASTIC_PASSWORD" -X PUT "https://$FRONTEND_IP:9200/_ilm/policy/logstash-flow-policy" \
        -H "Content-Type: application/json" -d @templates/logstash-flow-policy.json
    
    # 2. Index Template
    curl -s -k -u "elastic:$ELASTIC_PASSWORD" -X PUT "https://$FRONTEND_IP:9200/_index_template/logstash-flow-template" \
        -H "Content-Type: application/json" -d @templates/logstash-flow-template.json
    
    log_success "Templates applied to https://$FRONTEND_IP:9200"
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
    --frontend) load_config; deploy_frontend; apply_templates ;;
    --backend)  load_config; deploy_backend ;;
    --import)   load_config; import_dashboards ;;
    *) echo "Usage: $0 {--generate|--frontend|--backend|--import}" ;;
esac

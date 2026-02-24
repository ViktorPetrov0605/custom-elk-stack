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
LICENSE="basic"
MEM_LIMIT="4294967296"

# Connectivity
FRONTEND_IP="{YOUR_FRONTEND_IP}"
BACKEND_IPS="{YOUR_BACKEND_IP_1},{YOUR_BACKEND_IP_2}"
ES_PORT="9200"
KIBANA_PORT="5601"

# Security
ELASTIC_PASSWORD="telehouse"
KIBANA_PASSWORD="telehouse"

# Generated encryption keys: openssl rand -base64 32
KIBANA_ENCRYPTION_KEY="$(openssl rand -base64 32)"
KIBANA_SECURITY_KEY="$(openssl rand -base64 32)"
KIBANA_REPORTING_KEY="$(openssl rand -base64 32)"
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

generate_certificates() {
    log_info "Checking certificates..."
    local certs_dir="$SCRIPT_DIR/certs"

    if [ -f "$certs_dir/ca/ca.crt" ] && [ -f "$certs_dir/wildcard/wildcard.crt" ]; then
        log_success "Certificates already exist"
        return 0
    fi

    log_info "Generating certificates..."
    mkdir -p "$certs_dir/ca" "$certs_dir/wildcard"

    # Generate CA
    openssl req -x509 -new -nodes -sha256 -days 3650 \
        -subj "/CN=elasticsearch-ca" \
        -addext "basicConstraints=critical,CA:TRUE" \
        -addext "keyUsage=critical,keyCertSign,cRLSign" \
        -keyout "$certs_dir/ca/ca.key" \
        -out "$certs_dir/ca/ca.crt" 2>/dev/null

    # Create SAN config
    cat > "$certs_dir/wildcard.cnf" << EOF
[req]
distinguished_name = req_distinguished_name
x509_extensions = v3_req
prompt = no

[req_distinguished_name]
CN = *.flow-monitoring.local

[v3_req]
basicConstraints = CA:FALSE
keyUsage = critical, digitalSignature, keyEncipherment, dataEncipherment
extendedKeyUsage = serverAuth, clientAuth
subjectAltName = @alt_names

[alt_names]
DNS.1 = localhost
DNS.2 = *.flow-monitoring.local
DNS.3 = elasticsearch
DNS.4 = kibana
DNS.5 = es-remote
IP.1 = 127.0.0.1
IP.2 = $FRONTEND_IP
EOF

    # Generate and sign certificate
    openssl req -new -nodes -sha256 \
        -config "$certs_dir/wildcard.cnf" \
        -keyout "$certs_dir/wildcard/wildcard.key" \
        -out "$certs_dir/wildcard/wildcard.csr" 2>/dev/null

    openssl x509 -req -sha256 -days 3650 \
        -in "$certs_dir/wildcard/wildcard.csr" \
        -CA "$certs_dir/ca/ca.crt" \
        -CAkey "$certs_dir/ca/ca.key" \
        -CAcreateserial \
        -extensions v3_req \
        -extfile "$certs_dir/wildcard.cnf" \
        -out "$certs_dir/wildcard/wildcard.crt" 2>/dev/null

    chmod 600 "$certs_dir/ca/ca.key" "$certs_dir/wildcard/wildcard.key" 2>/dev/null || true
    chmod 755 "$certs_dir"

    log_success "Certificates generated"
}

create_unicast_hosts() {
    local unicast_file="$SCRIPT_DIR/unicast_hosts.txt"
    
    # Start fresh
    echo "$FRONTEND_IP:9300" > "$unicast_file"
    echo "$FRONTEND_IP:9301" >> "$unicast_file"
    
    IFS=',' read -ra BACKEND_ARRAY <<< "$BACKEND_IPS"
    for ip in "${BACKEND_ARRAY[@]}"; do
        ip=$(echo "$ip" | xargs)
        if [ ! -z "$ip" ] && [ "$ip" != "$FRONTEND_IP" ]; then
            echo "$ip:9300" >> "$unicast_file"
        fi
    done
    
    log_info "Generated unicast_hosts.txt with $(wc -l < "$unicast_file") entries"
}

create_env_file() {
    cat > "$SCRIPT_DIR/.env" << EOF
CLUSTER_NAME=$CLUSTER_NAME
STACK_VERSION=$STACK_VERSION
LICENSE=${LICENSE:-basic}
MEM_LIMIT=${MEM_LIMIT:-4294967296}
ELASTIC_PASSWORD=$ELASTIC_PASSWORD
KIBANA_PASSWORD=$KIBANA_PASSWORD
KIBANA_ENCRYPTION_KEY=$KIBANA_ENCRYPTION_KEY
KIBANA_SECURITY_KEY=$KIBANA_SECURITY_KEY
KIBANA_REPORTING_KEY=$KIBANA_REPORTING_KEY
FRONTEND_IP=$FRONTEND_IP
ES_PORT=${ES_PORT:-9200}
KIBANA_PORT=${KIBANA_PORT:-5601}
EOF
    log_info "Created .env file"
}

deploy_frontend() {
    log_info "Deploying Frontend (ES + Kibana)..."
    create_env_file
    create_unicast_hosts
    generate_certificates
    $DC -f docker-compose-frontend.yml up -d
}

deploy_backend() {
    log_info "Deploying Backend (Collector)..."
    local current_ip=$(hostname -I | awk '{print $1}')
    
    cat > "$SCRIPT_DIR/.env" << EOF
CLUSTER_NAME=$CLUSTER_NAME
STACK_VERSION=$STACK_VERSION
LICENSE=${LICENSE:-basic}
MEM_LIMIT=${MEM_LIMIT:-4294967296}
ELASTIC_PASSWORD=$ELASTIC_PASSWORD
FRONTEND_IP=$FRONTEND_IP
BACKEND_IP=$current_ip
ES_PORT=${ES_PORT:-9200}
EOF

    $DC -f docker-compose-backend.yml up -d
}

apply_templates() {
    log_info "Applying ILM Policy and Index Templates from templates/ folder..."
    local ES_URL="https://$FRONTEND_IP:${ES_PORT:-9200}"
    
    # 1. ILM Policy
    curl -s -k -u "elastic:$ELASTIC_PASSWORD" -X PUT "$ES_URL/_ilm/policy/logstash-flow-policy" \
        -H "Content-Type: application/json" -d @templates/logstash-flow-policy.json
    
    # 2. Index Template
    curl -s -k -u "elastic:$ELASTIC_PASSWORD" -X PUT "$ES_URL/_index_template/logstash-flow" \
        -H "Content-Type: application/json" -d @templates/logstash-flow-template.json
        
    # 3. Bootstrap initial index
    log_info "Bootstrapping initial serialized index..."
    curl -s -k -u "elastic:$ELASTIC_PASSWORD" -X PUT "$ES_URL/%3Clogstash-flow-%7Bnow%2Fd%7D-000001%3E" \
        -H "Content-Type: application/json" -d '{"aliases": {"logstash-flow-write": {"is_write_index": true}}}'
    
    log_success "Templates and bootstrap applied to $ES_URL"
}

setup_cron() {
    log_info "Setting up hourly maintenance cron job..."
    (crontab -l 2>/dev/null | grep -v "prune_indices.sh"; echo "0 * * * * $SCRIPT_DIR/scripts/prune_indices.sh elastic $ELASTIC_PASSWORD >> $SCRIPT_DIR/maintenance.log 2>&1") | crontab -
    log_success "Cron job established."
}

import_dashboards() {
    log_info "Importing Dashboards from dashboards/ folder..."
    for f in dashboards/*.ndjson; do
        log_info "Importing $f..."
        curl -s -k -u "elastic:$ELASTIC_PASSWORD" \
            -X POST "http://$FRONTEND_IP:${KIBANA_PORT:-5601}/api/saved_objects/_import?overwrite=true" \
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

#!/bin/bash
#
# ELK Stack with Logstash Deployment Script
# Deploys Elasticsearch/Kibana frontend + Logstash collectors
#
# Usage: ./deploy.sh [OPTIONS]
#   -h, --help      Show help
#   -g, --generate  Generate example config file
#   -c, --check     Check prerequisites only
#   -f, --frontend  Deploy frontend (ES + Kibana) only
#   -b, --backend   Deploy backend (ES remote + Logstash) only
#   -i, --import    Import Kibana dashboards only
#   -v, --verify    Verify deployment health

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

# Detect Docker Compose command
if command -v docker-compose &> /dev/null; then
    DC="docker-compose"
elif docker compose version &> /dev/null; then
    DC="docker compose"
else
    DC="docker-compose" # fallback for check function
fi
CONFIG_FILE="${SCRIPT_DIR}/deploy.conf"

# ============================================================
# CONFIGURATION
# ============================================================

create_example_config() {
    cat > "$CONFIG_FILE" << 'EOF'
# ELK Stack with Logstash Deployment Configuration
# Copy this file and customize for your environment

# ============================================================
# ELASTICSEARCH CLUSTER
# ============================================================
CLUSTER_NAME="netflow-cluster"
STACK_VERSION="9.2.4"
LICENSE="basic"
MEM_LIMIT="4294967296"

# ============================================================
# SECURITY (CHANGE THESE!)
# ============================================================
ELASTIC_PASSWORD="your-secure-password-here"
KIBANA_PASSWORD="your-kibana-password-here"

# Generate encryption keys: openssl rand -base64 32
KIBANA_ENCRYPTION_KEY=""
KIBANA_SECURITY_KEY=""
KIBANA_REPORTING_KEY=""

# ============================================================
# FRONTEND SERVER (Kibana + Elasticsearch)
# ============================================================
FRONTEND_IP="10.4.4.87"
ES_PORT="9200"
KIBANA_PORT="5601"

# ============================================================
# BACKEND SERVERS (Logstash Collectors)
# Comma-separated list of all backend IPs
# ============================================================
BACKEND_IP="10.4.4.21,10.4.4.90"

# ============================================================
# DASHBOARDS & ILM
# ============================================================
DASHBOARD_FILE="$SCRIPT_DIR/dashboards/unified-flow-dashboards.ndjson"
ILM_POLICY_FILE="$SCRIPT_DIR/ilm-policy.json"
EOF
    
    log_info "Example config created at: $CONFIG_FILE"
    log_info "Please edit it with your actual settings"
}

load_config() {
    if [ ! -f "$CONFIG_FILE" ]; then
        log_error "Config file not found: $CONFIG_FILE"
        log_info "Run: ./deploy.sh --generate"
        exit 1
    fi
    
    source "$CONFIG_FILE"
    
    # Validate required variables
    local required_vars=(
        "CLUSTER_NAME" "STACK_VERSION" "ELASTIC_PASSWORD"
        "FRONTEND_IP"
    )
    
    for var in "${required_vars[@]}"; do
        if [ -z "${!var}" ]; then
            log_error "Missing required config variable: $var"
            exit 1
        fi
    done
    
    # Generate Kibana keys if not set
    if [ -z "$KIBANA_ENCRYPTION_KEY" ]; then
        KIBANA_ENCRYPTION_KEY=$(openssl rand -base64 32)
        KIBANA_SECURITY_KEY=$(openssl rand -base64 32)
        KIBANA_REPORTING_KEY=$(openssl rand -base64 32)
        log_info "Generated Kibana encryption keys"
    fi
}

# ============================================================
# PREREQUISITES
# ============================================================

check_prerequisites() {
    log_info "Checking prerequisites..."
    
    local missing=()
    
    command -v docker &> /dev/null || missing+=("docker")
    if ! command -v docker-compose &> /dev/null && ! docker compose version &> /dev/null; then
        missing+=("docker-compose or docker-plugin-compose")
    fi
    command -v openssl &> /dev/null || missing+=("openssl")
    command -v curl &> /dev/null || missing+=("curl")
    
    if [ ${#missing[@]} -gt 0 ]; then
        log_error "Missing: ${missing[*]}"
        log_info "Install with: sudo apt-get install ${missing[*]}"
        exit 1
    fi
    
    if ! groups | grep -q docker; then
        log_warn "User not in docker group. Run: sudo usermod -aG docker $USER"
    fi
    
    if ! docker ps &> /dev/null; then
        log_error "Cannot run docker. Check permissions or start docker service."
        exit 1
    fi
    
    log_success "All prerequisites met"
}

# ============================================================
# CERTIFICATES
# ============================================================

generate_certificates() {
    log_info "Checking certificates..."
    
    local certs_dir="$SCRIPT_DIR/certs"
    
    if [ -f "$certs_dir/ca/ca.crt" ] && [ -f "$certs_dir/wildcard/wildcard.crt" ]; then
        log_success "Certificates already exist"
        return 0
    fi
    
    log_info "Generating certificates..."
    mkdir -p "$certs_dir/ca" "$certs_dir/wildcard"
    
    # Generate CA with proper extensions
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
    
    chmod 600 "$certs_dir"/*.key 2>/dev/null || true
    chmod 755 "$certs_dir"
    
    log_success "Certificates generated"
}

# ============================================================
# UNICAST HOSTS
# ============================================================

create_unicast_hosts() {
    local unicast_file="$SCRIPT_DIR/unicast_hosts.txt"
    
    # Frontend nodes
    echo "$FRONTEND_IP:9300" > "$unicast_file"
    echo "$FRONTEND_IP:9301" >> "$unicast_file"
    
    # Backend nodes
    IFS=',' read -ra BACKEND_IPS <<< "$BACKEND_IP"
    for ip in "${BACKEND_IPS[@]}"; do
        ip=$(echo "$ip" | xargs)  # trim whitespace
        echo "$ip:9300" >> "$unicast_file"
    done
    
    log_info "Created unicast_hosts.txt with $(wc -l < "$unicast_file") entries"
}

# ============================================================
# ENV FILE
# ============================================================

create_env_file() {
    cat > "$SCRIPT_DIR/.env" << EOF
CLUSTER_NAME=$CLUSTER_NAME
STACK_VERSION=$STACK_VERSION
LICENSE=$LICENSE
MEM_LIMIT=$MEM_LIMIT
ELASTIC_PASSWORD=$ELASTIC_PASSWORD
KIBANA_PASSWORD=${KIBANA_PASSWORD:-$ELASTIC_PASSWORD}
KIBANA_ENCRYPTION_KEY=$KIBANA_ENCRYPTION_KEY
KIBANA_SECURITY_KEY=$KIBANA_SECURITY_KEY
KIBANA_REPORTING_KEY=$KIBANA_REPORTING_KEY
FRONTEND_IP=$FRONTEND_IP
BACKEND_IP=$BACKEND_IP
ES_PORT=$ES_PORT
KIBANA_PORT=$KIBANA_PORT
EOF
    log_info "Created .env file"
}

# ============================================================
# FRONTEND DEPLOYMENT (Elasticsearch + Kibana)
# ============================================================

deploy_frontend() {
    log_info "=========================================="
    log_info "DEPLOYING FRONTEND (Elasticsearch + Kibana)"
    log_info "=========================================="
    
    generate_certificates
    create_unicast_hosts
    create_env_file
    
    cd "$SCRIPT_DIR"
    
    log_info "Starting Elasticsearch and Kibana..."
    $DC -f docker-compose-frontend.yml down 2>/dev/null || true
    $DC -f docker-compose-frontend.yml up -d
    
    log_info "Waiting for Elasticsearch..."
    local retries=30
    while [ $retries -gt 0 ]; do
        if curl -s -k "https://$FRONTEND_IP:$ES_PORT/_cluster/health" \
            -u "elastic:$ELASTIC_PASSWORD" 2>/dev/null | grep -q "green\|yellow"; then
            log_success "Elasticsearch is up"
            break
        fi
        sleep 10
        ((retries--))
        echo -n "."
    done
    
    if [ $retries -eq 0 ]; then
        log_error "Elasticsearch failed to start"
        $DC -f docker-compose-frontend.yml logs es-frontend 2>/dev/null | tail -20
        exit 1
    fi
    
    log_info "Waiting for Kibana..."
    retries=60
    while [ $retries -gt 0 ]; do
        if curl -s "http://$FRONTEND_IP:$KIBANA_PORT/api/status" 2>/dev/null | grep -q "available"; then
            log_success "Kibana is up at http://$FRONTEND_IP:$KIBANA_PORT"
            break
        fi
        sleep 5
        ((retries--))
        echo -n "."
    done
    
    if [ $retries -eq 0 ]; then
        log_error "Kibana failed to start"
        $DC -f docker-compose-frontend.yml logs kibana 2>/dev/null | tail -20
        exit 1
    fi
    
    log_success "Frontend deployment complete"
}

# ============================================================
# BACKEND DEPLOYMENT (ES Remote + Logstash)
# ============================================================

deploy_backend() {
    log_info "Deploying Backend (Collector)..."
    
    # Identify which of the local IPs belongs to the BACKEND_IPS list in deploy.conf
    local current_ip=""
    local local_ips=\$(hostname -I)
    
    IFS="," read -ra CONF_IPS <<< "\$BACKEND_IPS"
    for c_ip in "\${CONF_IPS[@]}"; do
        c_ip=\$(echo "\$c_ip" | xargs) # trim
        for l_ip in \$local_ips; do
            if [ "\$c_ip" == "\$l_ip" ]; then
                current_ip="\$c_ip"
                break 2
            fi
        done
    done

    if [ -z "\$current_ip" ]; then
        log_error "Could not find a local IP matching the BACKEND_IPS list in deploy.conf"
        exit 1
    fi

    log_info "Identified local backend IP: \$current_ip"

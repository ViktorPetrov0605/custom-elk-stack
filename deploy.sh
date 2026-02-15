#!/bin/bash
#
# ELK Stack with ElastiFlow Deployment Script
# Deploys Elasticsearch/Kibana frontend + ElastiFlow collectors
#
# Usage: ./deploy.sh [OPTIONS]
#   -h, --help      Show help
#   -g, --generate  Generate example config file
#   -c, --check     Check prerequisites only
#   -f, --frontend  Deploy frontend (ES + Kibana) only
#   -e, --elastiflow Deploy ElastiFlow collector only
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
CONFIG_FILE="${SCRIPT_DIR}/deploy.conf"

# ============================================================
# CONFIGURATION
# ============================================================

create_example_config() {
    cat > "$CONFIG_FILE" << 'EOF'
# ELK Stack with ElastiFlow Deployment Configuration
# Copy this file and customize for your environment

# ============================================================
# ELASTICSEARCH CLUSTER
# ============================================================
CLUSTER_NAME="flow-monitoring-cluster"
STACK_VERSION="8.16.0"
LICENSE="basic"
MEM_LIMIT="4g"

# ============================================================
# SECURITY (CHANGE THESE!)
# ============================================================
ELASTIC_PASSWORD="your-secure-password-here"
KIBANA_PASSWORD="your-kibana-password-here"

# Generate encryption keys: openssl rand -hex 32
KIBANA_ENCRYPTION_KEY=""
KIBANA_SECURITY_KEY=""
KIBANA_REPORTING_KEY=""

# ============================================================
# FRONTEND SERVER (Kibana + Elasticsearch)
# ============================================================
FRONTEND_IP="10.0.0.10"
ES_PORT="9200"
KIBANA_PORT="5601"

# ============================================================
# ELASTICSEARCH HOST (for ElastiFlow collectors)
# Usually same as FRONTEND_IP
# ============================================================
ELASTICSEARCH_HOST="10.0.0.10:9200"

# ============================================================
# ELASTIFLOW COLLECTOR 1 (Primary - NetFlow)
# IMPORTANT: This collector manages ES index templates
# ============================================================
ELASTIFLOW_1_NAME="netflow-collector"
ELASTIFLOW_1_IP="10.0.0.20"
ELASTIFLOW_1_PORTS="2050"
ELASTIFLOW_1_NETFLOW="true"
ELASTIFLOW_1_SFLOW="false"
ELASTIFLOW_1_TEMPLATE_MANAGER="true"

# ============================================================
# ELASTIFLOW COLLECTOR 2 (Secondary - sFlow)
# IMPORTANT: TEMPLATE_MANAGER must be "false" to avoid conflict
# ============================================================
ELASTIFLOW_2_NAME="sflow-collector"
ELASTIFLOW_2_IP="10.0.0.30"
ELASTIFLOW_2_PORTS="2050,6343"
ELASTIFLOW_2_NETFLOW="true"
ELASTIFLOW_2_SFLOW="true"
ELASTIFLOW_2_TEMPLATE_MANAGER="false"

# ============================================================
# ADDITIONAL COLLECTORS (Optional)
# Copy the pattern above for more collectors
# ============================================================

# ============================================================
# DASHBOARDS
# ============================================================
DASHBOARD_FILE="$SCRIPT_DIR/configs/elastiflow/dashboards/unified-flow-dashboards.ndjson"
ILM_POLICY_FILE="$SCRIPT_DIR/configs/elastiflow/ilm-policy.json"
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
        "FRONTEND_IP" "ELASTICSEARCH_HOST"
    )
    
    for var in "${required_vars[@]}"; do
        if [ -z "${!var}" ]; then
            log_error "Missing required config variable: $var"
            exit 1
        fi
    done
    
    # Generate Kibana keys if not set
    if [ -z "$KIBANA_ENCRYPTION_KEY" ]; then
        KIBANA_ENCRYPTION_KEY=$(openssl rand -hex 32)
        KIBANA_SECURITY_KEY=$(openssl rand -hex 32)
        KIBANA_REPORTING_KEY=$(openssl rand -hex 32)
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
    command -v docker-compose &> /dev/null || missing+=("docker-compose")
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
    
    # Generate CA
    openssl req -x509 -new -nodes -sha256 -days 3650 \
        -subj "/CN=elasticsearch-ca" \
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
keyUsage = keyEncipherment, dataEncipherment
extendedKeyUsage = serverAuth, clientAuth
subjectAltName = @alt_names

[alt_names]
DNS.1 = localhost
DNS.2 = *.flow-monitoring.local
DNS.3 = elasticsearch
DNS.4 = kibana
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
    docker-compose -f docker-compose-frontend.yml down 2>/dev/null || true
    docker-compose -f docker-compose-frontend.yml up -d
    
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
        docker-compose -f docker-compose-frontend.yml logs es-frontend 2>/dev/null | tail -20
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
        docker-compose -f docker-compose-frontend.yml logs kibana 2>/dev/null | tail -20
        exit 1
    fi
    
    log_success "Frontend deployment complete"
}

create_unicast_hosts() {
    local unicast_file="$SCRIPT_DIR/unicast_hosts.txt"
    
    # Frontend nodes
    echo "$FRONTEND_IP:9300" > "$unicast_file"
    echo "$FRONTEND_IP:9301" >> "$unicast_file"
    
    # ElastiFlow collector nodes (if they run ES data nodes)
    local num=1
    while [ -n "$(eval echo "\${ELASTIFLOW_${num}_IP:-}")" ]; do
        local ip=$(eval echo "\${ELASTIFLOW_${num}_IP}")
        echo "$ip:9300" >> "$unicast_file"
        ((num++))
    done
    
    log_info "Created unicast_hosts.txt with $(wc -l < "$unicast_file") entries"
}

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
ES_PORT=$ES_PORT
KIBANA_PORT=$KIBANA_PORT
ELASTICSEARCH_HOST=$ELASTICSEARCH_HOST
EOF
    log_info "Created .env file"
}

# ============================================================
# ELASTIFLOW COLLECTOR DEPLOYMENT
# ============================================================

deploy_elastiflow() {
    local num=$1
    
    if [ -z "$num" ]; then
        # Deploy all collectors
        local i=1
        while [ -n "$(eval echo "\${ELASTIFLOW_${i}_IP:-}")" ]; do
            deploy_elastiflow_collector $i
            ((i++))
        done
        return
    fi
    
    deploy_elastiflow_collector $num
}

deploy_elastiflow_collector() {
    local num=$1
    local name=$(eval echo "\${ELASTIFLOW_${num}_NAME:-collector-$num}")
    local ip=$(eval echo "\${ELASTIFLOW_${num}_IP}")
    local ports=$(eval echo "\${ELASTIFLOW_${num}_PORTS:-2050}")
    local netflow=$(eval echo "\${ELASTIFLOW_${num}_NETFLOW:-true}")
    local sflow=$(eval echo "\${ELASTIFLOW_${num}_SFLOW:-false}")
    local template_mgr=$(eval echo "\${ELASTIFLOW_${num}_TEMPLATE_MANAGER:-false}")
    
    log_info "=========================================="
    log_info "DEPLOYING ELASTIFLOW: $name ($ip)"
    log_info "=========================================="
    
    if [ -z "$ip" ]; then
        log_error "No IP configured for ElastiFlow collector $num"
        return 1
    fi
    
    local current_ip=$(hostname -I | awk '{print $1}')
    if [ "$current_ip" != "$ip" ]; then
        log_warn "Current IP ($current_ip) doesn't match $name ($ip)"
        log_info "Deploy manually on $ip:"
        echo ""
        echo "  ssh root@$ip"
        echo "  cd /opt/elastiflow"
        echo "  # Copy configs/elastiflow/docker-compose-n*.yml"
        echo "  # Create .env with ELASTICSEARCH_HOST and ELASTIC_PASSWORD"
        echo "  docker compose up -d"
        echo ""
        return 0
    fi
    
    # Choose compose file based on template manager setting
    local compose_file="$SCRIPT_DIR/configs/elastiflow/docker-compose-n2.yml"
    if [ "$template_mgr" = "true" ]; then
        compose_file="$SCRIPT_DIR/configs/elastiflow/docker-compose-n1.yml"
    fi
    
    # Create .env for collector
    cat > "$SCRIPT_DIR/.env.collector" << EOF
ELASTICSEARCH_HOST=$ELASTICSEARCH_HOST
ELASTIC_PASSWORD=$ELASTIC_PASSWORD
EOF
    
    log_info "Starting ElastiFlow collector..."
    cd "$SCRIPT_DIR"
    docker-compose -f "$compose_file" --env-file .env.collector down 2>/dev/null || true
    docker-compose -f "$compose_file" --env-file .env.collector up -d
    
    log_info "Waiting for collector to start..."
    sleep 10
    
    if docker ps --format '{{.Names}}' | grep -q "flow-collector"; then
        log_success "ElastiFlow collector $name is running"
        log_info "Ports: $ports"
    else
        log_error "ElastiFlow collector failed to start"
        docker logs flow-collector --tail 20 2>/dev/null || true
        return 1
    fi
    
    # Verify health
    sleep 5
    if curl -s "http://localhost:8080/health" | grep -q "healthy"; then
        log_success "Collector health check passed"
    else
        log_warn "Collector health check failed - check logs"
    fi
}

# ============================================================
# KIBANA SETUP
# ============================================================

import_dashboards() {
    log_info "=========================================="
    log_info "IMPORTING KIBANA DASHBOARDS"
    log_info "=========================================="
    
    if [ ! -f "$DASHBOARD_FILE" ]; then
        log_error "Dashboard file not found: $DASHBOARD_FILE"
        return 1
    fi
    
    log_info "Importing: $(basename "$DASHBOARD_FILE")"
    
    local result=$(curl -s -k \
        -X POST "http://$FRONTEND_IP:$KIBANA_PORT/api/saved_objects/_import?overwrite=true" \
        -u "elastic:$ELASTIC_PASSWORD" \
        -H "kbn-xsrf: true" \
        --form file=@"$DASHBOARD_FILE" 2>/dev/null)
    
    if echo "$result" | grep -q "success.*true"; then
        local count=$(echo "$result" | grep -o '"successCount":[0-9]*' | cut -d: -f2)
        log_success "Dashboards imported ($count objects)"
    else
        log_warn "Dashboard import may have issues"
        echo "$result" | head -5
    fi
}

apply_ilm_policy() {
    log_info "=========================================="
    log_info "APPLYING ILM POLICY"
    log_info "=========================================="
    
    if [ ! -f "$ILM_POLICY_FILE" ]; then
        log_warn "ILM policy file not found: $ILM_POLICY_FILE"
        return 0
    fi
    
    log_info "Applying ILM policy..."
    curl -s -k -X PUT "https://$FRONTEND_IP:$ES_PORT/_ilm/policy/elastiflow" \
        -u "elastic:$ELASTIC_PASSWORD" \
        -H "Content-Type: application/json" \
        -d @"$ILM_POLICY_FILE" | grep -q "acknowledged" && \
        log_success "ILM policy applied" || \
        log_warn "ILM policy may already exist"
}

# ============================================================
# VERIFICATION
# ============================================================

verify_deployment() {
    log_info "=========================================="
    log_info "VERIFICATION"
    log_info "=========================================="
    
    # Check Elasticsearch
    log_info "Checking Elasticsearch cluster..."
    local health=$(curl -s -k "https://$FRONTEND_IP:$ES_PORT/_cluster/health" \
        -u "elastic:$ELASTIC_PASSWORD" 2>/dev/null)
    
    local status=$(echo "$health" | grep -o '"status":"[^"]*"' | cut -d'"' -f4)
    local nodes=$(echo "$health" | grep -o '"number_of_nodes":[0-9]*' | cut -d: -f2)
    
    if [ "$status" = "green" ]; then
        log_success "Cluster status: GREEN ($nodes nodes)"
    elif [ "$status" = "yellow" ]; then
        log_warn "Cluster status: YELLOW ($nodes nodes)"
    else
        log_error "Cluster status: $status"
    fi
    
    # Check Kibana
    log_info "Checking Kibana..."
    if curl -s "http://$FRONTEND_IP:$KIBANA_PORT/api/status" 2>/dev/null | grep -q "available"; then
        log_success "Kibana is available"
    else
        log_error "Kibana is not available"
    fi
    
    # Check indices
    log_info "Checking flow indices..."
    local indices=$(curl -s -k "https://$FRONTEND_IP:$ES_PORT/_cat/indices/elastiflow-*" \
        -u "elastic:$ELASTIC_PASSWORD" 2>/dev/null | wc -l)
    if [ "$indices" -gt 0 ]; then
        log_success "Found $indices elastiflow indices"
    else
        log_warn "No elastiflow indices yet (will be created when data arrives)"
    fi
    
    # Summary
    echo ""
    log_info "=========================================="
    log_info "ACCESS INFORMATION"
    log_info "=========================================="
    echo "Kibana:      http://$FRONTEND_IP:$KIBANA_PORT"
    echo "Elasticsearch: https://$FRONTEND_IP:$ES_PORT"
    echo "Username:    elastic"
    echo "Password:    [from deploy.conf]"
    echo ""
}

# ============================================================
# HELP
# ============================================================

show_help() {
    cat << EOF
ELK Stack with ElastiFlow Deployment Script

Usage: $0 [OPTIONS]

Options:
    -h, --help      Show this help
    -g, --generate  Generate example deploy.conf
    -c, --check     Check prerequisites only
    -f, --frontend  Deploy frontend (ES + Kibana)
    -e, --elastiflow Deploy ElastiFlow collectors
    -i, --import    Import Kibana dashboards
    -v, --verify    Verify deployment

Configuration:
    Edit deploy.conf before deployment.

Architecture:
    Frontend Server:
        - Elasticsearch (master, data, ingest)
        - Kibana

    ElastiFlow Collectors (deploy on separate servers):
        - Collector N1 (Primary): Manages ES index templates
        - Collector N2+ (Secondary): Template management disabled

Network Ports:
    Frontend:
        - 9200: Elasticsearch HTTP
        - 9300-9301: Elasticsearch transport
        - 5601: Kibana

    ElastiFlow:
        - 2050/udp: NetFlow
        - 6343/udp: sFlow

Examples:
    $0 --generate           # Create deploy.conf
    $0 --check              # Check prerequisites
    $0 --frontend           # Deploy ES + Kibana
    $0 --elastiflow         # Deploy ElastiFlow collectors
    $0 --import             # Import dashboards
    $0                      # Full deployment

EOF
}

# ============================================================
# MAIN
# ============================================================

main() {
    local mode="full"
    
    while [[ $# -gt 0 ]]; do
        case $1 in
            -h|--help) show_help; exit 0 ;;
            -g|--generate) create_example_config; exit 0 ;;
            -c|--check) mode="check"; shift ;;
            -f|--frontend) mode="frontend"; shift ;;
            -e|--elastiflow) mode="elastiflow"; shift ;;
            -i|--import) mode="import"; shift ;;
            -v|--verify) mode="verify"; shift ;;
            *) shift ;;
        esac
    done
    
    echo ""
    echo "╔══════════════════════════════════════════════════════════╗"
    echo "║    ELK Stack with ElastiFlow Deployment                  ║"
    echo "╚══════════════════════════════════════════════════════════╝"
    echo ""
    
    case $mode in
        check)
            check_prerequisites
            ;;
        frontend)
            check_prerequisites
            load_config
            deploy_frontend
            import_dashboards
            apply_ilm_policy
            verify_deployment
            ;;
        elastiflow)
            check_prerequisites
            load_config
            deploy_elastiflow
            ;;
        import)
            load_config
            import_dashboards
            apply_ilm_policy
            ;;
        verify)
            load_config
            verify_deployment
            ;;
        full)
            check_prerequisites
            load_config
            deploy_frontend
            import_dashboards
            apply_ilm_policy
            deploy_elastiflow
            verify_deployment
            ;;
    esac
    
    echo ""
    log_success "Done!"
}

main "$@"
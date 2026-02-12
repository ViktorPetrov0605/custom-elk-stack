#!/bin/bash
#
# ELK Stack Unified Deployment Script
# Deploys frontend + multiple backend servers for NetFlow/sFlow monitoring
#
# Usage: ./deploy.sh [config-file]
# Default config: ./deploy.conf

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Logging functions
log_info() { echo -e "${BLUE}[INFO]${NC} $1"; }
log_success() { echo -e "${GREEN}[OK]${NC}   $1"; }
log_warn() { echo -e "${YELLOW}[WARN]${NC}  $1"; }
log_error() { echo -e "${RED}[ERROR]${NC} $1"; }

# Default configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONFIG_FILE="${1:-$SCRIPT_DIR/deploy.conf}"
COMPOSE_FRONTEND="$SCRIPT_DIR/docker-compose-frontend.yml"
COMPOSE_BACKEND="$SCRIPT_DIR/docker-compose-backend-universal.yml"

# ============================================================
# PRE-FLIGHT CHECKS
# ============================================================

check_prerequisites() {
    log_info "Checking prerequisites..."
    
    # Check Docker
    if ! command -v docker &> /dev/null; then
        log_error "Docker not installed. Install with: sudo apt-get install docker.io"
        exit 1
    fi
    
    # Check Docker Compose
    if ! command -v docker-compose &> /dev/null; then
        log_error "Docker Compose not installed. Install with: sudo apt-get install docker-compose"
        exit 1
    fi
    
    # Check if user in docker group
    if ! groups | grep -q docker; then
        log_warn "User not in docker group. Run: sudo usermod -aG docker $USER"
        log_warn "Then log out and back in, or run: newgrp docker"
    fi
    
    # Check if we can run docker commands
    if ! docker ps &> /dev/null; then
        log_error "Cannot run docker commands. Check permissions or start docker service."
        exit 1
    fi
    
    log_success "Prerequisites OK"
}

check_config_file() {
    log_info "Loading configuration from: $CONFIG_FILE"
    
    if [ ! -f "$CONFIG_FILE" ]; then
        log_error "Config file not found: $CONFIG_FILE"
        log_info "Creating example config file..."
        create_example_config
        exit 1
    fi
    
    # Source the config file
    source "$CONFIG_FILE"
    
    # Validate required variables
    local required_vars=(
        "CLUSTER_NAME" "STACK_VERSION" "LICENSE" "MEM_LIMIT"
        "ELASTIC_PASSWORD" "KIBANA_PASSWORD" "KIBANA_ENCRYPTION_KEY"
        "FRONTEND_IP" "ES_PORT" "KIBANA_PORT"
    )
    
    for var in "${required_vars[@]}"; do
        if [ -z "${!var}" ]; then
            log_error "Missing required config variable: $var"
            exit 1
        fi
    done
    
    log_success "Configuration loaded"
}

create_example_config() {
    cat > "$CONFIG_FILE" << 'EOF'
# ELK Stack Deployment Configuration
# Copy this file and customize for your environment

# ============================================================
# CLUSTER SETTINGS
# ============================================================
CLUSTER_NAME="custom-elk-cluster"
STACK_VERSION="8.16.0"
LICENSE="basic"
MEM_LIMIT="6g"

# ============================================================
# SECURITY SETTINGS
# ============================================================
ELASTIC_PASSWORD="your-secure-password-here"
KIBANA_PASSWORD="your-kibana-password-here"

# Encryption keys (generate with: openssl rand -hex 32)
KIBANA_ENCRYPTION_KEY="generate-me-with-openssl-rand-hex-32"
KIBANA_SECURITY_KEY="generate-me-with-openssl-rand-hex-32"
KIBANA_REPORTING_KEY="generate-me-with-openssl-rand-hex-32"

# ============================================================
# FRONTEND SERVER (Kibana + ES Masters)
# ============================================================
FRONTEND_IP="10.4.4.87"
ES_PORT="9200"
KIBANA_PORT="5601"

# ============================================================
# BACKEND SERVERS (Data nodes with Logstash)
# Define as many backends as needed
# Format: BACKEND_N_NAME, BACKEND_N_IP, BACKEND_N_TYPE
# Types: netflow, sflow, or universal (both)
# ============================================================

# Backend 1 - NetFlow collector
BACKEND_1_NAME="netflow-collector"
BACKEND_1_IP="10.4.4.21"
BACKEND_1_TYPE="netflow"
BACKEND_1_NETFLOW_PORT="2050"

# Backend 2 - sFlow collector
BACKEND_2_NAME="sflow-collector"
BACKEND_2_IP="10.4.4.90"
BACKEND_2_TYPE="sflow"
BACKEND_2_SFLOW_PORT="6343"

# Backend 3 - Universal (both) - example
# BACKEND_3_NAME="universal-collector"
# BACKEND_3_IP="10.4.4.91"
# BACKEND_3_TYPE="universal"
# BACKEND_3_NETFLOW_PORT="2050"
# BACKEND_3_SFLOW_PORT="6343"

# ============================================================
# DASHBOARD SETTINGS
# ============================================================
DASHBOARD_FILE="$SCRIPT_DIR/kibana-dashboards-enhanced/unified-flow-dashboards-v2.ndjson"
INDEX_PATTERN="unified-flow-*"

# ============================================================
# NETWORK DEVICE SETTINGS
# ============================================================
JUNIPER_IP="192.168.224.1"
JUNIPER_TARGET_BACKEND="10.4.4.21"
JUNIPER_NETFLOW_PORT="2050"

NEXUS_1_IP="10.4.4.3"
NEXUS_2_IP="10.4.4.4"
NEXUS_TARGET_BACKEND="10.4.4.90"
NEXUS_SFLOW_PORT="6343"
EOF
    
    log_info "Example config created at: $CONFIG_FILE"
    log_info "Please edit it with your actual settings before running deploy.sh"
}

# ============================================================
# CERTIFICATE MANAGEMENT
# ============================================================

generate_certificates() {
    log_info "Checking certificates..."
    
    local certs_dir="$SCRIPT_DIR/certs"
    
    if [ -f "$certs_dir/ca/ca.crt" ] && [ -f "$certs_dir/wildcard/wildcard.crt" ]; then
        log_success "Certificates already exist"
        return 0
    fi
    
    log_info "Generating certificates..."
    
    mkdir -p "$certs_dir"
    
    # Generate CA
    if [ ! -f "$certs_dir/ca/ca.crt" ]; then
        log_info "Generating Certificate Authority..."
        mkdir -p "$certs_dir/ca"
        openssl req -x509 -new -nodes -sha256 -days 3650 \
            -subj "/CN=elasticsearch-ca" \
            -keyout "$certs_dir/ca/ca.key" \
            -out "$certs_dir/ca/ca.crt"
        log_success "CA certificate generated"
    fi
    
    # Generate wildcard certificate for all nodes
    if [ ! -f "$certs_dir/wildcard/wildcard.crt" ]; then
        log_info "Generating wildcard certificate..."
        mkdir -p "$certs_dir/wildcard"
        
        # Create config for SAN
        cat > "$certs_dir/wildcard.cnf" << EOF
[req]
distinguished_name = req_distinguished_name
x509_extensions = v3_req
prompt = no

[req_distinguished_name]
CN = *.custom-elk-stack.local

[v3_req]
keyUsage = keyEncipherment, dataEncipherment
extendedKeyUsage = serverAuth, clientAuth
subjectAltName = @alt_names

[alt_names]
DNS.1 = localhost
DNS.2 = *.custom-elk-stack.local
DNS.3 = elasticsearch
DNS.4 = es-frontend
DNS.5 = es-frontend-2
IP.1 = 127.0.0.1
IP.2 = $FRONTEND_IP
EOF
        
        # Add backend IPs
        local backend_num=1
        while [ -n "$(eval echo "\${BACKEND_${backend_num}_IP:-}")" ]; do
            local backend_ip=$(eval echo "\${BACKEND_${backend_num}_IP}")
            echo "IP.$((backend_num + 2)) = $backend_ip" >> "$certs_dir/wildcard.cnf"
            ((backend_num++))
        done
        
        # Generate key and CSR
        openssl req -new -nodes -sha256 \
            -config "$certs_dir/wildcard.cnf" \
            -keyout "$certs_dir/wildcard/wildcard.key" \
            -out "$certs_dir/wildcard/wildcard.csr"
        
        # Sign with CA
        openssl x509 -req -sha256 -days 3650 \
            -in "$certs_dir/wildcard/wildcard.csr" \
            -CA "$certs_dir/ca/ca.crt" \
            -CAkey "$certs_dir/ca/ca.key" \
            -CAcreateserial \
            -extensions v3_req \
            -extfile "$certs_dir/wildcard.cnf" \
            -out "$certs_dir/wildcard/wildcard.crt"
        
        log_success "Wildcard certificate generated"
    fi
    
    # Set permissions
    chmod 600 "$certs_dir"/*.key 2>/dev/null || true
    chmod 755 "$certs_dir"
}

# ============================================================
# FRONTEND DEPLOYMENT
# ============================================================

create_unicast_hosts() {
    log_info "Creating unicast hosts configuration..."
    
    local unicast_file="$SCRIPT_DIR/unicast_hosts.txt"
    
    # Add frontend nodes
    echo "$FRONTEND_IP:9300" > "$unicast_file"
    echo "$FRONTEND_IP:9301" >> "$unicast_file"
    
    # Add all backend nodes
    local backend_num=1
    while [ -n "$(eval echo "\${BACKEND_${backend_num}_IP:-}")" ]; do
        local backend_ip=$(eval echo "\${BACKEND_${backend_num}_IP}")
        echo "$backend_ip:9300" >> "$unicast_file"
        ((backend_num++))
    done
    
    log_success "Unicast hosts file created with $(wc -l < "$unicast_file") entries"
}

deploy_frontend() {
    log_info "=========================================="
    log_info "DEPLOYING FRONTEND SERVER"
    log_info "=========================================="
    
    local current_ip=$(hostname -I | awk '{print $1}')
    
    if [ "$current_ip" != "$FRONTEND_IP" ]; then
        log_warn "Current IP ($current_ip) doesn't match configured FRONTEND_IP ($FRONTEND_IP)"
        log_warn "Make sure you're running this on the correct server"
        read -p "Continue anyway? (y/N): " confirm
        if [[ ! $confirm =~ ^[Yy]$ ]]; then
            exit 1
        fi
    fi
    
    create_unicast_hosts
    generate_certificates
    
    # Create .env file for docker-compose
    cat > "$SCRIPT_DIR/.env" << EOF
CLUSTER_NAME=$CLUSTER_NAME
STACK_VERSION=$STACK_VERSION
LICENSE=$LICENSE
MEM_LIMIT=$MEM_LIMIT
ELASTIC_PASSWORD=$ELASTIC_PASSWORD
KIBANA_PASSWORD=$KIBANA_PASSWORD
KIBANA_ENCRYPTION_KEY=$KIBANA_ENCRYPTION_KEY
KIBANA_SECURITY_KEY=$KIBANA_SECURITY_KEY
KIBANA_REPORTING_KEY=$KIBANA_REPORTING_KEY
FRONTEND_IP=$FRONTEND_IP
ES_PORT=$ES_PORT
KIBANA_PORT=$KIBANA_PORT
EOF
    
    log_info "Starting frontend services..."
    
    cd "$SCRIPT_DIR"
    docker-compose -f "$COMPOSE_FRONTEND" down 2>/dev/null || true
    docker-compose -f "$COMPOSE_FRONTEND" up -d
    
    log_info "Waiting for Elasticsearch to start..."
    local retries=30
    while [ $retries -gt 0 ]; do
        if curl -s -k "https://$FRONTEND_IP:$ES_PORT/_cluster/health" -u "elastic:$ELASTIC_PASSWORD" | grep -q "green\|yellow"; then
            log_success "Elasticsearch is up and running"
            break
        fi
        sleep 10
        ((retries--))
        echo -n "."
    done
    
    if [ $retries -eq 0 ]; then
        log_error "Elasticsearch failed to start. Check logs: docker-compose logs es-frontend"
        exit 1
    fi
    
    log_info "Waiting for Kibana to be ready..."
    retries=60
    while [ $retries -gt 0 ]; do
        if curl -s "http://$FRONTEND_IP:$KIBANA_PORT/api/status" | grep -q "available"; then
            log_success "Kibana is up and running at http://$FRONTEND_IP:$KIBANA_PORT"
            break
        fi
        sleep 5
        ((retries--))
        echo -n "."
    done
    
    if [ $retries -eq 0 ]; then
        log_error "Kibana failed to start. Check logs: docker-compose logs kibana"
        exit 1
    fi
    
    log_success "Frontend deployment complete"
}

# ============================================================
# BACKEND DEPLOYMENT
# ============================================================

deploy_backend() {
    local backend_num=$1
    local backend_name=$(eval echo "\${BACKEND_${backend_num}_NAME}")
    local backend_ip=$(eval echo "\${BACKEND_${backend_num}_IP}")
    local backend_type=$(eval echo "\${BACKEND_${backend_num}_TYPE}")
    
    log_info "=========================================="
    log_info "DEPLOYING BACKEND $backend_num: $backend_name ($backend_type)"
    log_info "=========================================="
    
    local current_ip=$(hostname -I | awk '{print $1}')
    
    if [ "$current_ip" != "$backend_ip" ]; then
        log_warn "Current IP ($current_ip) doesn't match configured BACKEND_${backend_num}_IP ($backend_ip)"
        log_warn "Skipping local deployment. Deploy manually on $backend_ip:"
        echo ""
        echo "  ssh $backend_ip"
        echo "  cd $SCRIPT_DIR"
        echo "  ./deploy.sh $CONFIG_FILE"
        echo ""
        return 0
    fi
    
    # Create backend-specific environment file
    cat > "$SCRIPT_DIR/.env.backend" << EOF
CLUSTER_NAME=$CLUSTER_NAME
STACK_VERSION=$STACK_VERSION
LICENSE=$LICENSE
MEM_LIMIT=$MEM_LIMIT
ELASTIC_PASSWORD=$ELASTIC_PASSWORD
FRONTEND_IP=$FRONTEND_IP
BACKEND_IP=$backend_ip
EOF
    
    log_info "Starting backend services on $backend_ip..."
    
    cd "$SCRIPT_DIR"
    docker-compose -f "$COMPOSE_BACKEND" down 2>/dev/null || true
    docker-compose -f "$COMPOSE_BACKEND" up -d
    
    log_info "Waiting for backend Elasticsearch to join cluster..."
    local retries=30
    while [ $retries -gt 0 ]; do
        local node_count=$(curl -s -k "https://$FRONTEND_IP:$ES_PORT/_cat/nodes" -u "elastic:$ELASTIC_PASSWORD" | wc -l)
        if [ "$node_count" -ge $((backend_num + 2)) ]; then
            log_success "Backend joined cluster (total nodes: $node_count)"
            break
        fi
        sleep 10
        ((retries--))
        echo -n "."
    done
    
    if [ $retries -eq 0 ]; then
        log_error "Backend failed to join cluster. Check logs: docker-compose logs es-remote"
        log_warn "Common fix: docker-compose -f $COMPOSE_BACKEND down -v && docker-compose up -d"
    fi
    
    # Check if Logstash is listening
    sleep 5
    if ss -lnup | grep -q "2050\|6343"; then
        log_success "Logstash is listening on flow ports"
    else
        log_warn "Logstash ports not yet open. May take another minute."
    fi
    
    log_success "Backend $backend_num ($backend_name) deployment complete"
}

deploy_all_backends() {
    log_info "Deploying backend servers..."
    
    local backend_num=1
    while [ -n "$(eval echo "\${BACKEND_${backend_num}_IP:-}")" ]; do
        deploy_backend $backend_num
        ((backend_num++))
    done
    
    local total_backends=$((backend_num - 1))
    log_success "All $total_backends backend(s) deployed"
}

# ============================================================
# POST-DEPLOYMENT SETUP
# ============================================================

apply_ilm_policy() {
    log_info "=========================================="
    log_info "APPLYING ILM POLICY"
    log_info "=========================================="
    
    local policy_file="$SCRIPT_DIR/config/ilm-policy-1-day.json"
    
    if [ ! -f "$policy_file" ]; then
        log_warn "ILM policy file not found: $policy_file"
        return 1
    fi
    
    log_info "Creating ILM policy: flow-data-1-day-retention"
    
    curl -s -k -X PUT "https://$FRONTEND_IP:$ES_PORT/_ilm/policy/flow-data-1-day-retention" \
        -u "elastic:$ELASTIC_PASSWORD" \
        -H "Content-Type: application/json" \
        -d "@$policy_file" | grep -q "acknowledged.*true" && \
        log_success "ILM policy applied" || \
        log_warn "ILM policy may already exist"
    
    # Apply index template with ILM
    local template_file="$SCRIPT_DIR/config/index-template-unified-flow.json"
    if [ -f "$template_file" ]; then
        log_info "Creating index template..."
        curl -s -k -X PUT "https://$FRONTEND_IP:$ES_PORT/_index_template/unified-flow-template" \
            -u "elastic:$ELASTIC_PASSWORD" \
            -H "Content-Type: application/json" \
            -d "@$template_file" | grep -q "acknowledged.*true" && \
            log_success "Index template applied" || \
            log_warn "Index template may already exist"
    fi
}

import_dashboards() {
    log_info "=========================================="
    log_info "IMPORTING KIBANA DASHBOARDS"
    log_info "=========================================="
    
    local dashboard_file="${DASHBOARD_FILE:-$SCRIPT_DIR/kibana-dashboards-enhanced/unified-flow-dashboards-v2.ndjson}"
    
    if [ ! -f "$dashboard_file" ]; then
        log_warn "Dashboard file not found: $dashboard_file"
        log_info "Available dashboard files:"
        ls -1 "$SCRIPT_DIR/kibana-dashboards-enhanced/"*.ndjson 2>/dev/null || true
        return 1
    fi
    
    log_info "Importing dashboards from: $(basename "$dashboard_file")"
    
    # Wait for Kibana to be ready
    sleep 5
    
    local result=$(curl -s -k "https://$FRONTEND_IP:$ES_PORT" -u "elastic:$ELASTIC_PASSWORD" -o /dev/null -w "%{http_code}")
    if [ "$result" != "200" ]; then
        log_error "Cannot connect to Elasticsearch. Dashboard import skipped."
        return 1
    fi
    
    # Import via Kibana API
    local import_result=$(curl -s -k \
        -X POST "http://$FRONTEND_IP:$KIBANA_PORT/api/saved_objects/_import?overwrite=true" \
        -u "elastic:$ELASTIC_PASSWORD" \
        -H "kbn-xsrf: true" \
        --form file=@"$dashboard_file")
    
    if echo "$import_result" | grep -q "success.*true"; then
        local success_count=$(echo "$import_result" | grep -o '"successCount":[0-9]*' | cut -d: -f2)
        log_success "Dashboards imported successfully ($success_count objects)"
    else
        log_warn "Dashboard import may have had issues. Check Kibana manually."
        log_info "You can manually import via: Stack Management > Saved Objects > Import"
    fi
}

create_index_pattern() {
    log_info "=========================================="
    log_info "CREATING INDEX PATTERN"
    log_info "=========================================="
    
    local pattern="${INDEX_PATTERN:-unified-flow-*}"
    
    log_info "Creating index pattern: $pattern"
    
    curl -s -k -X POST "http://$FRONTEND_IP:$KIBANA_PORT/api/saved_objects/index-pattern" \
        -u "elastic:$ELASTIC_PASSWORD" \
        -H "Content-Type: application/json" \
        -H "kbn-xsrf: true" \
        -d "{
            \"attributes\": {
                \"title\": \"$pattern\",
                \"timeFieldName\": \"@timestamp\"
            }
        }" | grep -q "id" && \
        log_success "Index pattern created" || \
        log_warn "Index pattern may already exist"
}

# ============================================================
# VERIFICATION
# ============================================================

check_cluster_nodes() {
    log_info "=========================================="
    log_info "CLUSTER NODE VERIFICATION"
    log_info "=========================================="
    
    log_info "Checking all nodes in the cluster..."
    echo ""
    
    # Fetch node information
    local nodes_output=$(curl -s -k "https://$FRONTEND_IP:$ES_PORT/_cat/nodes?v" -u "elastic:$ELASTIC_PASSWORD" 2>/dev/null)
    
    if [ -z "$nodes_output" ]; then
        log_error "Cannot retrieve cluster nodes. Is Elasticsearch running?"
        return 1
    fi
    
    # Display the node table
    echo "$nodes_output"
    echo ""
    
    # Count nodes
    local node_count=$(echo "$nodes_output" | tail -n +2 | wc -l)
    local expected_nodes=0
    
    # Count expected nodes (2 frontend + backends)
    expected_nodes=2
    local backend_num=1
    while [ -n "$(eval echo "\${BACKEND_${backend_num}_IP:-}")" ]; do
        ((expected_nodes++))
        ((backend_num++))
    done
    
    log_info "Detected $node_count node(s) in cluster (expected: $expected_nodes)"
    
    # Check for master node
    if echo "$nodes_output" | grep -q "\*"; then
        log_success "Master node elected"
    else
        log_warn "No master node detected - cluster may be unstable"
    fi
    
    # Verify each expected backend is present
    backend_num=1
    while [ -n "$(eval echo "\${BACKEND_${backend_num}_IP:-}")" ]; do
        local backend_ip=$(eval echo "\${BACKEND_${backend_num}_IP}")
        if echo "$nodes_output" | grep -q "$backend_ip"; then
            log_success "Backend $backend_num ($backend_ip) connected"
        else
            log_error "Backend $backend_num ($backend_ip) NOT in cluster!"
            log_info "Troubleshooting: Check backend logs with: docker-compose -f $COMPOSE_BACKEND logs es-remote"
        fi
        ((backend_num++))
    done
    
    echo ""
    log_info "Node roles key: d=data, i=ingest, m=master, * = current master"
    echo ""
    
    return 0
}

verify_deployment() {
    log_info "=========================================="
    log_info "VERIFICATION"
    log_info "=========================================="
    
    local all_ok=true
    
    # Check cluster nodes first (detailed view)
    check_cluster_nodes
    
    # Check cluster health
    log_info "Checking cluster health..."
    local health=$(curl -s -k "https://$FRONTEND_IP:$ES_PORT/_cluster/health" -u "elastic:$ELASTIC_PASSWORD")
    local status=$(echo "$health" | grep -o '"status":"[^"]*"' | cut -d'"' -f4)
    local nodes=$(echo "$health" | grep -o '"number_of_nodes":[0-9]*' | cut -d: -f2)
    
    if [ "$status" == "green" ]; then
        log_success "Cluster status: GREEN ($nodes nodes)"
    elif [ "$status" == "yellow" ]; then
        log_warn "Cluster status: YELLOW ($nodes nodes) - may have unassigned shards"
    else
        log_error "Cluster status: $status ($nodes nodes)"
        all_ok=false
    fi
    
    # Check indices
    log_info "Checking indices..."
    local indices=$(curl -s -k "https://$FRONTEND_IP:$ES_PORT/_cat/indices" -u "elastic:$ELASTIC_PASSWORD" | grep -c "unified-flow" || echo "0")
    if [ "$indices" -gt 0 ]; then
        log_success "Found $indices unified-flow index(es)"
    else
        log_warn "No unified-flow indices yet (will be created when data arrives)"
    fi
    
    # Check Logstash ports on backends
    log_info "Checking flow collection ports..."
    local backend_num=1
    while [ -n "$(eval echo "\${BACKEND_${backend_num}_IP:-}")" ]; do
        local backend_ip=$(eval echo "\${BACKEND_${backend_num}_IP}")
        local backend_type=$(eval echo "\${BACKEND_${backend_num}_TYPE}")
        
        # Note: This only works if running locally on the backend
        if command -v ss &> /dev/null && [ "$backend_ip" == "$(hostname -I | awk '{print $1}')" ]; then
            if ss -lnup 2>/dev/null | grep -q "2050\|6343"; then
                log_success "Backend $backend_num: Logstash listening on flow ports"
            fi
        fi
        ((backend_num++))
    done
    
    # Print summary
    echo ""
    log_info "=========================================="
    log_info "DEPLOYMENT SUMMARY"
    log_info "=========================================="
    echo "Frontend: http://$FRONTEND_IP:$KIBANA_PORT"
    echo "Credentials: elastic / [configured password]"
    echo "Elasticsearch: https://$FRONTEND_IP:$ES_PORT"
    echo ""
    echo "Backend nodes:"
    curl -s -k "https://$FRONTEND_IP:$ES_PORT/_cat/nodes?v" -u "elastic:$ELASTIC_PASSWORD" 2>/dev/null || echo "  (unable to retrieve)"
    echo ""
    
    if [ "$all_ok" = true ]; then
        log_success "Deployment verification passed!"
    else
        log_warn "Some checks failed. Review logs above."
    fi
    
    return 0
}

generate_summary() {
    local output_file="${1:-$SCRIPT_DIR/DEPLOYMENT_SUMMARY.txt}"
    
    cat > "$output_file" << EOF
ELK Stack Deployment Summary
Generated: $(date)
================================

CONFIGURATION
-------------
Cluster Name: $CLUSTER_NAME
Stack Version: $STACK_VERSION
Frontend: http://$FRONTEND_IP:$KIBANA_PORT
Elasticsearch: https://$FRONTEND_IP:$ES_PORT

BACKENDS
--------
EOF
    
    local backend_num=1
    while [ -n "$(eval echo "\${BACKEND_${backend_num}_IP:-}")" ]; do
        local name=$(eval echo "\${BACKEND_${backend_num}_NAME}")
        local ip=$(eval echo "\${BACKEND_${backend_num}_IP}")
        local type=$(eval echo "\${BACKEND_${backend_num}_TYPE}")
        
        echo "Backend $backend_num:" >> "$output_file"
        echo "  Name: $name" >> "$output_file"
        echo "  IP: $ip" >> "$output_file"
        echo "  Type: $type" >> "$output_file"
        echo "" >> "$output_file"
        
        ((backend_num++))
    done
    
    cat >> "$output_file" << EOF

ACCESS INFORMATION
------------------
Kibana URL: http://$FRONTEND_IP:$KIBANA_PORT
Username: elastic
Password: [configured in deploy.conf]

POST-DEPLOYMENT COMMANDS
------------------------
# Check cluster health
curl -k -u elastic:$ELASTIC_PASSWORD https://$FRONTEND_IP:$ES_PORT/_cluster/health

# Check nodes
curl -k -u elastic:$ELASTIC_PASSWORD https://$FRONTEND_IP:$ES_PORT/_cat/nodes

# Check indices
curl -k -u elastic:$ELASTIC_PASSWORD https://$FRONTEND_IP:$ES_PORT/_cat/indices

# View cluster logs
docker-compose -f $COMPOSE_FRONTEND logs -f

# View backend logs (on backend server)
docker-compose -f $COMPOSE_BACKEND logs -f

FILES
-----
Config: $CONFIG_FILE
Frontend Compose: $COMPOSE_FRONTEND
Backend Compose: $COMPOSE_BACKEND
Certificates: $SCRIPT_DIR/certs/
Dashboards: $SCRIPT_DIR/kibana-dashboards-enhanced/
EOF
    
    log_success "Deployment summary saved to: $output_file"
}

# ============================================================
# CLEANUP
# ============================================================

cleanup_secrets() {
    # Remove temporary .env files that contain secrets
    rm -f "$SCRIPT_DIR/.env" "$SCRIPT_DIR/.env.backend"
    
    # Secure certificate files
    chmod 600 "$SCRIPT_DIR/certs"/*.key 2>/dev/null || true
    chmod 700 "$SCRIPT_DIR/certs"
}

# ============================================================
# USAGE & HELP
# ============================================================

show_help() {
    cat << EOF
ELK Stack Unified Deployment Script

Usage: $0 [OPTIONS] [config-file]

Options:
    -h, --help          Show this help message
    -c, --check         Run pre-flight checks only
    -f, --frontend      Deploy frontend only
    -b, --backends      Deploy backends only (local)
    -p, --post-deploy   Run post-deployment setup only
    -v, --verify        Verify deployment only
    -s, --cleanup       Cleanup and reset (dangerous!)
    -g, --generate      Generate example config file

Default config file: ./deploy.conf

Examples:
    $0                          # Full deployment with default config
    $0 /path/to/config.conf     # Full deployment with custom config
    $0 -f                       # Deploy frontend only
    $0 -b                       # Deploy local backend only
    $0 -p                       # Apply ILM policy, import dashboards
    $0 -v                       # Verify deployment health
    $0 -g                       # Generate example config

Deployment Steps:
    1. Checks prerequisites (Docker, Docker Compose)
    2. Generates certificates if needed
    3. Deploys frontend (Kibana + ES masters)
    4. Deploys backends (ES data + Logstash)
    5. Applies ILM policy for data retention
    6. Imports Kibana dashboards
    7. Verifies deployment

Network Flow Architecture:
    - Frontend: Kibana UI + Elasticsearch (master role)
    - Backends: Elasticsearch (data role) + Logstash collectors
    - Each backend can collect NetFlow (UDP 2050) and/or sFlow (UDP 6343)

For multiple backends, deploy this script on each backend server
after the frontend is running. The backends will auto-join the cluster.

EOF
}

# ============================================================
# MAIN
# ============================================================

main() {
    # Parse arguments
    local mode="full"
    local custom_config=""
    
    while [[ $# -gt 0 ]]; do
        case $1 in
            -h|--help)
                show_help
                exit 0
                ;;
            -c|--check)
                mode="check"
                shift
                ;;
            -f|--frontend)
                mode="frontend"
                shift
                ;;
            -b|--backends)
                mode="backends"
                shift
                ;;
            -p|--post-deploy)
                mode="post-deploy"
                shift
                ;;
            -v|--verify)
                mode="verify"
                shift
                ;;
            -s|--cleanup)
                mode="cleanup"
                shift
                ;;
            -g|--generate)
                create_example_config
                exit 0
                ;;
            -*)
                log_error "Unknown option: $1"
                show_help
                exit 1
                ;;
            *)
                custom_config="$1"
                shift
                ;;
        esac
    done
    
    # Set config file
    if [ -n "$custom_config" ]; then
        CONFIG_FILE="$custom_config"
    fi
    
    # Print banner
    echo ""
    echo "╔══════════════════════════════════════════════════════════╗"
    echo "║       ELK Stack Unified Deployment Script                ║"
    echo "║       NetFlow & sFlow Monitoring System                  ║"
    echo "╚══════════════════════════════════════════════════════════╝"
    echo ""
    
    # Execute based on mode
    case $mode in
        check)
            check_prerequisites
            check_config_file
            log_success "All checks passed!"
            ;;
            
        frontend)
            check_prerequisites
            check_config_file
            deploy_frontend
            apply_ilm_policy
            create_index_pattern
            import_dashboards
            verify_deployment
            generate_summary
            cleanup_secrets
            ;;
            
        backends)
            check_prerequisites
            check_config_file
            deploy_all_backends
            verify_deployment
            cleanup_secrets
            ;;
            
        post-deploy)
            check_prerequisites
            check_config_file
            apply_ilm_policy
            create_index_pattern
            import_dashboards
            verify_deployment
            ;;
            
        verify)
            check_config_file
            verify_deployment
            ;;
            
        cleanup)
            read -p "WARNING: This will remove ALL containers and data. Continue? (y/N): " confirm
            if [[ $confirm =~ ^[Yy]$ ]]; then
                cd "$SCRIPT_DIR"
                docker-compose -f "$COMPOSE_FRONTEND" down -v 2>/dev/null || true
                docker-compose -f "$COMPOSE_BACKEND" down -v 2>/dev/null || true
                rm -rf "$SCRIPT_DIR/data" 2>/dev/null || true
                log_success "Cleanup complete"
            fi
            ;;
            
        full)
            check_prerequisites
            check_config_file
            deploy_frontend
            deploy_all_backends
            apply_ilm_policy
            create_index_pattern
            import_dashboards
            verify_deployment
            generate_summary
            cleanup_secrets
            ;;
    esac
    
    echo ""
    log_success "Script completed!"
    echo ""
}

# Run main function
main "$@"

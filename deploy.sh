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
    log_info "=========================================="
    log_info "DEPLOYING BACKEND (ES Remote + Logstash)"
    log_info "=========================================="
    
    local current_ip=$(hostname -I | awk '{print $1}')
    
    # Check if we're on a backend server
    local is_backend=false
    IFS=',' read -ra BACKEND_IPS <<< "$BACKEND_IP"
    for ip in "${BACKEND_IPS[@]}"; do
        ip=$(echo "$ip" | xargs)
        if [ "$current_ip" = "$ip" ]; then
            is_backend=true
            break
        fi
    done
    
    if [ "$is_backend" = false ]; then
        log_warn "Current IP ($current_ip) is not in BACKEND_IP list"
        log_info "Deploy manually on backend servers:"
        echo ""
        IFS=',' read -ra BACKEND_IPS <<< "$BACKEND_IP"
        for ip in "${BACKEND_IPS[@]}"; do
            ip=$(echo "$ip" | xargs)
            echo "  ssh root@$ip"
            echo "  cd /path/to/custom-elk-stack"
            echo "  ./deploy.sh --backend"
            echo ""
        done
        return 0
    fi
    
    # Deploy on this backend server
    if [ ! -f "$SCRIPT_DIR/certs/ca/ca.crt" ]; then
        log_error "Certificates not found. Copy certs/ from frontend server:"
        echo "  scp -r root@$FRONTEND_IP:/path/to/custom-elk-stack/certs ./"
        exit 1
    fi
    
    create_env_file
    
    log_info "Starting ES remote node and Logstash..."
    cd "$SCRIPT_DIR"
    $DC -f docker-compose-backend.yml down 2>/dev/null || true
    $DC -f docker-compose-backend.yml up -d
    
    log_info "Waiting for ES remote node..."
    local retries=30
    while [ $retries -gt 0 ]; do
        if curl -s -k "https://localhost:9200/_cluster/health" \
            -u "elastic:$ELASTIC_PASSWORD" 2>/dev/null | grep -q "green\|yellow"; then
            log_success "ES remote node is up"
            break
        fi
        sleep 10
        ((retries--))
        echo -n "."
    done
    
    if [ $retries -eq 0 ]; then
        log_error "ES remote node failed to start"
        $DC -f docker-compose-backend.yml logs es-remote 2>/dev/null | tail -20
        exit 1
    fi
    
    # Check Logstash
    sleep 5
    if docker ps --format '{{.Names}}' | grep -q "logstash-flow"; then
        log_success "Logstash is running"
        
        # Verify Logstash is receiving data
        if curl -s "http://localhost:9600/_node/stats" 2>/dev/null | grep -q "logstash"; then
            log_success "Logstash API is responding"
        fi
    else
        log_error "Logstash failed to start"
        docker logs logstash-flow --tail 20 2>/dev/null || true
        exit 1
    fi
    
    log_success "Backend deployment complete on $current_ip"
}

# ============================================================
# KIBANA SETUP
# ============================================================

import_dashboards() {
    log_info "=========================================="
    log_info "IMPORTING KIBANA DASHBOARDS"
    log_info "=========================================="
    
    if [ ! -f "$DASHBOARD_FILE" ]; then
        log_warn "Dashboard file not found: $DASHBOARD_FILE"
        log_info "Skipping dashboard import"
        return 0
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
        log_info "Creating default ILM policy..."
        
        # Default 3-day retention policy
        curl -s -k -X PUT "https://$FRONTEND_IP:$ES_PORT/_ilm/policy/flow-data-3-day" \
            -u "elastic:$ELASTIC_PASSWORD" \
            -H "Content-Type: application/json" \
            -d '{
                "policy": {
                    "phases": {
                        "hot": {
                            "min_age": "0ms",
                            "actions": {
                                "rollover": {
                                    "max_age": "1d",
                                    "max_primary_shard_size": "50gb"
                                },
                                "set_priority": {"priority": 100}
                            }
                        },
                        "warm": {
                            "min_age": "1d",
                            "actions": {
                                "forcemerge": {"max_num_segments": 1},
                                "set_priority": {"priority": 50}
                            }
                        },
                        "delete": {
                            "min_age": "3d",
                            "actions": {"delete": {}}
                        }
                    }
                }
            }' | grep -q "acknowledged" && \
            log_success "ILM policy 'flow-data-3-day' created" || \
            log_warn "ILM policy may already exist"
    else
        log_info "Applying ILM policy from file..."
        curl -s -k -X PUT "https://$FRONTEND_IP:$ES_PORT/_ilm/policy/elastiflow" \
            -u "elastic:$ELASTIC_PASSWORD" \
            -H "Content-Type: application/json" \
            -d @"$ILM_POLICY_FILE" | grep -q "acknowledged" && \
            log_success "ILM policy applied" || \
            log_warn "ILM policy may already exist"
    fi
}

create_index_template() {
    log_info "=========================================="
    log_info "CREATING INDEX TEMPLATE"
    log_info "=========================================="
    
    log_info "Creating logstash-flow index template..."
    curl -s -k -X PUT "https://$FRONTEND_IP:$ES_PORT/_index_template/logstash-flow" \
        -u "elastic:$ELASTIC_PASSWORD" \
        -H "Content-Type: application/json" \
        -d '{
            "index_patterns": ["logstash-flow-*"],
            "template": {
                "settings": {
                    "index": {
                        "lifecycle": {"name": "flow-data-3-day", "rollover_alias": "logstash-flow"},
                        "number_of_shards": "2",
                        "number_of_replicas": "1"
                    }
                },
                "mappings": {
                    "dynamic_templates": [
                        {"strings_as_keywords": {"match_mapping_type": "string", "mapping": {"type": "keyword", "ignore_above": 1024}}},
                        {"ip_fields": {"match": "*ip", "mapping": {"type": "ip"}}}
                    ],
                    "properties": {
                        "@timestamp": {"type": "date"},
                        "source": {"properties": {"ip": {"type": "ip"}, "port": {"type": "integer"}, "bytes": {"type": "long"}, "packets": {"type": "long"}}},
                        "destination": {"properties": {"ip": {"type": "ip"}, "port": {"type": "integer"}, "bytes": {"type": "long"}, "packets": {"type": "long"}}},
                        "network": {"properties": {"bytes": {"type": "long"}, "packets": {"type": "long"}, "transport": {"type": "keyword"}, "protocol": {"type": "keyword"}}},
                        "host": {"properties": {"ip": {"type": "ip"}, "name": {"type": "keyword"}}}
                    }
                }
            }
        }' | grep -q "acknowledged" && \
        log_success "Index template created" || \
        log_warn "Index template may already exist"
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
    local indices=$(curl -s -k "https://$FRONTEND_IP:$ES_PORT/_cat/indices/logstash-flow-*" \
        -u "elastic:$ELASTIC_PASSWORD" 2>/dev/null | wc -l)
    if [ "$indices" -gt 0 ]; then
        log_success "Found $indices logstash-flow indices"
        
        # Show latest index
        local latest=$(curl -s -k "https://$FRONTEND_IP:$ES_PORT/_cat/indices/logstash-flow-*?h=index,docs.count,store.size&s=index:desc" \
            -u "elastic:$ELASTIC_PASSWORD" 2>/dev/null | head -1)
        log_info "Latest: $latest"
    else
        log_warn "No logstash-flow indices yet (will be created when data arrives)"
    fi
    
    # Summary
    echo ""
    log_info "=========================================="
    log_info "ACCESS INFORMATION"
    log_info "=========================================="
    echo "Kibana:       http://$FRONTEND_IP:$KIBANA_PORT"
    echo "Elasticsearch: https://$FRONTEND_IP:$ES_PORT"
    echo "Username:     elastic"
    echo "Password:     [from deploy.conf]"
    echo ""
}

# ============================================================
# HELP
# ============================================================

show_help() {
    cat << EOF
ELK Stack with Logstash Deployment Script

Usage: $0 [OPTIONS]

Options:
    -h, --help      Show this help
    -g, --generate  Generate example deploy.conf
    -c, --check     Check prerequisites only
    -f, --frontend  Deploy frontend (ES + Kibana)
    -b, --backend   Deploy backend (ES remote + Logstash)
    -i, --import    Import Kibana dashboards + ILM
    -v, --verify    Verify deployment

Configuration:
    Edit deploy.conf before deployment.

Architecture:
    Frontend Server (10.4.4.87):
        - Elasticsearch (master, data, ingest) x2
        - Kibana

    Backend Servers (10.4.4.21, 10.4.4.90):
        - Elasticsearch (data, ingest) - remote node
        - Logstash - flow collector

Network Ports:
    Frontend:
        - 9200: Elasticsearch HTTP
        - 9300-9301: Elasticsearch transport
        - 5601: Kibana

    Backend:
        - 9200: ES remote HTTP
        - 9300: ES remote transport
        - 2050/udp: NetFlow
        - 6343/udp: sFlow

Examples:
    $0 --generate           # Create deploy.conf
    $0 --check              # Check prerequisites
    $0 --frontend           # Deploy ES + Kibana on frontend
    $0 --backend            # Deploy ES + Logstash on backend
    $0 --import             # Import dashboards & ILM policies
    $0                      # Full deployment (frontend only)

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
            -b|--backend) mode="backend"; shift ;;
            -i|--import) mode="import"; shift ;;
            -v|--verify) mode="verify"; shift ;;
            *) shift ;;
        esac
    done
    
    echo ""
    echo "╔══════════════════════════════════════════════════════════╗"
    echo "║    ELK Stack with Logstash Deployment                   ║"
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
            create_index_template
            verify_deployment
            ;;
        backend)
            check_prerequisites
            load_config
            deploy_backend
            ;;
        import)
            load_config
            import_dashboards
            apply_ilm_policy
            create_index_template
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
            create_index_template
            verify_deployment
            ;;
    esac
    
    echo ""
    log_success "Done!"
}

main "$@"
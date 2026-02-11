#!/bin/bash
# Auto-Setup Script for 4-Node ELK Stack + Monitoring Dashboard
# Usage: ./auto-setup.sh [frontend|backend-n1|backend-n2|monitoring]

set -e

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Configuration
ES_VERSION="9.2.4"
FRONTEND_IP="10.4.4.87"
BACKEND_N1_IP="10.4.4.21"
BACKEND_N2_IP="10.4.4.90"
MONITORING_IP="10.4.4.52"
ES_USER="elastic"
ES_PASS="telehouse"

log() {
    echo -e "${GREEN}[$(date +'%Y-%m-%d %H:%M:%S')] $1${NC}"
}

warn() {
    echo -e "${YELLOW}[WARN] $1${NC}"
}

error() {
    echo -e "${RED}[ERROR] $1${NC}"
    exit 1
}

# Function: Install Elasticsearch
install_elasticsearch() {
    local node_type=$1
    log "Installing Elasticsearch ${ES_VERSION} (${node_type})..."
    
    # Add Elastic repository
    wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add - 2>/dev/null || true
    echo "deb https://artifacts.elastic.co/packages/9.x/apt stable main" | sudo tee /etc/apt/sources.list.d/elastic-9.x.list
    sudo apt update
    
    # Install specific version
    sudo apt install -y elasticsearch=${ES_VERSION}
    
    log "Elasticsearch installed"
}

# Function: Install Kibana
install_kibana() {
    log "Installing Kibana ${ES_VERSION}..."
    sudo apt install -y kibana=${ES_VERSION}
    log "Kibana installed"
}

# Function: Install Logstash
install_logstash() {
    log "Installing Logstash ${ES_VERSION}..."
    sudo apt install -y logstash=${ES_VERSION}
    log "Logstash installed"
}

# Function: Setup SSL Certificates
setup_ssl_certs() {
    log "Setting up SSL certificates..."
    
    local certs_dir="/etc/elasticsearch/certs"
    sudo mkdir -p ${certs_dir}
    
    if [ ! -f "${certs_dir}/elastic-certificates.p12" ]; then
        # Generate CA
        sudo /usr/share/elasticsearch/bin/elasticsearch-certutil ca -pass "" --out ${certs_dir}/elastic-stack-ca.p12
        
        # Generate node certificates
        sudo /usr/share/elasticsearch/bin/elasticsearch-certutil cert \
            --ca ${certs_dir}/elastic-stack-ca.p12 \
            --ca-pass "" \
            --pass "" \
            --out ${certs_dir}/elastic-certificates.p12
        
        sudo chmod 660 ${certs_dir}/*.p12
        sudo chown elasticsearch:elasticsearch ${certs_dir}/*.p12
    fi
    
    log "SSL certificates ready"
}

# Function: Configure Frontend Node
configure_frontend() {
    log "Configuring Frontend Node..."
    
    # Stop services
    sudo systemctl stop elasticsearch kibana logstash 2>/dev/null || true
    
    # Configure Elasticsearch
    sudo tee /etc/elasticsearch/elasticsearch.yml > /dev/null <<EOF
cluster.name: ElastiFlow-Cluster
node.name: es-frontend
node.roles: [master, data]
network.host: ["_site_", "_local_"]
http.port: 9200
transport.port: 9300
discovery.seed_hosts: ["${FRONTEND_IP}:9300", "${BACKEND_N1_IP}:9300", "${BACKEND_N2_IP}:9300"]
cluster.initial_master_nodes: ["es-frontend", "es-frontend-2", "es-remote"]

# SSL Settings for inter-node communication
xpack.security.enabled: true
xpack.security.transport.ssl.enabled: true
xpack.security.transport.ssl.verification_mode: certificate
xpack.security.transport.ssl.keystore.path: certs/elastic-certificates.p12
xpack.security.transport.ssl.truststore.path: certs/elastic-certificates.p12

# HTTP SSL (optional - can disable for local access)
xpack.security.http.ssl.enabled: false

# Memory settings
bootstrap.memory_lock: true
EOF
    
    # Configure Kibana (HTTP mode for compatibility)
    sudo tee /etc/kibana/kibana.yml > /dev/null <<EOF
server.port: 5601
server.host: "0.0.0.0"
server.name: "kibana-frontend"

# HTTP only (Debian 13 TLS compatibility)
server.ssl.enabled: false

# Elasticsearch connection
elasticsearch.hosts: ["https://${FRONTEND_IP}:9200", "https://${BACKEND_N1_IP}:9200", "https://${BACKEND_N2_IP}:9200"]
elasticsearch.username: "${ES_USER}"
elasticsearch.password: "${ES_PASS}"
elasticsearch.ssl.verificationMode: none

# Logging
logging.root.level: info
EOF
    
    # JVM Heap settings
    sudo tee /etc/elasticsearch/jvm.options.d/heap.options > /dev/null <<EOF
-Xms2g
-Xmx2g
EOF
    
    # Configure system limits
    sudo tee /etc/security/limits.d/elasticsearch.conf > /dev/null <<EOF
elasticsearch soft memlock unlimited
elasticsearch hard memlock unlimited
elasticsearch soft nofile 65536
elasticsearch hard nofile 65536
EOF
    
    # Start Elasticsearch
    sudo systemctl daemon-reload
    sudo systemctl enable elasticsearch
    sudo systemctl start elasticsearch
    
    log "Waiting for Elasticsearch to start..."
    sleep 30
    
    # Check cluster health
    until curl -s -u ${ES_USER}:${ES_PASS} http://localhost:9200/_cluster/health | grep -q '"status":"green"\|"status":"yellow"'; do
        warn "Waiting for cluster..."
        sleep 10
    done
    
    # Start Kibana
    sudo systemctl enable kibana
    sudo systemctl start kibana
    
    log "Frontend node configured"
}

# Function: Configure Backend Node
configure_backend() {
    local node_name=$1
    local config_name=$2
    log "Configuring Backend Node: ${node_name}..."
    
    # Stop services
    sudo systemctl stop elasticsearch logstash 2>/dev/null || true
    
    # Configure Elasticsearch
    sudo tee /etc/elasticsearch/elasticsearch.yml > /dev/null <<EOF
cluster.name: ElastiFlow-Cluster
node.name: ${node_name}
node.roles: [data]
network.host: ["_site_", "_local_"]
http.port: 9200
transport.port: 9300
discovery.seed_hosts: ["${FRONTEND_IP}:9300", "${BACKEND_N1_IP}:9300", "${BACKEND_N2_IP}:9300"]
cluster.initial_master_nodes: ["es-frontend", "es-frontend-2", "es-remote"]

# SSL Settings
xpack.security.enabled: true
xpack.security.transport.ssl.enabled: true
xpack.security.transport.ssl.verification_mode: certificate
xpack.security.transport.ssl.keystore.path: certs/elastic-certificates.p12
xpack.security.transport.ssl.truststore.path: certs/elastic-certificates.p12
xpack.security.http.ssl.enabled: false

# Memory settings
bootstrap.memory_lock: true
EOF
    
    # JVM Heap
    sudo tee /etc/elasticsearch/jvm.options.d/heap.options > /dev/null <<EOF
-Xms2g
-Xmx2g
EOF
    
    # System limits
    sudo tee /etc/security/limits.d/elasticsearch.conf > /dev/null <<EOF
elasticsearch soft memlock unlimited
elasticsearch hard memlock unlimited
elasticsearch soft nofile 65536
elasticsearch hard nofile 65536
EOF
    
    # Enable and start
    sudo systemctl daemon-reload
    sudo systemctl enable elasticsearch
    sudo systemctl start elasticsearch
    
    log "Backend node ${node_name} configured"
}

# Function: Setup Logstash NetFlow
setup_logstash_netflow() {
    log "Setting up Logstash NetFlow collector..."
    
    sudo tee /etc/logstash/conf.d/logstash-unified-netflow.conf > /dev/null <<'EOF'
input {
  udp {
    port => 2055
    codec => netflow
    type => "netflow"
  }
}

filter {
  # Common normalization
  mutate {
    add_field => {
      "[device][name]" => "juniper-sw"
      "[sampling][rate]" => 4096
    }
  }
  
  # Multiply bytes by sampling rate (4096x)
  if [netflow][in_bytes] {
    ruby {
      code => "event.set('[network][bytes]', event.get('[netflow][in_bytes]').to_i * 4096)"
    }
  }
  
  # IP and port mapping
  if [netflow][ipv4_src_addr] {
    mutate {
      add_field => {
        "[source][ip]" => "%{[netflow][ipv4_src_addr]}"
        "[source][port]" => "%{[netflow][l4_src_port]}"
        "[destination][ip]" => "%{[netflow][ipv4_dst_addr]}"
        "[destination][port]" => "%{[netflow][l4_dst_port]}"
        "[network][transport]" => "%{[netflow][protocol]}"
        "[network][packets]" => "%{[netflow][in_pkts]}"
        "[interface][input]" => "%{[netflow][input_snmp]}"
        "[interface][output]" => "%{[netflow][output_snmp]}"
      }
    }
  }
  
  # Protocol number to name
  translate {
    field => "[network][transport]"
    destination => "[network][transport]"
    dictionary => {
      "6" => "tcp"
      "17" => "udp"
      "1" => "icmp"
    }
    fallback => "other"
  }
  
  # Cleanup temporary fields
  mutate {
    remove_field => ["[netflow]", "type", "port"]
  }
}

output {
  elasticsearch {
    hosts => ["https://localhost:9200"]
    user => "elastic"
    password => "telehouse"
    ssl => true
    ssl_certificate_verification => false
    index => "unified-flow-%{+YYYY.MM.dd}"
    ilm_enabled => true
    ilm_rollover_alias => "unified-flow"
    ilm_pattern => "{now/d}-000001"
    ilm_policy => "flow-data-1-day-retention"
  }
}
EOF

    sudo systemctl enable logstash
    sudo systemctl start logstash
    
    log "NetFlow collector ready on port 2055"
}

# Function: Setup Logstash sFlow
setup_logstash_sflow() {
    log "Setting up Logstash sFlow collector..."
    
    sudo tee /etc/logstash/conf.d/logstash-unified-sflow.conf > /dev/null <<'EOF'
input {
  udp {
    port => 6343
    codec => sflow
    type => "sflow"
  }
}

filter {
  mutate {
    add_field => {
      "[device][name]" => "cisco-nexus"
      "[sampling][rate]" => 1
    }
  }
  
  # Map sFlow fields to unified schema
  if [sflow][datagram][sflow][sample][ipv4][src_ip] {
    mutate {
      add_field => {
        "[source][ip]" => "%{[sflow][datagram][sflow][sample][ipv4][src_ip]}"
        "[source][port]" => "%{[sflow][datagram][sflow][sample][ipv4][src_port]}"
        "[destination][ip]" => "%{[sflow][datagram][sflow][sample][ipv4][dst_ip]}"
        "[destination][port]" => "%{[sflow][datagram][sflow][sample][ipv4][dst_port]}"
        "[network][transport]" => "%{[sflow][datagram][sflow][sample][ipv4][protocol]}"
        "[network][bytes]" => "%{[sflow][datagram][sflow][sample][ipv4][length]}"
        "[network][packets]" => 1
      }
    }
  }
  
  # Protocol translation
  translate {
    field => "[network][transport]"
    destination => "[network][transport]"
    dictionary => {
      "6" => "tcp"
      "17" => "udp"
      "1" => "icmp"
    }
    fallback => "other"
  }
  
  # AS numbers (if available)
  if [sflow][datagram][sflow][sample][ipv4][src_as] {
    mutate {
      add_field => {
        "[source][as][number]" => "%{[sflow][datagram][sflow][sample][ipv4][src_as]}"
        "[destination][as][number]" => "%{[sflow][datagram][sflow][sample][ipv4][dst_as]}"
      }
    }
  }
  
  mutate {
    remove_field => ["[sflow]", "type", "port"]
  }
}

output {
  elasticsearch {
    hosts => ["https://localhost:9200"]
    user => "elastic"
    password => "telehouse"
    ssl => true
    ssl_certificate_verification => false
    index => "unified-flow-%{+YYYY.MM.dd}"
    ilm_enabled => true
    ilm_rollover_alias => "unified-flow"
    ilm_pattern => "{now/d}-000001"
    ilm_policy => "flow-data-1-day-retention"
  }
}
EOF

    sudo systemctl enable logstash
    sudo systemctl start logstash
    
    log "sFlow collector ready on port 6343"
}

# Function: Setup ILM Policy
setup_ilm() {
    log "Setting up ILM policy..."
    
    curl -s -XPUT -u ${ES_USER}:${ES_PASS} \
        -H "Content-Type: application/json" \
        "http://${FRONTEND_IP}:9200/_ilm/policy/flow-data-1-day-retention" \
        -d '{
      "policy": {
        "phases": {
          "hot": {
            "min_age": "0ms",
            "actions": {
              "rollover": {
                "max_size": "50GB",
                "max_age": "1d",
                "max_docs": 100000000
              },
              "set_priority": {
                "priority": 100
              }
            }
          },
          "delete": {
            "min_age": "1d",
            "actions": {
              "delete": {}
            }
          }
        }
      }
    }' | grep -q '"acknowledged":true' && log "ILM policy created" || warn "ILM policy may already exist"
}

# Function: Import Kibana Dashboards
import_dashboards() {
    log "Importing Kibana dashboards..."
    
    # Wait for Kibana
    until curl -s http://${FRONTEND_IP}:5601/api/status | grep -q '"level":"available"'; do
        warn "Waiting for Kibana..."
        sleep 10
    done
    
    # Import dashboards
    curl -s -u ${ES_USER}:${ES_PASS} -XPOST \
        -H "kbn-xsrf: true" \
        "http://${FRONTEND_IP}:5601/api/saved_objects/_import?overwrite=true" \
        --form file=@kibana-dashboard-fixed.ndjson | grep -q '"success":true' && \
        log "Dashboards imported successfully" || \
        warn "Dashboard import had issues"
}

# Function: Setup Index Template
setup_index_template() {
    log "Setting up index template..."
    
    curl -s -XPUT -u ${ES_USER}:${ES_PASS} \
        -H "Content-Type: application/json" \
        "http://${FRONTEND_IP}:9200/_index_template/unified-flow-template" \
        -d '{
      "index_patterns": ["unified-flow-*"],
      "template": {
        "settings": {
          "number_of_shards": 1,
          "number_of_replicas": 0,
          "index.lifecycle.name": "flow-data-1-day-retention",
          "index.lifecycle.rollover_alias": "unified-flow"
        },
        "mappings": {
          "properties": {
            "@timestamp": {"type": "date"},
            "device.name": {"type": "keyword"},
            "source.ip": {"type": "ip"},
            "source.port": {"type": "integer"},
            "source.as.number": {"type": "integer"},
            "destination.ip": {"type": "ip"},
            "destination.port": {"type": "integer"},
            "destination.as.number": {"type": "integer"},
            "network.transport": {"type": "keyword"},
            "network.bytes": {"type": "long"},
            "network.packets": {"type": "long"},
            "interface.input": {"type": "integer"},
            "interface.output": {"type": "integer"},
            "sampling.rate": {"type": "integer"}
          }
        }
      }
    }' | grep -q '"acknowledged":true' && log "Index template created" || warn "Template may already exist"
}

# Function: Setup Monitoring Dashboard
setup_monitoring() {
    log "Setting up Monitoring Dashboard..."
    
    # Install dependencies
    sudo apt install -y sqlite3 python3-pip
    pip3 install flask --break-system-packages 2>/dev/null || pip3 install flask --user
    
    # Create directories
    mkdir -p ~/.openclaw/monitor-dashboard/data
    mkdir -p ~/.openclaw/monitor-dashboard/templates
    mkdir -p ~/.openclaw/monitor-dashboard/static
    
    # Copy files (assuming we're in the repo directory)
    cp -r monitor-dashboard/* ~/.openclaw/monitor-dashboard/ 2>/dev/null || \
        warn "monitor-dashboard/ directory not found, manual setup required"
    
    # Initialize database
    cd ~/.openclaw/monitor-dashboard
    python3 -c "
from database import init_db, insert_default_servers
init_db()
insert_default_servers()
print('Database initialized')
"
    
    # Fix Kibana URL to use HTTP
    sqlite3 ~/.openclaw/monitor-dashboard/data/monitoring.db \
        "UPDATE services SET type='http', url='http://${FRONTEND_IP}:5601/api/status' WHERE name='Kibana';" 2>/dev/null || true
    
    log "Monitoring Dashboard ready"
    log "Start with: cd ~/.openclaw/monitor-dashboard && python3 app.py"
    log "Access at: http://${MONITORING_IP}:8080"
}

# Function: Show Status
show_status() {
    log "Setup Complete! Access URLs:"
    echo ""
    echo "  Kibana Dashboard:     http://${FRONTEND_IP}:5601"
    echo "  Monitoring Dashboard: http://${MONITORING_IP}:8080"
    echo "  Elasticsearch API:    http://${FRONTEND_IP}:9200"
    echo ""
    echo "  Login: elastic / telehouse"
    echo ""
    echo "  NetFlow Collector:    ${BACKEND_N1_IP}:2055 (UDP)"
    echo "  sFlow Collector:      ${BACKEND_N2_IP}:6343 (UDP)"
    echo ""
    
    # Test connections
    log "Testing connections..."
    curl -s -u ${ES_USER}:${ES_PASS} http://${FRONTEND_IP}:9200/_cluster/health | \
        jq -r '{status: .status, nodes: .number_of_nodes, data_nodes: .number_of_data_nodes}' 2>/dev/null || \
        warn "Could not connect to Elasticsearch"
}

# Main menu
case "${1:-menu}" in
    frontend)
        install_elasticsearch "frontend"
        install_kibana
        install_logstash
        setup_ssl_certs
        configure_frontend
        setup_ilm
        setup_index_template
        import_dashboards
        show_status
        ;;
    backend-n1)
        install_elasticsearch "backend"
        install_logstash
        configure_backend "es-remote" "backend-n1"
        setup_logstash_netflow
        ;;
    backend-n2)
        install_elasticsearch "backend"
        install_logstash
        configure_backend "es-remote" "backend-n2"
        setup_logstash_sflow
        ;;
    monitoring)
        setup_monitoring
        ;;
    full)
        log "This must be run on each node separately"
        log "Run on Frontend:  $0 frontend"
        log "Run on Backend 1: $0 backend-n1"
        log "Run on Backend 2: $0 backend-n2"
        log "Run on Monitor:   $0 monitoring"
        ;;
    status)
        show_status
        ;;
    *)
        echo "ELK Stack + Monitoring Auto-Setup"
        echo ""
        echo "Usage: $0 [command]"
        echo ""
        echo "Commands:"
        echo "  frontend    - Setup frontend node (ES + Kibana + Logstash)"
        echo "  backend-n1  - Setup Backend N1 (ES + NetFlow Logstash)"
        echo "  backend-n2  - Setup Backend N2 (ES + sFlow Logstash)"
        echo "  monitoring  - Setup Monitoring Dashboard"
        echo "  full        - Show instructions for full setup"
        echo "  status      - Check cluster status"
        echo ""
        echo "Run on each node in order: frontend → backend-n1 → backend-n2 → monitoring"
        ;;
esac

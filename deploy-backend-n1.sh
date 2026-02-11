#!/bin/bash
# Deploy script for Backend N1 (10.4.4.21) - Juniper NetFlow collector
# This machine should receive NetFlow data from Juniper, sampled 1/4096

set -e

# Install Docker if not present
if ! command -v docker &> /dev/null; then
    echo "Installing Docker..."
    apt-get update
    apt-get install -y docker.io docker-compose
    systemctl enable docker
    systemctl start docker
fi

# Create deployment directory
mkdir -p /opt/elk-backend-n1

# Create docker-compose file for Backend N1
cat > /opt/elk-backend-n1/docker-compose.yml << 'EOF'
version: '3.8'

services:
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:9.2.4
    container_name: es-data-n1
    restart: unless-stopped
    environment:
      - node.name=es-data-n1
      - cluster.name=netflow-cluster
      - node.roles=data,ingest
      - discovery.seed_hosts=10.4.4.87:9300
      - ELASTIC_PASSWORD=telehouse
      - xpack.security.enabled=true
      - xpack.security.http.ssl.enabled=true
      - xpack.security.http.ssl.certificate_authorities=/usr/share/elasticsearch/config/certs/ca/ca.crt
      - xpack.security.http.ssl.certificate=/usr/share/elasticsearch/config/certs/wildcard/wildcard.crt
      - xpack.security.http.ssl.key=/usr/share/elasticsearch/config/certs/wildcard/wildcard.key
      - xpack.security.transport.ssl.enabled=true
      - xpack.security.transport.ssl.certificate_authorities=/usr/share/elasticsearch/config/certs/ca/ca.crt
      - xpack.security.transport.ssl.certificate=/usr/share/elasticsearch/config/certs/wildcard/wildcard.crt
      - xpack.security.transport.ssl.key=/usr/share/elasticsearch/config/certs/wildcard/wildcard.key
      - bootstrap.memory_lock=true
      - "ES_JAVA_OPTS=-Xms2g -Xmx2g"
    ulimits:
      memlock:
        soft: -1
        hard: -1
    volumes:
      - es-data-n1:/usr/share/elasticsearch/data
      - ./certs:/usr/share/elasticsearch/config/certs:ro
    ports:
      - "9200:9200"
      - "9300:9300"
    networks:
      - elk-net

  logstash-netflow:
    image: docker.elastic.co/logstash/logstash:9.2.4
    container_name: logstash-netflow
    restart: unless-stopped
    environment:
      - ELASTIC_PASSWORD=telehouse
      - QUEUE_TYPE=persisted
      - QUEUE_MAX_BYTES=1gb
    volumes:
      - ./logstash-netflow.conf:/usr/share/logstash/pipeline/logstash.conf:ro
      - ./certs/ca/ca.crt:/usr/share/logstash/ca.crt:ro
    ports:
      - "2050:2050/udp"
    networks:
      - elk-net
    depends_on:
      - elasticsearch

volumes:
  es-data-n1:

networks:
  elk-net:
    driver: bridge
EOF

# Create Logstash config for NetFlow with sampling multiplier
cat > /opt/elk-backend-n1/logstash-netflow.conf << 'EOF'
input {
  udp {
    port => 2050
    type => "netflow"
    codec => netflow {
      versions => [5, 9, 10]
    }
  }
}

filter {
  # Apply sampling multiplier for Juniper 1/4096 sampling
  if [netflow][sampling_interval] {
    ruby {
      code => "
        sampling = event.get('[netflow][sampling_interval]') || 4096
        bytes = event.get('[netflow][in_bytes]') || 0
        packets = event.get('[netflow][in_pkts]') || 0
        event.set('[netflow][in_bytes_scaled]', bytes * sampling)
        event.set('[netflow][in_pkts_scaled]', packets * sampling)
      "
    }
  }

  # Add fields for ECS compatibility
  mutate {
    add_field => {
      "[network][bytes]" => "%{[netflow][in_bytes_scaled]}"
      "[source][ip]" => "%{[netflow][ipv4_src_addr]}"
      "[destination][ip]" => "%{[netflow][ipv4_dst_addr]}"
      "[@timestamp]" => "%{[netflow][flow_start]}"
    }
  }

  # Convert bytes to integer
  mutate {
    convert => {
      "[network][bytes]" => "integer"
    }
  }
}

output {
  elasticsearch {
    hosts => ["https://elasticsearch:9200", "https://10.4.4.87:9200"]
    index => "logs-netflow-%{+YYYY.MM.dd}"
    ssl => true
    ssl_certificate_authorities => "/usr/share/logstash/ca.crt"
    user => "elastic"
    password => "${ELASTIC_PASSWORD}"
  }
}
EOF

echo "Checking for SSL certificates..."
if [ ! -d "/opt/elk-backend-n1/certs" ]; then
    echo "WARNING: SSL certs directory not found at /opt/elk-backend-n1/certs"
    echo "Please copy certs from frontend node (10.4.4.87) before starting"
fi

echo ""
echo "============================================"
echo "Backend N1 deployment files created!"
echo "============================================"
echo ""
echo "Next steps:"
echo "1. Copy SSL certificates to /opt/elk-backend-n1/certs/"
echo "   You can get them from: root@10.4.4.87:/opt/elk/certs"
echo ""
echo "2. Start the containers:"
echo "   cd /opt/elk-backend-n1 && docker-compose up -d"
echo ""
echo "3. Verify connection to cluster:"
echo "   curl -k -u elastic:telehouse https://localhost:9200/_cluster/health"
echo ""

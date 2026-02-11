#!/bin/bash
# Deploy script for Backend N2 (10.4.4.90) - Cisco Nexus sFlow collector

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
mkdir -p /opt/elk-backend-n2

# Create docker-compose file for Backend N2
cat > /opt/elk-backend-n2/docker-compose.yml << 'EOF'
version: '3.8'

services:
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:9.2.4
    container_name: es-data-n2
    restart: unless-stopped
    environment:
      - node.name=es-data-n2
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
      - es-data-n2:/usr/share/elasticsearch/data
      - ./certs:/usr/share/elasticsearch/config/certs:ro
    ports:
      - "9200:9200"
      - "9300:9300"
    networks:
      - elk-net

  elastiflow-sflow:
    image: elastiflow/unified-collector:latest
    container_name: elastiflow-sflow
    restart: unless-stopped
    environment:
      - EF_LICENSE_KEY=free
      - EF_LOGGER_LEVEL=info
      - EF_SFLOW_PORT=6343
      - EF_SFLOW_IP=0.0.0.0
      - EF_OUTPUT_ELASTICSEARCH_ENABLE=true
      - EF_OUTPUT_ELASTICSEARCH_HOST=elasticsearch:9200
      - EF_OUTPUT_ELASTICSEARCH_INDEX=elastiflow
      - EF_OUTPUT_ELASTICSEARCH_TEMPLATE_ENABLED=true
      - EF_GEOIP_ENABLE=false
    ports:
      - "6343:6343/udp"
    networks:
      - elk-net
    depends_on:
      - elasticsearch

volumes:
  es-data-n2:

networks:
  elk-net:
    driver: bridge
EOF

echo "Checking for SSL certificates..."
if [ ! -d "/opt/elk-backend-n2/certs" ]; then
    echo "WARNING: SSL certs directory not found at /opt/elk-backend-n2/certs"
    echo "Please copy certs from frontend node (10.4.4.87) before starting"
fi

echo ""
echo "============================================"
echo "Backend N2 deployment files created!"
echo "============================================"
echo ""
echo "Next steps:"
echo "1. Copy SSL certificates to /opt/elk-backend-n2/certs/"
echo "   You can get them from: root@10.4.4.87:/opt/elk/certs"
echo ""
echo "2. Start the containers:"
echo "   cd /opt/elk-backend-n2 && docker-compose up -d"
echo ""
echo "3. Verify connection to cluster:"
echo "   curl -k -u elastic:telehouse https://localhost:9200/_cluster/health"
echo ""

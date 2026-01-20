#!/bin/bash

# Define filenames
CA_ZIP="elastic-stack-ca.zip"
CERTS_ZIP="node-certs.zip"
OUTPUT_DIR="./certs"

# Create directory structure
mkdir -p $OUTPUT_DIR

echo "--- Generating Certificate Authority (CA) ---"
# This creates a CA that both clusters will trust
docker run --rm -v $(pwd)/$OUTPUT_DIR:/certs \
  docker.elastic.co/elasticsearch/elasticsearch:9.2.4 \
  bin/elasticsearch-certutil ca --out /certs/elastic-stack-ca.p12 --pass "" --silent

echo "--- Generating Node Certificates ---"
# We create a YAML file to define the instances for which we need certs
cat <<EOF > $OUTPUT_DIR/instances.yml
instances:
  - name: es-frontend
    dns: ["es-frontend", "localhost"]
    ip: ["127.0.0.1"]
  - name: es-backend # Replace with Backend Server cluster.name
    dns: ["es-backend"] # Same as above
    ip: ["<BACKEND_SERVER_IP>"] # Replace with Backend Server IP
EOF

# Generate the certificates using the CA created above
docker run --rm -v $(pwd)/$OUTPUT_DIR:/certs \
  docker.elastic.co/elasticsearch/elasticsearch:9.2.4 \
  bin/elasticsearch-certutil cert --ca /certs/elastic-stack-ca.p12 --ca-pass "" \
  --in /certs/instances.yml --out /certs/bundle.zip --pass "" --silent

# Unzip the results
apt-get install unzip -y || yum install unzip -y
unzip $OUTPUT_DIR/bundle.zip -d $OUTPUT_DIR/

echo "--- Cleaning up ---"
rm $OUTPUT_DIR/bundle.zip $OUTPUT_DIR/instances.yml
chmod 644 $OUTPUT_DIR/*/*.p12

echo "Certificates generated in $OUTPUT_DIR"

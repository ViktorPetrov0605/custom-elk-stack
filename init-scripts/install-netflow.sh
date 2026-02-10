#!/bin/bash
# Auto-install NetFlow integration on Kibana startup
# This script waits for Kibana to be ready, then installs the NetFlow package

KIBANA_URL="http://es-frontend:5601"
ES_URL="http://es-frontend:9200"
MAX_RETRIES=30
RETRY_DELAY=10

echo "=== Kibana NetFlow Auto-Installer ==="
echo "Waiting for Kibana to be ready..."

# Wait for Kibana to be available
for i in $(seq 1 $MAX_RETRIES); do
    if curl -s "$KIBANA_URL/api/status" | grep -q '"level":"available"'; then
        echo "✓ Kibana is available (attempt $i)"
        break
    fi
    echo "  Waiting... ($i/$MAX_RETRIES)"
    sleep $RETRY_DELAY
done

# Check if already authenticated or need to wait for setup
sleep 10

echo "Installing NetFlow integration..."

# Install NetFlow package via Kibana API
curl -X POST "$KIBANA_URL/api/fleet/package_policies" \
  -H "Content-Type: application/json" \
  -H "kbn-xsrf: true" \
  -u "elastic:${ELASTIC_PASSWORD}" \
  -d '{
    "name": "netflow-auto",
    "description": "Auto-installed NetFlow integration",
    "namespace": "default",
    "policy_ids": ["${AGENT_POLICY_ID:-agent-policy-1}"],
    "package": {
      "name": "netflow",
      "version": "2.24.1"
    },
    "inputs": {
      "netflow-netflow": {
        "enabled": true,
        "streams": {
          "netflow.log": {
            "enabled": true,
            "vars": {
              "host": "0.0.0.0",
              "port": "2050",
              "queue_size": 8192,
              "workers": 1,
              "expiration_timeout": "30m",
              "custom_definitions": [],
              "internal_networks": [],
              "tags": ["netflow"]
            }
          }
        }
      }
    }
  }' -s -o /tmp/netflow_install_response.json -w "HTTP Status: %{http_code}\n"

echo "Installation response:"
cat /tmp/netflow_install_response.json

# Verify installation
if curl -s "$KIBANA_URL/api/fleet/package_policies" -u "elastic:${ELASTIC_PASSWORD}" | grep -q "netflow"; then
    echo "✓ NetFlow integration successfully installed!"
    exit 0
else
    echo "✗ NetFlow installation may have failed, check response above"
    exit 1
fi

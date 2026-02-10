#!/bin/bash
# Wait for Kibana to be ready before running init scripts

KIBANA_URL="${KIBANA_URL:-http://es-frontend:5601}"
MAX_RETRIES=30
RETRY_DELAY=10

echo "Waiting for Kibana at $KIBANA_URL..."

for i in $(seq 1 $MAX_RETRIES); do
    response=$(curl -s "$KIBANA_URL/api/status" 2>/dev/null)
    
    if echo "$response" | grep -q '"level":"available"'; then
        echo "✓ Kibana is available! (attempt $i)"
        echo "Kibana status: $(echo "$response" | grep -o '"level":"available"')"
        exit 0
    fi
    
    if echo "$response" | grep -q '"level":"degraded"'; then
        echo "~ Kibana is degraded but functional (attempt $i)"
        exit 0
    fi
    
    echo "  Kibana not ready yet... ($i/$MAX_RETRIES)"
    sleep $RETRY_DELAY
done

echo "✗ Timeout waiting for Kibana"
exit 1

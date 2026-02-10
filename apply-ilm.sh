#!/bin/bash
# VB: Script to apply ILM policy for 1-day data retention
# Run this after Elasticsearch is running

set -e

ES_HOST="${FRONTEND_IP:-10.4.4.87}"
ES_USER="${ES_USER:-elastic}"
ES_PASS="${ES_PASS:-<YOUR_PASSWORD>}"

echo "Applying ILM policy for 1-day retention..."

curl -k -X PUT "https://${ES_HOST}:9200/_ilm/policy/netflow-1day-retention" \
  -u "${ES_USER}:${ES_PASS}" \
  -H "Content-Type: application/json" \
  -d @ilm-policy.json

echo "ILM policy applied successfully."
echo ""
echo "Next: Create index templates with ILM policy..."

# Create index template for netflow data stream
curl -k -X PUT "https://${ES_HOST}:9200/_index_template/netflow-template" \
  -u "${ES_USER}:${ES_PASS}" \
  -H "Content-Type: application/json" \
  -d '{
    "index_patterns": ["netflow.log*"],
    "data_stream": {},
    "priority": 500,
    "template": {
      "settings": {
        "index.lifecycle.name": "netflow-1day-retention",
        "index.lifecycle.rollover_alias": "netflow"
      }
    }
  }'

echo "Index template created for netflow."

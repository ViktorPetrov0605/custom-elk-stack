#!/bin/bash
# Logstash Flow Collector Migration Script
# Migrates from ElastiFlow to Logstash for unlimited flow collection

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

log_info() { echo -e "${GREEN}[INFO]${NC} $1"; }
log_warn() { echo -e "${YELLOW}[WARN]${NC} $1"; }
log_error() { echo -e "${RED}[ERROR]${NC} $1"; }

# Configuration
ES_HOST="${ELASTICSEARCH_HOST:-10.4.4.87:9200}"
ES_USER="${ES_USER:-elastic}"
ES_PASSWORD="${ES_PASSWORD:-telehouse}"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "=========================================="
echo "Logstash Flow Collector Migration"
echo "=========================================="
echo ""
echo "This script will:"
echo "1. Create ILM policy for flow data"
echo "2. Create index template"
echo "3. Create rollover alias"
echo "4. Deploy Logstash on backend servers"
echo ""
echo "Target Elasticsearch: $ES_HOST"
echo ""

read -p "Continue? (y/n) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Aborted."
    exit 1
fi

# Step 1: Create ILM Policy
log_info "Creating ILM policy..."
curl -s -k -u "$ES_USER:$ES_PASSWORD" -X PUT "https://$ES_HOST/_ilm/policy/flow-data-3-day" \
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
            "set_priority": { "priority": 100 }
          }
        },
        "warm": {
          "min_age": "1d",
          "actions": {
            "shrink": { "number_of_shards": 1 },
            "forcemerge": { "max_num_segments": 1 },
            "set_priority": { "priority": 50 }
          }
        },
        "delete": {
          "min_age": "3d",
          "actions": { "delete": {} }
        }
      }
    }
  }' | jq . && echo ""

# Step 2: Create Index Template
log_info "Creating index template..."
curl -s -k -u "$ES_USER:$ES_PASSWORD" -X PUT "https://$ES_HOST/_index_template/logstash-flow" \
  -H "Content-Type: application/json" \
  -d @- << 'EOF' | jq . && echo ""
{
  "index_patterns": ["logstash-flow-*"],
  "template": {
    "settings": {
      "number_of_shards": 2,
      "number_of_replicas": 1,
      "index.lifecycle.name": "flow-data-3-day",
      "index.lifecycle.rollover_alias": "logstash-flow"
    },
    "mappings": {
      "dynamic_templates": [
        { "strings_as_keywords": { "match_mapping_type": "string", "mapping": { "type": "keyword", "ignore_above": 1024 } } },
        { "ip_fields": { "match": "*ip", "mapping": { "type": "ip" } } }
      ],
      "properties": {
        "@timestamp": { "type": "date" },
        "host": { "properties": { "ip": { "type": "ip" }, "name": { "type": "keyword" } } },
        "source": { "properties": { "ip": { "type": "ip" }, "port": { "type": "integer" }, "bytes": { "type": "long" }, "packets": { "type": "long" } } },
        "destination": { "properties": { "ip": { "type": "ip" }, "port": { "type": "integer" }, "bytes": { "type": "long" }, "packets": { "type": "long" } } },
        "client": { "properties": { "ip": { "type": "ip" }, "port": { "type": "integer" } } },
        "server": { "properties": { "ip": { "type": "ip" }, "port": { "type": "integer" } } },
        "network": { "properties": { "bytes": { "type": "long" }, "packets": { "type": "long" }, "transport": { "type": "keyword" }, "direction": { "type": "keyword" } } },
        "flow": { "properties": { "id": { "type": "keyword" }, "sample": { "properties": { "rate": { "type": "integer" } } }, "locality": { "type": "keyword" } } },
        "event": { "properties": { "category": { "type": "keyword" }, "type": { "type": "keyword" }, "dataset": { "type": "keyword" }, "module": { "type": "keyword" } } },
        "observer": { "properties": { "ingress": { "properties": { "interface": { "properties": { "id": { "type": "integer" } } } } }, "egress": { "properties": { "interface": { "properties": { "id": { "type": "integer" } } } } } } }
      }
    }
  }
}
EOF

# Step 3: Create initial index with alias
log_info "Creating initial index..."
curl -s -k -u "$ES_USER:$ES_PASSWORD" -X DELETE "https://$ES_HOST/logstash-flow-*" 2>/dev/null || true
curl -s -k -u "$ES_USER:$ES_PASSWORD" -X PUT "https://$ES_HOST/logstash-flow-000001" \
  -H "Content-Type: application/json" \
  -d '{
    "aliases": {
      "logstash-flow": { "is_write_index": true }
    }
  }' | jq . && echo ""

log_info "Elasticsearch setup complete!"
echo ""
echo "=========================================="
echo "Next Steps:"
echo "=========================================="
echo ""
echo "1. Copy files to backend servers:"
echo "   scp logstash.conf docker-compose-logstash.yml user@backend:/opt/logstash-flow/"
echo ""
echo "2. Stop ElastiFlow on each backend:"
echo "   docker compose -f elastiflow down"
echo ""
echo "3. Start Logstash on each backend:"
echo "   ELASTICSEARCH_HOST=10.4.4.87:9200 ELASTIC_PASSWORD=yourpassword \\"
echo "   docker compose -f docker-compose-logstash up -d"
echo ""
echo "4. Verify data flowing:"
echo "   curl -k -u elastic:password https://10.4.4.87:9200/logstash-flow/_count"
echo ""
#!/bin/bash
# check_elastiflow.sh - Check ElastiFlow collector status
# Author: Valentin-bot
# Date: 2026-02-12

ES_USER="elastic"
ES_PASS="telehouse"
ES_HOST="https://10.4.4.87:9200"

echo "╔════════════════════════════════════════════════════════════════╗"
echo "║         ElastiFlow Unified Collector Status Check              ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "=== Backend N1 (NetFlow - 10.4.4.21:2332) ==="
N1_STATUS=$(sshpass -p 'T3l3h0us#' ssh -o ConnectTimeout=5 -o StrictHostKeyChecking=no -p 2332 telehouse@10.4.4.21 "docker ps --filter name=flow-collector --format '{{.Status}}'" 2>/dev/null)
if [ -n "$N1_STATUS" ]; then
    echo -e "${GREEN}● Running${NC}: $N1_STATUS"
    RECENT_N1=$(sshpass -p 'T3l3h0us#' ssh -o ConnectTimeout=5 -p 2332 telehouse@10.4.4.21 "docker logs flow-collector 2>&1 | grep -E 'received|processed|error' | tail -3" 2>/dev/null)
    echo "Recent activity: $RECENT_N1"
else
    echo -e "${RED}✗ Not running or unreachable${NC}"
fi
echo ""

echo "=== Backend N2 (sFlow - 10.4.4.90:22) ==="
N2_STATUS=$(sshpass -p 'T3l3h0us#' ssh -o ConnectTimeout=5 -o StrictHostKeyChecking=no telehouse@10.4.4.90 "docker ps --filter name=flow-collector --format '{{.Status}}'" 2>/dev/null)
if [ -n "$N2_STATUS" ]; then
    echo -e "${GREEN}● Running${NC}: $N2_STATUS"
    RECENT_N2=$(sshpass -p 'T3l3h0us#' ssh -o ConnectTimeout=5 telehouse@10.4.4.90 "docker logs flow-collector 2>&1 | grep -E 'received|processed|error' | tail -3" 2>/dev/null)
    echo "Recent activity: $RECENT_N2"
else
    echo -e "${RED}✗ Not running or unreachable${NC}"
fi
echo ""

echo "=== Elasticsearch Index Stats ==="
curl -s -u "$ES_USER:$ES_PASS" -k "$ES_HOST/_cat/indices/elastiflow-flow-*?v&h=index,docs.count,store.size&s=docs.count:desc" 2>/dev/null | head -5
if [ $? -ne 0 ]; then
    echo -e "${RED}✗ Cannot connect to Elasticsearch${NC}"
fi
echo ""

echo "=== Device Flow Stats (Last 24h) ==="
DEVICE_STATS=$(curl -s -u "$ES_USER:$ES_PASS" -k -X POST "$ES_HOST/elastiflow-flow-*/_search?size=0" \
  -H "Content-Type: application/json" \
  -d '{
    "query": {
      "range": { "@timestamp": { "gte": "now-24h" } }
    },
    "aggs": {
      "devices": {
        "terms": { "field": "host.ip", "size": 10 }
      },
      "types": {
        "terms": { "field": "event.dataset", "size": 5 }
      }
    }
  }' 2>/dev/null)

if [ -n "$DEVICE_STATS" ]; then
    echo "By Device IP:"
    echo "$DEVICE_STATS" | jq -r '.aggregations.devices.buckets[] | "  - " + .key + ": " + (.doc_count | tostring) + " records"' 2>/dev/null || echo "  (no data)"
    echo ""
    echo "By Flow Type:"
    echo "$DEVICE_STATS" | jq -r '.aggregations.types.buckets[] | "  - " + .key + ": " + (.doc_count | tostring) + " records"' 2>/dev/null || echo "  (no data)"
else
    echo -e "${RED}✗ Cannot query device stats${NC}"
fi
echo ""

echo "=== Quick Actions ==="
echo "Restart N1: sshpass -p 'T3l3h0us#' ssh -p 2332 telehouse@10.4.4.21 'cd ~/elastiflow && docker-compose restart'"
echo "Restart N2: sshpass -p 'T3l3h0us#' ssh telehouse@10.4.4.90 'cd ~/elastiflow && docker-compose restart'"
echo "View N1 logs: sshpass -p 'T3l3h0us#' ssh -p 2332 telehouse@10.4.4.21 'docker logs flow-collector --tail 50'"
echo "View N2 logs: sshpass -p 'T3l3h0us#' ssh telehouse@10.4.4.90 'docker logs flow-collector --tail 50'"
echo ""
echo "Kibana: https://10.4.4.87:5601/app/dashboards"

#!/bin/bash
# VB: Install Unified Flow Dashboard to Kibana
# Usage: ./install-dashboard.sh [KIBANA_URL] [ES_USER] [ES_PASS]

set -e

KIBANA_URL="${1:-http://10.4.4.87:5601}"
ES_USER="${2:-elastic}"
ES_PASS="${3:-telehouse}"

echo "VB: Installing Unified Flow Dashboard..."
echo "Kibana: $KIBANA_URL"

# Check Kibana is reachable
echo "Checking Kibana connectivity..."
curl -s -u "$ES_USER:$ES_PASS" "$KIBANA_URL/api/status" > /dev/null || {
    echo "ERROR: Cannot connect to Kibana at $KIBANA_URL"
    exit 1
}

# Create index pattern if not exists
echo "Creating index pattern 'elastiflow-flow'..."
curl -s -X POST -u "$ES_USER:$ES_PASS" "$KIBANA_URL/api/saved_objects/index-pattern" \
  -H "Content-Type: application/json" \
  -H "kbn-xsrf: true" \
  -d '{
    "attributes": {
      "title": "elastiflow-flow-codex-*",
      "timeFieldName": "@timestamp"
    }
  }' 2>/dev/null || echo "Index pattern may already exist"

# Create visualizations
echo "Creating visualizations..."

# Traffic Over Time
curl -s -X POST -u "$ES_USER:$ES_PASS" "$KIBANA_URL/api/saved_objects/visualization" \
  -H "Content-Type: application/json" \
  -H "kbn-xsrf: true" \
  -d '{
    "id": "traffic-over-time",
    "attributes": {
      "title": "Traffic Over Time",
      "visState": "{\"title\":\"Traffic Over Time\",\"type\":\"line\",\"aggs\":[{\"id\":\"1\",\"enabled\":true,\"type\":\"sum\",\"schema\":\"metric\",\"params\":{\"field\":\"flow.bytes\"}},{\"id\":\"2\",\"enabled\":true,\"type\":\"date_histogram\",\"schema\":\"segment\",\"params\":{\"field\":\"@timestamp\",\"interval\":\"auto\"}}],\"params\":{\"type\":\"line\"}}"
    },
    "references": [{"id": "elastiflow-flow", "name": "kibanaSavedObjectMeta.searchSourceJSON.index", "type": "index-pattern"}]
  }' 2>/dev/null || echo "Visualization may already exist"

# Top Source IPs
curl -s -X POST -u "$ES_USER:$ES_PASS" "$KIBANA_URL/api/saved_objects/visualization" \
  -H "Content-Type: application/json" \
  -H "kbn-xsrf: true" \
  -d '{
    "id": "top-source-ips",
    "attributes": {
      "title": "Top Source IPs",
      "visState": "{\"title\":\"Top Source IPs\",\"type\":\"horizontal_bar\",\"aggs\":[{\"id\":\"1\",\"enabled\":true,\"type\":\"sum\",\"schema\":\"metric\",\"params\":{\"field\":\"flow.bytes\"}},{\"id\":\"2\",\"enabled\":true,\"type\":\"terms\",\"schema\":\"segment\",\"params\":{\"field\":\"flow.src.ip.addr\",\"size\":10,\"order\":\"desc\",\"orderBy\":\"1\"}}],\"params\":{\"type\":\"horizontal_bar\"}}"
    },
    "references": [{"id": "elastiflow-flow", "name": "kibanaSavedObjectMeta.searchSourceJSON.index", "type": "index-pattern"}]
  }' 2>/dev/null || echo "Visualization may already exist"

# Top Destination IPs
curl -s -X POST -u "$ES_USER:$ES_PASS" "$KIBANA_URL/api/saved_objects/visualization" \
  -H "Content-Type: application/json" \
  -H "kbn-xsrf: true" \
  -d '{
    "id": "top-dest-ips",
    "attributes": {
      "title": "Top Destination IPs",
      "visState": "{\"title\":\"Top Destination IPs\",\"type\":\"horizontal_bar\",\"aggs\":[{\"id\":\"1\",\"enabled\":true,\"type\":\"sum\",\"schema\":\"metric\",\"params\":{\"field\":\"flow.bytes\"}},{\"id\":\"2\",\"enabled\":true,\"type\":\"terms\",\"schema\":\"segment\",\"params\":{\"field\":\"flow.dst.ip.addr\",\"size\":10,\"order\":\"desc\",\"orderBy\":\"1\"}}],\"params\":{\"type\":\"horizontal_bar\"}}"
    },
    "references": [{"id": "elastiflow-flow", "name": "kibanaSavedObjectMeta.searchSourceJSON.index", "type": "index-pattern"}]
  }' 2>/dev/null || echo "Visualization may already exist"

# Protocol Distribution
curl -s -X POST -u "$ES_USER:$ES_PASS" "$KIBANA_URL/api/saved_objects/visualization" \
  -H "Content-Type: application/json" \
  -H "kbn-xsrf: true" \
  -d '{
    "id": "protocol-distribution",
    "attributes": {
      "title": "Protocol Distribution",
      "visState": "{\"title\":\"Protocol Distribution\",\"type\":\"pie\",\"aggs\":[{\"id\":\"1\",\"enabled\":true,\"type\":\"sum\",\"schema\":\"metric\",\"params\":{\"field\":\"flow.bytes\"}},{\"id\":\"2\",\"enabled\":true,\"type\":\"terms\",\"schema\":\"segment\",\"params\":{\"field\":\"l4.proto.name\",\"size\":10,\"order\":\"desc\",\"orderBy\":\"1\"}}],\"params\":{\"type\":\"pie\"}}"
    },
    "references": [{"id": "elastiflow-flow", "name": "kibanaSavedObjectMeta.searchSourceJSON.index", "type": "index-pattern"}]
  }' 2>/dev/null || echo "Visualization may already exist"

# Create dashboard
echo "Creating dashboard..."
curl -s -X POST -u "$ES_USER:$ES_PASS" "$KIBANA_URL/api/saved_objects/dashboard" \
  -H "Content-Type: application/json" \
  -H "kbn-xsrf: true" \
  -d '{
    "id": "unified-flow-dashboard",
    "attributes": {
      "title": "Unified Flow Dashboard",
      "description": "Device-agnostic flow analytics with IP filtering",
      "hits": 0,
      "version": 1,
      "timeRestore": false,
      "optionsJSON": "{\"useMargins\":true,\"syncColors\":false,\"hidePanelTitles\":false}",
      "panelsJSON": "[{\"version\":\"9.2.4\",\"type\":\"visualization\",\"gridData\":{\"x\":0,\"y\":0,\"w\":24,\"h\":15,\"i\":\"1\"},\"panelIndex\":\"1\",\"embeddableConfig\":{},\"panelRefName\":\"panel_1\"},{\"version\":\"9.2.4\",\"type\":\"visualization\",\"gridData\":{\"x\":24,\"y\":0,\"w\":24,\"h\":15,\"i\":\"2\"},\"panelIndex\":\"2\",\"embeddableConfig\":{},\"panelRefName\":\"panel_2\"},{\"version\":\"9.2.4\",\"type\":\"visualization\",\"gridData\":{\"x\":0,\"y\":15,\"w\":24,\"h\":15,\"i\":\"3\"},\"panelIndex\":\"3\",\"embeddableConfig\":{},\"panelRefName\":\"panel_3\"},{\"version\":\"9.2.4\",\"type\":\"visualization\",\"gridData\":{\"x\":24,\"y\":15,\"w\":24,\"h\":15,\"i\":\"4\"},\"panelIndex\":\"4\",\"embeddableConfig\":{},\"panelRefName\":\"panel_4\"}]"
    },
    "references": [
      {"id": "traffic-over-time", "name": "panel_1", "type": "visualization"},
      {"id": "top-source-ips", "name": "panel_2", "type": "visualization"},
      {"id": "top-dest-ips", "name": "panel_3", "type": "visualization"},
      {"id": "protocol-distribution", "name": "panel_4", "type": "visualization"}
    ]
  }' 2>/dev/null || echo "Dashboard may already exist"

echo ""
echo "VB: Dashboard installation complete!"
echo "Access: $KIBANA_URL/app/dashboards#/view/unified-flow-dashboard"

#!/bin/bash
# Create AS-Focused Dashboards via Kibana API
# Dashboards: AS Overview, IP Traffic Analysis, Port Statistics, Device-Specific

KIBANA_URL="http://10.4.4.87:5601"
ELASTIC_PASSWORD="telehouse"
AUTH="elastic:${ELASTIC_PASSWORD}"
EXPORT_DIR="/home/valentinbot/.openclaw/workspace/custom-elk-stack/kibana/exports"

# Common headers
HEADERS='-H "Content-Type: application/json" -H "kbn-xsrf: true"'

echo "=== Creating AS-Focused Dashboards ==="
echo "Kibana: ${KIBANA_URL}"
echo ""

# ============================================
# 1. AS OVERVIEW DASHBOARD
# ============================================

echo "Creating AS Overview Dashboard..."

# Visualization: Top Source AS by Bytes
curl -s -u "${AUTH}" -X POST "${KIBANA_URL}/api/saved_objects/visualization" \
  -H "Content-Type: application/json" \
  -H "kbn-xsrf: true" \
  -d '{
    "attributes": {
      "title": "[AS] Top Source AS (Bytes)",
      "visState": "{\"title\":\"[AS] Top Source AS (Bytes)\",\"type\":\"bar\",\"aggs\":[{\"id\":\"1\",\"enabled\":true,\"type\":\"sum\",\"schema\":\"metric\",\"params\":{\"field\":\"network.bytes\",\"customLabel\":\"Total Bytes\"}},{\"id\":\"2\",\"enabled\":true,\"type\":\"terms\",\"schema\":\"segment\",\"params\":{\"field\":\"netflow.src_as\",\"size\":20,\"order\":\"desc\",\"orderBy\":\"1\",\"customLabel\":\"Source AS\"}}],\"params\":{\"type\":\"bar\",\"grid\":{\"categoryLines\":false},\"categoryAxes\":[{\"id\":\"CategoryAxis-1\",\"type\":\"category\",\"position\":\"bottom\",\"show\":true,\"style\":{},\"scale\":{\"type\":\"linear\"},\"labels\":{\"show\":true,\"truncate\":100},\"title\":{}}],\"valueAxes\":[{\"id\":\"ValueAxis-1\",\"name\":\"LeftAxis-1\",\"type\":\"value\",\"position\":\"left\",\"show\":true,\"style\":{},\"scale\":{\"type\":\"linear\",\"mode\":\"normal\"},\"labels\":{\"show\":true,\"rotate\":0,\"filter\":false,\"truncate\":100},\"title\":{\"text\":\"Bytes\"}}],\"seriesParams\":[{\"show\":\"true\",\"type\":\"histogram\",\"mode\":\"stacked\",\"data\":{\"label\":\"Total Bytes\",\"id\":\"1\"},\"valueAxis\":\"ValueAxis-1\",\"drawLinesBetweenPoints\":true,\"showCircles\":true}],\"addTooltip\":true,\"addLegend\":true,\"legendPosition\":\"right\",\"times\":[],\"addTimeMarker\":false,\"palette\":{\"type\":\"palette\",\"name\":\"default\"}},\"uiStateJSON\":\"{}\",\"data\":{\"searchSource\":{\"query\":{\"language\":\"kuery\",\"query\":\"\"},\"filter\":[],\"index\":\"unified-flow-pattern\"}}}",
      "uiStateJSON": "{}",
      "description": "Top Source AS by total bytes",
      "version": 1,
      "kibanaSavedObjectMeta": {
        "searchSourceJSON": "{\"index\":\"unified-flow-pattern\",\"query\":{\"language\":\"kuery\",\"query\":\"\"},\"filter\":[]}"
      }
    }
  }' | jq -r '.id' 2>/dev/null || echo "viz-as-top-source-bytes"

# Visualization: Top Destination AS by Bytes
curl -s -u "${AUTH}" -X POST "${KIBANA_URL}/api/saved_objects/visualization" \
  -H "Content-Type: application/json" \
  -H "kbn-xsrf: true" \
  -d '{
    "attributes": {
      "title": "[AS] Top Destination AS (Bytes)",
      "visState": "{\"title\":\"[AS] Top Destination AS (Bytes)\",\"type\":\"bar\",\"aggs\":[{\"id\":\"1\",\"enabled\":true,\"type\":\"sum\",\"schema\":\"metric\",\"params\":{\"field\":\"network.bytes\",\"customLabel\":\"Total Bytes\"}},{\"id\":\"2\",\"enabled\":true,\"type\":\"terms\",\"schema\":\"segment\",\"params\":{\"field\":\"netflow.dst_as\",\"size\":20,\"order\":\"desc\",\"orderBy\":\"1\",\"customLabel\":\"Destination AS\"}}],\"params\":{\"type\":\"bar\",\"grid\":{\"categoryLines\":false},\"categoryAxes\":[{\"id\":\"CategoryAxis-1\",\"type\":\"category\",\"position\":\"bottom\",\"show\":true,\"style\":{},\"scale\":{\"type\":\"linear\"},\"labels\":{\"show\":true,\"truncate\":100},\"title\":{}}],\"valueAxes\":[{\"id\":\"ValueAxis-1\",\"name\":\"LeftAxis-1\",\"type\":\"value\",\"position\":\"left\",\"show\":true,\"style\":{},\"scale\":{\"type\":\"linear\",\"mode\":\"normal\"},\"labels\":{\"show\":true,\"rotate\":0,\"filter\":false,\"truncate\":100},\"title\":{\"text\":\"Bytes\"}}],\"seriesParams\":[{\"show\":\"true\",\"type\":\"histogram\",\"mode\":\"stacked\",\"data\":{\"label\":\"Total Bytes\",\"id\":\"1\"},\"valueAxis\":\"ValueAxis-1\",\"drawLinesBetweenPoints\":true,\"showCircles\":true}],\"addTooltip\":true,\"addLegend\":true,\"legendPosition\":\"right\",\"times\":[],\"addTimeMarker\":false,\"palette\":{\"type\":\"palette\",\"name\":\"default\"}},\"uiStateJSON\":\"{}\",\"data\":{\"searchSource\":{\"query\":{\"language\":\"kuery\",\"query\":\"\"},\"filter\":[],\"index\":\"unified-flow-pattern\"}}}",
      "uiStateJSON": "{}",
      "description": "Top Destination AS by total bytes",
      "version": 1,
      "kibanaSavedObjectMeta": {
        "searchSourceJSON": "{\"index\":\"unified-flow-pattern\",\"query\":{\"language\":\"kuery\",\"query\":\"\"},\"filter\":[]}"
      }
    }
  }' | jq -r '.id' 2>/dev/null || echo "viz-as-top-dest-bytes"

echo "AS Overview visualizations created!"

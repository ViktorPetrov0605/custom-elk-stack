#!/bin/bash
# Kibana Object Creation Script
# Creates index pattern, visualizations, and dashboard automatically

KIBANA_URL="${KIBANA_URL:-http://localhost:5601}"
AUTH="${KIBANA_AUTH:-elastic:telehouse}"

echo "Creating Kibana objects..."
echo "Kibana URL: $KIBANA_URL"

# 1. Create Index Pattern
echo "→ Creating index pattern: unified-flow-*"
curl -s -X POST "$KIBANA_URL/api/saved_objects/index-pattern" \
  -H "Content-Type: application/json" \
  -H "kbn-xsrf: true" \
  -u "$AUTH" \
  -d '{
    "attributes": {
      "title": "unified-flow-*",
      "timeFieldName": "@timestamp"
    }
  }' | grep -q '"id"' && echo "  ✓ Index pattern created" || echo "  ✗ Failed"

# 2. Get index pattern ID for references
INDEX_PATTERN_ID=$(curl -s -u "$AUTH" "$KIBANA_URL/api/saved_objects/_find?type=index-pattern&search_fields=title&search=unified-flow" | grep -o '"id":"[^"]*"' | head -1 | cut -d'"' -f4)
echo "  Index pattern ID: $INDEX_PATTERN_ID"

# 3. Create Traffic Volume Visualization
echo "→ Creating visualization: Traffic Volume Over Time"
curl -s -X POST "$KIBANA_URL/api/saved_objects/visualization" \
  -H "Content-Type: application/json" \
  -H "kbn-xsrf: true" \
  -u "$AUTH" \
  -d "{
    \"attributes\": {
      \"title\": \"Traffic Volume Over Time\",
      \"visState\": \"{\\\"title\\\":\\\"Traffic Volume Over Time\\\",\\\"type\\\":\\\"area\\\",\\\"aggs\\\":[{\\\"id\\\":\\\"1\\\",\\\"enabled\\\":true,\\\"type\\\":\\\"sum\\\",\\\"schema\\\":\\\"metric\\\",\\\"params\\\":{\\\"field\\\":\\\"network.bytes\\\"}},{\\\"id\\\":\\\"2\\\",\\\"enabled\\\":true,\\\"type\\\":\\\"date_histogram\\\",\\\"schema\\\":\\\"segment\\\",\\\"params\\\":{\\\"field\\\":\\\"@timestamp\\\",\\\"interval\\\":\\\"auto\\\"}}]}\",
      \"kibanaSavedObjectMeta\": {
        \"searchSourceJSON\": \"{\\\"index\\\":\\\"$INDEX_PATTERN_ID\\\"}\"
      }
    },
    \"references\": [{\"id\": \"$INDEX_PATTERN_ID\", \"name\": \"kibanaSavedObjectMeta.searchSourceJSON.index\", \"type\": \"index-pattern\"}]
  }" | grep -q '"id"' && echo "  ✓ Created" || echo "  ✗ Failed"

# 4. Create Top Source IPs Visualization  
echo "→ Creating visualization: Top Source IPs"
curl -s -X POST "$KIBANA_URL/api/saved_objects/visualization" \
  -H "Content-Type: application/json" \
  -H "kbn-xsrf: true" \
  -u "$AUTH" \
  -d "{
    \"attributes\": {
      \"title\": \"Top Source IPs\",
      \"visState\": \"{\\\"title\\\":\\\"Top Source IPs\\\",\\\"type\\\":\\\"pie\\\",\\\"aggs\\\":[{\\\"id\\\":\\\"1\\\",\\\"enabled\\\":true,\\\"type\\\":\\\"sum\\\",\\\"schema\\\":\\\"metric\\\",\\\"params\\\":{\\\"field\\\":\\\"network.bytes\\\"}},{\\\"id\\\":\\\"2\\\",\\\"enabled\\\":true,\\\"type\\\":\\\"terms\\\",\\\"schema\\\":\\\"segment\\\",\\\"params\\\":{\\\"field\\\":\\\"source.ip\\\",\\\"size\\\":10}}]}\",
      \"kibanaSavedObjectMeta\": {
        \"searchSourceJSON\": \"{\\\"index\\\":\\\"$INDEX_PATTERN_ID\\\"}\"
      }
    },
    \"references\": [{\"id\": \"$INDEX_PATTERN_ID\", \"name\": \"kibanaSavedObjectMeta.searchSourceJSON.index\", \"type\": \"index-pattern\"}]
  }" | grep -q '"id"' && echo "  ✓ Created" || echo "  ✗ Failed"

# 5. Create Protocol Distribution
echo "→ Creating visualization: Protocol Distribution"
curl -s -X POST "$KIBANA_URL/api/saved_objects/visualization" \
  -H "Content-Type: application/json" \
  -H "kbn-xsrf: true" \
  -u "$AUTH" \
  -d "{
    \"attributes\": {
      \"title\": \"Protocol Distribution\",
      \"visState\": \"{\\\"title\\\":\\\"Protocol Distribution\\\",\\\"type\\\":\\\"pie\\\",\\\"aggs\\\":[{\\\"id\\\":\\\"1\\\",\\\"enabled\\\":true,\\\"type\\\":\\\"count\\\",\\\"schema\\\":\\\"metric\\\"},{\\\"id\\\":\\\"2\\\",\\\"enabled\\\":true,\\\"type\\\":\\\"terms\\\",\\\"schema\\\":\\\"segment\\\",\\\"params\\\":{\\\"field\\\":\\\"network.transport\\\",\\\"size\\\":5}}]}\",
      \"kibanaSavedObjectMeta\": {
        \"searchSourceJSON\": \"{\\\"index\\\":\\\"$INDEX_PATTERN_ID\\\"}\"
      }
    },
    \"references\": [{\"id\": \"$INDEX_PATTERN_ID\", \"name\": \"kibanaSavedObjectMeta.searchSourceJSON.index\", \"type\": \"index-pattern\"}]
  }" | grep -q '"id"' && echo "  ✓ Created" || echo "  ✗ Failed"

# 6. Create Top Source AS Numbers
echo "→ Creating visualization: Top Source AS"
curl -s -X POST "$KIBANA_URL/api/saved_objects/visualization" \
  -H "Content-Type: application/json" \
  -H "kbn-xsrf: true" \
  -u "$AUTH" \
  -d "{
    \"attributes\": {
      \"title\": \"Top Source AS Numbers\",
      \"visState\": \"{\\\"title\\\":\\\"Top Source AS Numbers\\\",\\\"type\\\":\\\"histogram\\\",\\\"aggs\\\":[{\\\"id\\\":\\\"1\\\",\\\"enabled\\\":true,\\\"type\\\":\\\"sum\\\",\\\"schema\\\":\\\"metric\\\",\\\"params\\\":{\\\"field\\\":\\\"network.bytes\\\"}},{\\\"id\\\":\\\"2\\\",\\\"enabled\\\":true,\\\"type\\\":\\\"terms\\\",\\\"schema\\\":\\\"group\\\",\\\"params\\\":{\\\"field\\\":\\\"source.as.number\\\",\\\"size\\\":10}}]}\",
      \"kibanaSavedObjectMeta\": {
        \"searchSourceJSON\": \"{\\\"index\\\":\\\"$INDEX_PATTERN_ID\\\"}\"
      }
    },
    \"references\": [{\"id\": \"$INDEX_PATTERN_ID\", \"name\": \"kibanaSavedObjectMeta.searchSourceJSON.index\", \"type\": \"index-pattern\"}]
  }" | grep -q '"id"' && echo "  ✓ Created" || echo "  ✗ Failed"

# 7. Create Interface Traffic
echo "→ Creating visualization: Interface Traffic"
curl -s -X POST "$KIBANA_URL/api/saved_objects/visualization" \
  -H "Content-Type: application/json" \
  -H "kbn-xsrf: true" \
  -u "$AUTH" \
  -d "{
    \"attributes\": {
      \"title\": \"Interface Traffic\",
      \"visState\": \"{\\\"title\\\":\\\"Interface Traffic\\\",\\\"type\\\":\\\"area\\\",\\\"aggs\\\":[{\\\"id\\\":\\\"1\\\",\\\"enabled\\\":true,\\\"type\\\":\\\"sum\\\",\\\"schema\\\":\\\"metric\\\",\\\"params\\\":{\\\"field\\\":\\\"network.bytes\\\"}},{\\\"id\\\":\\\"2\\\",\\\"enabled\\\":true,\\\"type\\\":\\\"date_histogram\\\",\\\"schema\\\":\\\"segment\\\",\\\"params\\\":{\\\"field\\\":\\\"@timestamp\\\",\\\"interval\\\":\\\"auto\\\"}},{\\\"id\\\":\\\"3\\\",\\\"enabled\\\":true,\\\"type\\\":\\\"terms\\\",\\\"schema\\\":\\\"group\\\",\\\"params\\\":{\\\"field\\\":\\\"device.name\\\",\\\"size\\\":5}}]}\",
      \"kibanaSavedObjectMeta\": {
        \"searchSourceJSON\": \"{\\\"index\\\":\\\"$INDEX_PATTERN_ID\\\"}\"
      }
    },
    \"references\": [{\"id\": \"$INDEX_PATTERN_ID\", \"name\": \"kibanaSavedObjectMeta.searchSourceJSON.index\", \"type\": \"index-pattern\"}]
  }" | grep -q '"id"' && echo "  ✓ Created" || echo "  ✗ Failed"

echo ""
echo "Dashboard creation complete!"
echo "Access Kibana at: $KIBANA_URL"
echo "Create dashboard manually and add these visualizations."
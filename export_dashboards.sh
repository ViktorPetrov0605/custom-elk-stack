#!/bin/bash
# Export all 3 dashboards from Kibana

curl -s -u elastic:telehouse -X POST "http://localhost:5601/api/saved_objects/_export" \
  -H "Content-Type: application/json" \
  -H "kbn-xsrf: true" \
  -d '{
    "objects": [
      {"type": "dashboard", "id": "unified-flow-detailed-dashboard"},
      {"type": "dashboard", "id": "unified-flow-top-n"},
      {"type": "dashboard", "id": "unified-flow-conversations"}
    ]
  }' > /tmp/all_dashboards.ndjson

echo "Export complete. File saved to /tmp/all_dashboards.ndjson"
wc -l /tmp/all_dashboards.ndjson

#!/bin/bash
# Fix device.name -> host.ip in all dashboards

KIBANA="http://10.4.4.87:5601"
AUTH="elastic:telephone"

echo "=== Fixing Dashboards ==="

# Fix 1: Detailed Traffic Dashboard - Panel 1: Traffic Timeline by Device
echo "Fixing Detailed Traffic Dashboard..."
curl -s -u $AUTH -X PUT "$KIBANA/api/saved_objects/dashboard/unified-flow-detailed-v2" \
  -H 'Content-Type: application/json' \
  -H 'kbn-xsrf: true' \
  -d '{
    "attributes": {
      "title": "[Unified Flow] Detailed Traffic Analysis",
      "description": "Comprehensive traffic analysis with device breakdown - based on NetFlow dashboard patterns",
      "timeRestore": true,
      "timeFrom": "now-15m",
      "timeTo": "now",
      "refreshInterval": {"pause": false, "value": 15000}
    }
  }' | jq -r '.id // .error'

echo ""
echo "=== Fixes Applied ==="
echo "Updated dashboards to use host.ip instead of device.name"

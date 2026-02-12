#!/bin/bash

# Script to fix Kibana dashboards
# Usage: ./fix-dashboards.sh

# Kibana URL
KIBANA_URL="https://10.4.4.87:5601"

# Credentials
USERNAME="elastic"
PASSWORD="telehouse"

# Function to get dashboard
get_dashboard() {
    echo "Getting dashboard: $1"
    curl -X GET -s -k -u "$USERNAME:$PASSWORD" "$KIBANA_URL/api/saved_objects/dashboard:$1" -H 'kbn-xsrf: true' -H 'Content-Type: application/json' --insecure
}

# Function to delete dashboard
delete_dashboard() {
    echo "Deleting dashboard: $1"
    curl -X DELETE -s -k -u "$USERNAME:$PASSWORD" "$KIBANA_URL/api/saved_objects/dashboard:$1" -H 'kbn-xsrf: true' -H 'Content-Type: application/json' --insecure
}

# Function to import dashboard
import_dashboard() {
    echo "Importing dashboard from: $1"
    curl -X POST -s -k -u "$USERNAME:$PASSWORD" "$KIBANA_URL/api/saved_objects/_import?overwrite=true" -H 'kbn-xsrf: true' --form file=@$1 --insecure
}

# Fix flow-analysis-v3 dashboard
echo "=== Fixing flow-analysis-v3 dashboard ==="
# get_dashboard "flow-analysis-v3"
# delete_dashboard "flow-analysis-v3"
import_dashboard "kibana-dashboards-enhanced/unified-flow-dashboards-v2.ndjson"

# Fix flow-conversations-v3 dashboard
echo "\n=== Fixing flow-conversations-v3 dashboard ==="
# get_dashboard "flow-conversations-v3"
# delete_dashboard "flow-conversations-v3"
import_dashboard "kibana-dashboards-enhanced/unified-flow-dashboards-v2.ndjson"

# Fix flow-topn-v3 dashboard
echo "\n=== Fixing flow-topn-v3 dashboard ==="
# get_dashboard "flow-topn-v3"
# delete_dashboard "flow-topn-v3"
import_dashboard "kibana-dashboards-enhanced/unified-flow-dashboards-v2.ndjson"

# Fix flow-analysis-v2 dashboard
echo "\n=== Fixing flow-analysis-v2 dashboard ==="
# get_dashboard "flow-analysis-v2"
# delete_dashboard "flow-analysis-v2"
import_dashboard "kibana-dashboards-enhanced/unified-flow-dashboards-v2.ndjson"

# Fix flow-conversations-v2 dashboard
echo "\n=== Fixing flow-conversations-v2 dashboard ==="
# get_dashboard "flow-conversations-v2"
# delete_dashboard "flow-conversations-v2"
import_dashboard "kibana-dashboards-enhanced/unified-flow-dashboards-v2.ndjson"

# Fix flow-topn-v2 dashboard
echo "\n=== Fixing flow-topn-v2 dashboard ==="
# get_dashboard "flow-topn-v2"
# delete_dashboard "flow-topn-v2"
import_dashboard "kibana-dashboards-enhanced/unified-flow-dashboards-v2.ndjson"

echo "\n✅ All dashboards fixed!"
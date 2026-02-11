#!/bin/bash
# Unified Flow Dashboards Import Script
# This script imports the unified-flow-* dashboards into Kibana

set -e

KIBANA_URL="${KIBANA_URL:-http://localhost:5601}"
KIBANA_USER="${KIBANA_USER:-elastic}"
KIBANA_PASS="${KIBANA_PASS:-changeme}"
NDJSON_FILE="${1:-unified-flow-dashboards-combined.ndjson}"

echo "=========================================="
echo "Unified Flow Dashboards Import Tool"
echo "=========================================="
echo "Target Kibana: $KIBANA_URL"
echo "Import file: $NDJSON_FILE"
echo ""

# Check if file exists
if [ ! -f "$NDJSON_FILE" ]; then
    echo "ERROR: File not found: $NDJSON_FILE"
    echo "Available files in current directory:"
    ls -la *.ndjson 2>/dev/null || echo "No .ndjson files found"
    exit 1
fi

# Test Kibana connectivity
echo "Testing Kibana connectivity..."
if curl -s -u "$KIBANA_USER:$KIBANA_PASS" "$KIBANA_URL/api/status" > /dev/null 2>&1; then
    echo "✓ Kibana is accessible"
else
    echo "ERROR: Cannot connect to Kibana at $KIBANA_URL"
    echo "Please check:"
    echo "  - Kibana is running"
    echo "  - Credentials are correct (KIBANA_USER/KIBANA_PASS)"
    echo "  - URL is correct (KIBANA_URL)"
    exit 1
fi

# Check for unified-flow-* index pattern
echo ""
echo "Checking for unified-flow-* index pattern..."
INDEX_PATTERN_CHECK=$(curl -s -u "$KIBANA_USER:$KIBANA_PASS" \
    "$KIBANA_URL/api/saved_objects/index-pattern/unified-flow-*" \
    -H "kbn-xsrf: true" 2>/dev/null | grep -c '"id":"unified-flow-\*"' || true)

if [ "$INDEX_PATTERN_CHECK" -eq 0 ]; then
    echo "⚠ WARNING: unified-flow-* index pattern not found in Kibana"
    echo "  Please create the index pattern before importing dashboards"
    echo "  Or run the create-index-pattern.sh script first"
    read -p "Continue anyway? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
else
    echo "✓ unified-flow-* index pattern exists"
fi

# Import the dashboards
echo ""
echo "Importing dashboards..."
IMPORT_RESULT=$(curl -s -u "$KIBANA_USER:$KIBANA_PASS" \
    -X POST "$KIBANA_URL/api/saved_objects/_import?overwrite=true" \
    -H "kbn-xsrf: true" \
    --form "file=@$NDJSON_FILE" 2>&1)

# Check import result
if echo "$IMPORT_RESULT" | grep -q '"success":true'; then
    IMPORTED_COUNT=$(echo "$IMPORT_RESULT" | grep -o '"successCount":[0-9]*' | cut -d: -f2)
    echo "✓ Successfully imported $IMPORTED_COUNT saved objects"
    echo ""
    echo "Imported dashboards:"
    echo "  1. [Unified Flow] Detailed Traffic Analysis"
    echo "  2. [Unified Flow] Top-N Analysis"
    echo "  3. [Unified Flow] Conversation Partners"
    echo ""
    echo "View dashboards at: $KIBANA_URL/app/dashboards"
else
    echo "ERROR: Import failed"
    echo "Response:"
    echo "$IMPORT_RESULT" | python3 -m json.tool 2>/dev/null || echo "$IMPORT_RESULT"
    exit 1
fi

echo ""
echo "=========================================="
echo "Import complete!"
echo "=========================================="

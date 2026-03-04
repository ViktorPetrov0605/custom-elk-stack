#!/bin/bash
#
# ELK Stack Deployment Validation Script
# Validates ILM policy, index template, dashboards, and index status
#

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONFIG_FILE="${SCRIPT_DIR}/../deploy.conf"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

log_pass() { echo -e "${GREEN}✓ PASS${NC} $1"; }
log_fail() { echo -e "${RED}✗ FAIL${NC} $1"; }
log_info() { echo -e "${BLUE}ℹ INFO${NC} $1"; }

# Load configuration
if [ ! -f "$CONFIG_FILE" ]; then
    echo -e "${RED}ERROR:${NC} Config file not found: $CONFIG_FILE"
    echo "Run './deploy.sh --generate' first or ensure deploy.conf exists"
    exit 1
fi

source "$CONFIG_FILE"

ES_URL="https://localhost:${ES_PORT:-9200}"
KIBANA_URL="http://localhost:${KIBANA_PORT:-5601}"
ES_AUTH="elastic:${ELASTIC_PASSWORD}"

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}ELK Stack Deployment Validation${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

# =============================================================================
# 1. ILM Policy Check (5GB Rollover)
# =============================================================================
echo -e "${YELLOW}1. Checking ILM Policy...${NC}"

ROLLOVER_SIZE=$(curl -k -s -u "$ES_AUTH" "$ES_URL/_ilm/policy/logstash-flow-policy?pretty" 2>/dev/null | grep -o '"max_primary_shard_size"[[:space:]]*:[[:space:]]*"[^"]*"' | cut -d'"' -f4)

if [ "$ROLLOVER_SIZE" = "5gb" ]; then
    log_pass "ILM rollover: $ROLLOVER_SIZE (2 shards × 5GB = 10GB per index)"
else
    log_fail "ILM rollover: Expected '5gb', got '$ROLLOVER_SIZE'"
fi

# =============================================================================
# 2. Index Template Check (2 Shards, 0 Replicas)
# =============================================================================
echo -e "${YELLOW}2. Checking Index Template...${NC}"

SHARDS=$(curl -k -s -u "$ES_AUTH" "$ES_URL/_index_template/logstash-flow?pretty" 2>/dev/null | grep -o '"number_of_shards"[[:space:]]*:[[:space:]]*"[^"]*"' | cut -d'"' -f4)
REPLICAS=$(curl -k -s -u "$ES_AUTH" "$ES_URL/_index_template/logstash-flow?pretty" 2>/dev/null | grep -o '"number_of_replicas"[[:space:]]*:[[:space:]]*"[^"]*"' | cut -d'"' -f4)

if [ "$SHARDS" = "2" ] && [ "$REPLICAS" = "0" ]; then
    log_pass "Index template: $SHARDS shards, $REPLICAS replicas"
else
    log_fail "Index template: Expected 2/0, got $SHARDS/$REPLICAS"
fi

# =============================================================================
# 3. Dashboard Import Check
# =============================================================================
echo -e "${YELLOW}3. Checking Dashboard Import...${NC}"

DASHBOARDS=$(curl -k -s -u "$ES_AUTH" "$KIBANA_URL/api/saved_objects/_find?type=dashboard&fields=title&per_page=100" -H "kbn-xsrf: true" 2>/dev/null | \
    python3 -c "import sys,json; d=json.load(sys.stdin); print('\n'.join([s['attributes']['title'] for s in d.get('saved_objects',[]) if 'Flow' in s['attributes'].get('title','')]))" 2>/dev/null || echo "")

DASH_COUNT=$(echo "$DASHBOARDS" | grep -c "Unified Flow" 2>/dev/null || echo "0")

if [ "$DASH_COUNT" -ge 3 ]; then
    log_pass "Found $DASH_COUNT Unified Flow dashboards:"
    echo "$DASHBOARDS" | while read -r line; do
        [ -n "$line" ] && echo "      - $line"
    done
else
    log_fail "Expected 3 dashboards, found $DASH_COUNT"
    echo "$DASHBOARDS" | head -5
fi

# =============================================================================
# 4. ILM Management Status on Indices
# =============================================================================
echo -e "${YELLOW}4. Checking ILM Status on Indices...${NC}"

MANAGED_COUNT=$(curl -k -s -u "$ES_AUTH" "$ES_URL/logstash-flow-*/_ilm/explain" 2>/dev/null | grep -o '"managed":true' | wc -l | tr -d '[:space:]')

if [ "$MANAGED_COUNT" -gt 0 ] 2>/dev/null; then
    log_pass "$MANAGED_COUNT indices managed by ILM"
else
    log_fail "No indices found with ILM management"
fi

# =============================================================================
# 5. Index Pattern with Device Lookup
# =============================================================================
echo -e "${YELLOW}5. Checking Device Lookup Configuration...${NC}"

LOOKUP_CONFIG=$(curl -k -s -u "$ES_AUTH" "$ES_URL/.kibana/_doc/index-pattern:unified-flow-pattern?pretty" 2>/dev/null | grep -o '"static_lookup"' | head -1)

if [ -n "$LOOKUP_CONFIG" ]; then
    log_pass "Device static lookup formatter configured"
else
    log_info "Device lookup not configured (optional - edit dashboards/device-lookup.json and re-import)"
fi

# =============================================================================
# 6. Current Index Sizes
# =============================================================================
echo -e "${YELLOW}6. Current Index Sizes...${NC}"

curl -k -s -u "$ES_AUTH" "$ES_URL/_cat/indices/logstash-flow-*?v&s=index" 2>/dev/null | \
    awk 'NR==1 {print} NR>1 {printf "  %s  %s  %s\n", $1, $3, $5}' || \
    log_info "No indices found yet"

echo ""
echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}Validation Complete${NC}"
echo -e "${BLUE}========================================${NC}"

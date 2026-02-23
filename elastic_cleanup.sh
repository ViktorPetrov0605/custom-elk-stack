#!/bin/bash
ELASTIC_USER="elastic"
ELASTIC_PASS="telehouse"
ELASTIC_URL="https://localhost:9200"

# Get indexes, sort by creation date (cat indices doesn't give date, so we use _settings)
# Actually 'cat indices' gives name, we can sort by name if they are dated-based.
# Flow indexes are usually named like 'flow-netflow-2026.02.23'

log() { echo "$(date '+%Y-%m-%d %H:%M:%S') $1"; }

# 1. Check index count
INDEX_COUNT=$(curl -k -s -u $ELASTIC_USER:$ELASTIC_PASS "$ELASTIC_URL/_cat/indices/flow-*?h=index" | wc -l)

if [ "$INDEX_COUNT" -gt 10 ]; then
    log "Found $INDEX_COUNT flow indexes. Checking for deletion candidates..."
    
    # Get all flow indexes with size, sorted by name (date-based)
    # flow-netflow-2026.02.18 10.2gb
    # flow-netflow-2026.02.19 5.5gb
    
    # We want the oldest one that is > 10GB? User said "deletes the oldest 10gb index if there are more than 10"
    # Interpreting as: If > 10 indexes, find oldest one. If it's > 10GB, delete it.
    
    # Get oldest index name
    OLDEST_INDEX=$(curl -k -s -u $ELASTIC_USER:$ELASTIC_PASS "$ELASTIC_URL/_cat/indices/flow-*?s=index&h=index" | head -n 1)
    
    # Get its size in bytes
    SIZE_BYTES=$(curl -k -s -u $ELASTIC_USER:$ELASTIC_PASS "$ELASTIC_URL/_cat/indices/$OLDEST_INDEX?h=pri.store.size&bytes=b")
    
    TEN_GB=10737418240
    
    if [ "$SIZE_BYTES" -gt "$TEN_GB" ]; then
        log "Deleting oldest index $OLDEST_INDEX (Size: $SIZE_BYTES bytes > 10GB)..."
        curl -k -s -u $ELASTIC_USER:$ELASTIC_PASS -X DELETE "$ELASTIC_URL/$OLDEST_INDEX"
    else
        log "Oldest index $OLDEST_INDEX is only $SIZE_BYTES bytes. Skipping deletion."
    fi
else
    log "Only $INDEX_COUNT flow indexes found. No action needed."
fi

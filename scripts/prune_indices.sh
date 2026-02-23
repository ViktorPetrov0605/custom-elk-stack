#!/bin/bash
ELASTIC_USER=${1:-"elastic"}
ELASTIC_PASS=${2:-"telehouse"}
ELASTIC_URL="https://localhost:9200"
PATTERN="logstash-flow-*"
MAX_INDEXES=10

log() { echo "$(date '+%Y-%m-%d %H:%M:%S') $1"; }

# Get all indexes matching pattern, sorted by creation date (using _cat/indices/s=index sorts alphanumeric, which works for sequential names)
INDEX_LIST=$(curl -k -s -u $ELASTIC_USER:$ELASTIC_PASS "$ELASTIC_URL/_cat/indices/$PATTERN?s=index&h=index")
INDEX_COUNT=$(echo "$INDEX_LIST" | grep -v '^$' | wc -l)

if [ "$INDEX_COUNT" -gt "$MAX_INDEXES" ]; then
    log "Found $INDEX_COUNT indexes. Keeping max $MAX_INDEXES. Deleting oldest..."
    
    # Calculate how many to delete
    TO_DELETE_COUNT=$(($INDEX_COUNT - $MAX_INDEXES))
    
    # Get the names of the oldest N indexes
    TO_DELETE_NAMES=$(echo "$INDEX_LIST" | head -n $TO_DELETE_COUNT)
    
    for idx in $TO_DELETE_NAMES; do
        log "Deleting index: $idx"
        curl -k -s -u $ELASTIC_USER:$ELASTIC_PASS -X DELETE "$ELASTIC_URL/$idx"
    done
else
    log "Total indexes: $INDEX_COUNT. No cleanup needed."
fi

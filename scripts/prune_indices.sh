#!/bin/bash
# 
# Keep only the N newest logstash-flow indices to protect disk space.
# Uses serial index naming established for Unified Pipeline.
#

KEEP_COUNT=10
ES_URL="https://10.4.4.87:9200"
USER_AUTH="elastic:telehouse"

# Get list of indices, sort them naturally, take all except the last N
indices_to_delete=$(curl -s -k -u "$USER_AUTH" "$ES_URL/_cat/indices/logstash-flow-*?h=index&s=index" | head -n -$KEEP_COUNT)

if [ -z "$indices_to_delete" ]; then
    echo "$(date): No indices to prune. (Count <= $KEEP_COUNT)"
    exit 0
fi

for idx in $indices_to_delete; do
    echo "$(date): Deleting old index: $idx"
    curl -s -k -u "$USER_AUTH" -X DELETE "$ES_URL/$idx"
done

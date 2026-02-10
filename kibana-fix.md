# Kibana "unavailable" Status Fix

## Problem
Kibana at 10.4.4.87:5601 was returning `{"status":{"overall":{"level":"unavailable"}}}`

## Root Cause
Frontend Elasticsearch nodes (`es-frontend` and `es-frontend-2`) had incorrect node roles:
- **Before:** `node.roles=master` (only master role)
- **Required:** `node.roles=master,data,ingest` (master + data + ingest roles)

Without the `data` role, the frontend ES nodes could not access the `.security-7` index, which is required for Kibana authentication.

## Diagnosis Commands Used

```bash
# Check ES cluster health and node roles
curl -k -u elastic:$ELASTIC_PASSWORD https://10.4.4.87:9200/_cat/nodes?v

# Output showed:
# ip        heap.percent ram.percent cpu load_1m load_5m load_15m node.role master name
# 10.4.4.87           18          68   1    0.04    0.03     0.03 im        -      es-frontend-2
# 10.4.4.90           46          95  15    0.23    0.85     1.21 di        -      es-remote
# 10.4.4.87            9          70   1    0.04    0.03     0.03 im        *      es-frontend
# 10.4.4.21           55         100  16    0.83    0.98     1.45 di        -      es-remote
#
# PROBLEM: Both frontend nodes show "im" (ingest+master) but NOT "data" role

# Check .security index exists
curl -k -u elastic:$ELASTIC_PASSWORD https://10.4.4.87:9200/_cat/indices/.security*?v

# Output confirmed .security-7 index exists and is green

# Check Kibana status
curl -s http://10.4.4.87:5601/api/status
```

## Fix Applied to docker-compose-frontend.yml

### Change 1: es-frontend service
```yaml
# BEFORE:
      - node.roles=master
      - node.attr.node_type=master_only

# AFTER:
      - node.roles=master,data,ingest
      - node.attr.node_type=frontend
```

### Change 2: es-frontend-2 service
```yaml
# BEFORE:
      - node.roles=master
      - node.attr.node_type=master_only

# AFTER:
      - node.roles=master,data,ingest
      - node.attr.node_type=frontend
```

## Deployment Steps (Run on 10.4.4.87)

```bash
# 1. SSH to frontend server
ssh $USER@10.4.4.87
cd /opt/netflow

# 2. Stop ES containers (keep Kibana running for now)
docker-compose -f docker-compose-frontend.yml stop es-frontend es-frontend-2

# 3. Apply the fixed docker-compose-frontend.yml
cp docker-compose-frontend.yml docker-compose-frontend.yml.backup
curl -o docker-compose-frontend.yml [URL_TO_FIXED_FILE_OR_MANUAL_EDIT]

# 4. Recreate ES containers with new roles
docker-compose -f docker-compose-frontend.yml up -d es-frontend es-frontend-2

# 5. Verify nodes now have data role
curl -k -u elastic:$ELASTIC_PASSWORD https://10.4.4.87:9200/_cat/nodes?v
# Should show "dim" (data+ingest+master) instead of "im"

# 6. Restart Kibana to reconnect
docker-compose -f docker-compose-frontend.yml restart kibana

# 7. Wait for Kibana to becomec available (can take 1-2 minutes)
sleep 60

# 8. Verify Kibana is now available
curl -s http://10.4.4.87:5601/api/status | grep -o '"level":"[^"]*"'
# Expected: "level":"available"
```

## Verification

Success = `curl http://10.4.4.87:5601/api/status` returns:
```json
{"status":{"overall":{"level":"available"}}}
```

## Node Roles Reference

| Role | Letter | Purpose |
|------|--------|---------|
| master | m | Can be elected master |
| data | d | Stores data shards |
| ingest | i | Can run ingest pipelines |
| remote_cluster_client | r | Can connect to remote clusters |

Frontend nodes need `dim` (data+ingest+master) to:
1. Store the `.security` index locally (data role)
2. Run ingest pipelines for NetFlow (ingest role)
3. Participate in master election (master role)

## Related Files

- `docker-compose-frontend.yml` - Fixed configuration
- `.env` - Must contain `KIBANA_PASSWORD` matching `ELASTIC_PASSWORD` or setup container's set password
- `kibana/kibana.yml` - If using custom Kibana config

## Notes

- The `node.attr.node_type` was also updated from `master_only` to `frontend` for clarity
- After adding `data` role, ES may need to relocate some shards to the frontend nodes
- The .security index should automatically become available to frontend nodes after they gain data role
- If authentication still fails, re-run the setup container to reset kibana_system password:
  ```bash
  docker-compose -f docker-compose-frontend.yml run --rm setup
  ```

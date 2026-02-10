# Backend N1 Elasticsearch Restart Report

**Date:** 2026-02-10
**Server:** Backend N1 (10.4.4.21:2332)
**Task:** Restart ES and join netflow-cluster

## Summary

**Status: ⚠️ ISSUE IDENTIFIED - Cluster UUID Mismatch**

The Elasticsearch node (es-remote) on Backend N1 encountered a critical cluster UUID mismatch that prevents it from joining the netflow-cluster.

## Steps Completed

1. ✅ **SSH to 10.4.4.21:2332** - Successfully logged in as telehouse
2. ✅ **Located docker-compose** - Found at `~/custom-elk-stack/docker-compose-backend.yml`
3. ✅ **Stopped containers** - Executed `docker-compose -f docker-compose-backend.yml down`
4. ✅ **Started containers** - Executed `docker-compose -f docker-compose-backend.yml up -d`
5. ⚠️ **ES Startup Issue** - Node started but failed to join cluster

## Critical Issue Found

The ES logs show a `CoordinationStateRejectedException`:

```
This node previously joined a cluster with UUID [8Gix5T7VRyuyFHyXVwsHyg] 
and is now trying to join a different cluster with UUID [GIJOoEyDRDCC_qQCPbg23Q].
```

**Error Details:**
- The es-remote node has persistent cluster state data from a previous cluster (UUID: 8Gix5T7VRyuyFHyXVwsHyg)
- The frontend cluster (es-frontend at 10.4.4.87) expects a different cluster UUID (GIJOoEyDRDCC_qQCPbg23Q)
- ES prevents joining different clusters to protect data integrity

## Required Action

To resolve this issue, the node's data directory must be cleared. According to the ES documentation and the error message:

> "Note that the cluster UUID persists across restarts and can only be changed 
> by deleting the contents of the node's data paths [] which will also remove 
> any data held by this node."

### Manual Fix Required:

```bash
# SSH to the server
ssh -p 2332 telehouse@10.4.4.21

# Navigate to compose directory
cd ~/custom-elk-stack

# Stop containers
docker-compose -f docker-compose-backend.yml down

# Clear ES data volume (IMPORTANT: This will remove any data on this node)
docker volume rm custom-elk-stack_es-data
# OR if using bind mounts:
# sudo rm -rf /path/to/es/data/*

# Restart containers
docker-compose -f docker-compose-backend.yml up -d

# Verify cluster membership from frontend
curl -k -u elastic:telehouse https://10.4.4.87:9200/_cat/nodes
```

## Observations

1. The containers started successfully after restart
2. The node publishes to address `10.4.4.21:9200` correctly
3. The cluster discovery configuration is working (discovers es-frontend and es-frontend-2)
4. Only the UUID mismatch prevents cluster join

## Cluster Status

**Before Fix:**
- es-remote is running but NOT joined to netflow-cluster
- Cannot verify cluster membership from frontend

**After Fix (expected):**
- es-remote should join the netflow-cluster
- curl to frontend should show es-remote with IP 10.4.4.21
- Backend N1 indices should be visible from frontend

---
**Note:** This issue may have occurred if the frontend cluster was recreated/reinitialized with a new cluster UUID, or if the backend node had stale data from a previous cluster configuration.

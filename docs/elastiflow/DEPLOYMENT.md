# ElastiFlow Unified Collector Deployment

**Date:** 2026-02-12  
**Deployed by:** Valentin-bot  
**Status:** ✅ Production  
**Version:** v1.2 (3-day retention, 1 shard, runtime fields)

## Architecture

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   Juniper SW    │     │  Cisco Nexus 1  │     │  Cisco Nexus 2  │
│   10.4.4.93     │     │    10.4.4.3     │     │    10.4.4.4     │
│   NetFlow v9    │     │    sFlow v5     │     │    sFlow v5     │
└────────┬────────┘     └────────┬────────┘     └────────┬────────┘
         │                       │                       │
         │ UDP 2050              │ UDP 6343              │ UDP 6343
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────────────────────────────────────────────────────┐
│                     Backend N1 (10.4.4.21)                       │
│              ElastiFlow Collector (NetFlow only)                 │
│                      Port: 2050 (host mode)                      │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │
┌─────────────────────────────────────────────────────────────────┐
│                     Backend N2 (10.4.4.90)                       │
│              ElastiFlow Collector (sFlow only)                   │
│                      Port: 6343 (host mode)                      │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ HTTP/HTTPS 9200
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│              Elasticsearch Cluster (10.4.4.87:9200)              │
│                    Index: elastiflow-flow-ecs-*                  │
│                    Shards: 1 | Replicas: 0 | Retention: 3 days   │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    Kibana (10.4.4.87:5601)                       │
│              Unified Flow Dashboards & Analytics                 │
└─────────────────────────────────────────────────────────────────┘
```

## Quick Stats

| Metric | Value |
|--------|-------|
| **Total Flow Records** | 2.8M+ |
| **NetFlow (Juniper)** | 864K+ docs |
| **sFlow (Cisco)** | 1.48M+ docs |
| **Index Size** | ~3GB |
| **Devices** | 3 active |
| **Shards** | 1 per index |
| **Replicas** | 0 |
| **Retention** | 3 days |

## Collectors

### Backend N1 - NetFlow Collector
- **IP:** 10.4.4.21
- **SSH:** Port 2332 (NOT standard 22!)
- **Purpose:** Receives NetFlow v9 from Juniper (10.4.4.93)
- **Port:** 2050/UDP
- **Docker Compose:** `~/elastiflow/docker-compose.yml`

### Backend N2 - sFlow Collector  
- **IP:** 10.4.4.90
- **SSH:** Port 22
- **Purpose:** Receives sFlow v5 from Cisco Nexus (10.4.4.3, 10.4.4.4)
- **Port:** 6343/UDP
- **Docker Compose:** `~/elastiflow/docker-compose.yml`

## Docker Compose Files

### Backend N1: `docker-compose.yml` (~/elastiflow/)
```yaml
version: '2'
services:
  flow-collector:
    image: elastiflow/flow-collector:7.21.0
    container_name: flow-collector
    restart: unless-stopped
    network_mode: host
    environment:
      EF_LICENSE_ACCEPTED: "true"
      EF_FLOW_SERVER_UDP_IP: "0.0.0.0"
      EF_FLOW_SERVER_UDP_PORT: "2050"
      EF_PROCESSOR_DECODE_NETFLOW9_ENABLE: "true"
      EF_PROCESSOR_DECODE_ENRICH_IP_LOOKUP_ENABLED: "true"
      EF_OUTPUT_ELASTICSEARCH_ENABLE: "true"
      EF_OUTPUT_ELASTICSEARCH_ADDRESSES: "10.4.4.87:9200"
      EF_OUTPUT_ELASTICSEARCH_USERNAME: "elastic"
      EF_OUTPUT_ELASTICSEARCH_PASSWORD: "telehouse"
      EF_OUTPUT_ELASTICSEARCH_INDEX_TEMPLATE_ENABLE: "true"
      EF_OUTPUT_ELASTICSEARCH_INDEX_TEMPLATE_SHARDS: "1"
      EF_OUTPUT_ELASTICSEARCH_INDEX_TEMPLATE_REPLICAS: "0"
      EF_OUTPUT_ELASTICSEARCH_ECS_ENABLE: "true"
      EF_OUTPUT_ELASTICSEARCH_TLS_ENABLE: "true"
      EF_OUTPUT_ELASTICSEARCH_TLS_SKIP_VERIFICATION: "true"
      EF_PIPELINE_WORKERS: "2"
      EF_PIPELINE_BATCH_SIZE: "1000"
```

### Backend N2: `docker-compose.yml` (~/elastiflow/)
```yaml
version: '2'
services:
  flow-collector:
    image: elastiflow/flow-collector:7.21.0
    container_name: flow-collector
    restart: unless-stopped
    network_mode: host
    environment:
      EF_LICENSE_ACCEPTED: "true"
      EF_FLOW_SERVER_UDP_IP: "0.0.0.0"
      EF_FLOW_SERVER_UDP_PORT: "6343"
      EF_PROCESSOR_DECODE_SFLOW5_ENABLE: "true"
      EF_PROCESSOR_DECODE_SFLOW_FLOWS_ENABLE: "true"
      EF_PROCESSOR_DECODE_ENRICH_IP_LOOKUP_ENABLED: "true"
      EF_OUTPUT_ELASTICSEARCH_ENABLE: "true"
      EF_OUTPUT_ELASTICSEARCH_ADDRESSES: "10.4.4.87:9200"
      EF_OUTPUT_ELASTICSEARCH_USERNAME: "elastic"
      EF_OUTPUT_ELASTICSEARCH_PASSWORD: "telehouse"
      EF_OUTPUT_ELASTICSEARCH_INDEX_TEMPLATE_ENABLE: "true"
      EF_OUTPUT_ELASTICSEARCH_INDEX_TEMPLATE_SHARDS: "1"
      EF_OUTPUT_ELASTICSEARCH_INDEX_TEMPLATE_REPLICAS: "0"
      EF_OUTPUT_ELASTICSEARCH_ECS_ENABLE: "true"
      EF_OUTPUT_ELASTICSEARCH_TLS_ENABLE: "true"
      EF_OUTPUT_ELASTICSEARCH_TLS_SKIP_VERIFICATION: "true"
      EF_PIPELINE_WORKERS: "2"
      EF_PIPELINE_BATCH_SIZE: "1000"
```

## Index Lifecycle Management (ILM) v1.2

**Policy:** `elastiflow`

| Phase | Trigger | Action |
|-------|---------|--------|
| **Hot** | 0-1 days OR 10GB | Active indexing, rollover |
| **Warm** | Immediately after rollover | Shrink to 1 shard, 0 replicas, forcemerge |
| **Delete** | **3 days total** | Index removed |

**Key Changes:**
- Reduced from 365 days → **3 days** retention
- 1 shard per index (was 2)
- 0 replicas per index (was 1)
- Rollover triggers every 1 day or 10GB

### Update Index Settings
```bash
# Update ILM policy
curl -u elastic:telehouse -k -X PUT "https://10.4.4.87:9200/_ilm/policy/elastiflow" \
  -H 'Content-Type: application/json' \
  -d '{"policy":{"phases":{"hot":{"min_age":"0ms","actions":{"rollover":{"max_age":"1d","max_primary_shard_size":"10gb"},"set_priority":{"priority":100}},"warm":{"min_age":"0d","actions":{"forcemerge":{"max_num_segments":1},"set_priority":{"priority":50},"shrink":{"number_of_shards":1,"allow_write_after_shrink":false},"allocate":{"number_of_replicas":0}}},"delete":{"min_age":"3d","actions":{"delete":{}}}}}}'

# Update index template for 1 shard, 0 replicas
curl -u elastic:telehouse -k -X PUT "https://10.4.4.87:9200/_index_template/elastiflow-flow-ecs-8.0-2.5" \
  -H 'Content-Type: application/json' \
  -d '{"index_patterns":["elastiflow-flow-ecs-8.0-2.5-*"],"template":{"settings":{"number_of_shards":1,"number_of_replicas":0,"index.lifecycle.name":"elastiflow","index.lifecycle.rollover_alias":"elastiflow-flow-ecs-8.0-2.5-rollover","index.codec":"best_compression","refresh_interval":"20s"}},"priority":500}'

# Force rollover to apply new settings
curl -u elastic:telehouse -k -X POST "https://10.4.4.87:9200/elastiflow-flow-ecs-8.0-2.5-rollover/_rollover"
```

## Field Reference for Filtering

| Field | Description | Example Values |
|-------|-------------|----------------|
| `host.ip` | Flow exporter IP (**use this!**) | `10.4.4.93`, `10.4.4.3`, `10.4.4.4` |
| `host.name` | Flow exporter hostname | IP or hostname |
| `event.dataset` | Flow type | `netflow`, `sflow` |
| `source.ip` | Source of traffic | Any IP |
| `destination.ip` | Destination of traffic | Any IP |
| `@timestamp` | Event time | ISO timestamp |
| `network.protocol` | Protocol | `tcp`, `udp`, `icmp` |
| `source.port` | Source port | 80, 443, etc. |
| `destination.port` | Dest port | 80, 443, etc. |

### Kibana Quick Filters

| Filter | Search Query |
|--------|--------------|
| **Juniper only** | `host.ip: 10.4.4.93` |
| **Cisco Nexus 1 only** | `host.ip: 10.4.4.3` |
| **Cisco Nexus 2 only** | `host.ip: 10.4.4.4` |
| **Both Cisco** | `host.ip: (10.4.4.3 OR 10.4.4.4)` |
| **All NetFlow** | `event.dataset: netflow` |
| **All sFlow** | `event.dataset: sflow` |

### About device.name
**Note:** The `device.name` field is **not natively present** in ElastiFlow data. Use `host.ip` instead for device filtering.

If dashboard visualizations reference `device.name` and show errors:
1. Edit the visualization
2. Change field from `device.name` to `host.ip`
3. Save

Or create a **runtime field** in Kibana:
1. Stack Management → Index Patterns → unified-flow-*
2. Add field → Runtime field
3. Name: `device.name`
4. Script: `emit(doc['host.ip'].value)`

## Management Scripts

### Check Status
```bash
./scripts/check_elastiflow.sh
```

### Restart Collectors
```bash
# Backend N1
sshpass -p 'T3l3h0us#' ssh -p 2332 telehouse@10.4.4.21 "cd ~/elastiflow && docker-compose restart"

# Backend N2  
sshpass -p 'T3l3h0us#' ssh telehouse@10.4.4.90 "cd ~/elastiflow && docker-compose restart"
```

### View Logs
```bash
# Backend N1
sshpass -p 'T3l3h0us#' ssh -p 2332 telehouse@10.4.4.21 "docker logs flow-collector --tail 50 -f"

# Backend N2
sshpass -p 'T3l3h0us#' ssh telehouse@10.4.4.90 "docker logs flow-collector --tail 50 -f"
```

### Force Immediate Cleanup (Delete all but latest index)
```bash
# List all flow indices
curl -s -u elastic:telehouse -k "https://10.4.4.87:9200/_cat/indices/elastiflow-flow-*?v&s=index"

# Delete old indices (use carefully!)
curl -s -u elastic:telehouse -k -X DELETE "https://10.4.4.87:9200/elastiflow-flow-ecs-8.0-2.5-rollover-000001"
```

## Network Device Configuration

### Cisco Nexus (sFlow)
```
! Enable sFlow globally
sflow enable

! Set collector (Backend N2)
sflow collector-ip 10.4.4.90 port 6343

! Set agent IP per switch
sflow agent-ip 10.4.4.3   ! For switch 10.4.4.3
sflow agent-ip 10.4.4.4   ! For switch 10.4.4.4

! Verify
show sflow
show sflow detail
```

### Juniper (NetFlow v9)
```
! Configure sampling
set forwarding-options sampling input rate 4096
set forwarding-options sampling input run-length 1

! Set collector (Backend N1)
set forwarding-options sampling family inet output flow-server 10.4.4.21 port 2050
set forwarding-options sampling family inet output flow-server 10.4.4.21 version9 template refresh-rate 30

! Commit
commit and-quit

! Verify
show configuration forwarding-options sampling
```

## Kibana Dashboards

### Access
- **URL:** https://10.4.4.87:5601/app/dashboards
- **Credentials:** elastic / telehouse

### Dashboards Available
- `[Unified Flow] Detailed Traffic Analysis` - Full traffic breakdown
- `[Unified Flow] Top-N Analysis` - Top talkers, protocols, ports
- `[Unified Flow] Conversation Partners` - Flow pairs

### Index Pattern Fix Applied
| Index Pattern | Now Points To |
|---------------|---------------|
| `unified-flow-*` | `elastiflow-flow-ecs-*` ✅ |
| `unified-flow-index` | `elastiflow-flow-ecs-*` ✅ |
| `unified-flow-clean` | `elastiflow-flow-ecs-*` ✅ |
| `unified-flow-pattern` | `elastiflow-flow-ecs-*` ✅ |

### Fixing device.name Errors
If visualizations show "Field device.name was not found":

**Option 1: Edit Visualization (Quick)**
1. Open dashboard → Edit panel
2. Change field from `device.name` to `host.ip`
3. Save

**Option 2: Add Runtime Field (Persistent)**
1. Stack Management → Index Patterns
2. Select `unified-flow-*`
3. Add field → Runtime field
4. Name: `device.name`
5. Type: Keyword
6. Script: `emit(doc['host.ip'].value)`
7. Save

## Troubleshooting

### NetFlow templates not received
- **Symptom:** Logs show "template not yet received"
- **Solution:** Wait 5 minutes - NetFlow v9 sends templates periodically
- **Check:** `docker logs flow-collector | grep template`

### No sFlow data
```bash
# Verify Cisco config
sshpass -p 't3l3h0us3' ssh admin@10.4.4.3 "show sflow"

# Verify collector port
sshpass -p 'T3l3h0us#' ssh telehouse@10.4.4.90 "ss -ulnp | grep 6343"
```

### Dashboard shows no data
1. Check index pattern points to `elastiflow-flow-ecs-*`
2. Check time range (default is last 15 minutes)
3. Verify filter pills not excluding data
4. Try broad search: `*`

### High disk usage (old 2-shard indices)
```bash
# Force ILM to run immediately
curl -s -u elastic:telehouse -k -X POST "https://10.4.4.87:9200/elastiflow-flow-*/_ilm/retry"
```

## Maintenance

### Update ElastiFlow Image
```bash
# Backend N1
sshpass -p 'T3l3h0us#' ssh -p 2332 telehouse@10.4.4.21 \
  "cd ~/elastiflow && docker-compose pull && docker-compose up -d"

# Backend N2
sshpass -p 'T3l3h0us#' ssh telehouse@10.4.4.90 \
  "cd ~/elastiflow && docker-compose pull && docker-compose up -d"
```

### Manual Index Cleanup (Emergency)
```bash
# Only if disk is critical and ILM hasn't run
curl -s -u elastic:telehouse -k -X DELETE \
  "https://10.4.4.87:9200/elastiflow-flow-ecs-8.0-2.5-rollover-000001"
```

## Credentials Reference

| Service | Host | User | Password |
|---------|------|------|----------|
| Elasticsearch | 10.4.4.87:9200 | elastic | telehouse |
| Kibana | 10.4.4.87:5601 | elastic | telehouse |
| Backend N1 SSH | 10.4.4.21:2332 | telehouse | T3l3h0us# |
| Backend N2 SSH | 10.4.4.90:22 | telehouse | T3l3h0us# |
| Cisco Nexus | 10.4.4.3, 10.4.4.4 | admin | t3l3h0us3 |
| Juniper | 10.4.4.93 | telehouse | telehouse |

## Credits
- **ElastiFlow:** https://docs.elastiflow.com
- **Deployment:** Valentin-bot (2026-02-12)
- **Repository:** https://github.com/ViktorPetrov0605/custom-elk-stack
- **Version:** v1.2 (3-day retention, 1 shard, 0 replicas)

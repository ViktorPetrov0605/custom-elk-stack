# ElastiFlow Unified Collector Deployment

**Date:** 2026-02-12  
**Deployed by:** Valentin-bot  
**Status:** ✅ Production  
**Version:** v1.1 (with dashboard fix)

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
      EF_OUTPUT_ELASTICSEARCH_INDEX_TEMPLATE_SHARDS: "2"
      EF_OUTPUT_ELASTICSEARCH_INDEX_TEMPLATE_REPLICAS: "1"
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
      EF_OUTPUT_ELASTICSEARCH_INDEX_TEMPLATE_SHARDS: "2"
      EF_OUTPUT_ELASTICSEARCH_INDEX_TEMPLATE_REPLICAS: "1"
      EF_OUTPUT_ELASTICSEARCH_ECS_ENABLE: "true"
      EF_OUTPUT_ELASTICSEARCH_TLS_ENABLE: "true"
      EF_OUTPUT_ELASTICSEARCH_TLS_SKIP_VERIFICATION: "true"
      EF_PIPELINE_WORKERS: "2"
      EF_PIPELINE_BATCH_SIZE: "1000"
```

## Management Scripts

### Check Status (Both Backends)
```bash
#!/bin/bash
# check_elastiflow.sh

echo "=== Backend N1 (NetFlow) ==="
sshpass -p 'T3l3h0us#' ssh -p 2332 telehouse@10.4.4.21 "docker ps && docker logs flow-collector --tail 5" 2>/dev/null

echo ""
echo "=== Backend N2 (sFlow) ==="
sshpass -p 'T3l3h0us#' ssh telehouse@10.4.4.90 "docker ps && docker logs flow-collector --tail 5" 2>/dev/null

echo ""
echo "=== Elasticsearch Index Stats ==="
curl -s -u elastic:telehouse -k "https://10.4.4.87:9200/_cat/indices/elastiflow-flow-*?v&h=index,docs.count,store.size"

echo ""
echo "=== Device Stats ==="
curl -s -u elastic:telehouse -k -X POST "https://10.4.4.87:9200/elastiflow-flow-*/_search?size=0" \
  -H "Content-Type: application/json" \
  -d '{"aggs":{"devices":{"terms":{"field":"host.ip","size":10}},"types":{"terms":{"field":"event.dataset"}}}}' | \
  jq -r '.aggregations | "Devices: " + (.devices.buckets | map(.key + " (" + (.doc_count | tostring) + ")") | join(", ")) + " | Types: " + (.types.buckets | map(.key + " (" + (.doc_count | tostring) + ")") | join(", "))'
```

### Quick Filter Examples (Kibana Search Bar)

| Filter | Search Query |
|--------|--------------|
| **Juniper only** | `host.ip: 10.4.4.93` |
| **Cisco Nexus 1 only** | `host.ip: 10.4.4.3` |
| **Cisco Nexus 2 only** | `host.ip: 10.4.4.4` |
| **Both Cisco** | `host.ip: (10.4.4.3 OR 10.4.4.4)` |
| **All NetFlow** | `event.dataset: netflow` |
| **All sFlow** | `event.dataset: sflow` |
| **Specific time range** | `@timestamp >= "2026-02-12T10:00:00"` |

### Restart Collectors
```bash
# Backend N1
sshpass -p 'T3l3h0us#' ssh -p 2332 telehouse@10.4.4.21 "cd ~/elastiflow && docker-compose restart"

# Backend N2  
sshpass -p 'T3l3h0us#' ssh telehouse@10.4.4.90 "cd ~/elastiflow && docker-compose restart"
```

## Kibana Dashboard Filters

### Add Filter Pills
1. Open dashboard (**Detailed Traffic Analysis** or **Top-N**)
2. Click **Add filter** (top left)
3. Configure:
   - **Field:** `host.ip` or `event.dataset`
   - **Operator:** is / is one of / is between
   - **Value:** See table above
4. Click **Save**

### Edit Existing Dashboard Filter
1. Click filter pill
2. Click **Edit filter**
3. Change value
4. Click **Save**

## Index Pattern Fix (Important!)

**Issue:** Dashboards originally pointed to `unified-flow-*` (old Logstash index)
**Fix:** Updated all index patterns to `elastiflow-flow-ecs-*`

**Applied to:**
- `unified-flow-*` → `elastiflow-flow-ecs-*` ✅
- `unified-flow-index` → `elastiflow-flow-ecs-*` ✅
- `unified-flow-clean` → `elastiflow-flow-ecs-*` ✅
- `unified-flow-pattern` → `elastiflow-flow-ecs-*` ✅

## Index Lifecycle Management (ILM)

**Policy:** `elastiflow` (auto-created by ElastiFlow)

| Phase | Trigger | Action |
|-------|---------|--------|
| **Hot** | 0-7 days OR 50GB | Active indexing, rollover |
| **Warm** | After 7 days | Shrink to 1 shard, forcemerge |
| **Cold** | After 30 days | Lower priority |
| **Delete** | After 365 days | Index removed |

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

## Field Reference for Filtering

| Field | Description | Example Values |
|-------|-------------|----------------|
| `host.ip` | Flow exporter IP | `10.4.4.93`, `10.4.4.3`, `10.4.4.4` |
| `event.dataset` | Flow type | `netflow`, `sflow` |
| `source.ip` | Source of traffic | Any IP |
| `destination.ip` | Destination of traffic | Any IP |
| `@timestamp` | Event time | ISO timestamp |
| `network.protocol` | Protocol | `tcp`, `udp`, `icmp` |
| `source.port` | Source port | 80, 443, etc. |
| `destination.port` | Dest port | 80, 443, etc. |

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

# Check logs
sshpass -p 'T3l3h0us#' ssh telehouse@10.4.4.90 "docker logs flow-collector --tail 50"
```

### Dashboard shows no data
1. Check index pattern points to `elastiflow-flow-ecs-*`
2. Check time range (default is last 15 minutes)
3. Verify filter pills not excluding data
4. Try broad search: `*` (asterisk = all)

### Collector stopped
```bash
# Backend N1
sshpass -p 'T3l3h0us#' ssh -p 2332 telehouse@10.4.4.21 "cd ~/elastiflow && docker-compose up -d"

# Backend N2
sshpass -p 'T3l3h0us#' ssh telehouse@10.4.4.90 "cd ~/elastiflow && docker-compose up -d"
```

## Maintenance

### Update ElastiFlow Image
```bash
# On both backends
sshpass -p 'T3l3h0us#' ssh -p 2332 telehouse@10.4.4.21 "cd ~/elastiflow && docker-compose pull && docker-compose up -d"
sshpass -p 'T3l3h0us#' ssh telehouse@10.4.4.90 "cd ~/elastiflow && docker-compose pull && docker-compose up -d"
```

### Clean Old Indices
```bash
# Delete indices older than X days (use carefully!)
curl -s -u elastic:telehouse -k -X DELETE "https://10.4.4.87:9200/elastiflow-flow-ecs-8.0-2.5-2026.02.01"
```

## Credits
- **ElastiFlow:** https://docs.elastiflow.com
- **Deployment:** Valentin-bot (2026-02-12)
- **Repository:** https://github.com/ViktorPetrov0605/custom-elk-stack

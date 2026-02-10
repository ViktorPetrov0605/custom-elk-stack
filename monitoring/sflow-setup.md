# sFlow Configuration for Backend N2 (10.4.4.90)

## Overview

This document describes the sFlow collection setup for Backend N2 to receive flow data from Cisco Nexus switches.

## Current Configuration

### Logstash Pipeline Status

**Location:** `custom-elk-stack/logstash.conf`

The sFlow input is already configured on the backend:

```
udp {
  port => 6343
  type => "sflow"
  receive_buffer_bytes => 16777216
  workers => 4
}
```

**Docker Compose Port Mapping:**
- `6343:6343/udp` - sFlow from Cisco Nexus (currently active)
- `8514:8514/udp` - Legacy Cisco Nexus syslog (deprecated)

### Current Filter Processing

The sFlow data is processed with the following mappings:

1. **IP Addresses:**
   - `[sflow][ipv4_src_addr]` → `[source][ip]`
   - `[sflow][ipv4_dst_addr]` → `[destination][ip]`

2. **Ports:**
   - `[sflow][l4_src_port]` → `[source][port]`
   - `[sflow][l4_dst_port]` → `[destination][port]`

3. **Protocol:**
   - `[sflow][protocol]` → `[network][iana_number]`

4. **Bytes/Packets (Sampled - scaled by 4096):**
   - `[sflow][in_bytes]` × 4096 → `[source][bytes]` / `[network][bytes]`
   - `[sflow][in_pkts]` × 4096 → `[source][packets]` / `[network][packets]`

5. **Interface Information:**
   - `[sflow][if_index_in]` → `[observer][ingress][interface][id]`
   - `[sflow][if_index_out]` → `[observer][egress][interface][id]`
   - `[sflow][agent_ip]` → `[observer][ip]` (switch IP)

6. **Type Conversions:**
   - Protocol number converted to integer
   - Interface IDs kept as strings

### Output Configuration

sFlow data is sent to Elasticsearch as a data stream:

```
elasticsearch {
  hosts => ["https://es-remote:9200"]  # Local ES on Backend N2
  data_stream => "true"
  data_stream_type => "logs"
  data_stream_dataset => "sflow.net"
}
```

**Note:** Data stays on Backend N2 only. The `es-remote` service is the local Elasticsearch node that joins the cluster but stores data locally.

## Index Template & ILM Configuration

### ILM Policy

**File:** `custom-elk-stack/ilm-policy.json`

```json
{
  "policy": {
    "phases": {
      "hot": {
        "min_age": "0ms",
        "actions": {
          "set_priority": { "priority": 100 }
        }
      },
      "delete": {
        "min_age": "1d",
        "actions": { "delete": {} }
      }
    }
  }
}
```

**Applied on Backend N2:**
```bash
curl -k -X PUT "https://localhost:9200/_ilm/policy/netflow-1day-retention" \
  -u "elastic:$ELASTIC_PASSWORD" \
  -H "Content-Type: application/json" \
  -d '{"policy": {"phases": {"hot": {"min_age": "0ms", "actions": {"set_priority": {"priority": 100}}}, "delete": {"min_age": "1d", "actions": {"delete": {}}}}}}'
```

**Status:** ✅ Applied 2026-02-09  
**Script:** `custom-elk-stack/apply-ilm.sh` (configured for frontend IP)

### sFlow-Specific Index Template Requirements

Per the requirements, we need:
- **Index pattern:** `sflow-*`
- **Shards:** 1 (single shard)
- **Replicas:** 0 (no duplication)
- **ILM:** 1-day retention policy

### Applying sFlow Index Template

Run the following on Backend N2 to create the sFlow-specific index template:

```bash
curl -k -X PUT "https://localhost:9200/_index_template/sflow-template" \
  -u "elastic:$ELASTIC_PASSWORD" \
  -H "Content-Type: application/json" \
  -d '{
    "index_patterns": ["logs-sflow.net-*"],
    "data_stream": {},
    "priority": 500,
    "template": {
      "settings": {
        "number_of_shards": 1,
        "number_of_replicas": 0,
        "index.lifecycle.name": "netflow-1day-retention",
        "index.lifecycle.rollover_alias": "sflow"
      }
    }
  }'
```

**Status:** ✅ Applied 2026-02-09  
**Note:** Data streams are named based on the `data_stream_dataset` (sflow.net), so the index pattern is `logs-sflow.net-*`.

## Port Configuration Notes

### Requirement vs. Current Setup

| Requirement | Current Setup | Status |
|------------|---------------|--------|
| sFlow UDP 8514 | sFlow on 6343, 8514 used for legacy syslog | **CONFLICT** |

The standard sFlow port is **6343** (per RFC 3176). Port 8514 is currently used for legacy Cisco Nexus syslog.

**Options:**
1. **Keep 6343** (recommended) - Standard sFlow port, no changes needed to switches
2. **Change to 8514** - Requires:
   - Moving legacy syslog to another port
   - Reconfiguring Logstash inputs
   - Updating Cisco Nexus switch sFlow destination ports

### Recommendation

Keep the current configuration using **port 6343** as it follows the sFlow standard and requires no changes to switch configurations.

If port 8514 is specifically required, the switches must be reconfigured to send sFlow to port 8514, and the following changes are needed:

1. Update `docker-compose-backend.yml` port mapping
2. Update `logstash.conf` input port for sFlow
3. Coordinate with network team to update switch sFlow destination ports

## Sampling Rate

**Requirement:** 1-out-of-4096

This is configured on the **Cisco Nexus switches**, not on the collector.

### Cisco Nexus Configuration

On each switch, run:

```
configure terminal
sflow sampling-rate 4096
sflow collector 10.4.4.90 port 6343
sflow enable
end
```

The Logstash pipeline already scales the sampled values by 4096 in the ruby filter.

## Testing Reception

### 1. Verify Pipeline is Ready

Check Logstash is listening on the sFlow port:

```bash
docker exec custom-elk-stack-logstash-1 netstat -anu | grep 6343
```

### 2. Test with Sample Data

Send test sFlow packet (requires sflowtool):

```bash
# Generate test sFlow data
sflowtool -f <sample.pcap> | nc -u 10.4.4.90 6343
```

### 3. Check Elasticsearch for Data

```bash
curl -k -u elastic:$ELASTIC_PASSWORD "https://localhost:9200/logs-sflow.net-*/_search?size=1" \
  -H "Content-Type: application/json"
```

### 4. Monitor Logstash Logs

```bash
docker logs -f custom-elk-stack-logstash-1 | grep sflow
```

## Verification Checklist

- [x] Logstash container is running
- [x] Port 6343/udp is mapped and listening
- [x] sFlow index template created with 1 shard, 0 replicas
- [x] ILM policy applied (1-day retention)
- [ ] Cisco Nexus switches configured with sampling rate 4096
- [ ] Test sFlow data received and indexed

## Files Modified/Created

| File | Status | Description |
|------|--------|-------------|
| `logstash.conf` | Existing | Already has sFlow pipeline configured |
| `docker-compose-backend.yml` | Existing | Already has port 6343 mapped |
| `ilm-policy.json` | Existing | 1-day retention policy |
| `apply-ilm.sh` | Existing | Script to apply ILM |
| `monitoring/sflow-setup.md` | **Created** | This documentation file |

## Configuration Summary

### What Was Configured

| Component | Setting | Status |
|-----------|---------|--------|
| sFlow Input Port | UDP 6343 | ✅ Already configured |
| Logstash Pipeline | sFlow parsing and scaling by 4096 | ✅ Already configured |
| Index Template | `sflow-template` with 1 shard, 0 replicas | ✅ Created |
| ILM Policy | `netflow-1day-retention` (1 day deletion) | ✅ Created & Applied |
| Data Stream Output | `logs-sflow.net-*` | ✅ Configured |
| Data Location | Backend N2 only (local ES) | ✅ Confirmed |

### Listening Ports (verified)

```
UNCONN 0 0 0.0.0.0:6343 0.0.0.0:*  (sFlow from Cisco Nexus)
UNCONN 0 0 0.0.0.0:8514 0.0.0.0:*  (Legacy Cisco Nexus syslog)
```

### Elasticsearch Objects Created

```bash
# Index Template
curl -k -s -u "elastic:$ELASTIC_PASSWORD" \
  "https://localhost:9200/_index_template/sflow-template"
# Result: sflow-template with logs-sflow.net-* pattern, 1 shard, 0 replicas

# ILM Policy
curl -k -s -u "elastic:$ELASTIC_PASSWORD" \
  "https://localhost:9200/_ilm/policy/netflow-1day-retention"
# Result: 1-day hot phase, then delete
```

## Next Steps

1. ~~Apply sFlow index template~~ ✅ Completed
2. ~~Apply ILM policy~~ ✅ Completed
3. **Cisco Nexus switch configuration** - Configure switches to send sFlow to 10.4.4.90:6343 with sampling rate 4096
4. **Test data flow** - Verify sFlow records appear in Elasticsearch
5. **Monitor data retention** - Confirm 1-day ILM is working after data arrives

---

**Document Version:** 2026-02-09  
**Backend:** N2 (10.4.4.90)  
**Configuration Status:** ✅ Ready for switch configuration

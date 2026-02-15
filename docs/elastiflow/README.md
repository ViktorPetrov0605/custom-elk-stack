# ElastiFlow Deployment Guide

Complete deployment guide for ElastiFlow unified flow collector with NetFlow and sFlow support.

## Architecture

```
┌─────────────────┐     ┌─────────────────┐
│   Switch 1      │     │   Switch 2      │
│   (sFlow v5)    │     │   (sFlow v5)    │
└────────┬────────┘     └────────┬────────┘
         │ UDP 6343              │
         └──────────┬────────────┘
                    │
         ┌──────────▼──────────┐
         │    Collector N2     │
         │  ElastiFlow 7.21.0  │
         │  (sFlow collector)  │
         │  INDEX_TEMPLATE: ✗  │
         └──────────┬──────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────────┐
│              Elasticsearch Cluster                   │
│              <ES_HOST>:9200                          │
└─────────────────────────────────────────────────────┘
                    ▲
                    │
         ┌──────────┴──────────┐
         │    Collector N1     │
         │  ElastiFlow 7.21.0  │
         │ (NetFlow collector) │
         │  INDEX_TEMPLATE: ✓  │
         └──────────┬──────────┘
                    │ UDP 2050
                    │
         ┌──────────▼──────────┐
         │   Router/Switch     │
         │   (NetFlow v9)      │
         └─────────────────────┘
```

## Quick Start

### Step 1: Deploy Frontend (Elasticsearch + Kibana)

```bash
# Generate config
./deploy.sh --generate

# Edit deploy.conf with your IPs and passwords
nano deploy.conf

# Deploy
./deploy.sh --frontend
```

### Step 2: Deploy ElastiFlow Collector N1 (Primary)

```bash
# On collector server
cat > .env << EOF
ELASTICSEARCH_HOST=<YOUR_ES_IP>:9200
ELASTIC_PASSWORD=<YOUR_PASSWORD>
EOF

# Primary collector manages index templates
docker-compose -f configs/elastiflow/docker-compose-n1.yml up -d
```

### Step 3: Deploy ElastiFlow Collector N2 (Secondary)

```bash
# On secondary collector server
cat > .env << EOF
ELASTICSEARCH_HOST=<YOUR_ES_IP>:9200
ELASTIC_PASSWORD=<YOUR_PASSWORD>
EOF

# Secondary has templates DISABLED
docker-compose -f configs/elastiflow/docker-compose-n2.yml up -d
```

### Step 4: Verify

```bash
# Check collector health
docker logs flow-collector --tail 20
curl http://localhost:8080/health

# Check Elasticsearch indices
curl -k -u elastic:<password> https://<ES_IP>:9200/_cat/indices/elastiflow-*?v
```

## Critical: Index Template Management

**IMPORTANT:** When running multiple ElastiFlow collectors:

| Collector | INDEX_TEMPLATE_ENABLE | Reason |
|-----------|----------------------|--------|
| N1 (Primary) | `true` | Creates/updates ES templates |
| N2+ (Secondary) | `false` | Avoids bootstrap conflict |

If both have `true`, the second collector will fail with:
```
Invalid alias name [...] already exists
```

## Configuration Files

### N1 - Primary (NetFlow)

```yaml
# configs/elastiflow/docker-compose-n1.yml
environment:
  EF_FLOW_SERVER_UDP_PORT: "2050"
  EF_PROCESSOR_DECODE_NETFLOW9_ENABLE: "true"
  EF_PROCESSOR_DECODE_SFLOW5_ENABLE: "false"
  EF_OUTPUT_ELASTICSEARCH_INDEX_TEMPLATE_ENABLE: "true"  # PRIMARY
  EF_OUTPUT_ELASTICSEARCH_ADDRESSES: "${ELASTICSEARCH_HOST}"
```

### N2 - Secondary (sFlow + NetFlow)

```yaml
# configs/elastiflow/docker-compose-n2.yml
environment:
  EF_FLOW_SERVER_UDP_PORT: "2050,6343"
  EF_PROCESSOR_DECODE_NETFLOW9_ENABLE: "true"
  EF_PROCESSOR_DECODE_SFLOW5_ENABLE: "true"
  EF_OUTPUT_ELASTICSEARCH_INDEX_TEMPLATE_ENABLE: "false"  # SECONDARY
  EF_OUTPUT_ELASTICSEARCH_ADDRESSES: "${ELASTICSEARCH_HOST}"
```

## Multiple Backend Configurations

ElastiFlow supports flexible collector deployments. A single collector can receive both NetFlow and sFlow simultaneously, or you can specialize collectors for specific protocols.

### Protocol Support

Each collector can independently enable/disable protocols:

| Setting | Description |
|---------|-------------|
| `EF_PROCESSOR_DECODE_NETFLOW9_ENABLE` | NetFlow v9 / IPFIX |
| `EF_PROCESSOR_DECODE_SFLOW5_ENABLE` | sFlow v5 raw headers |
| `EF_PROCESSOR_DECODE_SFLOW_FLOWS_ENABLE` | sFlow flow records |

### Example: Three-Backend Deployment

For redundancy and load distribution, you can deploy specialized collectors:

| Backend | Ports | NetFlow | sFlow | Template Manager |
|---------|-------|---------|-------|------------------|
| N1 (NetFlow only) | `2050` | `true` | `false` | `true` (PRIMARY) |
| N2 (sFlow only) | `6343` | `false` | `true` | `false` |
| N3 (Both) | `2050,6343` | `true` | `true` | `false` |

**N1 — NetFlow Only (Primary, manages templates):**
```yaml
environment:
  EF_FLOW_SERVER_UDP_PORT: "2050"
  EF_PROCESSOR_DECODE_NETFLOW9_ENABLE: "true"
  EF_PROCESSOR_DECODE_SFLOW5_ENABLE: "false"
  EF_PROCESSOR_DECODE_SFLOW_FLOWS_ENABLE: "false"
  EF_OUTPUT_ELASTICSEARCH_INDEX_TEMPLATE_ENABLE: "true"
```

**N2 — sFlow Only:**
```yaml
environment:
  EF_FLOW_SERVER_UDP_PORT: "6343"
  EF_PROCESSOR_DECODE_NETFLOW9_ENABLE: "false"
  EF_PROCESSOR_DECODE_SFLOW5_ENABLE: "true"
  EF_PROCESSOR_DECODE_SFLOW_FLOWS_ENABLE: "true"
  EF_OUTPUT_ELASTICSEARCH_INDEX_TEMPLATE_ENABLE: "false"
```

**N3 — Both Protocols:**
```yaml
environment:
  EF_FLOW_SERVER_UDP_PORT: "2050,6343"
  EF_PROCESSOR_DECODE_NETFLOW9_ENABLE: "true"
  EF_PROCESSOR_DECODE_SFLOW5_ENABLE: "true"
  EF_PROCESSOR_DECODE_SFLOW_FLOWS_ENABLE: "true"
  EF_OUTPUT_ELASTICSEARCH_INDEX_TEMPLATE_ENABLE: "false"
```

### Traffic Distribution

Configure network devices to send flow data to the appropriate collectors:

```
NetFlow exporters (routers)     → N1:2050 and/or N3:2050
sFlow exporters (switches)      → N2:6343 and/or N3:6343
All devices (redundancy)        → Any collector with matching protocol enabled
```

**Important:** All collectors write to the same Elasticsearch cluster, so data is unified regardless of which collector receives it.

## Switch Configuration

### Cisco Nexus (sFlow v5)

```cisco
feature sflow
sflow collector-ip <COLLECTOR_IP> vrf default
sflow collector-port 6343
sflow agent-ip <switch-ip>
sflow sampling-rate 4096
sflow max-sampled-size 128
sflow counter-poll-interval 20
sflow max-datagram-size 1400

# Configure interfaces
sflow data-source interface Ethernet1/1
sflow data-source interface port-channel1
```

### Juniper (NetFlow v9)

```juniper
set services flow-monitoring version 9
set forwarding-options sampling input rate 4096
set forwarding-options sampling family inet output flow-server <COLLECTOR_IP> port 2050
set forwarding-options sampling family inet output flow-server <COLLECTOR_IP> version 9
```

## Elasticsearch Indices

| Index Pattern | Description | ILM Policy |
|---------------|-------------|------------|
| `elastiflow-flow-ecs-*` | Flow records | elastiflow |
| `elastiflow-metric-ecs-*` | Metrics | elastiflow |
| `elastiflow-telemetry_flow-ecs-*` | Telemetry | elastiflow |

### ILM Policy (Default: 3-day retention)

```json
{
  "policy": {
    "phases": {
      "hot": { "min_age": "0ms", "actions": { "rollover": { "max_age": "1d", "max_primary_shard_size": "10gb" } } },
      "warm": { "min_age": "0d", "actions": { "shrink": { "number_of_shards": 1 }, "forcemerge": { "max_num_segments": 1 } } },
      "delete": { "min_age": "3d", "actions": { "delete": {} } }
    }
  }
}
```

## Kibana Dashboards

Pre-built dashboards in `configs/elastiflow/dashboards/`:

1. **[Unified Flow] Detailed Traffic Analysis** - Traffic overview
2. **[Unified Flow] Conversation Partners** - Source-destination pairs
3. **[Unified Flow] Top-N Analysis** - Top talkers, ports, ASNs

### Import

```bash
# Via API
curl -k -u elastic:<password> \
  -X POST "http://<KIBANA_IP>:5601/api/saved_objects/_import?overwrite=true" \
  -H "kbn-xsrf: true" \
  --form file=@configs/elastiflow/dashboards/unified-flow-dashboards.ndjson
```

## Query Examples

```json
// Filter by device/exporter IP
{ "term": { "host.ip": "<DEVICE_IP>" } }

// Filter by source IP
{ "term": { "source.ip": "<SOURCE_IP>" } }

// Filter by destination IP
{ "term": { "destination.ip": "<DEST_IP>" } }

// Filter by protocol
{ "term": { "network.transport": "tcp" } }
```

## Troubleshooting

### Collector Unhealthy

```bash
# Check logs
docker logs flow-collector --tail 50

# Check health endpoint
curl http://localhost:8080/health
```

**Common causes:**
1. **Index template conflict** - Ensure only primary has `INDEX_TEMPLATE_ENABLE: true`
2. **Connection refused** - Check ES connectivity, TLS settings
3. **Auth failed** - Verify `ELASTIC_PASSWORD`

### No Data from Devices

```bash
# Check if ports are listening
ss -uln | grep -E "(2050|6343)"

# Check switch config (Cisco)
show sflow

# Check incoming packets
tcpdump -i any udp port 6343 -n
```

---
*Last updated: 2026-02-15*
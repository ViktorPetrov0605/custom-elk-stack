# ElastiFlow Deployment Guide

Complete deployment guide for ElastiFlow unified flow collector with NetFlow (Juniper) and sFlow (Cisco Nexus) support.

## Architecture

```
┌─────────────────┐     ┌─────────────────┐
│  Cisco Nexus 1  │     │  Cisco Nexus 2  │
│   10.4.4.3      │     │   10.4.4.4      │
│   sFlow v5      │     │   sFlow v5      │
└────────┬────────┘     └────────┬────────┘
         │ UDP 6343              │ UDP 6343
         └──────────┬────────────┘
                    │
         ┌──────────▼──────────┐
         │    Backend N2       │
         │   10.4.4.90         │
         │  ElastiFlow 7.21.0  │
         │  (sFlow collector)  │
         └──────────┬──────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────────┐
│              Elasticsearch Cluster                   │
│              10.4.4.87:9200                          │
│         elastiflow-flow-ecs-* indices               │
└─────────────────────────────────────────────────────┘
                    ▲
                    │
         ┌──────────┴──────────┐
         │    Backend N1       │
         │   10.4.4.21:2332    │
         │  ElastiFlow 7.21.0  │
         │ (NetFlow collector) │
         └──────────┬──────────┘
                    │ UDP 2050
                    │
         ┌──────────▼──────────┐
         │   Juniper Switch    │
         │    10.4.4.93        │
         │    NetFlow v9       │
         └─────────────────────┘
```

## Prerequisites

- Elasticsearch 8.x cluster (10.4.4.87:9200)
- Kibana 8.x (10.4.4.87:5601)
- Docker & Docker Compose on collector hosts
- Network connectivity:
  - Backend N1 → Elasticsearch:9200
  - Backend N2 → Elasticsearch:9200
  - Cisco Nexus switches → Backend N2:6343 (UDP)
  - Juniper switch → Backend N1:2050 (UDP)

## Quick Start

### Step 1: Deploy Backend N1 (NetFlow Collector)

```bash
# On 10.4.4.21:2332
mkdir -p ~/elastiflow && cd ~/elastiflow

# Download config
curl -O https://raw.githubusercontent.com/ViktorPetrov0605/oclaw-bak/main/configs/elastiflow/docker-compose-n1.yml
mv docker-compose-n1.yml docker-compose.yml

# Start collector
docker compose up -d
```

### Step 2: Deploy Backend N2 (sFlow Collector)

```bash
# On 10.4.4.90
mkdir -p ~/elastiflow && cd ~/elastiflow

# Download config
curl -O https://raw.githubusercontent.com/ViktorPetrov0605/oclaw-bak/main/configs/elastiflow/docker-compose-n2.yml
mv docker-compose-n2.yml docker-compose.yml

# Start collector
docker compose up -d
```

### Step 3: Verify Data Flow

```bash
# Check Elasticsearch indices
curl -k -u elastic:telehouse https://10.4.4.87:9200/_cat/indices/elastiflow-*?v

# Query by device
curl -k -u elastic:telehouse https://10.4.4.87:9200/elastiflow-*/_search -d '{
  "query": { "term": { "host.ip": "10.4.4.3" } }
}'
```

## Configuration Files

### Backend N1 (NetFlow - Primary Template Manager)

Located at: `configs/elastiflow/docker-compose-n1.yml`

Key settings:
- `EF_FLOW_SERVER_UDP_PORT: "2050"` - NetFlow port
- `EF_OUTPUT_ELASTICSEARCH_INDEX_TEMPLATE_ENABLE: "true"` - **Manages templates**

### Backend N2 (sFlow - Secondary Collector)

Located at: `configs/elastiflow/docker-compose-n2.yml`

Key settings:
- `EF_FLOW_SERVER_UDP_PORT: "2050,6343"` - Both ports
- `EF_OUTPUT_ELASTICSEARCH_INDEX_TEMPLATE_ENABLE: "false"` - **Disabled to avoid conflict**

### Important: Dual Collector Setup

When running multiple collectors writing to the same Elasticsearch cluster:

1. **Only ONE collector** should have `EF_OUTPUT_ELASTICSEARCH_INDEX_TEMPLATE_ENABLE: "true"`
2. All other collectors must set this to `"false"`
3. This prevents index template/alias conflicts during bootstrap

## Switch Configuration

### Cisco Nexus (sFlow v5)

```cisco
# On Nexus switches (10.4.4.3 and 10.4.4.4)
feature sflow

sflow collector-ip 10.4.4.90 vrf default
sflow collector-port 6343
sflow agent-ip <switch-ip>
sflow sampling-rate 4096
sflow max-sampled-size 128
sflow counter-poll-interval 20
sflow max-datagram-size 1400

# Configure interfaces to monitor
sflow data-source interface port-channel4
sflow data-source interface port-channel6
sflow data-source interface port-channel10
# ... add more interfaces as needed
```

### Juniper (NetFlow v9)

```juniper
# On Juniper switch (10.4.4.93)
set services flow-monitoring version 9
set forwarding-options sampling input rate 4096
set forwarding-options sampling family inet output flow-server 10.4.4.21 port 2050
set forwarding-options sampling family inet output flow-server 10.4.4.21 version 9
```

## Elasticsearch Indices

| Index Pattern | Description | Retention |
|---------------|-------------|-----------|
| `elastiflow-flow-ecs-8.0-2.5-rollover` | Main flow data | ILM managed |
| `elastiflow-metric-ecs-8.0-2.5-*` | Metrics | ILM managed |
| `elastiflow-telemetry_flow-ecs-*` | Telemetry | ILM managed |

### ILM Policy

```json
{
  "policy": {
    "phases": {
      "hot": { "min_age": "0ms", "actions": { "rollover": { "max_size": "50gb", "max_age": "7d" } } },
      "warm": { "min_age": "7d", "actions": { "shrink": { "number_of_shards": 1 }, "forcemerge": { "max_num_segments": 1 } } },
      "cold": { "min_age": "30d", "actions": {} },
      "delete": { "min_age": "365d", "actions": { "delete": {} } }
    }
  }
}
```

## Kibana Dashboards

Pre-built dashboards are available in `configs/elastiflow/dashboards/`:

1. **[Unified Flow] Conversation Partners** - Traffic by source/destination
2. **[Unified Flow] Top-N Analysis** - Top talkers, destinations, ports
3. **[Unified Flow] Detailed Traffic Analysis** - Comprehensive flow breakdown

### Import Dashboards

```bash
# In Kibana: Stack Management → Saved Objects → Import
# Upload: dashboards/unified-flow-dashboards.ndjson
```

## Troubleshooting

### Collector Shows "unhealthy"

Check logs:
```bash
docker logs flow-collector --tail 50
```

Common issues:
1. **Bootstrap failure** - Index template conflict
   - Solution: Ensure only ONE collector has `INDEX_TEMPLATE_ENABLE: true`
2. **Permission denied** - Volume permissions
   - Solution: `docker volume rm elastiflow-data && docker compose up -d`
3. **Connection refused** - Elasticsearch unreachable
   - Check network, TLS settings, credentials

### No Data from Specific Device

1. **Check switch config** - Is sFlow/NetFlow enabled?
2. **Check firewall** - UDP port open on collector?
3. **Verify data arrival**:
   ```bash
   ss -uln | grep 6343  # Check listening
   ss -uln | grep 2050
   ```

### Query by Device

```json
// Filter by device/exporter IP
{ "term": { "host.ip": "10.4.4.3" } }

// Filter by source IP
{ "term": { "source.ip": "X.X.X.X" } }

// Filter by destination IP
{ "term": { "destination.ip": "X.X.X.X" } }
```

## Credentials

| Service | URL | Username | Password |
|---------|-----|----------|----------|
| Elasticsearch | https://10.4.4.87:9200 | elastic | telehouse |
| Kibana | https://10.4.4.87:5601 | elastic | telehouse |
| Backend N1 SSH | telehouse@10.4.4.21:2332 | telehouse | T3l3h0us# |
| Backend N2 SSH | telehouse@10.4.4.90 | telehouse | T3l3h0us# |
| Cisco Nexus | 10.4.4.3, 10.4.4.4 | admin | t3l3h0us3 |

## Maintenance

### Restart Collectors

```bash
# On collector host
cd ~/elastiflow
docker compose restart
```

### Check Health

```bash
docker ps --filter name=flow
docker logs flow-collector --tail 20
```

### Update Configuration

1. Edit `docker-compose.yml`
2. `docker compose down`
3. `docker compose up -d`

## Files in This Repository

```
configs/elastiflow/
├── docker-compose-n1.yml      # Backend N1 (NetFlow, primary)
├── docker-compose-n2.yml      # Backend N2 (sFlow, secondary)
├── dashboards/
│   └── unified-flow-dashboards.ndjson
├── ilm-policy.json            # Elasticsearch ILM policy
└── index-template.json        # Field mappings
```

## Changelog

| Date | Change |
|------|--------|
| 2026-02-15 | Fixed dual-collector bootstrap conflict (N2 INDEX_TEMPLATE_ENABLE:false) |
| 2026-02-14 | Added Nexus 10.4.4.3, 10.4.4.4 sFlow data collection |
| 2026-02-12 | Initial deployment with Juniper NetFlow |

---

*Last updated: 2026-02-15 by Valentin-bot*
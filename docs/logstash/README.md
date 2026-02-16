# Logstash Unified Flow Collector

Complete deployment guide for unified NetFlow and sFlow collection using Logstash.

> **Note:** This replaces ElastiFlow for unlimited flow collection capacity. See [Migration Guide](../../MIGRATION.md) for transitioning from ElastiFlow.

## Overview

Logstash with the `logstash-codec-netflow` and `logstash-codec-sflow` plugins provides a license-unlimited alternative to ElastiFlow for collecting and processing network flows.

### Key Benefits

- **No license limits** - Handle 50+ devices without rate restrictions
- **Unified schema** - Single ECS-compliant index for both NetFlow and sFlow
- **Single collector** - One Logstash instance handles both protocols
- **Compatible dashboards** - Works with existing Kibana dashboards

## Architecture

```
┌─────────────────────────────────────┐
│         Network Devices              │
├──────────────────┬──────────────────┤
│  Router/Switch   │     Switch 1      │
│  (NetFlow v9)    │   (sFlow v5)    │
└────────┬─────────┴────────┬─────────┘
         │                   │
         │ UDP 2050          │ UDP 6343
         └─────────┬─────────┘
                   │
        ┌──────────▼──────────┐
        │   Logstash Flow     │
        │   Unified Collector │
        │  ┌───────────────┐  │
        │  │ NetFlow Codec │  │──┐
        │  │    Port 2050  │  │  │
        │  └───────────────┘  │  │
        │  ┌───────────────┐  │  │
        │  │  sFlow Codec  │  │  │
        │  │    Port 6343  │  │  │
        │  └───────────────┘  │  │
        └─────────────────────┘  │
                   │             │
                   ▼             │
        ┌─────────────────────┐  │
        │ Elasticsearch       │◀─┘
        │ logstash-flow-*     │
        │ (ECS-compliant)     │
        └──────────┬──────────┘
                   │
        ┌──────────▼──────────┐
        │     Kibana          │
        │   Dashboards        │
        └─────────────────────┘
```

## Quick Start

### 1. Clone Repository

```bash
git clone https://github.com/your-org/custom-elk-stack.git
cd custom-elk-stack
```

### 2. Deploy Frontend (Elasticsearch + Kibana)

```bash
# Generate config
./deploy.sh --generate

# Edit deploy.conf
nano deploy.conf
# - Set ELASTIC_PASSWORD
# - Set FRONTEND_IP
# - Set ELASTICSEARCH_HOST

# Deploy frontend
./deploy.sh --frontend

# Set up Elasticsearch for Logstash
./logstash-migration/setup-elasticsearch.sh
```

### 3. Deploy Logstash Collectors

```bash
# On each backend server
cd /opt/logstash-flow
docker compose up -d

# Check health
curl http://localhost:9600/_node/stats
```

## Configuration Files

### Logstash Configuration

**File:** `logstash-migration/logstash.conf`

Key sections:

```ruby
input {
  # NetFlow v9 from Juniper devices
  udp {
    port => 2050
    codec => netflow { versions => [9] }
  }

  # sFlow v5 from Cisco Nexus
  udp {
    port => 6343
    codec => sflow
  }
}

filter {
  # ECS field mapping
  # Protocol detection
  # Sampling rate calculations
  # Locality detection
}

output {
  elasticsearch {
    hosts => ["https://<ES_HOST>:9200"]
    index => "logstash-flow-%{+YYYY.MM.dd}"
    template => "/usr/share/logstash/templates/flow-template.json"
  }
}
```

### Docker Compose

**File:** `logstash-migration/docker-compose.yml`

```yaml
version: '3'
services:
  logstash:
    build: .
    container_name: logstash-flow
    network_mode: host
    volumes:
      - ./logstash.conf:/usr/share/logstash/pipeline/logstash.conf:ro
      - ./flow-template.json:/usr/share/logstash/templates/flow-template.json:ro
```

### Elasticsearch Index Template

**File:** `logstash-migration/flow-template.json`

ECS-compliant mapping for:
- `source.ip`, `destination.ip` - Flow endpoints
- `host.ip` - Exporting device
- `network.bytes`, `network.packets` - Traffic metrics
- `network.transport` - Protocol (tcp/udp/icmp)
- `flow.sample.rate` - Sampling multiplier
- `flow.locality` - Internal/mixed/public

## Filtering by Device (host.ip)

### Kibana Query Language (KQL)

**Filter by exporting device:**
```
host.ip: 10.4.4.93
```

**Filter by source device:**
```
source.ip: 10.4.4.93
```

**Filter by destination:**
```
destination.ip: 10.4.4.3
```

### Available Fields

| Field | Description | Example |
|-------|-------------|---------|
| `host.ip` | Flow exporter device | Juniper router, Cisco switch |
| `source.ip` | Source of traffic | Originating IP |
| `destination.ip` | Destination of traffic | Target IP |
| `source.port` | Source port | 443, 80, 22 |
| `destination.port` | Destination port | 443, 80, 22 |
| `network.transport` | Protocol | tcp, udp, icmp |
| `flow.sample.rate` | Sampling rate | 4096, 1000 |

### Query Examples

**View all flows from a specific exporter:**
```
host.ip: 10.4.4.93
```

**View flows between two devices:**
```
(source.ip: 10.4.4.93 AND destination.ip: 10.4.4.3) OR
(source.ip: 10.4.4.3 AND destination.ip: 10.4.4.93)
```

**View traffic by protocol:**
```
host.ip: 10.4.4.93 AND network.transport: tcp
```

**View high-volume flows:**
```
host.ip: 10.4.4.93 AND network.bytes > 1000000
```

**View conversations on specific port:**
```
(destination.port: 443 OR source.port: 443) AND host.ip: 10.4.4.93
```

**Filter by flow locality:**
```
flow.locality: internal      # Both source and dest are private
flow.locality: mixed         # One side is public
flow.locality: public        # Both sides are public
```

**Exclude specific traffic:**
```
host.ip: 10.4.4.93 AND NOT destination.port: (22 OR 53)
```

### Using Dashboard Filters

1. Open any Unified Flow dashboard
2. Click the **KQL search bar** at the top
3. Type your filter (e.g., `host.ip: 10.4.4.93`)
4. Press **Enter** - all visualizations update automatically

### Dashboard-Specific Filters

**Detailed Traffic Analysis Dashboard:**
- Traffic Timeline by Device - Uses `host.ip`
- Top Sources - Uses `source.ip`
- Top Destinations - Uses `destination.ip`

**Top-N Analysis Dashboard:**
- Top Sources - `source.ip`
- Top Destinations - `destination.ip`
- Top Devices - `host.ip`

**Conversation Partners Dashboard:**
- Conversation table - `source.ip` + `destination.ip`

## Network Device Configuration

### Cisco Nexus (sFlow v5)

```cisco
feature sflow
sflow collector-ip <LOGSTASH_IP> vrf default
sflow collector-port 6343
sflow agent-ip <SWITCH_IP>
sflow sampling-rate 4096
sflow max-sampled-size 128
sflow counter-poll-interval 20

# Configure interfaces
sflow data-source interface Ethernet1/1
sflow data-source interface port-channel1
```

### Juniper (NetFlow v9)

```juniper
set services flow-monitoring version 9
set forwarding-options sampling input rate 4096
set forwarding-options sampling family inet output flow-server <LOGSTASH_IP> port 2050
set forwarding-options sampling family inet output flow-server <LOGSTASH_IP> version 9
```

## Kibana Dashboards

### Import Dashboards

```bash
curl -k -u elastic:password \
  -X POST "https://<KIBANA_IP>:5601/api/saved_objects/_import?overwrite=true" \
  -H "kbn-xsrf: true" \
  --form file=@logstash-migration/dashboards/unified-flow-dashboards.ndjson
```

### Available Dashboards

1. **[Unified Flow] Detailed Traffic Analysis**
   - Traffic timeline by device
   - Protocol distribution
   - Top sources/destinations
   - Device breakdown

2. **[Unified Flow] Top-N Analysis**
   - Top source IPs
   - Top destination IPs
   - Top source ports
   - Top destination ports
   - Top protocols
   - Top devices

3. **[Unified Flow] Conversation Partners**
   - Source-destination pairs
   - Bytes transferred
   - Packets transferred
   - Flow counts

**Index Pattern:** `logstash-flow-*`

## Verification

### Check Logstash is Receiving Flows

```bash
# Check UDP ports are listening
ss -uln | grep -E "(2050|6343)"

# Check Logstash pipeline
systemctl status logstash
docker logs logstash-flow --tail 50

# Check Elasticsearch indexing
curl -k -u elastic:password \
  https://<ES_IP>:9200/logstash-flow-*/_count
```

### Verify Data from Specific Device

```bash
# Check flows from a specific exporter
curl -k -u elastic:password \
  "https://<ES_IP>:9200/logstash-flow-*/_search?size=0" \
  -H "Content-Type: application/json" \
  -d '{
    "query": {
      "term": { "host.ip": "10.4.4.93" }
    },
    "aggs": {
      "total_flows": { "value_count": { "field": "_id" } },
      "total_bytes": { "sum": { "field": "network.bytes" } }
    }
  }'
```

## Troubleshooting

### No Data from Devices

```bash
# Check network
ping <device_ip>
telnet <device_ip> 2050  # or 6343

# Check Logstash is listening
lsof -i :2050
lsof -i :6343

# Check with tcpdump
tcpdump -i any udp port 6343 -n
tcpdump -i any udp port 2050 -n
```

### Mapping Errors

If you see field type conflicts:

```bash
# Delete old indices and let template recreate
curl -k -u elastic:password -X DELETE \
  "https://<ES_IP>:9200/logstash-flow-*"

# Re-apply template
./logstash-migration/setup-elasticsearch.sh
```

### Dashboard Shows "No Results"

1. Check index pattern: Stack Management → Index Patterns → `logstash-flow-*`
2. Verify time range: Last 15 minutes or adjust as needed
3. Check field names match: `source.ip`, not `netflow.src_addr`

### Sampling Rate Issues

If byte counts seem low:

```
# Check sampling rate in flows
curl -k -u elastic:password \
  "https://<ES_IP>:9200/logstash-flow-*/_search" \
  -H "Content-Type: application/json" \
  -d '{
    "_source": ["host.ip", "flow.sample.rate", "network.bytes"],
    "size": 5
  }'
```

Logstash automatically multiplies bytes by sampling rate if >1.

## Elasticsearch Indices

| Index Pattern | Description | ILM Policy |
|---------------|-------------|------------|
| `logstash-flow-*` | Flow records | flow-data-3-day |

Default retention: 3 days (configurable in `logstash-migration/setup-elasticsearch.sh`)

## Ports

| Service | Port | Protocol | Direction |
|---------|------|----------|-------------|
| NetFlow | 2050 | UDP | Inbound from devices |
| sFlow | 6343 | UDP | Inbound from devices |
| Logstash API | 9600 | HTTP | Localhost only |
| Elasticsearch | 9200 | HTTPS | Outbound to ES |

## Performance

### Scaling

For high-volume environments:

1. **Increase Logstash workers**
   ```yaml
   environment:
     - PIPELINE_WORKERS=4
   ```

2. **Use multiple collectors**
   - Deploy Logstash on multiple servers
   - Spread device load across collectors
   - All write to same Elasticsearch cluster

3. **Elasticsearch tuning**
   - 2+ data nodes
   -适当增加 heap size

### Monitoring

```bash
# Logstash JVM stats
curl http://localhost:9600/_node/stats/jvm

# Pipeline stats
curl http://localhost:9600/_node/stats/pipelines

# Event rates
curl http://localhost:9600/_node/stats/events
```

## Schema Differences from ElastiFlow

Logstash Flow vs ElastiFlow Field Mapping:

| ElastiFlow (Old) | Logstash Flow (New) | Notes |
|------------------|---------------------|-------|
| `flow.exporter.ip` | `host.ip` | Device IP |
| `flow.src_addr` | `source.ip` | Source IP |
| `flow.dst_addr` | `destination.ip` | Dest IP |
| `flow.src_port` | `source.port` | Source port |
| `flow.dst_port` | `destination.port` | Dest port |
| `flow.bytes` | `network.bytes` | Total bytes |
| `flow.protocol_name` | `network.transport` | Protocol |
| `flow.sampling_interval` | `flow.sample.rate` | Sampling rate |

**All mapped to ECS-compliant fields for compatibility.**

## Migration from ElastiFlow

See [MIGRATION.md](../../MIGRATION.md) for step-by-step migration instructions.

## Support

- Logstash docs: https://www.elastic.co/guide/en/logstash/current/index.html
- NetFlow codec: https://github.com/logstash-plugins/logstash-codec-netflow
- sFlow codec: https://github.com/alqasemelab/logstash-codec-sflow

---

*Last updated: 2026-02-16*
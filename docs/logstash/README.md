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
git clone https://github.com/ViktorPetrov0605/custom-elk-stack.git
cd custom-elk-stack
```

### 2. Deploy Frontend (Elasticsearch + Kibana)

```bash
# Generate config
./deploy.sh --generate

# Edit deploy.conf
nano deploy.conf
# - Set ELASTIC_PASSWORD
# - Set FRONTEND_IP={YOUR_FRONTEND_IP}
# - Set BACKEND_IPS={YOUR_BACKEND_IP_1},{YOUR_BACKEND_IP_2}

# Deploy frontend
./deploy.sh --frontend
```

### 3. Deploy Logstash Collectors

```bash
# On each backend server
./deploy.sh --backend

# Check health
curl http://localhost:9600/_node/stats
```

## Configuration Files

### Logstash Configuration

**File:** `logstash-unified.conf`

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
    hosts => ["https://{YOUR_FRONTEND_IP}:9200"]
    index => "logstash-flow-write"
  }
}
```

### Docker Compose

**File:** `docker-compose-backend.yml`

```yaml
version: '3'
services:
  logstash:
    build: .
    container_name: logstash-flow
    network_mode: host
    volumes:
      - ./logstash-unified.conf:/usr/share/logstash/pipeline/logstash.conf:ro
```

## Filtering by Device (host.ip)

### Kibana Query Language (KQL)

**Filter by exporting device:**
```
host.ip: {SWITCH_IP_1}
```

**Filter by source device:**
```
source.ip: {SWITCH_IP_1}
```

**Filter by destination:**
```
destination.ip: {SWITCH_IP_2}
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
host.ip: {SWITCH_IP_1}
```

**View flows between two devices:**
```
(source.ip: {SWITCH_IP_1} AND destination.ip: {SWITCH_IP_2}) OR
(source.ip: {SWITCH_IP_2} AND destination.ip: {SWITCH_IP_1})
```

**View traffic by protocol:**
```
host.ip: {SWITCH_IP_1} AND network.transport: tcp
```

**View high-volume flows:**
```
host.ip: {SWITCH_IP_1} AND network.bytes > 1000000
```

**View conversations on specific port:**
```
(destination.port: 443 OR source.port: 443) AND host.ip: {SWITCH_IP_1}
```

**Exclude specific traffic:**
```
host.ip: {SWITCH_IP_1} AND NOT destination.port: (22 OR 53)
```

### Using Dashboard Filters

1. Open any Unified Flow dashboard
2. Click the **KQL search bar** at the top
3. Type your filter (e.g., `host.ip: {SWITCH_IP_1}`)
4. Press **Enter** - all visualizations update automatically

## Network Device Configuration

### Cisco Nexus (sFlow v5)

```cisco
feature sflow
sflow collector-ip {YOUR_BACKEND_IP} vrf default
sflow collector-port 6343
sflow agent-ip {SWITCH_IP_1}
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
set forwarding-options sampling family inet output flow-server {YOUR_BACKEND_IP} port 2050
```

## Kibana Dashboards

### Import Dashboards

```bash
curl -k -u elastic:password \
  -X POST "http://{YOUR_FRONTEND_IP}:5601/api/saved_objects/_import?overwrite=true" \
  -H "kbn-xsrf: true" \
  --form file=@dashboards/as-analysis.ndjson
```

## Verification

### Check Logstash is Receiving Flows

```bash
# Check UDP ports are listening
ss -uln | grep -E "(2050|6343)"

# Check Logstash pipeline
docker logs logstash-flow --tail 50

# Check Elasticsearch indexing
curl -k -u elastic:password \
  https://{YOUR_FRONTEND_IP}:9200/logstash-flow-*/_count
```

### Verify Data from Specific Device

```bash
# Check flows from a specific exporter
curl -k -u elastic:password \
  "https://{YOUR_FRONTEND_IP}:9200/logstash-flow-*/_search?size=0" \
  -H "Content-Type: application/json" \
  -d '{
    "query": {
      "term": { "host.ip": "{SWITCH_IP_1}" }
    },
    "aggs": {
      "total_flows": { "value_count": { "field": "_id" } },
      "total_bytes": { "sum": { "field": "network.bytes" } }
    }
  }'
```

---

*Last updated: 2026-02-24*

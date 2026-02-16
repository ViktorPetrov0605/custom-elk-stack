# ELK Stack with Logstash Unified Flow Collector

Distributed ELK deployment using Logstash for unlimited NetFlow and sFlow collection.

**> Note:** This repository has been migrated from ElastiFlow to Logstash for unlimited flow collection capacity. See [MIGRATION.md](MIGRATION.md) for migration details.

**SECURITY WARNING:** See [SECURITY.md](SECURITY.md) - Change all default passwords before use!

## Architecture

```
Frontend Server (<FRONTEND_IP>)
├── Elasticsearch (master + data + ingest)
├── Elasticsearch-2 (master + data + ingest)
└── Kibana (port 5601)
           │
           │ HTTPS 9200
           ▼
    ┌─────────────────────────┐
    │   Logstash Collectors   │
    │   (NetFlow + sFlow)     │
    ├─────────────────────────┤
    │  Backend N1: Port 2050  │──┐
    │  Backend N2: Port 6343  │  │
    │  (or both ports)        │  │
    └──────────┬──────────────┘  │
               │                  │
        ┌──────┴──────┐           │
        ▼             ▼           │
   Router/Switch   Switches       │
   (NetFlow v9)   (sFlow v5)      │
                                  │
    ┌─────────────────────────────┘
    ▼
┌─────────────────────────────────────┐
│  Elasticsearch                      │
│  logstash-flow-* indices            │
│  (ECS-compliant, unified schema)    │
└─────────────────────────────────────┘
```

## Key Features

- **Unified Collector** - Single Logstash instance handles both NetFlow and sFlow
- **Unlimited Capacity** - No license restrictions (vs ElastiFlow's 4000 RPS limit)
- **ECS Schema** - Compatible with existing dashboards
- **Protocol Agnostic** - Filter by `host.ip` to view data from specific devices

## Quick Start

```bash
# 1. Clone repository
git clone https://github.com/your-org/custom-elk-stack.git
cd custom-elk-stack

# 2. Generate configuration
./deploy.sh --generate

# 3. Edit deploy.conf
nano deploy.conf
# - Set ELASTIC_PASSWORD and KIBANA_PASSWORD
# - Set FRONTEND_IP (Elasticsearch/Kibana server)
# - Set ELASTICSEARCH_HOST
# - Configure backend collector IPs

# 4. Deploy frontend
./deploy.sh --frontend

# 5. Set up Elasticsearch
./logstash-migration/setup-elasticsearch.sh

# 6. Deploy collectors
./deploy.sh --collectors
```

## Deployment Options

```bash
./deploy.sh -h              # Show help
./deploy.sh -g              # Generate config file
./deploy.sh -c              # Check prerequisites
./deploy.sh -f              # Deploy frontend (ES + Kibana)
./deploy.sh -l              # Deploy Logstash collectors
./deploy.sh -i              # Import dashboards
./deploy.sh -v              # Verify deployment
```

## Index Pattern

| Index | Description | Documents |
|-------|-------------|-----------|
| `logstash-flow-*` | Unified NetFlow + sFlow | Flow records |

## Filtering by Device (host.ip)

### Quick Filters in Kibana

```
# Filter by specific exporter device
host.ip: 10.4.4.93

# Filter by source IP
source.ip: 10.4.4.93

# Filter by destination IP
destination.ip: 10.4.4.3

# Traffic between two devices
(source.ip: 10.4.4.93 AND destination.ip: 10.4.4.3) OR
(source.ip: 10.4.4.3 AND destination.ip: 10.4.4.93)

# By protocol
host.ip: 10.4.4.93 AND network.transport: tcp

# High volume flows
network.bytes > 10000000

# Specific port traffic
source.port: 443 OR destination.port: 443
```

See full documentation: [docs/logstash/README.md](docs/logstash/README.md)

## Network Device Configuration

### Cisco Nexus (sFlow v5)

```cisco
feature sflow
sflow collector-ip <LOGSTASH_IP> vrf default
sflow collector-port 6343
sflow agent-ip <SWITCH_IP>
sflow sampling-rate 4096

# Configure interfaces
sflow data-source interface Ethernet1/1
sflow data-source interface port-channel1
```

### Juniper (NetFlow v9)

```juniper
set services flow-monitoring version 9
set forwarding-options sampling input rate 4096
set forwarding-options sampling family inet output flow-server <LOGSTASH_IP> port 2050
```

## Kibana Dashboards

Pre-built dashboards available in `logstash-migration/dashboards/`:

1. **[Unified Flow] Detailed Traffic Analysis** - Traffic overview by device
2. **[Unified Flow] Top-N Analysis** - Top talkers, ports, protocols
3. **[Unified Flow] Conversation Partners** - Source-destination pairs

### Import Dashboards

```bash
./deploy.sh --import
# or manually:
curl -k -u elastic:password \
  -X POST "https://<KIBANA_IP>:5601/api/saved_objects/_import?overwrite=true" \
  -H "kbn-xsrf: true" \
  --form file=@logstash-migration/dashboards/unified-flow-dashboards.ndjson
```

## Verification

```bash
# Check cluster health
curl -k -u elastic:password https://<ES_IP>:9200/_cluster/health

# Check indices
curl -k -u elastic:password https://<ES_IP>:9200/_cat/indices/logstash-flow-*?v

# Check document count
curl -k -u elastic:password https://<ES_IP>:9200/logstash-flow-*/_count

# Check Logstash health
curl http://<COLLECTOR_IP>:9600/_node/stats
```

## Files

```
logstash-migration/
├── logstash.conf              # Unified NetFlow + sFlow config
├── flow-template.json         # ECS index template
├── docker-compose.yml         # Collector deployment
├── Dockerfile                 # Custom image with sflow codec
├── setup-elasticsearch.sh    # ES setup script
└── dashboards/                # Kibana dashboards

docker-compose-frontend.yml    # Elasticsearch + Kibana
deploy.sh                      # Unified deployment script
deploy.conf                    # Configuration (auto-generated)
docs/logstash/README.md        # Full documentation
```

## Schema Fields

| Field | Type | Description |
|-------|------|-------------|
| `@timestamp` | date | Event timestamp |
| `host.ip` | ip | Flow exporter device |
| `source.ip` | ip | Source address |
| `destination.ip` | ip | Destination address |
| `source.port` | integer | Source port |
| `destination.port` | integer | Destination port |
| `network.bytes` | long | Total bytes |
| `network.packets` | long | Total packets |
| `network.transport` | keyword | Protocol (tcp/udp/icmp) |
| `flow.sample.rate` | integer | Sampling rate |
| `flow.locality` | keyword | internal/mixed/public |

See [docs/logstash/README.md](docs/logstash/README.md) for complete field reference.

## Ports

| Service | Port | Protocol | Notes |
|---------|------|----------|-------|
| Kibana | 5601 | HTTP | Web UI |
| Elasticsearch | 9200 | HTTPS | API |
| Elasticsearch | 9300-9301 | TCP | Inter-node |
| NetFlow | 2050 | UDP | From routers |
| sFlow | 6343 | UDP | From switches |

## Troubleshooting

### No Data from Devices

```bash
# Check Logstash is listening
ss -uln | grep -E "(2050|6343)"

# Check logs
docker logs logstash-flow --tail 50

# Test with tcpdump
tcpdump -i any udp port 6343 -n
tcpdump -i any udp port 2050 -n

# Check Elasticsearch
curl -k -u elastic:password https://<ES_IP>:9200/_cat/indices?v
```

### Dashboard Shows "No Results"

1. Check time range (try "Last 15 minutes")
2. Verify index pattern exists: Stack Management → Index Patterns
3. Check `logstash-flow-*` is selected
4. Try filter `host.ip: *` to see all devices

### Field Mapping Conflicts

```bash
# Reset and recreate indices
curl -k -u elastic:password -X DELETE \
  "https://<ES_IP>:9200/logstash-flow-*"

# Re-run setup
./logstash-migration/setup-elasticsearch.sh
```

## Migration from ElastiFlow

If upgrading from ElastiFlow:

1. See [MIGRATION.md](MIGRATION.md)
2. Deploy Logstash alongside (temporary)
3. Update dashboards to new index pattern
4. Stop ElastiFlow when verified

## Performance

- **Throughput:** 10,000+ flows/second per collector
- **Devices:** 50+ supported (vs ElastiFlow's 20-30)
- **Memory:** ~3-4GB per collector
- **CPU:** Moderate usage

## License

- Elastic Stack: Basic License (free)
- Logstash: Apache 2.0 (open source)
- Custom configs: MIT

## Documentation

- [Full Logstash Guide](docs/logstash/README.md)
- [Migration Guide](MIGRATION.md)
- [Deployment Guide](DEPLOYMENT.md)

---

*Last updated: 2026-02-16*
*Migrated from ElastiFlow to Logstash: 2026-02-16*
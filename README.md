# ELK Stack with NetFlow & sFlow Monitoring

Distributed ELK deployment with NetFlow (Juniper) and sFlow (Cisco Nexus) support.

⚠️ **SECURITY WARNING:** See [SECURITY.md](SECURITY.md) - Change all default passwords before use!


## Architecture

```
Frontend (10.4.4.87)
├── Elasticsearch (master role)
├── Kibana UI (port 5601)
└── .env configuration

Backend N1 (10.4.4.21) - NetFlow
├── Logstash (UDP 2050)
└── Elasticsearch (data node)

Backend N2 (10.4.4.90) - sFlow
├── Logstash (UDP 6343)
└── Elasticsearch (data node)

Network Devices
├── Juniper (NetFlow v9) → Backend N1:2050
└── Cisco Nexus (sFlow) → Backend N2:6343
```

## Prerequisites

- 3 servers with Docker & Docker Compose
- Ubuntu/Debian with SSH access
- Network devices configured for flow export
- TLS certificates generated

## Quick Start

### 1. Clone Repository
```bash
git clone https://github.com/ViktorPetrov0605/custom-elk-stack.git
cd custom-elk-stack
```

### 2. Generate Certificates
```bash
./generate-certs.sh
# Distributes certs to all nodes
```

### 3. Configure Environment
```bash
# Edit .env file
ELASTIC_PASSWORD=your-password
KIBANA_PASSWORD=your-password
```

### 4. Deploy Frontend
```bash
# On 10.4.4.87
docker-compose -f docker-compose-frontend.yml up -d
```

### 5. Deploy Backends
```bash
# On 10.4.4.21 (NetFlow)
docker-compose -f docker-compose-backend.yml up -d

# On 10.4.4.90 (sFlow)
docker-compose -f docker-compose-backend.yml up -d
```

### 6. Import Dashboards
```bash
# Via Kibana UI or API
curl -k -u elastic:password \
  -X POST "https://10.4.4.87:5601/api/saved_objects/_import" \
  -H "kbn-xsrf: true" \
  --form file=@kibana/exports/unified-dashboards.ndjson
```

## Known Issues & Troubleshooting

### Cluster UUID Mismatch
**Symptom:** `failed to join different cluster UUID`
**Fix:** Clear ES data volume on backend
```bash
docker-compose -f docker-compose-backend.yml down -v
sudo rm -rf ./data/es/*
docker-compose -f docker-compose-backend.yml up -d
```

### Kibana "unavailable"
**Symptom:** Kibana shows unavailable status
**Cause:** Frontend ES nodes need `data` role
**Fix:** Set `node.roles=master,data,ingest` in compose file

### Data Not Showing
**Symptom:** Dashboards empty
**Checks:**
```bash
# Verify indices
curl -k -u elastic:pass https://10.4.4.87:9200/_cat/indices

# Check cluster health
curl -k -u elastic:pass https://10.4.4.87:9200/_cluster/health

# Verify Logstash listening
ss -lnup | grep -E "(2050|6343)"
```

## Data Sources

### NetFlow (Juniper)
- Port: UDP 2050
- Version: v9
- Backend: N1 (10.4.4.21)
- Field: `netflow.*`

### sFlow (Cisco Nexus)
- Port: UDP 6343
- Sampling: 1/4096
- Backend: N2 (10.4.4.90)
- Field: `flow.*`

## Filtering Data

| Filter By | Field | Example Values |
|-----------|-------|----------------|
| Juniper NetFlow | `host.ip` | `192.168.224.1` |
| Nexus 1 sFlow | `host.ip` | `10.4.4.3` |
| Nexus 2 sFlow | `host.ip` | `10.4.4.4` |

## ILM Policy

All data retained for **1 day** then auto-deleted:
```json
{
  "policy": {
    "phases": {
      "hot": { "min_age": "0ms" },
      "delete": { "min_age": "1d" }
    }
  }
}
```

## Ports

| Service | Port | Access |
|---------|------|--------|
| Kibana | 5601 | Public (with auth) |
| Elasticsearch (Frontend) | 9200, 9201 | Private |
| Logstash NetFlow | 2050/udp | Network devices |
| Logstash sFlow | 6343/udp | Network devices |

## License

- Elastic Stack: Basic License (free)
- Custom configs: MIT

## Status

✅ Working deployment with:
- 4-node cluster (GREEN status)
- NetFlow + sFlow ingestion active
- Unified dashboards visualizing data
- Auto-deletion after 1 day

## Timeline

- Development started: Feb 6, 2026
- Production ready: Feb 10, 2026
- Major troubleshooting: Cluster UUID issues, role configuration

---
*Last updated: 2026-02-10*

# ELK Stack with NetFlow & sFlow Monitoring

Distributed ELK deployment with NetFlow (Juniper) and sFlow (Cisco Nexus) support.

**SECURITY WARNING:** See [SECURITY.md](SECURITY.md) - Change all default passwords before use!


## Architecture

```
Frontend (<FRONTEND_IP>)
├── Elasticsearch (master+data role)
├── Elasticsearch-2 (master+data role)
├── Kibana UI (port 5601)
└── .env configuration

Backend N1 (<BACKEND_N1_IP>) - NetFlow PRIMARY
├── ElastiFlow 7.21.0 (UDP 2050)
├── Manages ES index templates ✓
└── Receives from: Juniper <NETFLOW_DEVICE_IP>

Backend N2 (<BACKEND_N2_IP>) - sFlow SECONDARY
├── ElastiFlow 7.21.0 (UDP 2050, 6343)
├── Index templates DISABLED ✓
└── Receives from: Nexus <SFLOW_DEVICE_1>, <SFLOW_DEVICE_2>

Network Devices
├── Juniper <NETFLOW_DEVICE_IP> (NetFlow v9) → Backend N1:2050
├── Cisco Nexus <SFLOW_DEVICE_1> (sFlow v5) → Backend N2:6343
└── Cisco Nexus <SFLOW_DEVICE_2> (sFlow v5) → Backend N2:6343
```

**Example Data Flow:**
| Device Type | Protocol | Typical Records |
|-------------|----------|-----------------|
| Core Router | NetFlow v9 | High volume |
| Distribution Switch | sFlow v5 | Medium volume |
| Access Switch | sFlow v5 | Medium volume |

## Prerequisites

- 3 servers with Docker & Docker Compose
- Ubuntu/Debian with SSH access
- Network devices configured for flow export
- TLS certificates generated

## Quick Start (Recommended - Automated Deployment)

Use the unified deployment script for automatic setup:

```bash
# 1. Clone the repository
git clone https://github.com/your-org/elk-flow-monitoring.git
cd elk-flow-monitoring

# 2. Generate configuration template
./deploy.sh --generate

# 3. Edit configuration with your settings
nano deploy.conf
# - Set passwords (ELASTIC_PASSWORD, KIBANA_PASSWORD)
# - Configure IPs (FRONTEND_IP, BACKEND_*_IP)
# - Add as many backends as needed
# - Generate encryption keys: openssl rand -hex 32

# 4. Run the deployment
./deploy.sh
```

The script will:
- Check prerequisites on all servers
- Generate SSL certificates automatically
- Deploy the frontend (Kibana + Elasticsearch masters)
- Deploy all configured backends (Elasticsearch data + Logstash)
- Apply ILM policy for configurable data retention
- Import Kibana dashboards
- Verify the deployment

### Deploy Script Options

```bash
./deploy.sh -h              # Show help
./deploy.sh -c              # Check prerequisites only
./deploy.sh -f              # Deploy frontend only
./deploy.sh -b              # Deploy local backend only
./deploy.sh -p              # Post-deploy: apply ILM, import dashboards
./deploy.sh -v              # Verify deployment health
```

## Dashboard Screenshots

### Detailed Traffic Analysis
![Detailed Traffic Analysis](screenshots/dashboard-detailed-analysis.png)
*Real-time traffic overview showing traffic timeline, protocol distribution (TCP/UDP/ICMP), top sources/destinations, and device traffic metrics.*

### Conversation Partners
![Conversation Partners](screenshots/dashboard-conversation-partners.png)
*Conversation tracking showing source-destination pairs, protocol breakdown, and traffic patterns between network endpoints.*

### Top-N Analysis
![Top-N Analysis](screenshots/dashboard-topn-analysis.png)
*Comprehensive Top-N analysis including top sources, destinations, ports, protocols, and AS numbers.*

## Manual Deployment (Advanced)

For manual control or fine-tuning:

### 1. Clone Repository
```bash
git clone https://github.com/your-org/elk-flow-monitoring.git
cd elk-flow-monitoring
```

### 2. Generate Certificates
```bash
# Certificates will be generated automatically by deploy.sh
# Or manually create in certs/ directory
```

### 3. Configure Environment
```bash
# Copy and edit environment file
cp env.example .env
# Edit passwords, IPs, and settings
```

### 4. Deploy Frontend
```bash
# On frontend server
docker-compose -f docker-compose-frontend.yml up -d
```

### 5. Deploy Backends
```bash
# On each backend server
# The universal backend supports both NetFlow and sFlow:
docker-compose -f docker-compose-backend-universal.yml up -d

# Or use separate configs for dedicated collectors:
docker-compose -f docker-compose-backend.yml up -d
```

### 6. Import Dashboards
```bash
# Via API (after Kibana is ready)
curl -k -u elastic:password \
  -X POST "https://<FRONTEND_IP>:5601/api/saved_objects/_import" \
  -H "kbn-xsrf: true" \
  --form file=@kibana-dashboards-enhanced/unified-flow-dashboards-v2.ndjson
```

## Known Issues & Troubleshooting

### Dual Collector Bootstrap Conflict
**Symptom:** Secondary collector shows "unhealthy" with error:
```
Invalid alias name [...] an index or data stream exists with the same name as the alias
```
**Cause:** Multiple collectors with `EF_OUTPUT_ELASTICSEARCH_INDEX_TEMPLATE_ENABLE: true`
**Fix:** Set `EF_OUTPUT_ELASTICSEARCH_INDEX_TEMPLATE_ENABLE: "false"` on secondary collectors

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
curl -k -u elastic:pass https://<FRONTEND_IP>:9200/_cat/indices

# Check cluster health
curl -k -u elastic:pass https://<FRONTEND_IP>:9200/_cluster/health

# Verify collector listening
ss -lnup | grep -E "(2050|6343)"
```

### Cluster Node Verification
**Check:** Verify all nodes joined the cluster
```bash
curl -k -u elastic:password https://<FRONTEND_IP>:9200/_cat/nodes?v
```

**Expected output (4-node cluster):**
```
ip            heap.percent ram.percent cpu load_1m load_5m load_15m node.role master name
<FRONTEND_IP> 60           72          17  1.05    0.72    0.68     dim       *      es-frontend-2
<BACKEND_N1>  41           80          57  4.43    4.57    4.99     di        -      es-remote
<FRONTEND_IP> 48           81          17  0.79    0.66    0.66     dim       -      es-frontend
<BACKEND_N2>  64           66          0   0.00    0.01    0.01     di        -      es-remote
```

**Node roles explained:**
- `d` = data node (stores data)
- `i` = ingest node (processes data)
- `m` = master node (cluster management)
- `*` = current master node

## Data Sources

### NetFlow (Juniper)
- Port: UDP 2050
- Version: v9
- Backend: N1 (NetFlow collector)
- Field: `netflow.*`

### sFlow (Cisco Nexus)
- Port: UDP 6343
- Sampling: 1/4096 (configurable)
- Backend: N2 (sFlow collector)
- Field: `flow.*`

## Filtering Data

**Filter by device/exporter IP:**
```json
{ "term": { "host.ip": "<YOUR_DEVICE_IP>" } }
```

**Filter by source/destination:**
```json
{ "term": { "source.ip": "<SOURCE_IP>" } }
{ "term": { "destination.ip": "<DEST_IP>" } }
```

| Filter By | Field | Description |
|-----------|-------|-------------|
| Device/Exporter | `host.ip` | IP of flow-exporting device |
| Source IP | `source.ip` | Traffic source |
| Destination IP | `destination.ip` | Traffic destination |
| Protocol | `network.transport` | `tcp`, `udp`, `icmp` |

## ILM Policy

Default retention is **1 day** then auto-deleted. Customize as needed:
```json
{
  "policy": {
    "phases": {
      "hot": { "min_age": "0ms", "actions": { "rollover": { "max_age": "1d", "max_primary_shard_size": "10gb" } } },
      "warm": { "min_age": "7d", "actions": { "shrink": { "number_of_shards": 1 } } },
      "delete": { "min_age": "30d", "actions": { "delete": {} } }
    }
  }
}
```

## Ports

| Service | Port | Access |
|---------|------|--------|
| Kibana | 5601 | Public (with auth) |
| Elasticsearch (Frontend) | 9200, 9300 | Private (cluster) |
| ElastiFlow NetFlow | 2050/udp | Network devices |
| ElastiFlow sFlow | 6343/udp | Network devices |

## License

- Elastic Stack: Basic License (free)
- Custom configs: MIT

## Development Log

### 2026-02-15 - Dual Collector Fix & Documentation
- **CRITICAL FIX**: Backend N2 sFlow collector was failing to bootstrap
  - Root cause: Both collectors had `EF_OUTPUT_ELASTICSEARCH_INDEX_TEMPLATE_ENABLE: true`
  - Primary created Elasticsearch index templates/aliases first
  - Secondary failed with alias conflict during bootstrap
  - Fix: Set `INDEX_TEMPLATE_ENABLE: false` on secondary collector
- **Result**: sFlow data now flowing correctly from all devices
- **Documentation**: Created comprehensive deployment guide in `docs/elastiflow/README.md`
- **Configs**: Added production-ready docker-compose files:
  - `configs/elastiflow/docker-compose-n1.yml` - Primary (manages templates)
  - `configs/elastiflow/docker-compose-n2.yml` - Secondary (templates disabled)
- **Dashboards**: Exported Kibana dashboards to `configs/elastiflow/dashboards/`
- **ILM**: Exported Elasticsearch lifecycle policy
- **Architecture Note**: When running multiple ElastiFlow collectors to the same ES cluster, only ONE should manage templates

### 2026-02-12 - Repository Restructure & Unified Deployment
- **Major refactor**: Flattened repository structure, removed broken submodule
- **New feature**: Created `deploy.sh` - unified deployment script for automated setup
  - Auto-generates SSL certificates
  - Deploys frontend + multiple backends with single command
  - Built-in verification and health checks
- **Added**: `docker-compose-backend-universal.yml` - single backend for both NetFlow and sFlow
- **Added**: `logstash-universal.conf` - unified Logstash config handling both flow types
- **Cleanup**: Removed 40+ temporary/dev files, Python generators, screenshot scripts
- **Result**: Clean, production-ready repository structure

### 2026-02-11 - Dashboard Fixes & Backend Stabilization
- **Fixed**: Kibana dashboard JSON errors (deleted corrupted v2/v3 versions)
- **Fixed**: Recreated clean dashboards from `unified-flow-dashboards-v2.ndjson`
- **Fixed**: Index pattern dependencies - created `unified-flow-pattern`
- **Fixed**: Backend Logstash config with multi-device support
- **Status**: Cluster GREEN, flow documents indexed successfully

### 2026-02-10 - Initial Production Deployment
- **Completed**: 4-node cluster deployment (2 frontend + 2 backend)
- **Resolved**: Cluster UUID mismatch issues between nodes
- **Resolved**: Frontend ES node role configuration (master,ingest,data)
- **Network**: Configured flow exporters on network devices
- **Applied**: ILM policy for data retention
- **Sampling**: Configured appropriate sampling rates

### 2026-02-09 to 2026-02-06 - Development Phase
- Initial Docker Compose configurations
- Logstash pipeline development for NetFlow v9 and sFlow v5
- SSL certificate generation and distribution
- Dashboard prototyping in Kibana
- Network device configuration testing

---
*Last updated: 2026-02-15*
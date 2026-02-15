# Deployment Guide

## Quick Start

### Prerequisites
- Elasticsearch 8.x cluster
- Kibana 8.x
- Docker & Docker Compose on collector hosts
- Network connectivity between collectors and ES

### One-Line Deploy

```bash
# Backend N1 (Primary - manages templates)
curl -O https://raw.githubusercontent.com/your-org/elk-flow-monitoring/main/configs/elastiflow/docker-compose-n1.yml
mv docker-compose-n1.yml docker-compose.yml
docker compose up -d

# Backend N2 (Secondary - templates disabled)
curl -O https://raw.githubusercontent.com/your-org/elk-flow-monitoring/main/configs/elastiflow/docker-compose-n2.yml
mv docker-compose-n2.yml docker-compose.yml
docker compose up -d
```

## Architecture

```
┌─────────────────┐     ┌─────────────────┐
│   Switch 1      │     │   Switch 2      │
│  <SFLOW_IP_1>   │     │  <SFLOW_IP_2>   │
│   sFlow v5      │     │   sFlow v5      │
└────────┬────────┘     └────────┬────────┘
         │ UDP 6343              │ UDP 6343
         └──────────┬────────────┘
                    │
         ┌──────────▼──────────┐
         │    Backend N2       │
         │  <BACKEND_N2_IP>    │
         │  ElastiFlow 7.21.0  │
         │  (sFlow collector)  │
         └──────────┬──────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────────┐
│              Elasticsearch Cluster                   │
│              <ES_CLUSTER_IP>:9200                    │
│         elastiflow-flow-ecs-* indices               │
└─────────────────────────────────────────────────────┘
                    ▲
                    │
         ┌──────────┴──────────┐
         │    Backend N1       │
         │  <BACKEND_N1_IP>    │
         │  ElastiFlow 7.21.0  │
         │ (NetFlow collector) │
         └──────────┬──────────┘
                    │ UDP 2050
                    │
         ┌──────────▼──────────┐
         │   Core Router       │
         │  <NETFLOW_IP>       │
         │    NetFlow v9       │
         └─────────────────────┘
```

## Step-by-Step Setup

### Phase 1: Certificate Generation
```bash
# On any server with OpenSSL
./generate-certs.sh
# Certificates will be in certs/ directory
# Copy to all servers
```

### Phase 2: Frontend Server

1. **Install Docker**
```bash
sudo apt-get update
sudo apt-get install docker.io docker-compose
sudo usermod -aG docker $USER
```

2. **Deploy Frontend**
```bash
cd ~/elk-flow-monitoring
docker-compose -f docker-compose-frontend.yml up -d
```

3. **Verify**
```bash
curl -k -u elastic:$ELASTIC_PASSWORD https://<FRONTEND_IP>:9200/_cluster/health
# Should show: "status":"green"
```

### Phase 3: Backend Servers

**IMPORTANT: Dual Collector Setup**

When running multiple ElastiFlow collectors to the same Elasticsearch cluster:
- **Only ONE collector** must have `EF_OUTPUT_ELASTICSEARCH_INDEX_TEMPLATE_ENABLE: "true"`
- All other collectors must set it to `"false"`
- This prevents bootstrap conflicts with index templates/aliases

**Backend N1 - NetFlow (Primary Template Manager)**
```bash
# SSH to backend
ssh $USER@<BACKEND_N1_IP>

# Deploy
curl -O https://raw.githubusercontent.com/your-org/elk-flow-monitoring/main/configs/elastiflow/docker-compose-n1.yml
mv docker-compose-n1.yml docker-compose.yml
docker compose up -d
```

**Backend N2 - sFlow (Secondary)**
```bash
# SSH to backend
ssh $USER@<BACKEND_N2_IP>

# Deploy with templates DISABLED
curl -O https://raw.githubusercontent.com/your-org/elk-flow-monitoring/main/configs/elastiflow/docker-compose-n2.yml
mv docker-compose-n2.yml docker-compose.yml
docker compose up -d
```

### Phase 4: Network Device Configuration

**Juniper (NetFlow v9)**
```
set services flow-monitoring version 9
set forwarding-options sampling input rate 4096
set forwarding-options sampling family inet output flow-server <COLLECTOR_IP> port 2050
set forwarding-options sampling family inet output flow-server <COLLECTOR_IP> version 9
```

**Cisco Nexus (sFlow v5)**
```
feature sflow
sflow collector-ip <COLLECTOR_IP> vrf default
sflow collector-port 6343
sflow agent-ip <switch-ip>
sflow sampling-rate 4096
sflow max-sampled-size 128
sflow counter-poll-interval 20
sflow max-datagram-size 1400
sflow data-source interface <interface-name>
# ... add more interfaces as needed
```

### Phase 5: Dashboard Import

**Option A: Via Kibana UI**
1. Browse to https://<KIBANA_IP>:5601
2. Login with your credentials
3. Stack Management → Saved Objects → Import
4. Select: `configs/elastiflow/dashboards/unified-flow-dashboards.ndjson`

**Option B: Via API**
```bash
curl -k -u elastic:<password> \
  -X POST "https://<KIBANA_IP>:5601/api/saved_objects/_import?overwrite=true" \
  -H "kbn-xsrf: true" \
  --form file=@configs/elastiflow/dashboards/unified-flow-dashboards.ndjson
```

## Troubleshooting

### Issue 1: Collector Shows "unhealthy"

**Check logs:**
```bash
docker logs flow-collector --tail 50
```

**Common causes:**
1. **Bootstrap failure** - Index template conflict
   ```
   ERROR: Invalid alias name [...] already exists
   ```
   **Fix:** Set `EF_OUTPUT_ELASTICSEARCH_INDEX_TEMPLATE_ENABLE: "false"` on secondary collectors

2. **Permission denied** - Volume permissions
   **Fix:** `docker volume rm elastiflow-data && docker compose up -d`

3. **Connection refused** - Elasticsearch unreachable
   **Fix:** Check network, TLS settings, credentials

### Issue 2: No Data from Specific Device

1. Check switch config: `show sflow` (Cisco) or `show configuration | match flow` (Juniper)
2. Verify firewall allows UDP: `ss -uln | grep 6343`
3. Check data arrival: `ss -uln` shows Receive-Q growing

### Issue 3: Cluster UUID Mismatch
**Error:** `failed to join different cluster uuid`
**Fix:**
```bash
docker-compose down -v
sudo rm -rf ./data/es/*
docker-compose up -d
```

### Issue 4: Kibana Unavailable
**Fix:** Ensure frontend ES nodes have `data` role:
```yaml
environment:
  - node.roles=master,data,ingest
```

## Verification Checklist

- [ ] All ES nodes in cluster: `curl -k -u elastic:<pass> https://<ES_IP>:9200/_cat/nodes`
- [ ] Indices exist: `curl -k -u elastic:<pass> https://<ES_IP>:9200/_cat/indices/elastiflow-*`
- [ ] Data from all devices: Query `host.ip` aggregation
- [ ] Dashboards load without errors
- [ ] ILM policy applied: `curl -k -u elastic:<pass> https://<ES_IP>:9200/_ilm/policy/elastiflow`

## Files in This Repository

```
configs/elastiflow/
├── docker-compose-n1.yml      # Backend N1 (NetFlow, primary)
├── docker-compose-n2.yml      # Backend N2 (sFlow, secondary)
├── dashboards/
│   └── unified-flow-dashboards.ndjson
├── ilm-policy.json            # Elasticsearch ILM policy
└── index-template.json        # Field mappings (auto-created)

docs/elastiflow/
└── README.md                  # Full deployment guide
```

## Changelog

| Date | Change |
|------|--------|
| 2026-02-15 | Fixed dual-collector bootstrap conflict (INDEX_TEMPLATE_ENABLE:false on secondary) |
| 2026-02-15 | Added sFlow collection from multiple switches |
| 2026-02-12 | Deployed ElastiFlow 7.21.0 on both backends |
| 2026-02-12 | Unified NetFlow/sFlow into single `elastiflow-flow-ecs-*` index |
| 2026-02-10 | Initial deployment with Juniper NetFlow |
| 2026-02-10 | Elasticsearch cluster setup (4 nodes) |
| 2026-02-10 | Kibana dashboards created |

---
*Last updated: 2026-02-15*
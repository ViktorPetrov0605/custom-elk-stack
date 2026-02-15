# Deployment Guide

## Quick Start

### Prerequisites
- Elasticsearch 8.x cluster (10.4.4.87:9200)
- Kibana 8.x (10.4.4.87:5601)
- Docker & Docker Compose on collector hosts
- Network connectivity between collectors and ES

### One-Line Deploy

```bash
# Backend N1 (Primary - manages templates)
curl -O https://raw.githubusercontent.com/ViktorPetrov0605/custom-elk-stack/main/configs/elastiflow/docker-compose-n1.yml
mv docker-compose-n1.yml docker-compose.yml
docker compose up -d

# Backend N2 (Secondary - templates disabled)
curl -O https://raw.githubusercontent.com/ViktorPetrov0605/custom-elk-stack/main/configs/elastiflow/docker-compose-n2.yml
mv docker-compose-n2.yml docker-compose.yml
docker compose up -d
```

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

## Step-by-Step Setup

### Phase 1: Certificate Generation
```bash
# On any server with OpenSSL
./generate-certs.sh
# Certificates will be in certs/ directory
# Copy to all three servers: ~/.openclaw/workspace/custom-elk-stack/certs/
```

### Phase 2: Frontend Server (10.4.4.87)

1. **Install Docker**
```bash
sudo apt-get update
sudo apt-get install docker.io docker-compose
sudo usermod -aG docker $USER
```

2. **Deploy Frontend**
```bash
cd ~/custom-elk-stack
docker-compose -f docker-compose-frontend.yml up -d
```

3. **Verify**
```bash
curl -k -u elastic:$ELASTIC_PASSWORD https://10.4.4.87:9200/_cluster/health
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
# SSH to backend (port 2332)
ssh -p 2332 $USER@10.4.4.21

# Deploy
cd ~/custom-elk-stack
curl -O https://raw.githubusercontent.com/ViktorPetrov0605/custom-elk-stack/main/configs/elastiflow/docker-compose-n1.yml
mv docker-compose-n1.yml docker-compose.yml
docker compose up -d
```

**Backend N2 - sFlow (Secondary)**
```bash
# SSH to backend
ssh $USER@10.4.4.90

# Deploy with templates DISABLED
cd ~/custom-elk-stack
curl -O https://raw.githubusercontent.com/ViktorPetrov0605/custom-elk-stack/main/configs/elastiflow/docker-compose-n2.yml
mv docker-compose-n2.yml docker-compose.yml
docker compose up -d
```

### Phase 4: Network Device Configuration

**Juniper (NetFlow v9)**
```
set services flow-monitoring version 9
set forwarding-options sampling input rate 4096
set forwarding-options sampling family inet output flow-server 10.4.4.21 port 2050
set forwarding-options sampling family inet output flow-server 10.4.4.21 version 9
```

**Cisco Nexus (sFlow v5)**
```
feature sflow
sflow collector-ip 10.4.4.90 vrf default
sflow collector-port 6343
sflow agent-ip <switch-ip>
sflow sampling-rate 4096
sflow max-sampled-size 128
sflow counter-poll-interval 20
sflow max-datagram-size 1400
sflow data-source interface port-channel4
sflow data-source interface port-channel6
# ... add more interfaces
```

### Phase 5: Dashboard Import

**Option A: Via Kibana UI**
1. Browse to https://10.4.4.87:5601
2. Login: elastic / telehouse
3. Stack Management → Saved Objects → Import
4. Select: `configs/elastiflow/dashboards/unified-flow-dashboards.ndjson`

**Option B: Via API**
```bash
curl -k -u elastic:telehouse \
  -X POST "https://10.4.4.87:5601/api/saved_objects/_import?overwrite=true" \
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

- [ ] All ES nodes in cluster: `curl -k -u elastic:telehouse https://10.4.4.87:9200/_cat/nodes`
- [ ] Indices exist: `curl -k -u elastic:telehouse https://10.4.4.87:9200/_cat/indices/elastiflow-*`
- [ ] Data from all devices: Query `host.ip` aggregation
- [ ] Dashboards load without errors
- [ ] ILM policy applied: `curl -k -u elastic:telehouse https://10.4.4.87:9200/_ilm/policy/elastiflow`

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
| 2026-02-15 | Fixed dual-collector bootstrap conflict (N2 INDEX_TEMPLATE_ENABLE:false) |
| 2026-02-15 | Added Nexus 10.4.4.3, 10.4.4.4 sFlow collection (94K+ records) |
| 2026-02-12 | Deployed ElastiFlow 7.21.0 on both backends |
| 2026-02-12 | Unified NetFlow/sFlow into single `elastiflow-flow-ecs-*` index |
| 2026-02-10 | Initial deployment with Juniper NetFlow |
| 2026-02-10 | Elasticsearch cluster setup (4 nodes) |
| 2026-02-10 | Kibana dashboards created |

## Credentials

| Service | URL | Username | Password |
|---------|-----|----------|----------|
| Elasticsearch | https://10.4.4.87:9200 | elastic | telehouse |
| Kibana | https://10.4.4.87:5601 | elastic | telehouse |
| Backend N1 SSH | telehouse@10.4.4.21:2332 | telehouse | T3l3h0us# |
| Backend N2 SSH | telehouse@10.4.4.90 | telehouse | T3l3h0us# |
| Cisco Nexus | 10.4.4.3, 10.4.4.4 | admin | t3l3h0us3 |

---
*Last updated: 2026-02-15*
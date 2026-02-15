# Deployment Guide

## Quick Start

### Prerequisites
- Docker & Docker Compose on all servers
- Network connectivity between collectors and Elasticsearch

### Deploy Frontend (Elasticsearch + Kibana)

```bash
# On frontend server
git clone https://github.com/your-org/custom-elk-stack.git
cd custom-elk-stack

# Generate config
./deploy.sh --generate

# Edit deploy.conf
nano deploy.conf

# Deploy
./deploy.sh --frontend
```

### Deploy ElastiFlow Collectors

```bash
# On collector server
git clone https://github.com/your-org/custom-elk-stack.git
cd custom-elk-stack

# Create .env file
cat > .env << EOF
ELASTICSEARCH_HOST=<YOUR_ES_IP>:9200
ELASTIC_PASSWORD=<YOUR_PASSWORD>
EOF

# For PRIMARY collector (manages templates)
docker-compose -f configs/elastiflow/docker-compose-n1.yml up -d

# For SECONDARY collectors (templates disabled)
docker-compose -f configs/elastiflow/docker-compose-n2.yml up -d
```

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
         │    Backend N2       │
         │  ElastiFlow 7.21.0  │
         │  (sFlow collector)  │
         │  INDEX_TEMPLATE: ✗  │
         └──────────┬──────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────────┐
│              Elasticsearch Cluster                   │
│              <FRONTEND_IP>:9200                      │
└─────────────────────────────────────────────────────┘
                    ▲
                    │
         ┌──────────┴──────────┐
         │    Backend N1       │
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

## Critical: Dual Collector Setup

When running multiple ElastiFlow collectors to the same Elasticsearch cluster:

1. **Only ONE collector** must have `EF_OUTPUT_ELASTICSEARCH_INDEX_TEMPLATE_ENABLE: "true"`
2. All other collectors must set it to `"false"`
3. This prevents index template/alias conflicts during bootstrap

## Files Reference

| File | Purpose |
|------|---------|
| `docker-compose-frontend.yml` | Elasticsearch + Kibana frontend |
| `configs/elastiflow/docker-compose-n1.yml` | Primary collector (NetFlow, templates ON) |
| `configs/elastiflow/docker-compose-n2.yml` | Secondary collector (sFlow, templates OFF) |
| `configs/elastiflow/ilm-policy.json` | 3-day retention policy |
| `configs/elastiflow/dashboards/` | Kibana dashboards |
| `deploy.sh` | Unified deployment script |

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

# Add interfaces
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

## Verification

```bash
# Check cluster health
curl -k -u elastic:<password> https://<ES_IP>:9200/_cluster/health

# Check nodes
curl -k -u elastic:<password> https://<ES_IP>:9200/_cat/nodes?v

# Check indices
curl -k -u elastic:<password> https://<ES_IP>:9200/_cat/indices/elastiflow-*?v

# Check collector health
docker logs flow-collector --tail 20
curl http://localhost:8080/health
```

## Troubleshooting

### Collector Bootstrap Failure

**Symptom:** Container shows "unhealthy" with alias conflict error

```
ERROR: Invalid alias name [...] an index or data stream exists with the same name
```

**Fix:** 
- Primary collector: `EF_OUTPUT_ELASTICSEARCH_INDEX_TEMPLATE_ENABLE: "true"`
- Secondary collectors: `EF_OUTPUT_ELASTICSEARCH_INDEX_TEMPLATE_ENABLE: "false"`

### No Data from Devices

1. Verify switch config: `show sflow` (Cisco) or `show configuration | match flow` (Juniper)
2. Check firewall allows UDP: `sudo ufw allow 2050/udp`, `sudo ufw allow 6343/udp`
3. Verify packets arriving: `ss -uln | grep 6343`

### Dashboard Import Issues

```bash
# Manual import via API
curl -k -u elastic:<password> \
  -X POST "http://<KIBANA_IP>:5601/api/saved_objects/_import?overwrite=true" \
  -H "kbn-xsrf: true" \
  --form file=@configs/elastiflow/dashboards/unified-flow-dashboards.ndjson
```

---
*Last updated: 2026-02-15*
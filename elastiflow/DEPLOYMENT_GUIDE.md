# ElastiFlow Deployment Guide

## Overview
Complete ElastiFlow NetFlow/sFlow collector deployment with Elasticsearch cluster.

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│  Frontend (10.4.4.87)                                        │
│  ┌──────────────┐  ┌──────────────┐                          │
│  │ Elasticsearch│  │    Kibana    │                          │
│  │ Master Node  │  │   Dashboard  │                          │
│  │ :9200        │  │   :5601      │                          │
│  └──────────────┘  └──────────────┘                          │
└─────────────────────────────────────────────────────────────┘
                              │
           ┌──────────────────┴──────────────────┐
           │                                     │
┌──────────▼──────────┐              ┌──────────▼──────────┐
│ Backend N1          │              │ Backend N2          │
│ (10.4.4.21:2332)    │              │ (10.4.4.90)         │
│ ┌─────────────────┐ │              │ ┌─────────────────┐ │
│ │ ES Data +       │ │              │ │ ES Data +       │ │
│ │ ElastiFlow      │ │              │ │ ElastiFlow      │ │
│ │ NetFlow:2050/udp│ │              │ │ sFlow:6343/udp  │ │
│ └─────────────────┘ │              │ └─────────────────┘ │
└─────────────────────┘              └─────────────────────┘
           │                                     │
           ▼                                     ▼
    ┌────────────┐                     ┌────────────┐
    │  Juniper   │                     │   Nexus 1  │
    │  NetFlow   │                     │   sFlow    │
    └────────────┘                     └────────────┘
```

## Prerequisites
- Docker and Docker Compose installed on all servers
- SSH access to all servers
- Network devices configured to export flow data

## Phase 1: Copy Configs to Servers

```bash
# Frontend (10.4.4.87)
scp docker-compose-frontend.yml telehouse@10.4.4.87:~/elastiflow/
scp deploy.sh telehouse@10.4.4.87:~/elastiflow/

# Backend N1 (10.4.4.21:2332)
scp -P 2332 docker-compose-backend-n1.yml telehouse@10.4.4.21:~/elastiflow/
scp -P 2332 deploy.sh telehouse@10.4.4.21:~/elastiflow/

# Backend N2 (10.4.4.90)
scp docker-compose-backend-n2.yml telehouse@10.4.4.90:~/elastiflow/
scp deploy.sh telehouse@10.4.4.90:~/elastiflow/
```

## Phase 2: Deploy

**Order matters!** Deploy frontend first (master), then backends.

### 1. Frontend (Master Node + Kibana)
```bash
ssh telehouse@10.4.4.87
cd ~/elastiflow
chmod +x deploy.sh
./deploy.sh frontend
```

### 2. Backend N1 (NetFlow Collector)
```bash
ssh -p 2332 telehouse@10.4.4.21
cd ~/elastiflow
chmod +x deploy.sh
./deploy.sh backend-n1
```

### 3. Backend N2 (sFlow Collector)
```bash
ssh telehouse@10.4.4.90
cd ~/elastiflow
chmod +x deploy.sh
./deploy.sh backend-n2
```

## Phase 3: Verify Cluster

```bash
# On any server
curl http://10.4.4.87:9200/_cluster/health?pretty

# Should show:
# - "status" : "green" or "yellow"
# - "number_of_nodes" : 3
# - "number_of_data_nodes" : 2
```

## Phase 4: Configure Network Devices

### Juniper (NetFlow → Backend N1:10.4.4.21:2050)

```junos
set forwarding-options sampling input rate 100
set forwarding-options sampling input run-length 0
set forwarding-options sampling family inet output flow-server 10.4.4.21 port 2050
set forwarding-options sampling family inet output flow-server 10.4.4.21 version 9
```

### Nexus 1 & 2 (sFlow → Backend N2:10.4.4.90:6343)

```nexus
sflow enable
sflow collector 10.4.4.90 port 6343
sflow sampling-rate 10000
sflow counter-poll-interval 60
```

## Access URLs

| Service | URL | Notes |
|---------|-----|-------|
| Kibana | http://10.4.4.87:5601 | Main dashboard |
| Elasticsearch | http://10.4.4.87:9200 | API endpoint |
| NetFlow | 10.4.4.21:2050/udp | Juniper flows |
| sFlow | 10.4.4.90:6343/udp | Nexus 1 & 2 flows |

## Verification Checklist

- [ ] All 3 ES nodes joined cluster (`_cluster/health` shows 3 nodes)
- [ ] Kibana loads at http://10.4.4.87:5601
- [ ] ElastiFlow indices created (`curl /_cat/indices/elastiflow*`)
- [ ] NetFlow data arriving from Juniper
- [ ] sFlow data arriving from Nexus switches
- [ ] ElastiFlow dashboards showing AS paths, IPs, ports

## Troubleshooting

```bash
# Check collector logs (on backend servers)
docker logs elastiflow-collector-netflow   # or -sflow

# Check ES logs
docker logs elasticsearch-master  # or es-data-n1, es-data-n2

# Check cluster health
curl http://10.4.4.87:9200/_cluster/health?pretty

# List indices
curl http://10.4.4.87:9200/_cat/indices?v

# View flow stats on collector
docker exec -it elastiflow-collector-netflow /bin/sh -c "cat /var/log/elastiflow/*.log"
```

## Configuration Details

### Free Tier Limits
- Max 4,000 flows/second per collector
- Community support only
- No Flow Classification License required

### Elasticsearch Settings
- Cluster name: `elastiflow-cluster`
- Security: Disabled (xpack.security.enabled=false)
- Memory: 2GB heap per node
- Master: Single master on frontend
- Data: 2 data nodes on backends

### Flow Collection
- **NetFlow**: UDP port 2050, supports v5/v9/IPFIX
- **sFlow**: UDP port 6343, supports v5
- Index name: `elastiflow`
- Auto-creation of index templates enabled

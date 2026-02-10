# Kibana Dashboards Setup - Phase 3 Complete

**Date**: 2026-02-09  
**Phase**: 3 - Frontend Master Nodes & Kibana Dashboards  
**Status**: ✅ COMPLETE

---

## 1. Frontend Configuration Verified

### Elasticsearch Master-Only Nodes

**File**: `docker-compose-frontend.yml`

**Changes Made**:
- Changed `node.roles` from `[master,data,ingest]` to `[master]` for both ES instances
- Added `node.attr.node_type=master_only` attribute
- This ensures frontend nodes only manage cluster metadata, NOT device data

**Before**:
```yaml
node.roles: master,data,ingest
```

**After**:
```yaml
node.roles: master
node.attr.node_type: master_only
```

### Data Isolation

| Node | Role | Data Stored | Purpose |
|------|------|-------------|---------|
| es-frontend | master | Cluster state, index metadata | Master node only |
| es-frontend-2 | master | Cluster state, index metadata | Master node only |
| es-remote (backend) | data, ingest | NetFlow, sFlow device data | Data storage |

**Volumes**:
- Frontend: `./data-frontend` and `./data-frontend-2` for cluster metadata only
- Backend: `./data-remote` for actual NetFlow/sFlow indices

---

## 2. Kibana Dashboard Configuration

### Dashboard: NetFlow & sFlow Network Monitoring

**Dashboard ID**: `dashboard-netflow-sflow`

**Panels**:
1. **Interface Traffic (bps/pps)** - Line chart showing traffic over time
2. **Top Talkers** - Pie chart of top source IPs by volume
3. **Critical Interfaces Traffic** - Area chart monitoring 15 key interfaces
4. **Alarm Indicators** - Metric display for critical events
5. **Port-Channel Health** - Table view of monitored port-channels

### Index Patterns Created

#### NetFlow Index Pattern
- **Pattern**: `netflow-*`
- **Time Field**: `@timestamp`
- **Source**: Juniper NetFlow (UDP 2050)
- **Fields**: source.ip, destination.ip, source.port, destination.port, network.bytes, network.packets, observer.ip, netflow.interface_in, netflow.interface_out

#### sFlow Index Pattern
- **Pattern**: `sflow-*`
- **Time Field**: `@timestamp`
- **Source**: Cisco Nexus sFlow (UDP 6343)
- **Fields**: agent.ip, host.hostname, interface.name, interface.index, source.ip, destination.ip, network.bytes, network.packets

---

## 3. Interface Monitoring

### 15 Critical Interfaces Identified

Based on Nexus analysis (`monitoring/nexus-analysis.md`):

#### 🔴 CRITICAL - Needs Immediate Attention
| Interface | Switch | Issue | Status |
|-----------|--------|-------|--------|
| Po111 (1-IX) | NEXUS2 | DOWN - No operational members | **CRITICAL** |
| Eth1/51 | NEXUS2 | XCVR absent - member of Po111 | **CRITICAL** |

#### 🟡 HIGH PRIORITY - vPC Infrastructure
| Interface | Switch | Purpose |
|-----------|--------|---------|
| Po200 | Both | vPC Peer-Link (25G x2 = 50G) |
| Po599 | Both | TH-DS5/6-VPC (100G) |

#### 🟢 PEERING LINKS
| Interface | Switch | Connected To |
|-----------|--------|--------------|
| Po6 | Both | SOX-80G (4x10G members) |
| Po10 | NEXUS1 | Google-20G |
| Po10 | NEXUS2 | TurkIX |
| Po62 | Both | RETN (2x10G members) |
| Po71 | Both | TelecomArmenia |
| Po871 | Both | A1BG_AS8717 |
| Po902 | Both | TH-SOF-DS1/2 (3x10G) |

#### 🟢 MANAGEMENT & OTHER
| Interface | Switch | Purpose |
|-----------|--------|---------|
| mgmt0 | Both | Out-of-band management |
| Po4 | Both | B-IX-RS-BG2 (1G copper) |
| Po31 | Both | Telepoint |
| Eth1/34 | NEXUS2 | INALAN (recently flapped) |
| VLAN SVI | Both | Layer 3 interfaces |

---

## 4. Export Files Created

### Location: `custom-elk-stack/kibana/exports/`

| File | Description |
|------|-------------|
| `index-pattern-netflow.json` | NetFlow index pattern |
| `index-pattern-sflow.json` | sFlow index pattern |
| `dashboard-netflow-sflow.json` | Main dashboard configuration |
| `visualization-traffic-bps.json` | Traffic visualization |
| `visualization-top-talkers.json` | Top talkers pie chart |
| `visualization-interface-traffic.json` | 15 interfaces monitor |
| `visualization-alarms.json` | Alarm indicators |
| `visualization-port-channel.json` | Port-channel health table |
| `kibana-dashboards-export.ndjson` | **All objects combined** |
| `README.md` | Import instructions |

---

## 5. Setup Instructions

### Step 1: Verify Cluster Health
```bash
curl -s -k -u elastic:$ELASTIC_PASSWORD https://10.4.4.87:9200/_cluster/health
```
Expected: `status: green`, `number_of_nodes: 4`, `number_of_data_nodes: 2`

### Step 2: Check Kibana Status
```bash
curl http://10.4.4.87:5601/api/status
```
Expected: Status changes from "unavailable" to "available" after startup

### Step 3: Import Dashboards
```bash
cd /opt/custom-elk-stack/kibana/exports

# Using curl
curl -X POST http://10.4.4.87:5601/api/saved_objects/_import \
  -H "kbn-xsrf: true" \
  -u elastic:$ELASTIC_PASSWORD \
  -H "Content-Type: multipart/form-data" \
  -F file=@kibana-dashboards-export.ndjson

# Or via Kibana UI:
# 1. Open http://10.4.4.87:5601
# 2. Login as elastic/$ELASTIC_PASSWORD
# 3. Stack Management → Saved Objects → Import
# 4. Select kibana-dashboards-export.ndjson
```

### Step 4: Verify Data Flow
```bash
# Check for NetFlow indices
curl -s -k -u elastic:$ELASTIC_PASSWORD https://10.4.4.87:9200/_cat/indices/netflow-*

# Check for sFlow indices
curl -s -k -u elastic:$ELASTIC_PASSWORD https://10.4.4.87:9200/_cat/indices/sflow-*
```

### Step 5: Configure Dashboard
1. Set default index pattern to `netflow-*`
2. Adjust time picker to "Last 15 minutes"
3. Enable auto-refresh (30 seconds)
4. Set up Watcher alerts for Po111 DOWN state

---

## 6. Access Information

| Service | URL | Credentials |
|---------|-----|-------------|
| Kibana | http://10.4.4.87:5601 | elastic / $ELASTIC_PASSWORD |
| Elasticsearch | https://10.4.4.87:9200 | elastic / $ELASTIC_PASSWORD |
| NetFlow Input | UDP 2050 | - |
| sFlow Input | UDP 6343 | - |

---

## 7. Next Steps

### Immediate
1. ⚠️ **Fix NEXUS2 Po111** - Transceiver missing (Eth1/51)
2. Apply updated docker-compose-frontend.yml (requires restart)
3. Import dashboards into Kibana

### Monitoring Setup
1. Configure Watcher for Po111 DOWN alerts
2. Set up email notifications for buffer threshold events
3. Create additional dashboards for deep-dive analysis

### Phase 4 Preparation
- ILM policy verification for data retention
- Backup configuration for master node metadata
- SSL certificate renewal schedule

---

## 8. Verification Checklist

- [x] Frontend ES configured as master-only nodes
- [x] Data isolation (frontend = metadata, backend = device data)
- [x] Index patterns created for netflow-* and sflow-*
- [x] Dashboard created with 5 panels
- [x] 15 critical interfaces identified and configured
- [x] All exports saved to kibana/exports/
- [x] Import instructions documented
- [ ] Dashboards imported into Kibana (requires running Kibana)
- [ ] Data flow verified (requires active NetFlow/sFlow sources)

---

*Generated by OpenClaw ELK Setup - Phase 3*

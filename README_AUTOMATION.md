# ELK Stack + Monitoring - Complete Setup

## 🚀 Quick Start (Fresh Install)

```bash
git clone https://github.com/ViktorPetrov0605/custom-elk-stack.git
cd custom-elk-stack
git checkout elastiflow
chmod +x auto-setup.sh

# Run on each node in order:
./auto-setup.sh frontend      # On 10.4.4.87
./auto-setup.sh backend-n1    # On 10.4.4.21 (port 2332)
./auto-setup.sh backend-n2    # On 10.4.4.90
./auto-setup.sh monitoring    # On 10.4.4.52
```

## 📋 What's Included

### 1. ELK Stack (4 Nodes)
- **Frontend (10.4.4.87)**: ES Master + Kibana (HTTP) + Logstash
- **Backend N1 (10.4.4.21)**: ES Data + NetFlow Logstash (port 2055)
- **Backend N2 (10.4.4.90)**: ES Data + sFlow Logstash (port 6343)
- **Monitoring (10.4.4.52)**: Flask Dashboard (port 8080)

### 2. Configuration Files
| File | Purpose |
|------|---------|
| `auto-setup.sh` | Master automation script |
| `logstash-unified-netflow.conf` | NetFlow collector (Juniper) |
| `logstash-unified-sflow.conf` | sFlow collector (Cisco) |
| `kibana-dashboard-fixed.ndjson` | Working dashboard export |
| `ilm-policy-1-day.json` | 1-day data retention |
| `index-template-unified-flow.json` | Unified schema mapping |

### 3. Features
- ✅ Unified NetFlow/sFlow schema
- ✅ 4096× sampling multiplier for Juniper
- ✅ 1-day ILM retention
- ✅ Kibana dashboards (6 viz + 1 dashboard)
- ✅ 15-sec auto-refresh
- ✅ Monitoring dashboard with health checks
- ✅ 4-day monitoring data retention

## 🔑 Default Credentials

| Service | URL | Username | Password |
|---------|-----|----------|----------|
| Kibana | http://10.4.4.87:5601 | elastic | telehouse |
| Monitoring | http://10.4.4.52:8080 | - | - |
| ES API | http://10.4.4.87:9200 | elastic | telehouse |

SSH: `telehouse` / `T3l3h0us#`

## 📚 Documentation

- `docs/KIBANA_IP_FILTERING_GUIDE.md` - How to filter by IP in Kibana
- `docs/COMPLETE_SETUP_AUTOMATION.md` - Full deployment guide
- `docs/DEPLOYMENT_STATUS.md` - Troubleshooting
- `docs/KIBANA_SETUP_GUIDE.md` - Manual Kibana setup

## 🎯 IP Filtering in Kibana

### Quick Filters
```
# Source IP
source.ip: 192.168.1.100

# Destination IP Range
destination.ip: 10.4.4.0/24

# Specific Device
device.name: juniper-sw

# Top Talkers (>1MB)
network.bytes > 1000000

# Protocol + IP
network.transport: tcp and source.ip: 192.168.1.100
```

See full guide: `docs/KIBANA_IP_FILTERING_GUIDE.md`

## 🔧 Post-Setup Verification

```bash
# Check cluster health
curl -s -u elastic:telehouse http://10.4.4.87:9200/_cluster/health | jq .

# Check nodes
curl -s -u elastic:telehouse http://10.4.4.87:9200/_cat/nodes?v

# Check index
curl -s -u elastic:telehouse http://10.4.4.87:9200/unified-flow-*/_count
```

## 🐛 Troubleshooting

### Kibana "Data View Not Found" Error
Clear browser cache: `Ctrl+Shift+R` or open incognito window

### Kibana Shows DOWN in Monitoring
Database has wrong URL. Fix:
```bash
sqlite3 ~/.openclaw/monitor-dashboard/data/monitoring.db \
    "UPDATE services SET type='http', url='http://10.4.4.87:5601/api/status' WHERE name='Kibana';"
```

### No Flow Data
```bash
# Check Logstash ports
netstat -tlnp | grep -E '2055|6343'

# Check Logstash logs
journalctl -u logstash -f
```

## 📝 Data Retention

- **Flow Data**: 1 day (ILM automatic)
- **Monitoring**: 4 days (SQLite cleanup)
- **Audit Logs**: OS managed

## 💡 Architecture

```
Network Flows:
  Juniper SW (NetFlow) ──→ 10.4.4.21:2055 ──→ Logstash ──→ ES
  Cisco Nexus (sFlow)  ──→ 10.4.4.90:6343 ──→ Logstash ──→ ES
                                                  ↓
  Users:  Kibana ←── 10.4.4.87:5601 ←── ES Cluster (4 nodes)
          Dashboard ←── 10.4.4.52:8080 (SQLite + Flask)
```

## 🔄 Full Automation Script

The `auto-setup.sh` handles:
1. Package installation (ES, Kibana, Logstash)
2. SSL certificate generation for cluster
3. Service configuration
4. ILM policy setup
5. Index template creation
6. Kibana dashboard import
7. Monitoring dashboard setup

Run with: `./auto-setup.sh [frontend|backend-n1|backend-n2|monitoring]`

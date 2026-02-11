# Complete ELK Stack + Monitoring Auto-Setup Guide

## Overview
This guide enables full automated setup of the 4-node ELK cluster with monitoring dashboard.

## Quick Start - Fresh Install

```bash
# 1. Clone repository
git clone https://github.com/ViktorPetrov0605/custom-elk-stack.git
cd custom-elk-stack
git checkout elastiflow

# 2. Run automated setup
chmod +x auto-setup.sh
./auto-setup.sh
```

## What Gets Installed Automatically

### 1. Elasticsearch Cluster (4 nodes)
- **Frontend (es-frontend, es-frontend-2)** - 10.4.4.87
  - ES master-eligible nodes
  - Kibana + Logstash
- **Backend N1 (es-remote)** - 10.4.4.21
  - ES data node
  - Logstash (NetFlow collector)
  - Port 2332 SSH
- **Backend N2 (es-remote)** - 10.4.4.90
  - ES data node  
  - Logstash (sFlow collector)

### 2. Monitoring Dashboard (Port 8080)
- Flask-based web UI
- SQLite database
- 15-second health checks
- 4-day data retention
- Auto-cleanup cron job

### 3. Kibana Dashboards
- Index pattern: unified-flow-*
- 6 visualizations + 1 dashboard
- Auto-refresh every 15 seconds
- Pre-configured for NetFlow + sFlow data

## Manual Steps (If Auto-Script Fails)

### Frontend Server (10.4.4.87)
```bash
# Install Elasticsearch
wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
echo "deb https://artifacts.elastic.co/packages/9.x/apt stable main" | sudo tee /etc/apt/sources.list.d/elastic-9.x.list
sudo apt update
sudo apt install elasticsearch=9.2.4

# Install Kibana
sudo apt install kibana=9.2.4

# Install Logstash
sudo apt install logstash=9.2.4

# Stop services for configuration
sudo systemctl stop elasticsearch kibana logstash

# Copy configs
cp config/elasticsearch-frontend.yml /etc/elasticsearch/elasticsearch.yml
cp config/kibana.yml /etc/kibana/kibana.yml
cp config/logstash-frontend.conf /etc/logstash/conf.d/

# Start services
sudo systemctl start elasticsearch
sleep 30
sudo systemctl start kibana
sudo systemctl start logstash
```

### Backend N1 (10.4.4.21:2332)
```bash
# SSH: ssh -p 2332 telehouse@10.4.4.21

sudo apt install elasticsearch=9.2.4 logstash=9.2.4

# Copy SSL certs from frontend (required for cluster)
scp -P 2332 telehouse@10.4.4.21:/path/to/certs /etc/elasticsearch/certs/

# Copy configs
cp config/elasticsearch-backend.yml /etc/elasticsearch/elasticsearch.yml
cp config/logstash-netflow.conf /etc/logstash/conf.d/

sudo systemctl start elasticsearch logstash
```

### Backend N2 (10.4.4.90)
```bash
# SSH: ssh telehouse@10.4.4.90

sudo apt install elasticsearch=9.2.4 logstash=9.2.4

# Copy SSL certs from frontend
scp telehouse@10.4.4.87:/etc/elasticsearch/certs/* /etc/elasticsearch/certs/

# Copy configs
cp config/elasticsearch-backend.yml /etc/elasticsearch/elasticsearch.yml
cp config/logstash-sflow.conf /etc/logstash/conf.d/

sudo systemctl start elasticsearch logstash
```

### Monitoring Dashboard (10.4.4.52)
```bash
# SSH: ssh telehouse@10.4.4.52

# Install Python dependencies
pip3 install flask --break-system-packages

# Create directories
mkdir -p ~/.openclaw/monitor-dashboard/data

# Copy code
cp -r monitor-dashboard/* ~/.openclaw/monitor-dashboard/

# Initialize database
cd ~/.openclaw/monitor-dashboard
python3 -c "from database import init_db, insert_default_servers; init_db(); insert_default_servers()"

# Start service
cd ~/.openclaw/monitor-dashboard
python3 app.py
```

## Post-Setup Configuration

### 1. Verify Cluster Health
```bash
# On frontend
curl -s -u elastic:telehouse http://localhost:9200/_cluster/health | jq .
# Expected: "status" : "green"
```

### 2. Import Kibana Dashboards
```bash
# Via API
curl -s -u elastic:telehouse -XPOST -H "kbn-xsrf: true" \
  "http://localhost:5601/api/saved_objects/_import?overwrite=true" \
  --form file=@kibana-dashboard-fixed.ndjson
```

### 3. Configure ILM Policy
```bash
curl -s -u elastic:telehouse -XPUT -H "Content-Type: application/json" \
  "http://localhost:9200/_ilm/policy/flow-data-1-day-retention" \
  -d @config/ilm-policy-1-day.json
```

### 4. Start Monitoring
```bash
# On monitoring server
sudo apt install sqlite3
pip3 install flask

# Start monitoring service
cd ~/.openclaw/monitor-dashboard
python3 app.py  # Runs on port 8080
```

## Default Credentials

| Service | Username | Password |
|---------|----------|----------|
| Elasticsearch | elastic | telehouse |
| Kibana | elastic | telehouse |
| SSH (all servers) | telehouse | T3l3h0us# |

## Network Flow

```
Juniper SW (NetFlow) → 10.4.4.21:2055 → Logstash → ES
Cisco Nexus (sFlow)  → 10.4.4.90:6343 → Logstash → ES
                       ↓
                Kibana ← 10.4.4.87:5601 (HTTP)
                Dashboard ← 10.4.4.52:8080 (HTTP)
```

## Verification Checklist

- [ ] All 4 ES nodes show in `/_cluster/health`
- [ ] `/_cat/nodes` shows 4 nodes
- [ ] Kibana loads at http://IP:5601
- [ ] Dashboard shows all services UP
- [ ] Flow data appears in unified-flow-* index
- [ ] Visualizations render without errors
- [ ] Auto-refresh works (15s)

## Troubleshooting

### SSL Certificate Issues
```bash
# Regenerate certs
/usr/share/elasticsearch/bin/elasticsearch-certutil ca
/usr/share/elasticsearch/bin/elasticsearch-certutil cert --ca elastic-stack-ca.p12

# Copy to all nodes
scp certs/* root@backend1:/etc/elasticsearch/certs/
scp certs/* root@backend2:/etc/elasticsearch/certs/
```

### Kibana HTTPS Issues
If Debian 13 TLS errors occur:
```bash
# Switch to HTTP in kibana.yml
SERVER_SSL_ENABLED: false
```

### No Flow Data
```bash
# Check Logstash logs
sudo journalctl -u logstash -f

# Verify ports listening
sudo netstat -tlnp | grep -E '2055|6343'
```

## Data Retention

- **Flow Data**: 1 day (ILM policy automatic)
- **Monitoring Data**: 4 days (SQLite cron cleanup)
- **Audit Logs**: OS managed

## Files Included in Repo

```
custom-elk-stack/
├── auto-setup.sh              # Master automation script
├── kibana-dashboard-fixed.ndjson  # Working dashboard export
├── config/
│   ├── elasticsearch-frontend.yml
│   ├── elasticsearch-backend.yml
│   ├── kibana.yml
│   ├── logstash-frontend.conf
│   ├── logstash-netflow.conf
│   ├── logstash-sflow.conf
│   ├── ilm-policy-1-day.json
│   └── index-template-unified-flow.json
├── monitor-dashboard/
│   ├── app.py
│   ├── database.py
│   ├── checker.py
│   └── templates/
└── docs/
    ├── KIBANA_IP_FILTERING_GUIDE.md
    ├── KIBANA_SETUP_GUIDE.md
    ├── DEPLOYMENT_STATUS.md
    └── COMPLETE_SETUP_AUTOMATION.md  # This file
```

## Support

- Kibana: http://10.4.4.87:5601
- Monitoring: http://10.4.4.52:8080
- ES API: curl -u elastic:telehouse http://10.4.4.87:9200

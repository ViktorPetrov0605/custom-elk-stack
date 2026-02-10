# Deployment Guide

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

**Backend N1 - NetFlow (10.4.4.21)**
```bash
# SSH to backend (port 2332)
ssh -p 2332 $USER@10.4.4.21

# Deploy
cd ~/custom-elk-stack
docker-compose -f docker-compose-backend.yml up -d

# Verify cluster join
docker logs custom-elk-stack_es-remote_1 | grep "cluster name"
```

**Backend N2 - sFlow (10.4.4.90)**
```bash
# SSH to backend
ssh $USER@10.4.4.90

# Deploy
cd ~/custom-elk-stack
docker-compose -f docker-compose-backend.yml up -d
```

### Phase 4: Network Device Configuration

**Juniper (NetFlow)**
```bash
# Already configured by network team
# Verify: show configuration | match flow
```

**Cisco Nexus (sFlow)**
```bash
# Already configured by network team
# Collector: 10.4.4.90:6343
# Sampling: 1/4096
```

### Phase 5: Dashboard Import

**Option A: Via Kibana UI**
1. Browse to http://10.4.4.87:5601
2. Login: elastic / <YOUR_PASSWORD>
3. Stack Management → Saved Objects → Import
4. Select: `kibana/exports/unified-dashboards.ndjson`

**Option B: Via API**
```bash
curl -k -u elastic:$ELASTIC_PASSWORD \
  -X POST "https://10.4.4.87:5601/api/saved_objects/_import?overwrite=true" \
  -H "kbn-xsrf: true" \
  --form file=@kibana/exports/unified-dashboards.ndjson
```

## Troubleshooting Common Issues

### Issue 1: Cluster UUID Mismatch
**Error:** `failed to join different cluster uuid`
**Cause:** ES data volume from previous cluster

**Fix:**
```bash
docker-compose -f docker-compose-backend.yml down -v
sudo rm -rf ./data/es/*
docker-compose -f docker-compose-backend.yml up -d
# Wait 60 seconds for rejoin
```

### Issue 2: Kibana Unavailable
**Error:** `{"status":{"overall":{"level":"unavailable"}}}`
**Cause:** Frontend ES nodes missing `data` role

**Fix:**
In `docker-compose-frontend.yml`, change:
```yaml
environment:
  - node.roles=master,data,ingest  # NOT just master,ingest
```
Then restart:
```bash
docker-compose -f docker-compose-frontend.yml restart es-frontend es-frontend-2
sleep 30
docker-compose -f docker-compose-frontend.yml restart kibana
```

### Issue 3: No Data in Dashboards
**Check 1:** Verify indices exist
```bash
curl -k -u elastic:$ELASTIC_PASSWORD https://10.4.4.87:9200/_cat/indices | grep -E "(netflow|sflow)"
```

**Check 2:** Verify cluster has all nodes
```bash
curl -k -u elastic:$ELASTIC_PASSWORD https://10.4.4.87:9200/_cat/nodes
# Should show 4 nodes: 2 frontend (10.4.4.87), 2 backends (10.4.4.21, 10.4.4.90)
```

**Check 3:** Verify Logstash receiving
```bash
# On backend N1
ss -lnup | grep 2050
docker logs custom-elk-stack-logstash-1 | grep netflow

# On backend N2
ss -lnup | grep 6343
docker logs custom-elk-stack-logstash-1 | grep sflow
```

### Issue 4: Port Forward Not Working
If accessing via 10.241.108.5:5601 fails:
```bash
# Restart socat on main host
pkill socat
nohup socat TCP4-LISTEN:5601,bind=10.241.108.5,fork,reuseaddr TCP4:10.4.4.87:5601 &
```

## Verification Checklist

- [ ] All 4 ES nodes appear in `_cat/nodes`
- [ ] Kibana shows "available" status
- [ ] NetFlow index has documents (17K+)
- [ ] sFlow index has documents (791K+)
- [ ] Dashboards show visualizations without errors
- [ ] ILM policy shows "1-day retention"
- [ ] TLS/SSL working (green lock in browser)

## Post-Deployment

### Daily Checks
```bash
# Check cluster health
curl -k -u elastic:$ELASTIC_PASSWORD https://10.4.4.87:9200/_cluster/health | jq '.status'

# Check data flow
curl -k -u elastic:$ELASTIC_PASSWORD https://10.4.4.87:9200/_cat/indices | grep -E "(netflow|sflow)"

# Check disk usage on backends
df -h | grep docker
```

### Adding New Network Devices

1. Configure device to send flows to appropriate backend
2. Verify with tcpdump:
```bash
sudo tcpdump -i eth0 udp port 2050 -n  # NetFlow
sudo tcpdump -i eth0 udp port 6343 -n  # sFlow
```
3. Check indices for new data after 5 minutes

---
*Deployment completed: February 10, 2026*

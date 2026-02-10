# ElastiFlow NetFlow/sFlow Collector Deployment

## 📦 Deployment Package Contents

| File | Purpose |
|------|---------|
| `docker-compose-frontend.yml` | Kibana + ES Master (10.4.4.87) |
| `docker-compose-backend-n1.yml` | NetFlow Collector + ES Data (10.4.4.21) |
| `docker-compose-backend-n2.yml` | sFlow Collector + ES Data (10.4.4.90) |
| `deploy.sh` | Local deployment script for each server |
| `remote-deploy.sh` | Full remote deployment via SSH |
| `DEPLOYMENT_GUIDE.md` | Complete deployment documentation |
| `inventory.ini` | Server inventory for Ansible/use |

## 🚀 Quick Deploy (Manual)

1. **Copy configs to each server:**
```bash
# Frontend
scp docker-compose-frontend.yml deploy.sh telehouse@10.4.4.87:~/elastiflow/

# Backend N1 (NetFlow)
scp -P 2332 docker-compose-backend-n1.yml deploy.sh telehouse@10.4.4.21:~/elastiflow/

# Backend N2 (sFlow)
scp docker-compose-backend-n2.yml deploy.sh telehouse@10.4.4.90:~/elastiflow/
```

2. **Deploy in order:**
```bash
# 1. Frontend first (starts master node)
ssh telehouse@10.4.4.87 'cd ~/elastiflow && ./deploy.sh frontend'

# 2. Then Backend N1
ssh -p 2332 telehouse@10.4.4.21 'cd ~/elastiflow && ./deploy.sh backend-n1'

# 3. Finally Backend N2
ssh telehouse@10.4.4.90 'cd ~/elastiflow && ./deploy.sh backend-n2'
```

## 🚀 Automated Deploy (SSH Key Required)

If you have SSH key authentication set up:
```bash
cd elastiflow/
./remote-deploy.sh
```

## 📊 Verification

Check cluster health:
```bash
curl http://10.4.4.87:9200/_cluster/health?pretty
```

Expected output:
```json
{
  "cluster_name": "elastiflow-cluster",
  "status": "green",
  "number_of_nodes": 3,
  "number_of_data_nodes": 2,
  ...
}
```

## 🌐 Access URLs

| Service | URL |
|---------|-----|
| Kibana Dashboard | http://10.4.4.87:5601 |
| Elasticsearch API | http://10.4.4.87:9200 |
| NetFlow Receiver | 10.4.4.21:2050/udp |
| sFlow Receiver | 10.4.4.90:6343/udp |

## 📝 Network Device Configuration

### Juniper (NetFlow to 10.4.4.21:2050)
```junos
set forwarding-options sampling family inet output flow-server 10.4.4.21 port 2050 version 9
```

### Nexus (sFlow to 10.4.4.90:6343)
```nexus
sflow collector 10.4.4.90 port 6343
sflow enable
```

## 🔧 Configuration Notes

- **License**: Free tier (up to 4,000 flows/sec per collector)
- **Security**: xpack disabled - accessible without authentication
- **ES Heap**: 2GB per node
- **Cluster**: 1 master + 2 data nodes
- **Index**: `elastiflow` (auto-created by collector)

---
*Generated: 2026-02-10*

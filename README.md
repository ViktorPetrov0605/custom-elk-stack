# Unified NetFlow & sFlow Monitoring Stack

Distributed ELK deployment utilizing Logstash for unlimited NetFlow (Juniper) and sFlow (Cisco Nexus) collection.

## 🚀 Key Improvements (2026.02.20)
- **Automatic Rollover**: Indices now roll over automatically at **10GB** to optimize shard performance.
- **Strict Mapping**: Explicit field types (IP, Keyword, Long) prevent Kibana "Fielddata" errors.
- **Sankey AS Analysis**: Brand new interactive Sankey diagram for Source-to-Destination AS flow analysis.
- **Unlimited Capacity**: Logstash-based collection with no RPS license limits.

---

## 🏗️ Architecture

- **Frontend (10.4.4.87)**:
  - 2x Elasticsearch Nodes (Master/Data)
  - 1x Kibana (Port 5601)
- **Backends (10.4.4.21, 10.4.4.90)**:
  - 1x Elasticsearch Remote Node (Local storage)
  - 1x Logstash Collector (NetFlow: 2050, sFlow: 6343)

---

## 📦 Repository Structure

- `deploy.sh`: Unified deployment script for Frontend/Backend.
- `logstash-unified.conf`: The active multi-protocol Logstash pipeline.
- `templates/`:
  - `logstash-flow-template.json`: Explicit field mappings.
  - `logstash-flow-policy.json`: ILM policy (10GB rollover, 7-day retention).
- `scripts/`:
  - `prune_indices.sh`: Manual index cleanup script (keeps last 10 indices).
- `dashboards/`: Latest compatible dashboard exports (NDJSON).

---

## ⚙️ Setup & Deployment

### 1. Configure the Environment
Generate and edit the configuration file:
```bash
./deploy.sh --generate
nano deploy.conf
```

### 2. Deploy Frontend (10.4.4.87)
```bash
./deploy.sh --frontend
```

### 3. Deploy Backends (Collectors)
Run on both 10.4.4.21 and 10.4.4.90:
```bash
./deploy.sh --backend
```

### 4. Import Dashboards
```bash
./deploy.sh --import
```

---

## 🗑️ Index Management (ILM)

The system is configured for **Rollover-based indexing**:
- **Write Alias**: `logstash-flow`
- **Naming**: `logstash-flow-YYYY.MM.DD-00000x`
- **Rollover**: Automatic at **10GB**.
- **Retention**: **7 Days** (Default).

To manually enforce a strict count of 10 indices (deleting the oldest), use the provided script:
```bash
./scripts/prune_indices.sh
```

---

## 📊 Analytics Schema

| Field | Type | Description |
|-------|------|-------------|
| `@timestamp` | date | Event time |
| `source.ip` | ip | Source IP address |
| `destination.ip` | ip | Destination IP address |
| `network.bytes` | long | Total bytes (Juniper 4096 multiplier applied) |
| `source.as.as.organization.name.keyword` | keyword | ASN Organization Name |

---

## 🛠️ Troubleshooting

**Common: "Fielddata is disabled"**
- **Cause**: Elasticsearch guessed a field as "text" instead of "keyword/ip".
- **Fix**: Re-apply the template in `templates/` and run `POST /logstash-flow/_rollover`.

**Common: Container Restart**
- Frontend: `docker-compose -f docker-compose-frontend.yml restart`
- Backend: `docker restart logstash-flow`

---
*Maintained by TeleHouse/TelePoint NetOps*

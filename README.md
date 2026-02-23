# Unified NetFlow & sFlow Monitoring Stack

Distributed ELK deployment utilizing Logstash for unlimited NetFlow (Juniper) and sFlow (Cisco Nexus) collection.

## Key Improvements (2026.02.23)
- **Serialized Indexing**: Indices now use numbering (`-000001`, `-000002`) and rollover automatically at **10GB per shard**.
- **Backend Data Locality**: Index templates force flow data to stay on Backend nodes, keeping the Frontend (87) master nodes lightweight for Kibana.
- **Strict Mapping**: Explicit field types (IP, Keyword, Long) for `device.ip`, `source.ip`, and `destination.ip` to prevent Kibana "Fielddata" errors.
- **Automated Lifecycle**: Includes an hourly cron job to prune old indices, maintaining a rotating window of 10x 10GB logs.

---

## Architecture

- **Frontend (10.4.4.87)**:
  - 2x Elasticsearch Nodes (Master/Data Role)
  - 1x Kibana (Port 5601)
- **Backends (10.4.4.21, 10.4.4.90)**:
  - 1x Elasticsearch Data Node (Local storage)
  - 1x Logstash Collector (NetFlow: 2050, sFlow: 6343)

---

## Repository Structure

- `deploy.sh`: Unified deployment script for Frontend/Backend.
- `logstash-unified.conf`: The active multi-protocol Logstash pipeline.
- `templates/`:
  - `logstash-flow-template.json`: Explicit field mappings and node allocation rules.
  - `logstash-flow-policy.json`: ILM policy for 10GB primary shard rollover.
- `scripts/`:
  - `prune_indices.sh`: Manual index cleanup script (keeps last 10 indices).
- `dashboards/`: Latest compatible dashboard exports (NDJSON).

---

## Setup & Deployment

### 1. Configure the Environment
Generate and edit the configuration file:
```bash
./deploy.sh --generate
nano deploy.conf
```

### 2. Deploy Frontend (10.4.4.87)
This sets up ES, Kibana, applies ILM/Templates, and bootstraps the first index:
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

## Index Management (Serialized)

The system is configured for **Serialized Rollover**:
- **Write Alias**: `logstash-flow-write`
- **Naming**: `logstash-flow-YYYY.MM.DD-00000x`
- **Rollover**: Automatic at **10GB**.
- **Retention**: Controlled by crontab running `./scripts/prune_indices.sh` (Keeps latest 10 indices).

---

## Scaling: Adding Multiple Netflow Devices

To add additional NetFlow sources (e.g., more Juniper or Cisco switches) without manual configuration:

1.  **Configure Switch**: Point NetFlow exports to your Backend IP on port **2050**.
2.  **Mapping (Optional)**: If the new switch has a different sampling rate (e.g., 2048 instead of 4096), add it to the `dictionary` in `logstash-unified.conf`:
    ```ruby
    dictionary => {
      "10.4.4.93" => "4096"
      "10.4.4.96" => "2048"  # New device
    }
    ```
3.  **Automatic Detection**: Because of `network_mode: host`, the device IP will be automatically captured from the packet source. No other changes are required.

---

| Field | Type | Description |
|-------|------|-------------|
| `@timestamp` | date | Event time |
| `device.ip` | ip | Exporter IP |
| `source.ip` | ip | Source IP address |
| `destination.ip` | ip | Destination IP address |
| `network.bytes` | long | Total bytes (Juniper 4096 multiplier applied) |
| `network.transport`| keyword| Protocol (tcp/udp/icmp) |

---

## Troubleshooting

**Error: "Fielddata is disabled"**
- **Cause**: Fields mapped as `text` accidentally.
- **Fix**: Re-run `./deploy.sh --frontend` to reapply templates, followed by:
  `curl -k -u elastic:telehouse -X POST "https://10.4.4.87:9200/logstash-flow-write/_rollover"`

---
*Maintained by TeleHouse/TelePoint NetOps - ValentinBot*

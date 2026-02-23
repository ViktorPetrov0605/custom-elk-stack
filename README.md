# Unified NetFlow & sFlow Monitoring Stack

Distributed ELK deployment utilizing Logstash for unlimited NetFlow (Juniper) and sFlow (Cisco Nexus) collection. Optimized for TeleHouse/TelePoint environments.

## Critical Deployment Traps (READ FIRST)

*   **PERMISSION DENIED / UID MATCH:** Logstash will crash-loop if the host user's UID doesn't match the internal container expectations. 
    *   *Symptom:* `[FATAL] (LoadError) failure to load file: build.rb (Permission denied)`
    *   *Location:* **10.4.4.21** uses UID **1003**. You must manually update `docker-compose-backend.yml` to include `user: "1003:1003"` if redeploying there.
*   **THE NETFLOW TEMPLATE DELAY:** After restarting a collector, dashboards will show **zero data** for the first 1-5 minutes for Juniper devices.
    *   *Why:* Logstash must wait for the hardware to send a "NetFlow Template" before it can decode traffic. 
    *   *Action:* Grab a coffee and wait; do not assume the service is broken if `docker ps` is up.
*   **SSL WARNINGS:** For internal TeleHouse convenience, this setup uses self-signed certificates. 
    *   Always use `curl -k` and `ssl_verification_mode => none`.

---

## Architecture

- **Frontend (10.4.4.87)**:
  - 2x Elasticsearch Nodes (Master/Data Role)
  - 1x Kibana (Port 5601)
  - Manages ILM policies and Index Templates.
- **Backends (10.4.4.21, 10.4.4.90)**:
  - 1x Elasticsearch Remote Node (Local storage only)
  - 1x Logstash Collector (NetFlow: 2050, sFlow: 6343)
  - **Data Locality:** Shards are automatically routed to stay on these nodes, keeping the Frontend lightweight.

---

## Index Management (Serialized)

The system is configured for a **Size + Count** rotation:
1.  **Rollover (ILM):** Indices rollover automatically when they hit **10GB**.
2.  **Numbering:** Indices use a serial suffix (`-000001`, `-000002`).
3.  **Rotation (Cron):** An hourly cron job (`./scripts/prune_indices.sh`) keeps exactly the **latest 10 indices**.
    *   *Total System Capacity:* ~100GB of flow data.

---

## Setup & Deployment

1.  **Configure Environment**:
    `./deploy.sh --generate`
2.  **Deploy Frontend (10.4.4.87)**:
    `./deploy.sh --frontend`
3.  **Deploy Backends (Collectors)**:
    `./deploy.sh --backend`
4.  **Import Dashboards**:
    `./deploy.sh --import`

---

## Scaling: Adding Multiple Netflow Devices

Adding new switches (e.g., a new Juniper at 10.4.4.96) is now automatic:

1.  **Configure Switch**: Point NetFlow v9 exports to your Backend IP on port **2050**.
2.  **IP Identification:** Because we use `network_mode: host` or the `netflow.exporter.ipv4_address` field, devices are labeled by their real Management IP, not Docker's bridge IP.
3.  **Multipliers (Optional)**: If the new switch has a different sampling rate, update the `dictionary` in `logstash-unified.conf`:
    ```ruby
    dictionary => {
      "10.4.4.93" => "4096",
      "10.4.4.96" => "2048"
    }
    ```

---

## Common Troubleshooting

**Error: "Fielddata is disabled"**
- **Cause:** A field was accidentally mapped as `text` (likely in a new index created without the template).
- **Fix:** Re-apply the frontend template and manually rollover the index:
  `curl -k -u elastic:telehouse -X POST "https://10.4.4.87:9200/logstash-flow-write/_rollover"`

**Data Missing After Restart?**
- Check `docker logs logstash-flow`. If you see "Can't (yet) decode flowset...", just wait for the switch template to arrive.

---
*Maintained by TeleHouse/TelePoint NetOps*

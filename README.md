# Unified NetFlow & sFlow Monitoring Stack

Distributed ELK deployment utilizing Logstash for unlimited NetFlow (Juniper) and sFlow (Cisco Nexus) collection. Optimized for TeleHouse/TelePoint environments.

## Critical Deployment Traps (READ FIRST)

*   **PERMISSION DENIED / UID MATCH:** Logstash will crash-loop if the host user's UID doesn't match the internal container expectations. 
    *   *Symptom:* `[FATAL] (LoadError) failure to load file: build.rb (Permission denied)`
    *   *Location:* **{YOUR_BACKEND_IP_1}** uses UID **1003**. You must manually update `docker-compose-backend.yml` to include `user: "1003:1003"` if redeploying there.
*   **THE NETFLOW TEMPLATE DELAY:** After restarting a collector, dashboards will show **zero data** for the first 1-5 minutes for Juniper devices.
    *   *Why:* Logstash must wait for the hardware to send a "NetFlow Template" before it can decode traffic. 
    *   *Action:* Grab a coffee and wait; do not assume the service is broken if `docker ps` is up.
*   **SSL WARNINGS:** For internal TeleHouse convenience, this setup uses self-signed certificates. 
    *   Always use `curl -k` and `ssl_verification_mode => none`.
*   **MANDATORY CERTIFICATE TRANSFER:** The `deploy.sh` script generates certificates on the Frontend, but **does not** automatically send them to Backends. 
    *   *Action:* You must manually copy the `certs/` folder to every Backend server:
    `scp -r ~/custom-elk-stack/certs thsadmin@{YOUR_BACKEND_IP}:~/custom-elk-stack/`

---

## Architecture

- **Frontend ({YOUR_FRONTEND_IP})**:
  - 2x Elasticsearch Nodes (Master/Data Role)
  - 1x Kibana (Port 5601)
  - Manages ILM policies and Index Templates.
- **Backends ({YOUR_BACKEND_IP_1}, {YOUR_BACKEND_IP_2})**:
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

## 🛠 Setup & Deployment (Step-by-Step)

Follow these steps in the exact order listed. Skipping steps or changing the order will lead to cluster synchronization failures.

### Phase 0: Prerequisites
Ensure all participating servers (Frontend and Backends) meet the following requirements:
*   **Docker & Docker Compose:** Installed and running (`docker compose version` should return >2.20).
*   **Operating System:** Linux (Ubuntu/Debian recommended).
*   **Networking:** Port **9300** and **9301** must be open between all nodes for cluster communication.
*   **Hardware:** Minimum 8GB RAM per node (ES requires significant heap memory).

### Phase 1: Global Configuration (On Frontend Node)
1.  Clone this repository to the server intended to be the **Frontend (87)**.
2.  Generate the base configuration template:
    ```bash
    ./deploy.sh --generate
    ```
3.  Edit the generated `deploy.conf` using `nano` or `vi`:
    *   `FRONTEND_IP`: The static IP of the current server.
    *   `BACKEND_IPS`: Comma-separated list of all other nodes (e.g., `10.4.4.21,10.4.4.90`).
    *   `ELASTIC_PASSWORD`: Set your secure cluster password.
    *   *Note:* The script will automatically generate Kibana encryption keys for you during this step.

### Phase 2: Mastering the Cluster (Deploy Frontend)
1.  Execute the frontend deployment:
    ```bash
    ./deploy.sh --frontend
    ```
2.  **What this does automatically:**
    *   Creates a `.env` file with your credentials.
    *   Generates `unicast_hosts.txt` (The cluster's phonebook).
    *   **Generates SSL Certificates:** Creates the Root CA and Wildcard keys in the `./certs` folder.
    *   Starts Elasticsearch (2 nodes) and Kibana.
    *   Applies the 10GB ILM policies and Index Templates via API.
    *   Bootstraps the first serialized index (`-000001`).
    *   Installs the hourly maintenance cron job.

### Phase 3: The Diplomatic Mission (Certificate Transfer)
**CRITICAL:** The backends cannot join the cluster without the keys generated in Phase 2.
1.  From the Frontend node, securely copy the project files to the Backend nodes:
    ```bash
    # Run once for each backend
    scp -r ~/custom-elk-stack {USER}@{BACKEND_IP}:~/
    ```
2.  Verify that the `~/custom-elk-stack/certs` directory exists and is populated on the backend servers.

### Phase 4: Setting up Remote Nodes (Deploy Backends)
Perform these steps on **each** Backend server:
1.  **Check the UID Trap:**
    Run `id`. If your UID is **not 1000** (e.g., it is `1003`):
    *   Open `docker-compose-backend.yml`.
    *   Find the `logstash` service.
    *   Uncomment and set `user: "1003:1003"` to match your system.
2.  **Initialize the Node:**
    ```bash
    ./deploy.sh --backend
    ```
3.  **Automatic Discovery:** The script will detect the local IP, create a specific `.env` file, and point the node back to the Frontend master. The node will join the cluster and immediately begin readying the collectors.

### Phase 5: Verification & Dashboards
1.  **Check Cluster Health:** On the Frontend, run:
    ```bash
    curl -k -u elastic:{YOUR_PASSWORD} https://localhost:9200/_cat/nodes?v
    ```
    *All nodes should be visible and listed as 'di' or 'dim'.*
2.  **Import Visualizations:** On the Frontend, run:
    ```bash
    ./deploy.sh --import
    ```
3.  **Access UI:** Open `http://{FRONTEND_IP}:5601` in your browser. Log in as `elastic`.

### Phase 6: Final Audit
Use these commands on the **Frontend** server to verify that all automation (ILM, Cron, Dashboards) is functioning correctly:

*   **Check ILM Policy:**
    ```bash
    curl -k -u elastic:{ELASTIC_PASSWORD} -X GET "https://localhost:9200/_ilm/policy/logstash-flow-policy?pretty"
    ```
*   **Check Maintenance Cronjob:**
    ```bash
    crontab -l
    ```
*   **Verify Dashboard Import:**
    ```bash
    curl -s -u elastic:{ELASTIC_PASSWORD} -X GET "http://localhost:5601/api/saved_objects/_find?type=dashboard" -H "kbn-xsrf: true"
    ```

---

## Scaling: Adding Multiple Netflow Devices

Adding new switches (e.g., a new Juniper at {NEW_SWITCH_IP}) is now automatic:

1.  **Configure Switch**: Point NetFlow v9 exports to your Backend IP on port **2050**.
2.  **IP Identification:** Because we use `network_mode: host` or the `netflow.exporter.ipv4_address` field, devices are labeled by their real Management IP, not Docker's bridge IP.
3.  **Multipliers (Optional)**: If the new switch has a different sampling rate, update the `dictionary` in `logstash-unified.conf`:
    ```ruby
    dictionary => {
      "{SWITCH_IP}" => "4096",
      "{NEW_SWITCH_IP}" => "2048"
    }
    ```

---

## Common Troubleshooting

**Error: "Fielddata is disabled"**
- **Cause:** A field was accidentally mapped as `text` (likely in a new index created without the template).
- **Fix:** Re-apply the frontend template and manually rollover the index:
  `curl -k -u elastic:telehouse -X POST "https://{YOUR_FRONTEND_IP}:9200/logstash-flow-write/_rollover"`

**Data Missing After Restart?**
- Check `docker logs logstash-flow`. If you see "Can't (yet) decode flowset...", just wait for the switch template to arrive.

---

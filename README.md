# TH Customised ELK Stack

A specialized, in-house monitoring solution designed for distributed environments. This project implements a **"Hub-and-Spoke"** architecture utilizing **ELK Stack 9.2.4**, enabling centralized visualization with decentralized data ingestion.

---

##  Architecture Overview

This solution separates the visualization layer (Frontend) from the data ingestion layer (Backend).

- **Frontend (The Hub):** Hosts Kibana and a lightweight Elasticsearch instance for metadata and internal logs. It acts as the central gateway for Cross-Cluster Search (CCS).
- **Backend (The Spokes):** Distributed nodes running Elasticsearch and Logstash to ingest and store local Netflow data.

---

## Project Structure

```plaintext
.
├── elastic-frontend/
│   ├── certs/                 # Generated SSL certificates
│   ├── config/                # Kibana & Elasticsearch YAML configs
│   ├── data/                  # Persistent volume for metadata
│   ├── docker-compose.yml     # Frontend service definition
│   ├── generate-certs.sh      # PKI automation script
│   └── run.sh                 # Initialization & startup script
└── elastic-backend/
    ├── config/                # Elasticsearch node configs
    ├── data/                  # Local ingestion data storage
    ├── logstash_pipeline/
    │   └── netflow.conf       # Logstash ingestion logic
    └── docker-compose.yml     # Backend service definition

```

---

##  Getting Started

### 1. Prerequisites

On both Frontend and Backend servers, you must increase the memory map count for Elasticsearch to initialize properly:

```bash
sudo sysctl -w vm.max_map_count=262144

```

### 2. Certificate Generation

The `generate-certs.sh` script manages SSL for the entire cluster.

1. Give execution permissions: `chmod +x generate-certs.sh`
2. Edit the script (from line 20) to define your nodes. Use a unique `name` (cluster name) for every backend server.

**Example Configuration:**

```yaml
instances:
  - name: es-frontend
    dns: ["es-frontend", "localhost"]
    ip: ["127.0.0.1"]
  - name: es-server-01
    dns: ["es-server-01"]
    ip: ["1.2.3.4"]
  - name: bistrica-pod
    dns: ["bistrica-pod"]
    ip: ["4.5.6.7"]

```

 Run the script and distribute the generated folders in `./certs` to their respective backend servers.

### 3. Frontend account token generation

Running the frontend ```docker-compose.yml``` file for the first time requires the creation of a kibana access token. This can be achieved in the following way:

1. From the directory of the frontend compose file start up only the elasticsearch container:

```bash
docker compose up -d es-frontend
```
2. Use the built-in binary inside the container to create a new service token:

```bash
docker exec -it es-frontend /usr/share/elasticsearch/bin/elasticsearch-service-tokens create elastic/kibana kibana-token
```
 The output should be similar to: ```SERVICE_TOKEN elastic/kibana/kibana-token = AOIUSGHDAWLDAWD....```
 Copy the token value, which follows the equal sign.
3. Edit the compose file to include the token:
Find the line ```- ELASTICSEARCH_SERVICEACCOUNT_TOKEN= #Put your token here``` and place the token value before the comment.
Here is an example of how the line should look:

```yaml
- ELASTICSEARCH_SERVICEACCOUNT_TOKEN=AOIUSGHDAWLDAWD.... #Put your token here
```
4. Start up the kibana frontend container ( **WITHOUT** shutting down the currently running elasticsearch container )
   
```bash
 docker compose up -d kibana-frontend
```

### 4. Frontend Deployment

Navigate to `elastic-frontend/` and execute the startup script:

```bash
./run.sh

```

*Note: run.sh automatically optimizes the JVM heap size before starting containers.*

---

##  Cross-Cluster Search (CCS) Setup

Once your backend nodes are live, "adopt" them into the Frontend via the **Kibana Dev Tools Console**:

```http
PUT _cluster/settings
{
  "persistent": {
    "cluster": {
      "remote": {
        "site_a": {
          "seeds": ["10.0.0.10:9300"]
        },
        "site_b": {
          "seeds": ["10.0.0.20:9300"]
        }
      }
    }
  }
}

```

### Querying Data

Use the following index pattern syntax in Kibana to target specific locations or the entire network:

| Goal |Index Pattern in Kibana
|--- | --- 
|**Search Site A only**|`site_a:netflow-data-*`
|**Search Site B only**|`site_b:netflow-data-*`
|**Search ALL Sites**|`*:netflow-data-*`
---

##  Adding a New Monitoring Server (Spoke)

To scale the solution, follow these steps for every new server:

1. **System Prep:** Install Docker and set `vm.max_map_count`.
2. **Certs:** Update `instances.yml` on the **Frontend**, re-run `generate-certs.sh`, and copy the new certificate folder to the new node.
3. **Config:** In the backend `docker-compose.yml`:

   - Set a unique `cluster.name` (e.g., `backend-site-c`).
   - Map the volume to the new certs: `- ./certs/es-backend-site-c:/usr/share/elasticsearch/config/certs`.
4. **Logstash:** Update the output block to point to the `localhost` Elasticsearch container.
5. **Networking:** Allow **UDP 2055** for incoming Netflow.

   - Allow **TCP 9300** (Restricted to Frontend IP only).
6. **Register:** Run the `PUT _cluster/settings` command on the Frontend.

---

##  Pro Tip: Data Views & Tagging

To make global dashboards more intuitive, add a location identifier in the Logstash filter of each backend:

```ruby
filter {
  mutate {
    add_field => { "data_source_location" => "London_Data_Center" }
  }
}

```

This allows you to build **Map Visualizations** that display exactly which physical location handled a specific flow, even when using the global `*:netflow-data-*` pattern.

---



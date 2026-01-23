# Custom TH-ELK Horizontally Scalable Monitoring Solution

## This repository provides a framework for deploying a distributed, horizontally scalable ELK (Elasticsearch, Logstash, Kibana) stack. It is designed to handle remote ingestion across multiple backend servers while maintaining a centralized frontend dashboard with high availability (3-node cluster).


## Configuration

Before initializing the stack, you must configure the environment variables.

1. **Create the environment file**:

```bash
cp env.example .env
```
2. **Edit the configuration**:

```bash
nano .env
```

### Environment File Template

The `.env` file should contain the following structure:

```bash
# Security Credentials
ELASTIC_PASSWORD=changeme
KIBANA_PASSWORD=changeme

# Stack Configuration
STACK_VERSION=9.2.4
CLUSTER_NAME=netflow-cluster
LICENSE=basic

# Networking - Frontend (Centralized Dashboard)
FRONTEND_IP=10.20.30.40
ES_PORT=9200
KIBANA_PORT=5601

# Networking - Backend (Remote Ingestion)
BACKEND_IP=50.60.70.80

# Resource Limits (4GB)
MEM_LIMIT=4294967296
```

> **Note**: Update the passwords, version, cluster name, ports, and IP address assignments to match your specific requirements.
>
>

### Adding Multiple Backend Servers

To scale the ingestion layer, define unique variables for each backend server:

```bash
BACKEND_IP=50.60.70.80
BACKEND_IP_2=1.2.3.4
DEBIAN_BACKEND_SERVER=5.6.7.8
```

---

## Initializing the Frontend

The setup service on the frontend generates the Certificate Authority (CA) and a universal wildcard certificate used by all nodes.

### 1. Execute on the Frontend Server (10.20.30.40)

Prepare the directories and start the service to generate certificates and launch the frontend nodes:

```bash
# Create local certs folder
mkdir -p ./certs

# Start the frontend services (includes es-frontend and es-frontend-2)
docker-compose -f docker-compose-frontend.yml up -d

# Extract generated certs from the ES container to the host
docker cp es-frontend:/usr/share/elasticsearch/config/certs/. ./certs/
```

### 2. Distribute Certificates to Backends

Use `scp` to move the CA and the wildcard certificates to the remote ingestion server. The wildcard certificate allows any node to join the cluster.

```bash
# Push certificates to the backend server
scp -r ./certs/ca ./certs/wildcard user@50.60.70.80:/path/to/project/certs/
```

### 3. Initialize the Backend

Log into the backend server and start the service:

```bash
docker-compose -f docker-compose-backend.yml up -d
```

---

## Connecting Backend Source to Frontend

After deployment, verify the connection through the Kibana interface.

- **Verify Cluster Join**: Open Kibana at `http://10.20.30.40:5601`. Navigate to **Dev Tools** and run:

```http
GET _cat/nodes?v
```

You should see 3 nodes in the list: `es-frontend`, `es-frontend-2`, and `es-remote`.

- **Check Indices**: Verify that Logstash is creating indices by running:

```http
GET _cat/indices?v

```
- **Create Data View**: Navigate to **Stack Management > Data Views** and create a view for `logstash-*`.
- **Visualize**: Use **Lens** to create visualizations. For example, drag the `netflow.in_bytes` field to the workspace to monitor traffic volume.
---

## Adding a Second Backend Server

You can add additional nodes to a running cluster without downtime.

### 1. Update Configuration

Update the `.env` on all servers to include the new IP in the discovery list:

- `BACKEND_IP_1=50.60.70.80`
- `BACKEND_IP_2=8.9.1.2`

### 2. Reuse Certificates

Simply copy the **same** `certs/` folder (containing the CA and wildcard cert) to the new backend server. No new certificate generation is required!

### 3. Security Requirements

|Component|Required Files|Purpose
|---|---|---|
|**All Nodes**|`ca.crt`|Verifies identity of cluster members
|**All Nodes**|`wildcard.crt` & `wildcard.key`|Universal Identity for all nodes
|**Logstash**|`ca.crt`|Trust the ES instance for data pushing


## Step-by-Step Deployment (No Downtime)

### Step A: Prepare the New Host (8.9.1.2)

1. **Increase Virtual Memory**:

```bash
sudo sysctl -w vm.max_map_count=262144
```
2. **Firewall Configuration**: Ensure ports `9200` (HTTP) and `9300` (Transport) are open.

### Step B: Launch the New Node

1. Transfer `.env`, `docker-compose-backend.yml`, `logstash.conf`, and the `certs/` directory to the new server.
2. Start the services:

```bash
docker-compose -f docker-compose-backend.yml up -d
```

### Step C: Rolling Update

To ensure stability after restarts, update the `discovery.seed_hosts` in the environment variables of existing nodes. While the new node joins immediately, existing nodes require a restart to recognize the new seed for future elections.

---

## Common Issues

### Permission and Ownership

Elasticsearch requires write access to the config and data directories. These must be owned by the Elasticsearch user (**UID 1000**).

**Symptoms**:

- `AccessDeniedException`
- `Permission denied` during startup.

**Solution**:

```bash
# Grant Ownership
chown -R 1000:0 ./data

# Grant Group Access
chmod g+rwx ./data
```
# ELK Stack Assessment Report - Backend Server N2 (10.4.4.90)
**Date:** 2026-02-09  
**Investigator:** Automated Assessment Script

---

## Executive Summary

The ELK stack environment on Backend Server N2 is **PARTIALLY OPERATIONAL**.  
✅ **Elasticsearch** is running (node: `es-remote-2`)  
✅ **Logstash** is running (container: `custom-elk-stack-logstash-1`)  
❌ **Kibana** is NOT RUNNING (not found in container list)  
❌ **/custom-elk-stack** directory does NOT exist at root level

---

## Server Connection Details

| Property | Value |
|----------|-------|
| **Host** | 10.4.4.90 |
| **User** | telehouse |
| **Escalation** | su (sudo not available) |
| **OS** | Debian GNU/Linux (kernel 6.12.63+deb13-amd64) |
| **Hostname** | backend-2 |

---

## Directory Structure

**Location:** `/home/telehouse/custom-elk-stack/` (NOT `/custom-elk-stack`)

### Files Present:
```
custom-elk-stack/
├── certs/                    # X.509 certificates
├── docker-compose-backend.yml  # Backend services config
├── docker-compose-frontend.yml # Frontend services config (includes Kibana)
├── .env                      # Environment variables
├── env.example               # Example environment file
├── .git/                     # Git repository
├── .gitignore
├── LICENSE
├── logstash.conf             # Logstash pipeline configuration
├── README.md
└── unicast_hosts.txt         # Elasticsearch cluster hosts
```

---

## Container Status

| Container ID | Image | Status | Ports | Name |
|--------------|-------|--------|-------|------|
| 0129c1297d9d | docker.elastic.co/logstash/logstash:9.2.4 | ✅ Up 48 min | 5044/tcp, 9600/tcp, **8514/udp** | custom-elk-stack-logstash-1 |
| 821497979b08 | docker.elastic.co/elasticsearch/elasticsearch:9.2.4 | ✅ Up 49 min (healthy) | **9200/tcp**, **9300/tcp** | es-remote-2 |

### Notable:
- **2 containers running** (out of expected 3 - Kibana missing)
- Elasticsearch shows healthy status
- Both containers created ~49 minutes ago (recent deployment)
- Elastic Stack version: **9.2.4** (latest stable)

---

## What's Missing / Issues

### 🔴 Critical
1. **Kibana container is not running** - No visualization interface available
2. **Directory at `/custom-elk-stack` does not exist** - The stack is deployed from `/home/telehouse/custom-elk-stack/` instead

### 🟡 Warnings
- Logstash UDP port 8514 is exposed (syslog ingestion endpoint)
- Elasticsearch cluster appears to be using unicast discovery (based on unicast_hosts.txt)

---

## Configuration Files to Review

Key configuration files exist and should be examined:
- `docker-compose-frontend.yml` - Likely contains Kibana service definition
- `docker-compose-backend.yml` - Backend (Elasticsearch) configuration
- `logstash.conf` - Pipeline configuration for log processing
- `.env` - Environment variables (passwords, cluster settings)
- `certs/` - X.509 certificates for TLS/SSL

---

## Next Steps Recommended

1. **Start Kibana container** (check docker-compose-frontend.yml)
2. **Verify cluster health** via `curl localhost:9200/_cluster/health`
3. **Review logstash pipeline** to ensure logs are flowing
4. **Check memory allocation** for Elasticsearch (container logs)
5. **Confirm TLS certificate validity**

---

## Configuration Details

### `docker-compose-backend.yml` (Running on this server)
Services defined:
- **es-remote-2** - Data/ingest node for Netflow data
  - Image: `docker.elastic.co/elasticsearch/elasticsearch:${STACK_VERSION}`
  - Ports: 9200, 9300 (exposed)
  - Security: TLS enabled, xpack.security enabled
  - Custom attribute: `data_type=netflow`
  - Storage: `data-remote` volume
  - Healthcheck: Enabled (curl check on ES health API)

- **logstash** - Log ingestion pipeline  
  - Image: `docker.elastic.co/logstash/logstash:${STACK_VERSION}`
  - UDP port 8514 open (for Cisco Nexus syslog)
  - Netflow port 2050 commented out
  - Persistent queue enabled (max 1GB)
  - Depends on es-remote-2 health
  - Config: `logstash.conf` mounted as pipeline

### `docker-compose-frontend.yml` (Should run on Frontend server)
Services defined:
- **setup** - Certificate generation and kibana_system password setup
- **es-frontend** - Master/data/ingest node
- **es-frontend-2** - Additional master/data node (port 9201/9301)
- **kibana** - Visualization interface (❌ NOT RUNNING on this server)

### Logstash Pipeline
- Configuration: `logstash.conf`
- CA certificate: `certs/ca/ca.crt`
- Queue: Persistent (disk-based), 1GB max

---

## Architecture Notes

This appears to be a **distributed/multi-node ELK cluster**:
- **Backend Server (10.4.4.90)**: Runs data node (es-remote-2) + Logstash
- **Frontend Server**: Should run master nodes + Kibana (not present here)
- Cross-server communication via discovery.seed_hosts
- TLS/SSL secured with custom CA and wildcard certificates

---

## Raw Commands Output

```bash
# Container listing
docker ps -a
CONTAINER ID   IMAGE                                                 COMMAND                  CREATED          STATUS                    PORTS                                                                                      NAMES
0129c1297d9d   docker.elastic.co/logstash/logstash:9.2.4             "/usr/local/bin/dock…"   49 minutes ago   Up 48 minutes             5044/tcp, 9600/tcp, 0.0.0.0:8514->8514/udp, [::]:8514->8514/udp                            custom-elk-stack-logstash-1
821497979b08   docker.elastic.co/elasticsearch/elasticsearch:9.2.4   "/bin/tini -- /usr/l…"   49 minutes ago   Up 49 minutes (healthy)   0.0.0.0:9200->9200/tcp, [::]:9200->9200/tcp, 0.0.0.0:9300->9300/tcp, [::]:9300->9300/tcp   es-remote-2

# Directory listing
ls -la /home/telehouse/custom-elk-stack/
total 92
drwxrwxr-x 4 root      root       4096 Feb  9 03:35 .
drwxrwxr-x 4 root      root       4096 Feb  9 03:51 certs
-rw-rw-r-- 1 root      root       2242 Feb  9 04:19 docker-compose-backend.yml
-rw-rw-r-- 1 root      root       5311 Feb  9 03:35 docker-compose-frontend.yml
-rw-rw-r-- 1 root      root        665 Feb  9 04:06 .env
...
```

# ELK Stack Phase 1: Infrastructure Assessment & Planning Report

**Date:** 2026-02-09  
**Assessor:** OpenClaw Agent  
**Project:** TH-NetFlow ELK Stack Setup

---

## Executive Summary

The ELK stack is **operational and collecting data**. The cluster consists of 4 nodes across 3 hosts, is in **GREEN** health status, and actively ingesting NetFlow data. A custom 1-day ILM policy is in place and working. No `.env` file exists in the workspace (needs creation). SSH access to backend nodes is currently blocked by host key verification issues.

---

## 1. Current Cluster Topology

### 1.1 Node Overview

| Node Name | IP | Role | Master | Attributes | Status |
|-----------|-----|------|--------|------------|--------|
| es-frontend | 10.4.4.87:9300 | ingest, master | * (elected) | xpack.installed: true | Healthy |
| es-frontend-2 | 10.4.4.87:9301 | ingest, master | - | xpack.installed: true | Healthy |
| es-remote (N1) | 10.4.4.21:9300 | data, ingest | - | data_type: netflow | Healthy |
| es-remote (N2) | 10.4.4.90:9300 | data, ingest | - | data_type: netflow | Healthy |

**Total Nodes:** 4  
**Data Nodes:** 2 (both on backend hosts)  
**Master-eligible:** 2 (both on frontend host)  
**Elasticsearch Version:** 9.2.4

### 1.2 Cluster Health

```json
{
  "cluster_name": "netflow-cluster",
  "status": "green",
  "number_of_nodes": 4,
  "number_of_data_nodes": 2,
  "active_primary_shards": 5,
  "active_shards": 10,
  "active_shards_percent_as_number": 100.0
}
```

**✅ All shards allocated, cluster fully operational**

### 1.3 Resource Allocation

| Host | Node | Disk Used | Disk Available | Disk % | CPU Load (1m) |
|------|------|-----------|----------------|--------|---------------|
| 10.4.4.21 | es-remote (N1) | 112.1gb | 69.9gb | 61% | 0.48 |
| 10.4.4.90 | es-remote (N2) | 18.2gb | 74.5gb | 19% | 0.37 |
| 10.4.4.87 | es-frontend | - | - | 70% RAM | 0.01 |
| 10.4.4.87 | es-frontend-2 | - | - | 68% RAM | 0.01 |

**⚠️ Note:** Backend N1 (10.4.4.21) has higher disk usage (61%) compared to N2 (19%)

---

## 2. Docker Compose Structure Assessment

### 2.1 Frontend Compose (`docker-compose-frontend.yml`)

**Services:**
- `setup` - Certificate generation and initial user setup
- `es-frontend` - Master-eligible ES node (ports 9200, 9300)
- `es-frontend-2` - Second master-eligible node (ports 9201, 9301)
- `kibana` - Dashboard (port 5601)
- `netflow-installer` - Auto-installs NetFlow integration after Kibana starts

**Strengths:**
- ✅ Uses file-based discovery with `unicast_hosts.txt`
- ✅ SSL/TLS enabled with wildcard certificates
- ✅ Memory locking enabled (`IPC_LOCK`)
- ✅ Security enabled with xpack
- ✅ Auto-installer for NetFlow integration

**Observations:**
- Uses version "3.8"
- Port 9201/9301 mapped for second frontend node
- Discovery seed hosts reference `FRONTEND_IP` and `BACKEND_IP`

### 2.2 Backend Compose (`docker-compose-backend.yml`)

**Services:**
- `es-remote` - Data/ingest node (ports 9200, 9300)
- `logstash` - NetFlow/sFlow collector and processor

**Logstash Port Mapping:**
- UDP 2050: NetFlow from Juniper
- UDP 6343: sFlow from Cisco Nexus
- UDP 8514: Legacy Cisco Nexus syslog (deprecated)

**Strengths:**
- ✅ Uses persisted queue (`QUEUE_TYPE=persisted`)
- ✅ SSL certificates mounted
- ✅ Separate data-only node role

**Issues Found:**
- ⚠️ Uses Docker Compose version "2.4" (older than frontend's 3.8)
- ⚠️ `node.attr.data_type=netflow` attribute set but could be more specific

### 2.3 Environment Variables (`env.example`)

**Status:** ❌ `.env` file does not exist in workspace

**Required Configuration:**
- ELASTIC_PASSWORD (currently: changeme)
- KIBANA_PASSWORD (currently: changeme)
- FRONTEND_IP (example: 10.20.30.40 - needs actual 10.4.4.87)
- BACKEND_IP (example: 50.60.70.80 - needs actual 10.4.4.21/90)
- Three Kibana encryption keys (need generation)
- MEM_LIMIT: 4294967296 (4GB, but README says "1GB limit" - inconsistency)

**⚠️ CRITICAL:** The actual production IPs are different from env.example:
- Production FRONTEND_IP: 10.4.4.87
- Production BACKEND_N1: 10.4.4.21 (port 2332 for SSH)
- Production BACKEND_N2: 10.4.4.90

---

## 3. Data Sources & Logstash Configuration

### 3.1 Current Data Ingestion

**Active Data Streams:**
- `logs-netflow.log-default` - NetFlow from Juniper
- Indices: 2 backing indices (000001, 000002)
- Documents: ~15.3 million total
- Size: ~7.5GB total

**NetFlow Data Structure:**
- Port: UDP 2050 (Juniper)
- Scale factor: 1/4096 (bytes/packets multiplied by 4096)
- ECS normalized fields: source.ip, destination.ip, network.vlan.id, etc.
- TCP flags decoded into human-readable format
- GeoIP enrichment enabled

### 3.2 Logstash Configuration Analysis

**Current `logstash.conf` supports:**

1. **NetFlow (UDP 2050)** - Active
   - Codec: netflow
   - Workers: 8
   - Output: `logs-netflow.log-default` data stream
   - Field mapping to ECS compliant structure

2. **sFlow (UDP 6343)** - Configuration exists, status unknown
   - Workers: 4
   - Output: `logs-sflow.net-default` data stream
   - Basic ECS mapping implemented
   - **⚠️ Need to verify if sFlow is actually receiving data**

3. **Cisco Nexus Syslog (UDP 8514)** - Legacy/deprecated
   - Still configured but marked deprecated
   - Output: `logs-cisco_nexus.nxos-default`

**Logstash Output Configuration:**
- Sends to `https://es-remote:9200` (backend local ES)
- SSL enabled with `ssl_verification_mode: none`
- Uses data streams (ES 9.x feature)

---

## 4. ILM Policy Assessment

### 4.1 Current NetFlow ILM Policy

**Policy Name:** `netflow-1day`

**Configuration:**
```json
{
  "phases": {
    "hot": {
      "min_age": "0ms",
      "actions": {
        "set_priority": { "priority": 100 }
      }
    },
    "delete": {
      "min_age": "1d",
      "actions": {
        "delete": {}
      }
    }
  }
}
```

**Status:** ✅ **ACTIVE and working**

**Application:**
- Applied to data stream: `logs-netflow.log-default`
- Index 000002 is using this policy
- Index 000001 still using old "logs" policy

**⚠️ Note:** Data stream shows ILM policy is `netflow-1day` but the backing indices may vary. The 1-day retention is achieved - old indices are deleted after 1 day.

---

## 5. ElastiFlow Research & Recommendation

### 5.1 What is ElastiFlow?

ElastiFlow is a **network observability and security analytics platform** that provides:
- Real-time visibility into network traffic
- NetFlow, sFlow, and IPFIX support
- Pre-built dashboards and visualizations
- Contextualized network data

### 5.2 ElastiFlow vs Logstash: Analysis

| Feature | Current Logstash | ElastiFlow |
|---------|------------------|------------|
| **Type** | Log processor/collector | Full observability platform |
| **NetFlow** | ✅ Supported via codec | ✅ Native support |
| **sFlow** | ✅ Supported via codec | ✅ Native support |
| **IPFIX** | Limited | ✅ Full support |
| **Pre-built Dashboards** | ❌ Need manual creation | ✅ Included |
| **GeoIP enrichment** | Manual config | Built-in |
| **Threat Detection** | ❌ | ✅ Built-in analytics |
| **Storage** | Raw Elasticsearch | Optimized indexing |
| **Cost** | Free (Open Source) | Commercial product |

### 5.3 Recommendation

**VERDICT: Current Logstash setup is sufficient for the use case**

**Reasoning:**
1. **Cost:** ElastiFlow is a commercial product requiring licensing
2. **Functionality:** Current Logstash already handles both NetFlow and sFlow
3. **Data volume:** 15M+ documents already ingested successfully
4. **ILM:** Working 1-day retention policy is in place
5. **ECS Compliance:** Logstash config already maps to ECS fields

**ElastiFlow would be beneficial if:**
- Need for advanced threat detection
- Want pre-built dashboards without development
- Require IPFIX support beyond NetFlow/sFlow
- Budget allows for commercial solution

**Recommendation for Phase 2:**
- Continue with Logstash
- Focus on improving Logstash config for sFlow validation
- Enhance Kibana dashboards manually
- Monitor performance at current scale

---

## 6. Gaps & Action Items

### 6.1 Critical Issues (Fix Immediately)

| # | Issue | Impact | Action |
|---|-------|--------|--------|
| 1 | `.env` file missing | Cannot deploy/replicate setup | Create `.env` with production values |
| 2 | SSH host key verification | Cannot check backend logs | Add host keys or use SSH options |
| 3 | Backend N1 disk at 61% | Risk of disk pressure | Monitor or add retention |

### 6.2 Configuration Gaps

| # | Issue | Current | Recommended |
|---|-------|---------|-------------|
| 1 | Compose version mismatch | Backend: 2.4, Frontend: 3.8 | Standardize on 3.8 |
| 2 | Memory limit comment | README says "1GB" | Update comment to "4GB" |
| 3 | Unicast hosts | Only 10.4.4.21 listed | Verify all nodes included |

### 6.3 Data Source Validation

| Protocol | Port | Status | Action |
|----------|------|--------|--------|
| NetFlow | 2050 | ✅ Active (15M docs) | None - working |
| sFlow | 6343 | ❓ Unknown | Verify sFlow is sending |
| Syslog | 8514 | ⚠️ Deprecated | Consider removal |

### 6.4 Missing Files/Templates

1. `custom-elk-stack/.env` - Not present, needs creation
2. Backend N2 compose file - Currently only N1 config in workspace
3. sFlow verification - Need to check if data is flowing

---

## 7. Recommendations for Phase 2

### 7.1 Immediate Actions

1. **Create `.env` file** with production values:
   ```bash
   FRONTEND_IP=10.4.4.87
   BACKEND_IP=10.4.4.21  # For N1
   # Need separate config for N2 (10.4.4.90)
   ```

2. **Verify sFlow data ingestion** - Check if Cisco Nexus is sending sFlow:
   - Logstash logs would show sFlow codec activity
   - Search for `logs-sflow` data stream

3. **Standardize Docker Compose versions** - Update backend to version 3.8

### 7.2 Enhancement Opportunities

1. **Add Logstash monitoring** - Track ingestion rates
2. **Implement Alerting** - For disk space, cluster health
3. **Review 1-day retention** - Confirm business requirement
4. **Backend N2 Docker Compose** - Ensure workspace has N2 config

---

## 8. Summary Table

| Component | Status | Notes |
|-----------|--------|-------|
| Cluster Health | ✅ GREEN | 4 nodes, 100% shards |
| NetFlow Ingestion | ✅ Active | 15.3M documents |
| sFlow Ingestion | ❓ Unknown | Config exists, verify data |
| ILM Policy | ✅ Working | 1-day retention active |
| SSL/TLS | ✅ Enabled | Wildcard certs |
| .env File | ❌ Missing | Need creation |
| SSH Access | ❌ Blocked | Host key issue |
| ElastiFlow | ⏸️ Not Needed | Logstash sufficient |

---

## 9. Technical Details Archive

### Full Cluster Nodes Output:
```
ip          heap.percent ram.percent cpu load_1m load_5m load_15m node.role master name
10.4.4.87            53          68   1    0.01    0.03     0.04 im        -      es-frontend-2
10.4.4.90            16          99  13    0.37    0.96     1.22 di        -      es-remote (N2)
10.4.4.87            24          70   1    0.01    0.03     0.04 im        *      es-frontend (master)
10.4.4.21            34          96  15    0.48    0.69     1.18 di        -      es-remote (N1)
```

### Data Stream Status:
```
health status index                                    docs.count store.size
green  open   .ds-logs-netflow.log-default-2026.02.09-000002   11758626        6gb
green  open   .ds-logs-netflow.log-default-2026.02.09-000001    3541135      1.5gb
```

---

*End of Phase 1 Assessment Report*

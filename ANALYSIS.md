# VB: Initial Analysis and Project Understanding

**Date:** 2026-02-09  
**Analyst:** Valentin-bot

---

## Architecture Understanding

### Current Design (From Documentation)
- **Frontend (10.4.4.87)**: Kibana + 2 ES frontend nodes (master + data roles)
- **Backend N1 (10.4.4.21)**: Logstash + ES data node, receiving NetFlow on UDP 2050 from Juniper
- **Backend N2 (10.4.4.90)**: TBD - likely similar to Backend N1
- **Data Sources**: 
  - Juniper switch → NetFlow v5/v9 on UDP 2050 (WORKING)
  - Cisco Nexus switches (10.4.4.3, 10.4.4.4) → Syslog on UDP 8514 (NOT WORKING)

### Key Requirements from Viktor
1. ✅ **Frontend does NOT store device data** - currently violated in docker-compose-frontend.yml
2. ✅ **No sharding/replication across cluster** - need to verify
3. ✅ **Each Logstash stores data on its own local ES** - current design has this
4. ❌ **ILM with 1-day data retention** - not yet implemented
5. ❌ **Cisco Nexus syslog ingestion** - not working yet
6. ✅ **Version 9.2.4** - configured correctly

### Issues Identified

#### Issue 1: Frontend Data Storage
The frontend ES nodes currently have `node.roles=master,data,ingest` which means they WILL store data. According to requirements, frontend should NOT keep device data.

**Fix needed:** Change frontend roles to `master,ingest` (remove `data`)

#### Issue 2: Missing ILM Configuration
No Index Lifecycle Management is configured. Need to add ILM policy for 1-day retention.

**Fix needed:** Create ILM policy and apply to data streams

#### Issue 3: Cisco Nexus Not Sending Logs
TBD - need to investigate switch configuration and connectivity

---

## Connection Information

**Note:** Credentials and full connection details are maintained separately. Contact Viktor or check the local `.credentials` file for access information.

### Servers
- **Frontend (10.4.4.87)**: Kibana + ES master/coordinating nodes
- **Backend N1 (10.4.4.21:2332)**: Logstash + ES data node (NetFlow)
- **Backend N2 (10.4.4.90)**: Logstash + ES data node (Syslog)

### Network Devices
- **Juniper Router**: NetFlow v5/v9 on UDP 2050 (WORKING - do not modify)
- **Cisco Nexus 1 (10.4.4.3)**: Nexus 9000 series, Syslog UDP 8514 - **PRODUCTION - READ ONLY**
- **Cisco Nexus 2 (10.4.4.4)**: Nexus 9000 series, Syslog UDP 8514 - **PRODUCTION - READ ONLY**

**WARNING:** Cisco Nexus switches are PRODUCTION devices. Any configuration changes require explicit permission from Viktor.

---

## Next Steps

1. Connect to all 3 servers to assess current state
2. Check existing configurations in `/custom-elk-stack` directories
3. Fix frontend node roles to prevent data storage
4. Implement ILM policy for 1-day retention
5. Troubleshoot Cisco Nexus syslog configuration
6. Test end-to-end data flow

---

## Git Commit
VB: Initial project analysis and architecture understanding

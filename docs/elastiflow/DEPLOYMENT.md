# ElastiFlow Unified Collector Deployment

**Date:** 2026-02-12  
**Deployed by:** Valentin-bot  
**Status:** ✅ Production

## Architecture

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   Juniper SW    │     │  Cisco Nexus 1  │     │  Cisco Nexus 2  │
│   10.4.4.93     │     │    10.4.4.3     │     │    10.4.4.4     │
│   NetFlow v9    │     │    sFlow v5     │     │    sFlow v5     │
└────────┬────────┘     └────────┬────────┘     └────────┬────────┘
         │                       │                       │
         │ UDP 2050              │ UDP 6343              │ UDP 6343
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────────────────────────────────────────────────────┐
│                     Backend N1 (10.4.4.21)                       │
│              ElastiFlow Collector (NetFlow only)                 │
│                      Port: 2050 (host mode)                      │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │
┌─────────────────────────────────────────────────────────────────┐
│                     Backend N2 (10.4.4.90)                       │
│              ElastiFlow Collector (sFlow only)                   │
│                      Port: 6343 (host mode)                      │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ HTTP/HTTPS 9200
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│              Elasticsearch Cluster (10.4.4.87:9200)              │
│                    Index: elastiflow-flow-ecs-*                  │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    Kibana (10.4.4.87:5601)                       │
│              Unified Flow Dashboards & Analytics                 │
└─────────────────────────────────────────────────────────────────┘
```

## Collectors

### Backend N1 - NetFlow Collector
- **IP:** 10.4.4.21
- **SSH:** Port 2332 (telehouse/T3l3h0us#)
- **Purpose:** Receives NetFlow v9 from Juniper (10.4.4.93)
- **Port:** 2050/UDP
- **Docker Compose:** `~/elastiflow/docker-compose.yml`

### Backend N2 - sFlow Collector  
- **IP:** 10.4.4.90
- **SSH:** Port 22 (telehouse/T3l3h0us#)
- **Purpose:** Receives sFlow v5 from Cisco Nexus (10.4.4.3, 10.4.4.4)
- **Port:** 6343/UDP
- **Docker Compose:** `~/elastiflow/docker-compose.yml`

## Configuration

### Backend N1 docker-compose.yml
```yaml
version: '2'
services:
  flow-collector:
    image: elastiflow/flow-collector:7.21.0
    container_name: flow-collector
    restart: unless-stopped
    network_mode: host
    environment:
      EF_LICENSE_ACCEPTED: "true"
      EF_FLOW_SERVER_UDP_IP: "0.0.0.0"
      EF_FLOW_SERVER_UDP_PORT: "2050"
      EF_PROCESSOR_DECODE_NETFLOW9_ENABLE: "true"
      EF_OUTPUT_ELASTICSEARCH_ENABLE: "true"
      EF_OUTPUT_ELASTICSEARCH_ADDRESSES: "10.4.4.87:9200"
      EF_OUTPUT_ELASTICSEARCH_USERNAME: "elastic"
      EF_OUTPUT_ELASTICSEARCH_PASSWORD: "telehouse"
      EF_OUTPUT_ELASTICSEARCH_ECS_ENABLE: "true"
      EF_OUTPUT_ELASTICSEARCH_TLS_ENABLE: "true"
      EF_OUTPUT_ELASTICSEARCH_TLS_SKIP_VERIFICATION: "true"
```

### Backend N2 docker-compose.yml
```yaml
version: '2'
services:
  flow-collector:
    image: elastiflow/flow-collector:7.21.0
    container_name: flow-collector
    restart: unless-stopped
    network_mode: host
    environment:
      EF_LICENSE_ACCEPTED: "true"
      EF_FLOW_SERVER_UDP_IP: "0.0.0.0"
      EF_FLOW_SERVER_UDP_PORT: "6343"
      EF_PROCESSOR_DECODE_SFLOW5_ENABLE: "true"
      EF_OUTPUT_ELASTICSEARCH_ENABLE: "true"
      EF_OUTPUT_ELASTICSEARCH_ADDRESSES: "10.4.4.87:9200"
      EF_OUTPUT_ELASTICSEARCH_ECS_ENABLE: "true"
      ...
```

## Index Lifecycle Management (ILM)

**Policy:** `elastiflow`
- **Hot Phase:** 7 days or 50GB → Rollover
- **Warm Phase:** After 7 days → Shrink, Forcemerge
- **Cold Phase:** After 30 days → Set priority 0
- **Delete Phase:** After 365 days → Delete

## Verification Commands

```bash
# Check collector status
curl -u elastic:telehouse -k "https://10.4.4.87:9200/_cat/indices?v&h=index,docsCount&s=docsCount:desc"

# List devices
curl -u elastic:telehouse -k -X POST "https://10.4.4.87:9200/elastiflow-flow-*/_search?size=0" \
  -H "Content-Type: application/json" \
  -d '{"aggs":{"devices":{"terms":{"field":"host.name","size":20}}}}'

# Check container logs
sshpass -p 'T3l3h0us#' ssh -p 2332 telehouse@10.4.4.21 "docker logs flow-collector --tail 20"
```

## Network Device Configuration

### Cisco Nexus (sFlow)
```
sflow enable
sflow collector-ip 10.4.4.90 port 6343
sflow agent-ip 10.4.4.3   !(for switch 10.4.4.3)
sflow agent-ip 10.4.4.4   !(for switch 10.4.4.4)
```

### Juniper (NetFlow v9)
```
forwarding-options {
    sampling {
        input {
            rate 4096;
            run-length 1;
        }
        family inet {
            output {
                flow-server 10.4.4.21 {
                    port 2050;
                    version9 {
                        template refresh-rate 30;
                    }
                }
            }
        }
    }
}
```

## Dashboards
- **Kibana:** https://10.4.4.87:5601
- **Index Pattern:** `elastiflow-flow-ecs-*`
- **Dashboards:**
  - `unified-flow-detailed-v2` - Detailed traffic analysis
  - `unified-flow-topn-v2` - Top-N statistics

## Troubleshooting

**NetFlow templates not received:**
- Normal behavior - NetFlow v9 requires periodic template packets
- Should resolve within 5 minutes of collector startup
- Check with: `docker logs flow-collector | grep template`

**No sFlow data:**
- Verify Cisco switches: `show sflow`
- Check agent-ip is set correctly
- Verify collector port: `ss -ulnp | grep 6343`

## Credits
- **ElastiFlow:** https://docs.elastiflow.com
- **Deployment:** Valentin-bot (2026-02-12)

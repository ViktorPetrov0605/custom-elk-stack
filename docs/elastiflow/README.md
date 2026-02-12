# ElastiFlow Documentation

## Overview

ElastiFlow is a high-performance Unified Flow Collector that processes:
- **NetFlow** (v1, v5, v6, v7, v9)
- **IPFIX**
- **sFlow** (v5)
- AWS VPC Flow Logs
- Azure NSG Flow Logs

## Docker Deployment

### Image
```
elastiflow/flow-collector:7.21.0
```

### Key Ports (UDP)
- **2055** - NetFlow
- **4739** - IPFIX
- **6343** - sFlow
- **9995** - Other flow protocols

### Docker Compose Example

```yaml
services:
  flow-collector:
    image: elastiflow/flow-collector:7.21.0
    container_name: flow-collector
    restart: 'unless-stopped'
    network_mode: 'host'
    volumes:
      - /etc/elastiflow:/etc/elastiflow
      - /usr/share/elastiflow/flowcoll:/var/lib/elastiflow/flowcoll
    environment:
      EF_LICENSE_ACCEPTED: "true"
      EF_FLOW_SERVER_UDP_IP: 0.0.0.0
      EF_FLOW_SERVER_UDP_PORT: "2055,4739,6343,9995"
      
      # Enable NetFlow, sFlow, IPFIX decoding
      EF_PROCESSOR_DECODE_NETFLOW9_ENABLE: "true"
      EF_PROCESSOR_DECODE_SFLOW5_ENABLE: "true"
      EF_PROCESSOR_DECODE_SFLOW_FLOWS_ENABLE: "true"
      
      # Elasticsearch output
      EF_OUTPUT_ELASTICSEARCH_ENABLE: "true"
      EF_OUTPUT_ELASTICSEARCH_ADDRESSES: "localhost:9200"
      EF_OUTPUT_ELASTICSEARCH_USERNAME: "elastic"
      EF_OUTPUT_ELASTICSEARCH_PASSWORD: "changeme"
      EF_OUTPUT_ELASTICSEARCH_TLS_ENABLE: "false"
      
      # Index settings
      EF_OUTPUT_ELASTICSEARCH_INDEX_TEMPLATE_SHARDS: 1
      EF_OUTPUT_ELASTICSEARCH_INDEX_TEMPLATE_REPLICAS: 0
      EF_OUTPUT_ELASTICSEARCH_ECS_ENABLE: "true"
```

## Critical Environment Variables

### License
- `EF_LICENSE_ACCEPTED` - Must be "true" to run

### Input (Flow Collection)
- `EF_FLOW_SERVER_UDP_IP` - IP to listen on (0.0.0.0 for all)
- `EF_FLOW_SERVER_UDP_PORT` - Comma-separated ports (2055,6343 for NetFlow+sFlow)

### Decoders (Enable what you need)
- `EF_PROCESSOR_DECODE_NETFLOW9_ENABLE` - NetFlow v9
- `EF_PROCESSOR_DECODE_SFLOW5_ENABLE` - sFlow v5
- `EF_PROCESSOR_DECODE_IPFIX_ENABLE` - IPFIX

### Elasticsearch Output
- `EF_OUTPUT_ELASTICSEARCH_ENABLE` - "true" to enable
- `EF_OUTPUT_ELASTICSEARCH_ADDRESSES` - ES host:port
- `EF_OUTPUT_ELASTICSEARCH_USERNAME` - ES username
- `EF_OUTPUT_ELASTICSEARCH_PASSWORD` - ES password
- `EF_OUTPUT_ELASTICSEARCH_INDEX_TEMPLATE_SHARDS` - Number of shards
- `EF_OUTPUT_ELASTICSEARCH_INDEX_TEMPLATE_REPLICAS` - Number of replicas
- `EF_OUTPUT_ELASTICSEARCH_ECS_ENABLE` - Enable ECS format

## Comparison: Standard Logstash vs ElastiFlow

| Feature | Logstash + Codec | ElastiFlow |
|---------|-----------------|------------|
| sFlow parsing | ❌ No native codec | ✅ Built-in |
| NetFlow parsing | ✅ Via codec | ✅ Built-in |
| Unified schema | Manual config | Pre-built |
| Dashboards | Manual creation | Pre-built |
| Performance | Good | Optimized |
| Multiple outputs | Configurable | Multiple built-in |

## Migration from Logstash to ElastiFlow

1. Stop existing Logstash containers
2. Deploy ElastiFlow container with matching port mappings
3. Update network devices to point to ElastiFlow IP (if changed)
4. Configure Elasticsearch output to match your existing cluster
5. Import ElastiFlow Kibana dashboards

## Sources

- Docker Hub: https://hub.docker.com/r/elastiflow/flow-collector
- GitHub: https://github.com/elastiflow/elastiflow_for_elasticsearch

# Unified Flow Dashboard

Pre-built Kibana dashboard for ElastiFlow network flow analytics.

## Quick Install

```bash
cd kibana/scripts
./install-dashboard.sh [KIBANA_URL] [USERNAME] [PASSWORD]
```

**Example:**
```bash
./install-dashboard.sh http://10.4.4.87:5601 elastic telehouse
```

## Features

- **Traffic Over Time** — Line chart showing bytes over time
- **Top Source IPs** — Horizontal bar of busiest sources  
- **Top Destination IPs** — Horizontal bar of top destinations
- **Protocol Distribution** — Pie chart of traffic by protocol

## Field Mappings (ElastiFlow)

| Purpose | Field |
|---------|-------|
| Traffic volume | `flow.bytes` |
| Source IP | `flow.src.ip.addr` |
| Destination IP | `flow.dst.ip.addr` |
| Protocol | `l4.proto.name` |
| Device filter | `flow.export.ip.addr` |
| Time | `@timestamp` |

## Device Filtering

Add a filter in Kibana for specific devices:
- `flow.export.ip.addr: 10.4.4.3` — Show only Nexus data
- `flow.export.ip.addr: 10.4.4.93` — Show only Juniper data

## Pre-installation (Docker Compose)

To auto-install on stack startup, add to your `docker-compose.yml`:

```yaml
  dashboard-install:
    image: curlimages/curl:latest
    depends_on:
      - kibana
    volumes:
      - ./kibana/scripts/install-dashboard.sh:/install.sh:ro
    entrypoint: ["/bin/sh", "-c", "sleep 60 && /install.sh"]
    restart: "no"
```

## Files

- `dashboards/unified-flow-dashboard.json` — Dashboard export
- `scripts/install-dashboard.sh` — Automated installer

# Unified Network Flow Analytics Dashboards

## Overview

This package contains unified Kibana dashboards for monitoring both **NetFlow** (Juniper) and **sFlow** (Cisco Nexus) data in a single view.

## Dashboard: Network Flow Analytics

**Title:** Network Flow Analytics - Unified NetFlow & sFlow View  
**ID:** `dashboard-network-flow-analytics`

### Visualizations Included

| Panel | Type | Description |
|-------|------|-------------|
| Traffic Over Time (bps) | Line Chart | Bandwidth utilization over time combining both sources |
| Top Source IPs | Data Table | Top 10 source IP addresses by traffic volume |
| Top Destination IPs | Data Table | Top 10 destination IP addresses by traffic volume |
| Protocol Distribution | Pie Chart | Traffic breakdown by TCP/UDP/other protocols |
| Interface Metrics | Metric | Summary statistics for monitored interfaces |
| Geographic Traffic Map | Region Map | Source country distribution (requires GeoIP) |

## Data Sources

### Index Patterns
- **Unified Pattern:** `logs-*` (combines NetFlow and sFlow)
- **NetFlow Only:** `logs-netflow.log-*` (Juniper router data)
- **sFlow Only:** `logs-sflow.net-*` (Cisco Nexus switches)

### Field Mappings (Unified Schema)

Both NetFlow and sFlow data are normalized to the same ECS (Elastic Common Schema) fields:

| Field | Type | Description |
|-------|------|-------------|
| `@timestamp` | date | Event timestamp |
| `source.ip` | ip | Source IP address |
| `destination.ip` | ip | Destination IP address |
| `source.port` | long | Source port number |
| `destination.port` | long | Destination port number |
| `network.bytes` | long | Total bytes transferred |
| `network.packets` | long | Total packets transferred |
| `network.transport` | keyword | Protocol (tcp/udp/icmp) |
| `observer.ip` | ip | Device that observed the flow |
| `flow.type` | keyword | netflow or sflow |

## Installation

### Method 1: Kibana Import (Recommended)

1. Open Kibana at `https://<kibana-host>:5601`
2. Navigate to **Stack Management > Saved Objects**
3. Click **Import** button
4. Select `unified-dashboards.ndjson`
5. Click **Import** with the default options

### Method 2: API Import

```bash
# Set Kibana credentials and URL
KIBANA_URL="https://10.4.4.87:5601"
KIBANA_USER="elastic"
KIBANA_PASS="<your-password>"

# Import the dashboard
curl -k -u $KIBANA_USER:$KIBANA_PASS \
  -X POST "$KIBANA_URL/api/saved_objects/_import?overwrite=true" \
  -H "kbn-xsrf: true" \
  --form file=@unified-dashboards.ndjson
```

### Method 3: Dev Tools Console

Open Kibana Dev Tools and run:

```json
POST kbn:/api/saved_objects/_import?overwrite=true
{
  "file": "<paste ndjson content here>"
}
```

## Post-Import Setup

### 1. Verify Index Patterns

After import, ensure the index patterns exist:

```bash
curl -k -u elastic:<password> \
  "https://<kibana>:5601/api/index_pattern_management/create"
```

Or manually via Kibana:
- Stack Management > Index Patterns
- Create `logs-*` pattern if missing
- Set `@timestamp` as time field

### 2. Create Data Views (Kibana 8.x+)

Go to **Stack Management > Data Views** and create:
- **Name:** `Unified Flow Data`
- **Index pattern:** `logs-*`
- **Time field:** `@timestamp`

### 3. Set Refresh Interval

The dashboard defaults to 30-second refresh. Adjust as needed via:
- Dashboard > Options > Refresh every

## Data Verification

### Check if Data is Flowing

**NetFlow (Juniper):**
```bash
curl -k -u elastic:<password> \
  "https://<es-backend>:9200/logs-netflow.log-*/_count"
```

**sFlow (Cisco Nexus):**
```bash
curl -k -u elastic:<password> \
  "https://<es-backend>:9200/logs-sflow.net-*/_count"
```

### Expected Data Volumes

| Source | Sampling Rate | Expected Records |
|--------|---------------|------------------|
| Juniper NetFlow | 1:4096 | ~18M records/day |
| Nexus sFlow | 1:4096 | Variable per switch |

## Troubleshooting

### No Data Displayed

1. **Check index patterns exist:**
   ```bash
   curl -k -u elastic:<password> \
     "https://<es>:9200/_cat/indices"
   ```

2. **Verify data is being written:**
   - Logstash logs: `docker logs custom-elk-stack-logstash-1`
   - Look for sflow/netflow tags

3. **Check field mappings:**
   - Stack Management > Index Patterns > `logs-*` > Fields
   - Ensure `network.bytes`, `source.ip`, etc. are listed

### Geographic Map Not Working

The geographic map requires GeoIP enrichment. Verify:
```bash
curl -k -u elastic:<password> \
  "https://<es>:9200/logs-*/_search?q=source.geo.country_iso_code:*&size=1"
```

If empty:
1. Check Logstash GeoIP filter is enabled in `logstash.conf`
2. Verify GeoIP database is available

## Architecture

```
                    ┌──────────────────┐
                    │  Kibana          │
                    │  (10.4.4.87)     │
                    │  Dashboards      │
                    └────────┬─────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
      ┌───────▼──────┐ ┌─────▼─────┐ ┌──────▼──────┐
      │ ES Master    │ │ ES Master │ │ ES Data     │
      │ Node 1       │ │ Node 2    │ │ (Frontend)  │
      └──────────────┘ └───────────┘ └─────────────┘
              │              │              │
              └──────────────┼──────────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
      ┌───────▼───────────────────┐ ┌──────▼───────────────────┐
      │ Backend N1 (10.4.4.21)    │ │ Backend N2 (10.4.4.90)   │
      │ - Logstash (NetFlow 2050) │ │ - Logstash (sFlow 6343)  │
      │ - ES Data Node            │ │ - ES Data Node           │
      │ - Data: logs-netflow*     │ │ - Data: logs-sflow*      │
      └───────────────────────────┘ └──────────────────────────┘
              │                              │
              │                              │
      ┌───────▼──────────┐          ┌───────▼──────────┬──────────────┐
      │ Juniper Router   │          │ Nexus Switch 1   │ Nexus Switch 2│
      │ (NetFlow v5)     │          │ (10.4.4.3)       │ (10.4.4.4)   │
      │ Port: UDP 2050   │          │ Port: UDP 6343   │ Port: UDP 6343│
      └──────────────────┘          └──────────────────┴──────────────┘
```

## Files in This Export

| Object | ID | Type |
|--------|-----|------|
| Unified Flow Index Pattern | `unified-flow-pattern` | index-pattern |
| Traffic Over Time Visualization | `viz-traffic-bps` | visualization |
| Top Sources Visualization | `viz-top-sources` | visualization |
| Top Destinations Visualization | `viz-top-destinations` | visualization |
| Protocol Distribution Visualization | `viz-protocol-pie` | visualization |
| Interface Metrics Visualization | `viz-interface-metrics` | visualization |
| Geographic Map Visualization | `viz-geo-map` | visualization |
| Network Flow Analytics Dashboard | `dashboard-network-flow-analytics` | dashboard |

## Maintenance

### Data Retention

Both NetFlow and sFlow use 1-day retention via ILM policy:
```bash
curl -k -u elastic:<password> \
  "https://<es>:9200/_ilm/policy/netflow-1day-retention"
```

### Re-importing After Changes

Always use `overwrite=true` when re-importing:
```bash
curl -k -u elastic:<password> \
  -X POST "$KIBANA_URL/api/saved_objects/_import?overwrite=true" \
  -H "kbn-xsrf: true" \
  --form file=@unified-dashboards.ndjson
```

## Support

For issues with:
- **Dashboard display:** Check Kibana logs and browser console
- **Missing data:** Verify Logstash configuration and switch configuration
- **Field mappings:** Compare with `logstash.conf` ECS mapping

## Changelog

- **2026-02-09:** Initial unified dashboard creation
- **Includes:** NetFlow + sFlow combined view with 6 panels

---
*Generated: 2026-02-09*
*Compatible with: ELK Stack 8.x*

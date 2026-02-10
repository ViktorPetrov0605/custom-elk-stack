# Network Flow Dashboard Best Practices - Research Report

## Executive Summary

This research synthesized findings from ElastiFlow documentation, Kibana best practices, network monitoring standards, and Elastic Common Schema (ECS) field references to identify the most valuable visualizations and metrics for network flow analysis dashboards.

---

## Recommended Visualizations (12 Total)

### MUST-HAVE Visualizations (Priority 1)

#### 1. **Top Talkers Overview**
**Type**: Data Table + Horizontal Bar Chart  
**Purpose**: Identify highest bandwidth consumers by source/destination IP  
**ECS Fields**:
- `source.ip` / `destination.ip` - IP addresses
- `source.bytes` / `destination.bytes` - Traffic volume
- `source.packets` / `destination.packets` - Packet counts
- `client.ip` / `server.ip` (alternative perspective)

**Metrics**: Sum of bytes, packet count, flow count  
**Why Essential**: Quickly identifies bandwidth hogs and potential DDoS sources

---

#### 2. **GeoIP Traffic Heat Map**
**Type**: Coordinate Map / Choropleth Map  
**Purpose**: Visualize geographic distribution of traffic  
**ECS Fields**:
- `client.geo.location` (geo_point) - Client coordinates
- `client.geo.country_iso_code` - Country
- `client.geo.city_name` - City
- `destination.geo.location` - Destination coordinates (for server perspective)
- `client.bytes` / `destination.bytes` - Volume by location

**Metrics**: Bytes by geographic region, unique source IPs by country  
**Why Essential**: Identifies unexpected international traffic, data exfiltration patterns

---

#### 3. **Traffic Volume Time Series**
**Type**: Stacked Area Chart / TSVB (Time Series Visual Builder)  
**Purpose**: Track bandwidth utilization over time with trend analysis  
**ECS Fields**:
- `@timestamp` - Event time
- `source.bytes` / `destination.bytes` - Data volume
- `network.name` (if enriched) - Interface or segment name
- `host.name` - Exporter device

**Metrics**: Bits/second, bytes/second, packets/second  
**Best Practice**: Use TSVB for network data; normalize to bits-per-second for consistent scale  
**Why Essential**: Baseline establishment, anomaly detection, capacity planning

---

#### 4. **Port Analysis Dashboard**
**Type**: Pie Chart + Data Table + Vertical Bar Chart  
**Purpose**: Identify top ports, service usage, and potential port scans  
**ECS Fields**:
- `source.port` / `destination.port` - Port numbers (as keyword)
- `network.protocol` (TCP/UDP/ICMP)
- `source.bytes` by `destination.port` - Volume per service

**Metrics**: Top source ports, top destination ports, unique port count per host  
**Why Essential**: Service identification, unauthorized service detection, security analysis

---

#### 5. **Protocol Distribution**
**Type**: Pie Chart / Donut Chart  
**Purpose**: Breakdown of traffic by Layer 3/4 protocols  
**ECS Fields**:
- `network.protocol` - Protocol name (tcp, udp, icmp)
- `network.iana_number` - Protocol number
- `network.transport` - Transport layer

**Metrics**: Percentage distribution by protocol, bytes per protocol  
**Why Essential**: Protocol compliance monitoring, unusual protocol detection

---

### HIGH PRIORITY Visualizations (Priority 2)

#### 6. **Flow Sankey Diagram**
**Type**: Sankey / Vega Visualization  
**Purpose**: Visualize flow paths from source to destination  
**ECS Fields**:
- `source.ip` -> `destination.ip` - Connection paths
- `source.bytes` / `destination.bytes` - Volume weights
- `client.as.organization.name` / `destination.as.organization.name` - ASN path

**Why High Priority**: Shows relationship patterns, identifies lateral movement, visual traffic paths

---

#### 7. **Autonomous System (ASN) Analysis**
**Type**: Data Table + Bar Chart  
**Purpose**: Identify traffic to/from external AS organizations  
**ECS Fields**:
- `client.as.number` / `destination.as.number` - ASN
- `client.as.organization.name` - AS organization name
- `client.as.organization.name.text` - For search

**Metrics**: Traffic volume by AS, top communicating ASNs  
**Why High Priority**: Peering analysis, threat intelligence correlation, external dependency visibility

---

#### 8. **Bandwidth Utilization Gauge**
**Type**: Gauge / Metric Visualization  
**Purpose**: Real-time utilization percentage indicators  
**ECS Fields**:
- `source.bytes` + `destination.bytes` - Total volume
- `interface.name` (enriched) - Interface identifier
- `network.speed` (if available) - Total capacity

**Metrics**: Utilization % (requires calculation: current_rate / link_capacity * 100)  
**Thresholds**: Warning at 70%, Critical at 85%  
**Why High Priority**: Immediate visual status, capacity alert indicator

---

#### 9. **Device/Exporter Filtering Panel**
**Type**: Controls / Input Controls  
**Purpose**: Filter all dashboard visualizations by specific flow exporters  
**ECS Fields**:
- `host.name` / `agent.name` - Device name
- `host.ip` - Device IP
- `agent.type` - Exporter type (netflow, sflow, ipfix)
- `flow.exporter.ip` (if ElastiFlow enriched)

**Control Types**: Dropdown multi-select, free text with wildcard support  
**Why High Priority**: Multi-tenant isolation, troubleshooting specific network segments

---

### NICE-TO-HAVE Visualizations (Priority 3)

#### 10. **Traffic Pattern Analysis**
**Type**: Heat Map / Calendar Heat Map  
**Purpose**: Identify hourly/daily/weekly traffic patterns  
**ECS Fields**:
- `@timestamp` - For time bucketing
- `event.hour_of_day` (scripted) - Hour aggregation
- `event.day_of_week` (scripted) - Day aggregation
- `source.bytes` / `destination.bytes` - Volume

**Metrics**: Average bytes by hour-of-day, bytes by day-of-week  
**Why Nice-to-Have**: Capacity planning, anomaly detection, business pattern analysis

---

#### 11. **TCP Flags Analysis**
**Type**: Data Table + Bar Chart  
**Purpose**: Analyze connection states and potential SYN floods  
**ECS Fields**:
- `netflow.tcp_flags` (or `tcp.flags` in some parsers)
- `event.action` - Connection state
- `network.protocol` - TCP

**Metrics**: SYN count, RST count, distinct flag combinations  
**Why Nice-to-Have**: Security analysis, connection quality assessment

---

#### 12. **Interface Utilization Heat Map**
**Type**: Heat Map Matrix  
**Purpose**: Compare utilization across multiple interfaces/devices  
**ECS Fields**:
- `interface.name` / `network.interface.name` - Interface
- `host.name` - Device
- `source.bytes` + `destination.bytes` - Traffic

**Metrics**: Bytes per interface per time bucket  
**Why Nice-to-Have**: At-a-glance interface status across infrastructure

---

## ECS Field Mappings Reference

### Core Flow Fields (Required)
```
@timestamp              - Event timestamp (date)
source.ip               - Source IP address (ip)
destination.ip          - Destination IP address (ip)
source.port             - Source port (long)
destination.port        - Destination port (long)
source.bytes            - Bytes from source (long)
destination.bytes       - Bytes to destination (long)
source.packets          - Packets from source (long)
destination.packets     - Packets to destination (long)
network.protocol        - Protocol name (keyword)
network.transport       - Transport protocol (keyword)
event.duration          - Flow duration in nanoseconds (long)
```

### GeoIP Enrichment Fields
```
client.geo.location             - Geo coordinates (geo_point)
client.geo.country_iso_code     - Country code (keyword)
client.geo.country_name         - Country name (keyword)
client.geo.city_name            - City name (keyword)
client.geo.region_name          - Region/state (keyword)
destination.geo.location        - Destination geo (geo_point)
```

### ASN/BGP Fields
```
client.as.number                - Autonomous System Number (long)
client.as.organization.name     - AS organization (keyword)
destination.as.number           - Destination ASN (long)
destination.as.organization.name - Destination AS org (keyword)
```

### Host/Exporter Fields
```
host.name               - Hostname (keyword)
host.ip                 - Host IP(s) (ip)
agent.name              - Agent name (keyword)
agent.type              - Agent type - netflow/sflow/ipfix (keyword)
agent.id                - Unique agent identifier (keyword)
```

---

## Dashboard Design Best Practices

### From ElastiFlow & Kibana Documentation:

1. **Tell a Story**: Organize visualizations left-to-right, top-to-bottom: Overview → Details → Investigation
2. **Reduce Cognitive Load**: Use consistent colors (blue=good, red=warning/critical), normalize axes
3. **Template Variables**: Use `host.name`, `client.ip`, or time range as filters to avoid dashboard sprawl
4. **Directed Browsing**: Link dashboards together (e.g., from Top Talkers → IP Investigation dashboard)
5. **Thresholds**: Set visual thresholds on gauges and charts (70% warning, 85% critical)
6. **Time Series (TSVB)**: Use TSVB for network metrics instead of standard charts for better rate calculations
7. **Data Tables**: Include clickable data tables for drill-down investigations

### Grafana-Specific (if applicable):
1. Use RED method (Rate, Errors, Duration) for service dashboards
2. USE method (Utilization, Saturation, Errors) for infrastructure hardware
3. Four Golden Signals: Latency, Traffic, Errors, Saturation

---

## Key Metrics to Calculate

| Metric | Calculation | Visualization |
|--------|-------------|---------------|
| Bits/Second | `(source.bytes + destination.bytes) * 8 / time_window` | Line/Area Chart |
| Utilization % | `(current_bps / interface_capacity_bps) * 100` | Gauge |
| Flows/Second | `count(flows) / time_window` | Metric/Stat |
| Top N | `terms` aggregation on IP with sum(bytes) | Data Table/Bar |
| Unique Conversations | `cardinality(source.ip + destination.ip)` | Metric |

---

## Security-Focused Visualizations

Based on SELKS/Security dashboard patterns:

1. **Top Destination Countries** - Identify data exfiltration
2. **Unusual Port Activity** - Port scans, tunneling attempts
3. **TCP Flag Anomalies** - SYN floods, connection patterns
4. **Long Duration Flows** - `event.duration > threshold` - Data exfiltration
5. **External Threat Intel Matches** - Flows matching known bad IPs

---

## Summary Priority Matrix

| # | Visualization | Priority | Effort | Impact |
|---|---------------|----------|--------|--------|
| 1 | Top Talkers | MUST-HAVE | Low | High |
| 2 | GeoIP Heat Map | MUST-HAVE | Medium | High |
| 3 | Traffic Volume Time Series | MUST-HAVE | Low | High |
| 4 | Port Analysis | MUST-HAVE | Low | High |
| 5 | Protocol Distribution | MUST-HAVE | Low | Medium |
| 6 | Flow Sankey | HIGH | High | Medium |
| 7 | ASN Analysis | HIGH | Medium | Medium |
| 8 | Bandwidth Utilization Gauge | HIGH | Low | High |
| 9 | Device Filtering Panel | HIGH | Low | High |
| 10 | Traffic Pattern Heat Map | NICE | Medium | Medium |
| 11 | TCP Flags Analysis | NICE | Medium | Low |
| 12 | Interface Utilization Matrix | NICE | Medium | Medium |

---

## Sources

1. ElastiFlow Documentation (elastiflow.com/docs)
2. Elastic NetFlow Integration (elastic.co/docs/integrations/netflow)
3. Grafana Dashboard Best Practices (grafana.com/docs)
4. SELKS Kibana Dashboard Guide (stamus-networks.com)
5. Kentik Bandwidth Monitoring Best Practices (kentik.com)
6. Kibana Dashboard Examples (logit.io)

---

*Research completed: 2026-02-10*

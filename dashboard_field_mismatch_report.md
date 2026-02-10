# Dashboard Data Issue - Investigation Report

**Date:** 2026-02-10
**Investigation Focus:** Field/Index Mismatches in Dashboards

---

## EXECUTIVE SUMMARY

Both dashboards (Juniper and Nexus) show "No results found" due to **different root causes**:

| Dashboard | Issue Type | Root Cause | Severity |
|-----------|------------|------------|----------|
| Juniper Flow Analytics | Index Unavailability | Netflow index shards are UNASSIGNED (Cluster RED) | CRITICAL |
| Nexus Flow Analytics | Field Naming Mismatch | Visualizations use ECS fields but ElastiFlow uses custom field names | MAJOR |

---

## 1. JUNIPER DASHBOARD ISSUE - INDEX UNAVAILABILITY

### Dashboard Configuration
- **Dashboard ID:** juniper-flow-analytics
- **Index Pattern:** netflow-pattern → `logs-netflow-*`
- **Description:** NetFlow analytics for Juniper switch (10.4.4.93)

### Visualizations (4 panels)
| Panel | Visualization ID | Title | Fields Used |
|-------|------------------|-------|-------------|
| 1 | b57be944-ad91-43b2-ae56-e43f8f7a36eb | Juniper - Traffic Over Time | `network.bytes`, `@timestamp` |
| 2 | a46a59cd-bb89-4249-bb70-8bfc64c517a4 | Juniper - Top Source IPs | `network.bytes`, `source.ip` |
| 3 | 10383b0a-eff2-45f7-bdd6-7ddeb5996cc5 | Juniper - Top Destination IPs | `network.bytes`, `destination.ip` |
| 4 | d8e74ac4-807e-467b-ba87-9d1b455af817 | Juniper - Protocol Distribution | `network.bytes`, `network.transport` |

### Index Health Status
```
Index: .ds-logs-netflow.log-default-2026.02.10-000001
Status: RED
Shard 0 (Primary): UNASSIGNED
Shard 0 (Replica): UNASSIGNED
Docs: 0 searchable
```

### Root Cause
The netflow data stream index exists but **both primary and replica shards are unassigned**. This makes the index completely unsearchable, resulting in 503 errors for any query.

**Cluster Status:** RED
- Unassigned shards: 2
- Unassigned primary shards: 1

### Fix Commands
```bash
# Check shard allocation explain
curl -k -u elastic:telehouse https://10.4.4.87:9200/_cluster/allocation/explain

# Try to force reallocate the primary shard
curl -k -u elastic:telehouse -XPOST https://10.4.4.87:9200/_cluster/reroute \
  -H 'Content-Type: application/json' \
  -d '{
    "commands": [
      {
        "allocate_empty_primary": {
          "index": ".ds-logs-netflow.log-default-2026.02.10-000001",
          "shard": 0,
          "node": "NODE_NAME",
          "accept_data_loss": true
        }
      }
    ]
  }'

# Or allocate stale primary if data exists elsewhere
curl -k -u elastic:telehouse -XPOST https://10.4.4.87:9200/_cluster/reroute \
  -H 'Content-Type: application/json' \
  -d '{
    "commands": [
      {
        "allocate_stale_primary": {
          "index": ".ds-logs-netflow.log-default-2026.02.10-000001",
          "shard": 0,
          "node": "NODE_NAME",
          "accept_data_loss": false
        }
      }
    ]
  }'
```

---

## 2. NEXUS DASHBOARD ISSUE - FIELD MISMATCH

### Dashboard Configuration
- **Dashboard ID:** nexus-flow-analytics
- **Index Pattern:** elastiflow-flow → `elastiflow-flow-codex-*`
- **Description:** sFlow analytics for Nexus switches (10.4.4.3)

### Visualizations (4 panels)
| Panel | Visualization ID | Title | Fields Used (Expected) | Fields in Index |
|-------|------------------|-------|------------------------|-----------------|
| 1 | 41ba58ad-8753-467c-b464-462bab49f3ad | Nexus - Traffic Over Time | `network.bytes`, `@timestamp` | `flow.bytes` ❌ |
| 2 | 8254c07b-33cf-45ce-a583-3dd1ee057cae | Nexus - Top Source IPs | `network.bytes`, `source.ip` | `flow.bytes`, `flow.src.ip.addr` ❌ |
| 3 | d31aff23-5432-4a17-a37e-80f5f733d77d | Nexus - Top Destination IPs | `network.bytes`, `destination.ip` | `flow.bytes`, `flow.dst.ip.addr` ❌ |
| 4 | 0ad5cd5c-99aa-48f7-ab59-00bcc954e51b | Nexus - Protocol Distribution | `network.bytes`, `network.transport` | `flow.bytes`, `l4.proto.name` ❌ |

### Field Compatibility Matrix

| Visualization Field | Available in Index? | Correct Field Name |
|---------------------|--------------------|--------------------|
| `network.bytes` | ❌ NO | `flow.bytes` |
| `source.ip` | ❌ NO | `flow.src.ip.addr` |
| `destination.ip` | ❌ NO | `flow.dst.ip.addr` |
| `network.transport` | ❌ NO | `l4.proto.name` |
| `@timestamp` | ✅ YES | `@timestamp` |

### ElastiFlow Data Format (Actual Index Fields)
From sample document:
```json
{
  "@timestamp": 1770728517473,
  "flow.bytes": 6184960,
  "flow.src.ip.addr": "193.200.237.144",
  "flow.dst.ip.addr": "82.118.229.82",
  "flow.server.ip.addr": "82.118.229.82",
  "flow.client.ip.addr": "193.200.237.144",
  "flow.export.ip.addr": "10.4.4.3",
  "flow.packets": 4096,
  "flow.direction.name": "Ingress",
  "flow.locality": "public",
  "l4.proto.name": "ESP",
  "ip.version.name": "IPv4",
  "ip.packet.size": 1492
}
```

### Root Cause
The visualizations were created using standard **ECS (Elastic Common Schema)** field names:
- `network.bytes`, `source.ip`, `destination.ip`, `network.transport`

But ElastiFlow uses its **own nested field naming convention**:
- `flow.bytes`, `flow.src.ip.addr`, `flow.dst.ip.addr`, `l4.proto.name`

Since the fields don't match, queries return no results.

### Fix Options

#### Option A: Update Visualizations to Use ElastiFlow Fields (Recommended)
Update all 4 Nexus visualizations to use the correct field names:

```bash
# 1. Update Nexus - Traffic Over Time
curl -k -u elastic:telehouse -XPUT "http://10.4.4.87:5601/api/saved_objects/visualization/41ba58ad-8753-467c-b464-462bab49f3ad" \
  -H 'Content-Type: application/json' \
  -H 'kbn-xsrf: true' \
  -d '{
    "attributes": {
      "title": "Nexus - Traffic Over Time",
      "visState": "{\"title\":\"Nexus - Traffic Over Time\",\"type\":\"area\",\"aggs\":[{\"id\":\"1\",\"enabled\":true,\"type\":\"sum\",\"schema\":\"metric\",\"params\":{\"field\":\"flow.bytes\",\"customLabel\":\"Bytes\"}},{\"id\":\"2\",\"enabled\":true,\"type\":\"date_histogram\",\"schema\":\"segment\",\"params\":{\"field\":\"@timestamp\",\"fixed_interval\":\"1m\",\"customLabel\":\"Time\"}}],\"params\":{\"type\":\"area\",\"grid\":{\"categoryLines\":false,\"style\":{\"color\":\"#eee\"}},\"categoryAxes\":[{\"id\":\"CategoryAxis-1\",\"type\":\"category\",\"position\":\"bottom\",\"show\":true,\"style\":{},\"scale\":{\"type\":\"linear\"},\"labels\":{\"show\":true,\"truncate\":100},\"title\":{}}],\"valueAxes\":[{\"id\":\"ValueAxis-1\",\"name\":\"LeftAxis-1\",\"type\":\"value\",\"position\":\"left\",\"show\":true,\"style\":{},\"scale\":{\"type\":\"linear\",\"mode\":\"normal\"},\"labels\":{\"show\":true,\"rotate\":0,\"filter\":false,\"truncate\":100},\"title\":{\"text\":\"Bytes\"},\"unit\":\"bytes\"}],\"seriesParams\":[{\"show\":true,\"type\":\"area\",\"mode\":\"stacked\",\"data\":{\"label\":\"Bytes\",\"id\":\"1\"},\"valueAxis\":\"ValueAxis-1\",\"drawLinesBetweenPoints\":true,\"showCircles\":true,\"interpolate\":\"linear\",\"lineWidth\":2,\"fill\":0.5}],\"addTooltip\":true,\"addLegend\":true,\"legendPosition\":\"right\",\"palette\":{\"type\":\"palette\",\"name\":\"default\"}},\"uiStateJSON\":\"{}\"}"
    },
    "references": [{"id": "elastiflow-flow", "name": "kibanaSavedObjectMeta.searchSourceJSON.index", "type": "index-pattern"}]
  }'

# 2. Update Nexus - Top Source IPs
curl -k -u elastic:telehouse -XPUT "http://10.4.4.87:5601/api/saved_objects/visualization/8254c07b-33cf-45ce-a583-3dd1ee057cae" \
  -H 'Content-Type: application/json' \
  -H 'kbn-xsrf: true' \
  -d '{
    "attributes": {
      "title": "Nexus - Top Source IPs",
      "visState": "{\"title\":\"Nexus - Top Source IPs\",\"type\":\"table\",\"aggs\":[{\"id\":\"1\",\"enabled\":true,\"type\":\"sum\",\"schema\":\"metric\",\"params\":{\"field\":\"flow.bytes\",\"customLabel\":\"Total Bytes\"}},{\"id\":\"2\",\"enabled\":true,\"type\":\"terms\",\"schema\":\"bucket\",\"params\":{\"field\":\"flow.src.ip.addr\",\"size\":10,\"order\":\"desc\",\"orderBy\":\"1\",\"customLabel\":\"Source IP\"}}],\"params\":{\"perPage\":10,\"showPartialRows\":false,\"showMetricsAtAllLevels\":false,\"showTotal\":false,\"totalFunc\":\"sum\",\"percentageCol\":\"\"},\"uiStateJSON\":\"{}\"}"
    },
    "references": [{"id": "elastiflow-flow", "name": "kibanaSavedObjectMeta.searchSourceJSON.index", "type": "index-pattern"}]
  }'

# 3. Update Nexus - Top Destination IPs
curl -k -u elastic:telehouse -XPUT "http://10.4.4.87:5601/api/saved_objects/visualization/d31aff23-5432-4a17-a37e-80f5f733d77d" \
  -H 'Content-Type: application/json' \
  -H 'kbn-xsrf: true' \
  -d '{
    "attributes": {
      "title": "Nexus - Top Destination IPs",
      "visState": "{\"title\":\"Nexus - Top Destination IPs\",\"type\":\"table\",\"aggs\":[{\"id\":\"1\",\"enabled\":true,\"type\":\"sum\",\"schema\":\"metric\",\"params\":{\"field\":\"flow.bytes\",\"customLabel\":\"Total Bytes\"}},{\"id\":\"2\",\"enabled\":true,\"type\":\"terms\",\"schema\":\"bucket\",\"params\":{\"field\":\"flow.dst.ip.addr\",\"size\":10,\"order\":\"desc\",\"orderBy\":\"1\",\"customLabel\":\"Destination IP\"}}],\"params\":{\"perPage\":10,\"showPartialRows\":false,\"showMetricsAtAllLevels\":false,\"showTotal\":false,\"totalFunc\":\"sum\",\"percentageCol\":\"\"},\"uiStateJSON\":\"{}\"}"
    },
    "references": [{"id": "elastiflow-flow", "name": "kibanaSavedObjectMeta.searchSourceJSON.index", "type": "index-pattern"}]
  }'

# 4. Update Nexus - Protocol Distribution
curl -k -u elastic:telehouse -XPUT "http://10.4.4.87:5601/api/saved_objects/visualization/0ad5cd5c-99aa-48f7-ab59-00bcc954e51b" \
  -H 'Content-Type: application/json' \
  -H 'kbn-xsrf: true' \
  -d '{
    "attributes": {
      "title": "Nexus - Protocol Distribution",
      "visState": "{\"title\":\"Nexus - Protocol Distribution\",\"type\":\"pie\",\"aggs\":[{\"id\":\"1\",\"enabled\":true,\"type\":\"sum\",\"schema\":\"metric\",\"params\":{\"field\":\"flow.bytes\",\"customLabel\":\"Bytes\"}},{\"id\":\"2\",\"enabled\":true,\"type\":\"terms\",\"schema\":\"segment\",\"params\":{\"field\":\"l4.proto.name\",\"size\":10,\"order\":\"desc\",\"orderBy\":\"1\",\"customLabel\":\"Protocol\"}}],\"params\":{\"type\":\"pie\",\"addTooltip\":true,\"addLegend\":true,\"legendPosition\":\"right\",\"isDonut\":false,\"palette\":{\"type\":\"palette\",\"name\":\"default\"},\"labels\":{\"show\":false,\"values\":true,\"last_level\":true,\"truncate\":100}},\"uiStateJSON\":\"{}\"}"
    },
    "references": [{"id": "elastiflow-flow", "name": "kibanaSavedObjectMeta.searchSourceJSON.index", "type": "index-pattern"}]
  }'
```

#### Option B: Create Runtime Fields in Index Pattern
Add runtime fields to the `elastiflow-flow` index pattern to alias ECS fields:

```bash
# Get current index pattern
curl -k -u elastic:telehouse "http://10.4.4.87:5601/api/saved_objects/index-pattern/elastiflow-flow" > elastiflow-pattern.json

# Update with runtime fields
curl -k -u elastic:telehouse -XPUT "http://10.4.4.87:5601/api/saved_objects/index-pattern/elastiflow-flow" \
  -H 'Content-Type: application/json' \
  -H 'kbn-xsrf: true' \
  -d '{
    "attributes": {
      "title": "elastiflow-flow-codex-*",
      "timeFieldName": "@timestamp",
      "runtimeFieldMap": {
        "network.bytes": {
          "type": "long",
          "script": {
            "source": "emit(doc['flow.bytes'].value)"
          }
        },
        "source.ip": {
          "type": "ip",
          "script": {
            "source": "emit(doc['flow.src.ip.addr'].value)"
          }
        },
        "destination.ip": {
          "type": "ip",
          "script": {
            "source": "emit(doc['flow.dst.ip.addr'].value)"
          }
        },
        "network.transport": {
          "type": "keyword",
          "script": {
            "source": "emit(doc['l4.proto.name'].value)"
          }
        }
      }
    }
  }'
```

---

## SUMMARY OF FIXES NEEDED

### Immediate Actions (Priority 1)
1. **Fix Juniper Dashboard - Cluster Issue:**
   - Investigate why netflow index shards are unassigned
   - Allocate/recover the primary shard
   - Check data node disk space and memory

2. **Fix Nexus Dashboard - Field Mapping:**
   - Update all 4 visualizations to use ElastiFlow field names:
     - `network.bytes` → `flow.bytes`
     - `source.ip` → `flow.src.ip.addr`
     - `destination.ip` → `flow.dst.ip.addr`
     - `network.transport` → `l4.proto.name`

### Suggested Field Mapping Reference Table
| ECS Field | ElastiFlow Field | Usage |
|-----------|-----------------|-------|
| `network.bytes` | `flow.bytes` | Traffic volume metrics |
| `source.ip` | `flow.src.ip.addr` | Source IP addresses |
| `destination.ip` | `flow.dst.ip.addr` | Destination IP addresses |
| `network.transport` | `l4.proto.name` | Protocol (TCP, UDP, etc.) |
| `@timestamp` | `@timestamp` | Time field (same in both) |

---

## APPENDIX: Index Details

### logs-netflow.log-* (Netflow Pattern)
- **Type:** Data Stream
- **Backing Index:** `.ds-logs-netflow.log-default-2026.02.10-000001`
- **Status:** RED (unassigned shards)
- **Fields:** Standard ECS fields including `network.bytes`, `source.ip`, `destination.ip`

### elastiflow-flow-codex-* (ElastiFlow Pattern)
- **Type:** Index with rollover alias
- **Backing Index:** `elastiflow-flow-codex-2.5-rollover-000001`
- **Status:** GREEN
- **Fields:** Custom ElastiFlow schema with `flow.*` prefixed fields
- **Data Count:** 10,000+ documents

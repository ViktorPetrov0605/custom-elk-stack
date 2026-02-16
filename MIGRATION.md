# Migration Guide: ElastiFlow to Logstash

Complete guide for migrating from ElastiFlow to Logstash unified flow collector.

## Why Migrate?

| Feature | ElastiFlow | Logstash |
|---------|------------|----------|
| License | Free tier limited to 4000 RPS | Unlimited |
| Devices | ~20-30 recommended | 50+ supported |
| Protocols | NetFlow + sFlow | NetFlow + sFlow |
| Cost | Commercial license for scale | Open source (free) |
| Schema | ECS-compliant | ECS-compliant |
| Dashboards | Compatible with modifications | Fully compatible |

## Pre-Migration Checklist

- [ ] Current flow rate documented
- [ ] Number of exporters noted
- [ ] Existing dashboards backed up
- [ ] Elasticsearch health verified
- [ ] Network device configurations documented

## Migration Steps

### Step 1: Prepare Elasticsearch

**On Frontend (10.4.4.87):**

```bash
cd /opt/custom-elk-stack/logstash-migration/

# Create ILM policy and index template
./setup-elasticsearch.sh
```

This creates:
- `flow-data-3-day` ILM policy
- `logstash-flow` index template
- Initial index with rollover alias

### Step 2: Deploy Logstash on Backend N1

**On Backend N1 (NetFlow collector):**

```bash
# Copy Logstash files
mkdir -p /opt/logstash-flow/
cd /opt/logstash-flow/

# Copy from frontend
cp /path/to/custom-elk-stack/logstash-migration/*.conf .
cp /path/to/custom-elk-stack/logstash-migration/*.json .
cp /path/to/custom-elk-stack/logstash-migration/*.yml .
cp /path/to/custom-elk-stack/logstash-migration/Dockerfile .

# Stop ElastiFlow
docker stop flow-collector 2>/dev/null || true
docker rm flow-collector 2>/dev/null || true

# Start Logstash
docker compose up -d --build

# Verify
sleep 10
docker logs logstash-flow --tail 30
curl http://localhost:9600/_node/stats
```

### Step 3: Deploy Logstash on Backend N2

**On Backend N2 (sFlow collector):**

```bash
# Same process as N1
mkdir -p /opt/logstash-flow/
cd /opt/logstash-flow/

# Copy files
cp /path/to/custom-elk-stack/logstash-migration/*.conf .
cp /path/to/custom-elk-stack/logstash-migration/*.json .
cp /path/to/custom-elk-stack/logstash-migration/*.yml .
cp /path/to/custom-elk-stack/logstash-migration/Dockerfile .

# Stop ElastiFlow
docker stop flow-collector 2>/dev/null || true
docker rm flow-collector 2>/dev/null || true

# Start Logstash
docker compose up -d --build

# Verify
docker logs logstash-flow --tail 30
```

### Step 4: Verify Data Flow

**On Frontend:**

```bash
# Check index created
curl -k -u elastic:password \
  https://10.4.4.87:9200/_cat/indices/logstash-flow-*?v

# Check document count
curl -k -u elastic:password \
  https://10.4.4.87:9200/logstash-flow-*/_count

# Sample recent documents
curl -k -u elastic:password \
  "https://10.4.4.87:9200/logstash-flow-*/_search?size=1&sort=@timestamp:desc"
```

Expected output:
```json
{
  "count": 12345,
  "_shards": { "total": 2, "successful": 2, "skipped": 0, "failed": 0 }
}
```

### Step 5: Update Dashboards

**Option A: Update Existing Dashboards**

Update index pattern references from `elastiflow-flow-ecs-*` to `logstash-flow-*`:

```bash
# Get current dashboards
curl -k -u elastic:password \
  "https://10.4.4.87:5601/api/saved_objects/_find?type=dashboard" \
  -H "kbn-xsrf: true" | jq '.savedObjects[] | .id, .attributes.title'

# For each dashboard, update references via UI:
# 1. Open Kibana → Stack Management → Saved Objects
# 2. Find dashboard → Export
# 3. Replace old index pattern ID with new one
# 4. Re-import with overwrite
```

**Option B: Create New Dashboards**

Create dashboards using `logstash-flow-*` index pattern:

```bash
# Import pre-built dashboards
curl -k -u elastic:password \
  -X POST "https://10.4.4.87:5601/api/saved_objects/_import?overwrite=true" \
  -H "kbn-xsrf: true" \
  --form file=@logstash-migration/dashboards/unified-flow-dashboards.ndjson
```

### Step 6: Verify Dashboard Functionality

Open Kibana (https://10.4.4.87:5601):

1. Navigate to **Analytics** → **Dashboard**
2. Select **[Unified Flow] Detailed Traffic Analysis**
3. Set time range to **Last 15 minutes**
4. Verify visualizations show data
5. Test filters: `host.ip: 10.4.4.93`

### Step 7: Clean Up ElastiFlow

After 24-48 hours of stable operation:

**On each backend:**

```bash
# Stop ElastiFlow services
docker stop flow-collector
docker rm flow-collector

# Remove ElastiFlow images
docker image prune -a

# Remove volumes (WARNING: Deletes old data)
docker volume rm elastiflow-data-elastic
```

**On Frontend:**

```bash
# Optional: Delete old ElastiFlow indices
# (keep if you need historical data)
curl -k -u elastic:password -X DELETE \
  "https://10.4.4.87:9200/elastiflow-flow-*"
curl -k -u elastic:password -X DELETE \
  "https://10.4.4.87:9200/elastiflow-metric-*"
```

## Post-Migration Verification

### Data Verification

```bash
# Compare old vs new data counts
# (Run during overlap period)

echo "Old ElastiFlow indices:"
curl -k -u elastic:password \
  "https://10.4.4.87:9200/elastiflow-flow-*/_count"

echo "New Logstash indices:"
curl -k -u elastic:password \
  "https://10.4.4.87:9200/logstash-flow-*/_count"
```

### Dashboard Verification

1. **Traffic Timeline** - Shows bytes over time
2. **Protocol Distribution** - Pie chart of TCP/UDP/ICMP
3. **Top Sources** - Table of source IPs
4. **Top Destinations** - Table of destination IPs
5. **Device Breakdown** - Traffic by `host.ip`

### Network Device Verification

Test each device is sending:

```bash
# Juniper (NetFlow)
curl -k -u elastic:password \
  "https://10.4.4.87:9200/logstash-flow-*/_search" \
  -H "Content-Type: application/json" \
  -d '{
    "query": { "term": { "host.ip": "10.4.4.93" } },
    "size": 0,
    "aggs": { "count": { "value_count": { "field": "_id" } } }
  }'

# Cisco (sFlow)
curl -k -u elastic:password \
  "https://10.4.4.87:9200/logstash-flow-*/_search" \
  -H "Content-Type: application/json" \
  -d '{
    "query": { "term": { "host.ip": "10.4.4.3" } },
    "size": 0,
    "aggs": { "count": { "value_count": { "field": "_id" } } }
  }'
```

## Rollback Procedure

If issues occur:

```bash
# Stop Logstash
docker stop logstash-flow
docker rm logstash-flow

# Start ElastiFlow (if still installed)
cd /opt/elastiflow
docker compose up -d

# Update dashboards back to old index pattern
# (If dashboards were updated)
```

## Troubleshooting Migration Issues

### Issue: No data in new indices

**Check:**
```bash
# Logstash logs
docker logs logstash-flow --tail 50

# Port listening
ss -uln | grep -E "(2050|6343)"

# Firewall
sudo ufw status

# Network connection to Elasticsearch
curl -k -u elastic:password https://10.4.4.87:9200
```

### Issue: Dashboard shows "no results found"

**Check index pattern:**
1. Kibana → Stack Management → Index Patterns
2. Look for `logstash-flow-*`
3. Check timestamp field is `@timestamp`
4. Refresh field list

**Check time range:**
- Default may be "Last 15 minutes"
- Data might be older or newer

### Issue: Field mapping conflicts

**Symptom:** 
```
"event": "fail",
"error": {
  "type": "mapper_parsing_exception",
  "reason": "failed to parse field"
}
```

**Fix:**
```bash
# Delete conflicting index
curl -k -u elastic:password -X DELETE \
  "https://10.4.4.87:9200/logstash-flow-*"

# Recreate with proper template
./logstash-migration/setup-elasticsearch.sh
```

### Issue: sFlow data missing

**Check codec installation:**
```bash
docker exec logstash-flow logstash-plugin list | grep sflow

# If missing, rebuild Docker image with codec
docker compose down
docker compose up -d --build
```

## Field Mapping Reference

### Schema Differences

| ElastiFlow | Logstash Flow | Dashboard Field |
|------------|---------------|-----------------|
| `flow.exporter.ip` | `host.ip` | Device filter |
| `flow.src_addr` | `source.ip` | Source |
| `flow.dst_addr` | `destination.ip` | Destination |
| `flow.src_port` | `source.port` | Source port |
| `flow.dst_port` | `destination.port` | Dest port |
| `flow.bytes` | `network.bytes` | Bytes |
| `flow.packets` | `network.packets` | Packets |
| `flow.protocol_name` | `network.transport` | Protocol |
| `flow.sampling_interval` | `flow.sample.rate` | Sampling |
| N/A | `flow.locality` | Internal/Public |

### Updating Custom Dashboards

For custom dashboards, update these fields:

1. **Visualization data sources:**
   - `elastiflow-flow-ecs-*` → `logstash-flow-*`

2. **Visualization fields:**
   - `flow.src_addr` → `source.ip`
   - `flow.dst_addr` → `destination.ip`
   - etc.

3. **Lens visualizations:**
   - Edit each panel
   - Change data source/index pattern
   - Map fields using reference above

## Performance Comparison

### ElastiFlow (4000 RPS limit)

```
Max throughput: ~4,000 flows/second
Devices: ~20-30 (depending on sampling)
Latency: Low
CPU: Moderate
Memory: ~2GB
```

### Logstash (unlimited)

```
Max throughput: 10,000+ flows/second
Devices: 50+ supported
Latency: Low-Moderate
CPU: Moderate
Memory: ~3-4GB
```

## Maintenance

### Regular Checks

```bash
# Weekly: Check data flow
curl -k -u elastic:password \
  https://10.4.4.87:9200/logstash-flow-*/_count

# Weekly: Check index rollover
curl -k -u elastic:password \
  https://10.4.4.87:9200/_cat/indices/logstash-flow-*?v

# Monthly: Review ILM policy
curl -k -u elastic:password \
  https://10.4.4.87:9200/_ilm/policy/flow-data-3-day
```

### Updates

```bash
# Update Logstash version in Dockerfile
vim Dockerfile

# Rebuild
docker compose down
docker compose up -d --build
```

## Summary

Migration complete when:
- [ ] Both backends running Logstash
- [ ] Data flowing to `logstash-flow-*`
- [ ] Dashboards showing real-time data
- [ ] Old ElastiFlow stopped
- [ ] Team trained on new filter syntax

**Benefits achieved:**
- Unlimited device capacity
- No license costs
- Simplified architecture
- Unified NetFlow + sFlow handling

---

*Migration completed: 2026-02-16*
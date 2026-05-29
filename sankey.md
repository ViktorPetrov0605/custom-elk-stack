# Sankey Diagram Implementation

## Status: ✅ WORKING

Implemented a custom Vega-based Sankey diagram for the Unfied NetFlow/sFlow monitoring stack (ELK 9.2.4) to visualize source→destination traffic by volume.

---

## Architecture Review

### Stack Versions (as deployed)
| Component | Version | Role |
|-----------|---------|------|
| Elasticsearch | 9.2.4 | Distributed storage, ILM, index templates |
| Kibana | 9.2.4 | Dashboard & visualization UI |
| Logstash | 9.2.4 (custom build) | NetFlow v9 + sFlow collector |
| Docker | 29.4.2 | Container runtime |
| Python | 3.13 | Synthetic data generation |

### Existing Dashboards (Lens-based, no Vega)
- `[Unifed Flow] Conversation Partners` — datatable + donuts + stacked area
- `[Unifed Flow] Top-N` — all datatables (sources, dests, ports, devices)
- `[Unifed Flow] Detailed Traffic Analysis` — timelines + pie + datatables

### Index Template (`logstash-flow-*`)
- 2 shards, 0 replicas
- Serial rollover (`-000001`, `-000002`, ...)
- ILM policy: Hot (5GB primary shard) → Warm (1d → forcemerge) → Delete (3d)
- Fields: `source.ip`, `destination.ip`, `network.bytes`, `network.packets`, `device.ip`, `network.transport`, etc.

### Data Flow
```
Switch (NetFlow v9/sFlow)
  ↓ UDP :2050/:6343
Logstash (decode → rename ECS → sampling multiplier → GeoIP/ASN)
  ↓ HTTPS :9200
Elasticsearch (logstash-flow-write alias → serial indices)
  ↓
Kibana Dashboards (Lens datatables, area, pie)
```

---

## Research: Sankey in Kibana 9.x

### Approach: Vega (not Lens)
Kibana Lens does NOT support Sankey diagrams. Kibana **does** support custom Vega/Vega-Lite visualizations (via "Aggregation Based" → "Vega" in the visualization editor).

### Available References

| Source | Vega Version | Features |
|--------|-------------|----------|
| [Elastic Blog 2018](https://www.elastic.co/blog/sankey-visualization-with-vega-in-kibana) | v3 | Two-level Sankey, src→dst by `doc_count`, composite agg, click-to-filter, "Show All" button |
| [Elastic Labs 2024 GitHub](https://github.com/elastic/elasticsearch-labs/blob/main/supporting-blog-content/add-filter-capabilities-to-vega-sankey-chart/sankey.hjson) | v5 | Same layout + `kibanaAddFilter()` for dashboard-level cross-filtering |
| [Yuri Astrakhan's demo](https://nyurik.github.io/Vega-Sankey-Graph-for-Kibana/) | v3 | Same base code, well-commented |

### How the Vega Sankey Works

1. **ES Query**: Composite aggregation on `source.ip` + `destination.ip` + sub-agg `sum(network.bytes)`
2. **Data Transform Pipeline**:
   - `rawData` → composite agg results
   - `nodes` → fold each (src,dst) pair into 2 rows (one per stack), then calculate `y0`/`y1` stacking positions via Vega stack transform
   - `groups` → aggregate nodes by (stack, IP) for the vertical bars
   - `edges` → lookup matching destination nodes, generate SVG `linkpath`
3. **Rendering**:
   - `path` marks draw the curved Sankey links
   - `rect` marks draw the source/destination vertical bars
   - `text` marks label IPs
4. **Interaction**: Click a group → `groupSelector` signal → filtered redraw. Double-click → reset to all.

---

## Implementation Journey & Bugs Fixed

### Bug 1: HJSON Parse Failure (Error in Dashboard)
**Symptom:** Vega visualization showed "Error" — no console message in Kibana.

**Root cause:** The original spec used HJSON syntax (bare unquoted keys, no quotes on string values). Kibana 9.x stores the spec as JSON string inside `visState.params.spec`. When the original specs were authored as HJSON with unquoted `%context%`, `%timefield%`, and `logstash-flow-*`, the internal parser failed silently.

**Fix:** Convert the entire spec to **pure JSON** (all keys quoted, all strings quoted). HJSON looks cleaner but Kibana 9.x apparently parses the embedded spec as JSON, not HJSON.

**Key differences:**
```
# ❌ BROKEN (HJSON style - unquoted keys with special chars)
url: {
  %context%: true
  %timefield%: "@timestamp"
  index: logstash-flow-*
}

# ✅ FIXED (JSON style)
"url": {
  "%context%": true,
  "%timefield%": "@timestamp",
  "index": "logstash-flow-*"
}
```

### Bug 2: Infinite y-axis Domain
**Symptom:** The Sankey rendered but showed "Infinite extent for field 'y1': [Infinity, -Infinity]" — rendering was invisible except for axis labels.

**Root cause:** Two issues:
1. Raw `network.bytes` values are in the 500KB–50MB range per flow pair. The composite agg returns 100+ pairs. Stacking their **sum** on the y-axis means the total can be 100M–500M per stack. When we divided by 1GB (1073741824), every node value was 0.000x → effectively zero → the y-scale domain became `[0, 0]` → Infinity.
2. Old data: initial test data was generated once, dashboard time range was "Last 15 minutes", but data was from hours ago → zero results → empty domain.

**Fixes:**
- Change scaling: divide by **1MB (1048576)** instead of 1GB
- Generate fresh data within the time window

### Bug 3: Shard Allocation Excluding Local Nodes
**Symptom:** Indices showed UNASSIGNED shards after first deploy.

**Root cause:** The production template has `index.routing.allocation.exclude.node_type: frontend` to keep data on backend-only nodes. On a single-box test where ALL nodes are `dim` (data+ingest+master), this routing rule blocks allocation everywhere.

**Fix:** Removed the routing exclusion from the index template for local testing.

---

## Working Vega JSON Spec (Pure JSON)

The finalized spec is at `dashboards/sankey-flow.hjson` (stored as readable JSON, not HJSON).

### Key Spec Adaptations

| Aspect | Original Reference | This Implementation |
|--------|-------------------|-------------------|
| Data source | `geo.src` / `geo.dest` | `source.ip` / `destination.ip` |
| Metric | `doc_count` | `sum(network.bytes)` |
| Size scaling | Raw doc count | `/ 1048576` (MB) |
| Index | `logstash-*` | `logstash-flow-*` |
| Vega schema | v3 | v5 |
| Format | HJSON | Pure JSON |
| Composite size | 10000 | 1000 |
| Node key separator | " → " | "\|" (safer for Vega) |

### Spec Structure (abbreviated)

```json
{
  "$schema": "https://vega.github.io/schema/vega/v5.json",
  "data": [
    { "name": "rawData", "url": { "%context%": true, "index": "logstash-flow-*", ... } },
    { "name": "nodes", "source": "rawData", "transform": [ "fold", "stack", ... ] },
    { "name": "groups", "source": "nodes", "transform": [ "aggregate", "stack", ... ] },
    { "name": "destinationNodes", "source": "nodes", ... },
    { "name": "edges", "source": "nodes", "transform": [ "lookup", "linkpath", ... ] }
  ],
  "scales": [ "x": "band", "y": "linear", "color": "ordinal" ],
  "marks": [ "path" for edges, "rect" for groups, "text" for labels ],
  "signals": [ "groupHover", "groupSelector" ]
}
```

The full spec is in `dashboards/sankey-flow.hjson`.

---

## Synthetic Data Generation

### Strategy: Direct ES Bulk API
Generate documents matching the Logstash ECS schema and POST via `_bulk` API. No Logstash, no containers, no device config needed.

### Generator
**Script:** `scripts/generate-synthetic-flow-data.py`

**Schema (every doc matches what Logstash produces):**
```json
{
  "@timestamp": "ISO8601",
  "source.ip": "str",
  "source.port": int,
  "destination.ip": "str",
  "destination.port": int,
  "network.bytes": int,
  "network.packets": int,
  "network.transport": "tcp|udp|icmp",
  "network.iana_number": "6|17|1",
  "device.ip": "str",
  "device.name": "str",
  "event.type": "netflow"
}
```

**Usage:**
```bash
python3 scripts/generate-synthetic-flow-data.py --count 5000
python3 scripts/generate-synthetic-flow-data.py --count 10000 --seed 42
python3 scripts/generate-synthetic-flow-data.py --es-url https://192.168.122.160:9200 --password telehouse
```

**Test IP Pool:**
- Sources: `10.0.0.1-4`, `192.168.1.10-40`, `172.16.0.5-8`
- Destinations: `8.8.8.8`, `8.8.4.4`, `1.1.1.1`, `1.0.0.1`, `185.148.163.50`, `10.57.144.162`, plus cloud IPs
- Collectors (device.ip): `192.168.36.21`, `.22`, `.25`, `.26`, `.70`, `.71` (matches device-lookup.json)

**Byte distribution:** Uses `random.lognormvariate(12, 1.8)` → 10KB - 50MB per flow pair, realistic variation.

### Alternative: nflow-generator (Real NetFlow Packets)
Available as `networkstatic/nflow-generator` Docker image. Generates NetFlow v5 UDP packets:
```bash
docker run --rm networkstatic/nflow-generator -t <LOGSTASH_IP> -p 2050
```
Exercises the **full pipeline** (Logstash decode → filter → ES), but requires Logstash running + 1-5 min template delay.

### Why Direct Bulk Is Better for Testing
| Factor | nflow-generator | Direct Bulk |
|--------|----------------|-------------|
| Startup delay | 1-5 min (template) | Immediate |
| Pipeline test | Full | Partial (skip Logstash) |
| Data control | Random fields | Full control |
| Simplicity | Docker + network | Python + HTTP call |
| Cleanup | Port conflicts | `DELETE logstash-flow-write` |

---

## Local Single-Machine Deployment

### Environment
- **Host:** Debian 13, 16 cores, 15GB RAM
- **IP:** 192.168.122.160
- **Docker:** 29.4.2, Compose v5.1.3

### Architecture (All on one box)
```
Frontend (2 ES nodes + Kibana):
  custom-elk-stack-es-frontend-1    :9200 (ES HTTP)  :9300 (transport)
  custom-elk-stack-es-frontend-2    :9201            :9301
  custom-elk-stack-kibana-1         :5601
```

### Key Config Changes from Production

1. **Memory limits reduced** — ES 1.5GB each, Kibana 1GB (vs 4GB in prod)
2. **Added `ES_JAVA_OPTS=-Xms1g -Xmx1g`** — prevents JVM from grabbing all memory
3. **Removed `index.routing.allocation.exclude.node_type: frontend`** — single-box has no dedicated data nodes
4. **Removed NetFlow auto-installer** — not needed for testing
5. **Disable `bootstrap.memory_lock=false`** — not possible inside container without privileged mode

### Deployment Walkthrough
```bash
cd custom-elk-stack

# Generate config template
./deploy.sh --generate
# Edit deploy.conf with local IP and credentials

# Start frontend (2 ES nodes + Kibana)
./deploy.sh --frontend

# Wait ~2min for ES to form cluster, then:
./deploy.sh --import

# Verify
curl -k -u elastic:telehouse https://192.168.122.160:9200/_cat/nodes?v

# Generate test data
python3 scripts/generate-synthetic-flow-data.py --count 5000 --verify
```

### Verification
```bash
curl -k -u elastic:telehouse https://192.168.122.160:9200/_cluster/health
curl -k -u elastic:telehouse https://192.168.122.160:9200/_cat/indices/logstash-flow-*?v
curl -k -u elastic:telehouse https://192.168.122.160:9200/logstash-flow-000001/_count
```

### What Didn't Work
- **es-remote backend container** — all nodes on same host causes transport port conflicts (same IP, overlapping 9300). Not needed for Sankey testing.
- **Logstash** — brought down for local testing. Direct `_bulk` API is cleaner for this purpose.

---

## How to Install the Sankey Visualisation in Production

1. **Go to Kibana** → **Visualize Library** → **Create Visualization**
2. Select **Vega** (under "Aggregation Based")
3. Copy the JSON spec from `dashboards/sankey-flow.hjson` (the PURE JSON version, not HJSON)
4. Save as `[Flow] Traffic Sankey`
5. Add to any dashboard as a new panel

### Customising for Your Network
- **Index pattern:** Update `"index": "logstash-flow-*"` if your index differs
- **Fields:** Change `source.ip`, `destination.ip`, `network.bytes` to match your field mapping
- **Scale:** Adjust the divisor (`/ 1048576` = MB) if your byte volumes differ — aim for node values in 1-1000 range
- **Composite size:** `"size": 1000` — increase for more pairs, decrease for performance

---

## Known Limitations

1. **Composite aggregations are pagination-only** — if you have >1000 src-dst pairs, you'll miss some. A future improvement could use `sigterms` with `sum(network.bytes)` for true top-N.
2. **Vega renderer slows down with >200 edges** — the composite limit and `clip: true` on paths help.
3. **IP addresses as labels** — IPs can be ugly with many nodes. The `device-lookup.json` field formatter won't apply to Vega (it's an index-pattern Lens formatter).
4. **No dashboard cross-filtering** — Clicking on a group only filters within the Vega viz. To enable dashboard-level filtering, add `kibanaAddFilter()` in the signal handler (requires additional Kibana integration).

---

## Repo Status

All files committed to `custom-elk-stack`:

| File | Contents | Status |
|------|----------|--------|
| `sankey.md` | This document | ✅ Latest |
| `dashboards/sankey-flow.hjson` | The working Vega JSON spec | ✅ Pure JSON format |
| `scripts/generate-synthetic-flow-data.py` | Python data generator | ✅ Tested with 5000 docs |
| `templates/logstash-flow-template.json` | Removed `exclude.node_type: frontend` | ✅ Fixed for single-box |
| `docker-compose-frontend.yml` | Reduced mem + ES_JAVA_OPTS | ✅ Working |

---

## Lessons Learned (ELK Vega on 9.x)

1. **Use pure JSON, not HJSON** — Kibana 9.x stores spec inside `visState.params.spec` as a JSON string. HJSON syntax (bare unquoted keys) causes silent parse failures. Even `%context%` and `logstash-flow-*` need quotes.

2. **Scale your data** — Raw bytes from NetFlow can be 10MB+ per flow. Stacking 100+ pairs gives y-axis values in hundreds of millions. Divide by 1MB (1048576) to keep Vega maths in a sane range.

3. **Fresh data matters** — The dashboard defaults to "Last 15 minutes". If data is hours old, Vega gets zero results → `[Infinity, -Infinity]` domain.

4. **ES routing rules break single-box** — Production templates use `index.routing.allocation.exclude.node_type: frontend`. On a single box where all nodes are `data+ingest+master`, this blocks shard allocation everywhere.

5. **Browser console is the only debug view** — Vega errors in Kibana 9.x don't appear in the UI. Only `console.error` in browser dev tools reveals the actual error message.

---

## TODO / Future Improvements

- [ ] Add **kibanaAddFilter()** to the click handler for dashboard-level cross-filtering
- [ ] Add **sigterms** aggregation for true top-N instead of composite pagination
- [ ] Add **multi-stack Sankey** (source → destination, then destination → AS, three columns)
- [ ] Add **sampling rate weight** to handle mixed-rate collectors

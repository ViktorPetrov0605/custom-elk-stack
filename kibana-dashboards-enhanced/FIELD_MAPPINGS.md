# Unified Flow Dashboard Field Mappings

This document describes the field mappings used to adapt the NetFlow dashboards to the unified-flow-* index pattern.

## Source to Target Field Mapping

### Index Pattern
| Source (NetFlow) | Target (Unified Flow) |
|------------------|----------------------|
| `logs-*` | `unified-flow-*` |

### Key Field Mappings

| NetFlow Field | Unified Flow Field | Notes |
|---------------|-------------------|-------|
| `agent.name` | `device.name` | Flow exporter device name |
| `netflow.exporter.version` | `device.name` | Grouping by device version (use scripted field if needed) |
| `netflow.ingress_interface` | `interface.input` | Input interface |
| `netflow.egress_interface` | `interface.output` | Output interface |
| `source.as.organization.name` | `source.as.number` | Use AS number instead of org name |
| `destination.as.organization.name` | `destination.as.number` | Use AS number instead of org name |
| `data_stream.dataset` filter | *removed* | Not needed for unified schema |
| `destination.geo.*` | *removed* | Geo fields not available in unified schema |
| `source.geo.*` | *removed* | Geo fields not available in unified schema |
| `network.type` | `network.type` or omitted | Can use network.type if available |

### Common Fields (No Change)
These fields are the same in both schemas:

| Field | Description |
|-------|-------------|
| `@timestamp` | Event timestamp |
| `source.ip` | Source IP address |
| `source.port` | Source port |
| `destination.ip` | Destination IP address |
| `destination.port` | Destination port |
| `network.transport` | Transport protocol (tcp, udp, etc.) |
| `network.bytes` | Total bytes transferred |
| `network.packets` | Total packets transferred |

### Visualization Type Mapping

| NetFlow Dashboard | Unified Flow Dashboard | Key Changes |
|-------------------|------------------------|-------------|
| `[Logs Netflow] Traffic Analysis` | `[Unified Flow] Detailed Traffic Analysis` | agent.name → device.name, removed geo visualizations |
| `[Logs Netflow] Top-N` | `[Unified Flow] Top-N Analysis` | AS org name → AS number, added device metrics |
| `[Logs Netflow] Conversation Partners` | `[Unified Flow] Conversation Partners` | Simplified, device-based timeline added |
| `[Logs Netflow] Flow records` | *not included* | Replaced by table in Detailed Analysis |
| `[Logs Netflow] Flow Exporters` | *merged into* Top-N | Device metrics now in Top-N dashboard |
| `[Logs Netflow] Geo Location` | *not included* | No geo fields in unified schema |
| `[Logs Netflow] Autonomous Systems` | *merged into* Top-N | AS analysis in Top-N dashboard |
| `[Logs Netflow] Overview` | *merged into* all dashboards | Key metrics distributed |

## Dashboard Features

### [Unified Flow] Detailed Traffic Analysis
- **Flow Records Timeline**: Stacked bar chart by device with colorful palette
- **Total Flow Records**: Large metric card
- **Sources Donut**: Top sources by bytes (temperature palette)
- **Destinations Donut**: Top destinations by bytes (complementary palette)
- **Protocol Distribution**: Transport protocol breakdown (warm palette)
- **Device Traffic by Bytes**: Stacked area chart (rainbow palette)
- **Device Traffic by Packets**: Stacked area chart (ocean palette)
- **Metric Cards**: Unique sources, destinations, source ports, destination ports

### [Unified Flow] Top-N Analysis
- **Top Sources**: Data table with bytes, packets, flow count
- **Top Destinations**: Data table with bytes, packets, flow count
- **Top Source Ports**: Data table with metrics
- **Top Destination Ports**: Data table with metrics
- **Top Protocols**: Data table summary
- **Top Devices**: Data table by device.name
- **Top Source AS**: Data table using source.as.number
- **Top Destination AS**: Data table using destination.as.number

### [Unified Flow] Conversation Partners
- **Conversation Partners**: Data table showing source/destination pairs
- **IP Version & Protocol**: Donut chart by network.type and network.transport
- **Source/Dest Ports**: Port pair distribution (donut)
- **Top Src-Dst Pairs**: Top conversation pairs by bytes
- **Top Devices**: Horizontal bar chart
- **Device Traffic Timeline**: Line chart by device

## Palette Usage

Each visualization uses a specific color palette for better visual distinction:

| Visualization | Palette | Colors |
|--------------|---------|--------|
| Traffic timeline | status | Blue/green status colors |
| Sources donut | temperature | Red-yellow temperature scale |
| Destinations donut | complementary | Complementary color pairs |
| Protocol distribution | warm | Red/orange/yellow |
| Device traffic bytes | rainbow | Full rainbow spectrum |
| Device traffic packets | ocean | Blue-green ocean colors |

## Configuration

### Time Settings
- **Time Range**: Last 15 minutes (can be adjusted)
- **Auto-refresh**: Every 15 seconds
- **Refresh pause**: false (auto-refresh enabled by default)

### Layout
- **Width**: Full 48-column grid (Kibana default)
- **Margins**: Enabled
- **Panel titles**: Visible
- **Cursor sync**: Enabled
- **Tooltip sync**: Disabled

## Import Instructions

1. Ensure the `unified-flow-*` index pattern exists in Kibana
2. Run the import script:
   ```bash
   ./import-dashboards.sh unified-flow-dashboards-combined.ndjson
   ```
3. Or manually import via Kibana UI:
   - Stack Management → Saved Objects → Import
   - Select the NDJSON file
   - Check "Automatically overwrite saved objects"

## Troubleshooting

### Missing Index Pattern
If you see errors about missing index patterns:
```bash
# Create the index pattern via API
curl -X POST http://localhost:5601/api/saved_objects/index-pattern/unified-flow-* \
  -H "Content-Type: application/json" \
  -H "kbn-xsrf: true" \
  -u elastic:changeme \
  -d '{"attributes":{"title":"unified-flow-*","timeFieldName":"@timestamp"}}'
```

### No Data Showing
- Verify data is flowing to unified-flow-* indices
- Check that field names match exactly
- Use Kibana Dev Tools to verify field mappings:
  ```
  GET unified-flow-*/_mapping/field/device.name
  ```

### Field Conflicts
If fields show as "conflict" in Kibana:
- The field may have different types across indices
- Refresh the index pattern in Stack Management
- Re-create the index pattern if necessary

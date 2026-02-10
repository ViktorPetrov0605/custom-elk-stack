# KQL Filter Guide for Device Filtering (Kibana 9.x)

## Background
The `input_control_vis` visualization type used for device filtering is **DEPRECATED** in Kibana 9.x. It has been removed from the Unified Flow Dashboard to prevent errors.

## Using KQL (Kibana Query Language) Instead

You can filter by device IP directly in the Kibana search bar using KQL syntax:

### Basic Device Filtering

```kql
# Filter by specific device (flow exporter IP)
flow.export.ip.addr: 10.4.4.93

# Filter by multiple devices
flow.export.ip.addr: (10.4.4.93 OR 10.4.4.3)

# Filter by device subnet
flow.export.ip.addr: 10.4.4.0/24

# Filter by specific device AND time range (combined with other filters)
flow.export.ip.addr: 10.4.4.93 AND flow.bytes > 1000000
```

### Common Filter Examples

| Filter Purpose | KQL Query |
|---------------|-----------|
| Specific device | `flow.export.ip.addr: 10.4.4.93` |
| Multiple devices | `flow.export.ip.addr: (10.4.4.93 OR 10.4.4.3)` |
| Juniper only | `flow.export.ip.addr: 10.4.4.93` |
| Nexus only | `flow.export.ip.addr: 10.4.4.3` |
| Exclude device | `NOT flow.export.ip.addr: 10.4.4.93` |
| Device + Protocol | `flow.export.ip.addr: 10.4.4.93 AND flow.protocol: TCP` |

### Using the Filter UI

1. Click **Add filter** in Kibana
2. Select field: `flow.export.ip.addr`
3. Choose operator: `is` or `is one of`
4. Enter the IP address(es)
5. Click **Add filter**

### Using Kibana Controls (Recommended Alternative)

For interactive filtering, use the newer **Controls** feature:

1. Edit the dashboard
2. Click **Add control**
3. Configure:
   - **Control type**: Options list
   - **Field**: `flow.export.ip.addr`
   - **Label**: "Device IP"
4. Save the dashboard

This creates an interactive dropdown without using the deprecated input_control_vis.

---
**Note:** Dashboard updated on 2026-02-10 to remove deprecated visualizations.

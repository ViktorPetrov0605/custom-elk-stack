# Enhanced Unified Flow Dashboard - Complete Guide

## 🎯 Dashboard Overview

**Dashboard ID:** `unified-flow-1770732722`  
**URL:** http://10.4.4.87:5601/app/dashboards#/view/unified-flow-1770732722  
**Total Panels:** 8 visualizations

---

## 📊 All Visualizations

### Row 1: Device Filter + Traffic Overview
| Panel | Type | Field(s) | Purpose |
|-------|------|----------|---------|
| **Device Filter** | Input Control | `flow.export.ip.addr` | Select which device's flows to display |
| **Traffic Over Time** | Line | `flow.bytes` + `@timestamp` | Trend analysis |

### Row 2: Source Analysis
| Panel | Type | Field(s) | Purpose |
|-------|------|----------|---------|
| **Top Source IPs** | Horizontal Bar | `flow.src.ip.addr` | Who's sending most traffic |
| **Top Source Ports** | Horizontal Bar | `flow.src.port` | Which ports are sending |
| **Hourly Traffic** | Line | `@timestamp` (hour) | Peak hours analysis |

### Row 3: Destination Analysis
| Panel | Type | Field(s) | Purpose |
|-------|------|----------|---------|
| **Top Destination IPs** | Horizontal Bar | `flow.dst.ip.addr` | Top targets |
| **Top Destination Ports** | Horizontal Bar | `flow.dst.port` | Target services |
| **Protocol Distribution** | Pie | `l4.proto.name` | Protocol breakdown |

---

## 🔧 Device Filtering Guide

### Method 1: Device Filter Dropdown (Easiest)
1. Look at the **"Device Filter"** panel at top of dashboard
2. Click the dropdown
3. Select device IP:
   - `10.4.4.3` — Nexus switch
   - `10.4.4.93` — Juniper (when data flows)
4. All panels update automatically

### Method 2: Kibana Query Language (KQL)
Click the search bar and type:
```
flow.export.ip.addr: 10.4.4.3
```
Or for multiple devices:
```
flow.export.ip.addr: (10.4.4.3 or 10.4.4.93)
```

### Method 3: Add Filter Button
1. Click "Add filter" (top left)
2. Field: `flow.export.ip.addr`
3. Operator: `is`
4. Value: Enter device IP

### Method 4: Saved Searches (For Reuse)
Save filtered views:
- **Nexus View:** `flow.export.ip.addr: 10.4.4.3`
- **Combined View:** No filter (all devices)

---

## 📈 Field Reference

| What You Want | Field Name | Example Values |
|---------------|------------|----------------|
| Traffic volume | `flow.bytes` | 1492, 65535 |
| Source IP | `flow.src.ip.addr` | 192.168.1.1 |
| Destination IP | `flow.dst.ip.addr` | 10.0.0.1 |
| Source Port | `flow.src.port` | 443, 22, 3389 |
| Destination Port | `flow.dst.port` | 80, 443, 53 |
| Protocol | `l4.proto.name` | TCP, UDP, ESP, ICMP |
| Device/Exporter | `flow.export.ip.addr` | 10.4.4.3, 10.4.4.93 |
| Direction | `flow.direction.name` | Ingress, Egress |
| Time | `@timestamp` | 2026-02-10T09:30:00Z |

---

## 🎨 Tips & Tricks

### Time Range
- Use time picker (top right) for historical analysis
- Common ranges: "Last 15 minutes", "Last 4 hours", "Today"
- Custom: Click "Absolute" for specific dates

### Refresh
- Click 🔄 to refresh manually
- Set "Refresh every" (e.g., 30s) for live monitoring

### Panel Actions
- **Full screen:** Click panel title → "Maximize"
- **Inspect:** Click panel → "Inspect" to see raw data
- **Download:** Click panel → "Download as CSV" for reports

### Multiple Filters
Combine filters:
- Device + Time range + Protocol
- Example: Nexus (10.4.4.3) + TCP + Last hour

---

## 🔍 Use Cases

### "Show me Nexus traffic only"
1. Device Filter → Select `10.4.4.3`
2. All panels update

### "Find top ports hitting us"
1. Clear all filters
2. Look at "Top Destination Ports" panel
3. Ports like 22 (SSH), 3389 (RDP) may indicate scan attempts

### "When is peak traffic?"
1. Set time range to "Last 7 days"
2. View "Hourly Traffic" panel
3. Identify busy hours

### "What protocols are in use?"
1. View "Protocol Distribution" pie chart
2. Common: UDP (DNS, streaming), TCP (web), ESP (VPN)

---

## 🚨 Currently Available Data

| Device | Exporter IP | Status | Records |
|--------|-------------|--------|---------|
| **Nexus-1** | 10.4.4.3 | ✅ Active | 2,172,727 flows |
| **Juniper** | 10.4.4.93 | ⚠️ Partial | Legacy indices |

**Note:** Only Nexus actively sending flows via ElastiFlow. Juniper data is in older indices.

---

## 📝 GitHub Resources

- **Dashboard Export:** `kibana/dashboards/unified-flow-dashboard.json`
- **Install Script:** `kibana/scripts/install-dashboard.sh`
- **This Guide:** `kibana/ENHANCED_DASHBOARD_GUIDE.md`

---

## 🆘 Troubleshooting

### "No results found"
1. Check time range (try "Last 30 days")
2. Check device filter (clear if needed)
3. Verify data exists in ES on port 9200

### Dashboard won't load
1. Verify Kibana: http://10.4.4.87:5601
2. Check cluster health: `curl https://10.4.4.87:9200/_cluster/health`

### Device not in filter list
- Device must have sent flows recently
- Check ElastiFlow collector status
- Verify firewall allows UDP 6343 (sFlow) or 2050 (NetFlow)

---

*Last updated: 2026-02-10*  
*Dashboard Version: 2.0 (Enhanced with device filtering)*

# Kibana Setup Guide - Manual Steps

## ✅ PREREQUISITES COMPLETED

- 122,000+ flow documents indexed with unified schema
- All data has 4096x sampling multiplier applied
- ILM policy active (1-day retention)

---

## 🔧 STEP 1: Access Kibana

**URL:** https://10.4.4.87:5601  
**Credentials:** elastic / telehouse

> Note: Browser will show SSL warning (self-signed cert). Click "Advanced" → "Proceed".

---

## 📊 STEP 2: Create Index Pattern

1. Go to **Stack Management** → **Index Patterns**
2. Click **Create index pattern**
3. Pattern name: `unified-flow-*`
4. Time field: `@timestamp`
5. Click **Create index pattern**

---

## 📈 STEP 3: Create Visualizations

### Visualization 1: Traffic Volume Over Time
- Type: **Area** or **Line**
- Index: `unified-flow-*`
- Y-axis: Sum of `network.bytes`
- X-axis: Date Histogram `@timestamp` (Auto or 1m)
- Title: "Traffic Volume Over Time"

### Visualization 2: Top Source IPs
- Type: **Pie** or **Data Table**
- Index: `unified-flow-*`
- Metrics: Sum of `network.bytes`
- Buckets: Terms aggregation on `source.ip` (Top 10)
- Title: "Top 10 Source IPs"

### Visualization 3: Top Destination IPs
- Type: **Pie** or **Data Table**
- Index: `unified-flow-*`
- Metrics: Sum of `network.bytes`
- Buckets: Terms aggregation on `destination.ip` (Top 10)
- Title: "Top 10 Destination IPs"

### Visualization 4: Protocol Distribution
- Type: **Pie**
- Index: `unified-flow-*`
- Metrics: Sum of `network.bytes`
- Buckets: Terms on `network.transport` (tcp, udp, icmp)
- Title: "Protocol Distribution"

### Visualization 5: Top Source AS Numbers
- Type: **Bar Vertical**
- Index: `unified-flow-*`
- Metrics: Sum of `network.bytes`
- Buckets: Terms on `source.as.number` (Top 10)
- Title: "Top 10 Source AS Numbers"

### Visualization 6: Top Destination AS Numbers
- Type: **Bar Vertical**
- Index: `unified-flow-*`
- Metrics: Sum of `network.bytes`
- Buckets: Terms on `destination.as.number` (Top 10)
- Title: "Top 10 Destination AS Numbers"

### Visualization 7: Interface Traffic
- Type: **Bar Vertical Stacked**
- Index: `unified-flow-*`
- Metrics: Sum of `network.bytes`
- Buckets X: Terms on `interface.input` (Top 10)
- Split series: Terms on `device.name`
- Title: "Interface Traffic Summary"

### Visualization 8: Top Source Ports
- Type: **Data Table**
- Index: `unified-flow-*`
- Metrics: Sum of `network.bytes`, Count
- Buckets: Terms on `source.port` (Top 20)
- Title: "Top Source Ports"

### Visualization 9: Top Destination Ports
- Type: **Data Table**
- Index: `unified-flow-*`
- Metrics: Sum of `network.bytes`, Count
- Buckets: Terms on `destination.port` (Top 20)
- Title: "Top Destination Ports"

---

## 📋 STEP 4: Create Dashboard

1. Go to **Dashboard** → **Create new dashboard**
2. Title: "Network Flow Analytics"
3. Add all 9 visualizations above
4. **Add Device Filter**:
   - In top bar, click **Add filter**
   - Field: `device.name`
   - Operator: is / is one of
   - Values: `juniper-sw`, `cisco-nexus`
   - Save filter as "Device Selector"

5. **Enable auto-refresh**: 30 seconds
6. **Set time range**: Last 1 hour (or Last 15 minutes for real-time)
7. Save dashboard

---

## 🔍 AVAILABLE FIELDS TO VISUALIZE

| Field | Type | Use For |
|-------|------|---------|
| `device.name` | keyword | Filter (juniper-sw / cisco-nexus) |
| `source.ip` | ip | Top sources |
| `destination.ip` | ip | Top destinations |
| `source.port` | integer | Service ports |
| `destination.port` | integer | Service ports |
| `network.transport` | keyword | Protocol (tcp/udp/icmp) |
| `network.bytes` | long | Traffic volume |
| `network.packets` | long | Packet counts |
| `source.as.number` | integer | BGP AS paths |
| `destination.as.number` | integer | BGP AS paths |
| `interface.input` | integer | Ingress interface |
| `interface.output` | integer | Egress interface |

---

## 📊 FILTER EXAMPLES

### Show only Juniper data:
```
device.name: juniper-sw
```

### Show only Cisco Nexus data:
```
device.name: cisco-nexus
```

### Show specific IP traffic:
```
source.ip: 192.168.1.1 or destination.ip: 192.168.1.1
```

### Show specific protocol:
```
network.transport: tcp
```

### Show high-volume flows (>1GB):
```
network.bytes > 1073741824
```

---

## 🎯 SAMPLE DASHBOARD LAYOUT

```
┌─────────────────────────┬─────────────────────────┐
│  Traffic Volume         │  Top Source IPs         │
│  Over Time              │  (Pie Chart)            │
├─────────────────────────┼─────────────────────────┤
│  Protocol Distribution  │  Top Source AS          │
│  (Pie)                  │  (Bar Chart)            │
├─────────────────────────┴─────────────────────────┤
│  Interface Traffic (Stacked Bar by Device)        │
├─────────────────────────┬─────────────────────────┤
│  Top Ports (Table)      │  Top Dest AS (Bar)      │
└─────────────────────────┴─────────────────────────┘
```

---

## 💾 DATA RETENTION

- Index pattern: `unified-flow-*`
- ILM Policy: Automatic deletion after 1 day
- Current docs: 122,000+ and growing
- Sampling: 4096x multiplier applied

---

## 🔧 TROUBLESHOOTING

### No data in visualizations?
1. Check time range is recent (Last 1 hour)
2. Verify index pattern matches `unified-flow-*`
3. Check device.name filter isn't too restrictive

### SSL Certificate Warning?
- This is expected with self-signed certificates
- Click "Advanced" → "Proceed to site"
- Or add certificate exception in browser

### Slow queries?
- Reduce time range (Last 15 min instead of 24 hours)
- Add device.name filter to limit data scope
- Use sampling if visualizing millions of records

---

## 📞 SSH ACCESS (If Needed)

```bash
# Frontend
ssh telehouse@10.4.4.87  # pass: T3l3h0us#

# Backend N1 (NetFlow)
ssh -p 2332 telehouse@10.4.4.21  # pass: T3l3h0us#

# Backend N2 (sFlow)
ssh telehouse@10.4.4.90  # pass: T3l3h0us#
```

---

## 📝 NOTES

- All NetFlow data from Juniper has 4096x sampling multiplier applied
- sFlow data from Cisco is un-sampled (actual counts)
- Device filter allows switching between Juniper/Cisco/all devices instantly
- Data older than 1 day is automatically deleted per ILM policy
# Kibana Dashboard - IP Address Filtering Guide

## How to Filter by IP Addresses in the Dashboard

### Method 1: Global Filter Bar (Recommended)
1. Open the dashboard: `http://10.4.4.87:5601/app/dashboards#/view/network-flow-dashboard`
2. Look at the top of the page - you'll see a search/filter bar
3. Click on it and type KQL (Kibana Query Language) queries:

**Filter by Source IP:**
```
source.ip: 192.168.1.100
```

**Filter by Destination IP:**
```
destination.ip: 10.4.4.87
```

**Filter by multiple IPs:**
```
source.ip: (192.168.1.100 or 192.168.1.101)
```

**Filter by IP range:**
```
source.ip: 192.168.1.0/24
```

**Exclude an IP:**
```
NOT source.ip: 192.168.1.1
```

### Method 2: Visualization-Specific Filter
1. Click on any visualization (pie chart, bar chart, etc.)
2. Click on a specific data point (e.g., an IP address in the pie chart)
3. Select "Filter for value" to filter the entire dashboard

### Method 3: Create a New Filter
1. Click "Add filter" button (top left)
2. Select field: `source.ip` or `destination.ip`
3. Choose operator: "is", "is one of", "is between", "exists"
4. Enter the IP address value
5. Click "Add filter"

### Common Filter Combinations

**Specific Device:**
```
device.name: juniper-sw
```

**Traffic from specific source to specific dest:**
```
source.ip: 192.168.1.100 and destination.ip: 10.4.4.87
```

**Top talkers (by traffic volume):**
```
network.bytes > 1000000
```

**Specific protocol:**
```
network.transport: tcp
```

**Time range + IP:**
First set time range (top right), then add IP filter

### Saving Filters
1. After adding filters, click "Save" button
2. The dashboard will save with your current filter set
3. To remove filters, click the "X" on each filter pill

### Creating IP-Based Visualizations

**Top Source IPs (already exists):**
- Pie chart showing top 10 source.ip by sum of network.bytes

**To create new IP-based visualization:**
1. Go to Analytics → Visualize Library
2. Click "Create visualization"
3. Select data view: `unified-flow-*`
4. Choose chart type: Pie, Bar, or Table
5. Configure:
   - Metrics: Sum of `network.bytes` or Count
   - Buckets: Terms aggregation on `source.ip` or `destination.ip`
6. Save and add to dashboard

### Filter by Device
The unified schema includes `device.name` field:
- `juniper-sw` - Juniper switches (NetFlow)
- `cisco-nexus` - Cisco Nexus (sFlow)

Filter by device:
```
device.name: juniper-sw
```

### Tips
- Filters affect ALL visualizations on the dashboard
- Click on chart segments to drill down
- Use the time picker (top right) to change date ranges
- Export filtered data: Share → CSV Reports

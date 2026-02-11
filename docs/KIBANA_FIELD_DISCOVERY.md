# Viewing All Field Values in Kibana

## Method 1: Field Selector (Fastest)
1. Open the dashboard: `http://10.4.4.87:5601`
2. Look at the left sidebar for available fields
3. Find `device.name` and click it
4. Shows top 5 values and count

## Method 2: Add Filter Dropdown
1. Click "Add filter" button (top left)
2. Select field: `device.name`
3. Select operator: "is"
4. The value dropdown will show all available options:
   - `juniper-sw` (NetFlow from Juniper switches)
   - `cisco-nexus` (sFlow from Cisco Nexus switches)
   - Any other devices you've configured

## Method 3: Discover View (See All Values)
1. Go to Analytics → Discover
2. Select data view: `unified-flow-*`
3. In the search bar, leave empty or use `*`
4. Look at `device.name` field on the left sidebar
5. Click it to expand and see all values with document counts

## Method 4: Aggregation Query (Advanced)
```json
GET unified-flow-*/_search
{
  "size": 0,
  "aggs": {
    "devices": {
      "terms": {
        "field": "device.name",
        "size": 100
      }
    }
  }
}
```

## Currently Active Devices
Based on your setup:
- `juniper-sw` → NetFlow from 10.4.4.21 (Backend N1)
- `cisco-nexus` → sFlow from 10.4.4.90 (Backend N2)

Add more devices by updating the Logstash config `device.name` field.

## Quick Filter Examples
```
# Specific device
device.name: juniper-sw

# Exclude device
NOT device.name: cisco-nexus

# Multiple devices
device.name: (juniper-sw or cisco-nexus)

# Device + Time + IP
device.name: juniper-sw AND source.ip: 192.168.1.0/24
```

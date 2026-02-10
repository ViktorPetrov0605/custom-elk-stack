#!/usr/bin/env python3
"""
Create Additional Visualizations for Enhanced Unified Dashboard
"""

import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

KIBANA_URL = "http://10.4.4.87:5601"
AUTH = ("elastic", "telehouse")
HEADERS = {
    "Content-Type": "application/json",
    "kbn-xsrf": "true"
}

INDEX_PATTERN = "elastiflow-flow"
DASHBOARD_ID = "unified-flow-1770732722"

results = {}

def api_call(method, endpoint, data=None):
    url = f"{KIBANA_URL}/api{endpoint}"
    try:
        if method == "POST":
            return requests.post(url, json=data, auth=AUTH, headers=HEADERS, verify=False, timeout=30)
        elif method == "GET":
            return requests.get(url, auth=AUTH, headers=HEADERS, verify=False, timeout=30)
        elif method == "PUT":
            return requests.put(url, json=data, auth=AUTH, headers=HEADERS, verify=False, timeout=30)
    except Exception as e:
        return None

def create_control_vis(name, field):
    """Create input control visualization"""
    payload = {
        "attributes": {
            "title": name,
            "visState": json.dumps({
                "title": name,
                "type": "input_control_vis",
                "aggs": [],
                "params": {
                    "controls": [{
                        "id": "flow_exporter_control",
                        "fieldName": field,
                        "label": "Flow Exporter Device",
                        "type": "list",
                        "options": {
                            "type": "terms",
                            "multiselect": True,
                            "dynamicOptions": True,
                            "size": 20,
                            "order": "desc"
                        },
                        "indexPattern": INDEX_PATTERN
                    }],
                    "updateFiltersOnChange": False,
                    "useTimeFilter": True,
                    "pinFilters": False
                }
            }),
            "uiStateJSON": "{}",
            "kibanaSavedObjectMeta": {
                "searchSourceJSON": json.dumps({"query": {"query": "", "language": "kuery"}, "filter": []})
            }
        }
    }
    r = api_call("POST", "/saved_objects/visualization", payload)
    if r and r.status_code in [200, 201]:
        return r.json().get('id')
    return None

def create_table_vis(name, bucket_field, metric_field="flow.bytes"):
    """Create table visualization"""
    payload = {
        "attributes": {
            "title": name,
            "visState": json.dumps({
                "title": name,
                "type": "table",
                "aggs": [
                    {"id": "1", "enabled": True, "type": "sum", "schema": "metric", "params": {"field": metric_field, "customLabel": "Bytes"}},
                    {"id": "2", "enabled": True, "type": "terms", "schema": "bucket",
                     "params": {"field": bucket_field, "size": 20, "order": "desc", "orderBy": "1"}}
                ],
                "params": {"perPage": 20, "showMeticsAtAllLevels": False}
            }),
            "uiStateJSON": json.dumps({"vis": {"params": {"sort": {"columnIndex": 1, "direction": "desc"}}}}),
            "kibanaSavedObjectMeta": {
                "searchSourceJSON": json.dumps({
                    "index": INDEX_PATTERN,
                    "query": {"query": "", "language": "kuery"},
                    "filter": []
                })
            }
        }
    }
    r = api_call("POST", "/saved_objects/visualization", payload)
    if r and r.status_code in [200, 201]:
        return r.json().get('id')
    return None

def create_bar_vis(name, x_field, y_field):
    """Create bar chart visualization"""
    payload = {
        "attributes": {
            "title": name,
            "visState": json.dumps({
                "title": name,
                "type": "histogram",
                "aggs": [
                    {"id": "1", "enabled": True, "type": "count", "schema": "metric", "params": {"customLabel": "Count"}},
                    {"id": "2", "enabled": True, "type": "date_histogram", "schema": "segment",
                     "params": {"field": x_field, "calendar_interval": "1h", "min_doc_count": 1}}
                ],
                "params": {
                    "type": "histogram",
                    "addTooltip": True,
                    "addLegend": True,
                    "legendPosition": "right"
                }
            }),
            "uiStateJSON": "{}",
            "kibanaSavedObjectMeta": {
                "searchSourceJSON": json.dumps({
                    "index": INDEX_PATTERN,
                    "query": {"query": "", "language": "kuery"},
                    "filter": []
                })
            }
        }
    }
    r = api_call("POST", "/saved_objects/visualization", payload)
    if r and r.status_code in [200, 201]:
        return r.json().get('id')
    return None

def create_pie_vis(name, bucket_field):
    """Create pie chart visualization"""
    payload = {
        "attributes": {
            "title": name,
            "visState": json.dumps({
                "title": name,
                "type": "pie",
                "aggs": [
                    {"id": "1", "enabled": True, "type": "sum", "schema": "metric", "params": {"field": "flow.bytes"}},
                    {"id": "2", "enabled": True, "type": "terms", "schema": "segment",
                     "params": {"field": bucket_field, "size": 10, "order": "desc", "orderBy": "1"}}
                ],
                "params": {
                    "type": "pie",
                    "addTooltip": True,
                    "addLegend": True,
                    "legendPosition": "right",
                    "isDonut": True
                }
            }),
            "uiStateJSON": "{}",
            "kibanaSavedObjectMeta": {
                "searchSourceJSON": json.dumps({
                    "index": INDEX_PATTERN,
                    "query": {"query": "", "language": "kuery"},
                    "filter": []
                })
            }
        }
    }
    r = api_call("POST", "/saved_objects/visualization", payload)
    if r and r.status_code in [200, 201]:
        return r.json().get('id')
    return None

def create_line_vis(name, x_field, y_field, split_field=None):
    """Create line chart visualization"""
    aggs = [
        {"id": "1", "enabled": True, "type": "sum", "schema": "metric", "params": {"field": y_field}},
        {"id": "2", "enabled": True, "type": "date_histogram", "schema": "segment",
         "params": {"field": x_field, "interval": "auto"}}
    ]
    if split_field:
        aggs.append({"id": "3", "enabled": True, "type": "terms", "schema": "group",
                    "params": {"field": split_field, "size": 3}})
    
    payload = {
        "attributes": {
            "title": name,
            "visState": json.dumps({
                "title": name,
                "type": "line",
                "aggs": aggs,
                "params": {
                    "type": "line",
                    "grid": {"categoryLines": False},
                    "categoryAxes": [{"id": "CategoryAxis-1", "type": "category", "position": "bottom", "show": True, "style": {}, "scale": {"type": "linear"}, "labels": {"show": True, "truncate": 100}}],
                    "valueAxes": [{"id": "ValueAxis-1", "name": "LeftAxis-1", "type": "value", "position": "left", "show": True}],
                    "seriesParams": [{"show": True, "mode": "normal", "type": "line", "lineWidth": 2, "valueAxis": "ValueAxis-1", "data": {"id": "1"}}],
                    "addTooltip": True,
                    "addLegend": True
                }
            }),
            "uiStateJSON": "{}",
            "kibanaSavedObjectMeta": {
                "searchSourceJSON": json.dumps({
                    "index": INDEX_PATTERN,
                    "query": {"query": "", "language": "kuery"},
                    "filter": []
                })
            }
        }
    }
    r = api_call("POST", "/saved_objects/visualization", payload)
    if r and r.status_code in [200, 201]:
        return r.json().get('id')
    return None

def create_metric_count_vis(name):
    """Create metric visualization for count"""
    payload = {
        "attributes": {
            "title": name,
            "visState": json.dumps({
                "title": name,
                "type": "metric",
                "aggs": [
                    {"id": "1", "enabled": True, "type": "count", "schema": "metric", "params": {"customLabel": "Flows"}}
                ],
                "params": {
                    "addTooltip": True,
                    "addLegend": False,
                    "type": "metric",
                    "metric": {"percentageMode": False, "useRanges": False, "colorSchema": "Green to Red",
                               "metricColorMode": "None", "labels": {"show": True},
                               "style": {"fontSize": 40, "labelFontSize": 16}}
                }
            }),
            "uiStateJSON": "{}",
            "kibanaSavedObjectMeta": {
                "searchSourceJSON": json.dumps({
                    "index": INDEX_PATTERN,
                    "query": {"query": "", "language": "kuery"},
                    "filter": []
                })
            }
        }
    }
    r = api_call("POST", "/saved_objects/visualization", payload)
    if r and r.status_code in [200, 201]:
        return r.json().get('id')
    return None

def get_existing_dashboard():
    """Get existing dashboard content"""
    r = api_call("GET", f"/saved_objects/dashboard/{DASHBOARD_ID}")
    if r and r.status_code == 200:
        return r.json()
    return None

def update_dashboard_with_panels(panel_refs):
    """Add new panels to existing dashboard"""
    dashboard = get_existing_dashboard()
    if not dashboard:
        print(f"  ✗ Could not find dashboard {DASHBOARD_ID}")
        return False
    
    attrs = dashboard.get('attributes', {})
    existing_panels = json.loads(attrs.get('panelsJSON', '[]'))
    existing_refs = dashboard.get('references', [])
    
    # Calculate starting positions
    max_y = 0
    for panel in existing_panels:
        y = panel.get('gridData', {}).get('y', 0)
        h = panel.get('gridData', {}).get('h', 0)
        max_y = max(max_y, y + h)
    
    # Add new panels in 2-column layout
    new_panels = []
    new_refs = []
    base_y = max_y + 5
    
    for i, (vis_id, name) in enumerate(panel_refs):
        panel_id = f"new_{i}"
        col = i % 2
        row = i // 2
        
        panel = {
            "panelIndex": panel_id,
            "version": "9.2.4",
            "type": "visualization",
            "gridData": {
                "x": col * 24,
                "y": base_y + (row * 20),
                "w": 24,
                "h": 20,
                "i": panel_id
            },
            "panelRefName": f"panel_{panel_id}",
            "embeddableConfig": {"enhancements": {}}
        }
        new_panels.append(panel)
        new_refs.append({
            "id": vis_id,
            "type": "visualization",
            "name": f"panel_{panel_id}"
        })
    
    # Merge panels
    combined_panels = existing_panels + new_panels
    combined_refs = existing_refs + new_refs
    
    # Update dashboard
    payload = {
        "attributes": {
            "title": attrs.get('title', 'Updated Dashboard'),
            "description": attrs.get('description', '') + " | Enhanced with device filtering",
            "hits": attrs.get('hits', 0),
            "panelsJSON": json.dumps(combined_panels),
            "optionsJSON": attrs.get('optionsJSON', '{}'),
            "version": attrs.get('version', 1) + 1,
            "timeRestore": attrs.get('timeRestore', False),
            "kibanaSavedObjectMeta": attrs.get('kibanaSavedObjectMeta', {})
        },
        "references": combined_refs
    }
    
    r = api_call("PUT", f"/saved_objects/dashboard/{DASHBOARD_ID}", payload)
    if r and r.status_code in [200, 201]:
        print(f"  ✓ Dashboard updated with {len(new_panels)} new panels")
        return True
    else:
        print(f"  ✗ Failed to update dashboard: {r.status_code if r else 'No response'}")
        return False

# ============================================================================
# MAIN EXECUTION
# ============================================================================

print("="*70)
print("Creating 8 New Visualizations for Enhanced Dashboard")
print(f"Dashboard ID: {DASHBOARD_ID}")
print("="*70)

print("\n[1/8] Creating Device Filter Control...")
vid = create_control_vis("Device Filter - Exporter IP", "flow.export.ip.addr")
results['device-filter-control'] = vid
print(f"  {'✓' if vid else '✗'} ID: {vid or 'FAILED'}")

print("\n[2/8] Creating Top Source Ports...")
vid = create_table_vis("Top Source Ports", "flow.src.port")
results['top-source-ports'] = vid
print(f"  {'✓' if vid else '✗'} ID: {vid or 'FAILED'}")

print("\n[3/8] Creating Top Destination Ports...")
vid = create_table_vis("Top Destination Ports", "flow.dst.port")
results['top-dest-ports'] = vid
print(f"  {'✓' if vid else '✗'} ID: {vid or 'FAILED'}")

print("\n[4/8] Creating Traffic by Hour of Day...")
vid = create_bar_vis("Traffic by Hour of Day", "@timestamp", "_index")
results['traffic-by-hour'] = vid
print(f"  {'✓' if vid else '✗'} ID: {vid or 'FAILED'}")

print("\n[5/8] Creating Top Exporters (Devices)...")
vid = create_table_vis("Top Flow Exporters", "flow.export.ip.addr")
results['top-exporters'] = vid
print(f"  {'✓' if vid else '✗'} ID: {vid or 'FAILED'}")

print("\n[6/8] Creating Bytes In vs Out...")
vid = create_line_vis("Bytes In vs Out", "@timestamp", "flow.bytes", "flow.direction.name")
results['bytes-in-out'] = vid
print(f"  {'✓' if vid else '✗'} ID: {vid or 'FAILED'}")

# Map visualization - use pie as fallback (map needs special setup)
print("\n[7/8] Creating Geographic Traffic Map...")
vid = create_pie_vis("Traffic by Source Country", "flow.src.geo.country_name.keyword")
results['geo-traffic-map'] = vid
print(f"  {'✓' if vid else '✗'} ID: {vid or 'FAILED'}")
print("  Note: Changed to pie chart - Maps require geo_point field and special setup")

print("\n[8/8] Creating Flow Count Over Time...")
vid = create_metric_count_vis("Flow Count Over Time")
results['flow-count-over-time'] = vid
print(f"  {'✓' if vid else '✗'} ID: {vid or 'FAILED'}")

# Update dashboard
print("\n" + "="*70)
print("Updating Dashboard with New Visualization Panels")
print("="*70)

successful = [(v, n) for n, v in results.items() if v]
if successful:
    update_dashboard_with_panels(successful)
else:
    print("  ✗ No successful visualizations to add")

# Final summary
print("\n" + "="*70)
print("CREATION RESULTS SUMMARY")
print("="*70)
for name, vid in results.items():
    status = "✓ CREATED" if vid else "✗ FAILED"
    print(f"  {status} - {name}: {vid or 'N/A'}")

print(f"\n{'='*70}")
print("DASHBOARD URL:")
print(f"{KIBANA_URL}/app/dashboards#/view/{DASHBOARD_ID}")
print("="*70)

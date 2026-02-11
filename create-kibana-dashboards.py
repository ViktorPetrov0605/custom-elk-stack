#!/usr/bin/env python3
"""
Kibana Dashboard Automation Script
Uses REST APIs to create index patterns, visualizations, and dashboards
"""
import requests
import json
import sys
from urllib3.exceptions import InsecureRequestWarning

# Disable SSL warnings
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

KIBANA_URL = "https://10.4.4.87:5601"
AUTH = ("elastic", "telehouse")
HEADERS = {
    "Content-Type": "application/json",
    "kbn-xsrf": "true"
}

def create_index_pattern():
    """Create unified-flow-* index pattern"""
    url = f"{KIBANA_URL}/api/saved_objects/index-pattern"
    data = {
        "attributes": {
            "title": "unified-flow-*",
            "timeFieldName": "@timestamp"
        }
    }
    
    try:
        resp = requests.post(url, headers=HEADERS, auth=AUTH, 
                           json=data, verify=False, timeout=30)
        if resp.status_code in [200, 201]:
            print(f"✓ Index pattern created: {resp.json().get('id')}")
            return resp.json().get('id')
        else:
            print(f"✗ Index pattern failed: {resp.status_code} - {resp.text[:100]}")
            return None
    except Exception as e:
        print(f"✗ Error: {e}")
        return None

def create_visualization(title, vis_type, index_pattern_id, metric_field, bucket_field):
    """Create a visualization via Lens API"""
    url = f"{KIBANA_URL}/api/saved_objects/visualization"
    
    # Build visState based on type
    if vis_type == "area":
        vis_state = {
            "title": title,
            "type": "area",
            "aggs": [
                {"id": "1", "enabled": True, "type": "sum", "schema": "metric", 
                 "params": {"field": metric_field}},
                {"id": "2", "enabled": True, "type": "date_histogram", "schema": "segment",
                 "params": {"field": "@timestamp", "interval": "auto"}}
            ]
        }
    elif vis_type == "pie":
        vis_state = {
            "title": title,
            "type": "pie",
            "aggs": [
                {"id": "1", "enabled": True, "type": "sum", "schema": "metric",
                 "params": {"field": metric_field}},
                {"id": "2", "enabled": True, "type": "terms", "schema": "segment",
                 "params": {"field": bucket_field, "size": 10}}
            ]
        }
    else:  # histogram/bar
        vis_state = {
            "title": title,
            "type": "histogram",
            "aggs": [
                {"id": "1", "enabled": True, "type": "sum", "schema": "metric",
                 "params": {"field": metric_field}},
                {"id": "2", "enabled": True, "type": "terms", "schema": "group",
                 "params": {"field": bucket_field, "size": 10}}
            ]
        }
    
    data = {
        "attributes": {
            "title": title,
            "visState": json.dumps(vis_state),
            "kibanaSavedObjectMeta": {
                "searchSourceJSON": json.dumps({"index": index_pattern_id})
            }
        },
        "references": [
            {"id": index_pattern_id, "name": "kibanaSavedObjectMeta.searchSourceJSON.index", 
             "type": "index-pattern"}
        ]
    }
    
    try:
        resp = requests.post(url, headers=HEADERS, auth=AUTH,
                           json=data, verify=False, timeout=30)
        if resp.status_code in [200, 201]:
            print(f"✓ Visualization created: {title}")
            return resp.json().get('id')
        else:
            print(f"✗ Visualization failed: {resp.status_code}")
            return None
    except Exception as e:
        print(f"✗ Error: {e}")
        return None

def create_dashboard(title, viz_ids, index_pattern_id):
    """Create dashboard with visualizations"""
    url = f"{KIBANA_URL}/api/saved_objects/dashboard"
    
    panels = []
    for i, viz_id in enumerate(viz_ids):
        panels.append({
            "id": viz_id,
            "type": "visualization",
            "panelIndex": str(i+1),
            "gridData": {"x": (i%2)*24, "y": (i//2)*15, "w": 24, "h": 15},
            "version": "9.2.4"
        })
    
    data = {
        "attributes": {
            "title": title,
            "hits": 0,
            "description": "Network Flow Analytics Dashboard",
            "panelsJSON": json.dumps(panels),
            "optionsJSON": json.dumps({"useMargins": True, "syncColors": False}),
            "version": 1,
            "timeRestore": True,
            "timeFrom": "now-15m",
            "timeTo": "now"
        },
        "references": [
            {"id": index_pattern_id, "name": "kibanaSavedObjectMeta.searchSourceJSON.index",
             "type": "index-pattern"}
        ] + [{"id": vid, "name": f"panel_{i+1}", "type": "visualization"} 
             for i, vid in enumerate(viz_ids)]
    }
    
    try:
        resp = requests.post(url, headers=HEADERS, auth=AUTH,
                           json=data, verify=False, timeout=30)
        if resp.status_code in [200, 201]:
            print(f"✓ Dashboard created: {title}")
            return resp.json().get('id')
        else:
            print(f"✗ Dashboard failed: {resp.status_code} - {resp.text[:200]}")
            return None
    except Exception as e:
        print(f"✗ Error: {e}")
        return None

def main():
    print("="*60)
    print("Kibana Dashboard Automation")
    print("="*60)
    print(f"Target: {KIBANA_URL}")
    print()
    
    # Step 1: Create index pattern
    print("Step 1: Creating index pattern...")
    index_id = create_index_pattern()
    if not index_id:
        print("Failed to create index pattern. Exiting.")
        return 1
    
    # Step 2: Create visualizations
    print("\nStep 2: Creating visualizations...")
    viz_ids = []
    
    viz_configs = [
        ("Traffic Volume Over Time", "area", "network.bytes", "@timestamp"),
        ("Top Source IPs", "pie", "network.bytes", "source.ip"),
        ("Protocol Distribution", "pie", "network.bytes", "network.transport"),
        ("Top Source AS", "histogram", "network.bytes", "source.as.number"),
        ("Top Destination AS", "histogram", "network.bytes", "destination.as.number"),
        ("Interface Traffic", "histogram", "network.bytes", "interface.input"),
    ]
    
    for title, vtype, metric, bucket in viz_configs:
        vid = create_visualization(title, vtype, index_id, metric, bucket)
        if vid:
            viz_ids.append(vid)
    
    if len(viz_ids) < 3:
        print("Not enough visualizations created. Exiting.")
        return 1
    
    # Step 3: Create dashboard
    print("\nStep 3: Creating dashboard...")
    dashboard_id = create_dashboard("Network Flow Analytics", viz_ids, index_id)
    
    if dashboard_id:
        print(f"\n✓ Success! Dashboard ID: {dashboard_id}")
        print(f"\nAccess at: {KIBANA_URL}/app/dashboards#/view/{dashboard_id}")
        return 0
    else:
        print("\n✗ Dashboard creation failed")
        return 1

if __name__ == "__main__":
    sys.exit(main())
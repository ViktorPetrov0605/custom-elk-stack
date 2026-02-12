#!/usr/bin/env python3
"""Fix device.name -> host.ip in Kibana dashboards"""
import json
import requests
import sys

# Config
KIBANA_URL = "http://10.4.4.87:5601"
AUTH = ("elastic", "telehouse")
HEADERS = {"kbn-xsrf": "true"}

DASHBOARDS = [
    "unified-flow-detailed-v2",
    "unified-flow-topn-v2", 
    "unified-flow-conversations-v2"
]

def fix_dashboard(dashboard_id):
    """Fetch, fix and update a dashboard"""
    url = f"{KIBANA_URL}/api/saved_objects/dashboard/{dashboard_id}"
    
    # Fetch
    resp = requests.get(url, auth=AUTH)
    if resp.status_code != 200:
        print(f"❌ Failed to fetch {dashboard_id}: {resp.status_code}")
        return False
    
    data = resp.json()
    attrs = data.get("attributes", {})
    panels_json = attrs.get("panelsJSON", "[]")
    
    # Parse and fix
    try:
        panels = json.loads(panels_json)
    except:
        print(f"❌ Failed to parse panelsJSON for {dashboard_id}")
        return False
    
    fixed_count = 0
    for panel in panels:
        embeddable = panel.get("embeddableConfig", {})
        state = embeddable.get("attributes", {}).get("state", {})
        form_based = state.get("datasourceStates", {}).get("formBased", {})
        
        for layer_id, layer in form_based.get("layers", {}).items():
            for col_id, col in layer.get("columns", {}).items():
                source_field = col.get("sourceField", "")
                if source_field == "device.name":
                    col["sourceField"] = "host.ip"
                    col["dataType"] = "ip"
                    fixed_count += 1
                    print(f"  ✅ Fixed panel '{panel.get('title', 'Untitled')}' column '{col_id}'")
    
    if fixed_count == 0:
        print(f"  ℹ️ No device.name references found in {dashboard_id}")
        return True
    
    # Update back
    attrs["panelsJSON"] = json.dumps(panels)
    update_resp = requests.put(url, 
                                auth=AUTH, 
                                headers=HEADERS,
                                json={"attributes": attrs})
    
    if update_resp.status_code in [200, 201]:
        print(f"✅ Fixed {fixed_count} fields in {dashboard_id}")
        return True
    else:
        print(f"❌ Failed to update {dashboard_id}: {update_resp.status_code}")
        print(f"   {update_resp.text[:200]}")
        return False

if __name__ == "__main__":
    print("=== Fixing Dashboards (device.name -> host.ip) ===\n")
    
    results = {}
    for dash_id in DASHBOARDS:
        print(f"\nDashboard: {dash_id}")
        results[dash_id] = fix_dashboard(dash_id)
    
    print("\n=== Summary ===")
    for dash_id, success in results.items():
        status = "✅" if success else "❌"
        print(f"{status} {dash_id}")
    
    sys.exit(0)

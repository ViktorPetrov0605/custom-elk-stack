#!/usr/bin/env python3
"""Fix index pattern references in dashboards"""
import json
import requests
import sys

KIBANA_URL = "http://10.4.4.87:5601"
AUTH = ("elastic", "telehouse")
HEADERS = {"kbn-xsrf": "true"}

NEW_INDEX_PATTERN_ID = "cc96ae84-f35b-49a8-8945-a55cd69daea7"
DASHBOARDS = [
    "unified-flow-detailed-v2",
    "unified-flow-topn-v2", 
    "unified-flow-conversations-v2"
]

def fix_dashboard_ref(dashboard_id):
    """Update index pattern references"""
    url = f"{KIBANA_URL}/api/saved_objects/dashboard/{dashboard_id}"
    
    resp = requests.get(url, auth=AUTH)
    if resp.status_code != 200:
        print(f"❌ Failed to fetch {dashboard_id}: {resp.status_code}")
        return False
    
    data = resp.json()
    attrs = data.get("attributes", {})
    
    # Fix references
    refs = data.get("references", [])
    for ref in refs:
        if ref.get("type") == "index-pattern":
            old_id = ref.get("id", "")
            ref["id"] = NEW_INDEX_PATTERN_ID
            print(f"  ✅ Updated ref: {old_id} -> {NEW_INDEX_PATTERN_ID}")
    
    # Fix panelsJSON references too
    panels_json = attrs.get("panelsJSON", "[]")
    try:
        panels = json.loads(panels_json)
        for panel in panels:
            embeddable = panel.get("embeddableConfig", {})
            attributes = embeddable.get("attributes", {})
            refs_list = attributes.get("references", [])
            for ref in refs_list:
                if ref.get("type") == "index-pattern":
                    ref["id"] = NEW_INDEX_PATTERN_ID
    except:
        print(f"  ⚠️ Failed to parse panelsJSON")
    
    attrs["panelsJSON"] = json.dumps(panels)
    
    # Update
    update_resp = requests.put(url, auth=AUTH, headers=HEADERS,
                                json={"attributes": attrs, "references": refs})
    
    if update_resp.status_code in [200, 201]:
        print(f"✅ Updated {dashboard_id}")
        return True
    else:
        print(f"❌ Failed to update {dashboard_id}: {update_resp.status_code}")
        return False

if __name__ == "__main__":
    print("=== Updating Dashboard Index Pattern References ===\n")
    
    for dash_id in DASHBOARDS:
        print(f"\nDashboard: {dash_id}")
        fix_dashboard_ref(dash_id)

print("\nDone - Refresh Kibana (F5) to see changes")

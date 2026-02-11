#!/usr/bin/env python3
"""
Script to update Kibana dashboard with Source-Destination pair visualizations
"""

import json
import sys

# Read the current dashboard
with open('/tmp/dashboard_current.json', 'r') as f:
    dashboard = json.load(f)

# Parse the current panels
panels_json = dashboard['attributes']['panelsJSON']
panels = json.loads(panels_json)

# Update panel positions to make room for new panels at row 15
# Shift all panels below y=15 down by 18 rows to accommodate new panels
for panel in panels:
    y = panel['gridData']['y']
    if y >= 15:
        panel['gridData']['y'] = y + 18

# Add new Source IPs bar chart panel (left side)
source_panel = {
    "embeddableConfig": {
        "enhancements": {},
        "savedObjectId": "src-dst-sources-viz",
        "savedObjectType": "lens"
    },
    "gridData": {
        "h": 18,
        "i": "12",
        "w": 24,
        "x": 0,
        "y": 15
    },
    "panelIndex": "12",
    "title": "Top 10 Source IPs (Bar Chart)",
    "type": "lens",
    "version": "8.9.0"
}

# Add new Destination IPs bar chart panel (right side)
dest_panel = {
    "embeddableConfig": {
        "enhancements": {},
        "savedObjectId": "src-dst-dests-viz",
        "savedObjectType": "lens"
    },
    "gridData": {
        "h": 18,
        "i": "13",
        "w": 24,
        "x": 24,
        "y": 15
    },
    "panelIndex": "13",
    "title": "Top 10 Destination IPs (Bar Chart)",
    "type": "lens",
    "version": "8.9.0"
}

# Insert the new panels
panels.insert(2, source_panel)  # After first 2 panels
panels.insert(3, dest_panel)   # After source panel

# Re-index panel indices
for idx, panel in enumerate(panels):
    panel['panelIndex'] = str(idx + 1)
    panel['gridData']['i'] = str(idx + 1)

# Update the panelsJSON
dashboard['attributes']['panelsJSON'] = json.dumps(panels)

# Add references to the new lens visualizations
references = dashboard.get('references', [])
references.append({
    "id": "src-dst-sources-viz",
    "name": "1:panel_12",
    "type": "lens"
})
references.append({
    "id": "src-dst-dests-viz",
    "name": "2:panel_13",
    "type": "lens"
})
dashboard['references'] = references

# Remove internal Kibana fields that shouldn't be sent in update
for key in ['id', 'type', 'namespaces', 'migrationVersion', 'updated_at', 
            'created_at', 'version', 'managed', 'coreMigrationVersion', 
            'typeMigrationVersion', 'score']:
    if key in dashboard:
        del dashboard[key]

# Save the updated dashboard
with open('/tmp/dashboard_updated.json', 'w') as f:
    json.dump(dashboard, f, indent=2)

print("Dashboard updated successfully!")
print(f"Total panels: {len(panels)}")

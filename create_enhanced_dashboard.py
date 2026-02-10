#!/usr/bin/env python3
"""
Enhanced Unified Dashboard with Device Filtering
Creates all visualizations and dashboard for ElastiFlow using Kibana API
"""

import requests
import json
import uuid
import urllib3
from datetime import datetime

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Kibana configuration
KIBANA_URL = "http://10.4.4.87:5601"
AUTH = ("elastic", "telehouse")
HEADERS = {
    "Content-Type": "application/json",
    "kbn-xsrf": "true"
}

# Index pattern
INDEX_PATTERN = "elastiflow-flow"

class KibanaObjectCreator:
    def __init__(self):
        self.base_url = KIBANA_URL
        self.auth = AUTH
        self.created_objects = []
        
    def make_request(self, method, endpoint, data=None):
        url = f"{self.base_url}/api{endpoint}"
        try:
            if method == "GET":
                response = requests.get(url, auth=self.auth, headers=HEADERS, verify=False, timeout=30)
            elif method == "POST":
                response = requests.post(url, json=data, auth=self.auth, headers=HEADERS, verify=False, timeout=30)
            elif method == "PUT":
                response = requests.put(url, json=data, auth=self.auth, headers=HEADERS, verify=False, timeout=30)
            else:
                raise ValueError(f"Unsupported method: {method}")
            
            return response
        except Exception as e:
            print(f"  ERROR: {e}")
            return None
    
    def create_control_vis(self, id_suffix, name, field, index_pattern_id):
        """Create an input control (list) visualization"""
        vis_id = f"elastiflow-{id_suffix}-{uuid.uuid4().hex[:8]}"
        
        vis_data = {
            "attributes": {
                "title": name,
                "visState": json.dumps({
                    "title": name,
                    "type": "input_control_vis",
                    "params": {
                        "controls": [
                            {
                                "id": f"device_filter_{uuid.uuid4().hex[:6]}",
                                "fieldName": field,
                                "parent": "",
                                "label": "Select Device (Flow Exporter)",
                                "type": "list",
                                "options": {
                                    "type": "terms",
                                    "multiselect": True,
                                    "dynamicOptions": True,
                                    "size": 50,
                                    "order": "desc"
                                },
                                "indexPattern": index_pattern_id
                            }
                        ],
                        "updateFiltersOnChange": False,
                        "useTimeFilter": True,
                        "pinFilters": False
                    },
                    "aggs": []
                }),
                "uiStateJSON": "{}",
                "description": "",
                "kibanaSavedObjectMeta": {
                    "searchSourceJSON": json.dumps({
                        "query": {"query": "", "language": "kuery"},
                        "filter": []
                    })
                }
            }
        }
        
        response = self.make_request("POST", "/saved_objects/visualization", vis_data)
        if response and response.status_code in [200, 201]:
            result = response.json()
            print(f"  ✓ Created: {name} (ID: {result.get('id', vis_id)})")
            return result.get('id', vis_id)
        else:
            print(f"  ✗ Failed to create {name}: {response.status_code if response else 'No response'}")
            if response:
                print(f"    Error: {response.text[:200]}")
            return None
    
    def create_table_vis(self, id_suffix, name, bucket_field, metric_field="flow.bytes", bucket_label=None, index_pattern_id=None):
        """Create a data table visualization"""
        vis_id = f"elastiflow-{id_suffix}-{uuid.uuid4().hex[:8]}"
        bucket_label = bucket_label or bucket_field.split('.')[-1].replace('_', ' ').title()
        
        vis_data = {
            "attributes": {
                "title": name,
                "visState": json.dumps({
                    "title": name,
                    "type": "table",
                    "aggs": [
                        {"id": "1", "enabled": True, "type": "sum", "schema": "metric", "params": {"field": metric_field, "customLabel": "Bytes"}},
                        {"id": "2", "enabled": True, "type": "terms", "schema": "bucket", 
                         "params": {"field": bucket_field, "size": 10, "order": "desc", "orderBy": "1", 
                                   "customLabel": bucket_label}}
                    ],
                    "params": {
                        "perPage": 10,
                        "showMeticsAtAllLevels": False,
                        "showPartialRows": False,
                        "showToolbar": True,
                        "showTotal": False,
                        "totalFunc": "sum"
                    }
                }),
                "uiStateJSON": json.dumps({"vis": {"params": {"sort": {"columnIndex": 1, "direction": "desc"}}}}),
                "description": "",
                "kibanaSavedObjectMeta": {
                    "searchSourceJSON": json.dumps({
                        "index": index_pattern_id,
                        "query": {"query": "", "language": "kuery"},
                        "filter": []
                    })
                }
            }
        }
        
        response = self.make_request("POST", "/saved_objects/visualization", vis_data)
        if response and response.status_code in [200, 201]:
            result = response.json()
            print(f"  ✓ Created: {name} (ID: {result.get('id', vis_id)})")
            return result.get('id', vis_id)
        else:
            print(f"  ✗ Failed to create {name}: {response.status_code if response else 'No response'}")
            if response:
                print(f"    Error: {response.text[:200]}")
            return None
    
    def create_pie_vis(self, id_suffix, name, bucket_field, metric_field="flow.bytes", index_pattern_id=None):
        """Create a pie chart visualization"""
        vis_id = f"elastiflow-{id_suffix}-{uuid.uuid4().hex[:8]}"
        
        vis_data = {
            "attributes": {
                "title": name,
                "visState": json.dumps({
                    "title": name,
                    "type": "pie",
                    "aggs": [
                        {"id": "1", "enabled": True, "type": "sum", "schema": "metric", "params": {"field": metric_field}},
                        {"id": "2", "enabled": True, "type": "terms", "schema": "segment", 
                         "params": {"field": bucket_field, "size": 10, "order": "desc", "orderBy": "1"}}
                    ],
                    "params": {
                        "type": "pie",
                        "addTooltip": True,
                        "addLegend": True,
                        "legendPosition": "right",
                        "isDonut": True,
                        "labels": {"show": False, "values": True, "last_level": True, "truncate": 100}
                    }
                }),
                "uiStateJSON": "{}",
                "description": "",
                "kibanaSavedObjectMeta": {
                    "searchSourceJSON": json.dumps({
                        "index": index_pattern_id,
                        "query": {"query": "", "language": "kuery"},
                        "filter": []
                    })
                }
            }
        }
        
        response = self.make_request("POST", "/saved_objects/visualization", vis_data)
        if response and response.status_code in [200, 201]:
            result = response.json()
            print(f"  ✓ Created: {name} (ID: {result.get('id', vis_id)})")
            return result.get('id', vis_id)
        else:
            print(f"  ✗ Failed to create {name}: {response.status_code if response else 'No response'}")
            return None
    
    def create_area_vis(self, id_suffix, name, x_field="@timestamp", y_field="flow.bytes", split_field=None, mode="area", index_pattern_id=None):
        """Create an area or line chart visualization"""
        vis_id = f"elastiflow-{id_suffix}-{uuid.uuid4().hex[:8]}"
        
        aggs = [
            {"id": "1", "enabled": True, "type": "sum", "schema": "metric", "params": {"field": y_field}},
            {"id": "2", "enabled": True, "type": "date_histogram", "schema": "segment", 
             "params": {"field": x_field, "interval": "auto", "min_doc_count": 1}}
        ]
        
        if split_field:
            aggs.append({"id": "3", "enabled": True, "type": "terms", "schema": "group", 
                        "params": {"field": split_field, "size": 5, "order": "desc", "orderBy": "1"}})
        
        vis_data = {
            "attributes": {
                "title": name,
                "visState": json.dumps({
                    "title": name,
                    "type": mode,
                    "aggs": aggs,
                    "params": {
                        "type": mode,
                        "grid": {"categoryLines": False},
                        "categoryAxes": [{"id": "CategoryAxis-1", "type": "category", "position": "bottom", 
                                          "show": True, "style": {}, "scale": {"type": "linear"}, 
                                          "labels": {"show": True, "truncate": 100}, "title": {}}],
                        "valueAxes": [{"id": "ValueAxis-1", "name": "LeftAxis-1", "type": "value", "position": "left", 
                                       "show": True, "style": {}, "scale": {"type": "linear", "mode": "normal"}, 
                                       "labels": {"show": True, "rotate": 0, "filter": False, "truncate": 100}, 
                                       "title": {"text": "Bytes"}}],
                        "seriesParams": [{"show": True, "mode": "stacked", "type": mode, 
                                         "drawLinesBetweenPoints": True, "showCircles": True, 
                                         "interpolate": "linear", "lineWidth": 2, 
                                         "valueAxis": "ValueAxis-1", "data": {"id": "1", "label": "Sum of Bytes"}}],
                        "addTooltip": True,
                        "addLegend": True,
                        "legendPosition": "right",
                        "times": [],
                        "addTimeMarker": False
                    }
                }),
                "uiStateJSON": "{}",
                "description": "",
                "kibanaSavedObjectMeta": {
                    "searchSourceJSON": json.dumps({
                        "index": index_pattern_id,
                        "query": {"query": "", "language": "kuery"},
                        "filter": []
                    })
                }
            }
        }
        
        response = self.make_request("POST", "/saved_objects/visualization", vis_data)
        if response and response.status_code in [200, 201]:
            result = response.json()
            print(f"  ✓ Created: {name} (ID: {result.get('id', vis_id)})")
            return result.get('id', vis_id)
        else:
            print(f"  ✗ Failed to create {name}: {response.status_code if response else 'No response'}")
            return None
    
    def create_metric_vis(self, id_suffix, name, metric_field, index_pattern_id=None):
        """Create a metric/number visualization"""
        vis_id = f"elastiflow-{id_suffix}-{uuid.uuid4().hex[:8]}"
        
        vis_data = {
            "attributes": {
                "title": name,
                "visState": json.dumps({
                    "title": name,
                    "type": "metric",
                    "aggs": [
                        {"id": "1", "enabled": True, "type": "count" if metric_field == "_index" else "sum", 
                         "schema": "metric", "params": {"field": metric_field, "customLabel": "Count" if metric_field == "_index" else "Bytes"}}
                    ],
                    "params": {
                        "addTooltip": True,
                        "addLegend": False,
                        "type": "metric",
                        "metric": {
                            "percentageMode": False,
                            "useRanges": False,
                            "colorSchema": "Green to Red",
                            "metricColorMode": "None",
                            "colorsRange": [{"from": 0, "to": 10000}],
                            "labels": {"show": True},
                            "style": {"bgColor": False, "bgFill": "#000", "fontSize": 60, "labelColor": False, "labelFontSize": 20, "subText": "", "width": "medium"}
                        }
                    }
                }),
                "uiStateJSON": "{}",
                "description": "",
                "kibanaSavedObjectMeta": {
                    "searchSourceJSON": json.dumps({
                        "index": index_pattern_id,
                        "query": {"query": "", "language": "kuery"},
                        "filter": []
                    })
                }
            }
        }
        
        response = self.make_request("POST", "/saved_objects/visualization", vis_data)
        if response and response.status_code in [200, 201]:
            result = response.json()
            print(f"  ✓ Created: {name} (ID: {result.get('id', vis_id)})")
            return result.get('id', vis_id)
        else:
            print(f"  ✗ Failed to create {name}: {response.status_code if response else 'No response'}")
            return None
    
    def create_date_histogram_vis(self, id_suffix, name, date_field="@timestamp", metric_type="count", index_pattern_id=None):
        """Create a date histogram visualization"""
        vis_id = f"elastiflow-{id_suffix}-{uuid.uuid4().hex[:8]}"
        
        aggs = [
            {"id": "1", "enabled": True, "type": metric_type, "schema": "metric", "params": {"customLabel": "Count"}},
            {"id": "2", "enabled": True, "type": "date_histogram", "schema": "segment", 
             "params": {"field": date_field, "calendar_interval": "1h", "min_doc_count": 1, "customLabel": "Hour of Day"}}
        ]
        
        vis_data = {
            "attributes": {
                "title": name,
                "visState": json.dumps({
                    "title": name,
                    "type": "histogram",
                    "aggs": aggs,
                    "params": {
                        "type": "histogram",
                        "grid": {"categoryLines": False},
                        "categoryAxes": [{"id": "CategoryAxis-1", "type": "category", "position": "bottom", 
                                          "show": True, "style": {}, "scale": {"type": "linear"}, 
                                          "labels": {"show": True, "truncate": 100}, "title": {}}],
                        "valueAxes": [{"id": "ValueAxis-1", "name": "LeftAxis-1", "type": "value", "position": "left", 
                                       "show": True, "style": {}, "scale": {"type": "linear", "mode": "normal"}, 
                                       "labels": {"show": True, "rotate": 0, "filter": False, "truncate": 100}}],
                        "seriesParams": [{"show": "true", "type": "histogram", "mode": "stacked", 
                                         "data": {"label": "Count", "id": "1"}, 
                                         "valueAxis": "ValueAxis-1", "drawLinesBetweenPoints": True, 
                                         "showCircles": True, "lineWidth": 2}],
                        "addTooltip": True,
                        "addLegend": False,
                        "legendPosition": "right",
                        "times": [],
                        "addTimeMarker": False
                    }
                }),
                "uiStateJSON": "{}",
                "description": "",
                "kibanaSavedObjectMeta": {
                    "searchSourceJSON": json.dumps({
                        "index": index_pattern_id,
                        "query": {"query": "", "language": "kuery"},
                        "filter": []
                    })
                }
            }
        }
        
        response = self.make_request("POST", "/saved_objects/visualization", vis_data)
        if response and response.status_code in [200, 201]:
            result = response.json()
            print(f"  ✓ Created: {name} (ID: {result.get('id', vis_id)})")
            return result.get('id', vis_id)
        else:
            print(f"  ✗ Failed to create {name}: {response.status_code if response else 'No response'}")
            return None
    
    def find_or_create_index_pattern(self):
        """Find the ElastiFlow index pattern"""
        print("\n[1/4] Checking for ElastiFlow index pattern...")
        
        # Try to get existing index patterns
        response = self.make_request("GET", "/saved_objects/_find?type=index-pattern&per_page=100")
        if response and response.status_code == 200:
            data = response.json()
            for obj in data.get('saved_objects', []):
                title = obj.get('attributes', {}).get('title', '')
                if 'elastiflow' in title.lower() or 'flow' in title.lower():
                    print(f"  ✓ Found index pattern: {obj['id']} ({title})")
                    return obj['id']
        
        # If not found, try a common ID
        print("  ! Using default index pattern ID: elastiflow-flow-*")
        return "elastiflow-flow-*"
    
    def create_dashboard(self, title, panels, control_vis_id=None):
        """Create a dashboard with panels"""
        print(f"\n[4/4] Creating Dashboard: {title}...")
        
        # Build panels JSON with proper references
        references = []
        dashboard_panels = []
        
        for i, panel in enumerate(panels):
            panel_id = f"panel_{i}"
            
            # Determine grid data based on position
            # Layout: 2 columns, device filter spans full width at top
            
            if panel.get('full_width', False):
                grid_x = 0
                grid_y = panel.get('y', 0) * 15
                grid_w = 48  # Full width
                grid_h = 15 if panel.get('type') == 'control' else 20
            else:
                # 2-column layout
                col = panel.get('col', 0) % 2
                row = panel.get('y', 0)
                grid_x = col * 24  # Each column is 24 units
                grid_y = row * 20
                grid_w = 24
                grid_h = 20
            
            if panel.get('vis_id'):
                panel_obj = {
                    "panelIndex": panel_id,
                    "version": "9.2.4",
                    "type": "visualization",
                    "gridData": {"x": grid_x, "y": grid_y, "w": grid_w, "h": grid_h, "i": panel_id},
                    "panelRefName": f"panel_{panel_id}",
                    "embeddableConfig": {
                        "enhancements": {}
                    }
                }
                references.append({
                    "id": panel['vis_id'],
                    "type": "visualization",
                    "name": f"panel_{panel_id}"
                })
                dashboard_panels.append(panel_obj)
        
        dashboard_data = {
            "attributes": {
                "title": title,
                "hits": 0,
                "description": f"Enhanced Unified Dashboard with Device Filtering - Created {datetime.now().strftime('%Y-%m-%d %H:%M')}",
                "panelsJSON": json.dumps(dashboard_panels),
                "optionsJSON": json.dumps({"useMargins": True, "syncColors": False, "hidePanelTitles": False}),
                "version": 1,
                "timeRestore": False,
                "kibanaSavedObjectMeta": {
                    "searchSourceJSON": json.dumps({"query": {"query": "", "language": "kuery"}, "filter": []})
                }
            },
            "references": references
        }
        
        response = self.make_request("POST", "/saved_objects/dashboard", dashboard_data)
        if response and response.status_code in [200, 201]:
            result = response.json()
            dash_id = result.get('id')
            print(f"  ✓ Dashboard created: {dash_id}")
            return dash_id
        else:
            print(f"  ✗ Failed to create dashboard: {response.status_code if response else 'No response'}")
            if response:
                print(f"    Error: {response.text[:300]}")
            return None
    
    def run(self):
        """Main execution - create all visualizations and dashboard"""
        print("="*70)
        print("Enhanced Unified Dashboard with Device Filtering - Kibana Creator")
        print("="*70)
        
        # Step 1: Find index pattern
        index_pattern_id = self.find_or_create_index_pattern()
        
        # Step 2: Create visualizations
        print("\n[2/4] Creating Visualizations...")
        
        visualizations = {}
        
        # Task 1: Device Filter Control
        print("\n  --- Device Filter Control ---")
        visualizations['device_filter'] = self.create_control_vis(
            "device-filter", 
            "Device Filter - Flow Exporter", 
            "flow.export.ip.addr",
            index_pattern_id
        )
        
        # Task 2: Additional Visualizations
        print("\n  --- Port Analysis ---")
        # 1. Top Source Ports
        visualizations['top_src_ports'] = self.create_table_vis(
            "top-src-ports", 
            "Top Source Ports", 
            "flow.src.port",
            "flow.bytes",
            "Source Port",
            index_pattern_id
        )
        
        # 2. Top Destination Ports
        visualizations['top_dst_ports'] = self.create_table_vis(
            "top-dst-ports", 
            "Top Destination Ports", 
            "flow.dst.port",
            "flow.bytes",
            "Destination Port",
            index_pattern_id
        )
        
        print("\n  --- Geographic Analysis ---")
        # 3. Top Source Countries
        visualizations['top_src_countries'] = self.create_table_vis(
            "top-src-countries", 
            "Top Source Countries", 
            "flow.src.geo.country_name",
            "flow.bytes",
            "Source Country",
            index_pattern_id
        )
        
        print("\n  --- Traffic Patterns ---")
        # 4. Traffic by Hour of Day
        visualizations['traffic_by_hour'] = self.create_date_histogram_vis(
            "traffic-by-hour",
            "Traffic by Hour of Day",
            "@timestamp",
            "count",
            index_pattern_id
        )
        
        # 5. Top Applications (L4 Protocol)
        visualizations['top_applications'] = self.create_pie_vis(
            "top-applications",
            "Top Applications (L4 Protocol)",
            "l4.proto.name",
            "flow.bytes",
            index_pattern_id
        )
        
        # 6. Bytes In vs Out
        visualizations['bytes_in_out'] = self.create_area_vis(
            "bytes-in-out",
            "Bytes In vs Out",
            "@timestamp",
            "flow.bytes",
            "flow.direction.name",
            "line",
            index_pattern_id
        )
        
        # 7. Flow Count Over Time
        visualizations['flow_count'] = self.create_area_vis(
            "flow-count",
            "Flow Count Over Time",
            "@timestamp",
            "_index",  # count
            None,
            "line",
            index_pattern_id
        )
        
        print("\n  --- Device Overview ---")
        # 8. Top Exporters (Devices)
        visualizations['top_exporters'] = self.create_table_vis(
            "top-exporters",
            "Top Flow Exporters (Devices)",
            "flow.export.ip.addr",
            "flow.bytes",
            "Device (Exporter IP)",
            index_pattern_id
        )
        
        # Original 4 visualizations (create for completeness)
        print("\n  --- Original Core Visualizations ---")
        visualizations['traffic_over_time'] = self.create_area_vis(
            "traffic-over-time",
            "Total Traffic Over Time",
            "@timestamp",
            "flow.bytes",
            None,
            "area",
            index_pattern_id
        )
        
        visualizations['top_src_ip'] = self.create_table_vis(
            "top-src-ip",
            "Top Source IPs",
            "flow.src.addr",
            "flow.bytes",
            "Source IP",
            index_pattern_id
        )
        
        visualizations['top_dst_ip'] = self.create_table_vis(
            "top-dst-ip",
            "Top Destination IPs",
            "flow.dst.addr",
            "flow.bytes",
            "Destination IP",
            index_pattern_id
        )
        
        visualizations['traffic_by_proto'] = self.create_pie_vis(
            "traffic-by-proto",
            "Traffic by Protocol",
            "l4.proto.name",
            "flow.bytes",
            index_pattern_id
        )
        
        # Step 3: Create Dashboard
        print("\n[3/4] Building Dashboard Panels...")
        
        panels = []
        
        # Row 0: Device Filter (full width)
        if visualizations['device_filter']:
            panels.append({'vis_id': visualizations['device_filter'], 'y': 0, 'col': 0, 'full_width': True, 'type': 'control'})
        
        # Row 1: Traffic Overview (full width - original 1)
        if visualizations['traffic_over_time']:
            panels.append({'vis_id': visualizations['traffic_over_time'], 'y': 1, 'col': 0, 'full_width': True})
        
        # Row 2: Flow Count + Bytes In/Out
        if visualizations['flow_count']:
            panels.append({'vis_id': visualizations['flow_count'], 'y': 2, 'col': 0})
        if visualizations['bytes_in_out']:
            panels.append({'vis_id': visualizations['bytes_in_out'], 'y': 2, 'col': 1})
        
        # Row 3: Top Exporters + Applications
        if visualizations['top_exporters']:
            panels.append({'vis_id': visualizations['top_exporters'], 'y': 3, 'col': 0})
        if visualizations['top_applications']:
            panels.append({'vis_id': visualizations['top_applications'], 'y': 3, 'col': 1})
        
        # Row 4: Source IPs + Destination IPs
        if visualizations['top_src_ip']:
            panels.append({'vis_id': visualizations['top_src_ip'], 'y': 4, 'col': 0})
        if visualizations['top_dst_ip']:
            panels.append({'vis_id': visualizations['top_dst_ip'], 'y': 4, 'col': 1})
        
        # Row 5: Source Ports + Destination Ports
        if visualizations['top_src_ports']:
            panels.append({'vis_id': visualizations['top_src_ports'], 'y': 5, 'col': 0})
        if visualizations['top_dst_ports']:
            panels.append({'vis_id': visualizations['top_dst_ports'], 'y': 5, 'col': 1})
        
        # Row 6: Source Countries + Protocol Distribution
        if visualizations['top_src_countries']:
            panels.append({'vis_id': visualizations['top_src_countries'], 'y': 6, 'col': 0})
        if visualizations['traffic_by_proto']:
            panels.append({'vis_id': visualizations['traffic_by_proto'], 'y': 6, 'col': 1})
        
        # Row 7: Traffic by Hour
        if visualizations['traffic_by_hour']:
            panels.append({'vis_id': visualizations['traffic_by_hour'], 'y': 7, 'col': 0, 'full_width': True})
        
        # Create the dashboard
        dashboard_id = self.create_dashboard("Enhanced Unified - Flow Analysis (Device Filtered)", panels)
        
        # Summary
        print("\n" + "="*70)
        print("SUMMARY")
        print("="*70)
        print(f"\nDashboard Created: {dashboard_id}")
        print(f"\nVisualization IDs:")
        print(f"  1. Device Filter:           {visualizations.get('device_filter', 'N/A')}")
        print(f"  2. Top Source Ports:        {visualizations.get('top_src_ports', 'N/A')}")
        print(f"  3. Top Destination Ports:   {visualizations.get('top_dst_ports', 'N/A')}")
        print(f"  4. Top Source Countries:    {visualizations.get('top_src_countries', 'N/A')}")
        print(f"  5. Traffic by Hour:         {visualizations.get('traffic_by_hour', 'N/A')}")
        print(f"  6. Top Applications:        {visualizations.get('top_applications', 'N/A')}")
        print(f"  7. Bytes In vs Out:         {visualizations.get('bytes_in_out', 'N/A')}")
        print(f"  8. Flow Count Over Time:    {visualizations.get('flow_count', 'N/A')}")
        print(f"  9. Top Exporters:           {visualizations.get('top_exporters', 'N/A')}")
        print(f" 10. Traffic Over Time:       {visualizations.get('traffic_over_time', 'N/A')}")
        print(f" 11. Top Source IPs:          {visualizations.get('top_src_ip', 'N/A')}")
        print(f" 12. Top Destination IPs:     {visualizations.get('top_dst_ip', 'N/A')}")
        print(f" 13. Traffic by Protocol:     {visualizations.get('traffic_by_proto', 'N/A')}")
        
        print(f"\nDashboard URL:")
        print(f"  {KIBANA_URL}/app/dashboards#/view/{dashboard_id}")
        
        return {
            'dashboard_id': dashboard_id,
            'visualizations': visualizations
        }


if __name__ == "__main__":
    creator = KibanaObjectCreator()
    result = creator.run()
    
    print("\n" + "="*70)
    print("Device Filtering Mechanism:")
    print("="*70)
    print("""
The device filter is an Input Control Visualization that:
1. Uses the 'flow.export.ip.addr' field to list all unique flow exporters
2. When you select one or more devices, it adds filter pills to the dashboard
3. All panels then update to show only flows from the selected devices
4. The filter is applied at the dashboard level (global filter)
5. Uses Kibana's time filter for date range selection integrated with device filter

To use:
- Open the dashboard
- Use the dropdown at the top to select device(s)
- Click 'Apply' to filter all panels
- Charts and tables update dynamically
    """)

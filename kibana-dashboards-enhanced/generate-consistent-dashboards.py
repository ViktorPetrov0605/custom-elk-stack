#!/usr/bin/env python3
"""
Generate unified flow dashboards following the base structure of network-flow-dashboard:
- 2-column layout (panels 24w wide)
- Consistent panel heights (15h for charts, 10h for metrics)
- timeRestore: true with last 15m
- refreshInterval: 15s
- Links navigation panel
- Uses unified-flow-pattern (consistent with existing)
"""
import json

# Dashboard IDs and titles
DASHBOARD_DETAILED = {
    "id": "unified-flow-detailed-v2",
    "title": "[Unified Flow] Detailed Traffic Analysis",
    "description": "Comprehensive traffic analysis with device breakdown - based on NetFlow dashboard patterns"
}

DASHBOARD_TOPN = {
    "id": "unified-flow-topn-v2", 
    "title": "[Unified Flow] Top-N Analysis",
    "description": "Top talkers, ports, protocols, and AS - enhanced rankings"
}

DASHBOARD_CONVERSATIONS = {
    "id": "unified-flow-conversations-v2",
    "title": "[Unified Flow] Conversation Partners", 
    "description": "Source-destination pairs and connection analysis"
}

def build_nav_links(current_id):
    """Build navigation links panel for dashboard header"""
    links = []
    dashboards = [
        ("unified-flow-detailed-v2", "Detailed Analysis", 0),
        ("unified-flow-topn-v2", "Top-N", 1),
        ("unified-flow-conversations-v2", "Conversations", 2),
    ]
    for dash_id, label, order in dashboards:
        links.append({
            "id": f"link_{dash_id}",
            "type": "dashboardLink",
            "destinationRefName": f"link_{dash_id}_dashboard",
            "label": label,
            "order": order
        })
    return {
        "embeddableConfig": {
            "attributes": {
                "layout": "horizontal",
                "links": links
            },
            "disabledActions": ["OPEN_FLYOUT_ADD_DRILLDOWN"],
            "enhancements": {}
        },
        "gridData": {"x": 0, "y": 0, "w": 48, "h": 4, "i": "nav"},
        "panelIndex": "nav",
        "title": "Dashboard Navigation",
        "type": "links",
        "version": "8.9.0"
    }

def build_metric_panel(index, title, field, color, x, y, label=None):
    """Build a metric card panel using Lens"""
    layer_id = f"metric_{index}"
    metric_col = f"metric_col_{index}"
    return {
        "embeddableConfig": {
            "attributes": {
                "references": [{"id": "unified-flow-pattern", "name": f"indexpattern-datasource-layer-{layer_id}", "type": "index-pattern"}],
                "state": {
                    "datasourceStates": {
                        "formBased": {
                            "layers": {
                                layer_id: {
                                    "columnOrder": [metric_col],
                                    "columns": {
                                        metric_col: {"customLabel": True, "dataType": "number", "isBucketed": False, "label": label or title, "operationType": "unique_count" if "unique" in title.lower() else "sum" if "bytes" in field or "packets" in field else "count", "params": {"emptyAsNull": True}, "scale": "ratio", "sourceField": field}
                                    },
                                    "incompleteColumns": {}
                                }
                            }
                        }
                    },
                    "query": {"language": "kuery", "query": ""},
                    "filters": [],
                    "visualization": {"color": color, "layerId": layer_id, "layerType": "data", "metricAccessor": metric_col}
                },
                "title": f"[Flow] {title}",
                "type": "lens",
                "visualizationType": "lnsMetric"
            },
            "enhancements": {},
            "hidePanelTitles": False
        },
        "gridData": {"x": x, "y": y, "w": 12, "h": 10, "i": str(index)},
        "panelIndex": str(index),
        "title": title,
        "type": "lens",
        "version": "8.9.0"
    }

def build_timeline_panel(index, title, x, y, h=15):
    """Build traffic timeline with device breakdown"""
    layer_id = f"timeline_{index}"
    return {
        "embeddableConfig": {
            "attributes": {
                "references": [{"id": "unified-flow-pattern", "name": f"indexpattern-datasource-layer-{layer_id}", "type": "index-pattern"}],
                "state": {
                    "datasourceStates": {
                        "formBased": {
                            "layers": {
                                layer_id: {
                                    "columnOrder": ["device", "ts", "bytes"],
                                    "columns": {
                                        "device": {"customLabel": True, "dataType": "string", "isBucketed": True, "label": "Device", "operationType": "terms", "params": {"exclude": [], "excludeIsRegex": False, "include": [], "includeIsRegex": False, "missingBucket": False, "orderBy": {"columnId": "bytes", "type": "column"}, "orderDirection": "desc", "otherBucket": False, "parentFormat": {"id": "terms"}, "size": 5}, "scale": "ordinal", "sourceField": "device.name"},
                                        "ts": {"customLabel": True, "dataType": "date", "isBucketed": True, "label": "@timestamp", "operationType": "date_histogram", "params": {"dropPartials": False, "includeEmptyRows": True, "interval": "auto"}, "scale": "interval", "sourceField": "@timestamp"},
                                        "bytes": {"customLabel": True, "dataType": "number", "isBucketed": False, "label": "Bytes", "operationType": "sum", "params": {"emptyAsNull": True}, "scale": "ratio", "sourceField": "network.bytes"}
                                    },
                                    "incompleteColumns": {}
                                }
                            }
                        }
                    },
                    "query": {"language": "kuery", "query": ""},
                    "filters": [],
                    "visualization": {
                        "axisTitlesVisibilitySettings": {"x": True, "yLeft": True, "yRight": True},
                        "fittingFunction": "None",
                        "gridlinesVisibilitySettings": {"x": True, "yLeft": True, "yRight": True},
                        "labelsOrientation": {"x": 0, "yLeft": 0, "yRight": 0},
                        "layers": [{"accessors": ["bytes"], "layerId": layer_id, "layerType": "data", "seriesType": "area_stacked", "palette": {"name": "status", "type": "palette"}, "splitAccessor": "device", "xAccessor": "ts"}],
                        "legend": {"isVisible": True, "position": "right"},
                        "preferredSeriesType": "area_stacked",
                        "tickLabelsVisibilitySettings": {"x": True, "yLeft": True, "yRight": True},
                        "valueLabels": "hide"
                    }
                },
                "title": f"[Flow] {title}",
                "type": "lens",
                "visualizationType": "lnsXY"
            },
            "enhancements": {},
            "hidePanelTitles": False
        },
        "gridData": {"x": x, "y": y, "w": 24, "h": h, "i": str(index)},
        "panelIndex": str(index),
        "title": title,
        "type": "lens",
        "version": "8.9.0"
    }

def build_pie_panel(index, title, field, field_label, palette, x, y):
    """Build donut/pie chart panel"""
    layer_id = f"pie_{index}"
    return {
        "embeddableConfig": {
            "attributes": {
                "references": [{"id": "unified-flow-pattern", "name": f"indexpattern-datasource-layer-{layer_id}", "type": "index-pattern"}],
                "state": {
                    "datasourceStates": {
                        "formBased": {
                            "layers": {
                                layer_id: {
                                    "columnOrder": ["field", "bytes"],
                                    "columns": {
                                        "field": {"customLabel": True, "dataType": "string" if field in ["network.transport", "device.name"] else "ip", "isBucketed": True, "label": field_label, "operationType": "terms", "params": {"exclude": [], "excludeIsRegex": False, "include": [], "includeIsRegex": False, "missingBucket": False, "orderBy": {"columnId": "bytes", "type": "column"}, "orderDirection": "desc", "otherBucket": False, "parentFormat": {"id": "terms"}, "size": 10}, "scale": "ordinal", "sourceField": field},
                                        "bytes": {"customLabel": True, "dataType": "number", "isBucketed": False, "label": "Bytes", "operationType": "sum", "params": {"emptyAsNull": True, "format": {"id": "bytes", "params": {"decimals": 2}}}, "scale": "ratio", "sourceField": "network.bytes"}
                                    },
                                    "incompleteColumns": {}
                                }
                            }
                        }
                    },
                    "query": {"language": "kuery", "query": ""},
                    "filters": [],
                    "visualization": {
                        "layers": [{"categoryDisplay": "default", "emptySizeRatio": 0.3, "layerId": layer_id, "layerType": "data", "legendDisplay": "show", "legendPosition": "right", "metrics": ["bytes"], "nestedLegend": False, "numberDisplay": "percent", "percentDecimals": 2, "primaryGroups": ["field"], "secondaryGroups": [], "showValuesInLegend": True}],
                        "palette": {"name": palette, "type": "palette"},
                        "shape": "donut"
                    }
                },
                "title": f"[Flow] {title}",
                "type": "lens",
                "visualizationType": "lnsPie"
            },
            "enhancements": {},
            "hidePanelTitles": False
        },
        "gridData": {"x": x, "y": y, "w": 24, "h": 15, "i": str(index)},
        "panelIndex": str(index),
        "title": title,
        "type": "lens",
        "version": "8.9.0"
    }

def build_table_panel(index, title, field, field_label, x, y):
    """Build data table panel for Top-N"""
    layer_id = f"table_{index}"
    return {
        "embeddableConfig": {
            "attributes": {
                "references": [{"id": "unified-flow-pattern", "name": f"indexpattern-datasource-layer-{layer_id}", "type": "index-pattern"}],
                "state": {
                    "datasourceStates": {
                        "formBased": {
                            "layers": {
                                layer_id: {
                                    "columnOrder": ["field", "bytes", "packets", "flows"],
                                    "columns": {
                                        "field": {"customLabel": True, "dataType": "string" if field in ["network.transport", "device.name"] else "ip" if field in ["source.ip", "destination.ip"] else "number", "isBucketed": True, "label": field_label, "operationType": "terms", "params": {"exclude": [], "excludeIsRegex": False, "include": [], "includeIsRegex": False, "missingBucket": False, "orderBy": {"columnId": "bytes", "type": "column"}, "orderDirection": "desc", "otherBucket": False, "parentFormat": {"id": "terms"}, "size": 50}, "scale": "ordinal", "sourceField": field},
                                        "bytes": {"customLabel": True, "dataType": "number", "isBucketed": False, "label": "Bytes", "operationType": "sum", "params": {"emptyAsNull": True, "format": {"id": "bytes", "params": {"decimals": 2}}}, "scale": "ratio", "sourceField": "network.bytes"},
                                        "packets": {"customLabel": True, "dataType": "number", "isBucketed": False, "label": "Packets", "operationType": "sum", "params": {"emptyAsNull": True}, "scale": "ratio", "sourceField": "network.packets"},
                                        "flows": {"customLabel": True, "dataType": "number", "isBucketed": False, "label": "Flows", "operationType": "count", "params": {"emptyAsNull": True}, "scale": "ratio", "sourceField": "___records___"}
                                    },
                                    "incompleteColumns": {}
                                }
                            }
                        }
                    },
                    "query": {"language": "kuery", "query": ""},
                    "filters": [],
                    "visualization": {
                        "columns": [
                            {"alignment": "left", "columnId": "bytes", "summaryRow": "sum"},
                            {"alignment": "left", "columnId": "packets", "summaryRow": "sum"},
                            {"alignment": "left", "columnId": "flows", "summaryRow": "sum"},
                            {"alignment": "left", "columnId": "field"}
                        ],
                        "headerRowHeight": "single",
                        "layerId": layer_id,
                        "layerType": "data",
                        "paging": {"enabled": True, "size": 10},
                        "rowHeight": "single"
                    }
                },
                "title": f"[Flow] {title}",
                "type": "lens",
                "visualizationType": "lnsDatatable"
            },
            "enhancements": {},
            "hidePanelTitles": False
        },
        "gridData": {"x": x, "y": y, "w": 24, "h": 20, "i": str(index)},
        "panelIndex": str(index),
        "title": title,
        "type": "lens",
        "version": "8.9.0"
    }

def build_conversation_table(index, x, y):
    """Build conversation partners table with src/dst"""
    layer_id = f"conv_{index}"
    return {
        "embeddableConfig": {
            "attributes": {
                "references": [{"id": "unified-flow-pattern", "name": f"indexpattern-datasource-layer-{layer_id}", "type": "index-pattern"}],
                "state": {
                    "datasourceStates": {
                        "formBased": {
                            "layers": {
                                layer_id: {
                                    "columnOrder": ["src", "dst", "bytes", "packets", "flows"],
                                    "columns": {
                                        "src": {"customLabel": True, "dataType": "ip", "isBucketed": True, "label": "Source", "operationType": "terms", "params": {"exclude": [], "excludeIsRegex": False, "include": [], "includeIsRegex": False, "missingBucket": False, "orderBy": {"columnId": "bytes", "type": "column"}, "orderDirection": "desc", "otherBucket": False, "parentFormat": {"id": "terms"}, "size": 50}, "scale": "ordinal", "sourceField": "source.ip"},
                                        "dst": {"customLabel": True, "dataType": "ip", "isBucketed": True, "label": "Destination", "operationType": "terms", "params": {"exclude": [], "excludeIsRegex": False, "include": [], "includeIsRegex": False, "missingBucket": False, "orderBy": {"columnId": "bytes", "type": "column"}, "orderDirection": "desc", "otherBucket": False, "parentFormat": {"id": "terms"}, "size": 50}, "scale": "ordinal", "sourceField": "destination.ip"},
                                        "bytes": {"customLabel": True, "dataType": "number", "isBucketed": False, "label": "Bytes", "operationType": "sum", "params": {"emptyAsNull": True, "format": {"id": "bytes", "params": {"decimals": 2}}}, "scale": "ratio", "sourceField": "network.bytes"},
                                        "packets": {"customLabel": True, "dataType": "number", "isBucketed": False, "label": "Packets", "operationType": "sum", "params": {"emptyAsNull": True}, "scale": "ratio", "sourceField": "network.packets"},
                                        "flows": {"customLabel": True, "dataType": "number", "isBucketed": False, "label": "Flows", "operationType": "count", "params": {"emptyAsNull": True}, "scale": "ratio", "sourceField": "___records___"}
                                    },
                                    "incompleteColumns": {}
                                }
                            }
                        }
                    },
                    "query": {"language": "kuery", "query": ""},
                    "filters": [],
                    "visualization": {
                        "columns": [
                            {"alignment": "left", "columnId": "bytes"},
                            {"alignment": "left", "columnId": "packets"},
                            {"alignment": "left", "columnId": "flows"},
                            {"alignment": "left", "columnId": "src"},
                            {"alignment": "left", "columnId": "dst"}
                        ],
                        "headerRowHeight": "single",
                        "layerId": layer_id,
                        "layerType": "data",
                        "paging": {"enabled": True, "size": 10},
                        "rowHeight": "single"
                    }
                },
                "title": "[Flow] Conversation Partners",
                "type": "lens",
                "visualizationType": "lnsDatatable"
            },
            "enhancements": {},
            "hidePanelTitles": False
        },
        "gridData": {"x": x, "y": y, "w": 48, "h": 24, "i": str(index)},
        "panelIndex": str(index),
        "title": "Conversation Partners",
        "type": "lens",
        "version": "8.9.0"
    }

# ========== BUILD DETAILED TRAFFIC DASHBOARD ==========
panels_detailed = []
# Row 1: Navigation
y_pos = 0
panels_detailed.append(build_nav_links(DASHBOARD_DETAILED["id"]))
y_pos += 4

# Row 2: Traffic Timeline (full width like existing)
panels_detailed.append(build_timeline_panel(1, "Traffic Timeline by Device", 0, y_pos, 15))
panels_detailed.append(build_pie_panel(2, "Protocol Distribution", "network.transport", "Protocol", "warm", 24, y_pos))
y_pos += 15

# Row 3: Metric cards (4 across, following existing metric style)
panels_detailed.append(build_metric_panel(3, "Total Bytes", "network.bytes", "#6092C0", 0, y_pos))
panels_detailed.append(build_metric_panel(4, "Total Packets", "network.packets", "#54B399", 12, y_pos))
panels_detailed.append(build_metric_panel(5, "Unique Sources", "source.ip", "#9170B8", 24, y_pos, "Sources"))
panels_detailed.append(build_metric_panel(6, "Unique Destinations", "destination.ip", "#D36086", 36, y_pos, "Destinations"))
y_pos += 10

# Row 4: Sources and Destinations donut charts
panels_detailed.append(build_pie_panel(7, "Top Sources", "source.ip", "Source", "temperature", 0, y_pos))
panels_detailed.append(build_pie_panel(8, "Top Destinations", "destination.ip", "Destination", "complementary", 24, y_pos))
y_pos += 15

# Row 5: Device traffic by bytes and packets
panels_detailed.append(build_timeline_panel(9, "Device Traffic (Bytes)", 0, y_pos))
panels_detailed.append(build_timeline_panel(10, "Device Traffic (Packets)", 24, y_pos))

# Build dashboard object
dashboard_detailed = {
    "attributes": {
        "description": DASHBOARD_DETAILED["description"],
        "kibanaSavedObjectMeta": {
            "searchSourceJSON": json.dumps({"filter": [], "query": {"language": "kuery", "query": ""}})
        },
        "optionsJSON": json.dumps({"hidePanelTitles": False, "syncColors": False, "syncCursor": True, "syncTooltips": False, "useMargins": True}),
        "panelsJSON": json.dumps(panels_detailed),
        "refreshInterval": {"pause": False, "value": 15000},
        "timeRestore": True,
        "timeFrom": "now-15m",
        "timeTo": "now",
        "title": DASHBOARD_DETAILED["title"]
    },
    "coreMigrationVersion": "8.8.0",
    "created_at": "2026-02-11T15:00:00Z",
    "id": DASHBOARD_DETAILED["id"],
    "managed": False,
    "references": [
        {"id": "unified-flow-pattern", "name": "index-pattern", "type": "index-pattern"},
        {"id": DASHBOARD_TOPN["id"], "name": "link_unified-flow-topn-v2_dashboard", "type": "dashboard"},
        {"id": DASHBOARD_CONVERSATIONS["id"], "name": "link_unified-flow-conversations-v2_dashboard", "type": "dashboard"}
    ],
    "type": "dashboard",
    "typeMigrationVersion": "10.3.0",
    "updated_at": "2026-02-11T15:00:00Z",
    "version": "WzE1MCwxXQ=="
}

# ========== BUILD TOP-N DASHBOARD ==========
panels_topn = []
y_pos = 0

# Navigation
panels_topn.append(build_nav_links(DASHBOARD_TOPN["id"]))
y_pos += 4

# Row 1: Top Sources and Top Destinations tables
panels_topn.append(build_table_panel(1, "Top Sources", "source.ip", "Source", 0, y_pos))
panels_topn.append(build_table_panel(2, "Top Destinations", "destination.ip", "Destination", 24, y_pos))
y_pos += 20

# Row 2: Top Source Ports and Top Destination Ports
panels_topn.append(build_table_panel(3, "Top Source Ports", "source.port", "Source Port", 0, y_pos))
panels_topn.append(build_table_panel(4, "Top Destination Ports", "destination.port", "Destination Port", 24, y_pos))
y_pos += 20

# Row 3: Top Protocols and Top Devices
panels_topn.append(build_table_panel(5, "Top Protocols", "network.transport", "Protocol", 0, y_pos))
panels_topn.append(build_table_panel(6, "Top Devices", "device.name", "Device", 24, y_pos))
y_pos += 20

# Row 4: Top Source AS and Top Destination AS
panels_topn.append(build_table_panel(7, "Top Source AS", "source.as.number", "AS Number", 0, y_pos))
panels_topn.append(build_table_panel(8, "Top Destination AS", "destination.as.number", "AS Number", 24, y_pos))

dashboard_topn = {
    "attributes": {
        "description": DASHBOARD_TOPN["description"],
        "kibanaSavedObjectMeta": {
            "searchSourceJSON": json.dumps({"filter": [], "query": {"language": "kuery", "query": ""}})
        },
        "optionsJSON": json.dumps({"hidePanelTitles": False, "syncColors": False, "syncCursor": True, "syncTooltips": False, "useMargins": True}),
        "panelsJSON": json.dumps(panels_topn),
        "refreshInterval": {"pause": False, "value": 15000},
        "timeRestore": True,
        "timeFrom": "now-15m",
        "timeTo": "now",
        "title": DASHBOARD_TOPN["title"]
    },
    "coreMigrationVersion": "8.8.0",
    "created_at": "2026-02-11T15:00:00Z",
    "id": DASHBOARD_TOPN["id"],
    "managed": False,
    "references": [
        {"id": "unified-flow-pattern", "name": "index-pattern", "type": "index-pattern"},
        {"id": DASHBOARD_DETAILED["id"], "name": "link_unified-flow-detailed-v2_dashboard", "type": "dashboard"},
        {"id": DASHBOARD_CONVERSATIONS["id"], "name": "link_unified-flow-conversations-v2_dashboard", "type": "dashboard"}
    ],
    "type": "dashboard",
    "typeMigrationVersion": "10.3.0",
    "updated_at": "2026-02-11T15:00:00Z",
    "version": "WzE2MCwxXQ=="
}

# ========== BUILD CONVERSATIONS DASHBOARD ==========
panels_conversations = []
y_pos = 0

# Navigation
panels_conversations.append(build_nav_links(DASHBOARD_CONVERSATIONS["id"]))
y_pos += 4

# Main conversation table (full width)
panels_conversations.append(build_conversation_table(1, 0, y_pos))
y_pos += 24

# Row 2: Protocol distribution and Port pairs
panels_conversations.append(build_pie_panel(2, "Protocol Distribution", "network.transport", "Protocol", "kibana_palette", 0, y_pos))
panels_conversations.append(build_pie_panel(3, "Top Src-Dst Pairs", "source.ip", "Source", "temperature", 24, y_pos))
y_pos += 15

# Row 3: Device bar chart and Timeline
panels_conversations.append({
    "embeddableConfig": {
        "attributes": {
            "references": [{"id": "unified-flow-pattern", "name": "indexpattern-datasource-layer-hbar", "type": "index-pattern"}],
            "state": {
                "datasourceStates": {
                    "formBased": {
                        "layers": {
                            "hbar": {
                                "columnOrder": ["device", "bytes"],
                                "columns": {
                                    "device": {"customLabel": True, "dataType": "string", "isBucketed": True, "label": "Device", "operationType": "terms", "params": {"exclude": [], "excludeIsRegex": False, "include": [], "includeIsRegex": False, "missingBucket": False, "orderBy": {"columnId": "bytes", "type": "column"}, "orderDirection": "desc", "otherBucket": False, "parentFormat": {"id": "terms"}, "size": 10}, "scale": "ordinal", "sourceField": "device.name"},
                                    "bytes": {"customLabel": True, "dataType": "number", "isBucketed": False, "label": "Bytes", "operationType": "sum", "params": {"emptyAsNull": True, "format": {"id": "bytes", "params": {"decimals": 2}}}, "scale": "ratio", "sourceField": "network.bytes"}
                                },
                                "incompleteColumns": {}
                            }
                        }
                    }
                },
                "query": {"language": "kuery", "query": ""},
                "filters": [],
                "visualization": {
                    "axisTitlesVisibilitySettings": {"x": True, "yLeft": True, "yRight": True},
                    "fittingFunction": "None",
                    "gridlinesVisibilitySettings": {"x": True, "yLeft": True, "yRight": True},
                    "labelsOrientation": {"x": 0, "yLeft": 0, "yRight": 0},
                    "layers": [{"accessors": ["bytes"], "layerId": "hbar", "layerType": "data", "seriesType": "bar_horizontal", "xAccessor": "device"}],
                    "legend": {"isVisible": False},
                    "preferredSeriesType": "bar_horizontal",
                    "tickLabelsVisibilitySettings": {"x": True, "yLeft": True, "yRight": True},
                    "valueLabels": "hide"
                }
            },
            "title": "[Flow] Top Devices by Bytes",
            "type": "lens",
            "visualizationType": "lnsXY"
        },
        "enhancements": {},
        "hidePanelTitles": False
    },
    "gridData": {"x": 0, "y": y_pos, "w": 24, "h": 16, "i": "4"},
    "panelIndex": "4",
    "title": "Top Devices by Bytes",
    "type": "lens",
    "version": "8.9.0"
})
panels_conversations.append(build_timeline_panel(5, "Device Traffic Timeline", 24, y_pos, 16))

dashboard_conversations = {
    "attributes": {
        "description": DASHBOARD_CONVERSATIONS["description"],
        "kibanaSavedObjectMeta": {
            "searchSourceJSON": json.dumps({"filter": [], "query": {"language": "kuery", "query": ""}})
        },
        "optionsJSON": json.dumps({"hidePanelTitles": False, "syncColors": False, "syncCursor": True, "syncTooltips": False, "useMargins": True}),
        "panelsJSON": json.dumps(panels_conversations),
        "refreshInterval": {"pause": False, "value": 15000},
        "timeRestore": True,
        "timeFrom": "now-15m",
        "timeTo": "now",
        "title": DASHBOARD_CONVERSATIONS["title"]
    },
    "coreMigrationVersion": "8.8.0",
    "created_at": "2026-02-11T15:00:00Z",
    "id": DASHBOARD_CONVERSATIONS["id"],
    "managed": False,
    "references": [
        {"id": "unified-flow-pattern", "name": "index-pattern", "type": "index-pattern"},
        {"id": DASHBOARD_DETAILED["id"], "name": "link_unified-flow-detailed-v2_dashboard", "type": "dashboard"},
        {"id": DASHBOARD_TOPN["id"], "name": "link_unified-flow-topn-v2_dashboard", "type": "dashboard"}
    ],
    "type": "dashboard",
    "typeMigrationVersion": "10.3.0",
    "updated_at": "2026-02-11T15:00:00Z",
    "version": "WzE3MCwxXQ=="
}

# Export all three dashboards
print(json.dumps(dashboard_detailed, separators=(',', ':')))
print(json.dumps(dashboard_topn, separators=(',', ':')))
print(json.dumps(dashboard_conversations, separators=(',', ':')))

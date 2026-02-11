#!/usr/bin/env python3
"""
Generate Kibana Dashboards for unified-flow-* index pattern
Based on NetFlow dashboards with field mapping:

FIELD MAPPINGS (NetFlow -> unified-flow):
- logs-* -> unified-flow-*
- data_stream.dataset:netflow.log -> unified-flow-* (index pattern filter)
- agent.name -> device.name
- netflow.exporter.version -> device.name (use for version grouping)
- netflow.ingress_interface -> interface.input
- netflow.egress_interface -> interface.output
- source.as.organization.name -> source.as.number
- destination.as.organization.name -> destination.as.number
- destination.geo.* -> (removed - no geo fields in unified schema)
- network.type -> source.ip (for IP version detection via scripted field or omit)
- @timestamp -> @timestamp (same)
- source.ip -> source.ip (same)
- source.port -> source.port (same)
- destination.ip -> destination.ip (same)
- destination.port -> destination.port (same)
- network.transport -> network.transport (same)
- network.bytes -> network.bytes (same)
- network.packets -> network.packets (same)

"""

import json
import uuid
import copy
from datetime import datetime, timezone

def generate_id(prefix="unified"):
    """Generate a unique ID for saved objects"""
    return f"{prefix}-{uuid.uuid4()}"

def create_index_pattern_ref(name="unified-flow-*"):
    """Create index pattern reference for unified-flow-*"""
    return [{"id": name, "name": "index-pattern", "type": "index-pattern"}]

def create_base_lens_config(title, layer_id, index_pattern="unified-flow-*"):
    """Create base Lens configuration"""
    return {
        "title": title,
        "type": "lens",
        "visualizationType": "lnsXY",
        "references": [
            {"id": index_pattern, "name": f"indexpattern-datasource-layer-{layer_id}", "type": "index-pattern"}
        ],
        "state": {
            "datasourceStates": {
                "formBased": {
                    "layers": {}
                }
            },
            "query": {"language": "kuery", "query": ""},
            "filters": []
        }
    }

def create_timestamp_column(col_id="timestamp"):
    """Create timestamp column for date histogram"""
    return {
        "customLabel": True,
        "dataType": "date",
        "isBucketed": True,
        "label": "@timestamp",
        "operationType": "date_histogram",
        "params": {
            "dropPartials": False,
            "includeEmptyRows": True,
            "interval": "auto"
        },
        "scale": "interval",
        "sourceField": "@timestamp"
    }

def create_terms_column(field, label, size=10, col_id=None):
    """Create terms aggregation column"""
    if col_id is None:
        col_id = str(uuid.uuid4())
    return {
        "customLabel": True,
        "dataType": "string" if field in ["device.name", "network.transport"] else "ip" if field in ["source.ip", "destination.ip"] else "number",
        "isBucketed": True,
        "label": label,
        "operationType": "terms",
        "params": {
            "exclude": [],
            "excludeIsRegex": False,
            "include": [],
            "includeIsRegex": False,
            "missingBucket": False,
            "orderBy": {"columnId": col_id, "type": "column"},
            "orderDirection": "desc",
            "otherBucket": False,
            "parentFormat": {"id": "terms"},
            "size": size
        },
        "scale": "ordinal",
        "sourceField": field
    }, col_id

def create_sum_column(field, label, format_id=None, col_id=None):
    """Create sum aggregation column"""
    if col_id is None:
        col_id = str(uuid.uuid4())
    params = {"emptyAsNull": True}
    if format_id:
        params["format"] = {"id": format_id, "params": {"decimals": 2}}
    return {
        "customLabel": True,
        "dataType": "number",
        "isBucketed": False,
        "label": label,
        "operationType": "sum",
        "params": params,
        "scale": "ratio",
        "sourceField": field
    }, col_id

def create_count_column(label, col_id=None):
    """Create count aggregation column"""
    if col_id is None:
        col_id = str(uuid.uuid4())
    return {
        "customLabel": True,
        "dataType": "number",
        "isBucketed": False,
        "label": label,
        "operationType": "count",
        "params": {"emptyAsNull": True},
        "scale": "ratio",
        "sourceField": "___records___"
    }, col_id

def create_unique_count_column(field, label, col_id=None):
    """Create unique count aggregation column"""
    if col_id is None:
        col_id = str(uuid.uuid4())
    return {
        "customLabel": True,
        "dataType": "number",
        "isBucketed": False,
        "label": label,
        "operationType": "unique_count",
        "params": {"emptyAsNull": True},
        "scale": "ratio",
        "sourceField": field
    }, col_id

def build_dashboard_1_traffic_analysis():
    """Build unified-flow-detailed-dashboard (Traffic Analysis)"""
    dashboard_id = "unified-flow-detailed-dashboard"
    
    panels = []
    panel_map = {}
    
    # Panel 1: Flow Records Timeline by Device (stacked bar)
    layer_id_1 = str(uuid.uuid4())
    timestamp_col = create_timestamp_column()
    device_terms_col, device_col_id = create_terms_column("device.name", "Device", size=10)
    count_col, count_col_id = create_count_column("Flow Records")
    
    lens_1 = {
        "title": f"[Unified Flow] Flow Records Timeline",
        "type": "lens",
        "visualizationType": "lnsXY",
        "references": [
            {"id": "unified-flow-*", "name": f"indexpattern-datasource-layer-{layer_id_1}", "type": "index-pattern"}
        ],
        "state": {
            "datasourceStates": {
                "formBased": {
                    "layers": {
                        layer_id_1: {
                            "columnOrder": [device_col_id, "timestamp", count_col_id],
                            "columns": {
                                device_col_id: device_terms_col,
                                "timestamp": timestamp_col,
                                count_col_id: count_col
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
                "curveType": "LINEAR",
                "gridlinesVisibilitySettings": {"x": False, "yLeft": True, "yRight": True},
                "labelsOrientation": {"x": 0, "yLeft": 0, "yRight": -90},
                "layers": [{
                    "accessors": [count_col_id],
                    "isHistogram": True,
                    "layerId": layer_id_1,
                    "layerType": "data",
                    "palette": {"name": "status", "type": "palette"},  # Colorful palette
                    "seriesType": "bar_stacked",
                    "splitAccessor": device_col_id,
                    "xAccessor": "timestamp"
                }],
                "legend": {"isVisible": True, "legendSize": "auto", "maxLines": 1, "position": "right", "shouldTruncate": True, "showSingleSeries": True},
                "preferredSeriesType": "bar_stacked",
                "tickLabelsVisibilitySettings": {"x": True, "yLeft": True, "yRight": True},
                "valueLabels": "hide",
                "yLeftScale": "linear"
            }
        }
    }
    
    panel_1 = {
        "embeddableConfig": lens_1,
        "gridData": {"h": 15, "i": "1", "w": 36, "x": 12, "y": 4},
        "panelIndex": "1",
        "title": "[Unified Flow] Flow Records Timeline",
        "type": "lens",
        "version": "8.9.0"
    }
    panels.append(panel_1)
    panel_map["1"] = lens_1
    
    # Panel 2: Total Flow Records Metric
    layer_id_2 = str(uuid.uuid4())
    metric_count_col, metric_count_id = create_count_column("Flow Records")
    
    lens_2 = {
        "title": f"[Unified Flow] Total Flow Records",
        "type": "lens",
        "visualizationType": "lnsMetric",
        "references": [
            {"id": "unified-flow-*", "name": f"indexpattern-datasource-layer-{layer_id_2}", "type": "index-pattern"}
        ],
        "state": {
            "datasourceStates": {
                "formBased": {
                    "layers": {
                        layer_id_2: {
                            "columnOrder": [metric_count_id],
                            "columns": {metric_count_id: metric_count_col},
                            "incompleteColumns": {}
                        }
                    }
                }
            },
            "query": {"language": "kuery", "query": ""},
            "filters": [],
            "visualization": {
                "color": "#6092C0",
                "layerId": layer_id_2,
                "layerType": "data",
                "metricAccessor": metric_count_id
            }
        }
    }
    
    panel_2 = {
        "embeddableConfig": lens_2,
        "gridData": {"h": 15, "i": "2", "w": 12, "x": 0, "y": 4},
        "panelIndex": "2",
        "title": "[Unified Flow] Total Flow Records",
        "type": "lens",
        "version": "8.9.0"
    }
    panels.append(panel_2)
    panel_map["2"] = lens_2
    
    # Panel 3: Sources Donut (Bytes)
    layer_id_3 = str(uuid.uuid4())
    source_terms_col, source_col_id = create_terms_column("source.ip", "Source", size=10)
    bytes_sum_col, bytes_col_id = create_sum_column("network.bytes", "Bytes", format_id="bytes")
    
    lens_3 = {
        "title": f"[Unified Flow] Sources by Bytes",
        "type": "lens",
        "visualizationType": "lnsPie",
        "references": [
            {"id": "unified-flow-*", "name": f"indexpattern-datasource-layer-{layer_id_3}", "type": "index-pattern"}
        ],
        "state": {
            "datasourceStates": {
                "formBased": {
                    "layers": {
                        layer_id_3: {
                            "columnOrder": [source_col_id, bytes_col_id],
                            "columns": {source_col_id: source_terms_col, bytes_col_id: bytes_sum_col},
                            "incompleteColumns": {}
                        }
                    }
                }
            },
            "query": {"language": "kuery", "query": ""},
            "filters": [],
            "visualization": {
                "layers": [{
                    "categoryDisplay": "default",
                    "emptySizeRatio": 0.3,
                    "layerId": layer_id_3,
                    "layerType": "data",
                    "legendDisplay": "show",
                    "legendPosition": "right",
                    "metrics": [bytes_col_id],
                    "nestedLegend": False,
                    "numberDisplay": "percent",
                    "percentDecimals": 2,
                    "primaryGroups": [source_col_id],
                    "secondaryGroups": [],
                    "showValuesInLegend": True
                }],
                "palette": {"name": "temperature", "type": "palette"},  # Colorful palette
                "shape": "donut"
            }
        }
    }
    
    panel_3 = {
        "embeddableConfig": lens_3,
        "gridData": {"h": 16, "i": "3", "w": 16, "x": 0, "y": 19},
        "panelIndex": "3",
        "title": "[Unified Flow] Sources by Bytes",
        "type": "lens",
        "version": "8.9.0"
    }
    panels.append(panel_3)
    panel_map["3"] = lens_3
    
    # Panel 4: Destinations Donut (Bytes)
    layer_id_4 = str(uuid.uuid4())
    dest_terms_col, dest_col_id = create_terms_column("destination.ip", "Destination", size=10)
    bytes_sum_col_4, bytes_col_id_4 = create_sum_column("network.bytes", "Bytes", format_id="bytes")
    
    lens_4 = {
        "title": f"[Unified Flow] Destinations by Bytes",
        "type": "lens",
        "visualizationType": "lnsPie",
        "references": [
            {"id": "unified-flow-*", "name": f"indexpattern-datasource-layer-{layer_id_4}", "type": "index-pattern"}
        ],
        "state": {
            "datasourceStates": {
                "formBased": {
                    "layers": {
                        layer_id_4: {
                            "columnOrder": [dest_col_id, bytes_col_id_4],
                            "columns": {dest_col_id: dest_terms_col, bytes_col_id_4: bytes_sum_col_4},
                            "incompleteColumns": {}
                        }
                    }
                }
            },
            "query": {"language": "kuery", "query": ""},
            "filters": [],
            "visualization": {
                "layers": [{
                    "categoryDisplay": "default",
                    "emptySizeRatio": 0.3,
                    "layerId": layer_id_4,
                    "layerType": "data",
                    "legendDisplay": "show",
                    "legendPosition": "right",
                    "metrics": [bytes_col_id_4],
                    "nestedLegend": False,
                    "numberDisplay": "percent",
                    "percentDecimals": 2,
                    "primaryGroups": [dest_col_id],
                    "secondaryGroups": [],
                    "showValuesInLegend": True
                }],
                "palette": {"name": "complementary", "type": "palette"},  # Colorful palette
                "shape": "donut"
            }
        }
    }
    
    panel_4 = {
        "embeddableConfig": lens_4,
        "gridData": {"h": 16, "i": "4", "w": 16, "x": 16, "y": 19},
        "panelIndex": "4",
        "title": "[Unified Flow] Destinations by Bytes",
        "type": "lens",
        "version": "8.9.0"
    }
    panels.append(panel_4)
    panel_map["4"] = lens_4
    
    # Panel 5: Protocol Distribution (Bytes)
    layer_id_5 = str(uuid.uuid4())
    proto_terms_col, proto_col_id = create_terms_column("network.transport", "Protocol", size=5)
    bytes_sum_col_5, bytes_col_id_5 = create_sum_column("network.bytes", "Bytes", format_id="bytes")
    
    lens_5 = {
        "title": f"[Unified Flow] Protocol Distribution",
        "type": "lens",
        "visualizationType": "lnsPie",
        "references": [
            {"id": "unified-flow-*", "name": f"indexpattern-datasource-layer-{layer_id_5}", "type": "index-pattern"}
        ],
        "state": {
            "datasourceStates": {
                "formBased": {
                    "layers": {
                        layer_id_5: {
                            "columnOrder": [proto_col_id, bytes_col_id_5],
                            "columns": {proto_col_id: proto_terms_col, bytes_col_id_5: bytes_sum_col_5},
                            "incompleteColumns": {}
                        }
                    }
                }
            },
            "query": {"language": "kuery", "query": ""},
            "filters": [],
            "visualization": {
                "layers": [{
                    "categoryDisplay": "default",
                    "emptySizeRatio": 0.3,
                    "layerId": layer_id_5,
                    "layerType": "data",
                    "legendDisplay": "show",
                    "legendPosition": "right",
                    "metrics": [bytes_col_id_5],
                    "nestedLegend": False,
                    "numberDisplay": "percent",
                    "percentDecimals": 2,
                    "primaryGroups": [proto_col_id],
                    "secondaryGroups": [],
                    "showValuesInLegend": True
                }],
                "palette": {"name": "warm", "type": "palette"},  # Red/yellow colors
                "shape": "donut"
            }
        }
    }
    
    panel_5 = {
        "embeddableConfig": lens_5,
        "gridData": {"h": 16, "i": "5", "w": 16, "x": 32, "y": 19},
        "panelIndex": "5",
        "title": "[Unified Flow] Protocol Distribution",
        "type": "lens",
        "version": "8.9.0"
    }
    panels.append(panel_5)
    panel_map["5"] = lens_5
    
    # Panel 6: Top Source Devices (Bytes stacked area)
    layer_id_6 = str(uuid.uuid4())
    device_terms_col_6, device_col_id_6 = create_terms_column("device.name", "Device", size=5)
    bytes_sum_col_6, bytes_col_id_6 = create_sum_column("network.bytes", "Bytes", format_id="bytes")
    
    lens_6 = {
        "title": f"[Unified Flow] Device Traffic (Bytes)",
        "type": "lens",
        "visualizationType": "lnsXY",
        "references": [
            {"id": "unified-flow-*", "name": f"indexpattern-datasource-layer-{layer_id_6}", "type": "index-pattern"}
        ],
        "state": {
            "datasourceStates": {
                "formBased": {
                    "layers": {
                        layer_id_6: {
                            "columnOrder": [device_col_id_6, "timestamp", bytes_col_id_6],
                            "columns": {
                                device_col_id_6: device_terms_col_6,
                                "timestamp": create_timestamp_column(),
                                bytes_col_id_6: bytes_sum_col_6
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
                "layers": [{
                    "accessors": [bytes_col_id_6],
                    "layerId": layer_id_6,
                    "layerType": "data",
                    "seriesType": "area_stacked",
                    "palette": {"name": "rainbow", "type": "palette"},  # Very colorful
                    "splitAccessor": device_col_id_6,
                    "xAccessor": "timestamp"
                }],
                "legend": {"isVisible": True, "position": "right"},
                "preferredSeriesType": "area_stacked",
                "tickLabelsVisibilitySettings": {"x": True, "yLeft": True, "yRight": True},
                "valueLabels": "hide"
            }
        }
    }
    
    panel_6 = {
        "embeddableConfig": lens_6,
        "gridData": {"h": 13, "i": "6", "w": 24, "x": 0, "y": 35},
        "panelIndex": "6",
        "title": "[Unified Flow] Device Traffic (Bytes)",
        "type": "lens",
        "version": "8.9.0"
    }
    panels.append(panel_6)
    panel_map["6"] = lens_6
    
    # Panel 7: Device Traffic by Packets (Stacked area)
    layer_id_7 = str(uuid.uuid4())
    device_terms_col_7, device_col_id_7 = create_terms_column("device.name", "Device", size=5)
    packets_sum_col_7, packets_col_id_7 = create_sum_column("network.packets", "Packets")
    
    lens_7 = {
        "title": f"[Unified Flow] Device Traffic (Packets)",
        "type": "lens",
        "visualizationType": "lnsXY",
        "references": [
            {"id": "unified-flow-*", "name": f"indexpattern-datasource-layer-{layer_id_7}", "type": "index-pattern"}
        ],
        "state": {
            "datasourceStates": {
                "formBased": {
                    "layers": {
                        layer_id_7: {
                            "columnOrder": [device_col_id_7, "timestamp", packets_col_id_7],
                            "columns": {
                                device_col_id_7: device_terms_col_7,
                                "timestamp": create_timestamp_column(),
                                packets_col_id_7: packets_sum_col_7
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
                "layers": [{
                    "accessors": [packets_col_id_7],
                    "layerId": layer_id_7,
                    "layerType": "data",
                    "seriesType": "area_stacked",
                    "palette": {"name": "ocean", "type": "palette"},
                    "splitAccessor": device_col_id_7,
                    "xAccessor": "timestamp"
                }],
                "legend": {"isVisible": True, "position": "right"},
                "preferredSeriesType": "area_stacked",
                "tickLabelsVisibilitySettings": {"x": True, "yLeft": True, "yRight": True},
                "valueLabels": "hide"
            }
        }
    }
    
    panel_7 = {
        "embeddableConfig": lens_7,
        "gridData": {"h": 13, "i": "7", "w": 24, "x": 24, "y": 35},
        "panelIndex": "7",
        "title": "[Unified Flow] Device Traffic (Packets)",
        "type": "lens",
        "version": "8.9.0"
    }
    panels.append(panel_7)
    panel_map["7"] = lens_7
    
    # Panel 8: Metric Cards Row - Source Count
    layer_id_8 = str(uuid.uuid4())
    unique_source_col, unique_source_id = create_unique_count_column("source.ip", "Unique Sources")
    
    lens_8 = {
        "title": f"[Unified Flow] Unique Sources",
        "type": "lens",
        "visualizationType": "lnsMetric",
        "references": [
            {"id": "unified-flow-*", "name": f"indexpattern-datasource-layer-{layer_id_8}", "type": "index-pattern"}
        ],
        "state": {
            "datasourceStates": {
                "formBased": {
                    "layers": {
                        layer_id_8: {
                            "columnOrder": [unique_source_id],
                            "columns": {unique_source_id: unique_source_col},
                            "incompleteColumns": {}
                        }
                    }
                }
            },
            "query": {"language": "kuery", "query": ""},
            "filters": [],
            "visualization": {
                "color": "#54B399",
                "layerId": layer_id_8,
                "layerType": "data",
                "metricAccessor": unique_source_id
            }
        }
    }
    
    panel_8 = {
        "embeddableConfig": lens_8,
        "gridData": {"h": 8, "i": "8", "w": 12, "x": 0, "y": 48},
        "panelIndex": "8",
        "title": "[Unified Flow] Unique Sources",
        "type": "lens",
        "version": "8.9.0"
    }
    panels.append(panel_8)
    panel_map["8"] = lens_8
    
    # Panel 9: Metric Card - Unique Destinations
    layer_id_9 = str(uuid.uuid4())
    unique_dest_col, unique_dest_id = create_unique_count_column("destination.ip", "Unique Destinations")
    
    lens_9 = {
        "title": f"[Unified Flow] Unique Destinations",
        "type": "lens",
        "visualizationType": "lnsMetric",
        "references": [
            {"id": "unified-flow-*", "name": f"indexpattern-datasource-layer-{layer_id_9}", "type": "index-pattern"}
        ],
        "state": {
            "datasourceStates": {
                "formBased": {
                    "layers": {
                        layer_id_9: {
                            "columnOrder": [unique_dest_id],
                            "columns": {unique_dest_id: unique_dest_col},
                            "incompleteColumns": {}
                        }
                    }
                }
            },
            "query": {"language": "kuery", "query": ""},
            "filters": [],
            "visualization": {
                "color": "#D36086",
                "layerId": layer_id_9,
                "layerType": "data",
                "metricAccessor": unique_dest_id
            }
        }
    }
    
    panel_9 = {
        "embeddableConfig": lens_9,
        "gridData": {"h": 8, "i": "9", "w": 12, "x": 12, "y": 48},
        "panelIndex": "9",
        "title": "[Unified Flow] Unique Destinations",
        "type": "lens",
        "version": "8.9.0"
    }
    panels.append(panel_9)
    panel_map["9"] = lens_9
    
    # Panel 10: Metric Card - Source Ports
    layer_id_10 = str(uuid.uuid4())
    unique_sp_col, unique_sp_id = create_unique_count_column("source.port", "Source Ports")
    
    lens_10 = {
        "title": f"[Unified Flow] Source Ports",
        "type": "lens",
        "visualizationType": "lnsMetric",
        "references": [
            {"id": "unified-flow-*", "name": f"indexpattern-datasource-layer-{layer_id_10}", "type": "index-pattern"}
        ],
        "state": {
            "datasourceStates": {
                "formBased": {
                    "layers": {
                        layer_id_10: {
                            "columnOrder": [unique_sp_id],
                            "columns": {unique_sp_id: unique_sp_col},
                            "incompleteColumns": {}
                        }
                    }
                }
            },
            "query": {"language": "kuery", "query": ""},
            "filters": [],
            "visualization": {
                "color": "#9170B8",
                "layerId": layer_id_10,
                "layerType": "data",
                "metricAccessor": unique_sp_id
            }
        }
    }
    
    panel_10 = {
        "embeddableConfig": lens_10,
        "gridData": {"h": 8, "i": "10", "w": 12, "x": 24, "y": 48},
        "panelIndex": "10",
        "title": "[Unified Flow] Source Ports",
        "type": "lens",
        "version": "8.9.0"
    }
    panels.append(panel_10)
    panel_map["10"] = lens_10
    
    # Panel 11: Metric Card - Destination Ports
    layer_id_11 = str(uuid.uuid4())
    unique_dp_col, unique_dp_id = create_unique_count_column("destination.port", "Destination Ports")
    
    lens_11 = {
        "title": f"[Unified Flow] Destination Ports",
        "type": "lens",
        "visualizationType": "lnsMetric",
        "references": [
            {"id": "unified-flow-*", "name": f"indexpattern-datasource-layer-{layer_id_11}", "type": "index-pattern"}
        ],
        "state": {
            "datasourceStates": {
                "formBased": {
                    "layers": {
                        layer_id_11: {
                            "columnOrder": [unique_dp_id],
                            "columns": {unique_dp_id: unique_dp_col},
                            "incompleteColumns": {}
                        }
                    }
                }
            },
            "query": {"language": "kuery", "query": ""},
            "filters": [],
            "visualization": {
                "color": "#CA8E00",
                "layerId": layer_id_11,
                "layerType": "data",
                "metricAccessor": unique_dp_id
            }
        }
    }
    
    panel_11 = {
        "embeddableConfig": lens_11,
        "gridData": {"h": 8, "i": "11", "w": 12, "x": 36, "y": 48},
        "panelIndex": "11",
        "title": "[Unified Flow] Destination Ports",
        "type": "lens",
        "version": "8.9.0"
    }
    panels.append(panel_11)
    panel_map["11"] = lens_11
    
    # Build dashboard JSON
    dashboard = {
        "attributes": {
            "description": "Unified Flow Detailed Traffic Analysis",
            "kibanaSavedObjectMeta": {
                "searchSourceJSON": json.dumps({
                    "filter": [],
                    "query": {"language": "kuery", "query": ""}
                })
            },
            "optionsJSON": json.dumps({
                "hidePanelTitles": False,
                "syncColors": False,
                "syncCursor": True,
                "syncTooltips": False,
                "useMargins": True
            }),
            "panelsJSON": json.dumps(panels),
            "refreshInterval": {
                "pause": False,
                "value": 15000  # Auto-refresh every 15 seconds
            },
            "timeRestore": True,
            "timeFrom": "now-15m",
            "timeTo": "now",
            "title": "[Unified Flow] Detailed Traffic Analysis"
        },
        "coreMigrationVersion": "8.8.0",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "id": dashboard_id,
        "references": [{"id": "unified-flow-*", "name": "index-pattern", "type": "index-pattern"}],
        "type": "dashboard",
        "updated_at": datetime.now(timezone.utc).isoformat(),
        "version": "WzE1MCwxXQ=="
    }
    
    return dashboard

print(json.dumps(build_dashboard_1_traffic_analysis(), indent=2))

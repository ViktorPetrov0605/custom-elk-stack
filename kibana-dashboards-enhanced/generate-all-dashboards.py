#!/usr/bin/env python3
"""
Generate all unified flow dashboards in proper NDJSON format (single line per object)
"""
import json
import uuid

# Dashboard 1: Detailed Traffic Analysis
dashboard_1 = {
    "attributes": {
        "description": "Unified Flow Detailed Traffic Analysis - Device traffic, sources, destinations, protocols with colorful visualizations",
        "kibanaSavedObjectMeta": {
            "searchSourceJSON": json.dumps({"filter": [], "query": {"language": "kuery", "query": ""}})
        },
        "optionsJSON": json.dumps({"hidePanelTitles": False, "syncColors": False, "syncCursor": True, "syncTooltips": False, "useMargins": True}),
        "panelsJSON": json.dumps([
            {
                "embeddableConfig": {
                    "attributes": {
                        "references": [{"id": "unified-flow-*", "name": "indexpattern-datasource-layer-timeline", "type": "index-pattern"}],
                        "state": {
                            "datasourceStates": {
                                "formBased": {
                                    "layers": {
                                        "timeline": {
                                            "columnOrder": ["device_col", "ts", "count_col"],
                                            "columns": {
                                                "device_col": {"customLabel": True, "dataType": "string", "isBucketed": True, "label": "Device", "operationType": "terms", "params": {"exclude": [], "excludeIsRegex": False, "include": [], "includeIsRegex": False, "missingBucket": False, "orderBy": {"columnId": "count_col", "type": "column"}, "orderDirection": "desc", "otherBucket": False, "parentFormat": {"id": "terms"}, "size": 10}, "scale": "ordinal", "sourceField": "device.name"},
                                                "ts": {"customLabel": True, "dataType": "date", "isBucketed": True, "label": "@timestamp", "operationType": "date_histogram", "params": {"dropPartials": False, "includeEmptyRows": True, "interval": "auto"}, "scale": "interval", "sourceField": "@timestamp"},
                                                "count_col": {"customLabel": True, "dataType": "number", "isBucketed": False, "label": "Flow Records", "operationType": "count", "params": {"emptyAsNull": True}, "scale": "ratio", "sourceField": "___records___"}
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
                                "layers": [{"accessors": ["count_col"], "isHistogram": True, "layerId": "timeline", "layerType": "data", "palette": {"name": "status", "type": "palette"}, "seriesType": "bar_stacked", "splitAccessor": "device_col", "xAccessor": "ts"}],
                                "legend": {"isVisible": True, "legendSize": "auto", "maxLines": 1, "position": "right", "shouldTruncate": True, "showSingleSeries": True},
                                "preferredSeriesType": "bar_stacked",
                                "tickLabelsVisibilitySettings": {"x": True, "yLeft": True, "yRight": True},
                                "valueLabels": "hide",
                                "yLeftScale": "linear"
                            }
                        },
                        "title": "[Unified Flow] Flow Records Timeline",
                        "type": "lens",
                        "visualizationType": "lnsXY"
                    },
                    "enhancements": {},
                    "hidePanelTitles": False
                },
                "gridData": {"h": 15, "i": "1", "w": 36, "x": 12, "y": 4},
                "panelIndex": "1",
                "title": "[Unified Flow] Flow Records Timeline",
                "type": "lens",
                "version": "8.9.0"
            },
            {
                "embeddableConfig": {
                    "attributes": {
                        "references": [{"id": "unified-flow-*", "name": "indexpattern-datasource-layer-metric", "type": "index-pattern"}],
                        "state": {
                            "datasourceStates": {
                                "formBased": {
                                    "layers": {
                                        "metric": {
                                            "columnOrder": ["total_count"],
                                            "columns": {
                                                "total_count": {"customLabel": True, "dataType": "number", "isBucketed": False, "label": "Flow Records", "operationType": "count", "params": {"emptyAsNull": True}, "scale": "ratio", "sourceField": "___records___"}
                                            },
                                            "incompleteColumns": {}
                                        }
                                    }
                                }
                            },
                            "query": {"language": "kuery", "query": ""},
                            "filters": [],
                            "visualization": {"color": "#6092C0", "layerId": "metric", "layerType": "data", "metricAccessor": "total_count"}
                        },
                        "title": "[Unified Flow] Total Flow Records",
                        "type": "lens",
                        "visualizationType": "lnsMetric"
                    },
                    "enhancements": {}
                },
                "gridData": {"h": 15, "i": "2", "w": 12, "x": 0, "y": 4},
                "panelIndex": "2",
                "title": "[Unified Flow] Total Flow Records",
                "type": "lens",
                "version": "8.9.0"
            },
            {
                "embeddableConfig": {
                    "attributes": {
                        "references": [{"id": "unified-flow-*", "name": "indexpattern-datasource-layer-sources", "type": "index-pattern"}],
                        "state": {
                            "datasourceStates": {
                                "formBased": {
                                    "layers": {
                                        "sources": {
                                            "columnOrder": ["src_ip", "bytes_col"],
                                            "columns": {
                                                "src_ip": {"customLabel": True, "dataType": "ip", "isBucketed": True, "label": "Source", "operationType": "terms", "params": {"exclude": [], "excludeIsRegex": False, "include": [], "includeIsRegex": False, "missingBucket": False, "orderBy": {"columnId": "bytes_col", "type": "column"}, "orderDirection": "desc", "otherBucket": False, "parentFormat": {"id": "terms"}, "size": 10}, "scale": "ordinal", "sourceField": "source.ip"},
                                                "bytes_col": {"customLabel": True, "dataType": "number", "isBucketed": False, "label": "Bytes", "operationType": "sum", "params": {"emptyAsNull": True, "format": {"id": "bytes", "params": {"decimals": 2}}}, "scale": "ratio", "sourceField": "network.bytes"}
                                            },
                                            "incompleteColumns": {}
                                        }
                                    }
                                }
                            },
                            "query": {"language": "kuery", "query": ""},
                            "filters": [],
                            "visualization": {
                                "layers": [{"categoryDisplay": "default", "emptySizeRatio": 0.3, "layerId": "sources", "layerType": "data", "legendDisplay": "show", "legendPosition": "right", "metrics": ["bytes_col"], "nestedLegend": False, "numberDisplay": "percent", "percentDecimals": 2, "primaryGroups": ["src_ip"], "secondaryGroups": [], "showValuesInLegend": True}],
                                "palette": {"name": "temperature", "type": "palette"},
                                "shape": "donut"
                            }
                        },
                        "title": "[Unified Flow] Sources by Bytes",
                        "type": "lens",
                        "visualizationType": "lnsPie"
                    },
                    "enhancements": {},
                    "hidePanelTitles": False
                },
                "gridData": {"h": 16, "i": "3", "w": 16, "x": 0, "y": 19},
                "panelIndex": "3",
                "title": "[Unified Flow] Sources by Bytes",
                "type": "lens",
                "version": "8.9.0"
            },
            {
                "embeddableConfig": {
                    "attributes": {
                        "references": [{"id": "unified-flow-*", "name": "indexpattern-datasource-layer-dests", "type": "index-pattern"}],
                        "state": {
                            "datasourceStates": {
                                "formBased": {
                                    "layers": {
                                        "dests": {
                                            "columnOrder": ["dst_ip", "bytes_col"],
                                            "columns": {
                                                "dst_ip": {"customLabel": True, "dataType": "ip", "isBucketed": True, "label": "Destination", "operationType": "terms", "params": {"exclude": [], "excludeIsRegex": False, "include": [], "includeIsRegex": False, "missingBucket": False, "orderBy": {"columnId": "bytes_col", "type": "column"}, "orderDirection": "desc", "otherBucket": False, "parentFormat": {"id": "terms"}, "size": 10}, "scale": "ordinal", "sourceField": "destination.ip"},
                                                "bytes_col": {"customLabel": True, "dataType": "number", "isBucketed": False, "label": "Bytes", "operationType": "sum", "params": {"emptyAsNull": True, "format": {"id": "bytes", "params": {"decimals": 2}}}, "scale": "ratio", "sourceField": "network.bytes"}
                                            },
                                            "incompleteColumns": {}
                                        }
                                    }
                                }
                            },
                            "query": {"language": "kuery", "query": ""},
                            "filters": [],
                            "visualization": {
                                "layers": [{"categoryDisplay": "default", "emptySizeRatio": 0.3, "layerId": "dests", "layerType": "data", "legendDisplay": "show", "legendPosition": "right", "metrics": ["bytes_col"], "nestedLegend": False, "numberDisplay": "percent", "percentDecimals": 2, "primaryGroups": ["dst_ip"], "secondaryGroups": [], "showValuesInLegend": True}],
                                "palette": {"name": "complementary", "type": "palette"},
                                "shape": "donut"
                            }
                        },
                        "title": "[Unified Flow] Destinations by Bytes",
                        "type": "lens",
                        "visualizationType": "lnsPie"
                    },
                    "enhancements": {},
                    "hidePanelTitles": False
                },
                "gridData": {"h": 16, "i": "4", "w": 16, "x": 16, "y": 19},
                "panelIndex": "4",
                "title": "[Unified Flow] Destinations by Bytes",
                "type": "lens",
                "version": "8.9.0"
            },
            {
                "embeddableConfig": {
                    "attributes": {
                        "references": [{"id": "unified-flow-*", "name": "indexpattern-datasource-layer-proto", "type": "index-pattern"}],
                        "state": {
                            "datasourceStates": {
                                "formBased": {
                                    "layers": {
                                        "proto": {
                                            "columnOrder": ["proto", "bytes_col"],
                                            "columns": {
                                                "proto": {"customLabel": True, "dataType": "string", "isBucketed": True, "label": "Protocol", "operationType": "terms", "params": {"exclude": [], "excludeIsRegex": False, "include": [], "includeIsRegex": False, "missingBucket": False, "orderBy": {"columnId": "bytes_col", "type": "column"}, "orderDirection": "desc", "otherBucket": False, "parentFormat": {"id": "terms"}, "size": 5}, "scale": "ordinal", "sourceField": "network.transport"},
                                                "bytes_col": {"customLabel": True, "dataType": "number", "isBucketed": False, "label": "Bytes", "operationType": "sum", "params": {"emptyAsNull": True, "format": {"id": "bytes", "params": {"decimals": 2}}}, "scale": "ratio", "sourceField": "network.bytes"}
                                            },
                                            "incompleteColumns": {}
                                        }
                                    }
                                }
                            },
                            "query": {"language": "kuery", "query": ""},
                            "filters": [],
                            "visualization": {
                                "layers": [{"categoryDisplay": "default", "emptySizeRatio": 0.3, "layerId": "proto", "layerType": "data", "legendDisplay": "show", "legendPosition": "right", "metrics": ["bytes_col"], "nestedLegend": False, "numberDisplay": "percent", "percentDecimals": 2, "primaryGroups": ["proto"], "secondaryGroups": [], "showValuesInLegend": True}],
                                "palette": {"name": "warm", "type": "palette"},
                                "shape": "donut"
                            }
                        },
                        "title": "[Unified Flow] Protocol Distribution",
                        "type": "lens",
                        "visualizationType": "lnsPie"
                    },
                    "enhancements": {},
                    "hidePanelTitles": False
                },
                "gridData": {"h": 16, "i": "5", "w": 16, "x": 32, "y": 19},
                "panelIndex": "5",
                "title": "[Unified Flow] Protocol Distribution",
                "type": "lens",
                "version": "8.9.0"
            },
            {
                "embeddableConfig": {
                    "attributes": {
                        "references": [{"id": "unified-flow-*", "name": "indexpattern-datasource-layer-device-bytes", "type": "index-pattern"}],
                        "state": {
                            "datasourceStates": {
                                "formBased": {
                                    "layers": {
                                        "device-bytes": {
                                            "columnOrder": ["dev", "ts", "bytes_col"],
                                            "columns": {
                                                "dev": {"customLabel": True, "dataType": "string", "isBucketed": True, "label": "Device", "operationType": "terms", "params": {"exclude": [], "excludeIsRegex": False, "include": [], "includeIsRegex": False, "missingBucket": False, "orderBy": {"columnId": "bytes_col", "type": "column"}, "orderDirection": "desc", "otherBucket": False, "parentFormat": {"id": "terms"}, "size": 5}, "scale": "ordinal", "sourceField": "device.name"},
                                                "ts": {"customLabel": True, "dataType": "date", "isBucketed": True, "label": "@timestamp", "operationType": "date_histogram", "params": {"dropPartials": False, "includeEmptyRows": True, "interval": "auto"}, "scale": "interval", "sourceField": "@timestamp"},
                                                "bytes_col": {"customLabel": True, "dataType": "number", "isBucketed": False, "label": "Bytes", "operationType": "sum", "params": {"emptyAsNull": True, "format": {"id": "bytes", "params": {"decimals": 2}}}, "scale": "ratio", "sourceField": "network.bytes"}
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
                                "layers": [{"accessors": ["bytes_col"], "layerId": "device-bytes", "layerType": "data", "seriesType": "area_stacked", "palette": {"name": "rainbow", "type": "palette"}, "splitAccessor": "dev", "xAccessor": "ts"}],
                                "legend": {"isVisible": True, "position": "right"},
                                "preferredSeriesType": "area_stacked",
                                "tickLabelsVisibilitySettings": {"x": True, "yLeft": True, "yRight": True},
                                "valueLabels": "hide"
                            }
                        },
                        "title": "[Unified Flow] Device Traffic by Bytes",
                        "type": "lens",
                        "visualizationType": "lnsXY"
                    },
                    "enhancements": {},
                    "hidePanelTitles": False
                },
                "gridData": {"h": 14, "i": "6", "w": 24, "x": 0, "y": 35},
                "panelIndex": "6",
                "title": "[Unified Flow] Device Traffic by Bytes",
                "type": "lens",
                "version": "8.9.0"
            },
            {
                "embeddableConfig": {
                    "attributes": {
                        "references": [{"id": "unified-flow-*", "name": "indexpattern-datasource-layer-device-packets", "type": "index-pattern"}],
                        "state": {
                            "datasourceStates": {
                                "formBased": {
                                    "layers": {
                                        "device-packets": {
                                            "columnOrder": ["dev", "ts", "packets_col"],
                                            "columns": {
                                                "dev": {"customLabel": True, "dataType": "string", "isBucketed": True, "label": "Device", "operationType": "terms", "params": {"exclude": [], "excludeIsRegex": False, "include": [], "includeIsRegex": False, "missingBucket": False, "orderBy": {"columnId": "packets_col", "type": "column"}, "orderDirection": "desc", "otherBucket": False, "parentFormat": {"id": "terms"}, "size": 5}, "scale": "ordinal", "sourceField": "device.name"},
                                                "ts": {"customLabel": True, "dataType": "date", "isBucketed": True, "label": "@timestamp", "operationType": "date_histogram", "params": {"dropPartials": False, "includeEmptyRows": True, "interval": "auto"}, "scale": "interval", "sourceField": "@timestamp"},
                                                "packets_col": {"customLabel": True, "dataType": "number", "isBucketed": False, "label": "Packets", "operationType": "sum", "params": {"emptyAsNull": True}, "scale": "ratio", "sourceField": "network.packets"}
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
                                "layers": [{"accessors": ["packets_col"], "layerId": "device-packets", "layerType": "data", "seriesType": "area_stacked", "palette": {"name": "ocean", "type": "palette"}, "splitAccessor": "dev", "xAccessor": "ts"}],
                                "legend": {"isVisible": True, "position": "right"},
                                "preferredSeriesType": "area_stacked",
                                "tickLabelsVisibilitySettings": {"x": True, "yLeft": True, "yRight": True},
                                "valueLabels": "hide"
                            }
                        },
                        "title": "[Unified Flow] Device Traffic by Packets",
                        "type": "lens",
                        "visualizationType": "lnsXY"
                    },
                    "enhancements": {},
                    "hidePanelTitles": False
                },
                "gridData": {"h": 14, "i": "7", "w": 24, "x": 24, "y": 35},
                "panelIndex": "7",
                "title": "[Unified Flow] Device Traffic by Packets",
                "type": "lens",
                "version": "8.9.0"
            },
            {
                "embeddableConfig": {
                    "attributes": {
                        "references": [{"id": "unified-flow-*", "name": "indexpattern-datasource-layer-uniq-src", "type": "index-pattern"}],
                        "state": {
                            "datasourceStates": {
                                "formBased": {
                                    "layers": {
                                        "uniq-src": {
                                            "columnOrder": ["uniq"],
                                            "columns": {
                                                "uniq": {"customLabel": True, "dataType": "number", "isBucketed": False, "label": "Unique Sources", "operationType": "unique_count", "params": {"emptyAsNull": True}, "scale": "ratio", "sourceField": "source.ip"}
                                            },
                                            "incompleteColumns": {}
                                        }
                                    }
                                }
                            },
                            "query": {"language": "kuery", "query": ""},
                            "filters": [],
                            "visualization": {"color": "#54B399", "layerId": "uniq-src", "layerType": "data", "metricAccessor": "uniq"}
                        },
                        "title": "[Unified Flow] Unique Sources",
                        "type": "lens",
                        "visualizationType": "lnsMetric"
                    },
                    "enhancements": {},
                    "hidePanelTitles": False
                },
                "gridData": {"h": 10, "i": "8", "w": 12, "x": 0, "y": 49},
                "panelIndex": "8",
                "title": "[Unified Flow] Unique Sources",
                "type": "lens",
                "version": "8.9.0"
            },
            {
                "embeddableConfig": {
                    "attributes": {
                        "references": [{"id": "unified-flow-*", "name": "indexpattern-datasource-layer-uniq-dst", "type": "index-pattern"}],
                        "state": {
                            "datasourceStates": {
                                "formBased": {
                                    "layers": {
                                        "uniq-dst": {
                                            "columnOrder": ["uniq"],
                                            "columns": {
                                                "uniq": {"customLabel": True, "dataType": "number", "isBucketed": False, "label": "Unique Destinations", "operationType": "unique_count", "params": {"emptyAsNull": True}, "scale": "ratio", "sourceField": "destination.ip"}
                                            },
                                            "incompleteColumns": {}
                                        }
                                    }
                                }
                            },
                            "query": {"language": "kuery", "query": ""},
                            "filters": [],
                            "visualization": {"color": "#D36086", "layerId": "uniq-dst", "layerType": "data", "metricAccessor": "uniq"}
                        },
                        "title": "[Unified Flow] Unique Destinations",
                        "type": "lens",
                        "visualizationType": "lnsMetric"
                    },
                    "enhancements": {},
                    "hidePanelTitles": False
                },
                "gridData": {"h": 10, "i": "9", "w": 12, "x": 12, "y": 49},
                "panelIndex": "9",
                "title": "[Unified Flow] Unique Destinations",
                "type": "lens",
                "version": "8.9.0"
            },
            {
                "embeddableConfig": {
                    "attributes": {
                        "references": [{"id": "unified-flow-*", "name": "indexpattern-datasource-layer-sp", "type": "index-pattern"}],
                        "state": {
                            "datasourceStates": {
                                "formBased": {
                                    "layers": {
                                        "sp": {
                                            "columnOrder": ["uniq"],
                                            "columns": {
                                                "uniq": {"customLabel": True, "dataType": "number", "isBucketed": False, "label": "Source Ports", "operationType": "unique_count", "params": {"emptyAsNull": True}, "scale": "ratio", "sourceField": "source.port"}
                                            },
                                            "incompleteColumns": {}
                                        }
                                    }
                                }
                            },
                            "query": {"language": "kuery", "query": ""},
                            "filters": [],
                            "visualization": {"color": "#9170B8", "layerId": "sp", "layerType": "data", "metricAccessor": "uniq"}
                        },
                        "title": "[Unified Flow] Source Ports",
                        "type": "lens",
                        "visualizationType": "lnsMetric"
                    },
                    "enhancements": {},
                    "hidePanelTitles": False
                },
                "gridData": {"h": 10, "i": "10", "w": 12, "x": 24, "y": 49},
                "panelIndex": "10",
                "title": "[Unified Flow] Source Ports",
                "type": "lens",
                "version": "8.9.0"
            },
            {
                "embeddableConfig": {
                    "attributes": {
                        "references": [{"id": "unified-flow-*", "name": "indexpattern-datasource-layer-dp", "type": "index-pattern"}],
                        "state": {
                            "datasourceStates": {
                                "formBased": {
                                    "layers": {
                                        "dp": {
                                            "columnOrder": ["uniq"],
                                            "columns": {
                                                "uniq": {"customLabel": True, "dataType": "number", "isBucketed": False, "label": "Destination Ports", "operationType": "unique_count", "params": {"emptyAsNull": True}, "scale": "ratio", "sourceField": "destination.port"}
                                            },
                                            "incompleteColumns": {}
                                        }
                                    }
                                }
                            },
                            "query": {"language": "kuery", "query": ""},
                            "filters": [],
                            "visualization": {"color": "#CA8E00", "layerId": "dp", "layerType": "data", "metricAccessor": "uniq"}
                        },
                        "title": "[Unified Flow] Destination Ports",
                        "type": "lens",
                        "visualizationType": "lnsMetric"
                    },
                    "enhancements": {},
                    "hidePanelTitles": False
                },
                "gridData": {"h": 10, "i": "11", "w": 12, "x": 36, "y": 49},
                "panelIndex": "11",
                "title": "[Unified Flow] Destination Ports",
                "type": "lens",
                "version": "8.9.0"
            }
        ]),
        "refreshInterval": {"pause": False, "value": 15000},
        "timeRestore": True,
        "timeFrom": "now-15m",
        "timeTo": "now",
        "title": "[Unified Flow] Detailed Traffic Analysis"
    },
    "coreMigrationVersion": "8.8.0",
    "created_at": "2026-02-11T14:30:00Z",
    "id": "unified-flow-detailed-dashboard",
    "managed": False,
    "references": [{"id": "unified-flow-*", "name": "index-pattern", "type": "index-pattern"}],
    "type": "dashboard",
    "typeMigrationVersion": "10.3.0",
    "updated_at": "2026-02-11T14:30:00Z",
    "version": "WzE1MCwxXQ=="
}

# Dashboard 2: Top-N Analysis
dashboard_2 = {
    "attributes": {
        "description": "Unified Flow Top-N Analysis - Top Sources, Destinations, Ports, Protocols, and AS",
        "kibanaSavedObjectMeta": {
            "searchSourceJSON": json.dumps({"filter": [], "query": {"language": "kuery", "query": ""}})
        },
        "optionsJSON": json.dumps({"hidePanelTitles": False, "syncColors": False, "syncCursor": True, "syncTooltips": False, "useMargins": True}),
        "panelsJSON": json.dumps([
            {
                "embeddableConfig": {
                    "attributes": {
                        "references": [{"id": "unified-flow-*", "name": "indexpattern-datasource-layer-src", "type": "index-pattern"}],
                        "state": {
                            "datasourceStates": {
                                "formBased": {
                                    "layers": {
                                        "src": {
                                            "columnOrder": ["src_ip", "bytes", "packets", "flows"],
                                            "columns": {
                                                "src_ip": {"customLabel": True, "dataType": "ip", "isBucketed": True, "label": "Source", "operationType": "terms", "params": {"exclude": [], "excludeIsRegex": False, "include": [], "includeIsRegex": False, "missingBucket": False, "orderBy": {"columnId": "bytes", "type": "column"}, "orderDirection": "desc", "otherBucket": False, "parentFormat": {"id": "terms"}, "size": 500}, "scale": "ordinal", "sourceField": "source.ip"},
                                                "bytes": {"customLabel": True, "dataType": "number", "isBucketed": False, "label": "Bytes", "operationType": "sum", "params": {"emptyAsNull": True, "format": {"id": "bytes", "params": {"decimals": 2}}}, "scale": "ratio", "sourceField": "network.bytes"},
                                                "packets": {"customLabel": True, "dataType": "number", "isBucketed": False, "label": "Packets", "operationType": "sum", "params": {"emptyAsNull": True}, "scale": "ratio", "sourceField": "network.packets"},
                                                "flows": {"customLabel": True, "dataType": "number", "isBucketed": False, "label": "Flows", "operationType": "count", "params": {"emptyAsNull": True}, "scale": "ratio", "sourceField": "___records___"}
                                            },
                                            "incompleteColumns": {}
                                        }
                                    }
                                }
                            },
                            "internalReferences": [],
                            "query": {"language": "kuery", "query": ""},
                            "visualization": {
                                "columns": [
                                    {"alignment": "left", "columnId": "bytes", "summaryRow": "sum"},
                                    {"alignment": "left", "columnId": "packets", "summaryRow": "sum"},
                                    {"alignment": "left", "columnId": "flows", "summaryRow": "sum"},
                                    {"alignment": "left", "columnId": "src_ip"}
                                ],
                                "headerRowHeight": "single",
                                "layerId": "src",
                                "layerType": "data",
                                "paging": {"enabled": True, "size": 10},
                                "rowHeight": "single"
                            }
                        },
                        "title": "[Unified Flow] Top Sources",
                        "type": "lens",
                        "visualizationType": "lnsDatatable"
                    },
                    "enhancements": {},
                    "hidePanelTitles": False
                },
                "gridData": {"h": 20, "i": "1", "w": 24, "x": 0, "y": 4},
                "panelIndex": "1",
                "title": "[Unified Flow] Top Sources",
                "type": "lens",
                "version": "8.9.0"
            },
            {
                "embeddableConfig": {
                    "attributes": {
                        "references": [{"id": "unified-flow-*", "name": "indexpattern-datasource-layer-dst", "type": "index-pattern"}],
                        "state": {
                            "datasourceStates": {
                                "formBased": {
                                    "layers": {
                                        "dst": {
                                            "columnOrder": ["dst_ip", "bytes", "packets", "flows"],
                                            "columns": {
                                                "dst_ip": {"customLabel": True, "dataType": "ip", "isBucketed": True, "label": "Destination", "operationType": "terms", "params": {"exclude": [], "excludeIsRegex": False, "include": [], "includeIsRegex": False, "missingBucket": False, "orderBy": {"columnId": "bytes", "type": "column"}, "orderDirection": "desc", "otherBucket": False, "parentFormat": {"id": "terms"}, "size": 500}, "scale": "ordinal", "sourceField": "destination.ip"},
                                                "bytes": {"customLabel": True, "dataType": "number", "isBucketed": False, "label": "Bytes", "operationType": "sum", "params": {"emptyAsNull": True, "format": {"id": "bytes", "params": {"decimals": 2}}}, "scale": "ratio", "sourceField": "network.bytes"},
                                                "packets": {"customLabel": True, "dataType": "number", "isBucketed": False, "label": "Packets", "operationType": "sum", "params": {"emptyAsNull": True}, "scale": "ratio", "sourceField": "network.packets"},
                                                "flows": {"customLabel": True, "dataType": "number", "isBucketed": False, "label": "Flows", "operationType": "count", "params": {"emptyAsNull": True}, "scale": "ratio", "sourceField": "___records___"}
                                            },
                                            "incompleteColumns": {}
                                        }
                                    }
                                }
                            },
                            "internalReferences": [],
                            "query": {"language": "kuery", "query": ""},
                            "visualization": {
                                "columns": [
                                    {"alignment": "left", "columnId": "bytes", "summaryRow": "sum"},
                                    {"alignment": "left", "columnId": "packets", "summaryRow": "sum"},
                                    {"alignment": "left", "columnId": "flows", "summaryRow": "sum"},
                                    {"alignment": "left", "columnId": "dst_ip"}
                                ],
                                "headerRowHeight": "single",
                                "layerId": "dst",
                                "layerType": "data",
                                "paging": {"enabled": True, "size": 10},
                                "rowHeight": "single"
                            }
                        },
                        "title": "[Unified Flow] Top Destinations",
                        "type": "lens",
                        "visualizationType": "lnsDatatable"
                    },
                    "enhancements": {},
                    "hidePanelTitles": False
                },
                "gridData": {"h": 20, "i": "2", "w": 24, "x": 24, "y": 4},
                "panelIndex": "2",
                "title": "[Unified Flow] Top Destinations",
                "type": "lens",
                "version": "8.9.0"
            },
            {
                "embeddableConfig": {
                    "attributes": {
                        "references": [{"id": "unified-flow-*", "name": "indexpattern-datasource-layer-sport", "type": "index-pattern"}],
                        "state": {
                            "datasourceStates": {
                                "formBased": {
                                    "layers": {
                                        "sport": {
                                            "columnOrder": ["sport", "bytes", "packets", "flows"],
                                            "columns": {
                                                "sport": {"customLabel": True, "dataType": "number", "isBucketed": True, "label": "Source Port", "operationType": "terms", "params": {"exclude": [], "excludeIsRegex": False, "include": [], "includeIsRegex": False, "missingBucket": False, "orderBy": {"columnId": "bytes", "type": "column"}, "orderDirection": "desc", "otherBucket": False, "parentFormat": {"id": "terms"}, "size": 500}, "scale": "ordinal", "sourceField": "source.port"},
                                                "bytes": {"customLabel": True, "dataType": "number", "isBucketed": False, "label": "Bytes", "operationType": "sum", "params": {"emptyAsNull": True, "format": {"id": "bytes", "params": {"decimals": 2}}}, "scale": "ratio", "sourceField": "network.bytes"},
                                                "packets": {"customLabel": True, "dataType": "number", "isBucketed": False, "label": "Packets", "operationType": "sum", "params": {"emptyAsNull": True}, "scale": "ratio", "sourceField": "network.packets"},
                                                "flows": {"customLabel": True, "dataType": "number", "isBucketed": False, "label": "Flows", "operationType": "count", "params": {"emptyAsNull": True}, "scale": "ratio", "sourceField": "___records___"}
                                            },
                                            "incompleteColumns": {}
                                        }
                                    }
                                }
                            },
                            "internalReferences": [],
                            "query": {"language": "kuery", "query": ""},
                            "visualization": {
                                "columns": [
                                    {"alignment": "left", "columnId": "bytes", "summaryRow": "sum"},
                                    {"alignment": "left", "columnId": "packets", "summaryRow": "sum"},
                                    {"alignment": "left", "columnId": "flows", "summaryRow": "sum"},
                                    {"alignment": "left", "columnId": "sport"}
                                ],
                                "headerRowHeight": "single",
                                "layerId": "sport",
                                "layerType": "data",
                                "paging": {"enabled": True, "size": 10},
                                "rowHeight": "single"
                            }
                        },
                        "title": "[Unified Flow] Top Source Ports",
                        "type": "lens",
                        "visualizationType": "lnsDatatable"
                    },
                    "enhancements": {},
                    "hidePanelTitles": False
                },
                "gridData": {"h": 20, "i": "3", "w": 24, "x": 0, "y": 24},
                "panelIndex": "3",
                "title": "[Unified Flow] Top Source Ports",
                "type": "lens",
                "version": "8.9.0"
            },
            {
                "embeddableConfig": {
                    "attributes": {
                        "references": [{"id": "unified-flow-*", "name": "indexpattern-datasource-layer-dport", "type": "index-pattern"}],
                        "state": {
                            "datasourceStates": {
                                "formBased": {
                                    "layers": {
                                        "dport": {
                                            "columnOrder": ["dport", "bytes", "packets", "flows"],
                                            "columns": {
                                                "dport": {"customLabel": True, "dataType": "number", "isBucketed": True, "label": "Destination Port", "operationType": "terms", "params": {"exclude": [], "excludeIsRegex": False, "include": [], "includeIsRegex": False, "missingBucket": False, "orderBy": {"columnId": "bytes", "type": "column"}, "orderDirection": "desc", "otherBucket": False, "parentFormat": {"id": "terms"}, "size": 500}, "scale": "ordinal", "sourceField": "destination.port"},
                                                "bytes": {"customLabel": True, "dataType": "number", "isBucketed": False, "label": "Bytes", "operationType": "sum", "params": {"emptyAsNull": True, "format": {"id": "bytes", "params": {"decimals": 2}}}, "scale": "ratio", "sourceField": "network.bytes"},
                                                "packets": {"customLabel": True, "dataType": "number", "isBucketed": False, "label": "Packets", "operationType": "sum", "params": {"emptyAsNull": True}, "scale": "ratio", "sourceField": "network.packets"},
                                                "flows": {"customLabel": True, "dataType": "number", "isBucketed": False, "label": "Flows", "operationType": "count", "params": {"emptyAsNull": True}, "scale": "ratio", "sourceField": "___records___"}
                                            },
                                            "incompleteColumns": {}
                                        }
                                    }
                                }
                            },
                            "internalReferences": [],
                            "query": {"language": "kuery", "query": ""},
                            "visualization": {
                                "columns": [
                                    {"alignment": "left", "columnId": "bytes", "summaryRow": "sum"},
                                    {"alignment": "left", "columnId": "packets", "summaryRow": "sum"},
                                    {"alignment": "left", "columnId": "flows", "summaryRow": "sum"},
                                    {"alignment": "left", "columnId": "dport"}
                                ],
                                "headerRowHeight": "single",
                                "layerId": "dport",
                                "layerType": "data",
                                "paging": {"enabled": True, "size": 10},
                                "rowHeight": "single"
                            }
                        },
                        "title": "[Unified Flow] Top Destination Ports",
                        "type": "lens",
                        "visualizationType": "lnsDatatable"
                    },
                    "enhancements": {},
                    "hidePanelTitles": False
                },
                "gridData": {"h": 20, "i": "4", "w": 24, "x": 24, "y": 24},
                "panelIndex": "4",
                "title": "[Unified Flow] Top Destination Ports",
                "type": "lens",
                "version": "8.9.0"
            },
            {
                "embeddableConfig": {
                    "attributes": {
                        "references": [{"id": "unified-flow-*", "name": "indexpattern-datasource-layer-proto", "type": "index-pattern"}],
                        "state": {
                            "datasourceStates": {
                                "formBased": {
                                    "layers": {
                                        "proto": {
                                            "columnOrder": ["proto", "bytes", "packets", "flows"],
                                            "columns": {
                                                "proto": {"customLabel": True, "dataType": "string", "isBucketed": True, "label": "Protocol", "operationType": "terms", "params": {"exclude": [], "excludeIsRegex": False, "include": [], "includeIsRegex": False, "missingBucket": False, "orderBy": {"columnId": "bytes", "type": "column"}, "orderDirection": "desc", "otherBucket": False, "parentFormat": {"id": "terms"}, "size": 500}, "scale": "ordinal", "sourceField": "network.transport"},
                                                "bytes": {"customLabel": True, "dataType": "number", "isBucketed": False, "label": "Bytes", "operationType": "sum", "params": {"emptyAsNull": True}, "scale": "ratio", "sourceField": "network.bytes"},
                                                "packets": {"customLabel": True, "dataType": "number", "isBucketed": False, "label": "Packets", "operationType": "sum", "params": {"emptyAsNull": True}, "scale": "ratio", "sourceField": "network.packets"},
                                                "flows": {"customLabel": True, "dataType": "number", "isBucketed": False, "label": "Flows", "operationType": "count", "params": {"emptyAsNull": True}, "scale": "ratio", "sourceField": "___records___"}
                                            },
                                            "incompleteColumns": {}
                                        }
                                    }
                                }
                            },
                            "internalReferences": [],
                            "query": {"language": "kuery", "query": ""},
                            "visualization": {
                                "columns": [
                                    {"alignment": "left", "columnId": "bytes", "summaryRow": "sum"},
                                    {"alignment": "left", "columnId": "packets", "summaryRow": "sum"},
                                    {"alignment": "left", "columnId": "flows", "summaryRow": "sum"},
                                    {"alignment": "left", "columnId": "proto"}
                                ],
                                "headerRowHeight": "single",
                                "layerId": "proto",
                                "layerType": "data",
                                "paging": {"enabled": True, "size": 10},
                                "rowHeight": "single"
                            }
                        },
                        "title": "[Unified Flow] Top Protocols",
                        "type": "lens",
                        "visualizationType": "lnsDatatable"
                    },
                    "enhancements": {},
                    "hidePanelTitles": False
                },
                "gridData": {"h": 20, "i": "5", "w": 24, "x": 0, "y": 44},
                "panelIndex": "5",
                "title": "[Unified Flow] Top Protocols",
                "type": "lens",
                "version": "8.9.0"
            },
            {
                "embeddableConfig": {
                    "attributes": {
                        "references": [{"id": "unified-flow-*", "name": "indexpattern-datasource-layer-device", "type": "index-pattern"}],
                        "state": {
                            "datasourceStates": {
                                "formBased": {
                                    "layers": {
                                        "device": {
                                            "columnOrder": ["device", "bytes", "packets", "flows"],
                                            "columns": {
                                                "device": {"customLabel": True, "dataType": "string", "isBucketed": True, "label": "Device", "operationType": "terms", "params": {"exclude": [], "excludeIsRegex": False, "include": [], "includeIsRegex": False, "missingBucket": False, "orderBy": {"columnId": "bytes", "type": "column"}, "orderDirection": "desc", "otherBucket": False, "parentFormat": {"id": "terms"}, "size": 500}, "scale": "ordinal", "sourceField": "device.name"},
                                                "bytes": {"customLabel": True, "dataType": "number", "isBucketed": False, "label": "Bytes", "operationType": "sum", "params": {"emptyAsNull": True}, "scale": "ratio", "sourceField": "network.bytes"},
                                                "packets": {"customLabel": True, "dataType": "number", "isBucketed": False, "label": "Packets", "operationType": "sum", "params": {"emptyAsNull": True}, "scale": "ratio", "sourceField": "network.packets"},
                                                "flows": {"customLabel": True, "dataType": "number", "isBucketed": False, "label": "Flows", "operationType": "count", "params": {"emptyAsNull": True}, "scale": "ratio", "sourceField": "___records___"}
                                            },
                                            "incompleteColumns": {}
                                        }
                                    }
                                }
                            },
                            "internalReferences": [],
                            "query": {"language": "kuery", "query": ""},
                            "visualization": {
                                "columns": [
                                    {"alignment": "left", "columnId": "bytes", "summaryRow": "sum"},
                                    {"alignment": "left", "columnId": "packets", "summaryRow": "sum"},
                                    {"alignment": "left", "columnId": "flows", "summaryRow": "sum"},
                                    {"alignment": "left", "columnId": "device"}
                                ],
                                "headerRowHeight": "single",
                                "layerId": "device",
                                "layerType": "data",
                                "paging": {"enabled": True, "size": 10},
                                "rowHeight": "single"
                            }
                        },
                        "title": "[Unified Flow] Top Devices",
                        "type": "lens",
                        "visualizationType": "lnsDatatable"
                    },
                    "enhancements": {},
                    "hidePanelTitles": False
                },
                "gridData": {"h": 20, "i": "6", "w": 24, "x": 24, "y": 44},
                "panelIndex": "6",
                "title": "[Unified Flow] Top Devices",
                "type": "lens",
                "version": "8.9.0"
            },
            {
                "embeddableConfig": {
                    "attributes": {
                        "references": [{"id": "unified-flow-*", "name": "indexpattern-datasource-layer-sas", "type": "index-pattern"}],
                        "state": {
                            "datasourceStates": {
                                "formBased": {
                                    "layers": {
                                        "sas": {
                                            "columnOrder": ["sas", "bytes", "packets", "flows"],
                                            "columns": {
                                                "sas": {"customLabel": True, "dataType": "number", "isBucketed": True, "label": "Source AS", "operationType": "terms", "params": {"exclude": [], "excludeIsRegex": False, "include": [], "includeIsRegex": False, "missingBucket": False, "orderBy": {"columnId": "bytes", "type": "column"}, "orderDirection": "desc", "otherBucket": False, "parentFormat": {"id": "terms"}, "size": 500}, "scale": "ordinal", "sourceField": "source.as.number"},
                                                "bytes": {"customLabel": True, "dataType": "number", "isBucketed": False, "label": "Bytes", "operationType": "sum", "params": {"emptyAsNull": True}, "scale": "ratio", "sourceField": "network.bytes"},
                                                "packets": {"customLabel": True, "dataType": "number", "isBucketed": False, "label": "Packets", "operationType": "sum", "params": {"emptyAsNull": True}, "scale": "ratio", "sourceField": "network.packets"},
                                                "flows": {"customLabel": True, "dataType": "number", "isBucketed": False, "label": "Flows", "operationType": "count", "params": {"emptyAsNull": True}, "scale": "ratio", "sourceField": "___records___"}
                                            },
                                            "incompleteColumns": {}
                                        }
                                    }
                                }
                            },
                            "internalReferences": [],
                            "query": {"language": "kuery", "query": ""},
                            "visualization": {
                                "columns": [
                                    {"alignment": "left", "columnId": "bytes", "summaryRow": "sum"},
                                    {"alignment": "left", "columnId": "packets", "summaryRow": "sum"},
                                    {"alignment": "left", "columnId": "flows", "summaryRow": "sum"},
                                    {"alignment": "left", "columnId": "sas"}
                                ],
                                "headerRowHeight": "single",
                                "layerId": "sas",
                                "layerType": "data",
                                "paging": {"enabled": True, "size": 10},
                                "rowHeight": "single"
                            }
                        },
                        "title": "[Unified Flow] Top Source AS",
                        "type": "lens",
                        "visualizationType": "lnsDatatable"
                    },
                    "enhancements": {},
                    "hidePanelTitles": False
                },
                "gridData": {"h": 20, "i": "7", "w": 24, "x": 0, "y": 64},
                "panelIndex": "7",
                "title": "[Unified Flow] Top Source AS",
                "type": "lens",
                "version": "8.9.0"
            },
            {
                "embeddableConfig": {
                    "attributes": {
                        "references": [{"id": "unified-flow-*", "name": "indexpattern-datasource-layer-das", "type": "index-pattern"}],
                        "state": {
                            "datasourceStates": {
                                "formBased": {
                                    "layers": {
                                        "das": {
                                            "columnOrder": ["das", "bytes", "packets", "flows"],
                                            "columns": {
                                                "das": {"customLabel": True, "dataType": "number", "isBucketed": True, "label": "Destination AS", "operationType": "terms", "params": {"exclude": [], "excludeIsRegex": False, "include": [], "includeIsRegex": False, "missingBucket": False, "orderBy": {"columnId": "bytes", "type": "column"}, "orderDirection": "desc", "otherBucket": False, "parentFormat": {"id": "terms"}, "size": 500}, "scale": "ordinal", "sourceField": "destination.as.number"},
                                                "bytes": {"customLabel": True, "dataType": "number", "isBucketed": False, "label": "Bytes", "operationType": "sum", "params": {"emptyAsNull": True}, "scale": "ratio", "sourceField": "network.bytes"},
                                                "packets": {"customLabel": True, "dataType": "number", "isBucketed": False, "label": "Packets", "operationType": "sum", "params": {"emptyAsNull": True}, "scale": "ratio", "sourceField": "network.packets"},
                                                "flows": {"customLabel": True, "dataType": "number", "isBucketed": False, "label": "Flows", "operationType": "count", "params": {"emptyAsNull": True}, "scale": "ratio", "sourceField": "___records___"}
                                            },
                                            "incompleteColumns": {}
                                        }
                                    }
                                }
                            },
                            "internalReferences": [],
                            "query": {"language": "kuery", "query": ""},
                            "visualization": {
                                "columns": [
                                    {"alignment": "left", "columnId": "bytes", "summaryRow": "sum"},
                                    {"alignment": "left", "columnId": "packets", "summaryRow": "sum"},
                                    {"alignment": "left", "columnId": "flows", "summaryRow": "sum"},
                                    {"alignment": "left", "columnId": "das"}
                                ],
                                "headerRowHeight": "single",
                                "layerId": "das",
                                "layerType": "data",
                                "paging": {"enabled": True, "size": 10},
                                "rowHeight": "single"
                            }
                        },
                        "title": "[Unified Flow] Top Destination AS",
                        "type": "lens",
                        "visualizationType": "lnsDatatable"
                    },
                    "enhancements": {},
                    "hidePanelTitles": False
                },
                "gridData": {"h": 20, "i": "8", "w": 24, "x": 24, "y": 64},
                "panelIndex": "8",
                "title": "[Unified Flow] Top Destination AS",
                "type": "lens",
                "version": "8.9.0"
            }
        ]),
        "refreshInterval": {"pause": False, "value": 15000},
        "timeRestore": True,
        "timeFrom": "now-15m",
        "timeTo": "now",
        "title": "[Unified Flow] Top-N Analysis"
    },
    "coreMigrationVersion": "8.8.0",
    "created_at": "2026-02-11T14:30:00Z",
    "id": "unified-flow-top-n",
    "managed": False,
    "references": [{"id": "unified-flow-*", "name": "index-pattern", "type": "index-pattern"}],
    "type": "dashboard",
    "typeMigrationVersion": "10.3.0",
    "updated_at": "2026-02-11T14:30:00Z",
    "version": "WzE2MCwxXQ=="
}

# Dashboard 3: Conversation Partners
dashboard_3 = {
    "attributes": {
        "description": "Unified Flow Conversation Partners - Source/Destination pairs, connection analysis with device timeline",
        "kibanaSavedObjectMeta": {
            "searchSourceJSON": json.dumps({"filter": [], "query": {"language": "kuery", "query": ""}})
        },
        "optionsJSON": json.dumps({"hidePanelTitles": False, "syncColors": False, "syncCursor": True, "syncTooltips": False, "useMargins": True}),
        "panelsJSON": json.dumps([
            {
                "embeddableConfig": {
                    "attributes": {
                        "references": [{"id": "unified-flow-*", "name": "indexpattern-datasource-layer-conv", "type": "index-pattern"}],
                        "state": {
                            "datasourceStates": {
                                "formBased": {
                                    "layers": {
                                        "conv": {
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
                            "internalReferences": [],
                            "query": {"language": "kuery", "query": ""},
                            "visualization": {
                                "columns": [
                                    {"alignment": "left", "columnId": "bytes"},
                                    {"alignment": "left", "columnId": "packets"},
                                    {"alignment": "left", "columnId": "flows"},
                                    {"alignment": "left", "columnId": "src"},
                                    {"alignment": "left", "columnId": "dst"}
                                ],
                                "headerRowHeight": "single",
                                "layerId": "conv",
                                "layerType": "data",
                                "paging": {"enabled": True, "size": 10},
                                "rowHeight": "single"
                            }
                        },
                        "title": "[Unified Flow] Conversation Partners",
                        "type": "lens",
                        "visualizationType": "lnsDatatable"
                    },
                    "enhancements": {},
                    "hidePanelTitles": False
                },
                "gridData": {"h": 24, "i": "1", "w": 48, "x": 0, "y": 4},
                "panelIndex": "1",
                "title": "[Unified Flow] Conversation Partners",
                "type": "lens",
                "version": "8.9.0"
            },
            {
                "embeddableConfig": {
                    "attributes": {
                        "references": [{"id": "unified-flow-*", "name": "indexpattern-datasource-layer-proto", "type": "index-pattern"}],
                        "state": {
                            "datasourceStates": {
                                "formBased": {
                                    "layers": {
                                        "proto": {
                                            "columnOrder": ["ipver", "protocol", "bytes"],
                                            "columns": {
                                                "ipver": {"customLabel": True, "dataType": "string", "isBucketed": True, "label": "IP Version", "operationType": "terms", "params": {"exclude": [], "excludeIsRegex": False, "include": [], "includeIsRegex": False, "missingBucket": True, "orderBy": {"columnId": "bytes", "type": "column"}, "orderDirection": "desc", "otherBucket": False, "parentFormat": {"id": "terms"}, "size": 5}, "scale": "ordinal", "sourceField": "network.type"},
                                                "protocol": {"customLabel": True, "dataType": "string", "isBucketed": True, "label": "Protocol", "operationType": "terms", "params": {"exclude": [], "excludeIsRegex": False, "include": [], "includeIsRegex": False, "missingBucket": False, "orderBy": {"columnId": "bytes", "type": "column"}, "orderDirection": "desc", "otherBucket": False, "parentFormat": {"id": "terms"}, "size": 50}, "scale": "ordinal", "sourceField": "network.transport"},
                                                "bytes": {"customLabel": True, "dataType": "number", "isBucketed": False, "label": "Bytes", "operationType": "sum", "params": {"emptyAsNull": True, "format": {"id": "bytes", "params": {"decimals": 2}}}, "scale": "ratio", "sourceField": "network.bytes"}
                                            },
                                            "incompleteColumns": {}
                                        }
                                    }
                                }
                            },
                            "internalReferences": [],
                            "query": {"language": "kuery", "query": ""},
                            "visualization": {
                                "layers": [{"categoryDisplay": "default", "emptySizeRatio": 0.3, "layerId": "proto", "layerType": "data", "legendDisplay": "show", "legendPosition": "right", "metrics": ["bytes"], "nestedLegend": False, "numberDisplay": "percent", "percentDecimals": 2, "primaryGroups": ["ipver", "protocol"], "secondaryGroups": [], "showValuesInLegend": True}],
                                "palette": {"name": "kibana_palette", "type": "palette"},
                                "shape": "donut"
                            }
                        },
                        "title": "[Unified Flow] Protocol Distribution",
                        "type": "lens",
                        "visualizationType": "lnsPie"
                    },
                    "enhancements": {},
                    "hidePanelTitles": False
                },
                "gridData": {"h": 18, "i": "2", "w": 16, "x": 0, "y": 28},
                "panelIndex": "2",
                "title": "[Unified Flow] IP Version & Protocol",
                "type": "lens",
                "version": "8.9.0"
            },
            {
                "embeddableConfig": {
                    "attributes": {
                        "references": [{"id": "unified-flow-*", "name": "indexpattern-datasource-layer-ports", "type": "index-pattern"}],
                        "state": {
                            "datasourceStates": {
                                "formBased": {
                                    "layers": {
                                        "ports": {
                                            "columnOrder": ["sport", "dport", "bytes"],
                                            "columns": {
                                                "sport": {"customLabel": True, "dataType": "number", "isBucketed": True, "label": "Source Port", "operationType": "terms", "params": {"exclude": [], "excludeIsRegex": False, "include": [], "includeIsRegex": False, "missingBucket": False, "orderBy": {"columnId": "bytes", "type": "column"}, "orderDirection": "desc", "otherBucket": False, "parentFormat": {"id": "terms"}, "size": 10}, "scale": "ordinal", "sourceField": "source.port"},
                                                "dport": {"customLabel": True, "dataType": "number", "isBucketed": True, "label": "Dest Port", "operationType": "terms", "params": {"exclude": [], "excludeIsRegex": False, "include": [], "includeIsRegex": False, "missingBucket": False, "orderBy": {"columnId": "bytes", "type": "column"}, "orderDirection": "desc", "otherBucket": False, "parentFormat": {"id": "terms"}, "size": 10}, "scale": "ordinal", "sourceField": "destination.port"},
                                                "bytes": {"customLabel": True, "dataType": "number", "isBucketed": False, "label": "Bytes", "operationType": "sum", "params": {"emptyAsNull": True, "format": {"id": "bytes", "params": {"decimals": 2}}}, "scale": "ratio", "sourceField": "network.bytes"}
                                            },
                                            "incompleteColumns": {}
                                        }
                                    }
                                }
                            },
                            "internalReferences": [],
                            "query": {"language": "kuery", "query": ""},
                            "visualization": {
                                "layers": [{"categoryDisplay": "default", "emptySizeRatio": 0.3, "layerId": "ports", "layerType": "data", "legendDisplay": "hide", "legendPosition": "right", "metrics": ["bytes"], "nestedLegend": False, "numberDisplay": "percent", "percentDecimals": 2, "primaryGroups": ["sport", "dport"], "secondaryGroups": [], "showValuesInLegend": True}],
                                "palette": {"name": "cool", "type": "palette"},
                                "shape": "donut"
                            }
                        },
                        "title": "[Unified Flow] Source/Dest Ports",
                        "type": "lens",
                        "visualizationType": "lnsPie"
                    },
                    "enhancements": {},
                    "hidePanelTitles": False
                },
                "gridData": {"h": 18, "i": "3", "w": 16, "x": 16, "y": 28},
                "panelIndex": "3",
                "title": "[Unified Flow] Port Pairs",
                "type": "lens",
                "version": "8.9.0"
            },
            {
                "embeddableConfig": {
                    "attributes": {
                        "references": [{"id": "unified-flow-*", "name": "indexpattern-datasource-layer-pair", "type": "index-pattern"}],
                        "state": {
                            "datasourceStates": {
                                "formBased": {
                                    "layers": {
                                        "pair": {
                                            "columnOrder": ["src", "dst", "bytes"],
                                            "columns": {
                                                "src": {"customLabel": True, "dataType": "ip", "isBucketed": True, "label": "Source", "operationType": "terms", "params": {"exclude": [], "excludeIsRegex": False, "include": [], "includeIsRegex": False, "missingBucket": False, "orderBy": {"columnId": "bytes", "type": "column"}, "orderDirection": "desc", "otherBucket": False, "parentFormat": {"id": "terms"}, "size": 10}, "scale": "ordinal", "sourceField": "source.ip"},
                                                "dst": {"customLabel": True, "dataType": "ip", "isBucketed": True, "label": "Destination", "operationType": "terms", "params": {"exclude": [], "excludeIsRegex": False, "include": [], "includeIsRegex": False, "missingBucket": False, "orderBy": {"columnId": "bytes", "type": "column"}, "orderDirection": "desc", "otherBucket": False, "parentFormat": {"id": "terms"}, "size": 10}, "scale": "ordinal", "sourceField": "destination.ip"},
                                                "bytes": {"customLabel": True, "dataType": "number", "isBucketed": False, "label": "Bytes", "operationType": "sum", "params": {"emptyAsNull": True, "format": {"id": "bytes", "params": {"decimals": 2}}}, "scale": "ratio", "sourceField": "network.bytes"}
                                            },
                                            "incompleteColumns": {}
                                        }
                                    }
                                }
                            },
                            "internalReferences": [],
                            "query": {"language": "kuery", "query": ""},
                            "visualization": {
                                "layers": [{"categoryDisplay": "default", "emptySizeRatio": 0.3, "layerId": "pair", "layerType": "data", "legendDisplay": "show", "legendPosition": "right", "metrics": ["bytes"], "nestedLegend": False, "numberDisplay": "percent", "percentDecimals": 2, "primaryGroups": ["src", "dst"], "secondaryGroups": [], "showValuesInLegend": True}],
                                "palette": {"name": "temperature", "type": "palette"},
                                "shape": "donut"
                            }
                        },
                        "title": "[Unified Flow] Source-Dest Distribution",
                        "type": "lens",
                        "visualizationType": "lnsPie"
                    },
                    "enhancements": {},
                    "hidePanelTitles": False
                },
                "gridData": {"h": 18, "i": "4", "w": 16, "x": 32, "y": 28},
                "panelIndex": "4",
                "title": "[Unified Flow] Top Src-Dst Pairs",
                "type": "lens",
                "version": "8.9.0"
            },
            {
                "embeddableConfig": {
                    "attributes": {
                        "references": [{"id": "unified-flow-*", "name": "indexpattern-datasource-layer-devbar", "type": "index-pattern"}],
                        "state": {
                            "datasourceStates": {
                                "formBased": {
                                    "layers": {
                                        "devbar": {
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
                            "internalReferences": [],
                            "query": {"language": "kuery", "query": ""},
                            "visualization": {
                                "axisTitlesVisibilitySettings": {"x": True, "yLeft": True, "yRight": True},
                                "fittingFunction": "None",
                                "gridlinesVisibilitySettings": {"x": True, "yLeft": True, "yRight": True},
                                "labelsOrientation": {"x": 0, "yLeft": 0, "yRight": 0},
                                "layers": [{"accessors": ["bytes"], "layerId": "devbar", "layerType": "data", "seriesType": "bar_horizontal", "xAccessor": "device"}],
                                "legend": {"isVisible": False},
                                "preferredSeriesType": "bar_horizontal",
                                "tickLabelsVisibilitySettings": {"x": True, "yLeft": True, "yRight": True},
                                "valueLabels": "hide"
                            }
                        },
                        "title": "[Unified Flow] Top Devices by Bytes",
                        "type": "lens",
                        "visualizationType": "lnsXY"
                    },
                    "enhancements": {},
                    "hidePanelTitles": False
                },
                "gridData": {"h": 16, "i": "5", "w": 24, "x": 0, "y": 46},
                "panelIndex": "5",
                "title": "[Unified Flow] Top Devices by Bytes",
                "type": "lens",
                "version": "8.9.0"
            },
            {
                "embeddableConfig": {
                    "attributes": {
                        "references": [{"id": "unified-flow-*", "name": "indexpattern-datasource-layer-timeline", "type": "index-pattern"}],
                        "state": {
                            "datasourceStates": {
                                "formBased": {
                                    "layers": {
                                        "timeline": {
                                            "columnOrder": ["dev", "ts", "bytes"],
                                            "columns": {
                                                "dev": {"customLabel": True, "dataType": "string", "isBucketed": True, "label": "Device", "operationType": "terms", "params": {"exclude": [], "excludeIsRegex": False, "include": [], "includeIsRegex": False, "missingBucket": False, "orderBy": {"columnId": "bytes", "type": "column"}, "orderDirection": "desc", "otherBucket": False, "parentFormat": {"id": "terms"}, "size": 5}, "scale": "ordinal", "sourceField": "device.name"},
                                                "ts": {"customLabel": True, "dataType": "date", "isBucketed": True, "label": "@timestamp", "operationType": "date_histogram", "params": {"dropPartials": False, "includeEmptyRows": True, "interval": "auto"}, "scale": "interval", "sourceField": "@timestamp"},
                                                "bytes": {"customLabel": True, "dataType": "number", "isBucketed": False, "label": "Bytes", "operationType": "sum", "params": {"emptyAsNull": True}, "scale": "ratio", "sourceField": "network.bytes"}
                                            },
                                            "incompleteColumns": {}
                                        }
                                    }
                                }
                            },
                            "internalReferences": [],
                            "query": {"language": "kuery", "query": ""},
                            "visualization": {
                                "axisTitlesVisibilitySettings": {"x": True, "yLeft": True, "yRight": True},
                                "fittingFunction": "None",
                                "gridlinesVisibilitySettings": {"x": True, "yLeft": True, "yRight": True},
                                "labelsOrientation": {"x": 0, "yLeft": 0, "yRight": 0},
                                "layers": [{"accessors": ["bytes"], "layerId": "timeline", "layerType": "data", "seriesType": "line", "splitAccessor": "dev", "xAccessor": "ts"}],
                                "legend": {"isVisible": True, "position": "right"},
                                "preferredSeriesType": "line",
                                "tickLabelsVisibilitySettings": {"x": True, "yLeft": True, "yRight": True},
                                "valueLabels": "hide"
                            }
                        },
                        "title": "[Unified Flow] Device Traffic Timeline",
                        "type": "lens",
                        "visualizationType": "lnsXY"
                    },
                    "enhancements": {},
                    "hidePanelTitles": False
                },
                "gridData": {"h": 16, "i": "6", "w": 24, "x": 24, "y": 46},
                "panelIndex": "6",
                "title": "[Unified Flow] Traffic Timeline",
                "type": "lens",
                "version": "8.9.0"
            }
        ]),
        "refreshInterval": {"pause": False, "value": 15000},
        "timeRestore": True,
        "timeFrom": "now-15m",
        "timeTo": "now",
        "title": "[Unified Flow] Conversation Partners"
    },
    "coreMigrationVersion": "8.8.0",
    "created_at": "2026-02-11T14:30:00Z",
    "id": "unified-flow-conversations",
    "managed": False,
    "references": [{"id": "unified-flow-*", "name": "index-pattern", "type": "index-pattern"}],
    "type": "dashboard",
    "typeMigrationVersion": "10.3.0",
    "updated_at": "2026-02-11T14:30:00Z",
    "version": "WzE3MCwxXQ=="
}

# Export all dashboards
print(json.dumps(dashboard_1, separators=(',', ':')))
print(json.dumps(dashboard_2, separators=(',', ':')))
print(json.dumps(dashboard_3, separators=(',', ':')))

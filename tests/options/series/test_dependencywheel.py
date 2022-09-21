"""Tests for ``highcharts.no_data``."""

import pytest

from json.decoder import JSONDecodeError

from highcharts_stock.options.series.dependencywheel import DependencyWheelSeries as cls
from highcharts_stock import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal

STANDARD_PARAMS = [
    ({}, None),
    ({
      'data': [
          {
            'weight': 0.75,

            'dataLabels': {
              'align': 'center',
              'allowOverlap': True,
              'animation': {
                  'defer': 5
              },
              'backgroundColor': {
                  'linearGradient': {
                      'x1': 0.123,
                      'x2': 0.234,
                      'y1': 0.345,
                      'y2': 0.456
                  },
                  'stops': [
                      [0.12, '#999'],
                      [0.34, '#fff']
                  ]
              },
              'borderColor': '#999999',
              'borderRadius': 24,
              'borderWidth': 1,
              'className': 'some-class-name',
              'color': '#000000',
              'crop': True,
              'defer': False,
              'enabled': True,
              'filter': {
                  'operator': '>=',
                  'property': 'some_property',
                  'value': 123
              },
              'format': 'some format',
              'formatter': """function() { return true; }""",
              'inside': True,
              'nullFormat': 'some format',
              'nullFormatter': """function() { return true; }""",
              'overflow': 'none',
              'padding': 12,
              'position': 'center',
              'rotation': 0,
              'shadow': False,
              'shape': 'rect',
              'style': 'style goes here',
              'useHTML': False,
              'verticalAlign': 'top',
              'x': 10,
              'y': 20,
              'z': 0
            },
            'dragDrop': {
                'draggableX': True,
                'draggableY': True,
                'dragHandle': {
                    'className': 'draghandle-classname-goes-here',
                    'color': '#ccc',
                    'cursor': 'alias',
                    'lineColor': '#ddd',
                    'lineWidth': 2,
                    'pathFormatter': """function() { return true; }""",
                    'zIndex': 10
                },
                'dragMaxX': 3456,
                'dragMaxY': 6532,
                'dragMinX': 123,
                'dragMinY': 321,
                'dragPrecisionX': 5,
                'dragPrecisionY': 5,
                'dragSensitivity': 2,
                'groupBy': 'some-property-name',
                'guideBox': {
                    'default': {
                        'className': 'some-classname-goes-here',
                        'color': '#999',
                        'cursor': 'pointer',
                        'lineColor': '#ccc',
                        'lineWidth': 2,
                        'zIndex': 100
                    }
                },
                'liveRedraw': True
            },

            'from': 'some-id-goes-here',
            'to': 'some-id-goes-here',

            'accessibility': {
                'description': 'Some description goes here',
                'enabled': True
            },
            'className': 'some-class-name',
            'color': '#ccc',
            'colorIndex': 2,
            'custom': {
                'some_key': 123,
                'other_key': 456
            },
            'description': 'Some description goes here',
            'events': {
              'click': """function(event) { return true; }""",
              'drag': """function(event) { return true; }""",
              'drop': """function(event) { return true; }""",
              'mouseOut': """function(event) { return true; }"""
            },
            'id': 'some-id-goes-here',
            'labelrank': 3,
            'name': 'Some Name Goes here',
            'selected': False
          }
      ],
      'nodes': [
          {
            'column': 2,
            'level': 2,
            'color': '#cccccc',
            'colorIndex': 123,
            'dataLabels': {
                'align': 'center',
                'allowOverlap': False,
                'backgroundColor': '#cccccc',
                'enabled': True,
                'overflow': 'justify',
                'shadow': False
            },
            'id': 'some-id-goes-here',
            'name': 'My Node Name',
            'offsetHorizontal': 10,
            'offsetVertical': '5%'
          }
      ]
    }, None),
    # + DependencyWheelOptions
    ({
      'data': [
          {
            'weight': 0.75,

            'dataLabels': {
              'align': 'center',
              'allowOverlap': True,
              'animation': {
                  'defer': 5
              },
              'backgroundColor': {
                  'linearGradient': {
                      'x1': 0.123,
                      'x2': 0.234,
                      'y1': 0.345,
                      'y2': 0.456
                  },
                  'stops': [
                      [0.12, '#999'],
                      [0.34, '#fff']
                  ]
              },
              'borderColor': '#999999',
              'borderRadius': 24,
              'borderWidth': 1,
              'className': 'some-class-name',
              'color': '#000000',
              'crop': True,
              'defer': False,
              'enabled': True,
              'filter': {
                  'operator': '>=',
                  'property': 'some_property',
                  'value': 123
              },
              'format': 'some format',
              'formatter': """function() { return true; }""",
              'inside': True,
              'nullFormat': 'some format',
              'nullFormatter': """function() { return true; }""",
              'overflow': 'none',
              'padding': 12,
              'position': 'center',
              'rotation': 0,
              'shadow': False,
              'shape': 'rect',
              'style': 'style goes here',
              'useHTML': False,
              'verticalAlign': 'top',
              'x': 10,
              'y': 20,
              'z': 0
            },
            'dragDrop': {
                'draggableX': True,
                'draggableY': True,
                'dragHandle': {
                    'className': 'draghandle-classname-goes-here',
                    'color': '#ccc',
                    'cursor': 'alias',
                    'lineColor': '#ddd',
                    'lineWidth': 2,
                    'pathFormatter': """function() { return true; }""",
                    'zIndex': 10
                },
                'dragMaxX': 3456,
                'dragMaxY': 6532,
                'dragMinX': 123,
                'dragMinY': 321,
                'dragPrecisionX': 5,
                'dragPrecisionY': 5,
                'dragSensitivity': 2,
                'groupBy': 'some-property-name',
                'guideBox': {
                    'default': {
                        'className': 'some-classname-goes-here',
                        'color': '#999',
                        'cursor': 'pointer',
                        'lineColor': '#ccc',
                        'lineWidth': 2,
                        'zIndex': 100
                    }
                },
                'liveRedraw': True
            },

            'from': 'some-id-goes-here',
            'to': 'some-id-goes-here',

            'accessibility': {
                'description': 'Some description goes here',
                'enabled': True
            },
            'className': 'some-class-name',
            'color': '#ccc',
            'colorIndex': 2,
            'custom': {
                'some_key': 123,
                'other_key': 456
            },
            'description': 'Some description goes here',
            'events': {
              'click': """function(event) { return true; }""",
              'drag': """function(event) { return true; }""",
              'drop': """function(event) { return true; }""",
              'mouseOut': """function(event) { return true; }"""
            },
            'id': 'some-id-goes-here',
            'labelrank': 3,
            'name': 'Some Name Goes here',
            'selected': False
          }
      ],
      'nodes': [
          {
            'column': 2,
            'level': 2,
            'color': '#cccccc',
            'colorIndex': 123,
            'dataLabels': {
                'align': 'center',
                'allowOverlap': False,
                'backgroundColor': '#cccccc',
                'enabled': True,
                'overflow': 'justify',
                'shadow': False
            },
            'id': 'some-id-goes-here',
            'name': 'My Node Name',
            'offsetHorizontal': 10,
            'offsetVertical': '5%'
          }
      ],

      'border_color': '#ccc',
      'border_width': 2,
      'center': ['50%', '30%'],
      'center_in_category': True,
      'color_by_point': False,
      'color_index': 3,
      'colors': [
          '#fff',
          'ccc',
          {
            'linearGradient': {
                'x1': 0.123,
                'x2': 0.567,
                'y1': 0.891,
                'y2': 0.987
            },
            'stops': [
                [0.123, '#cccccc'],
                [0.456, '#ff0000'],
                [1, '#00ff00']
            ]
          },
          {
            'animation': {
                'defer': 5
            },
            'patternOptions': {
                'aspectRatio': 0.5,
                'backgroundColor': '#999999',
                'id': 'some_id_goes_here',
                'opacity': 0.5,
                'width': 120,
                'x': 5,
                'y': 10
            },
            'patternIndex': 2
          }
      ],
      'curve_factor': 0.6,
      'levels': [
          {
           'colorByPoint': False,
           'linkOpacity': 0.5,
           'states': {
             'hover': {
                 'animation': {
                     'duration': 123
                 },
                 'borderColor': '#cccccc',
                 'brightness': 0.3,
                 'enabled': True
             },
             'inactive': {
                 'enabled': True,
                 'opacity': 0.5
             },
             'normal': {
                 'animation': {
                     'defer': 24
                 }
             },
             'select': {
                 'color': '#ff0000',
                 'enabled': True,
             }
           },
           'borderColor': '#ccc',
           'borderWidth': 1,
           'dataLabels': {
             'align': 'center',
             'allowOverlap': True,
             'animation': {
                 'defer': 5
             },
             'backgroundColor': {
                 'linearGradient': {
                     'x1': 0.123,
                     'x2': 0.234,
                     'y1': 0.345,
                     'y2': 0.456
                 },
                 'stops': [
                     [0.12, '#999'],
                     [0.34, '#fff']
                 ]
             },
             'borderColor': '#999999',
             'borderRadius': 24,
             'borderWidth': 1,
             'className': 'some-class-name',
             'color': '#000000',
             'crop': True,
             'defer': False,
             'enabled': True,
             'filter': {
                 'operator': '>=',
                 'property': 'some_property',
                 'value': 123
             },
             'format': 'some format',
             'formatter': """function() { return true; }""",
             'inside': True,
             'nullFormat': 'some format',
             'nullFormatter': """function() { return true; }""",
             'overflow': 'none',
             'padding': 12,
             'position': 'center',
             'rotation': 0,
             'shadow': False,
             'shape': 'rect',
             'style': 'style goes here',
             'useHTML': False,
             'verticalAlign': 'top',
             'x': 10,
             'y': 20,
             'z': 0
           },
           'level': 1
          },
          {
           'colorByPoint': False,
           'linkOpacity': 0.5,
           'states': {
             'hover': {
                 'animation': {
                     'duration': 123
                 },
                 'borderColor': '#cccccc',
                 'brightness': 0.3,
                 'enabled': True
             },
             'inactive': {
                 'enabled': True,
                 'opacity': 0.5
             },
             'normal': {
                 'animation': {
                     'defer': 24
                 }
             },
             'select': {
                 'color': '#ff0000',
                 'enabled': True,
             }
           },
           'borderColor': '#ccc',
           'borderWidth': 1,
           'dataLabels': {
             'align': 'center',
             'allowOverlap': True,
             'animation': {
                 'defer': 5
             },
             'backgroundColor': {
                 'linearGradient': {
                     'x1': 0.123,
                     'x2': 0.234,
                     'y1': 0.345,
                     'y2': 0.456
                 },
                 'stops': [
                     [0.12, '#999'],
                     [0.34, '#fff']
                 ]
             },
             'borderColor': '#999999',
             'borderRadius': 24,
             'borderWidth': 1,
             'className': 'some-class-name',
             'color': '#000000',
             'crop': True,
             'defer': False,
             'enabled': True,
             'filter': {
                 'operator': '>=',
                 'property': 'some_property',
                 'value': 123
             },
             'format': 'some format',
             'formatter': """function() { return true; }""",
             'inside': True,
             'nullFormat': 'some format',
             'nullFormatter': """function() { return true; }""",
             'overflow': 'none',
             'padding': 12,
             'position': 'center',
             'rotation': 0,
             'shadow': False,
             'shape': 'rect',
             'style': 'style goes here',
             'useHTML': False,
             'verticalAlign': 'top',
             'x': 10,
             'y': 20,
             'z': 0
           },
           'level': 1
          },
          {
           'colorByPoint': False,
           'linkOpacity': 0.5,
           'states': {
             'hover': {
                 'animation': {
                     'duration': 123
                 },
                 'borderColor': '#cccccc',
                 'brightness': 0.3,
                 'enabled': True
             },
             'inactive': {
                 'enabled': True,
                 'opacity': 0.5
             },
             'normal': {
                 'animation': {
                     'defer': 24
                 }
             },
             'select': {
                 'color': '#ff0000',
                 'enabled': True,
             }
           },
           'borderColor': '#ccc',
           'borderWidth': 1,
           'dataLabels': {
             'align': 'center',
             'allowOverlap': True,
             'animation': {
                 'defer': 5
             },
             'backgroundColor': {
                 'linearGradient': {
                     'x1': 0.123,
                     'x2': 0.234,
                     'y1': 0.345,
                     'y2': 0.456
                 },
                 'stops': [
                     [0.12, '#999'],
                     [0.34, '#fff']
                 ]
             },
             'borderColor': '#999999',
             'borderRadius': 24,
             'borderWidth': 1,
             'className': 'some-class-name',
             'color': '#000000',
             'crop': True,
             'defer': False,
             'enabled': True,
             'filter': {
                 'operator': '>=',
                 'property': 'some_property',
                 'value': 123
             },
             'format': 'some format',
             'formatter': """function() { return true; }""",
             'inside': True,
             'nullFormat': 'some format',
             'nullFormatter': """function() { return true; }""",
             'overflow': 'none',
             'padding': 12,
             'position': 'center',
             'rotation': 0,
             'shadow': False,
             'shape': 'rect',
             'style': 'style goes here',
             'useHTML': False,
             'verticalAlign': 'top',
             'x': 10,
             'y': 20,
             'z': 0
           },
           'level': 1
          }
      ],
      'link_opacity': 0.7,
      'min_link_width': 1,
      'node_padding': 6,
      'node_width': 12,
      'start_angle': 45
    }, None),
    # + Generic Options
    ({
      'data': [
          {
            'weight': 0.75,

            'dataLabels': {
              'align': 'center',
              'allowOverlap': True,
              'animation': {
                  'defer': 5
              },
              'backgroundColor': {
                  'linearGradient': {
                      'x1': 0.123,
                      'x2': 0.234,
                      'y1': 0.345,
                      'y2': 0.456
                  },
                  'stops': [
                      [0.12, '#999'],
                      [0.34, '#fff']
                  ]
              },
              'borderColor': '#999999',
              'borderRadius': 24,
              'borderWidth': 1,
              'className': 'some-class-name',
              'color': '#000000',
              'crop': True,
              'defer': False,
              'enabled': True,
              'filter': {
                  'operator': '>=',
                  'property': 'some_property',
                  'value': 123
              },
              'format': 'some format',
              'formatter': """function() { return true; }""",
              'inside': True,
              'nullFormat': 'some format',
              'nullFormatter': """function() { return true; }""",
              'overflow': 'none',
              'padding': 12,
              'position': 'center',
              'rotation': 0,
              'shadow': False,
              'shape': 'rect',
              'style': 'style goes here',
              'useHTML': False,
              'verticalAlign': 'top',
              'x': 10,
              'y': 20,
              'z': 0
            },
            'dragDrop': {
                'draggableX': True,
                'draggableY': True,
                'dragHandle': {
                    'className': 'draghandle-classname-goes-here',
                    'color': '#ccc',
                    'cursor': 'alias',
                    'lineColor': '#ddd',
                    'lineWidth': 2,
                    'pathFormatter': """function() { return true; }""",
                    'zIndex': 10
                },
                'dragMaxX': 3456,
                'dragMaxY': 6532,
                'dragMinX': 123,
                'dragMinY': 321,
                'dragPrecisionX': 5,
                'dragPrecisionY': 5,
                'dragSensitivity': 2,
                'groupBy': 'some-property-name',
                'guideBox': {
                    'default': {
                        'className': 'some-classname-goes-here',
                        'color': '#999',
                        'cursor': 'pointer',
                        'lineColor': '#ccc',
                        'lineWidth': 2,
                        'zIndex': 100
                    }
                },
                'liveRedraw': True
            },

            'from': 'some-id-goes-here',
            'to': 'some-id-goes-here',

            'accessibility': {
                'description': 'Some description goes here',
                'enabled': True
            },
            'className': 'some-class-name',
            'color': '#ccc',
            'colorIndex': 2,
            'custom': {
                'some_key': 123,
                'other_key': 456
            },
            'description': 'Some description goes here',
            'events': {
              'click': """function(event) { return true; }""",
              'drag': """function(event) { return true; }""",
              'drop': """function(event) { return true; }""",
              'mouseOut': """function(event) { return true; }"""
            },
            'id': 'some-id-goes-here',
            'labelrank': 3,
            'name': 'Some Name Goes here',
            'selected': False
          }
      ],
      'nodes': [
          {
            'column': 2,
            'level': 2,
            'color': '#cccccc',
            'colorIndex': 123,
            'dataLabels': {
                'align': 'center',
                'allowOverlap': False,
                'backgroundColor': '#cccccc',
                'enabled': True,
                'overflow': 'justify',
                'shadow': False
            },
            'id': 'some-id-goes-here',
            'name': 'My Node Name',
            'offsetHorizontal': 10,
            'offsetVertical': '5%'
          }
      ],
      
      'border_color': '#ccc',
      'border_width': 2,
      'center': ['50%', '30%'],
      'center_in_category': True,
      'color_by_point': False,
      'color_index': 3,
      'colors': [
          '#fff',
          'ccc',
          {
            'linearGradient': {
                'x1': 0.123,
                'x2': 0.567,
                'y1': 0.891,
                'y2': 0.987
            },
            'stops': [
                [0.123, '#cccccc'],
                [0.456, '#ff0000'],
                [1, '#00ff00']
            ]
          },
          {
            'animation': {
                'defer': 5
            },
            'patternOptions': {
                'aspectRatio': 0.5,
                'backgroundColor': '#999999',
                'id': 'some_id_goes_here',
                'opacity': 0.5,
                'width': 120,
                'x': 5,
                'y': 10
            },
            'patternIndex': 2
          }
      ],
      'curve_factor': 0.6,
      'levels': [
          {
           'colorByPoint': False,
           'linkOpacity': 0.5,
           'states': {
             'hover': {
                 'animation': {
                     'duration': 123
                 },
                 'borderColor': '#cccccc',
                 'brightness': 0.3,
                 'enabled': True
             },
             'inactive': {
                 'enabled': True,
                 'opacity': 0.5
             },
             'normal': {
                 'animation': {
                     'defer': 24
                 }
             },
             'select': {
                 'color': '#ff0000',
                 'enabled': True,
             }
           },
           'borderColor': '#ccc',
           'borderWidth': 1,
           'dataLabels': {
             'align': 'center',
             'allowOverlap': True,
             'animation': {
                 'defer': 5
             },
             'backgroundColor': {
                 'linearGradient': {
                     'x1': 0.123,
                     'x2': 0.234,
                     'y1': 0.345,
                     'y2': 0.456
                 },
                 'stops': [
                     [0.12, '#999'],
                     [0.34, '#fff']
                 ]
             },
             'borderColor': '#999999',
             'borderRadius': 24,
             'borderWidth': 1,
             'className': 'some-class-name',
             'color': '#000000',
             'crop': True,
             'defer': False,
             'enabled': True,
             'filter': {
                 'operator': '>=',
                 'property': 'some_property',
                 'value': 123
             },
             'format': 'some format',
             'formatter': """function() { return true; }""",
             'inside': True,
             'nullFormat': 'some format',
             'nullFormatter': """function() { return true; }""",
             'overflow': 'none',
             'padding': 12,
             'position': 'center',
             'rotation': 0,
             'shadow': False,
             'shape': 'rect',
             'style': 'style goes here',
             'useHTML': False,
             'verticalAlign': 'top',
             'x': 10,
             'y': 20,
             'z': 0
           },
           'level': 1
          },
          {
           'colorByPoint': False,
           'linkOpacity': 0.5,
           'states': {
             'hover': {
                 'animation': {
                     'duration': 123
                 },
                 'borderColor': '#cccccc',
                 'brightness': 0.3,
                 'enabled': True
             },
             'inactive': {
                 'enabled': True,
                 'opacity': 0.5
             },
             'normal': {
                 'animation': {
                     'defer': 24
                 }
             },
             'select': {
                 'color': '#ff0000',
                 'enabled': True,
             }
           },
           'borderColor': '#ccc',
           'borderWidth': 1,
           'dataLabels': {
             'align': 'center',
             'allowOverlap': True,
             'animation': {
                 'defer': 5
             },
             'backgroundColor': {
                 'linearGradient': {
                     'x1': 0.123,
                     'x2': 0.234,
                     'y1': 0.345,
                     'y2': 0.456
                 },
                 'stops': [
                     [0.12, '#999'],
                     [0.34, '#fff']
                 ]
             },
             'borderColor': '#999999',
             'borderRadius': 24,
             'borderWidth': 1,
             'className': 'some-class-name',
             'color': '#000000',
             'crop': True,
             'defer': False,
             'enabled': True,
             'filter': {
                 'operator': '>=',
                 'property': 'some_property',
                 'value': 123
             },
             'format': 'some format',
             'formatter': """function() { return true; }""",
             'inside': True,
             'nullFormat': 'some format',
             'nullFormatter': """function() { return true; }""",
             'overflow': 'none',
             'padding': 12,
             'position': 'center',
             'rotation': 0,
             'shadow': False,
             'shape': 'rect',
             'style': 'style goes here',
             'useHTML': False,
             'verticalAlign': 'top',
             'x': 10,
             'y': 20,
             'z': 0
           },
           'level': 1
          },
          {
           'colorByPoint': False,
           'linkOpacity': 0.5,
           'states': {
             'hover': {
                 'animation': {
                     'duration': 123
                 },
                 'borderColor': '#cccccc',
                 'brightness': 0.3,
                 'enabled': True
             },
             'inactive': {
                 'enabled': True,
                 'opacity': 0.5
             },
             'normal': {
                 'animation': {
                     'defer': 24
                 }
             },
             'select': {
                 'color': '#ff0000',
                 'enabled': True,
             }
           },
           'borderColor': '#ccc',
           'borderWidth': 1,
           'dataLabels': {
             'align': 'center',
             'allowOverlap': True,
             'animation': {
                 'defer': 5
             },
             'backgroundColor': {
                 'linearGradient': {
                     'x1': 0.123,
                     'x2': 0.234,
                     'y1': 0.345,
                     'y2': 0.456
                 },
                 'stops': [
                     [0.12, '#999'],
                     [0.34, '#fff']
                 ]
             },
             'borderColor': '#999999',
             'borderRadius': 24,
             'borderWidth': 1,
             'className': 'some-class-name',
             'color': '#000000',
             'crop': True,
             'defer': False,
             'enabled': True,
             'filter': {
                 'operator': '>=',
                 'property': 'some_property',
                 'value': 123
             },
             'format': 'some format',
             'formatter': """function() { return true; }""",
             'inside': True,
             'nullFormat': 'some format',
             'nullFormatter': """function() { return true; }""",
             'overflow': 'none',
             'padding': 12,
             'position': 'center',
             'rotation': 0,
             'shadow': False,
             'shape': 'rect',
             'style': 'style goes here',
             'useHTML': False,
             'verticalAlign': 'top',
             'x': 10,
             'y': 20,
             'z': 0
           },
           'level': 1
          }
      ],
      'link_opacity': 0.7,
      'min_link_width': 1,
      'node_padding': 6,
      'node_width': 12,
      'start_angle': 45,

      'accessibility': {
          'description': 'Description goes here',
          'enabled': True,
          'exposeAsGroupOnly': True,
          'keyboardNavigation': {
              'enabled': True
          },
          'point': {
              'dateFormat': 'format string',
              'dateFormatter': """function() { return true; }""",
              'describeNull': False,
              'descriptionFormatter': """function() { return true; }""",
              'valueDecimals': 2,
              'valueDescriptionFormat': 'format string',
              'valuePrefix': '$',
              'valueSuffix': 'USD'
          },
      },
      'allow_point_select': True,
      'animation': {
          'defer': 5
      },
      'class_name': 'some-class-name',
      'clip': False,
      'color': '#fff',
      'cursor': 'alias',
      'custom': {
          'item1': 'some value',
          'item2': 'some value'
      },
      'dash_style': 'Dash',
      'data_labels': {
        'align': 'center',
        'allowOverlap': True,
        'animation': {
            'defer': 5
        },
        'backgroundColor': {
            'linearGradient': {
                'x1': 0.123,
                'x2': 0.234,
                'y1': 0.345,
                'y2': 0.456
            },
            'stops': [
                [0.12, '#999'],
                [0.34, '#fff']
            ]
        },
        'borderColor': '#999999',
        'borderRadius': 24,
        'borderWidth': 1,
        'className': 'some-class-name',
        'color': '#000000',
        'crop': True,
        'defer': False,
        'enabled': True,
        'filter': {
            'operator': '>=',
            'property': 'some_property',
            'value': 123
        },
        'format': 'some format',
        'formatter': """function() { return true; }""",
        'inside': True,
        'nullFormat': 'some format',
        'nullFormatter': """function() { return true; }""",
        'overflow': 'none',
        'padding': 12,
        'position': 'center',
        'rotation': 0,
        'shadow': False,
        'shape': 'rect',
        'style': 'style goes here',
        'useHTML': False,
        'verticalAlign': 'top',
        'x': 10,
        'y': 20,
        'z': 0
      },
      'description': 'Description goes here',
      'enable_mouse_tracking': True,
      'events': {
        'afterAnimate': """function(event) { return true; }""",
        'click': """function(event) { return true; }""",
        'hide': """function(event) { return true; }""",
        'mouseOut': """function(event) { return true; }""",
        'show': """function(event) { return true; }"""
      },
      'include_in_data_export': True,
      'keys': [
          'somevalue',
          'somevalue',
          'somevalue'
      ],
      'label': {
          'boxesToAvoid': [
              {
               'bottom': 12,
               'left': -46,
               'right': 84,
               'top': 24
              },
              {
               'bottom': 48,
               'left': -46,
               'right': 84,
               'top': 86
              }
          ],
          'connectorAllowed': True,
          'connectorNeighbourDistance': 12,
          'enabled': True,
          'format': 'format string',
          'formatter': """function() { return true; }""",
          'maxFontSize': 18,
          'minFontSize': 6,
          'onArea': False,
          'style': 'some style string'
      },
      'linked_to': 'some_id',
      'marker': {
        'enabled': True,
        'fillColor': '#cccccc',
        'height': 24,
        'lineWidth': 2,
        'radius': 2,
        'states': {
            'hover': {
                'enabled': True
            }
        },
        'symbol': 'circle',
        'width': 48
      },
      'on_point': {
          'connectorOptions': {
              'dashstyle': 'Dash',
              'stroke': '#ccc',
              'width': 2
          },
          'id': 'some-id',
          'position': {
              'align': 'left',
              'verticalAlign': 'top',
              'x': 15,
              'y': -46
          }
      },
      'opacity': 0.2,
      'point': {
          'events': {
            'click': """function(event) { return true; }""",
            'drag': """function(event) { return true; }""",
            'drop': """function(event) { return true; }""",
            'mouseOut': """function(event) { return true; }"""
          }
      },
      'point_description_formatter': """function (point) { return true; }""",
      'selected': False,
      'show_checkbox': True,
      'show_in_legend': True,
      'skip_keyboard_navigation': False,
      'states': {
        'hover': {
            'animation': {
                'duration': 123
            },
            'borderColor': '#cccccc',
            'brightness': 0.3,
            'enabled': True
        },
        'inactive': {
            'enabled': True,
            'opacity': 0.5
        },
        'normal': {
            'animation': {
                'defer': 24
            }
        },
        'select': {
            'color': '#ff0000',
            'enabled': True,
        }
      },
      'sticky_tracking': True,
      'threshold': 123,
      'tooltip': {
        'animation': True,
        'backgroundColor': '#ccc',
        'borderColor': '#999',
        'borderRadius': 4,
        'borderWidth': 1,
        'className': 'some-class-name',
        'clusterFormat': 'format string',
        'dateTimeLabelFormats': {
          'day': 'test',
          'hour': 'test',
          'millisecond': 'test',
          'minute': 'test',
          'month': 'test',
          'second': 'test',
          'week': 'test',
          'year': 'test'
        },
        'distance': 12,
        'enabled': True,
        'followPointer': True,
        'followTouch_move': True,
        'footerFormat': 'format string',
        'formatter': """function() { return true; }""",
        'headerFormat': 'format string',
        'headerShape': 'circle',
        'hideDelay': 3,
        'nullFormat': 'format string',
        'nullFormatter': """function() { return true; }""",
        'outside': False,
        'padding': 6,
        'pointFormat': 'format string',
        'pointFormatter': """function() { return true; }""",
        'positioner': """function() { return true; }""",
        'shadow': False,
        'shape': 'rect',
        'shared': False,
        'snap': 4,
        'split': False,
        'stickOnContact': True,
        'style': 'style string goes here',
        'useHTML': False,
        'valueDecimals': 2,
        'valuePrefix': '$',
        'valueSuffix': ' USD',
        'xDateFormat': 'format string'
       },
      'turbo_threshold': 456,
      'visible': True
    }, None),

]


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test__init__(kwargs, error):
    Class__init__(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_from_dict(kwargs, error):
    Class_from_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_to_dict(kwargs, error):
    Class_to_dict(cls, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('series/dependencywheel/01.js', False, None),

    ('series/dependencywheel/error-01.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('series/dependencywheel/01.js', True, None),

    ('series/dependencywheel/error-01.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

])
def test_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls, input_files, filename, as_file, error)

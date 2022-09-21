"""Tests for ``highcharts.no_data``."""

import pytest

from json.decoder import JSONDecodeError

from highcharts_stock.options.series.treemap import TreemapSeries as cls
from highcharts_stock import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal

STANDARD_PARAMS = [
    ({}, None),
    ({
      'data': [
          {
            'colorValue': 2,
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
            'drilldown': 'some-id-goes-here',
            'parent': 'some-id-goes-here',
            'value': 123.45
          }
      ]
    }, None),
    # + Treemap Options
    ({
      'data': [
          {
            'colorValue': 2,
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
            'drilldown': 'some-id-goes-here',
            'parent': 'some-id-goes-here',
            'value': 123.45
          }
      ],

      'allow_traversing_tree': True,
      'alternate_starting_direction': False,
      'animation_limit': 10,
      'boost_blending': 'some-value-goes-here',
      'boost_threshold': 5000,
      'breadcrumbs': {
        'buttonSpacing': 6,
        'buttonTheme': {
            'fill': '#fff'
        },
        'events': {
          'click': """function(event) { return true; }"""
        },
        'floating': True,
        'format': 'some format string',
        'formatter': """function () { return true; }""",
        'position': None,
        'relativeTo': 'plot',
        'rtl': False,
        'separator': {
            'text': '>',
            'style': {
                'some-key': 'some-value'
            }
        },
        'useHTML': False,
        'zIndex': 3
      },
      'color_axis': 'some-id-goes-here',
      'color_by_point': True,
      'color_index': 2,
      'color_key': 'some-key-goes-here',
      'colors': [
          '#ccc',
          '#fff',
          '000000'
      ],
      'crisp': True,
      'crop_threshold': 500,
      'find_nearest_point_by': 'xy',
      'get_extremes_from_all': True,
      'ignore_hidden_point': True,
      'interact_by_leaf': True,
      'layout_algorithm': 'sliceAndDice',
      'layout_starting_direction': 'vertical',
      'level_is_constant': True,
      'levels': [
          {
           'borderDashStyle': 'Solid',
           'color': '#ccc',
           'colorVariation': {
               'key': 'brightness',
               'to': 50
           },
           'layoutAlgorithm': 'sliceAndDice',
           'layoutStartingDirection': 'vertical',
           'borderColor': '#ccc',
           'borderWidth': 1,
           'level': 1,
          }
      ],
      'linecap': 'round',
      'line_width': 1,
      'negative_color': '#ccc',
      'point_interval': 5,
      'point_interval_unit': 'day',
      'point_start': 1,
      'relative_x_value': True,
      'soft_threshold': True,
      'sort_index': 2,
      'stacking': 'normal',
      'step': 'left',
      'zone_axis': 'y',
      'zones': [
          {
            'className': 'some-class-name1',
            'color': '#999999',
            'dashStyle': 'Solid',
            'fillColor': '#cccccc',
            'value': 123
          },
          {
            'className': 'some-class-name1',
            'color': '#999999',
            'dashStyle': 'Solid',
            'fillColor': '#cccccc',
            'value': 123
          },
          {
            'className': 'some-class-name1',
            'color': '#999999',
            'dashStyle': 'Solid',
            'fillColor': '#cccccc',
            'value': 123
          }
      ]
    }, None),
    # + Generic Options
    ({
      'data': [
          {
            'colorValue': 2,
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
            'drilldown': 'some-id-goes-here',
            'parent': 'some-id-goes-here',
            'value': 123.45
          }
      ],

      'allow_traversing_tree': True,
      'alternate_starting_direction': False,
      'animation_limit': 10,
      'boost_blending': 'some-value-goes-here',
      'boost_threshold': 5000,
      'breadcrumbs': {
        'buttonSpacing': 6,
        'buttonTheme': {
            'fill': '#fff'
        },
        'events': {
          'click': """function(event) { return true; }"""
        },
        'floating': True,
        'format': 'some format string',
        'formatter': """function () { return true; }""",
        'position': None,
        'relativeTo': 'plot',
        'rtl': False,
        'separator': {
            'text': '>',
            'style': {
                'some-key': 'some-value'
            }
        },
        'useHTML': False,
        'zIndex': 3
      },
      'color_axis': 'some-id-goes-here',
      'color_by_point': True,
      'color_index': 2,
      'color_key': 'some-key-goes-here',
      'colors': [
          '#ccc',
          '#fff',
          '000000'
      ],
      'crisp': True,
      'crop_threshold': 500,
      'find_nearest_point_by': 'xy',
      'get_extremes_from_all': True,
      'ignore_hidden_point': True,
      'interact_by_leaf': True,
      'layout_algorithm': 'sliceAndDice',
      'layout_starting_direction': 'vertical',
      'level_is_constant': True,
      'levels': [
          {
           'borderDashStyle': 'Solid',
           'color': '#ccc',
           'colorVariation': {
               'key': 'brightness',
               'to': 50
           },
           'layoutAlgorithm': 'sliceAndDice',
           'layoutStartingDirection': 'vertical',
           'borderColor': '#ccc',
           'borderWidth': 1,
           'level': 1,
          }
      ],
      'linecap': 'round',
      'line_width': 1,
      'negative_color': '#ccc',
      'point_interval': 5,
      'point_interval_unit': 'day',
      'point_start': 1,
      'relative_x_value': True,
      'soft_threshold': True,
      'sort_index': 2,
      'stacking': 'normal',
      'step': 'left',
      'zone_axis': 'y',
      'zones': [
          {
            'className': 'some-class-name1',
            'color': '#999999',
            'dashStyle': 'Solid',
            'fillColor': '#cccccc',
            'value': 123
          },
          {
            'className': 'some-class-name1',
            'color': '#999999',
            'dashStyle': 'Solid',
            'fillColor': '#cccccc',
            'value': 123
          },
          {
            'className': 'some-class-name1',
            'color': '#999999',
            'dashStyle': 'Solid',
            'fillColor': '#cccccc',
            'value': 123
          }
      ],

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
    ('series/treemap/01.js', False, None),
    ('series/treemap/02.js', False, None),

    ('series/treemap/error-01.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),
    ('series/treemap/error-02.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('series/treemap/01.js', True, None),
    ('series/treemap/02.js', True, None),

    ('series/treemap/error-01.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),
    ('series/treemap/error-02.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

])
def test_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls, input_files, filename, as_file, error)

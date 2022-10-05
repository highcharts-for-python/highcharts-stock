{
  abands: {
    bottomLine: {
      styles: {
        lineWidth: 2
      }
    },
    fillColor: '#ccc',
    topLine: {
      styles: {
        lineWidth: 3
      }
    },

    compareStart: true,
    compareToMain: true,
    name: 'Some-Name-Goes-Here',
    params: {
      index: 0,
      period: 2
    },

    colorAxis: 1,
    connectEnds: true,
    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true
    },
    negativeColor: '#fff',
    pointInterval: 5,
    pointIntervalUnit: 'weeks',
    pointPlacement: 'on',
    pointStart: 12,
    stacking: 'normal',

    animationLimit: 10,
    boostBlending: '#ccc',
    boostThreshold: 1234,
    colorIndex: 5,
    colorKey: 'some-key-value',
    connectNulls: true,
    crisp: true,
    cropThreshold: 123,
    dataSorting: {
        enabled: true,
        matchByName: true,
        sortKey: 'some-key-value'
    },
    findNearestPointBy: 'x',
    getExtremesFromAll: true,
    linecap: 'round',
    lineWidth: 2,
    relativeXValue: true,
    shadow: false,
    softThreshold: true,
    step: 'left',
    zoneAxis: 'y',
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ],

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'abands',

    cumulative: false,
    dataAsColumns: false,
    gapSize: 6,
    gapUnit: 'relative',
    lastPrice: {
      color: '#ccc',
      enabled: true
    },
    lastVisiblePrice: {
      color: '#777',
      enabled: true
    }
  },
  ad: {
    compareStart: true,
    compareToMain: true,
    name: 'Some-Name-Goes-Here',
    params: {
      period: 2,
      volumeSeriesID: 'some-id-goes-here',
    },

    colorAxis: 1,
    connectEnds: true,
    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true
    },
    negativeColor: '#fff',
    pointInterval: 5,
    pointIntervalUnit: 'weeks',
    pointPlacement: 'on',
    pointStart: 12,
    stacking: 'normal',

    animationLimit: 10,
    boostBlending: '#ccc',
    boostThreshold: 1234,
    colorIndex: 5,
    colorKey: 'some-key-value',
    connectNulls: true,
    crisp: true,
    cropThreshold: 123,
    dataSorting: {
        enabled: true,
        matchByName: true,
        sortKey: 'some-key-value'
    },
    findNearestPointBy: 'x',
    getExtremesFromAll: true,
    linecap: 'round',
    lineWidth: 2,
    relativeXValue: true,
    shadow: false,
    softThreshold: true,
    step: 'left',
    zoneAxis: 'y',
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ],

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'ad',

    cumulative: false,
    dataAsColumns: false,
    gapSize: 6,
    gapUnit: 'relative',
    lastPrice: {
      color: '#ccc',
      enabled: true
    },
    lastVisiblePrice: {
      color: '#777',
      enabled: true
    }
  },
  ao: {
    greaterBarColor: '#ccc',
    groupPadding: 6,
    lowerBarColor: '#777',
    pointPadding: 2,

    compare: 'percent',
    compareBase: 0,

    compareStart: true,
    compareToMain: true,
    name: 'Some-Name-Goes-Here',
    params: {
      index: 0,
      period: 2
    },

    colorAxis: 1,
    connectEnds: true,
    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true
    },
    negativeColor: '#fff',
    pointInterval: 5,
    pointIntervalUnit: 'weeks',
    pointPlacement: 'on',
    pointStart: 12,
    stacking: 'normal',

    animationLimit: 10,
    boostBlending: '#ccc',
    boostThreshold: 1234,
    colorIndex: 5,
    colorKey: 'some-key-value',
    connectNulls: true,
    crisp: true,
    cropThreshold: 123,
    dataSorting: {
        enabled: true,
        matchByName: true,
        sortKey: 'some-key-value'
    },
    findNearestPointBy: 'x',
    getExtremesFromAll: true,
    linecap: 'round',
    lineWidth: 2,
    relativeXValue: true,
    shadow: false,
    softThreshold: true,
    step: 'left',
    zoneAxis: 'y',
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ],

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'ao',

    cumulative: false,
    dataAsColumns: false,
    gapSize: 6,
    gapUnit: 'relative',
    lastPrice: {
      color: '#ccc',
      enabled: true
    },
    lastVisiblePrice: {
      color: '#777',
      enabled: true
    }
  },
  apo: {
    compare: 'percent',
    compareBase: 0,

    compareStart: true,
    compareToMain: true,
    name: 'Some-Name-Goes-Here',
    params: {
      index: 0,
      period: 2
    },

    colorAxis: 1,
    connectEnds: true,
    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true
    },
    negativeColor: '#fff',
    pointInterval: 5,
    pointIntervalUnit: 'weeks',
    pointPlacement: 'on',
    pointStart: 12,
    stacking: 'normal',

    animationLimit: 10,
    boostBlending: '#ccc',
    boostThreshold: 1234,
    colorIndex: 5,
    colorKey: 'some-key-value',
    connectNulls: true,
    crisp: true,
    cropThreshold: 123,
    dataSorting: {
        enabled: true,
        matchByName: true,
        sortKey: 'some-key-value'
    },
    findNearestPointBy: 'x',
    getExtremesFromAll: true,
    linecap: 'round',
    lineWidth: 2,
    relativeXValue: true,
    shadow: false,
    softThreshold: true,
    step: 'left',
    zoneAxis: 'y',
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ],

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'apo',

    cumulative: false,
    dataAsColumns: false,
    gapSize: 6,
    gapUnit: 'relative',
    lastPrice: {
      color: '#ccc',
      enabled: true
    },
    lastVisiblePrice: {
      color: '#777',
      enabled: true
    }
  },
  aroon: {
    aroonDown: {
      styles: {
        lineWidth: 3,
        lineColor: '#ccc'
      }
    },

    compareStart: true,
    compareToMain: true,
    name: 'Some-Name-Goes-Here',
    params: {
      index: 0,
      period: 2,
    },

    colorAxis: 1,
    connectEnds: true,
    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true
    },
    negativeColor: '#fff',
    pointInterval: 5,
    pointIntervalUnit: 'weeks',
    pointPlacement: 'on',
    pointStart: 12,
    stacking: 'normal',

    animationLimit: 10,
    boostBlending: '#ccc',
    boostThreshold: 1234,
    colorIndex: 5,
    colorKey: 'some-key-value',
    connectNulls: true,
    crisp: true,
    cropThreshold: 123,
    dataSorting: {
        enabled: true,
        matchByName: true,
        sortKey: 'some-key-value'
    },
    findNearestPointBy: 'x',
    getExtremesFromAll: true,
    linecap: 'round',
    lineWidth: 2,
    relativeXValue: true,
    shadow: false,
    softThreshold: true,
    step: 'left',
    zoneAxis: 'y',
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ],

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'aroon',

    cumulative: false,
    dataAsColumns: false,
    gapSize: 6,
    gapUnit: 'relative',
    lastPrice: {
      color: '#ccc',
      enabled: true
    },
    lastVisiblePrice: {
      color: '#777',
      enabled: true
    }
  },
  aroonoscillator: {
    compareStart: true,
    compareToMain: true,
    name: 'Some-Name-Goes-Here',
    params: {
      index: 0,
      period: 2
    },

    colorAxis: 1,
    connectEnds: true,
    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true
    },
    negativeColor: '#fff',
    pointInterval: 5,
    pointIntervalUnit: 'weeks',
    pointPlacement: 'on',
    pointStart: 12,
    stacking: 'normal',

    animationLimit: 10,
    boostBlending: '#ccc',
    boostThreshold: 1234,
    colorIndex: 5,
    colorKey: 'some-key-value',
    connectNulls: true,
    crisp: true,
    cropThreshold: 123,
    dataSorting: {
        enabled: true,
        matchByName: true,
        sortKey: 'some-key-value'
    },
    findNearestPointBy: 'x',
    getExtremesFromAll: true,
    linecap: 'round',
    lineWidth: 2,
    relativeXValue: true,
    shadow: false,
    softThreshold: true,
    step: 'left',
    zoneAxis: 'y',
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ],

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'aroonoscillator',

    cumulative: false,
    dataAsColumns: false,
    gapSize: 6,
    gapUnit: 'relative',
    lastPrice: {
      color: '#ccc',
      enabled: true
    },
    lastVisiblePrice: {
      color: '#777',
      enabled: true
    }
  },
  bb: {
    bottomLine: {
      styles: {
        lineWidth: 2
      }
    },
    fillColor: '#ccc',
    topLine: {
      styles: {
        lineWidth: 3
      }
    },

    compare: 'percent',
    compareBase: 0,

    compareStart: true,
    compareToMain: true,
    name: 'Some-Name-Goes-Here',
    params: {
      index: 0,
      period: 2
    },

    colorAxis: 1,
    connectEnds: true,
    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true
    },
    negativeColor: '#fff',
    pointInterval: 5,
    pointIntervalUnit: 'weeks',
    pointPlacement: 'on',
    pointStart: 12,
    stacking: 'normal',

    animationLimit: 10,
    boostBlending: '#ccc',
    boostThreshold: 1234,
    colorIndex: 5,
    colorKey: 'some-key-value',
    connectNulls: true,
    crisp: true,
    cropThreshold: 123,
    dataSorting: {
        enabled: true,
        matchByName: true,
        sortKey: 'some-key-value'
    },
    findNearestPointBy: 'x',
    getExtremesFromAll: true,
    linecap: 'round',
    lineWidth: 2,
    relativeXValue: true,
    shadow: false,
    softThreshold: true,
    step: 'left',
    zoneAxis: 'y',
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ],

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'bb',

    cumulative: false,
    dataAsColumns: false,
    gapSize: 6,
    gapUnit: 'relative',
    lastPrice: {
      color: '#ccc',
      enabled: true
    },
    lastVisiblePrice: {
      color: '#777',
      enabled: true
    }
  },
  candlestick: {
    pointValKey: 'close',
    upColor: '#ccc',
    upLineColor: '#777',

    centerInCategory: true,
    colorByPoint: true,
    colors: [
        '#fff',
        '#ccc',
        {
          linearGradient: {
              x1: 0.123,
              x2: 0.567,
              y1: 0.891,
              y2: 0.987
          },
          stops: [
              [0.123, '#cccccc'],
              [0.456, '#ff0000'],
              [1, '#00ff00']
          ]
        },
        {
          animation: {
              defer: 5
          },
          patternOptions: {
              aspectRatio: 0.5,
              backgroundColor: '#999999',
              id: 'some_id_goes_here',
              opacity: 0.5,
              width: 120,
              x: 5,
              y: 10
          },
          patternIndex: 2
        }
    ],
    grouping: false,
    groupPadding: 6,
    maxPointWidth: 12,
    minPointLength: 12,
    pointPadding: 6,
    pointRange: 24,
    pointWidth: 12,

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,

    type: 'candlestick',

    compare: 'percent',
    compareBase: 100,
    navigatorOptions: {
      adaptToUpdatedData: true,
      enabled: true,
      handles: {
        backgroundColor: '#ccc',
        borderColor: '#777',
        enabled: true,
        height: 24,
        lineWidth: 2,
        symbols: [
          'navigator-handle',
          'navigator-handle'
        ],
        width: 24
      },
      height: 120,
      margin: 6,
      maskFill: '#ccc',
      maskInside: true,
      opposite: false,
      outlineColor: '#777',
      outlineWidth: 1,
      xAxis: {
          crosshair: {
              className: 'some-class-name',
              color: '#ccc',
              dashStyle: 'Dash',
              snap: true,
              width: 40,
              zIndex: 6
          },
          height: 60,
          left: 5,
          lineColor: '#999',
          lineWidth: 1,
          showEmpty: true,
          top: 340,
          width: 300
      },
      yAxis: {
        maxLength: '100%',
        maxRange: 123,
        minLength: '20%',
        range: 123,
        resize: {
          controlledAxis: {
            next: [1, 2, 3],
            prev: [0, 'some-id']
          },
          cursor: 'pointer',
          enabled: true,
          lineColor: '#777',
          lineDashStyle: 'Solid',
          lineWidth: 2,
          x: 0,
          y: 0
        },
        scrollbar: {
          barBackgroundColor: '#ccc',
          barBorderColor: '#777',
          barBorderRadius: 2,
          barBorderWidth: 2,
          buttonArrowColor: '#333',
          buttonBackgroundColor: '#ccc',
          buttonBorderColor: '#000',
          buttonBorderRadius: 2,
          buttonBorderWidth: 3,
          enabled: true,
          height: 120,
          liveRedraw: false,
          margin: 6,
          minWidth: 8,
          rifleColor: '#ccc',
          showFull: false,
          trackBackgroundColor: '#ccc',
          trackBorderColor: '#fff',
          trackBorderRadius: 0,
          trackBorderWidth: 2,
          zIndex: 3
        }
      }
    },
    showInNavigator: true
  },
  cci: {
    compare: 'percent',
    compareBase: 0,

    compareStart: true,
    compareToMain: true,
    name: 'Some-Name-Goes-Here',
    params: {
      index: 0,
      period: 2
    },

    colorAxis: 1,
    connectEnds: true,
    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true
    },
    negativeColor: '#fff',
    pointInterval: 5,
    pointIntervalUnit: 'weeks',
    pointPlacement: 'on',
    pointStart: 12,
    stacking: 'normal',

    animationLimit: 10,
    boostBlending: '#ccc',
    boostThreshold: 1234,
    colorIndex: 5,
    colorKey: 'some-key-value',
    connectNulls: true,
    crisp: true,
    cropThreshold: 123,
    dataSorting: {
        enabled: true,
        matchByName: true,
        sortKey: 'some-key-value'
    },
    findNearestPointBy: 'x',
    getExtremesFromAll: true,
    linecap: 'round',
    lineWidth: 2,
    relativeXValue: true,
    shadow: false,
    softThreshold: true,
    step: 'left',
    zoneAxis: 'y',
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ],

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'cci',

    cumulative: false,
    dataAsColumns: false,
    gapSize: 6,
    gapUnit: 'relative',
    lastPrice: {
      color: '#ccc',
      enabled: true
    },
    lastVisiblePrice: {
      color: '#777',
      enabled: true
    }
  },
  chaikin: {
    compare: 'percent',
    compareBase: 0,

    compareStart: true,
    compareToMain: true,
    name: 'Some-Name-Goes-Here',
    params: {
      index: 0,
      period: 2
    },

    colorAxis: 1,
    connectEnds: true,
    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true
    },
    negativeColor: '#fff',
    pointInterval: 5,
    pointIntervalUnit: 'weeks',
    pointPlacement: 'on',
    pointStart: 12,
    stacking: 'normal',

    animationLimit: 10,
    boostBlending: '#ccc',
    boostThreshold: 1234,
    colorIndex: 5,
    colorKey: 'some-key-value',
    connectNulls: true,
    crisp: true,
    cropThreshold: 123,
    dataSorting: {
        enabled: true,
        matchByName: true,
        sortKey: 'some-key-value'
    },
    findNearestPointBy: 'x',
    getExtremesFromAll: true,
    linecap: 'round',
    lineWidth: 2,
    relativeXValue: true,
    shadow: false,
    softThreshold: true,
    step: 'left',
    zoneAxis: 'y',
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ],

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'chaikin',

    cumulative: false,
    dataAsColumns: false,
    gapSize: 6,
    gapUnit: 'relative',
    lastPrice: {
      color: '#ccc',
      enabled: true
    },
    lastVisiblePrice: {
      color: '#777',
      enabled: true
    }
  },
  cmf: {
    compare: 'percent',
    compareBase: 0,

    compareStart: true,
    compareToMain: true,
    name: 'Some-Name-Goes-Here',
    params: {
      period: 2,
      volumeSeriesID: 'some-id-goes-here',
    },

    colorAxis: 1,
    connectEnds: true,
    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true
    },
    negativeColor: '#fff',
    pointInterval: 5,
    pointIntervalUnit: 'weeks',
    pointPlacement: 'on',
    pointStart: 12,
    stacking: 'normal',

    animationLimit: 10,
    boostBlending: '#ccc',
    boostThreshold: 1234,
    colorIndex: 5,
    colorKey: 'some-key-value',
    connectNulls: true,
    crisp: true,
    cropThreshold: 123,
    dataSorting: {
        enabled: true,
        matchByName: true,
        sortKey: 'some-key-value'
    },
    findNearestPointBy: 'x',
    getExtremesFromAll: true,
    linecap: 'round',
    lineWidth: 2,
    relativeXValue: true,
    shadow: false,
    softThreshold: true,
    step: 'left',
    zoneAxis: 'y',
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ],

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'cmf',

    cumulative: false,
    dataAsColumns: false,
    gapSize: 6,
    gapUnit: 'relative',
    lastPrice: {
      color: '#ccc',
      enabled: true
    },
    lastVisiblePrice: {
      color: '#777',
      enabled: true
    }
  },
  cmo: {
    compare: 'percent',
    compareBase: 0,

    compareStart: true,
    compareToMain: true,
    name: 'Some-Name-Goes-Here',
    params: {
      index: 0,
      period: 2
    },

    colorAxis: 1,
    connectEnds: true,
    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true
    },
    negativeColor: '#fff',
    pointInterval: 5,
    pointIntervalUnit: 'weeks',
    pointPlacement: 'on',
    pointStart: 12,
    stacking: 'normal',

    animationLimit: 10,
    boostBlending: '#ccc',
    boostThreshold: 1234,
    colorIndex: 5,
    colorKey: 'some-key-value',
    connectNulls: true,
    crisp: true,
    cropThreshold: 123,
    dataSorting: {
        enabled: true,
        matchByName: true,
        sortKey: 'some-key-value'
    },
    findNearestPointBy: 'x',
    getExtremesFromAll: true,
    linecap: 'round',
    lineWidth: 2,
    relativeXValue: true,
    shadow: false,
    softThreshold: true,
    step: 'left',
    zoneAxis: 'y',
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ],

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'cmo',

    cumulative: false,
    dataAsColumns: false,
    gapSize: 6,
    gapUnit: 'relative',
    lastPrice: {
      color: '#ccc',
      enabled: true
    },
    lastVisiblePrice: {
      color: '#777',
      enabled: true
    }
  },
  dema: {
    compareStart: true,
    compareToMain: true,
    name: 'Some-Name-Goes-Here',
    params: {
      index: 0,
      period: 2
    },

    colorAxis: 1,
    connectEnds: true,
    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true
    },
    negativeColor: '#fff',
    pointInterval: 5,
    pointIntervalUnit: 'weeks',
    pointPlacement: 'on',
    pointStart: 12,
    stacking: 'normal',

    animationLimit: 10,
    boostBlending: '#ccc',
    boostThreshold: 1234,
    colorIndex: 5,
    colorKey: 'some-key-value',
    connectNulls: true,
    crisp: true,
    cropThreshold: 123,
    dataSorting: {
        enabled: true,
        matchByName: true,
        sortKey: 'some-key-value'
    },
    findNearestPointBy: 'x',
    getExtremesFromAll: true,
    linecap: 'round',
    lineWidth: 2,
    relativeXValue: true,
    shadow: false,
    softThreshold: true,
    step: 'left',
    zoneAxis: 'y',
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ],

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'dema',

    cumulative: false,
    dataAsColumns: false,
    gapSize: 6,
    gapUnit: 'relative',
    lastPrice: {
      color: '#ccc',
      enabled: true
    },
    lastVisiblePrice: {
      color: '#777',
      enabled: true
    }
  },
  disparityindex: {
    compareStart: true,
    compareToMain: true,
    name: 'Some-Name-Goes-Here',
    params: {
      index: 0,
      period: 2,
      average: 'sma'
    },

    colorAxis: 1,
    connectEnds: true,
    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true
    },
    negativeColor: '#fff',
    pointInterval: 5,
    pointIntervalUnit: 'weeks',
    pointPlacement: 'on',
    pointStart: 12,
    stacking: 'normal',

    animationLimit: 10,
    boostBlending: '#ccc',
    boostThreshold: 1234,
    colorIndex: 5,
    colorKey: 'some-key-value',
    connectNulls: true,
    crisp: true,
    cropThreshold: 123,
    dataSorting: {
        enabled: true,
        matchByName: true,
        sortKey: 'some-key-value'
    },
    findNearestPointBy: 'x',
    getExtremesFromAll: true,
    linecap: 'round',
    lineWidth: 2,
    relativeXValue: true,
    shadow: false,
    softThreshold: true,
    step: 'left',
    zoneAxis: 'y',
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ],

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'disparityindex',

    cumulative: false,
    dataAsColumns: false,
    gapSize: 6,
    gapUnit: 'relative',
    lastPrice: {
      color: '#ccc',
      enabled: true
    },
    lastVisiblePrice: {
      color: '#777',
      enabled: true
    }
  },
  dmi: {
    minusDILine: {
      styles: {
        lineWidth: 2,
        lineColor: '#ccc'
      }
    },
    plusDILine: {
      styles: {
        lineWidth: 2,
        lineColor: '#fff'
      }
    },

    compareStart: true,
    compareToMain: true,
    name: 'Some-Name-Goes-Here',
    params: {
      period: 2
    },

    colorAxis: 1,
    connectEnds: true,
    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true
    },
    negativeColor: '#fff',
    pointInterval: 5,
    pointIntervalUnit: 'weeks',
    pointPlacement: 'on',
    pointStart: 12,
    stacking: 'normal',

    animationLimit: 10,
    boostBlending: '#ccc',
    boostThreshold: 1234,
    colorIndex: 5,
    colorKey: 'some-key-value',
    connectNulls: true,
    crisp: true,
    cropThreshold: 123,
    dataSorting: {
        enabled: true,
        matchByName: true,
        sortKey: 'some-key-value'
    },
    findNearestPointBy: 'x',
    getExtremesFromAll: true,
    linecap: 'round',
    lineWidth: 2,
    relativeXValue: true,
    shadow: false,
    softThreshold: true,
    step: 'left',
    zoneAxis: 'y',
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ],

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'dmi',

    cumulative: false,
    dataAsColumns: false,
    gapSize: 6,
    gapUnit: 'relative',
    lastPrice: {
      color: '#ccc',
      enabled: true
    },
    lastVisiblePrice: {
      color: '#777',
      enabled: true
    }
  },
  dpo: {
    compareStart: true,
    compareToMain: true,
    name: 'Some-Name-Goes-Here',
    params: {
      index: 0,
      period: 2
    },

    colorAxis: 1,
    connectEnds: true,
    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true
    },
    negativeColor: '#fff',
    pointInterval: 5,
    pointIntervalUnit: 'weeks',
    pointPlacement: 'on',
    pointStart: 12,
    stacking: 'normal',

    animationLimit: 10,
    boostBlending: '#ccc',
    boostThreshold: 1234,
    colorIndex: 5,
    colorKey: 'some-key-value',
    connectNulls: true,
    crisp: true,
    cropThreshold: 123,
    dataSorting: {
        enabled: true,
        matchByName: true,
        sortKey: 'some-key-value'
    },
    findNearestPointBy: 'x',
    getExtremesFromAll: true,
    linecap: 'round',
    lineWidth: 2,
    relativeXValue: true,
    shadow: false,
    softThreshold: true,
    step: 'left',
    zoneAxis: 'y',
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ],

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'dpo',

    cumulative: false,
    dataAsColumns: false,
    gapSize: 6,
    gapUnit: 'relative',
    lastPrice: {
      color: '#ccc',
      enabled: true
    },
    lastVisiblePrice: {
      color: '#777',
      enabled: true
    }
  },
  ema: {
    compareStart: true,
    compareToMain: true,
    name: 'Some-Name-Goes-Here',
    params: {
      index: 0,
      period: 2
    },

    colorAxis: 1,
    connectEnds: true,
    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true
    },
    negativeColor: '#fff',
    pointInterval: 5,
    pointIntervalUnit: 'weeks',
    pointPlacement: 'on',
    pointStart: 12,
    stacking: 'normal',

    animationLimit: 10,
    boostBlending: '#ccc',
    boostThreshold: 1234,
    colorIndex: 5,
    colorKey: 'some-key-value',
    connectNulls: true,
    crisp: true,
    cropThreshold: 123,
    dataSorting: {
        enabled: true,
        matchByName: true,
        sortKey: 'some-key-value'
    },
    findNearestPointBy: 'x',
    getExtremesFromAll: true,
    linecap: 'round',
    lineWidth: 2,
    relativeXValue: true,
    shadow: false,
    softThreshold: true,
    step: 'left',
    zoneAxis: 'y',
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ],

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'ema',

    cumulative: false,
    dataAsColumns: false,
    gapSize: 6,
    gapUnit: 'relative',
    lastPrice: {
      color: '#ccc',
      enabled: true
    },
    lastVisiblePrice: {
      color: '#777',
      enabled: true
    }
  },
  flags: {
    allowOverlapX: true,
    centerInCategory: true,
    colors: [
        '#fff',
        '#ccc',
        {
          linearGradient: {
              x1: 0.123,
              x2: 0.567,
              y1: 0.891,
              y2: 0.987
          },
          stops: [
              [0.123, '#cccccc'],
              [0.456, '#ff0000'],
              [1, '#00ff00']
          ]
        },
        {
          animation: {
              defer: 5
          },
          patternOptions: {
              aspectRatio: 0.5,
              backgroundColor: '#999999',
              id: 'some_id_goes_here',
              opacity: 0.5,
              width: 120,
              x: 5,
              y: 10
          },
          patternIndex: 2
        }
    ],
    groupPadding: 6,
    grouping: false,
    height: 123,
    lineColor: '#ccc',
    maxPointWidth: 12,
    minPointLength: 12,
    onKey: 'y',
    onSeries: 'some-series-id',
    shape: 'flag',
    stackDistance: 12,
    style: 'some-string-goes-here',
    textAlign: 'center',
    title: 'Some Title Goes Here',
    useHTML: false,
    width: 320,
    y: -30,


    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,

    type: 'flags',

    compare: 'percent',
    compareBase: 100,
    navigatorOptions: {
      adaptToUpdatedData: true,
      enabled: true,
      handles: {
        backgroundColor: '#ccc',
        borderColor: '#777',
        enabled: true,
        height: 24,
        lineWidth: 2,
        symbols: [
          'navigator-handle',
          'navigator-handle'
        ],
        width: 24
      },
      height: 120,
      margin: 6,
      maskFill: '#ccc',
      maskInside: true,
      opposite: false,
      outlineColor: '#777',
      outlineWidth: 1,
      xAxis: {
          crosshair: {
              className: 'some-class-name',
              color: '#ccc',
              dashStyle: 'Dash',
              snap: true,
              width: 40,
              zIndex: 6
          },
          height: 60,
          left: 5,
          lineColor: '#999',
          lineWidth: 1,
          showEmpty: true,
          top: 340,
          width: 300
      },
      yAxis: {
        maxLength: '100%',
        maxRange: 123,
        minLength: '20%',
        range: 123,
        resize: {
          controlledAxis: {
            next: [1, 2, 3],
            prev: [0, 'some-id']
          },
          cursor: 'pointer',
          enabled: true,
          lineColor: '#777',
          lineDashStyle: 'Solid',
          lineWidth: 2,
          x: 0,
          y: 0
        },
        scrollbar: {
          barBackgroundColor: '#ccc',
          barBorderColor: '#777',
          barBorderRadius: 2,
          barBorderWidth: 2,
          buttonArrowColor: '#333',
          buttonBackgroundColor: '#ccc',
          buttonBorderColor: '#000',
          buttonBorderRadius: 2,
          buttonBorderWidth: 3,
          enabled: true,
          height: 120,
          liveRedraw: false,
          margin: 6,
          minWidth: 8,
          rifleColor: '#ccc',
          showFull: false,
          trackBackgroundColor: '#ccc',
          trackBorderColor: '#fff',
          trackBorderRadius: 0,
          trackBorderWidth: 2,
          zIndex: 3
        }
      }
    },
    pointRange: 24,
    showInNavigator: true

  },
  heikinashi: {
    pointValKey: 'close',
    upColor: '#ccc',
    upLineColor: '#777',

    centerInCategory: true,
    colorByPoint: true,
    colors: [
        '#fff',
        '#ccc',
        {
          linearGradient: {
              x1: 0.123,
              x2: 0.567,
              y1: 0.891,
              y2: 0.987
          },
          stops: [
              [0.123, '#cccccc'],
              [0.456, '#ff0000'],
              [1, '#00ff00']
          ]
        },
        {
          animation: {
              defer: 5
          },
          patternOptions: {
              aspectRatio: 0.5,
              backgroundColor: '#999999',
              id: 'some_id_goes_here',
              opacity: 0.5,
              width: 120,
              x: 5,
              y: 10
          },
          patternIndex: 2
        }
    ],
    grouping: false,
    groupPadding: 6,
    maxPointWidth: 12,
    minPointLength: 12,
    pointPadding: 6,
    pointRange: 24,
    pointWidth: 12,

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,

    type: 'heikinashi',

    compare: 'percent',
    compareBase: 100,
    navigatorOptions: {
      adaptToUpdatedData: true,
      enabled: true,
      handles: {
        backgroundColor: '#ccc',
        borderColor: '#777',
        enabled: true,
        height: 24,
        lineWidth: 2,
        symbols: [
          'navigator-handle',
          'navigator-handle'
        ],
        width: 24
      },
      height: 120,
      margin: 6,
      maskFill: '#ccc',
      maskInside: true,
      opposite: false,
      outlineColor: '#777',
      outlineWidth: 1,
      xAxis: {
          crosshair: {
              className: 'some-class-name',
              color: '#ccc',
              dashStyle: 'Dash',
              snap: true,
              width: 40,
              zIndex: 6
          },
          height: 60,
          left: 5,
          lineColor: '#999',
          lineWidth: 1,
          showEmpty: true,
          top: 340,
          width: 300
      },
      yAxis: {
        maxLength: '100%',
        maxRange: 123,
        minLength: '20%',
        range: 123,
        resize: {
          controlledAxis: {
            next: [1, 2, 3],
            prev: [0, 'some-id']
          },
          cursor: 'pointer',
          enabled: true,
          lineColor: '#777',
          lineDashStyle: 'Solid',
          lineWidth: 2,
          x: 0,
          y: 0
        },
        scrollbar: {
          barBackgroundColor: '#ccc',
          barBorderColor: '#777',
          barBorderRadius: 2,
          barBorderWidth: 2,
          buttonArrowColor: '#333',
          buttonBackgroundColor: '#ccc',
          buttonBorderColor: '#000',
          buttonBorderRadius: 2,
          buttonBorderWidth: 3,
          enabled: true,
          height: 120,
          liveRedraw: false,
          margin: 6,
          minWidth: 8,
          rifleColor: '#ccc',
          showFull: false,
          trackBackgroundColor: '#ccc',
          trackBorderColor: '#fff',
          trackBorderRadius: 0,
          trackBorderWidth: 2,
          zIndex: 3
        }
      }
    },
    showInNavigator: true
  },
  hlc: {
    pointValKey: 'close',
    upLineColor: '#777',

    centerInCategory: true,
    colorByPoint: true,
    colors: [
        '#fff',
        '#ccc',
        {
          linearGradient: {
              x1: 0.123,
              x2: 0.567,
              y1: 0.891,
              y2: 0.987
          },
          stops: [
              [0.123, '#cccccc'],
              [0.456, '#ff0000'],
              [1, '#00ff00']
          ]
        },
        {
          animation: {
              defer: 5
          },
          patternOptions: {
              aspectRatio: 0.5,
              backgroundColor: '#999999',
              id: 'some_id_goes_here',
              opacity: 0.5,
              width: 120,
              x: 5,
              y: 10
          },
          patternIndex: 2
        }
    ],
    grouping: false,
    groupPadding: 6,
    maxPointWidth: 12,
    minPointLength: 12,
    pointPadding: 6,
    pointRange: 24,
    pointWidth: 12,

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,

    type: 'hlc',

    compare: 'percent',
    compareBase: 100,
    navigatorOptions: {
      adaptToUpdatedData: true,
      enabled: true,
      handles: {
        backgroundColor: '#ccc',
        borderColor: '#777',
        enabled: true,
        height: 24,
        lineWidth: 2,
        symbols: [
          'navigator-handle',
          'navigator-handle'
        ],
        width: 24
      },
      height: 120,
      margin: 6,
      maskFill: '#ccc',
      maskInside: true,
      opposite: false,
      outlineColor: '#777',
      outlineWidth: 1,
      xAxis: {
          crosshair: {
              className: 'some-class-name',
              color: '#ccc',
              dashStyle: 'Dash',
              snap: true,
              width: 40,
              zIndex: 6
          },
          height: 60,
          left: 5,
          lineColor: '#999',
          lineWidth: 1,
          showEmpty: true,
          top: 340,
          width: 300
      },
      yAxis: {
        maxLength: '100%',
        maxRange: 123,
        minLength: '20%',
        range: 123,
        resize: {
          controlledAxis: {
            next: [1, 2, 3],
            prev: [0, 'some-id']
          },
          cursor: 'pointer',
          enabled: true,
          lineColor: '#777',
          lineDashStyle: 'Solid',
          lineWidth: 2,
          x: 0,
          y: 0
        },
        scrollbar: {
          barBackgroundColor: '#ccc',
          barBorderColor: '#777',
          barBorderRadius: 2,
          barBorderWidth: 2,
          buttonArrowColor: '#333',
          buttonBackgroundColor: '#ccc',
          buttonBorderColor: '#000',
          buttonBorderRadius: 2,
          buttonBorderWidth: 3,
          enabled: true,
          height: 120,
          liveRedraw: false,
          margin: 6,
          minWidth: 8,
          rifleColor: '#ccc',
          showFull: false,
          trackBackgroundColor: '#ccc',
          trackBorderColor: '#fff',
          trackBorderRadius: 0,
          trackBorderWidth: 2,
          zIndex: 3
        }
      }
    },
    showInNavigator: true
  },
  hollowcandlestick: {
    pointValKey: 'close',
    upColor: '#ccc',
    upLineColor: '#777',

    centerInCategory: true,
    colorByPoint: true,
    colors: [
        '#fff',
        '#ccc',
        {
          linearGradient: {
              x1: 0.123,
              x2: 0.567,
              y1: 0.891,
              y2: 0.987
          },
          stops: [
              [0.123, '#cccccc'],
              [0.456, '#ff0000'],
              [1, '#00ff00']
          ]
        },
        {
          animation: {
              defer: 5
          },
          patternOptions: {
              aspectRatio: 0.5,
              backgroundColor: '#999999',
              id: 'some_id_goes_here',
              opacity: 0.5,
              width: 120,
              x: 5,
              y: 10
          },
          patternIndex: 2
        }
    ],
    grouping: false,
    groupPadding: 6,
    maxPointWidth: 12,
    minPointLength: 12,
    pointPadding: 6,
    pointRange: 24,
    pointWidth: 12,

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,

    type: 'hollowcandlestick',

    compare: 'percent',
    compareBase: 100,
    navigatorOptions: {
      adaptToUpdatedData: true,
      enabled: true,
      handles: {
        backgroundColor: '#ccc',
        borderColor: '#777',
        enabled: true,
        height: 24,
        lineWidth: 2,
        symbols: [
          'navigator-handle',
          'navigator-handle'
        ],
        width: 24
      },
      height: 120,
      margin: 6,
      maskFill: '#ccc',
      maskInside: true,
      opposite: false,
      outlineColor: '#777',
      outlineWidth: 1,
      xAxis: {
          crosshair: {
              className: 'some-class-name',
              color: '#ccc',
              dashStyle: 'Dash',
              snap: true,
              width: 40,
              zIndex: 6
          },
          height: 60,
          left: 5,
          lineColor: '#999',
          lineWidth: 1,
          showEmpty: true,
          top: 340,
          width: 300
      },
      yAxis: {
        maxLength: '100%',
        maxRange: 123,
        minLength: '20%',
        range: 123,
        resize: {
          controlledAxis: {
            next: [1, 2, 3],
            prev: [0, 'some-id']
          },
          cursor: 'pointer',
          enabled: true,
          lineColor: '#777',
          lineDashStyle: 'Solid',
          lineWidth: 2,
          x: 0,
          y: 0
        },
        scrollbar: {
          barBackgroundColor: '#ccc',
          barBorderColor: '#777',
          barBorderRadius: 2,
          barBorderWidth: 2,
          buttonArrowColor: '#333',
          buttonBackgroundColor: '#ccc',
          buttonBorderColor: '#000',
          buttonBorderRadius: 2,
          buttonBorderWidth: 3,
          enabled: true,
          height: 120,
          liveRedraw: false,
          margin: 6,
          minWidth: 8,
          rifleColor: '#ccc',
          showFull: false,
          trackBackgroundColor: '#ccc',
          trackBorderColor: '#fff',
          trackBorderRadius: 0,
          trackBorderWidth: 2,
          zIndex: 3
        }
      }
    },
    showInNavigator: true
  },
  ikh: {
    chikouLine: {
      styles: {
        lineWidth: 2,
        lineColor: '#ccc'
      }
    },
    kijunLine: {
      styles: {
        lineWidth: 2,
        lineColor: '#ccc'
      }
    },
    senkouSpan: {
      color: '#ccc',
      negativeColor: '#777'
    },
    senkouSpanA: {
      styles: {
        lineWidth: 2,
        lineColor: '#ccc'
      }
    },
    senkouSpanB: {
      styles: {
        lineWidth: 2,
        lineColor: '#ccc'
      }
    },
    tenkanLine: {
      styles: {
        lineWidth: 2,
        lineColor: '#ccc'
      }
    },

    compareStart: true,
    compareToMain: true,
    name: 'Some-Name-Goes-Here',
    params: {
      period: 20,
      periodSenkouSpanB: 52,
      periodTenkan: 9
    },

    colorAxis: 1,
    connectEnds: true,
    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true
    },
    negativeColor: '#fff',
    pointInterval: 5,
    pointIntervalUnit: 'weeks',
    pointPlacement: 'on',
    pointStart: 12,
    stacking: 'normal',

    animationLimit: 10,
    boostBlending: '#ccc',
    boostThreshold: 1234,
    colorIndex: 5,
    colorKey: 'some-key-value',
    connectNulls: true,
    crisp: true,
    cropThreshold: 123,
    dataSorting: {
        enabled: true,
        matchByName: true,
        sortKey: 'some-key-value'
    },
    findNearestPointBy: 'x',
    getExtremesFromAll: true,
    linecap: 'round',
    lineWidth: 2,
    relativeXValue: true,
    shadow: false,
    softThreshold: true,
    step: 'left',
    zoneAxis: 'y',
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ],

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'ikh',

    cumulative: false,
    dataAsColumns: false,
    gapSize: 6,
    gapUnit: 'relative',
    lastPrice: {
      color: '#ccc',
      enabled: true
    },
    lastVisiblePrice: {
      color: '#777',
      enabled: true
    }
  },
  keltnerchannels: {
    bottomLine: {
      styles: {
        lineWidth: 2
      }
    },
    fillColor: '#ccc',
    topLine: {
      styles: {
        lineWidth: 3
      }
    },

    compareStart: true,
    compareToMain: true,
    name: 'Some-Name-Goes-Here',
    params: {
      index: 0,
      period: 2
    },

    colorAxis: 1,
    connectEnds: true,
    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true
    },
    negativeColor: '#fff',
    pointInterval: 5,
    pointIntervalUnit: 'weeks',
    pointPlacement: 'on',
    pointStart: 12,
    stacking: 'normal',

    animationLimit: 10,
    boostBlending: '#ccc',
    boostThreshold: 1234,
    colorIndex: 5,
    colorKey: 'some-key-value',
    connectNulls: true,
    crisp: true,
    cropThreshold: 123,
    dataSorting: {
        enabled: true,
        matchByName: true,
        sortKey: 'some-key-value'
    },
    findNearestPointBy: 'x',
    getExtremesFromAll: true,
    linecap: 'round',
    lineWidth: 2,
    relativeXValue: true,
    shadow: false,
    softThreshold: true,
    step: 'left',
    zoneAxis: 'y',
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ],

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'keltnerchannels',

    cumulative: false,
    dataAsColumns: false,
    gapSize: 6,
    gapUnit: 'relative',
    lastPrice: {
      color: '#ccc',
      enabled: true
    },
    lastVisiblePrice: {
      color: '#777',
      enabled: true
    }
  },
  klinger: {
    signalLine: {
      styles: {
        lineWidth: 2,
        lineColor: '#ccc'
      }
    },

    compare: 'percent',
    compareBase: 0,

    compareStart: true,
    compareToMain: true,
    name: 'Some-Name-Goes-Here',
    params: {
      fastAvgPeriod: 3,
      signalPeriod: 4,
      slowAvgPeriod: 5,
      volumeSeriesID: 'some-id-goes-here'
    },

    colorAxis: 1,
    connectEnds: true,
    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true
    },
    negativeColor: '#fff',
    pointInterval: 5,
    pointIntervalUnit: 'weeks',
    pointPlacement: 'on',
    pointStart: 12,
    stacking: 'normal',

    animationLimit: 10,
    boostBlending: '#ccc',
    boostThreshold: 1234,
    colorIndex: 5,
    colorKey: 'some-key-value',
    connectNulls: true,
    crisp: true,
    cropThreshold: 123,
    dataSorting: {
        enabled: true,
        matchByName: true,
        sortKey: 'some-key-value'
    },
    findNearestPointBy: 'x',
    getExtremesFromAll: true,
    linecap: 'round',
    lineWidth: 2,
    relativeXValue: true,
    shadow: false,
    softThreshold: true,
    step: 'left',
    zoneAxis: 'y',
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ],

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'klinger',

    cumulative: false,
    dataAsColumns: false,
    gapSize: 6,
    gapUnit: 'relative',
    lastPrice: {
      color: '#ccc',
      enabled: true
    },
    lastVisiblePrice: {
      color: '#777',
      enabled: true
    }
  },
  linearregression: {
    compareStart: true,
    compareToMain: true,
    name: 'Some-Name-Goes-Here',
    params: {
      index: 0,
      period: 2,
      xAxisUnit: 86400000
    },

    colorAxis: 1,
    connectEnds: true,
    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true
    },
    negativeColor: '#fff',
    pointInterval: 5,
    pointIntervalUnit: 'weeks',
    pointPlacement: 'on',
    pointStart: 12,
    stacking: 'normal',

    animationLimit: 10,
    boostBlending: '#ccc',
    boostThreshold: 1234,
    colorIndex: 5,
    colorKey: 'some-key-value',
    connectNulls: true,
    crisp: true,
    cropThreshold: 123,
    dataSorting: {
        enabled: true,
        matchByName: true,
        sortKey: 'some-key-value'
    },
    findNearestPointBy: 'x',
    getExtremesFromAll: true,
    linecap: 'round',
    lineWidth: 2,
    relativeXValue: true,
    shadow: false,
    softThreshold: true,
    step: 'left',
    zoneAxis: 'y',
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ],

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'linearregression',

    cumulative: false,
    dataAsColumns: false,
    gapSize: 6,
    gapUnit: 'relative',
    lastPrice: {
      color: '#ccc',
      enabled: true
    },
    lastVisiblePrice: {
      color: '#777',
      enabled: true
    }
  },
  linearregressionangle: {
    compareStart: true,
    compareToMain: true,
    name: 'Some-Name-Goes-Here',
    params: {
      index: 0,
      period: 2,
      xAxisUnit: 86400000
    },

    colorAxis: 1,
    connectEnds: true,
    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true
    },
    negativeColor: '#fff',
    pointInterval: 5,
    pointIntervalUnit: 'weeks',
    pointPlacement: 'on',
    pointStart: 12,
    stacking: 'normal',

    animationLimit: 10,
    boostBlending: '#ccc',
    boostThreshold: 1234,
    colorIndex: 5,
    colorKey: 'some-key-value',
    connectNulls: true,
    crisp: true,
    cropThreshold: 123,
    dataSorting: {
        enabled: true,
        matchByName: true,
        sortKey: 'some-key-value'
    },
    findNearestPointBy: 'x',
    getExtremesFromAll: true,
    linecap: 'round',
    lineWidth: 2,
    relativeXValue: true,
    shadow: false,
    softThreshold: true,
    step: 'left',
    zoneAxis: 'y',
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ],

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'linearregressionangle',

    cumulative: false,
    dataAsColumns: false,
    gapSize: 6,
    gapUnit: 'relative',
    lastPrice: {
      color: '#ccc',
      enabled: true
    },
    lastVisiblePrice: {
      color: '#777',
      enabled: true
    }
  },
  linearregressionintercept: {
    compareStart: true,
    compareToMain: true,
    name: 'Some-Name-Goes-Here',
    params: {
      index: 0,
      period: 2,
      xAxisUnit: 86400000
    },

    colorAxis: 1,
    connectEnds: true,
    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true
    },
    negativeColor: '#fff',
    pointInterval: 5,
    pointIntervalUnit: 'weeks',
    pointPlacement: 'on',
    pointStart: 12,
    stacking: 'normal',

    animationLimit: 10,
    boostBlending: '#ccc',
    boostThreshold: 1234,
    colorIndex: 5,
    colorKey: 'some-key-value',
    connectNulls: true,
    crisp: true,
    cropThreshold: 123,
    dataSorting: {
        enabled: true,
        matchByName: true,
        sortKey: 'some-key-value'
    },
    findNearestPointBy: 'x',
    getExtremesFromAll: true,
    linecap: 'round',
    lineWidth: 2,
    relativeXValue: true,
    shadow: false,
    softThreshold: true,
    step: 'left',
    zoneAxis: 'y',
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ],

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'linearregressionintercept',

    cumulative: false,
    dataAsColumns: false,
    gapSize: 6,
    gapUnit: 'relative',
    lastPrice: {
      color: '#ccc',
      enabled: true
    },
    lastVisiblePrice: {
      color: '#777',
      enabled: true
    }
  },
  linearregressionslope: {
    compareStart: true,
    compareToMain: true,
    name: 'Some-Name-Goes-Here',
    params: {
      index: 0,
      period: 2,
      xAxisUnit: 86400000
    },

    colorAxis: 1,
    connectEnds: true,
    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true
    },
    negativeColor: '#fff',
    pointInterval: 5,
    pointIntervalUnit: 'weeks',
    pointPlacement: 'on',
    pointStart: 12,
    stacking: 'normal',

    animationLimit: 10,
    boostBlending: '#ccc',
    boostThreshold: 1234,
    colorIndex: 5,
    colorKey: 'some-key-value',
    connectNulls: true,
    crisp: true,
    cropThreshold: 123,
    dataSorting: {
        enabled: true,
        matchByName: true,
        sortKey: 'some-key-value'
    },
    findNearestPointBy: 'x',
    getExtremesFromAll: true,
    linecap: 'round',
    lineWidth: 2,
    relativeXValue: true,
    shadow: false,
    softThreshold: true,
    step: 'left',
    zoneAxis: 'y',
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ],

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'linearregressionslope',

    cumulative: false,
    dataAsColumns: false,
    gapSize: 6,
    gapUnit: 'relative',
    lastPrice: {
      color: '#ccc',
      enabled: true
    },
    lastVisiblePrice: {
      color: '#777',
      enabled: true
    }
  },
  macd: {
    groupPadding: 4,
    macdLine: {
      styles: {
        lineWidth: 2,
        lineColor: '#ccc'
      },
      zones:  [
          {
            className: 'some-class-name1',
            color: '#999999',
            dashStyle: 'Solid',
            fillColor: '#cccccc',
            value: 123
          },
          {
            className: 'some-class-name1',
            color: '#999999',
            dashStyle: 'Solid',
            fillColor: '#cccccc',
            value: 123
          },
          {
            className: 'some-class-name1',
            color: '#999999',
            dashStyle: 'Solid',
            fillColor: '#cccccc',
            value: 123
          }
      ]
    },
    minPointLength: 4,
    pointPadding: 6,
    signalLine: {
      styles: {
        lineWidth: 2,
        lineColor: '#ccc'
      },
      zones:  [
          {
            className: 'some-class-name1',
            color: '#999999',
            dashStyle: 'Solid',
            fillColor: '#cccccc',
            value: 123
          },
          {
            className: 'some-class-name1',
            color: '#999999',
            dashStyle: 'Solid',
            fillColor: '#cccccc',
            value: 123
          },
          {
            className: 'some-class-name1',
            color: '#999999',
            dashStyle: 'Solid',
            fillColor: '#cccccc',
            value: 123
          }
      ]
    },

    compareStart: true,
    compareToMain: true,
    name: 'Some-Name-Goes-Here',
    params: {
      index: 0,
      period: 20,
      longPeriod: 6,
      shortPeriod: 3,
      signalPeriod: 2
    },

    colorAxis: 1,
    connectEnds: true,
    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true
    },
    negativeColor: '#fff',
    pointInterval: 5,
    pointIntervalUnit: 'weeks',
    pointPlacement: 'on',
    pointStart: 12,
    stacking: 'normal',

    animationLimit: 10,
    boostBlending: '#ccc',
    boostThreshold: 1234,
    colorIndex: 5,
    colorKey: 'some-key-value',
    connectNulls: true,
    crisp: true,
    cropThreshold: 123,
    dataSorting: {
        enabled: true,
        matchByName: true,
        sortKey: 'some-key-value'
    },
    findNearestPointBy: 'x',
    getExtremesFromAll: true,
    linecap: 'round',
    lineWidth: 2,
    relativeXValue: true,
    shadow: false,
    softThreshold: true,
    step: 'left',
    zoneAxis: 'y',
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ],

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'macd',

    cumulative: false,
    dataAsColumns: false,
    gapSize: 6,
    gapUnit: 'relative',
    lastPrice: {
      color: '#ccc',
      enabled: true
    },
    lastVisiblePrice: {
      color: '#777',
      enabled: true
    }
  },
  mfi: {
    compare: 'percent',
    compareBase: 0,

    compareStart: true,
    compareToMain: true,
    name: 'Some-Name-Goes-Here',
    params: {
      period: 20,
      decimals: 4,
      volumeSeriesID: 'some-id-goes-here'
    },

    colorAxis: 1,
    connectEnds: true,
    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true
    },
    negativeColor: '#fff',
    pointInterval: 5,
    pointIntervalUnit: 'weeks',
    pointPlacement: 'on',
    pointStart: 12,
    stacking: 'normal',

    animationLimit: 10,
    boostBlending: '#ccc',
    boostThreshold: 1234,
    colorIndex: 5,
    colorKey: 'some-key-value',
    connectNulls: true,
    crisp: true,
    cropThreshold: 123,
    dataSorting: {
        enabled: true,
        matchByName: true,
        sortKey: 'some-key-value'
    },
    findNearestPointBy: 'x',
    getExtremesFromAll: true,
    linecap: 'round',
    lineWidth: 2,
    relativeXValue: true,
    shadow: false,
    softThreshold: true,
    step: 'left',
    zoneAxis: 'y',
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ],

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'mfi',

    cumulative: false,
    dataAsColumns: false,
    gapSize: 6,
    gapUnit: 'relative',
    lastPrice: {
      color: '#ccc',
      enabled: true
    },
    lastVisiblePrice: {
      color: '#777',
      enabled: true
    }
  },
  momentum: {
    compareStart: true,
    compareToMain: true,
    name: 'Some-Name-Goes-Here',
    params: {
      index: 0,
      period: 2
    },

    colorAxis: 1,
    connectEnds: true,
    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true
    },
    negativeColor: '#fff',
    pointInterval: 5,
    pointIntervalUnit: 'weeks',
    pointPlacement: 'on',
    pointStart: 12,
    stacking: 'normal',

    animationLimit: 10,
    boostBlending: '#ccc',
    boostThreshold: 1234,
    colorIndex: 5,
    colorKey: 'some-key-value',
    connectNulls: true,
    crisp: true,
    cropThreshold: 123,
    dataSorting: {
        enabled: true,
        matchByName: true,
        sortKey: 'some-key-value'
    },
    findNearestPointBy: 'x',
    getExtremesFromAll: true,
    linecap: 'round',
    lineWidth: 2,
    relativeXValue: true,
    shadow: false,
    softThreshold: true,
    step: 'left',
    zoneAxis: 'y',
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ],

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'momentum',

    cumulative: false,
    dataAsColumns: false,
    gapSize: 6,
    gapUnit: 'relative',
    lastPrice: {
      color: '#ccc',
      enabled: true
    },
    lastVisiblePrice: {
      color: '#777',
      enabled: true
    }
  },
  obv: {
    compareStart: true,
    compareToMain: true,
    name: 'Some-Name-Goes-Here',
    params: {
      volumeSeriesID: 'some-id-goes-here'
    },

    colorAxis: 1,
    connectEnds: true,
    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true
    },
    negativeColor: '#fff',
    pointInterval: 5,
    pointIntervalUnit: 'weeks',
    pointPlacement: 'on',
    pointStart: 12,
    stacking: 'normal',

    animationLimit: 10,
    boostBlending: '#ccc',
    boostThreshold: 1234,
    colorIndex: 5,
    colorKey: 'some-key-value',
    connectNulls: true,
    crisp: true,
    cropThreshold: 123,
    dataSorting: {
        enabled: true,
        matchByName: true,
        sortKey: 'some-key-value'
    },
    findNearestPointBy: 'x',
    getExtremesFromAll: true,
    linecap: 'round',
    lineWidth: 2,
    relativeXValue: true,
    shadow: false,
    softThreshold: true,
    step: 'left',
    zoneAxis: 'y',
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ],

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'obv',

    cumulative: false,
    dataAsColumns: false,
    gapSize: 6,
    gapUnit: 'relative',
    lastPrice: {
      color: '#ccc',
      enabled: true
    },
    lastVisiblePrice: {
      color: '#777',
      enabled: true
    }
  },
  ohlc: {
    pointValKey: 'close',
    upLineColor: '#777',

    centerInCategory: true,
    colorByPoint: true,
    colors: [
        '#fff',
        '#ccc',
        {
          linearGradient: {
              x1: 0.123,
              x2: 0.567,
              y1: 0.891,
              y2: 0.987
          },
          stops: [
              [0.123, '#cccccc'],
              [0.456, '#ff0000'],
              [1, '#00ff00']
          ]
        },
        {
          animation: {
              defer: 5
          },
          patternOptions: {
              aspectRatio: 0.5,
              backgroundColor: '#999999',
              id: 'some_id_goes_here',
              opacity: 0.5,
              width: 120,
              x: 5,
              y: 10
          },
          patternIndex: 2
        }
    ],
    grouping: false,
    groupPadding: 6,
    maxPointWidth: 12,
    minPointLength: 12,
    pointPadding: 6,
    pointRange: 24,
    pointWidth: 12,

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,

    type: 'ohlc',

    compare: 'percent',
    compareBase: 100,
    navigatorOptions: {
      adaptToUpdatedData: true,
      enabled: true,
      handles: {
        backgroundColor: '#ccc',
        borderColor: '#777',
        enabled: true,
        height: 24,
        lineWidth: 2,
        symbols: [
          'navigator-handle',
          'navigator-handle'
        ],
        width: 24
      },
      height: 120,
      margin: 6,
      maskFill: '#ccc',
      maskInside: true,
      opposite: false,
      outlineColor: '#777',
      outlineWidth: 1,
      xAxis: {
          crosshair: {
              className: 'some-class-name',
              color: '#ccc',
              dashStyle: 'Dash',
              snap: true,
              width: 40,
              zIndex: 6
          },
          height: 60,
          left: 5,
          lineColor: '#999',
          lineWidth: 1,
          showEmpty: true,
          top: 340,
          width: 300
      },
      yAxis: {
        maxLength: '100%',
        maxRange: 123,
        minLength: '20%',
        range: 123,
        resize: {
          controlledAxis: {
            next: [1, 2, 3],
            prev: [0, 'some-id']
          },
          cursor: 'pointer',
          enabled: true,
          lineColor: '#777',
          lineDashStyle: 'Solid',
          lineWidth: 2,
          x: 0,
          y: 0
        },
        scrollbar: {
          barBackgroundColor: '#ccc',
          barBorderColor: '#777',
          barBorderRadius: 2,
          barBorderWidth: 2,
          buttonArrowColor: '#333',
          buttonBackgroundColor: '#ccc',
          buttonBorderColor: '#000',
          buttonBorderRadius: 2,
          buttonBorderWidth: 3,
          enabled: true,
          height: 120,
          liveRedraw: false,
          margin: 6,
          minWidth: 8,
          rifleColor: '#ccc',
          showFull: false,
          trackBackgroundColor: '#ccc',
          trackBorderColor: '#fff',
          trackBorderRadius: 0,
          trackBorderWidth: 2,
          zIndex: 3
        }
      }
    },
    showInNavigator: true
  },
  pc: {
    bottomLine: {
      styles: {
        lineWidth: 2
      }
    },
    fillColor: '#ccc',
    topLine: {
      styles: {
        lineWidth: 3
      }
    },

    compareStart: true,
    compareToMain: true,
    name: 'Some-Name-Goes-Here',
    params: {
      period: 2
    },

    colorAxis: 1,
    connectEnds: true,
    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true
    },
    negativeColor: '#fff',
    pointInterval: 5,
    pointIntervalUnit: 'weeks',
    pointPlacement: 'on',
    pointStart: 12,
    stacking: 'normal',

    animationLimit: 10,
    boostBlending: '#ccc',
    boostThreshold: 1234,
    colorIndex: 5,
    colorKey: 'some-key-value',
    connectNulls: true,
    crisp: true,
    cropThreshold: 123,
    dataSorting: {
        enabled: true,
        matchByName: true,
        sortKey: 'some-key-value'
    },
    findNearestPointBy: 'x',
    getExtremesFromAll: true,
    linecap: 'round',
    lineWidth: 2,
    relativeXValue: true,
    shadow: false,
    softThreshold: true,
    step: 'left',
    zoneAxis: 'y',
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ],

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'pc',

    cumulative: false,
    dataAsColumns: false,
    gapSize: 6,
    gapUnit: 'relative',
    lastPrice: {
      color: '#ccc',
      enabled: true
    },
    lastVisiblePrice: {
      color: '#777',
      enabled: true
    }
  },
  pivotpoints: {
    compareStart: true,
    compareToMain: true,
    name: 'Some-Name-Goes-Here',
    params: {
      period: 2,
      algorithm: 'standard',
    },

    colorAxis: 1,
    connectEnds: true,
    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true
    },
    negativeColor: '#fff',
    pointInterval: 5,
    pointIntervalUnit: 'weeks',
    pointPlacement: 'on',
    pointStart: 12,
    stacking: 'normal',

    animationLimit: 10,
    boostBlending: '#ccc',
    boostThreshold: 1234,
    colorIndex: 5,
    colorKey: 'some-key-value',
    connectNulls: true,
    crisp: true,
    cropThreshold: 123,
    dataSorting: {
        enabled: true,
        matchByName: true,
        sortKey: 'some-key-value'
    },
    findNearestPointBy: 'x',
    getExtremesFromAll: true,
    linecap: 'round',
    lineWidth: 2,
    relativeXValue: true,
    shadow: false,
    softThreshold: true,
    step: 'left',
    zoneAxis: 'y',
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ],

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'pivotpoints',

    cumulative: false,
    dataAsColumns: false,
    gapSize: 6,
    gapUnit: 'relative',
    lastPrice: {
      color: '#ccc',
      enabled: true
    },
    lastVisiblePrice: {
      color: '#777',
      enabled: true
    }
  },
  ppo: {
    compare: 'percent',
    compareBase: 0,

    compareStart: true,
    compareToMain: true,
    name: 'Some-Name-Goes-Here',
    params: {
      index: 0
    },

    colorAxis: 1,
    connectEnds: true,
    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true
    },
    negativeColor: '#fff',
    pointInterval: 5,
    pointIntervalUnit: 'weeks',
    pointPlacement: 'on',
    pointStart: 12,
    stacking: 'normal',

    animationLimit: 10,
    boostBlending: '#ccc',
    boostThreshold: 1234,
    colorIndex: 5,
    colorKey: 'some-key-value',
    connectNulls: true,
    crisp: true,
    cropThreshold: 123,
    dataSorting: {
        enabled: true,
        matchByName: true,
        sortKey: 'some-key-value'
    },
    findNearestPointBy: 'x',
    getExtremesFromAll: true,
    linecap: 'round',
    lineWidth: 2,
    relativeXValue: true,
    shadow: false,
    softThreshold: true,
    step: 'left',
    zoneAxis: 'y',
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ],

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'ppo',

    cumulative: false,
    dataAsColumns: false,
    gapSize: 6,
    gapUnit: 'relative',
    lastPrice: {
      color: '#ccc',
      enabled: true
    },
    lastVisiblePrice: {
      color: '#777',
      enabled: true
    }
  },
  priceenvelopes: {
    bottomLine: {
      styles: {
        lineWidth: 2,
        lineColor: '#ccc'
      }
    },
    topLine: {
      styles: {
        lineWidth: 2,
        lineColor: '#ccc'
      }
    },

    compareStart: true,
    compareToMain: true,
    name: 'Some-Name-Goes-Here',
    params: {
      index: 0,
      period: 2,
      bottomBand: 0.1,
      topBand: 0.1
    },

    colorAxis: 1,
    connectEnds: true,
    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true
    },
    negativeColor: '#fff',
    pointInterval: 5,
    pointIntervalUnit: 'weeks',
    pointPlacement: 'on',
    pointStart: 12,
    stacking: 'normal',

    animationLimit: 10,
    boostBlending: '#ccc',
    boostThreshold: 1234,
    colorIndex: 5,
    colorKey: 'some-key-value',
    connectNulls: true,
    crisp: true,
    cropThreshold: 123,
    dataSorting: {
        enabled: true,
        matchByName: true,
        sortKey: 'some-key-value'
    },
    findNearestPointBy: 'x',
    getExtremesFromAll: true,
    linecap: 'round',
    lineWidth: 2,
    relativeXValue: true,
    shadow: false,
    softThreshold: true,
    step: 'left',
    zoneAxis: 'y',
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ],

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'priceenvelopes',

    cumulative: false,
    dataAsColumns: false,
    gapSize: 6,
    gapUnit: 'relative',
    lastPrice: {
      color: '#ccc',
      enabled: true
    },
    lastVisiblePrice: {
      color: '#777',
      enabled: true
    }
  },
  psar: {
    compareStart: true,
    compareToMain: true,
    name: 'Some-Name-Goes-Here',
    params: {
      index: 0,
      decimals: 4,
      increment: 0.02,
      initialAccelerationFactor: 0.02,
      maxAccelerationFactor: 0.2
    },

    colorAxis: 1,
    connectEnds: true,
    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true
    },
    negativeColor: '#fff',
    pointInterval: 5,
    pointIntervalUnit: 'weeks',
    pointPlacement: 'on',
    pointStart: 12,
    stacking: 'normal',

    animationLimit: 10,
    boostBlending: '#ccc',
    boostThreshold: 1234,
    colorIndex: 5,
    colorKey: 'some-key-value',
    connectNulls: true,
    crisp: true,
    cropThreshold: 123,
    dataSorting: {
        enabled: true,
        matchByName: true,
        sortKey: 'some-key-value'
    },
    findNearestPointBy: 'x',
    getExtremesFromAll: true,
    linecap: 'round',
    lineWidth: 2,
    relativeXValue: true,
    shadow: false,
    softThreshold: true,
    step: 'left',
    zoneAxis: 'y',
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ],

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'psar',

    cumulative: false,
    dataAsColumns: false,
    gapSize: 6,
    gapUnit: 'relative',
    lastPrice: {
      color: '#ccc',
      enabled: true
    },
    lastVisiblePrice: {
      color: '#777',
      enabled: true
    }
  },
  roc: {
    compareStart: true,
    compareToMain: true,
    name: 'Some-Name-Goes-Here',
    params: {
      index: 0,
      period: 2
    },

    colorAxis: 1,
    connectEnds: true,
    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true
    },
    negativeColor: '#fff',
    pointInterval: 5,
    pointIntervalUnit: 'weeks',
    pointPlacement: 'on',
    pointStart: 12,
    stacking: 'normal',

    animationLimit: 10,
    boostBlending: '#ccc',
    boostThreshold: 1234,
    colorIndex: 5,
    colorKey: 'some-key-value',
    connectNulls: true,
    crisp: true,
    cropThreshold: 123,
    dataSorting: {
        enabled: true,
        matchByName: true,
        sortKey: 'some-key-value'
    },
    findNearestPointBy: 'x',
    getExtremesFromAll: true,
    linecap: 'round',
    lineWidth: 2,
    relativeXValue: true,
    shadow: false,
    softThreshold: true,
    step: 'left',
    zoneAxis: 'y',
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ],

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'roc',

    cumulative: false,
    dataAsColumns: false,
    gapSize: 6,
    gapUnit: 'relative',
    lastPrice: {
      color: '#ccc',
      enabled: true
    },
    lastVisiblePrice: {
      color: '#777',
      enabled: true
    }
  },
  rsi: {
    compareStart: true,
    compareToMain: true,
    name: 'Some-Name-Goes-Here',
    params: {
      index: 0,
      period: 2,
      decimals: 4
    },

    colorAxis: 1,
    connectEnds: true,
    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true
    },
    negativeColor: '#fff',
    pointInterval: 5,
    pointIntervalUnit: 'weeks',
    pointPlacement: 'on',
    pointStart: 12,
    stacking: 'normal',

    animationLimit: 10,
    boostBlending: '#ccc',
    boostThreshold: 1234,
    colorIndex: 5,
    colorKey: 'some-key-value',
    connectNulls: true,
    crisp: true,
    cropThreshold: 123,
    dataSorting: {
        enabled: true,
        matchByName: true,
        sortKey: 'some-key-value'
    },
    findNearestPointBy: 'x',
    getExtremesFromAll: true,
    linecap: 'round',
    lineWidth: 2,
    relativeXValue: true,
    shadow: false,
    softThreshold: true,
    step: 'left',
    zoneAxis: 'y',
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ],

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'rsi',

    cumulative: false,
    dataAsColumns: false,
    gapSize: 6,
    gapUnit: 'relative',
    lastPrice: {
      color: '#ccc',
      enabled: true
    },
    lastVisiblePrice: {
      color: '#777',
      enabled: true
    }
  },
  slowstochastic: {
    smoothedLine: {
      styles: {
        lineWidth: 2,
        lineColor: '#ccc'
      }
    },

    compare: 'percent',
    compareBase: 0,

    compareStart: true,
    compareToMain: true,
    name: 'Some-Name-Goes-Here',
    params: {
      periods: [14, 3, 3]
    },

    colorAxis: 1,
    connectEnds: true,
    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true
    },
    negativeColor: '#fff',
    pointInterval: 5,
    pointIntervalUnit: 'weeks',
    pointPlacement: 'on',
    pointStart: 12,
    stacking: 'normal',

    animationLimit: 10,
    boostBlending: '#ccc',
    boostThreshold: 1234,
    colorIndex: 5,
    colorKey: 'some-key-value',
    connectNulls: true,
    crisp: true,
    cropThreshold: 123,
    dataSorting: {
        enabled: true,
        matchByName: true,
        sortKey: 'some-key-value'
    },
    findNearestPointBy: 'x',
    getExtremesFromAll: true,
    linecap: 'round',
    lineWidth: 2,
    relativeXValue: true,
    shadow: false,
    softThreshold: true,
    step: 'left',
    zoneAxis: 'y',
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ],

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'slowstochastic',

    cumulative: false,
    dataAsColumns: false,
    gapSize: 6,
    gapUnit: 'relative',
    lastPrice: {
      color: '#ccc',
      enabled: true
    },
    lastVisiblePrice: {
      color: '#777',
      enabled: true
    }
  },
  sma: {
    compareStart: true,
    compareToMain: true,
    name: 'Some-Name-Goes-Here',
    params: {
      index: 0,
      period: 2
    },

    colorAxis: 1,
    connectEnds: true,
    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true
    },
    negativeColor: '#fff',
    pointInterval: 5,
    pointIntervalUnit: 'weeks',
    pointPlacement: 'on',
    pointStart: 12,
    stacking: 'normal',

    animationLimit: 10,
    boostBlending: '#ccc',
    boostThreshold: 1234,
    colorIndex: 5,
    colorKey: 'some-key-value',
    connectNulls: true,
    crisp: true,
    cropThreshold: 123,
    dataSorting: {
        enabled: true,
        matchByName: true,
        sortKey: 'some-key-value'
    },
    findNearestPointBy: 'x',
    getExtremesFromAll: true,
    linecap: 'round',
    lineWidth: 2,
    relativeXValue: true,
    shadow: false,
    softThreshold: true,
    step: 'left',
    zoneAxis: 'y',
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ],

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'sma',

    cumulative: false,
    dataAsColumns: false,
    gapSize: 6,
    gapUnit: 'relative',
    lastPrice: {
      color: '#ccc',
      enabled: true
    },
    lastVisiblePrice: {
      color: '#777',
      enabled: true
    }
  },
  stochastic: {
    smoothedLine: {
      styles: {
        lineWidth: 2,
        lineColor: '#ccc'
      }
    },

    compare: 'percent',
    compareBase: 0,

    compareStart: true,
    compareToMain: true,
    name: 'Some-Name-Goes-Here',
    params: {
      periods: [14, 3]
    },

    colorAxis: 1,
    connectEnds: true,
    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true
    },
    negativeColor: '#fff',
    pointInterval: 5,
    pointIntervalUnit: 'weeks',
    pointPlacement: 'on',
    pointStart: 12,
    stacking: 'normal',

    animationLimit: 10,
    boostBlending: '#ccc',
    boostThreshold: 1234,
    colorIndex: 5,
    colorKey: 'some-key-value',
    connectNulls: true,
    crisp: true,
    cropThreshold: 123,
    dataSorting: {
        enabled: true,
        matchByName: true,
        sortKey: 'some-key-value'
    },
    findNearestPointBy: 'x',
    getExtremesFromAll: true,
    linecap: 'round',
    lineWidth: 2,
    relativeXValue: true,
    shadow: false,
    softThreshold: true,
    step: 'left',
    zoneAxis: 'y',
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ],

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'stochastic',

    cumulative: false,
    dataAsColumns: false,
    gapSize: 6,
    gapUnit: 'relative',
    lastPrice: {
      color: '#ccc',
      enabled: true
    },
    lastVisiblePrice: {
      color: '#777',
      enabled: true
    }
  },
  supertrend: {
    changeTrendLine: {
      styles: {
        dashStyle: 'Solid',
        lineColor: '#ccc',
        lineWidth: 2
      }
    },
    fallingTrendColor: '#ccc',
    risingTrendColor: '#777',

    compareStart: true,
    compareToMain: true,
    name: 'Some-Name-Goes-Here',
    params: {
      multiplier: 3,
      period: 20
    },

    colorAxis: 1,
    connectEnds: true,
    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true
    },
    negativeColor: '#fff',
    pointInterval: 5,
    pointIntervalUnit: 'weeks',
    pointPlacement: 'on',
    pointStart: 12,
    stacking: 'normal',

    animationLimit: 10,
    boostBlending: '#ccc',
    boostThreshold: 1234,
    colorIndex: 5,
    colorKey: 'some-key-value',
    connectNulls: true,
    crisp: true,
    cropThreshold: 123,
    dataSorting: {
        enabled: true,
        matchByName: true,
        sortKey: 'some-key-value'
    },
    findNearestPointBy: 'x',
    getExtremesFromAll: true,
    linecap: 'round',
    lineWidth: 2,
    relativeXValue: true,
    shadow: false,
    softThreshold: true,
    step: 'left',
    zoneAxis: 'y',
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ],

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'supertrend',

    cumulative: false,
    dataAsColumns: false,
    gapSize: 6,
    gapUnit: 'relative',
    lastPrice: {
      color: '#ccc',
      enabled: true
    },
    lastVisiblePrice: {
      color: '#777',
      enabled: true
    }
  },
  tema: {
    compareStart: true,
    compareToMain: true,
    name: 'Some-Name-Goes-Here',
    params: {
      index: 0,
      period: 2
    },

    colorAxis: 1,
    connectEnds: true,
    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true
    },
    negativeColor: '#fff',
    pointInterval: 5,
    pointIntervalUnit: 'weeks',
    pointPlacement: 'on',
    pointStart: 12,
    stacking: 'normal',

    animationLimit: 10,
    boostBlending: '#ccc',
    boostThreshold: 1234,
    colorIndex: 5,
    colorKey: 'some-key-value',
    connectNulls: true,
    crisp: true,
    cropThreshold: 123,
    dataSorting: {
        enabled: true,
        matchByName: true,
        sortKey: 'some-key-value'
    },
    findNearestPointBy: 'x',
    getExtremesFromAll: true,
    linecap: 'round',
    lineWidth: 2,
    relativeXValue: true,
    shadow: false,
    softThreshold: true,
    step: 'left',
    zoneAxis: 'y',
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ],

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'tema',

    cumulative: false,
    dataAsColumns: false,
    gapSize: 6,
    gapUnit: 'relative',
    lastPrice: {
      color: '#ccc',
      enabled: true
    },
    lastVisiblePrice: {
      color: '#777',
      enabled: true
    }
  },
  trendline: {
    compareStart: true,
    compareToMain: true,
    name: 'Some-Name-Goes-Here',
    params: {
      index: 0
    },

    colorAxis: 1,
    connectEnds: true,
    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true
    },
    negativeColor: '#fff',
    pointInterval: 5,
    pointIntervalUnit: 'weeks',
    pointPlacement: 'on',
    pointStart: 12,
    stacking: 'normal',

    animationLimit: 10,
    boostBlending: '#ccc',
    boostThreshold: 1234,
    colorIndex: 5,
    colorKey: 'some-key-value',
    connectNulls: true,
    crisp: true,
    cropThreshold: 123,
    dataSorting: {
        enabled: true,
        matchByName: true,
        sortKey: 'some-key-value'
    },
    findNearestPointBy: 'x',
    getExtremesFromAll: true,
    linecap: 'round',
    lineWidth: 2,
    relativeXValue: true,
    shadow: false,
    softThreshold: true,
    step: 'left',
    zoneAxis: 'y',
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ],

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'trendline',

    cumulative: false,
    dataAsColumns: false,
    gapSize: 6,
    gapUnit: 'relative',
    lastPrice: {
      color: '#ccc',
      enabled: true
    },
    lastVisiblePrice: {
      color: '#777',
      enabled: true
    }
  },
  trix: {
    compareStart: true,
    compareToMain: true,
    name: 'Some-Name-Goes-Here',
    params: {
      index: 0,
      period: 2
    },

    colorAxis: 1,
    connectEnds: true,
    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true
    },
    negativeColor: '#fff',
    pointInterval: 5,
    pointIntervalUnit: 'weeks',
    pointPlacement: 'on',
    pointStart: 12,
    stacking: 'normal',

    animationLimit: 10,
    boostBlending: '#ccc',
    boostThreshold: 1234,
    colorIndex: 5,
    colorKey: 'some-key-value',
    connectNulls: true,
    crisp: true,
    cropThreshold: 123,
    dataSorting: {
        enabled: true,
        matchByName: true,
        sortKey: 'some-key-value'
    },
    findNearestPointBy: 'x',
    getExtremesFromAll: true,
    linecap: 'round',
    lineWidth: 2,
    relativeXValue: true,
    shadow: false,
    softThreshold: true,
    step: 'left',
    zoneAxis: 'y',
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ],

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'trix',

    cumulative: false,
    dataAsColumns: false,
    gapSize: 6,
    gapUnit: 'relative',
    lastPrice: {
      color: '#ccc',
      enabled: true
    },
    lastVisiblePrice: {
      color: '#777',
      enabled: true
    }
  },
  vbp: {
    pointPadding: 4,
    volumeDivision: {
      enabled: true,
      styles: {
        negativeColor: '#ccc',
        positiveColor: '#777'
      }
    },
    zoneLines: {
      enabled: true,
      styles: 'some-style-goes-here'
    },

    compareToMain: true,
    name: 'Some-Name-Goes-Here',
    params: {
      ranges: 12
    },

    colorAxis: 1,
    connectEnds: true,
    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true
    },
    negativeColor: '#fff',
    pointInterval: 5,
    pointIntervalUnit: 'weeks',
    pointPlacement: 'on',
    pointStart: 12,
    stacking: 'normal',

    animationLimit: 10,
    boostBlending: '#ccc',
    boostThreshold: 1234,
    colorIndex: 5,
    colorKey: 'some-key-value',
    connectNulls: true,
    crisp: true,
    cropThreshold: 123,
    dataSorting: {
        enabled: true,
        matchByName: true,
        sortKey: 'some-key-value'
    },
    findNearestPointBy: 'x',
    getExtremesFromAll: true,
    linecap: 'round',
    lineWidth: 2,
    relativeXValue: true,
    shadow: false,
    softThreshold: true,
    step: 'left',
    zoneAxis: 'y',
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ],

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'vbp',

    cumulative: false,
    dataAsColumns: false,
    gapSize: 6,
    gapUnit: 'relative',
    lastPrice: {
      color: '#ccc',
      enabled: true
    },
    lastVisiblePrice: {
      color: '#777',
      enabled: true
    }
  },
  vwap: {
    compareStart: true,
    compareToMain: true,
    name: 'Some-Name-Goes-Here',
    params: {
      period: 2,
      volumeSeriesID: 'some-id-goes-here'
    },

    colorAxis: 1,
    connectEnds: true,
    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true
    },
    negativeColor: '#fff',
    pointInterval: 5,
    pointIntervalUnit: 'weeks',
    pointPlacement: 'on',
    pointStart: 12,
    stacking: 'normal',

    animationLimit: 10,
    boostBlending: '#ccc',
    boostThreshold: 1234,
    colorIndex: 5,
    colorKey: 'some-key-value',
    connectNulls: true,
    crisp: true,
    cropThreshold: 123,
    dataSorting: {
        enabled: true,
        matchByName: true,
        sortKey: 'some-key-value'
    },
    findNearestPointBy: 'x',
    getExtremesFromAll: true,
    linecap: 'round',
    lineWidth: 2,
    relativeXValue: true,
    shadow: false,
    softThreshold: true,
    step: 'left',
    zoneAxis: 'y',
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ],

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'vwap',

    cumulative: false,
    dataAsColumns: false,
    gapSize: 6,
    gapUnit: 'relative',
    lastPrice: {
      color: '#ccc',
      enabled: true
    },
    lastVisiblePrice: {
      color: '#777',
      enabled: true
    }
  },
  williamsr: {
    compare: 'percent',
    compareBase: 0,

    compareStart: true,
    compareToMain: true,
    name: 'Some-Name-Goes-Here',
    params: {
      period: 2
    },

    colorAxis: 1,
    connectEnds: true,
    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true
    },
    negativeColor: '#fff',
    pointInterval: 5,
    pointIntervalUnit: 'weeks',
    pointPlacement: 'on',
    pointStart: 12,
    stacking: 'normal',

    animationLimit: 10,
    boostBlending: '#ccc',
    boostThreshold: 1234,
    colorIndex: 5,
    colorKey: 'some-key-value',
    connectNulls: true,
    crisp: true,
    cropThreshold: 123,
    dataSorting: {
        enabled: true,
        matchByName: true,
        sortKey: 'some-key-value'
    },
    findNearestPointBy: 'x',
    getExtremesFromAll: true,
    linecap: 'round',
    lineWidth: 2,
    relativeXValue: true,
    shadow: false,
    softThreshold: true,
    step: 'left',
    zoneAxis: 'y',
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ],

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'williamsr',

    cumulative: false,
    dataAsColumns: false,
    gapSize: 6,
    gapUnit: 'relative',
    lastPrice: {
      color: '#ccc',
      enabled: true
    },
    lastVisiblePrice: {
      color: '#777',
      enabled: true
    }
  },
  wma: {
    compareStart: true,
    compareToMain: true,
    name: 'Some-Name-Goes-Here',
    params: {
      index: 0,
      period: 2
    },

    colorAxis: 1,
    connectEnds: true,
    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true
    },
    negativeColor: '#fff',
    pointInterval: 5,
    pointIntervalUnit: 'weeks',
    pointPlacement: 'on',
    pointStart: 12,
    stacking: 'normal',

    animationLimit: 10,
    boostBlending: '#ccc',
    boostThreshold: 1234,
    colorIndex: 5,
    colorKey: 'some-key-value',
    connectNulls: true,
    crisp: true,
    cropThreshold: 123,
    dataSorting: {
        enabled: true,
        matchByName: true,
        sortKey: 'some-key-value'
    },
    findNearestPointBy: 'x',
    getExtremesFromAll: true,
    linecap: 'round',
    lineWidth: 2,
    relativeXValue: true,
    shadow: false,
    softThreshold: true,
    step: 'left',
    zoneAxis: 'y',
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ],

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'wma',

    cumulative: false,
    dataAsColumns: false,
    gapSize: 6,
    gapUnit: 'relative',
    lastPrice: {
      color: '#ccc',
      enabled: true
    },
    lastVisiblePrice: {
      color: '#777',
      enabled: true
    }
  },
  zigzag: {
    compareStart: true,
    compareToMain: true,
    name: 'Some-Name-Goes-Here',
    params: {
      deviation: 1,
      highIndex: 1,
      lowIndex: 2
    },

    colorAxis: 1,
    connectEnds: true,
    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true
    },
    negativeColor: '#fff',
    pointInterval: 5,
    pointIntervalUnit: 'weeks',
    pointPlacement: 'on',
    pointStart: 12,
    stacking: 'normal',

    animationLimit: 10,
    boostBlending: '#ccc',
    boostThreshold: 1234,
    colorIndex: 5,
    colorKey: 'some-key-value',
    connectNulls: true,
    crisp: true,
    cropThreshold: 123,
    dataSorting: {
        enabled: true,
        matchByName: true,
        sortKey: 'some-key-value'
    },
    findNearestPointBy: 'x',
    getExtremesFromAll: true,
    linecap: 'round',
    lineWidth: 2,
    relativeXValue: true,
    shadow: false,
    softThreshold: true,
    step: 'left',
    zoneAxis: 'y',
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ],

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'zigzag',

    cumulative: false,
    dataAsColumns: false,
    gapSize: 6,
    gapUnit: 'relative',
    lastPrice: {
      color: '#ccc',
      enabled: true
    },
    lastVisiblePrice: {
      color: '#777',
      enabled: true
    }
  },
  
  arcdiagram: {
    borderColor: '#fff',
    borderWidth: 2,
    centeredLinks: true,
    colorByPoint: false,
    colorIndex: 2,
    colors: [
        '#fff',
        'ccc',
        {
          linearGradient: {
              x1: 0.123,
              x2: 0.567,
              y1: 0.891,
              y2: 0.987
          },
          stops: [
              [0.123, '#cccccc'],
              [0.456, '#ff0000'],
              [1, '#00ff00']
          ]
        },
        {
          animation: {
              defer: 5
          },
          patternOptions: {
              aspectRatio: 0.5,
              backgroundColor: '#999999',
              id: 'some_id_goes_here',
              opacity: 0.5,
              width: 120,
              x: 5,
              y: 10
          },
          patternIndex: 2
        }
    ],
    equalNodes: true,
    levels: [
        {
         colorByPoint: false,
         dataLabels: {
           align: 'center',
           allowOverlap: true,
           animation: {
               defer: 5
           },
           backgroundColor: {
               linearGradient: {
                   x1: 0.123,
                   x2: 0.234,
                   y1: 0.345,
                   y2: 0.456
               },
               stops: [
                   [0.12, '#999'],
                   [0.34, '#fff']
               ]
           },
           borderColor: '#999999',
           borderRadius: 24,
           borderWidth: 1,
           className: 'some-class-name',
           color: '#000000',
           crop: true,
           defer: false,
           enabled: true,
           filter: {
               operator: '>=',
               property: 'some_property',
               value: 123
           },
           format: 'some format',
           formatter: function() { return true; },
           inside: true,
           nullFormat: 'some format',
           nullFormatter: function() { return true; },
           overflow: 'none',
           padding: 12,
           position: 'center',
           rotation: 0,
           shadow: false,
           shape: 'rect',
           style: 'style goes here',
           useHTML: false,
           verticalAlign: 'top',
           x: 10,
           y: 20,
           z: 0
         },
         linkOpacity: 0.5,
         states: {
           hover: {
               animation: {
                   duration: 123
               },
               borderColor: '#cccccc',
               brightness: 0.3,
               enabled: true
           },
           inactive: {
               enabled: true,
               opacity: 0.5
           },
           normal: {
               animation: {
                   defer: 24
               }
           },
           select: {
               color: '#ff0000',
               enabled: true
           }
         },
         borderColor: '#ccc',
         borderWidth: 1,
         level: 1
        },
        {
         colorByPoint: false,
         dataLabels: {
           align: 'center',
           allowOverlap: true,
           animation: {
               defer: 5
           },
           backgroundColor: {
               linearGradient: {
                   x1: 0.123,
                   x2: 0.234,
                   y1: 0.345,
                   y2: 0.456
               },
               stops: [
                   [0.12, '#999'],
                   [0.34, '#fff']
               ]
           },
           borderColor: '#999999',
           borderRadius: 24,
           borderWidth: 1,
           className: 'some-class-name',
           color: '#000000',
           crop: true,
           defer: false,
           enabled: true,
           filter: {
               operator: '>=',
               property: 'some_property',
               value: 123
           },
           format: 'some format',
           formatter: function() { return true; },
           inside: true,
           nullFormat: 'some format',
           nullFormatter: function() { return true; },
           overflow: 'none',
           padding: 12,
           position: 'center',
           rotation: 0,
           shadow: false,
           shape: 'rect',
           style: 'style goes here',
           useHTML: false,
           verticalAlign: 'top',
           x: 10,
           y: 20,
           z: 0
         },
         linkOpacity: 0.5,
         states: {
           hover: {
               animation: {
                   duration: 123
               },
               borderColor: '#cccccc',
               brightness: 0.3,
               enabled: true
           },
           inactive: {
               enabled: true,
               opacity: 0.5
           },
           normal: {
               animation: {
                   defer: 24
               }
           },
           select: {
               color: '#ff0000',
               enabled: true
           }
         },
         borderColor: '#ccc',
         borderWidth: 1,
         level: 1
        },
        {
         colorByPoint: false,
         dataLabels: {
           align: 'center',
           allowOverlap: true,
           animation: {
               defer: 5
           },
           backgroundColor: {
               linearGradient: {
                   x1: 0.123,
                   x2: 0.234,
                   y1: 0.345,
                   y2: 0.456
               },
               stops: [
                   [0.12, '#999'],
                   [0.34, '#fff']
               ]
           },
           borderColor: '#999999',
           borderRadius: 24,
           borderWidth: 1,
           className: 'some-class-name',
           color: '#000000',
           crop: true,
           defer: false,
           enabled: true,
           filter: {
               operator: '>=',
               property: 'some_property',
               value: 123
           },
           format: 'some format',
           formatter: function() { return true; },
           inside: true,
           nullFormat: 'some format',
           nullFormatter: function() { return true; },
           overflow: 'none',
           padding: 12,
           position: 'center',
           rotation: 0,
           shadow: false,
           shape: 'rect',
           style: 'style goes here',
           useHTML: false,
           verticalAlign: 'top',
           x: 10,
           y: 20,
           z: 0
         },
         linkOpacity: 0.5,
         states: {
           hover: {
               animation: {
                   duration: 123
               },
               borderColor: '#cccccc',
               brightness: 0.3,
               enabled: true
           },
           inactive: {
               enabled: true,
               opacity: 0.5
           },
           normal: {
               animation: {
                   defer: 24
               }
           },
           select: {
               color: '#ff0000',
               enabled: true
           }
         },
         borderColor: '#ccc',
         borderWidth: 1,
         level: 1
        }
    ],
    linkOpacity: 0.7,
    minLinkWidth: 1,
    nodeWidth: 6,
    reversed: false,

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'arcdiagram'
  },
  area: {
    fillColor: '#ccc',
    fillOpacity: 0.7,
    lineColor: {
        radialGradient: {
            cx: 0.123,
            cy: 0.456,
            r: 0.789
        },
        stops: [
            [0.123, '#cccccc'],
            [0.456, '#ff0000'],
            [1, '#00ff00']
        ]
    },
    negativeFillColor: '#ccc',
    trackByArea: true,

    colorAxis: 1,
    connectEnds: true,
    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true
    },
    negativeColor: '#fff',
    pointInterval: 5,
    pointIntervalUnit: 'weeks',
    pointPlacement: 'on',
    pointStart: 12,
    stacking: 'normal',

    animationLimit: 10,
    boostBlending: '#ccc',
    boostThreshold: 1234,
    colorIndex: 5,
    colorKey: 'some-key-value',
    connectNulls: true,
    crisp: true,
    cropThreshold: 123,
    dataSorting: {
        enabled: true,
        matchByName: true,
        sortKey: 'some-key-value'
    },
    findNearestPointBy: 'x',
    getExtremesFromAll: true,
    linecap: 'round',
    lineWidth: 2,
    relativeXValue: true,
    shadow: false,
    softThreshold: true,
    step: 'left',
    zoneAxis: 'y',
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ],

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'area'
  },
  arearange: {
    fillColor: '#ccc',
    fillOpacity: 0.7,
    lineColor: {
        radialGradient: {
            cx: 0.123,
            cy: 0.456,
            r: 0.789
        },
        stops: [
            [0.123, '#cccccc'],
            [0.456, '#ff0000'],
            [1, '#00ff00']
        ]
    },
    negativeFillColor: '#ccc',
    trackByArea: true,

    colorAxis: 1,
    connectEnds: true,
    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true
    },
    negativeColor: '#fff',
    pointInterval: 5,
    pointIntervalUnit: 'weeks',
    pointPlacement: 'on',
    pointStart: 12,
    stacking: 'normal',

    animationLimit: 10,
    boostBlending: '#ccc',
    boostThreshold: 1234,
    colorIndex: 5,
    colorKey: 'some-key-value',
    connectNulls: true,
    crisp: true,
    cropThreshold: 123,
    dataSorting: {
        enabled: true,
        matchByName: true,
        sortKey: 'some-key-value'
    },
    findNearestPointBy: 'x',
    getExtremesFromAll: true,
    linecap: 'round',
    lineWidth: 2,
    relativeXValue: true,
    shadow: false,
    softThreshold: true,
    step: 'left',
    zoneAxis: 'y',
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ],

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'arearange'
  },
  areaspline: {
    fillColor: '#ccc',
    fillOpacity: 0.7,
    lineColor: {
        radialGradient: {
            cx: 0.123,
            cy: 0.456,
            r: 0.789
        },
        stops: [
            [0.123, '#cccccc'],
            [0.456, '#ff0000'],
            [1, '#00ff00']
        ]
    },
    negativeFillColor: '#ccc',
    trackByArea: true,

    colorAxis: 1,
    connectEnds: true,
    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true
    },
    negativeColor: '#fff',
    pointInterval: 5,
    pointIntervalUnit: 'weeks',
    pointPlacement: 'on',
    pointStart: 12,
    stacking: 'normal',

    animationLimit: 10,
    boostBlending: '#ccc',
    boostThreshold: 1234,
    colorIndex: 5,
    colorKey: 'some-key-value',
    connectNulls: true,
    crisp: true,
    cropThreshold: 123,
    dataSorting: {
        enabled: true,
        matchByName: true,
        sortKey: 'some-key-value'
    },
    findNearestPointBy: 'x',
    getExtremesFromAll: true,
    linecap: 'round',
    lineWidth: 2,
    relativeXValue: true,
    shadow: false,
    softThreshold: true,
    step: 'left',
    zoneAxis: 'y',
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ],

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'areaspline'
  },
  areasplinerange: {
    fillColor: '#ccc',
    fillOpacity: 0.7,
    lineColor: {
        radialGradient: {
            cx: 0.123,
            cy: 0.456,
            r: 0.789
        },
        stops: [
            [0.123, '#cccccc'],
            [0.456, '#ff0000'],
            [1, '#00ff00']
        ]
    },
    negativeFillColor: '#ccc',
    trackByArea: true,

    colorAxis: 1,
    connectEnds: true,
    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true
    },
    negativeColor: '#fff',
    pointInterval: 5,
    pointIntervalUnit: 'weeks',
    pointPlacement: 'on',
    pointStart: 12,
    stacking: 'normal',

    animationLimit: 10,
    boostBlending: '#ccc',
    boostThreshold: 1234,
    colorIndex: 5,
    colorKey: 'some-key-value',
    connectNulls: true,
    crisp: true,
    cropThreshold: 123,
    dataSorting: {
        enabled: true,
        matchByName: true,
        sortKey: 'some-key-value'
    },
    findNearestPointBy: 'x',
    getExtremesFromAll: true,
    linecap: 'round',
    lineWidth: 2,
    relativeXValue: true,
    shadow: false,
    softThreshold: true,
    step: 'left',
    zoneAxis: 'y',
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ],

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'areasplinerange'
  },
  bar: {
    depth: 10,
    edgeColor: '#999',
    edgeWidth: 1,
    groupZPadding: 4,

    borderColor: '#ccc',
    borderRadius: 4,
    borderWidth: 2,
    centerInCategory: true,
    colorByPoint: true,
    colors: [
        '#fff',
        '#ccc',
        {
          linearGradient: {
              x1: 0.123,
              x2: 0.567,
              y1: 0.891,
              y2: 0.987
          },
          stops: [
              [0.123, '#cccccc'],
              [0.456, '#ff0000'],
              [1, '#00ff00']
          ]
        },
        {
          animation: {
              defer: 5
          },
          patternOptions: {
              aspectRatio: 0.5,
              backgroundColor: '#999999',
              id: 'some_id_goes_here',
              opacity: 0.5,
              width: 120,
              x: 5,
              y: 10
          },
          patternIndex: 2
        }
    ],
    grouping: false,
    groupPadding: 6,
    maxPointWidth: 12,
    minPointLength: 12,
    pointPadding: 6,
    pointRange: 24,
    pointWidth: 12,

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'bar'
  },
  bellcurve: {
    intervals: 3,

    fillColor: '#ccc',
    fillOpacity: 0.7,
    lineColor: {
        radialGradient: {
            cx: 0.123,
            cy: 0.456,
            r: 0.789
        },
        stops: [
            [0.123, '#cccccc'],
            [0.456, '#ff0000'],
            [1, '#00ff00']
        ]
    },
    negativeFillColor: '#ccc',
    trackByArea: true,

    colorAxis: 1,
    connectEnds: true,
    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true
    },
    negativeColor: '#fff',
    pointInterval: 5,
    pointIntervalUnit: 'weeks',
    pointPlacement: 'on',
    pointStart: 12,
    stacking: 'normal',

    animationLimit: 10,
    boostBlending: '#ccc',
    boostThreshold: 1234,
    colorIndex: 5,
    colorKey: 'some-key-value',
    connectNulls: true,
    crisp: true,
    cropThreshold: 123,
    dataSorting: {
        enabled: true,
        matchByName: true,
        sortKey: 'some-key-value'
    },
    findNearestPointBy: 'x',
    getExtremesFromAll: true,
    linecap: 'round',
    lineWidth: 2,
    relativeXValue: true,
    shadow: false,
    softThreshold: true,
    step: 'left',
    zoneAxis: 'y',
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ],

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'bellcurve'
  },
  boxplot: {
    boxDashStyle: 'Solid',
    medianColor: '#ccc',
    medianDashStyle: 'Dash',
    medianWidth: 2,
    stemDashStyle: 'Solid',
    stemWidth: 1,
    whiskerColor: '#999',
    whiskerDashStyle: 'Solid',
    whiskerLength: 12,
    whiskerWidth: 2,

    depth: 10,
    edgeColor: '#999',
    edgeWidth: 1,
    groupZPadding: 4,

    borderColor: '#ccc',
    borderRadius: 4,
    borderWidth: 2,
    centerInCategory: true,
    colorByPoint: true,
    colors: [
        '#fff',
        '#ccc',
        {
          linearGradient: {
              x1: 0.123,
              x2: 0.567,
              y1: 0.891,
              y2: 0.987
          },
          stops: [
              [0.123, '#cccccc'],
              [0.456, '#ff0000'],
              [1, '#00ff00']
          ]
        },
        {
          animation: {
              defer: 5
          },
          patternOptions: {
              aspectRatio: 0.5,
              backgroundColor: '#999999',
              id: 'some_id_goes_here',
              opacity: 0.5,
              width: 120,
              x: 5,
              y: 10
          },
          patternIndex: 2
        }
    ],
    grouping: false,
    groupPadding: 6,
    maxPointWidth: 12,
    minPointLength: 12,
    pointPadding: 6,
    pointRange: 24,
    pointWidth: 12,

    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true,
        draggableHigh: true,
        draggableLow: true,
        draggableQ1: true,
        draggableQ3: true
    },

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'boxplot'
  },
  bubble: {
    displayNegative: false,
    jitter: {
      x: 123,
      y: 456
    },
    maxSize: 24,
    minSize: 6,
    sizeBy: 'width',
    sizeByAbsoluteValue: true,
    zMax: 6,
    zMin: 3,
    zThreshold: 50,

    colorAxis: 1,
    connectEnds: true,
    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true
    },
    negativeColor: '#fff',
    pointInterval: 5,
    pointIntervalUnit: 'weeks',
    pointPlacement: 'on',
    pointStart: 12,
    stacking: 'normal',

    animationLimit: 10,
    boostBlending: '#ccc',
    boostThreshold: 1234,
    colorIndex: 5,
    colorKey: 'some-key-value',
    connectNulls: true,
    crisp: true,
    cropThreshold: 123,
    dataSorting: {
        enabled: true,
        matchByName: true,
        sortKey: 'some-key-value'
    },
    findNearestPointBy: 'x',
    getExtremesFromAll: true,
    linecap: 'round',
    lineWidth: 2,
    relativeXValue: true,
    shadow: false,
    softThreshold: true,
    step: 'left',
    zoneAxis: 'y',
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ],

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'bubble'
  },
  bullet: {
    targetOptions: {
        borderColor: '#999',
        borderRadius: 2,
        borderWidth: 1,
        color: '#ccc',
        height: 12,
        width: '5%'
    },

    depth: 10,
    edgeColor: '#999',
    edgeWidth: 1,
    groupZPadding: 4,

    borderColor: '#ccc',
    borderRadius: 4,
    borderWidth: 2,
    centerInCategory: true,
    colorByPoint: true,
    colors: [
        '#fff',
        '#ccc',
        {
          linearGradient: {
              x1: 0.123,
              x2: 0.567,
              y1: 0.891,
              y2: 0.987
          },
          stops: [
              [0.123, '#cccccc'],
              [0.456, '#ff0000'],
              [1, '#00ff00']
          ]
        },
        {
          animation: {
              defer: 5
          },
          patternOptions: {
              aspectRatio: 0.5,
              backgroundColor: '#999999',
              id: 'some_id_goes_here',
              opacity: 0.5,
              width: 120,
              x: 5,
              y: 10
          },
          patternIndex: 2
        }
    ],
    grouping: false,
    groupPadding: 6,
    maxPointWidth: 12,
    minPointLength: 12,
    pointPadding: 6,
    pointRange: 24,
    pointWidth: 12,

    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true,
        draggableTarget: true
    },

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'bullet'
  },
  column: {
    depth: 10,
    edgeColor: '#999',
    edgeWidth: 1,
    groupZPadding: 4,

    borderColor: '#ccc',
    borderRadius: 4,
    borderWidth: 2,
    centerInCategory: true,
    colorByPoint: true,
    colors: [
        '#fff',
        '#ccc',
        {
          linearGradient: {
              x1: 0.123,
              x2: 0.567,
              y1: 0.891,
              y2: 0.987
          },
          stops: [
              [0.123, '#cccccc'],
              [0.456, '#ff0000'],
              [1, '#00ff00']
          ]
        },
        {
          animation: {
              defer: 5
          },
          patternOptions: {
              aspectRatio: 0.5,
              backgroundColor: '#999999',
              id: 'some_id_goes_here',
              opacity: 0.5,
              width: 120,
              x: 5,
              y: 10
          },
          patternIndex: 2
        }
    ],
    grouping: false,
    groupPadding: 6,
    maxPointWidth: 12,
    minPointLength: 12,
    pointPadding: 6,
    pointRange: 24,
    pointWidth: 12,

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'column'
  },
  columnpyramid: {
    depth: 10,
    edgeColor: '#999',
    edgeWidth: 1,
    groupZPadding: 4,

    borderColor: '#ccc',
    borderRadius: 4,
    borderWidth: 2,
    centerInCategory: true,
    colorByPoint: true,
    colors: [
        '#fff',
        '#ccc',
        {
          linearGradient: {
              x1: 0.123,
              x2: 0.567,
              y1: 0.891,
              y2: 0.987
          },
          stops: [
              [0.123, '#cccccc'],
              [0.456, '#ff0000'],
              [1, '#00ff00']
          ]
        },
        {
          animation: {
              defer: 5
          },
          patternOptions: {
              aspectRatio: 0.5,
              backgroundColor: '#999999',
              id: 'some_id_goes_here',
              opacity: 0.5,
              width: 120,
              x: 5,
              y: 10
          },
          patternIndex: 2
        }
    ],
    grouping: false,
    groupPadding: 6,
    maxPointWidth: 12,
    minPointLength: 12,
    pointPadding: 6,
    pointRange: 24,
    pointWidth: 12,

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'columnpyramid'
  },
  columnrange: {
    depth: 10,
    edgeColor: '#999',
    edgeWidth: 1,
    groupZPadding: 4,

    borderColor: '#ccc',
    borderRadius: 4,
    borderWidth: 2,
    centerInCategory: true,
    colorByPoint: true,
    colors: [
        '#fff',
        '#ccc',
        {
          linearGradient: {
              x1: 0.123,
              x2: 0.567,
              y1: 0.891,
              y2: 0.987
          },
          stops: [
              [0.123, '#cccccc'],
              [0.456, '#ff0000'],
              [1, '#00ff00']
          ]
        },
        {
          animation: {
              defer: 5
          },
          patternOptions: {
              aspectRatio: 0.5,
              backgroundColor: '#999999',
              id: 'some_id_goes_here',
              opacity: 0.5,
              width: 120,
              x: 5,
              y: 10
          },
          patternIndex: 2
        }
    ],
    grouping: false,
    groupPadding: 6,
    maxPointWidth: 12,
    minPointLength: 12,
    pointPadding: 6,
    pointRange: 24,
    pointWidth: 12,

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'columnrange'
  },
  cylinder: {
    depth: 10,
    edgeColor: '#999',
    edgeWidth: 1,
    groupZPadding: 4,

    borderColor: '#ccc',
    borderRadius: 4,
    borderWidth: 2,
    centerInCategory: true,
    colorByPoint: true,
    colors: [
        '#fff',
        '#ccc',
        {
          linearGradient: {
              x1: 0.123,
              x2: 0.567,
              y1: 0.891,
              y2: 0.987
          },
          stops: [
              [0.123, '#cccccc'],
              [0.456, '#ff0000'],
              [1, '#00ff00']
          ]
        },
        {
          animation: {
              defer: 5
          },
          patternOptions: {
              aspectRatio: 0.5,
              backgroundColor: '#999999',
              id: 'some_id_goes_here',
              opacity: 0.5,
              width: 120,
              x: 5,
              y: 10
          },
          patternIndex: 2
        }
    ],
    grouping: false,
    groupPadding: 6,
    maxPointWidth: 12,
    minPointLength: 12,
    pointPadding: 6,
    pointRange: 24,
    pointWidth: 12,

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'cylinder'
  },
  dependencywheel: {
    borderColor: '#ccc',
    borderWidth: 2,
    center: ['50%', '30%'],
    centerInCategory: true,
    colorByPoint: false,
    colorIndex: 3,
    colors: [
        '#fff',
        'ccc',
        {
          linearGradient: {
              x1: 0.123,
              x2: 0.567,
              y1: 0.891,
              y2: 0.987
          },
          stops: [
              [0.123, '#cccccc'],
              [0.456, '#ff0000'],
              [1, '#00ff00']
          ]
        },
        {
          animation: {
              defer: 5
          },
          patternOptions: {
              aspectRatio: 0.5,
              backgroundColor: '#999999',
              id: 'some_id_goes_here',
              opacity: 0.5,
              width: 120,
              x: 5,
              y: 10
          },
          patternIndex: 2
        }
    ],
    curveFactor: 0.6,
    levels: [
        {
         colorByPoint: false,
         dataLabels: {
           align: 'center',
           allowOverlap: true,
           animation: {
               defer: 5
           },
           backgroundColor: {
               linearGradient: {
                   x1: 0.123,
                   x2: 0.234,
                   y1: 0.345,
                   y2: 0.456
               },
               stops: [
                   [0.12, '#999'],
                   [0.34, '#fff']
               ]
           },
           borderColor: '#999999',
           borderRadius: 24,
           borderWidth: 1,
           className: 'some-class-name',
           color: '#000000',
           crop: true,
           defer: false,
           enabled: true,
           filter: {
               operator: '>=',
               property: 'some_property',
               value: 123
           },
           format: 'some format',
           formatter: function() { return true; },
           inside: true,
           nullFormat: 'some format',
           nullFormatter: function() { return true; },
           overflow: 'none',
           padding: 12,
           position: 'center',
           rotation: 0,
           shadow: false,
           shape: 'rect',
           style: 'style goes here',
           useHTML: false,
           verticalAlign: 'top',
           x: 10,
           y: 20,
           z: 0
         },
         linkOpacity: 0.5,
         states: {
           hover: {
               animation: {
                   duration: 123
               },
               borderColor: '#cccccc',
               brightness: 0.3,
               enabled: true
           },
           inactive: {
               enabled: true,
               opacity: 0.5
           },
           normal: {
               animation: {
                   defer: 24
               }
           },
           select: {
               color: '#ff0000',
               enabled: true
           }
         },
         borderColor: '#ccc',
         borderWidth: 1,
         level: 1
        },
        {
         colorByPoint: false,
         dataLabels: {
           align: 'center',
           allowOverlap: true,
           animation: {
               defer: 5
           },
           backgroundColor: {
               linearGradient: {
                   x1: 0.123,
                   x2: 0.234,
                   y1: 0.345,
                   y2: 0.456
               },
               stops: [
                   [0.12, '#999'],
                   [0.34, '#fff']
               ]
           },
           borderColor: '#999999',
           borderRadius: 24,
           borderWidth: 1,
           className: 'some-class-name',
           color: '#000000',
           crop: true,
           defer: false,
           enabled: true,
           filter: {
               operator: '>=',
               property: 'some_property',
               value: 123
           },
           format: 'some format',
           formatter: function() { return true; },
           inside: true,
           nullFormat: 'some format',
           nullFormatter: function() { return true; },
           overflow: 'none',
           padding: 12,
           position: 'center',
           rotation: 0,
           shadow: false,
           shape: 'rect',
           style: 'style goes here',
           useHTML: false,
           verticalAlign: 'top',
           x: 10,
           y: 20,
           z: 0
         },
         linkOpacity: 0.5,
         states: {
           hover: {
               animation: {
                   duration: 123
               },
               borderColor: '#cccccc',
               brightness: 0.3,
               enabled: true
           },
           inactive: {
               enabled: true,
               opacity: 0.5
           },
           normal: {
               animation: {
                   defer: 24
               }
           },
           select: {
               color: '#ff0000',
               enabled: true
           }
         },
         borderColor: '#ccc',
         borderWidth: 1,
         level: 1
        },
        {
         colorByPoint: false,
         dataLabels: {
           align: 'center',
           allowOverlap: true,
           animation: {
               defer: 5
           },
           backgroundColor: {
               linearGradient: {
                   x1: 0.123,
                   x2: 0.234,
                   y1: 0.345,
                   y2: 0.456
               },
               stops: [
                   [0.12, '#999'],
                   [0.34, '#fff']
               ]
           },
           borderColor: '#999999',
           borderRadius: 24,
           borderWidth: 1,
           className: 'some-class-name',
           color: '#000000',
           crop: true,
           defer: false,
           enabled: true,
           filter: {
               operator: '>=',
               property: 'some_property',
               value: 123
           },
           format: 'some format',
           formatter: function() { return true; },
           inside: true,
           nullFormat: 'some format',
           nullFormatter: function() { return true; },
           overflow: 'none',
           padding: 12,
           position: 'center',
           rotation: 0,
           shadow: false,
           shape: 'rect',
           style: 'style goes here',
           useHTML: false,
           verticalAlign: 'top',
           x: 10,
           y: 20,
           z: 0
         },
         linkOpacity: 0.5,
         states: {
           hover: {
               animation: {
                   duration: 123
               },
               borderColor: '#cccccc',
               brightness: 0.3,
               enabled: true
           },
           inactive: {
               enabled: true,
               opacity: 0.5
           },
           normal: {
               animation: {
                   defer: 24
               }
           },
           select: {
               color: '#ff0000',
               enabled: true
           }
         },
         borderColor: '#ccc',
         borderWidth: 1,
         level: 1
        }
    ],
    linkOpacity: 0.7,
    minLinkWidth: 1,
    nodePadding: 6,
    nodeWidth: 12,
    startAngle: 45,

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'dependencywheel'
  },
  dumbbell: {
      animationLimit: 10,
      colorAxis: 'some-id-goes-here',
      colorIndex: 3,
      colorKey: 'some-key-goes-here',
      connectEnds: true,
      connectNulls: false,
      connectorColor: '#777',
      connectorWidth: 1,
      crisp: true,
      cropThreshold: 500,
      dataSorting: {
          enabled: true,
          matchByName: true,
          sortKey: 'some-key-value'
      },
      dragDrop: {
          draggableHigh: true,
          draggableLow: true,
          draggableX: true,
          draggableY: true,
          dragHandle: {
              className: 'draghandle-classname-goes-here',
              color: '#ccc',
              cursor: 'alias',
              lineColor: '#ddd',
              lineWidth: 2,
              pathFormatter: function() { return true; },
              zIndex: 10
          },
          dragMaxX: 3456,
          dragMaxY: 6532,
          dragMinX: 123,
          dragMinY: 321,
          dragPrecisionX: 5,
          dragPrecisionY: 5,
          dragSensitivity: 2,
          groupBy: 'some-property-name',
          guideBox: {
              default: {
                  className: 'some-classname-goes-here',
                  color: '#999',
                  cursor: 'pointer',
                  lineColor: '#ccc',
                  lineWidth: 2,
                  zIndex: 100
              }
          },
          liveRedraw: true
      },
      findNearestPointBy: 'xy',
      getExtremesFromAll: true,
      groupPadding: 12,
      linecap: 'round',
      lineColor: '#ccc',
      lowColor: '#eee',
      negativeColor: '#ee0000',
      negativeFillColor: '#990000',
      pointInterval: 5,
      pointIntervalUnit: 'days',
      pointPadding: 6,
      pointPlacement: 'on',
      pointStart: 12,
      relativeXValue: true,
      shadow: {
        color: '#cccccc',
        offsetX: 10,
        offsetY: 5,
        width: 4
      },
      softThreshold: true,
      stacking: 'normal',
      step: 'right',
      zoneAxis: 'y',
      zones: [
          {
            className: 'some-class-name1',
            color: '#999999',
            dashStyle: 'Solid',
            fillColor: '#cccccc',
            value: 123
          },
          {
            className: 'some-class-name1',
            color: '#999999',
            dashStyle: 'Solid',
            fillColor: '#cccccc',
            value: 123
          },
          {
            className: 'some-class-name1',
            color: '#999999',
            dashStyle: 'Solid',
            fillColor: '#cccccc',
            value: 123
          }
      ],
      type: 'dumbbell'
  },
  errorbar: {
    boxDashStyle: 'Solid',
    medianColor: '#ccc',
    medianDashStyle: 'Dash',
    medianWidth: 2,
    stemDashStyle: 'Solid',
    stemWidth: 1,
    whiskerColor: '#999',
    whiskerDashStyle: 'Solid',
    whiskerLength: 12,
    whiskerWidth: 2,

    depth: 10,
    edgeColor: '#999',
    edgeWidth: 1,
    groupZPadding: 4,

    borderColor: '#ccc',
    borderRadius: 4,
    borderWidth: 2,
    centerInCategory: true,
    colorByPoint: true,
    colors: [
        '#fff',
        '#ccc',
        {
          linearGradient: {
              x1: 0.123,
              x2: 0.567,
              y1: 0.891,
              y2: 0.987
          },
          stops: [
              [0.123, '#cccccc'],
              [0.456, '#ff0000'],
              [1, '#00ff00']
          ]
        },
        {
          animation: {
              defer: 5
          },
          patternOptions: {
              aspectRatio: 0.5,
              backgroundColor: '#999999',
              id: 'some_id_goes_here',
              opacity: 0.5,
              width: 120,
              x: 5,
              y: 10
          },
          patternIndex: 2
        }
    ],
    grouping: false,
    groupPadding: 6,
    maxPointWidth: 12,
    minPointLength: 12,
    pointPadding: 6,
    pointRange: 24,
    pointWidth: 12,

    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true,
        draggableHigh: true,
        draggableLow: true,
        draggableQ1: true,
        draggableQ3: true
    },

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'errorbar'
  },
  funnel: {
    height: '60%',
    neckHeight: '15%',
    neckWidth: 36,
    reversed: false,
    width: 320,

    borderColor: '#ccc',
    borderWidth: 1,
    center: ['50%', '50%'],
    colorAxis: 1,
    colorIndex: 3,
    colorKey: 'some-key-goes-here',
    colors: [
        '#fff',
        'ccc',
        {
          linearGradient: {
              x1: 0.123,
              x2: 0.567,
              y1: 0.891,
              y2: 0.987
          },
          stops: [
              [0.123, '#cccccc'],
              [0.456, '#ff0000'],
              [1, '#00ff00']
          ]
        },
        {
          animation: {
              defer: 5
          },
          patternOptions: {
              aspectRatio: 0.5,
              backgroundColor: '#999999',
              id: 'some_id_goes_here',
              opacity: 0.5,
              width: 120,
              x: 5,
              y: 10
          },
          patternIndex: 2
        }
    ],
    depth: 10,
    endAngle: 90,
    fillColor: '#fff',
    ignoreHiddenPoint: true,
    innerSize: '30%',
    linecap: 'round',
    minSize: '20%',
    size: 80,
    slicedOffset: 24,
    startAngle: 45,
    thickness: 2,

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'funnel'
  },
  funnel3d: {
    gradientForSides: true,

    height: '60%',
    neckHeight: '15%',
    neckWidth: 36,
    reversed: false,
    width: 320,

    borderColor: '#ccc',
    borderWidth: 1,
    center: ['50%', '50%'],
    colorAxis: 1,
    colorIndex: 3,
    colorKey: 'some-key-goes-here',
    colors: [
        '#fff',
        'ccc',
        {
          linearGradient: {
              x1: 0.123,
              x2: 0.567,
              y1: 0.891,
              y2: 0.987
          },
          stops: [
              [0.123, '#cccccc'],
              [0.456, '#ff0000'],
              [1, '#00ff00']
          ]
        },
        {
          animation: {
              defer: 5
          },
          patternOptions: {
              aspectRatio: 0.5,
              backgroundColor: '#999999',
              id: 'some_id_goes_here',
              opacity: 0.5,
              width: 120,
              x: 5,
              y: 10
          },
          patternIndex: 2
        }
    ],
    depth: 10,
    endAngle: 90,
    fillColor: '#fff',
    ignoreHiddenPoint: true,
    innerSize: '30%',
    linecap: 'round',
    minSize: '20%',
    size: 80,
    slicedOffset: 24,
    startAngle: 45,
    thickness: 2,

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'funnel3d'
  },
  gauge: {
    colorIndex: 3,
    crisp: true,
    dial: {
        backgroundColor: '#ccc',
        baseLength: '80%',
        baseWidth: 120,
        borderColor: '#fff',
        borderWidth: 1,
        path: [1, 2, 3],
        radius: '80%',
        rearLength: '10%',
        topWidth: 80
    },
    linecap: 'round',
    lineWidth: 1,
    overshoot: 12.5,
    pivot: {
        backgroundColor: '#ccc',
        borderColor: '#eee',
        borderWidth: 2,
        radius: 60
    },
    pointInterval: 5,
    pointIntervalUnit: 'day',
    pointStart: 5,
    relativeXValue: true,
    shadow: false,
    wrap: false,

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'gauge'
  },
  heatmap: {
    borderRadius: 4,
    colsize: 1,
    nullColor: '#ccc',
    pointPadding: 6,
    rowsize: 1,

    colorAxis: 1,
    connectEnds: true,
    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true
    },
    negativeColor: '#fff',
    pointInterval: 5,
    pointIntervalUnit: 'weeks',
    pointPlacement: 'on',
    pointStart: 12,
    stacking: 'normal',

    animationLimit: 10,
    boostBlending: '#ccc',
    boostThreshold: 1234,
    colorIndex: 5,
    colorKey: 'some-key-value',
    connectNulls: true,
    crisp: true,
    cropThreshold: 123,
    dataSorting: {
        enabled: true,
        matchByName: true,
        sortKey: 'some-key-value'
    },
    findNearestPointBy: 'x',
    getExtremesFromAll: true,
    linecap: 'round',
    lineWidth: 2,
    relativeXValue: true,
    shadow: false,
    softThreshold: true,
    step: 'left',
    zoneAxis: 'y',
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ],

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'heatmap'
  },
  histogram: {
    binsNumber: 'square-root',
    binWidth: 24,

    depth: 10,
    edgeColor: '#999',
    edgeWidth: 1,
    groupZPadding: 4,

    borderColor: '#ccc',
    borderRadius: 4,
    borderWidth: 2,
    centerInCategory: true,
    colorByPoint: true,
    colors: [
        '#fff',
        '#ccc',
        {
          linearGradient: {
              x1: 0.123,
              x2: 0.567,
              y1: 0.891,
              y2: 0.987
          },
          stops: [
              [0.123, '#cccccc'],
              [0.456, '#ff0000'],
              [1, '#00ff00']
          ]
        },
        {
          animation: {
              defer: 5
          },
          patternOptions: {
              aspectRatio: 0.5,
              backgroundColor: '#999999',
              id: 'some_id_goes_here',
              opacity: 0.5,
              width: 120,
              x: 5,
              y: 10
          },
          patternIndex: 2
        }
    ],
    grouping: false,
    groupPadding: 6,
    maxPointWidth: 12,
    minPointLength: 12,
    pointPadding: 6,
    pointRange: 24,
    pointWidth: 12,

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'histogram'
  },
  item: {
    itemPadding: 12,
    layout: 'horizontal',
    rows: 3,

    borderColor: '#ccc',
    borderWidth: 1,
    center: ['50%', '50%'],
    colorAxis: 1,
    colorIndex: 3,
    colorKey: 'some-key-goes-here',
    colors: [
        '#fff',
        'ccc',
        {
          linearGradient: {
              x1: 0.123,
              x2: 0.567,
              y1: 0.891,
              y2: 0.987
          },
          stops: [
              [0.123, '#cccccc'],
              [0.456, '#ff0000'],
              [1, '#00ff00']
          ]
        },
        {
          animation: {
              defer: 5
          },
          patternOptions: {
              aspectRatio: 0.5,
              backgroundColor: '#999999',
              id: 'some_id_goes_here',
              opacity: 0.5,
              width: 120,
              x: 5,
              y: 10
          },
          patternIndex: 2
        }
    ],
    depth: 10,
    endAngle: 90,
    fillColor: '#fff',
    ignoreHiddenPoint: true,
    innerSize: '30%',
    linecap: 'round',
    minSize: '20%',
    size: 80,
    slicedOffset: 24,
    startAngle: 45,
    thickness: 2,

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'item'
  },
  line: {
    fillColor: '#ccc',
    fillOpacity: 0.7,
    lineColor: {
        radialGradient: {
            cx: 0.123,
            cy: 0.456,
            r: 0.789
        },
        stops: [
            [0.123, '#cccccc'],
            [0.456, '#ff0000'],
            [1, '#00ff00']
        ]
    },
    negativeFillColor: '#ccc',
    trackByArea: true,

    colorAxis: 1,
    connectEnds: true,
    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true
    },
    negativeColor: '#fff',
    pointInterval: 5,
    pointIntervalUnit: 'weeks',
    pointPlacement: 'on',
    pointStart: 12,
    stacking: 'normal',

    animationLimit: 10,
    boostBlending: '#ccc',
    boostThreshold: 1234,
    colorIndex: 5,
    colorKey: 'some-key-value',
    connectNulls: true,
    crisp: true,
    cropThreshold: 123,
    dataSorting: {
        enabled: true,
        matchByName: true,
        sortKey: 'some-key-value'
    },
    findNearestPointBy: 'x',
    getExtremesFromAll: true,
    linecap: 'round',
    lineWidth: 2,
    relativeXValue: true,
    shadow: false,
    softThreshold: true,
    step: 'left',
    zoneAxis: 'y',
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ],

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'line'
  },
  lollipop: {
      animationLimit: 10,
      colorAxis: 'some-id-goes-here',
      colorIndex: 3,
      colorKey: 'some-key-goes-here',
      connectEnds: true,
      connectNulls: false,
      connectorColor: '#777',
      connectorWidth: 1,
      crisp: true,
      cropThreshold: 500,
      dataSorting: {
          enabled: true,
          matchByName: true,
          sortKey: 'some-key-value'
      },
      dragDrop: {
          draggableHigh: true,
          draggableLow: true,
          draggableX: true,
          draggableY: true,
          dragHandle: {
              className: 'draghandle-classname-goes-here',
              color: '#ccc',
              cursor: 'alias',
              lineColor: '#ddd',
              lineWidth: 2,
              pathFormatter: function() { return true; },
              zIndex: 10
          },
          dragMaxX: 3456,
          dragMaxY: 6532,
          dragMinX: 123,
          dragMinY: 321,
          dragPrecisionX: 5,
          dragPrecisionY: 5,
          dragSensitivity: 2,
          groupBy: 'some-property-name',
          guideBox: {
              default: {
                  className: 'some-classname-goes-here',
                  color: '#999',
                  cursor: 'pointer',
                  lineColor: '#ccc',
                  lineWidth: 2,
                  zIndex: 100
              }
          },
          liveRedraw: true
      },
      findNearestPointBy: 'xy',
      getExtremesFromAll: true,
      groupPadding: 12,
      linecap: 'round',
      lineColor: '#ccc',
      lowColor: '#eee',
      negativeColor: '#ee0000',
      negativeFillColor: '#990000',
      pointInterval: 5,
      pointIntervalUnit: 'days',
      pointPadding: 6,
      pointPlacement: 'on',
      pointStart: 12,
      relativeXValue: true,
      shadow: {
        color: '#cccccc',
        offsetX: 10,
        offsetY: 5,
        width: 4
      },
      softThreshold: true,
      stacking: 'normal',
      step: 'right',
      zoneAxis: 'y',
      zones: [
          {
            className: 'some-class-name1',
            color: '#999999',
            dashStyle: 'Solid',
            fillColor: '#cccccc',
            value: 123
          },
          {
            className: 'some-class-name1',
            color: '#999999',
            dashStyle: 'Solid',
            fillColor: '#cccccc',
            value: 123
          },
          {
            className: 'some-class-name1',
            color: '#999999',
            dashStyle: 'Solid',
            fillColor: '#cccccc',
            value: 123
          }
      ],
      type: 'lollipop'
  },
  networkgraph: {
    colorIndex: 3,
    crisp: true,
    draggable: true,
    findNearestPointBy: 'xy',
    layoutAlgorithm: {
        approximation: 'barnes-hut',
        attractiveForce: function() { return true; },
        enableSimulation: true,
        friction: 0.98,
        gravitationalConstant: 0.0625,
        initialPositionRadius: 1,
        initialPositions: 'circle',
        integration: 'euler',
        linkLength: 12,
        maxIterations: 1000,
        maxSpeed: 10,
        repulsiveForce: function() { return true; },
        theta: 0.5,
        type: 'reingold-fruchterman'
    },
    lineWidth: 2,
    link: {
        color: '#ccc',
        dashStyle: 'Solid',
        width: 1
    },
    relativeXValue: true,
    shadow: false,
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ],

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'networkgraph'
  },
  organization: {
    hangingIndent: 24,
    hangingIndentTranslation: 'inherit',
    levels: [
        {
         colorByPoint: false,
         dataLabels: {
           align: 'center',
           allowOverlap: true,
           animation: {
               defer: 5
           },
           backgroundColor: {
               linearGradient: {
                   x1: 0.123,
                   x2: 0.234,
                   y1: 0.345,
                   y2: 0.456
               },
               stops: [
                   [0.12, '#999'],
                   [0.34, '#fff']
               ]
           },
           borderColor: '#999999',
           borderRadius: 24,
           borderWidth: 1,
           className: 'some-class-name',
           color: '#000000',
           crop: true,
           defer: false,
           enabled: true,
           filter: {
               operator: '>=',
               property: 'some_property',
               value: 123
           },
           format: 'some format',
           formatter: function() { return true; },
           inside: true,
           nullFormat: 'some format',
           nullFormatter: function() { return true; },
           overflow: 'none',
           padding: 12,
           position: 'center',
           rotation: 0,
           shadow: false,
           shape: 'rect',
           style: 'style goes here',
           useHTML: false,
           verticalAlign: 'top',
           x: 10,
           y: 20,
           z: 0
         },
         linkOpacity: 0.5,
         states: {
           hover: {
               animation: {
                   duration: 123
               },
               borderColor: '#cccccc',
               brightness: 0.3,
               enabled: true
           },
           inactive: {
               enabled: true,
               opacity: 0.5
           },
           normal: {
               animation: {
                   defer: 24
               }
           },
           select: {
               color: '#ff0000',
               enabled: true,
           }
         },
         borderColor: '#ccc',
         borderWidth: 1,
         level: 1
        },
        {
         colorByPoint: false,
         dataLabels: {
           align: 'center',
           allowOverlap: true,
           animation: {
               defer: 5
           },
           backgroundColor: {
               linearGradient: {
                   x1: 0.123,
                   x2: 0.234,
                   y1: 0.345,
                   y2: 0.456
               },
               stops: [
                   [0.12, '#999'],
                   [0.34, '#fff']
               ]
           },
           borderColor: '#999999',
           borderRadius: 24,
           borderWidth: 1,
           className: 'some-class-name',
           color: '#000000',
           crop: true,
           defer: false,
           enabled: true,
           filter: {
               operator: '>=',
               property: 'some_property',
               value: 123
           },
           format: 'some format',
           formatter: function() { return true; },
           inside: true,
           nullFormat: 'some format',
           nullFormatter: function() { return true; },
           overflow: 'none',
           padding: 12,
           position: 'center',
           rotation: 0,
           shadow: false,
           shape: 'rect',
           style: 'style goes here',
           useHTML: false,
           verticalAlign: 'top',
           x: 10,
           y: 20,
           z: 0
         },
         linkOpacity: 0.5,
         states: {
           hover: {
               animation: {
                   duration: 123
               },
               borderColor: '#cccccc',
               brightness: 0.3,
               enabled: true
           },
           inactive: {
               enabled: true,
               opacity: 0.5
           },
           normal: {
               animation: {
                   defer: 24
               }
           },
           select: {
               color: '#ff0000',
               enabled: true,
           }
         },
         borderColor: '#ccc',
         borderWidth: 1,
         level: 1
        },
        {
         colorByPoint: false,
         dataLabels: {
           align: 'center',
           allowOverlap: true,
           animation: {
               defer: 5
           },
           backgroundColor: {
               linearGradient: {
                   x1: 0.123,
                   x2: 0.234,
                   y1: 0.345,
                   y2: 0.456
               },
               stops: [
                   [0.12, '#999'],
                   [0.34, '#fff']
               ]
           },
           borderColor: '#999999',
           borderRadius: 24,
           borderWidth: 1,
           className: 'some-class-name',
           color: '#000000',
           crop: true,
           defer: false,
           enabled: true,
           filter: {
               operator: '>=',
               property: 'some_property',
               value: 123
           },
           format: 'some format',
           formatter: function() { return true; },
           inside: true,
           nullFormat: 'some format',
           nullFormatter: function() { return true; },
           overflow: 'none',
           padding: 12,
           position: 'center',
           rotation: 0,
           shadow: false,
           shape: 'rect',
           style: 'style goes here',
           useHTML: false,
           verticalAlign: 'top',
           x: 10,
           y: 20,
           z: 0
         },
         linkOpacity: 0.5,
         states: {
           hover: {
               animation: {
                   duration: 123
               },
               borderColor: '#cccccc',
               brightness: 0.3,
               enabled: true
           },
           inactive: {
               enabled: true,
               opacity: 0.5
           },
           normal: {
               animation: {
                   defer: 24
               }
           },
           select: {
               color: '#ff0000',
               enabled: true,
           }
         },
         borderColor: '#ccc',
         borderWidth: 1,
         level: 1
        }
    ],
    linkColor: '#999',
    linkLineWidth: 1,
    linkOpacity: 0.7,
    linkRadius: 4,
    minLinkWidth: 1,
    minNodeLength: 12,
    nodePadding: 6,
    nodeWidth: 24,

    depth: 10,
    edgeColor: '#999',
    edgeWidth: 1,
    groupZPadding: 4,

    borderColor: '#ccc',
    borderRadius: 4,
    borderWidth: 2,
    centerInCategory: true,
    colorByPoint: true,
    colors: [
        '#fff',
        '#ccc',
        {
          linearGradient: {
              x1: 0.123,
              x2: 0.567,
              y1: 0.891,
              y2: 0.987
          },
          stops: [
              [0.123, '#cccccc'],
              [0.456, '#ff0000'],
              [1, '#00ff00']
          ]
        },
        {
          animation: {
              defer: 5
          },
          patternOptions: {
              aspectRatio: 0.5,
              backgroundColor: '#999999',
              id: 'some_id_goes_here',
              opacity: 0.5,
              width: 120,
              x: 5,
              y: 10
          },
          patternIndex: 2
        }
    ],
    grouping: false,
    groupPadding: 6,
    maxPointWidth: 12,
    minPointLength: 12,
    pointPadding: 6,
    pointRange: 24,
    pointWidth: 12,

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'organization'
  },
  packedbubble: {
    displayNegative: false,
    maxSize: 36,
    minSize: 12,
    parentNode: {
        allowPointSelect: true
    },
    sizeBy: 'area',
    useSimulation: true,
    zThreshold: 246,

    colorIndex: 3,
    crisp: true,
    draggable: true,
    findNearestPointBy: 'xy',
    layoutAlgorithm: {
        approximation: 'barnes-hut',
        attractiveForce: function() { return true; },
        enableSimulation: true,
        friction: 0.98,
        gravitationalConstant: 0.0625,
        initialPositionRadius: 1,
        initialPositions: 'circle',
        integration: 'euler',
        linkLength: 12,
        maxIterations: 1000,
        maxSpeed: 10,
        repulsiveForce: function() { return true; },
        theta: 0.5,
        type: 'reingold-fruchterman'
    },
    lineWidth: 2,
    link: {
        color: '#ccc',
        dashStyle: 'Solid',
        width: 1
    },
    relativeXValue: true,
    shadow: false,
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ],

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'packedbubble'
  },
  pareto: {
    colorAxis: 1,
    connectEnds: true,
    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true
    },
    negativeColor: '#fff',
    pointInterval: 5,
    pointIntervalUnit: 'weeks',
    pointPlacement: 'on',
    pointStart: 12,
    stacking: 'normal',

    animationLimit: 10,
    boostBlending: '#ccc',
    boostThreshold: 1234,
    colorIndex: 5,
    colorKey: 'some-key-value',
    connectNulls: true,
    crisp: true,
    cropThreshold: 123,
    dataSorting: {
        enabled: true,
        matchByName: true,
        sortKey: 'some-key-value'
    },
    findNearestPointBy: 'x',
    getExtremesFromAll: true,
    linecap: 'round',
    lineWidth: 2,
    relativeXValue: true,
    shadow: false,
    softThreshold: true,
    step: 'left',
    zoneAxis: 'y',
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ],

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'pareto'
  },
  pie: {
    borderColor: '#ccc',
    borderWidth: 1,
    center: ['50%', '50%'],
    colorAxis: 1,
    colorIndex: 3,
    colorKey: 'some-key-goes-here',
    colors: [
        '#fff',
        'ccc',
        {
          linearGradient: {
              x1: 0.123,
              x2: 0.567,
              y1: 0.891,
              y2: 0.987
          },
          stops: [
              [0.123, '#cccccc'],
              [0.456, '#ff0000'],
              [1, '#00ff00']
          ]
        },
        {
          animation: {
              defer: 5
          },
          patternOptions: {
              aspectRatio: 0.5,
              backgroundColor: '#999999',
              id: 'some_id_goes_here',
              opacity: 0.5,
              width: 120,
              x: 5,
              y: 10
          },
          patternIndex: 2
        }
    ],
    depth: 10,
    endAngle: 90,
    fillColor: '#fff',
    ignoreHiddenPoint: true,
    innerSize: '30%',
    linecap: 'round',
    minSize: '20%',
    size: 80,
    slicedOffset: 24,
    startAngle: 45,
    thickness: 2,

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'pie'
  },
  polygon: {
    colorAxis: 1,
    connectEnds: true,
    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true
    },
    negativeColor: '#fff',
    pointInterval: 5,
    pointIntervalUnit: 'weeks',
    pointPlacement: 'on',
    pointStart: 12,
    stacking: 'normal',

    animationLimit: 10,
    boostBlending: '#ccc',
    boostThreshold: 1234,
    colorIndex: 5,
    colorKey: 'some-key-value',
    connectNulls: true,
    crisp: true,
    cropThreshold: 123,
    dataSorting: {
        enabled: true,
        matchByName: true,
        sortKey: 'some-key-value'
    },
    findNearestPointBy: 'x',
    getExtremesFromAll: true,
    linecap: 'round',
    lineWidth: 2,
    relativeXValue: true,
    shadow: false,
    softThreshold: true,
    step: 'left',
    zoneAxis: 'y',
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ],

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'polygon'
  },
  pyramid: {
    height: '60%',
    neckHeight: '15%',
    neckWidth: 36,
    reversed: false,
    width: 320,

    borderColor: '#ccc',
    borderWidth: 1,
    center: ['50%', '50%'],
    colorAxis: 1,
    colorIndex: 3,
    colorKey: 'some-key-goes-here',
    colors: [
        '#fff',
        'ccc',
        {
          linearGradient: {
              x1: 0.123,
              x2: 0.567,
              y1: 0.891,
              y2: 0.987
          },
          stops: [
              [0.123, '#cccccc'],
              [0.456, '#ff0000'],
              [1, '#00ff00']
          ]
        },
        {
          animation: {
              defer: 5
          },
          patternOptions: {
              aspectRatio: 0.5,
              backgroundColor: '#999999',
              id: 'some_id_goes_here',
              opacity: 0.5,
              width: 120,
              x: 5,
              y: 10
          },
          patternIndex: 2
        }
    ],
    depth: 10,
    endAngle: 90,
    fillColor: '#fff',
    ignoreHiddenPoint: true,
    innerSize: '30%',
    linecap: 'round',
    minSize: '20%',
    size: 80,
    slicedOffset: 24,
    startAngle: 45,
    thickness: 2,

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'pyramid'
  },
  pyramid3d: {
    gradientForSides: true,

    height: '60%',
    neckHeight: '15%',
    neckWidth: 36,
    reversed: false,
    width: 320,

    borderColor: '#ccc',
    borderWidth: 1,
    center: ['50%', '50%'],
    colorAxis: 1,
    colorIndex: 3,
    colorKey: 'some-key-goes-here',
    colors: [
        '#fff',
        'ccc',
        {
          linearGradient: {
              x1: 0.123,
              x2: 0.567,
              y1: 0.891,
              y2: 0.987
          },
          stops: [
              [0.123, '#cccccc'],
              [0.456, '#ff0000'],
              [1, '#00ff00']
          ]
        },
        {
          animation: {
              defer: 5
          },
          patternOptions: {
              aspectRatio: 0.5,
              backgroundColor: '#999999',
              id: 'some_id_goes_here',
              opacity: 0.5,
              width: 120,
              x: 5,
              y: 10
          },
          patternIndex: 2
        }
    ],
    depth: 10,
    endAngle: 90,
    fillColor: '#fff',
    ignoreHiddenPoint: true,
    innerSize: '30%',
    linecap: 'round',
    minSize: '20%',
    size: 80,
    slicedOffset: 24,
    startAngle: 45,
    thickness: 2,

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'pyramid3d'
  },
  sankey: {
    borderColor: '#ccc',
    borderWidth: 2,
    center: ['50%', '30%'],
    centerInCategory: true,
    colorByPoint: false,
    colorIndex: 3,
    colors: [
        '#fff',
        'ccc',
        {
          linearGradient: {
              x1: 0.123,
              x2: 0.567,
              y1: 0.891,
              y2: 0.987
          },
          stops: [
              [0.123, '#cccccc'],
              [0.456, '#ff0000'],
              [1, '#00ff00']
          ]
        },
        {
          animation: {
              defer: 5
          },
          patternOptions: {
              aspectRatio: 0.5,
              backgroundColor: '#999999',
              id: 'some_id_goes_here',
              opacity: 0.5,
              width: 120,
              x: 5,
              y: 10
          },
          patternIndex: 2
        }
    ],
    curveFactor: 0.6,
    levels: [
        {
         colorByPoint: false,
         dataLabels: {
           align: 'center',
           allowOverlap: true,
           animation: {
               defer: 5
           },
           backgroundColor: {
               linearGradient: {
                   x1: 0.123,
                   x2: 0.234,
                   y1: 0.345,
                   y2: 0.456
               },
               stops: [
                   [0.12, '#999'],
                   [0.34, '#fff']
               ]
           },
           borderColor: '#999999',
           borderRadius: 24,
           borderWidth: 1,
           className: 'some-class-name',
           color: '#000000',
           crop: true,
           defer: false,
           enabled: true,
           filter: {
               operator: '>=',
               property: 'some_property',
               value: 123
           },
           format: 'some format',
           formatter: function() { return true; },
           inside: true,
           nullFormat: 'some format',
           nullFormatter: function() { return true; },
           overflow: 'none',
           padding: 12,
           position: 'center',
           rotation: 0,
           shadow: false,
           shape: 'rect',
           style: 'style goes here',
           useHTML: false,
           verticalAlign: 'top',
           x: 10,
           y: 20,
           z: 0
         },
         linkOpacity: 0.5,
         states: {
           hover: {
               animation: {
                   duration: 123
               },
               borderColor: '#cccccc',
               brightness: 0.3,
               enabled: true
           },
           inactive: {
               enabled: true,
               opacity: 0.5
           },
           normal: {
               animation: {
                   defer: 24
               }
           },
           select: {
               color: '#ff0000',
               enabled: true
           }
         },
         borderColor: '#ccc',
         borderWidth: 1,
         level: 1
        },
        {
         colorByPoint: false,
         dataLabels: {
           align: 'center',
           allowOverlap: true,
           animation: {
               defer: 5
           },
           backgroundColor: {
               linearGradient: {
                   x1: 0.123,
                   x2: 0.234,
                   y1: 0.345,
                   y2: 0.456
               },
               stops: [
                   [0.12, '#999'],
                   [0.34, '#fff']
               ]
           },
           borderColor: '#999999',
           borderRadius: 24,
           borderWidth: 1,
           className: 'some-class-name',
           color: '#000000',
           crop: true,
           defer: false,
           enabled: true,
           filter: {
               operator: '>=',
               property: 'some_property',
               value: 123
           },
           format: 'some format',
           formatter: function() { return true; },
           inside: true,
           nullFormat: 'some format',
           nullFormatter: function() { return true; },
           overflow: 'none',
           padding: 12,
           position: 'center',
           rotation: 0,
           shadow: false,
           shape: 'rect',
           style: 'style goes here',
           useHTML: false,
           verticalAlign: 'top',
           x: 10,
           y: 20,
           z: 0
         },
         linkOpacity: 0.5,
         states: {
           hover: {
               animation: {
                   duration: 123
               },
               borderColor: '#cccccc',
               brightness: 0.3,
               enabled: true
           },
           inactive: {
               enabled: true,
               opacity: 0.5
           },
           normal: {
               animation: {
                   defer: 24
               }
           },
           select: {
               color: '#ff0000',
               enabled: true
           }
         },
         borderColor: '#ccc',
         borderWidth: 1,
         level: 1
        },
        {
         colorByPoint: false,
         dataLabels: {
           align: 'center',
           allowOverlap: true,
           animation: {
               defer: 5
           },
           backgroundColor: {
               linearGradient: {
                   x1: 0.123,
                   x2: 0.234,
                   y1: 0.345,
                   y2: 0.456
               },
               stops: [
                   [0.12, '#999'],
                   [0.34, '#fff']
               ]
           },
           borderColor: '#999999',
           borderRadius: 24,
           borderWidth: 1,
           className: 'some-class-name',
           color: '#000000',
           crop: true,
           defer: false,
           enabled: true,
           filter: {
               operator: '>=',
               property: 'some_property',
               value: 123
           },
           format: 'some format',
           formatter: function() { return true; },
           inside: true,
           nullFormat: 'some format',
           nullFormatter: function() { return true; },
           overflow: 'none',
           padding: 12,
           position: 'center',
           rotation: 0,
           shadow: false,
           shape: 'rect',
           style: 'style goes here',
           useHTML: false,
           verticalAlign: 'top',
           x: 10,
           y: 20,
           z: 0
         },
         linkOpacity: 0.5,
         states: {
           hover: {
               animation: {
                   duration: 123
               },
               borderColor: '#cccccc',
               brightness: 0.3,
               enabled: true
           },
           inactive: {
               enabled: true,
               opacity: 0.5
           },
           normal: {
               animation: {
                   defer: 24
               }
           },
           select: {
               color: '#ff0000',
               enabled: true
           }
         },
         borderColor: '#ccc',
         borderWidth: 1,
         level: 1
        }
    ],
    linkOpacity: 0.7,
    minLinkWidth: 1,
    nodePadding: 6,
    nodeWidth: 12,
    startAngle: 45,

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'sankey'
  },
  scatter: {
    jitter: {
      x: 123,
      y: 456
    },

    colorAxis: 1,
    connectEnds: true,
    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true
    },
    negativeColor: '#fff',
    pointInterval: 5,
    pointIntervalUnit: 'weeks',
    pointPlacement: 'on',
    pointStart: 12,
    stacking: 'normal',

    animationLimit: 10,
    boostBlending: '#ccc',
    boostThreshold: 1234,
    colorIndex: 5,
    colorKey: 'some-key-value',
    connectNulls: true,
    crisp: true,
    cropThreshold: 123,
    dataSorting: {
        enabled: true,
        matchByName: true,
        sortKey: 'some-key-value'
    },
    findNearestPointBy: 'x',
    getExtremesFromAll: true,
    linecap: 'round',
    lineWidth: 2,
    relativeXValue: true,
    shadow: false,
    softThreshold: true,
    step: 'left',
    zoneAxis: 'y',
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ],
    type: 'scatter'
  },
  scatter3d: {
    jitter: {
      x: 123,
      y: 456
    },

    colorAxis: 1,
    connectEnds: true,
    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true
    },
    negativeColor: '#fff',
    pointInterval: 5,
    pointIntervalUnit: 'weeks',
    pointPlacement: 'on',
    pointStart: 12,
    stacking: 'normal',

    animationLimit: 10,
    boostBlending: '#ccc',
    boostThreshold: 1234,
    colorIndex: 5,
    colorKey: 'some-key-value',
    connectNulls: true,
    crisp: true,
    cropThreshold: 123,
    dataSorting: {
        enabled: true,
        matchByName: true,
        sortKey: 'some-key-value'
    },
    findNearestPointBy: 'x',
    getExtremesFromAll: true,
    linecap: 'round',
    lineWidth: 2,
    relativeXValue: true,
    shadow: false,
    softThreshold: true,
    step: 'left',
    zoneAxis: 'y',
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ],

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'scatter3d'
  },
  series: {
    colorAxis: 1,
    connectEnds: true,
    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true
    },
    negativeColor: '#fff',
    pointInterval: 5,
    pointIntervalUnit: 'weeks',
    pointPlacement: 'on',
    pointStart: 12,
    stacking: 'normal',

    animationLimit: 10,
    boostBlending: '#ccc',
    boostThreshold: 1234,
    colorIndex: 5,
    colorKey: 'some-key-value',
    connectNulls: true,
    crisp: true,
    cropThreshold: 123,
    dataSorting: {
        enabled: true,
        matchByName: true,
        sortKey: 'some-key-value'
    },
    findNearestPointBy: 'x',
    getExtremesFromAll: true,
    linecap: 'round',
    lineWidth: 2,
    relativeXValue: true,
    shadow: false,
    softThreshold: true,
    step: 'left',
    zoneAxis: 'y',
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ],

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'series'
  },
  solidgauge: {
    innerRadius: 123,
    overshoot: 12.5,
    radius: 246,
    rounded: true,

    colorAxis: 1,
    connectEnds: true,
    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true
    },
    negativeColor: '#fff',
    pointInterval: 5,
    pointIntervalUnit: 'weeks',
    pointPlacement: 'on',
    pointStart: 12,
    stacking: 'normal',

    animationLimit: 10,
    boostBlending: '#ccc',
    boostThreshold: 1234,
    colorIndex: 5,
    colorKey: 'some-key-value',
    connectNulls: true,
    crisp: true,
    cropThreshold: 123,
    dataSorting: {
        enabled: true,
        matchByName: true,
        sortKey: 'some-key-value'
    },
    findNearestPointBy: 'x',
    getExtremesFromAll: true,
    linecap: 'round',
    lineWidth: 2,
    relativeXValue: true,
    shadow: false,
    softThreshold: true,
    step: 'left',
    zoneAxis: 'y',
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ],

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'solidgauge'
  },
  spline: {
    colorAxis: 1,
    connectEnds: true,
    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true
    },
    negativeColor: '#fff',
    pointInterval: 5,
    pointIntervalUnit: 'weeks',
    pointPlacement: 'on',
    pointStart: 12,
    stacking: 'normal',

    animationLimit: 10,
    boostBlending: '#ccc',
    boostThreshold: 1234,
    colorIndex: 5,
    colorKey: 'some-key-value',
    connectNulls: true,
    crisp: true,
    cropThreshold: 123,
    dataSorting: {
        enabled: true,
        matchByName: true,
        sortKey: 'some-key-value'
    },
    findNearestPointBy: 'x',
    getExtremesFromAll: true,
    linecap: 'round',
    lineWidth: 2,
    relativeXValue: true,
    shadow: false,
    softThreshold: true,
    step: 'left',
    zoneAxis: 'y',
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ],

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'spline'
  },
  streamgraph: {
    fillColor: '#ccc',
    fillOpacity: 0.7,
    lineColor: {
        radialGradient: {
            cx: 0.123,
            cy: 0.456,
            r: 0.789
        },
        stops: [
            [0.123, '#cccccc'],
            [0.456, '#ff0000'],
            [1, '#00ff00']
        ]
    },
    negativeFillColor: '#ccc',
    trackByArea: true,

    colorAxis: 1,
    connectEnds: true,
    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true
    },
    negativeColor: '#fff',
    pointInterval: 5,
    pointIntervalUnit: 'weeks',
    pointPlacement: 'on',
    pointStart: 12,
    stacking: 'normal',

    animationLimit: 10,
    boostBlending: '#ccc',
    boostThreshold: 1234,
    colorIndex: 5,
    colorKey: 'some-key-value',
    connectNulls: true,
    crisp: true,
    cropThreshold: 123,
    dataSorting: {
        enabled: true,
        matchByName: true,
        sortKey: 'some-key-value'
    },
    findNearestPointBy: 'x',
    getExtremesFromAll: true,
    linecap: 'round',
    lineWidth: 2,
    relativeXValue: true,
    shadow: false,
    softThreshold: true,
    step: 'left',
    zoneAxis: 'y',
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ],

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'streamgraph'
  },
  sunburst: {
    allowTraversingTree: true,
    borderColor: '#ccc',
    borderWidth: 2,
    breadcrumbs: {
      buttonSpacing: 6,
      buttonTheme: {
          'fill': '#fff'
      },
      events: {
        click: function(event) { return true; }
      },
      floating: true,
      format: 'some format string',
      formatter: function () { return true; },
      relativeTo: 'plot',
      rtl: false,
      separator: {
          style: {
              'some-key': 'some-value'
          },
          text: '>'
      },
      useHTML: false,
      zIndex: 3
    },
    center: ['50%', '50%'],
    colorByPoint: true,
    colorIndex: 2,
    crisp: true,
    fillColor: '#999',
    levelIsConstant: true,
    levels: [
        {
         borderDashStyle: 'Solid',
         color: '#ccc',
         colorVariation: {
             key: 'brightness',
             to: 50
         },
         levelSize: {
             unit: 'percentage',
             value: 10
         },
         borderColor: '#ccc',
         borderWidth: 1,
         level: 1,
        }
    ],
    levelSize: {
        unit: 'percentage',
        value: 123
    },
    rootId: 'some-id-goes-here',
    shadow: false,
    size: '50%',
    slicedOffset: 12.3,
    startAngle: 0,

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'sunburst'
  },
  tilemap: {
    tileShape: 'hexagon',

    borderRadius: 4,
    colsize: 1,
    nullColor: '#ccc',
    pointPadding: 6,
    rowsize: 1,

    colorAxis: 1,
    connectEnds: true,
    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true
    },
    negativeColor: '#fff',
    pointInterval: 5,
    pointIntervalUnit: 'weeks',
    pointPlacement: 'on',
    pointStart: 12,
    stacking: 'normal',

    animationLimit: 10,
    boostBlending: '#ccc',
    boostThreshold: 1234,
    colorIndex: 5,
    colorKey: 'some-key-value',
    connectNulls: true,
    crisp: true,
    cropThreshold: 123,
    dataSorting: {
        enabled: true,
        matchByName: true,
        sortKey: 'some-key-value'
    },
    findNearestPointBy: 'x',
    getExtremesFromAll: true,
    linecap: 'round',
    lineWidth: 2,
    relativeXValue: true,
    shadow: false,
    softThreshold: true,
    step: 'left',
    zoneAxis: 'y',
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ],

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'tilemap'
  },
  timeline: {
    colorAxis: 'some-id-goes-here',
    colorByPoint: false,
    colorIndex: 2,
    colorKey: 'some-key-goes-here',
    crisp: false,
    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true
    },
    ignoreHiddenPoint: true,
    linecap: 'round',
    relativeXValue: true,

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'timeline'
  },
  treemap: {
    allowTraversingTree: true,
    alternateStartingDirection: false,
    animationLimit: 10,
    boostBlending: 'some-value-goes-here',
    boostThreshold: 5000,
    breadcrumbs: {
      buttonSpacing: 6,
      buttonTheme: {
          'fill': '#fff'
      },
      events: {
        click: function(event) { return true; }
      },
      floating: true,
      format: 'some format string',
      formatter: function () { return true; },
      relativeTo: 'plot',
      rtl: false,
      separator: {
          style: {
              'some-key': 'some-value'
          },
          text: '>'
      },
      useHTML: false,
      zIndex: 3
    },
    colorAxis: 'some-id-goes-here',
    colorByPoint: true,
    colorIndex: 2,
    colorKey: 'some-key-goes-here',
    colors: [
        '#ccc',
        '#fff',
        '000000'
    ],
    crisp: true,
    cropThreshold: 500,
    findNearestPointBy: 'xy',
    getExtremesFromAll: true,
    ignoreHiddenPoint: true,
    interactByLeaf: true,
    layoutAlgorithm: 'sliceAndDice',
    layoutStartingDirection: 'vertical',
    levelIsConstant: true,
    levels: [
        {
         borderDashStyle: 'Solid',
         color: '#ccc',
         colorVariation: {
             key: 'brightness',
             to: 50
         },
         layoutAlgorithm: 'sliceAndDice',
         layoutStartingDirection: 'vertical',
         borderColor: '#ccc',
         borderWidth: 1,
         level: 1,
        }
    ],
    linecap: 'round',
    lineWidth: 1,
    negativeColor: '#ccc',
    pointInterval: 5,
    pointIntervalUnit: 'day',
    pointStart: 1,
    relativeXValue: true,
    softThreshold: true,
    sortIndex: 2,
    stacking: 'normal',
    step: 'left',
    zoneAxis: 'y',
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ],
    type: 'treemap'
  },
  variablepie: {
    maxPointSize: '15%',
    minPointSize: '5%',
    sizeBy: 'area',
    zMax: 30,
    zMin: 2,

    borderColor: '#ccc',
    borderWidth: 1,
    center: ['50%', '50%'],
    colorAxis: 1,
    colorIndex: 3,
    colorKey: 'some-key-goes-here',
    colors: [
        '#fff',
        'ccc',
        {
          linearGradient: {
              x1: 0.123,
              x2: 0.567,
              y1: 0.891,
              y2: 0.987
          },
          stops: [
              [0.123, '#cccccc'],
              [0.456, '#ff0000'],
              [1, '#00ff00']
          ]
        },
        {
          animation: {
              defer: 5
          },
          patternOptions: {
              aspectRatio: 0.5,
              backgroundColor: '#999999',
              id: 'some_id_goes_here',
              opacity: 0.5,
              width: 120,
              x: 5,
              y: 10
          },
          patternIndex: 2
        }
    ],
    depth: 10,
    endAngle: 90,
    fillColor: '#fff',
    ignoreHiddenPoint: true,
    innerSize: '30%',
    linecap: 'round',
    minSize: '20%',
    size: 80,
    slicedOffset: 24,
    startAngle: 45,
    thickness: 2,

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'variablepie'
  },
  variwide: {
    borderColor: '#ccc',
    borderRadius: 4,
    borderWidth: 2,
    centerInCategory: true,
    colorByPoint: true,
    colors: [
        '#fff',
        '#ccc',
        {
          linearGradient: {
              x1: 0.123,
              x2: 0.567,
              y1: 0.891,
              y2: 0.987
          },
          stops: [
              [0.123, '#cccccc'],
              [0.456, '#ff0000'],
              [1, '#00ff00']
          ]
        },
        {
          animation: {
              defer: 5
          },
          patternOptions: {
              aspectRatio: 0.5,
              backgroundColor: '#999999',
              id: 'some_id_goes_here',
              opacity: 0.5,
              width: 120,
              x: 5,
              y: 10
          },
          patternIndex: 2
        }
    ],
    grouping: false,
    groupPadding: 6,
    maxPointWidth: 12,
    minPointLength: 12,
    pointPadding: 6,
    pointRange: 24,
    pointWidth: 12,

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'variwide'
  },
  vector: {
    cluster: {
      allowOverlap: true,
      animation: {
          defer: 5
      },
      dataLabels: {
        align: 'center',
        allowOverlap: true,
        animation: {
            defer: 5
        },
        backgroundColor: {
            linearGradient: {
                x1: 0.123,
                x2: 0.234,
                y1: 0.345,
                y2: 0.456
            },
            stops: [
                [0.12, '#999'],
                [0.34, '#fff']
            ]
        },
        borderColor: '#999999',
        borderRadius: 24,
        borderWidth: 1,
        className: 'some-class-name',
        color: '#000000',
        crop: true,
        defer: false,
        enabled: true,
        filter: {
            operator: '>=',
            property: 'some_property',
            value: 123
        },
        format: 'some format',
        formatter: function() { return true; },
        inside: true,
        nullFormat: 'some format',
        nullFormatter: function() { return true; },
        overflow: 'none',
        padding: 12,
        position: 'center',
        rotation: 0,
        shadow: false,
        shape: 'rect',
        style: 'style goes here',
        useHTML: false,
        verticalAlign: 'top',
        x: 10,
        y: 20,
        z: 0
      },
      drillToCluster: true,
      enabled: true,
      events: {
        drillToCluster: function(event) { return true; }
      },
      layoutAlgorithm: {
          distance: '20%',
          gridSize: 123,
          iterations: 5,
          kmeansThreshold: 1000
      },
      marker: {
        enabled: true,
        fillColor: '#cccccc',
        height: 24,
        lineWidth: 2,
        radius: 2,
        states: {
            hover: {
                enabled: true
            }
        },
        symbol: 'circle',
        width: 48
      },
      minimumClusterSize: 5,
      states: {
        hover: {
            animation: {
                duration: 123
            },
            borderColor: '#cccccc',
            brightness: 0.3,
            enabled: true
        },
        inactive: {
            enabled: true,
            opacity: 0.5
        },
        normal: {
            animation: {
                defer: 24
            }
        },
        select: {
            color: '#ff0000',
            enabled: true,
        }
      },
      zones: [
          {
           className: 'classname-1',
           from: 0,
           marker: {
             enabled: true,
             fillColor: '#cccccc',
             height: 24,
             lineWidth: 2,
             radius: 2,
             states: {
                 hover: {
                     enabled: true
                 }
             },
             symbol: 'circle',
             width: 48
           },
           to: 123
          },
          {
           className: 'classname-1',
           from: 0,
           marker: {
             enabled: true,
             fillColor: '#cccccc',
             height: 24,
             lineWidth: 2,
             radius: 2,
             states: {
                 hover: {
                     enabled: true
                 }
             },
             symbol: 'circle',
             width: 48
           },
           to: 123
          },
          {
           className: 'classname-1',
           from: 0,
           marker: {
             enabled: true,
             fillColor: '#cccccc',
             height: 24,
             lineWidth: 2,
             radius: 2,
             states: {
                 hover: {
                     enabled: true
                 }
             },
             symbol: 'circle',
             width: 48
           },
           to: 123
          }
      ]
    },
    rotationOrigin: 'start',
    vectorLength: 12,

    colorAxis: 1,
    connectEnds: true,
    dragDrop: {
        draggableX: true,
        draggableY: true,
        dragHandle: {
            className: 'draghandle-classname-goes-here',
            color: '#ccc',
            cursor: 'alias',
            lineColor: '#ddd',
            lineWidth: 2,
            pathFormatter: function() { return true; },
            zIndex: 10
        },
        dragMaxX: 3456,
        dragMaxY: 6532,
        dragMinX: 123,
        dragMinY: 321,
        dragPrecisionX: 5,
        dragPrecisionY: 5,
        dragSensitivity: 2,
        groupBy: 'some-property-name',
        guideBox: {
            default: {
                className: 'some-classname-goes-here',
                color: '#999',
                cursor: 'pointer',
                lineColor: '#ccc',
                lineWidth: 2,
                zIndex: 100
            }
        },
        liveRedraw: true
    },
    negativeColor: '#fff',
    pointInterval: 5,
    pointIntervalUnit: 'weeks',
    pointPlacement: 'on',
    pointStart: 12,
    stacking: 'normal',

    animationLimit: 10,
    boostBlending: '#ccc',
    boostThreshold: 1234,
    colorIndex: 5,
    colorKey: 'some-key-value',
    connectNulls: true,
    crisp: true,
    cropThreshold: 123,
    dataSorting: {
        enabled: true,
        matchByName: true,
        sortKey: 'some-key-value'
    },
    findNearestPointBy: 'x',
    getExtremesFromAll: true,
    linecap: 'round',
    lineWidth: 2,
    relativeXValue: true,
    shadow: false,
    softThreshold: true,
    step: 'left',
    zoneAxis: 'y',
    zones: [
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        },
        {
          className: 'some-class-name1',
          color: '#999999',
          dashStyle: 'Solid',
          fillColor: '#cccccc',
          value: 123
        }
    ],

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'vector'
  },
  venn: {
    animationLimit: 10,
    borderDashStyle: 'Solid',
    brighten: 10,
    cluster: {
      allowOverlap: true,
      animation: {
          defer: 5
      },
      dataLabels: {
        align: 'center',
        allowOverlap: true,
        animation: {
            defer: 5
        },
        backgroundColor: {
            linearGradient: {
                x1: 0.123,
                x2: 0.234,
                y1: 0.345,
                y2: 0.456
            },
            stops: [
                [0.12, '#999'],
                [0.34, '#fff']
            ]
        },
        borderColor: '#999999',
        borderRadius: 24,
        borderWidth: 1,
        className: 'some-class-name',
        color: '#000000',
        crop: true,
        defer: false,
        enabled: true,
        filter: {
            operator: '>=',
            property: 'some_property',
            value: 123
        },
        format: 'some format',
        formatter: function() { return true; },
        inside: true,
        nullFormat: 'some format',
        nullFormatter: function() { return true; },
        overflow: 'none',
        padding: 12,
        position: 'center',
        rotation: 0,
        shadow: false,
        shape: 'rect',
        style: 'style goes here',
        useHTML: false,
        verticalAlign: 'top',
        x: 10,
        y: 20,
        z: 0
      },
      drillToCluster: true,
      enabled: true,
      events: {
        drillToCluster: function(event) { return true; }
      },
      layoutAlgorithm: {
          distance: '20%',
          gridSize: 123,
          iterations: 5,
          kmeansThreshold: 1000
      },
      marker: {
        enabled: true,
        fillColor: '#cccccc',
        height: 24,
        lineWidth: 2,
        radius: 2,
        states: {
            hover: {
                enabled: true
            }
        },
        symbol: 'circle',
        width: 48
      },
      minimumClusterSize: 5,
      states: {
        hover: {
            animation: {
                duration: 123
            },
            borderColor: '#cccccc',
            brightness: 0.3,
            enabled: true
        },
        inactive: {
            enabled: true,
            opacity: 0.5
        },
        normal: {
            animation: {
                defer: 24
            }
        },
        select: {
            color: '#ff0000',
            enabled: true,
        }
      },
      zones: [
          {
           className: 'classname-1',
           from: 0,
           marker: {
             enabled: true,
             fillColor: '#cccccc',
             height: 24,
             lineWidth: 2,
             radius: 2,
             states: {
                 hover: {
                     enabled: true
                 }
             },
             symbol: 'circle',
             width: 48
           },
           to: 123
          },
          {
           className: 'classname-1',
           from: 0,
           marker: {
             enabled: true,
             fillColor: '#cccccc',
             height: 24,
             lineWidth: 2,
             radius: 2,
             states: {
                 hover: {
                     enabled: true
                 }
             },
             symbol: 'circle',
             width: 48
           },
           to: 123
          },
          {
           className: 'classname-1',
           from: 0,
           marker: {
             enabled: true,
             fillColor: '#cccccc',
             height: 24,
             lineWidth: 2,
             radius: 2,
             states: {
                 hover: {
                     enabled: true
                 }
             },
             symbol: 'circle',
             width: 48
           },
           to: 123
          }
      ]
    },
    colorAxis: 'some-id-goes-here',
    colorIndex: 2,
    colorKey: 'some-key-goes-here',
    crisp: true,
    relativeXValue: true,

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'venn'
  },
  waterfall: {
    lineColor: '#fff',
    upColor: '#999',

    depth: 10,
    edgeColor: '#999',
    edgeWidth: 1,
    groupZPadding: 4,

    borderColor: '#ccc',
    borderRadius: 4,
    borderWidth: 2,
    centerInCategory: true,
    colorByPoint: true,
    colors: [
        '#fff',
        '#ccc',
        {
          linearGradient: {
              x1: 0.123,
              x2: 0.567,
              y1: 0.891,
              y2: 0.987
          },
          stops: [
              [0.123, '#cccccc'],
              [0.456, '#ff0000'],
              [1, '#00ff00']
          ]
        },
        {
          animation: {
              defer: 5
          },
          patternOptions: {
              aspectRatio: 0.5,
              backgroundColor: '#999999',
              id: 'some_id_goes_here',
              opacity: 0.5,
              width: 120,
              x: 5,
              y: 10
          },
          patternIndex: 2
        }
    ],
    grouping: false,
    groupPadding: 6,
    maxPointWidth: 12,
    minPointLength: 12,
    pointPadding: 6,
    pointRange: 24,
    pointWidth: 12,

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'waterfall'
  },
  windbarb: {
    dataGrouping: {
      anchor: 'start',
      approximation: 'windbarb',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      enabled: true,
      firstAnchor: 'start',
      forced: true,
      groupAll: true,
      groupPixelWidth: 10,
      lastAnchor: 'end',
      units: [
          [
              'millisecond',
              [1, 2, 5, 10, 20, 25, 50, 100, 200, 500]
          ],
          [
              'second',
              [1, 2, 5, 10, 15, 30]
          ],
          [
              'minute',
              [1, 2, 5, 10, 15, 30]
          ],
          [
              'hour',
              [1, 2, 3, 4, 6, 8, 12]
          ],
          [
              'day',
              [1]
          ],
          [
              'week',
              [1]
          ],
          [
              'month',
              [1, 3, 6]
          ],
          [
              'year',
              null
          ]
      ]
    },
    onSeries: 'some-id-goes-here',
    vectorLength: 10,
    xOffset: 5,
    yOffset: 2,

    depth: 10,
    edgeColor: '#999',
    edgeWidth: 1,
    groupZPadding: 4,

    borderColor: '#ccc',
    borderRadius: 4,
    borderWidth: 2,
    centerInCategory: true,
    colorByPoint: true,
    colors: [
        '#fff',
        '#ccc',
        {
          linearGradient: {
              x1: 0.123,
              x2: 0.567,
              y1: 0.891,
              y2: 0.987
          },
          stops: [
              [0.123, '#cccccc'],
              [0.456, '#ff0000'],
              [1, '#00ff00']
          ]
        },
        {
          animation: {
              defer: 5
          },
          patternOptions: {
              aspectRatio: 0.5,
              backgroundColor: '#999999',
              id: 'some_id_goes_here',
              opacity: 0.5,
              width: 120,
              x: 5,
              y: 10
          },
          patternIndex: 2
        }
    ],
    grouping: false,
    groupPadding: 6,
    maxPointWidth: 12,
    minPointLength: 12,
    pointPadding: 6,
    pointRange: 24,
    pointWidth: 12,

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'windbarb'
  },
  wordcloud: {
    allowExtendPlayingField: false,
    animationLimit: 10,
    borderColor: '#ccc',
    borderRadius: 2,
    borderWidth: 1,
    centerInCategory: true,
    colorByPoint: false,
    colorIndex: 2,
    colorKey: 'some-key-goes-here',
    colors: [
        '#ccc',
        '#fff',
        '000000'
    ],
    edgeWidth: 1,
    maxFontSize: 36,
    minFontSize: 6,
    placementStrategy: 'center',
    rotation: {
        from: 0,
        orientations: 4,
        to: 135
    },
    spiral: 'rectangle',

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'wordcloud'
  },
  xrange: {
    groupZPadding: 4,
    partialFill: {
      fill: '#cccccc'
    },

    borderColor: '#ccc',
    borderRadius: 4,
    borderWidth: 2,
    centerInCategory: true,
    colorByPoint: true,
    colors: [
        '#fff',
        '#ccc',
        {
          linearGradient: {
              x1: 0.123,
              x2: 0.567,
              y1: 0.891,
              y2: 0.987
          },
          stops: [
              [0.123, '#cccccc'],
              [0.456, '#ff0000'],
              [1, '#00ff00']
          ]
        },
        {
          animation: {
              defer: 5
          },
          patternOptions: {
              aspectRatio: 0.5,
              backgroundColor: '#999999',
              id: 'some_id_goes_here',
              opacity: 0.5,
              width: 120,
              x: 5,
              y: 10
          },
          patternIndex: 2
        }
    ],
    grouping: false,
    groupPadding: 6,
    maxPointWidth: 12,
    minPointLength: 12,
    pointPadding: 6,
    pointRange: 24,
    pointWidth: 12,

    accessibility: {
        description: 'Description goes here',
        enabled: true,
        exposeAsGroupOnly: true,
        keyboardNavigation: {
            enabled: true
        },
        point: {
            dateFormat: 'format string',
            dateFormatter: function() { return true; },
            describeNull: false,
            descriptionFormatter: function() { return true; },
            valueDecimals: 2,
            valueDescriptionFormat: 'format string',
            valuePrefix: '$',
            valueSuffix: 'USD'
        },
    },
    allowPointSelect: true,
    animation: {
        defer: 5
    },
    className: 'some-class-name',
    clip: false,
    color: '#fff',
    cursor: 'alias',
    custom: {
        'item1': 'some value',
        'item2': 'some value'
    },
    dashStyle: 'Dash',
    dataLabels: {
      align: 'center',
      allowOverlap: true,
      animation: {
          defer: 5
      },
      backgroundColor: {
          linearGradient: {
              x1: 0.123,
              x2: 0.234,
              y1: 0.345,
              y2: 0.456
          },
          stops: [
              [0.12, '#999'],
              [0.34, '#fff']
          ]
      },
      borderColor: '#999999',
      borderRadius: 24,
      borderWidth: 1,
      className: 'some-class-name',
      color: '#000000',
      crop: true,
      defer: false,
      enabled: true,
      filter: {
          operator: '>=',
          property: 'some_property',
          value: 123
      },
      format: 'some format',
      formatter: function() { return true; },
      inside: true,
      nullFormat: 'some format',
      nullFormatter: function() { return true; },
      overflow: 'none',
      padding: 12,
      position: 'center',
      rotation: 0,
      shadow: false,
      shape: 'rect',
      style: 'style goes here',
      useHTML: false,
      verticalAlign: 'top',
      x: 10,
      y: 20,
      z: 0
    },
    description: 'Description goes here',
    enableMouseTracking: true,
    events: {
      afterAnimate: function(event) { return true; },
      click: function(event) { return true; },
      hide: function(event) { return true; },
      mouseOut: function(event) { return true; },
      show: function(event) { return true; }
    },
    includeInDataExport: true,
    keys: [
        'somevalue',
        'somevalue',
        'somevalue'
    ],
    label: {
        boxesToAvoid: [
            {
             bottom: 12,
             left: -46,
             right: 84,
             top: 24
            },
            {
             bottom: 48,
             left: -46,
             right: 84,
             top: 86
            }
        ],
        connectorAllowed: true,
        connectorNeighbourDistance: 12,
        enabled: true,
        format: 'format string',
        formatter: function() { return true; },
        maxFontSize: 18,
        minFontSize: 6,
        onArea: false,
        style: 'some style string'
    },
    linkedTo: 'some_id',
    marker: {
      enabled: true,
      fillColor: '#cccccc',
      height: 24,
      lineWidth: 2,
      radius: 2,
      states: {
          hover: {
              enabled: true
          }
      },
      symbol: 'circle',
      width: 48
    },
    onPoint: {
        connectorOptions: {
            dashstyle: 'Dash',
            stroke: '#ccc',
            width: 2
        },
        id: 'some-id',
        position: {
            align: 'left',
            verticalAlign: 'top',
            x: 15,
            y: -46
        }
    },
    opacity: 0.2,
    point: {
        events: {
          click: function(event) { return true; },
          drag: function(event) { return true; },
          drop: function(event) { return true; },
          mouseOut: function(event) { return true; }
        }
    },
    pointDescriptionFormatter: function (point) { return true; },
    selected: false,
    showCheckbox: true,
    showInLegend: true,
    skipKeyboardNavigation: false,
    states: {
      hover: {
          animation: {
              duration: 123
          },
          borderColor: '#cccccc',
          brightness: 0.3,
          enabled: true
      },
      inactive: {
          enabled: true,
          opacity: 0.5
      },
      normal: {
          animation: {
              defer: 24
          }
      },
      select: {
          color: '#ff0000',
          enabled: true,
      }
    },
    stickyTracking: true,
    threshold: 123,
    tooltip: {
      animation: true,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      clusterFormat: 'format string',
      dateTimeLabelFormats: {
        day: 'test',
        hour: 'test',
        millisecond: 'test',
        minute: 'test',
        month: 'test',
        second: 'test',
        week: 'test',
        year: 'test'
      },
      distance: 12,
      enabled: true,
      followPointer: true,
      followTouchMove: true,
      footerFormat: 'format string',
      formatter: function() { return true; },
      headerFormat: 'format string',
      headerShape: 'circle',
      hideDelay: 3,
      nullFormat: 'format string',
      nullFormatter: function() { return true; },
      outside: false,
      padding: 6,
      pointFormat: 'format string',
      pointFormatter: function() { return true; },
      positioner: function() { return true; },
      shadow: false,
      shape: 'rect',
      shared: false,
      snap: 4,
      split: false,
      stickOnContact: true,
      style: 'style string goes here',
      useHTML: false,
      valueDecimals: 2,
      valuePrefix: '$',
      valueSuffix: ' USD',
      xDateFormat: 'format string'
     },
    turboThreshold: 456,
    visible: true,
    type: 'xrange'
  }
}

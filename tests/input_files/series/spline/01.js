{
  data: [
    {
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
      drilldown: 'some-id-goes-here',
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
      y: 123,
      name: 'some category'
    }
  ],
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
  ]
}

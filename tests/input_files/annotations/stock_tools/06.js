{
  controlPointOptions: {
      positioner: function(x, target) { return true; }
  },
  labelOptions: {
      accessibility: {
          description: 'Description goes here'
      },
      align: 'center',
      allowOverlap: false,
      backgroundColor: '#ccc',
      borderColor: '#999',
      borderRadius: 4,
      borderWidth: 1,
      className: 'some-class-name',
      crop: false,
      distance: 10,
      format: 'format string',
      formatter: function() { return true; },
      includeInDataExport: true,
      overflow: 'justify',
      padding: 12,
      shadow: false,
      shape: 'callout',
      style: 'style-string-goes-here',
      text: 'format string',
      useHTML: false,
      verticalAlign: 'top',
      x: 5,
      y: 10
  },
  shapeOptions: {
      dashStyle: 'Solid',
      fill: '#000',
      height: 123,
      r: 12,
      ry: 24,
      snap: 5,
      src: 'https://www.somewhere.com',
      stroke: '#ccc',
      strokeWidth: 1,
      type: 'rect',
      width: 12,
      xAxis: 1,
      yAxis: 1
  },
  typeOptions: {
    background: {
      fill: '#ccc',
      stroke: 'rgba(255,255,0)',
      strokeWidth: 2
    },
    crosshairX: {
      className: 'some-class-name',
      color: '#ccc',
      dashStyle: 'Solid',
      snap: true,
      width: 6,
      zIndex: 3
    },
    crosshairY: {
      className: 'some-class-name',
      color: '#ccc',
      dashStyle: 'Solid',
      snap: true,
      width: 6,
      zIndex: 3
    },
    label: {
      enabled: true,
      formatter: function() { return true; },
      style: {
        color: '#ccc',
        fontSize: '11px'
      }
    },
    line: {
      fill: '#ccc'
    },
    points: [
      {
        controlPoint: 1,
        x: 5,
        y: 15
      },
      {
        controlPoint: 2,
        x: 10,
        y: 25
      }
    ],
    selectType: 'xy',
    xAxis: 5,
    yAxis: 'some-id'
  }
}

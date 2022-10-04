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
    line: {
      fill: '#ccc'
    },
    points: [
      'invalid value',
      {
        controlPoint: 2,
        x: 10
      }
    ],
    xAxis: 5,
    yAxis: 'some-id'
  }
}

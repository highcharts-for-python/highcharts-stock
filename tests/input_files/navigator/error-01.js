{
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
  series: 'invalid value',
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
}

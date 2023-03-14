{
    alignThresholds: true,
    alignTicks: true,
    allowMutatingData: true,
    animation: false,
    backgroundColor: '#fff',
    borderColor: '#ccc',
    borderRadius: 3,
    borderWidth: 1,
    className: 'some-class-name',
    colorCount: 10,
    displayErrors: true,
    events: {
      addSeries: function(event) { return true;},
      afterPrint: function(event) {return true;},
      click: function(event) { return true; },
      selection: function(event) { return true; }
    },
    height: 120,
    ignoreHiddenSeries: false,
    inverted: false,
    margin: [20, 20, 20, 20],
    marginBottom: 20,
    marginLeft: 20,
    marginRight: 20,
    marginTop: 20,
    numberFormatter: function(value) { return true; },
    panKey: 'ctrl',
    panning: {
        enabled: true,
        type: 'x'
    },
    parallelCoordinates: false,
    plotBackgroundColor: '#ccc',
    plotBackgroundImage: 'http://www.somewhere.com',
    plotBorderColor: '#999',
    plotBorderWidth: 1,
    plotShadow: false,
    polar: false,
    reflow: false,
    renderTo: 'some-id',
    scrollablePlotArea: {
        minHeight: 120,
        minWidth: 300,
        opacity: 0.6,
        scrollPositionX: 0,
        scrollPositionY: 0
    },
    selectionMarkerFill: '#ccc',
    shadow: false,
    showAxes: true,
    spacing: [5, 5, 5, 5],
    spacingBottom: 5,
    spacingLeft: 5,
    spacingRight: 5,
    spacingTop: 5,
    style: 'style-string-goes-here',
    styledMode: false,
    type: 'line',
    width: 50,
    zooming: {
      key: 'alt',
      pinchType: 'xy',
      resetButton: {
          position: {
            align: 'center',
            verticalAlign: 'top',
            x: -10,
            y: 10
          },
          relativeTo: 'plot',
          theme: {
              'fill': '#ccc'
          }
      },
      singleTouch: false,
      type: 'xy'
    }
}

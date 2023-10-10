  .. note::

    The keyword pattern outlined below is supported by both the
    :class:`Chart <highcharts_stock.chart.Chart>` and
    :class:`HighchartsOptions <highcharts_stock.options.HighchartsOptions>`
    classes

.. code-block:: python

  from highcharts_stock.chart import Chart
  from highcharts_stock.options.series.area import LineSeries

  # EXAMPLE 1. Indicating data and series_type.
  my_chart = Chart(data = [[0, 1], [1, 2], [2, 3]],
                   series_type = 'line')

  # EXAMPLE 2. Supplying the Series instance(s) directly.
  my_chart = Chart(series = LineSeries(data = [
                                            [0, 1],
                                            [1, 2],
                                            [2, 3]
                                      ]))
  
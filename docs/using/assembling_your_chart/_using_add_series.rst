  .. note::

    ``.add_series()`` is supported by both the
    :class:`Chart <highcharts_stock.chart.Chart>` and
    :class:`HighchartsStockOptions <highcharts_stock.options.HighchartsStockOptions>`
    classes

.. code-block:: python

  my_chart = Chart()
  my_chart.add_series(my_series1, my_series2)

  my_series = LineSeries()
  my_chart.add_series(my_series)

.. collapse:: Method Signature

  .. method:: .add_series(self, *series)
    :noindex:

    Adds ``series`` to the
    :meth:`Chart.options.series <highcharts_stock.options.HighchartsStockOptions.series>`
    property.

    :param series: One or more :term:`series` instances (descended from
      :class:`SeriesBase <highcharts_stock.options.series.base.SeriesBase>`) or an
      instance (e.g. :class:`dict <python:dict>`, :class:`str <python:str>`, etc.)
      coercable to one
    :type series: :class:`SeriesBase <highcharts_stock.options.series.base.SeriesBase>`
      or coercable

.. tabs::

  .. tab:: Using ``Series.add_indicator()``

    .. note::

      All standard :term:`series` (descending from
      :class:`SeriesBase <highcharts_stock.options.series.base.SeriesBase>`) have an
      :meth:`.add_indicator() <highcharts_stock.options.series.base.SeriesBase>` method
      which can be used to easily configure a new indicator tied to the series in
      question.

    .. code-block:: python

      # Given a series instance in the variable "my_series"

      # Create a Chart instance
      my_chart = Chart.from_series(my_series)

      # Adds a new Simple Moving Average indicator to the chart, based off of the
      # "my_series" series.

      my_chart = my_series.add_indicator(my_chart, indicator_name = 'sma')

    .. collapse:: Method Signature

      .. method:: .add_indicator(chart, indicator_name, indicator_kwargs = None)
        :noindex:

        :param chart: The chart object in which the series is rendered and to which the
          indicator should be appended.
        :type chart: :class:`Chart <highcharts_stock.chart.Chart>`

        :param indicator_name: The name of the indicator that should be added to the series
          and chart. For the list of supported indicators, please review the
          :ref:`Indicator List <indicator_list>`.
        :type indicator_name: :class:`str <python:str>`

        :param indicator_kwargs: Keyword arguments to apply when instantiating the new
          indicator series. Defaults to :obj:`None <python:None>`.
        :type indicator_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`

        :returns: ``chart`` with a new indicator series included in its list of configured
          series.
        :rtype: :class:`Chart <highcharts_stock.chart.Chart>`

  .. tab:: Using ``Chart.add_indicator()``

    .. code-block:: python

      # Given a series instance with ID "my-series-id" in the variable "my_series"

      # Create a Chart instance from the series "my_series"
      my_chart = Chart.from_series(my_series)

      # Add a Simple Moving Average indicator to the series with the ID "my-series-id"
      my_chart.add_indicator(indicator_name = 'sma',
                             series = 'my-series-id')

      # Create a new Chart instance
      my_chart2 = Chart(options = {})

      # Add a Simple Moving Average indicator AND the series with the ID "my-series-id"
      # to the chart in "my_chart2"
      my_chart2.add_indicator(indicator_name = 'sma',
                              series = my_series)

    .. collapse:: Method Signature

      .. method:: .add_indicator(indicator_name, series, indicator_kwargs = None)
        :noindex:

        Creates a :class:`IndicatorSeriesBase` (descendant) that calculates the
        ``indicator_name`` :term:`technical indicator` for the series provided in
        ``series``, and adds it to the chart's
        :meth:`.options.series <highcharts_stock.options.HighchartsStockOptions.series>`.

        :param indicator_name: The name of the indicator that should be added to the series
          and chart. For the list of supported indicators, please review the
          :ref:`Indicator List <indicator_list>`.
        :type indicator_name: :class:`str <python:str>`

        :param series: The series to which the indicator should be added. Accepts either a
          series' :meth:`.id <highcharts_stock.options.series.SeriesBase.id>` as a
          :class:`str <python:str>`, or a
          :class:`SeriesBase <highcharts_stock.options.series.base.SeriesBase>` (descendant)
          instance.
        :type series: :class:`str <python:str>` or
          :class:`SeriesBase <highcharts_stock.options.series.base.SeriesBase>`

        :param indicator_kwargs: Keyword arguments to apply when instantiating the new
          indicator series. Defaults to :obj:`None <python:None>`.
        :type indicator_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`

        :returns: Nothing. It simply changes the composition of the chart instance's
          series to now include a new series with the indicator.

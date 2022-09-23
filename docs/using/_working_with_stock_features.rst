.. tabs::

  .. tab:: Stock Tools

    Stock tools are a custom toolbar that can be displayed on your chart which allows your
    users to interact with your chart in various ways. Using event bindings tied to the
    stock tools, you can toggle annotations, toggle
    :term:`technical indicators <technical indicator>`, or control the chart's zoom level.

      .. figure:: /_static/stock-tools-example.png
        :alt: Stock Tools Example
        :align: center

    To display the stock tools in your chart, you can use the
    :meth:`HighchartsStockOptions.stock_tools <highcharts_stock.options.HighchartsStockOptions.stock_tools>`
    setting, which can be configured using a
    :class:`StockTools <highcharts_stock.options.stock_tools.StockTools>` instance.

      .. code-block:: python

        my_stock_tools = StockTools(gui = { 'enabled': True })
        my_options = HighchartsStockOptions(stock_tools = my_stock_tools)
        my_chart = Chart.from_options(my_options)

      .. seealso::

        * :class:`StockTools <highcharts_stock.options.stock_tools.StockTools>`
        * :class:`StockToolsGUI <highcharts_stock.options.stock_tools.StockToolsGUI>`

  .. tab:: Navigator

    The :term:`Navigator` is a small series shown below the main series which displays a
    zoomed-out view of the entire dataset. It allows you to zoom in / out or jump to a
    particular range of time in the chart.

      .. figure:: /_static/navigator-example.png
        :alt: Navigator
        :align: center

    The navigator is enabled by default in :class:`Chart <highcharts_stock.chart.Chart>`
    instances where :meth:`.is_stock_chart <highcharts_stock.chart.Chart.is_stock_chart>`
    is ``True`` or whose :meth:`.options <highcharts_stock.chart.Chart.options>` contain
    a :class:`HighchartsStockOptions <highcharts_stock.options.HighchartsStockOptions>`
    instance.

    You can configure how the navigator is rendered using several different methods:

      * You can configure whether individual series are shown in the navigator by setting
        their ``.show_in_navigator`` property to ``True`` (to show) or ``False`` (to hide)
      * You can configure how the series is rendered within the navigator by setting their
        ``.navigator_options`` property.
      * You can set general navigator options for the series type by setting their
        ``PlotOptions.<SERIES TYPE>.show_in_navigator`` and
        ``PlotOptions.<SERIES TYPE>.navigator_options`` properties.
      * You can set overall configuration settings for the entire navigator using the
        :meth:`HighchartsStockOptions.navigator <highcharts_stock.HighchartsStockOptions.navigator>`
        setting.

    .. seealso::

      * :class:`Navigator <highcharts_stock.options.navigator.Navigator>`

  .. tab:: Range Selector

    The :term:`Range Selector` is a small tool displayed above (or beside) the
    visualization which allows the user to pre-select the time range that is displayed
    on the chart.

      .. figure:: /_static/range-selector-example.png
        :alt: Range Selector Example
        :align: center

    Based upon its configuration (via the
    :meth:`HighchartsStockOptions.options.range_selector <highcharts_stock.options.HighchartsStockOptions.options.range_selector>`
    property), it can display a series of buttons that allow the user to zoom to a
    specific granularity (e.g. display one day's worth of data, display one week's worth
    of data, display one month's worth of data, etc.) and can provide the user with inputs
    to select the range (start date / end date) which should be displayed.

    .. note::

      By default, the range selector is rendered in a responsive fashion. If there is not
      enough room to display the entire selector in a single row, it will collapse into a
      dropdown configuration based on the
      :meth:`RangeSelector.dropdown <highcharts_stock.options.range_selector.RangeSelector.dropdown>`
      setting.

    .. seealso::

      * :class:`RangeSelector <highcharts_stock.options.range_selector.RangeSelector>`
      * :meth:`HighchartsStockOptions.range_selector <highcharts_stock.options.HighchartsStockOptions.range_selector>`

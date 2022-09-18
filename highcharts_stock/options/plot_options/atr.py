from highcharts_stock.options.plot_options.indicators import ComparableIndicatorOptions


class ATROptions(ComparableIndicatorOptions):
    """Options to configure an Average True Range :term:`indicator <technical indicator>`,
    which is a measure of the degree of volatility in a value over time using a look-back
    period determined by the configuration of
    :meth:`.params <highcharts_stock.options.plot_options.atr.ATROptions.params`.

    .. figure:: ../../../_static/atr-example.png
      :alt: ATR Example Chart
      :align: center

    """
    pass


class NATROptions(ComparableIndicatorOptions):
    """Options to configure a Normalized Average True Range
    :term:`indicator <technical indicator>`.

    .. figure:: ../../../_static/natr-example.png
      :alt: NATR Example Chart
      :align: center

    """
    pass

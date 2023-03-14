from typing import Optional

from validator_collection import validators

from highcharts_core.utility_classes.data_grouping import DataGroupingOptions as DataGroupingBase

from highcharts_stock.decorators import validate_types
from highcharts_stock.utility_classes.javascript_functions import CallbackFunction


class DataGroupingOptions(DataGroupingBase):
    """Data grouping configures sampling the data values into larger blocks in order
    to ease readability and increase performance of the JavaScript charts.

    Highcharts Stock by default applies data grouping when the points become closer
    than the number of pixels specified by the
    :meth:`.group_pixel_width <highcharts_stock.utility_classes.data_grouping.DataGroupingOptions.group_pixel_width>`
    setting.

    .. note::

      If data grouping is applied, the grouping information of grouped points can be
      read (in JavaScript) from ``Point.dataGroup``.

    .. caution::

      In `Highcharts for Python <https://core-docs.highchartspython.com>`__ and
      `Highcharts JS <https://www.highcharts.com>`__, usage of the data grouping requires
      the ``modules/datagrouping.js`` JavaScript module. In
      **Highcharts Stock for Python**, it is included by default.


    .. caution::

      If point options other than the data itself are set, for example ``name``,
      ``color``, or custom properties, the grouping logic will not know how to group
      it. In this case, the options of the first point instance are copied over to the
      group point. This can be altered through a custom
      :meth:`approximation <highcharts_stock.utility_classes.data_grouping.DataGroupingOptions.approximation>`
      function.

    """

    @property
    def approximation(self) -> Optional[str | CallbackFunction]:
        """The method of approximation within a group. For example, when 30 days are
        grouped into a one month period, this property determines what value should
        represent the entire group.

        Accepts the following values if not using a custom function:

          * ``'average'``
          * ``'averages'``
          * ``'hlc'``
          * ``'ohlc'``
          * ``'open'``
          * ``'high'``
          * ``'low'``
          * ``'close'``
          * ``'sum'``
          * ``'range'``
          * ``'windbarb'``

        The default value will depend on the series type for which data grouping is being
        applied:

          * :class:`WindBarbSeries <highcharts_stock.options.series.windbarb.WindBarbSeries>`
            will default to ``'windbarb'``,
          * :class:`OHLCSeries <highcharts_stock.options.series.OHLCSeries>`,
            :class:`Candlestick <highcharts_stock.options.series.CandlestickSeries>`, will
            default to ``'ohlc'`` which are then calculated from the open, high, low, and
            close values.
          * :class:`HLCSeries <highcharts_stock.options.series.HLCSeries>` will default to
            ``'hlc'``, which then calculate the grouped values from the high, low, and
            close values.
          * For range-type series, will default to ``'range'``, which then calculates
            grouped values from the low and high-end values.
          * For line-type series, will default to ``'average'``.
          * For column-type series will default to ``'sum'``.
          * For all other data, will default to ``'averages'``.

        Custom aggregate methods can be added by assigning a :term:`callback function` as
        the approximation. This function should take a numeric array as the argument and
        should return a single numeric value or (JavaScript) ``null``.

          .. note::

            The numeric array will never contain null values, only true numbers. Instead,
            if null values are present in the raw data, the numeric array will have a
            (JavaScript) ``.hasNulls`` property set to ``true``.

            For single-value data sets the data is available in the first argument of the
            callback function. For OHLC data sets, all the open values are in the first
            argument, all high values in the second, etc.

        .. tip::

          Grouping meta data is available in the (JavaScript) approximation callback via
          ``this.dataGroupInfo``. It can be used to extract information from the raw data.

        :rtype: :class:`str <python:str>` or
          :class:`CallbackFunction <highcharts_core.utility_classes.javascript_functions.CallbackFunction>`
          or :obj:`None <python:None>`
        """
        return self._approximation

    @approximation.setter
    def approximation(self, value):
        if not value:
            self._approximation = None
        else:
            try:
                value = validate_types(value, CallbackFunction)
            except (ValueError, TypeError):
                value = validators.string(value)

            self._approximation = value

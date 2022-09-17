from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts_python.decorators import class_sensitive
from highcharts_python.metaclasses import HighchartsMeta
from highcharts_python.options.plot_options.series import SeriesOptions

from highcharts_stock import errors
from highcharts_stock.utility_classes.data_grouping import DataGroupingOptions
from highcharts_stock.utility_classes.last_price import LastPriceOptions


class ParameterBase(HighchartsMeta):
    """Base class for parameters used to calculate technical indicators."""

    def __init__(self, **kwargs):
        self._index = None
        self._period = None

        self.index = kwargs.get('index', None)
        self.period = kwargs.get('period', None)

    @property
    def index(self) -> Optional[int]:
        """The point value index which selects the value on which :term:`indicator`
        calculations will be based. Defaults to ``0``.

        For example, using OHLC data, a value of ``2`` means that the indicator will be
        calculated using the **Low** value of each data point.

        .. note::

          When applied to specific indicator types, the default value may change. Please
          see the documentation for the specific indicator, as applicable.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._index

    @index.setter
    def index(self, value):
        self._index = validators.integer(value,
                                         allow_empty = True,
                                         minimum = 0)

    @property
    def period(self) -> Optional[int]:
        """The base period for indicator calculations. This is the number of data points
        which are taken into account for when calculating the :term:`indicator`. Defaults
        to ``14``.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._period

    @period.setter
    def period(self, value):
        self._period = validators.integer(value,
                                          allow_empty = True,
                                          minimum = 0)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'index': as_dict.get('index', None),
            'period': as_dict.get('period', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'index': self.index,
            'period': self.period
        }

        return untrimmed


class IndicatorOptions(SeriesOptions):
    """Options for series that can be used as :term:`indicators` in
    **Highcharts Stock for Python**.
    """

    def __init__(self, **kwargs):
        self._compare_start = None
        self._compare_to_main = None
        self._cumulative = None
        self._data_as_columns = None
        self._data_grouping = None
        self._gap_size = None
        self._gap_unit = None
        self._last_price = None
        self._last_visible_price = None
        self._name = None
        self._params = None

        self.compare_start = kwargs.get('compare_start', None)
        self.compare_to_main = kwargs.get('compare_to_main', None)
        self.cumulative = kwargs.get('cumulative', None)
        self.data_as_columns = kwargs.get('data_as_columns', None)
        self.data_grouping = kwargs.get('data_grouping', None)
        self.gap_size = kwargs.get('gap_size', None)
        self.gap_unit = kwargs.get('gap_unit', None)
        self.last_price = kwargs.get('last_price', None)
        self.last_visible_price = kwargs.get('last_visible_price', None)
        self.name = kwargs.get('name', None)
        self.params = kwargs.get('params', None)

        super().__init__(**kwargs)

    @property
    def compare_start(self) -> Optional[bool]:
        """If ``True``, the first point in the visible range will be used for the
        comparative calculation, essentially starting from ``0``. If ``False``, the
        comparison will be performed based on the data point immediately *prior* to the
        visible range. Defaults to ``False``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._compare_start

    @compare_start.setter
    def compare_start(self, value):
        if value is None:
            self._compare_start = None
        else:
            self._compare_start = bool(value)

    @property
    def compare_to_main(self) -> Optional[bool]:
        """If ``True``, compares the indicator to the main series values. If ``False``,
        compares to the indicator values. Defaults to ``False``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._compare_to_main

    @compare_to_main.setter
    def compare_to_main(self, value):
        if value is None:
            self._compare_to_main = None
        else:
            self._compare_to_main = bool(value)

    @property
    def cumulative(self) -> Optional[bool]:
        """If ``True``, replaces points' values with the following (logcical) formula:

          ``sum of all previous visible points' values + current point's value``

        .. caution::

          This calculation is only applied to points in the visible range.

        If ``False``, the point values remain unchanged and are presented as-is. Defaults
        to ``False``.

        .. note::

          In JavaScript, each point object for the series will now have a new property -
          ``.cumulativeSum`` - available for use in formatter
          :term:`callback functions <callback function>` or format strings.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._cumulative

    @cumulative.setter
    def cumulative(self, value):
        if value is None:
            self._cumulative = None
        else:
            self._cumulative = bool(value)

    @property
    def data_as_columns(self) -> Optional[bool]:
        """If ``True``, indicates that the data is structured as columns instead of as
        rows. Defaults to ``False``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._data_as_columns

    @data_as_columns.setter
    def data_as_columns(self, value):
        if value is None:
            self._data_as_columns = None
        else:
            self._data_as_columns = bool(value)

    @property
    def data_grouping(self) -> Optional[DataGroupingOptions]:
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

          If point options other than the data itself are set, for example ``name``,
          ``color``, or custom properties, the grouping logic will not know how to group
          it. In this case, the options of the first point instance are copied over to the
          group point. This can be altered through a custom
          :meth:`approximation <highcharts_stock.utility_classes.data_grouping.DataGroupingOptions.approximation>`
          function.
        """
        return self._data_grouping

    @data_grouping.setter
    @class_sensitive(DataGroupingOptions)
    def data_grouping(self, value):
        self._data_grouping = value

    @property
    def gap_size(self) -> Optional[int | float | Decimal]:
        """In combination with
        :meth:`.gap_unit <highcharts_stock.options.indicators.IndicatorOptions.gap_unit>`
        defines when to display a gap in the graph. Defaults to ``0``.

        .. note::

          If
          :meth:`.data_grouping <highcharts_stock.options.indicators.IndicatorOptions.data_grouping>`
          is enabled, points can be grouped into a larger time span. This can make the
          grouped points have a greater distance than the absolute value of the
          ``.gap_size`` property, which would result in data disappearing from view
          completely. To prevent this situation, the mentioned distance between grouped
          points is applied rather than the explicitly supplied ``.gap_size``.

        .. tip::

          In practice, this option is most often used to visualize gaps in time series. In
          a stock chart, intraday data is available for daytime hours, while gaps will
          appear in nights and weekends.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._gap_size

    @gap_size.setter
    def gap_size(self, value):
        self._gap_size = validators.numeric(value, allow_empty = True)

    @property
    def gap_unit(self) -> Optional[str]:
        """In combination with
        :meth:`.gap_size <highcharts_stock.options.indicators.IndicatorOptions.gap_size>`
        defines when to display a gap in the graph. Defaults to ``'relative'``.

        Accepts two possible values:

          * ``'relative'`` - determines the gap based on a multiple of
            :meth:`.gap_size <highcharts_stock.options.indicators.IndicatorOptions.gap_size>`.
            For example, with a
            :meth:`.gap_size <highcharts_stock.options.indicators.IndicatorOptions.gap_size>`
            of ``5``, if the distance between two points is greater than 5x the two
            closest points, a gap will be rendered.
          * ``'value'`` - determines the gap based on the absolute axis values, which
            on a datetime axis are expressed in milliseconds.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._gap_unit

    @gap_unit.setter
    def gap_unit(self, value):
        if not value:
            self._gap_unit = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['relative', 'value']:
                raise errors.HighchartsValueError(f'gap_unit expects either "relative", '
                                                  f'or "value". Received: "{value}"')
            self._gap_unit = value

    @property
    def last_price(self) -> Optional[LastPriceOptions]:
        """Configuration of a line marking the last price from all data points (whether
        visible or not). Defaults to :obj:`None <python:None>`.

          .. seealso::

            * :meth:`.last_price_visible <highcharts_stock.options.plot_options.indicators.IndicatorOptions.last_price_visible>`


        :rtype: :class:`LastPriceOptions <highcharts_stock.utility_classes.last_price.LastPriceOptions>`
          or :obj:`None <python:None>`
        """
        return self._last_price

    @last_price.setter
    @class_sensitive(LastPriceOptions)
    def last_price(self, value):
        self._last_price = value

    @property
    def last_price_visible(self) -> Optional[LastPriceOptions]:
        """Configuration of a line marking the last price from all visible data points.
        Defaults to :obj:`None <python:None>`.

          .. seealso::

            * :meth:`.last_price <highcharts_stock.options.plot_options.indicators.IndicatorOptions.last_price>`

        :rtype: :class:`LastPriceOptions <highcharts_stock.utility_classes.last_price_visible.LastPriceOptions>`
          or :obj:`None <python:None>`
        """
        return self._last_price_visible

    @last_price_visible.setter
    @class_sensitive(LastPriceOptions)
    def last_price_visible(self, value):
        self._last_price_visible = value

    @property
    def name(self) -> Optional[str]:
        """The name of the series as shown in the legend, tooltip, etc. Defaults to
        :obj:`None <python:None>`.

        .. note::

          If :obj:`None <python:None>`, it will be set automatically based on the
          technical indicator type and default
          :meth:`.params <highcharts_stock.options.plot_options.indicators.IndicatorOptions.params>`.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._name

    @name.setter
    def name(self, value):
        self._name = validators.string(value, allow_empty = True)

    @property
    def params(self) -> Optional[ParameterBase]:
        """Parameters used in calculating the indicator's data points.

        :rtype: :class:`ParameterBase` or :obj:`None <python:None>`
        """
        return self._params

    @params.setter
    @class_sensitive(ParameterBase)
    def params(self, value):
        self._params = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'accessibility': as_dict.get('accessibility', None),
            'allow_point_select': as_dict.get('allowPointSelect', None),
            'animation': as_dict.get('animation', None),
            'class_name': as_dict.get('className', None),
            'clip': as_dict.get('clip', None),
            'color': as_dict.get('color', None),
            'cursor': as_dict.get('cursor', None),
            'custom': as_dict.get('custom', None),
            'dash_style': as_dict.get('dashStyle', None),
            'data_labels': as_dict.get('dataLabels', None),
            'description': as_dict.get('description', None),
            'enable_mouse_tracking': as_dict.get('enableMouseTracking', None),
            'events': as_dict.get('events', None),
            'include_in_data_export': as_dict.get('includeInDataExport', None),
            'keys': as_dict.get('keys', None),
            'label': as_dict.get('label', None),
            'linked_to': as_dict.get('linkedTo', None),
            'marker': as_dict.get('marker', None),
            'on_point': as_dict.get('onPoint', None),
            'opacity': as_dict.get('opacity', None),
            'point': as_dict.get('point', None),
            'point_description_formatter': as_dict.get('pointDescriptionFormatter', None),
            'selected': as_dict.get('selected', None),
            'show_checkbox': as_dict.get('showCheckbox', None),
            'show_in_legend': as_dict.get('showInLegend', None),
            'skip_keyboard_navigation': as_dict.get('skipKeyboardNavigation', None),
            'states': as_dict.get('states', None),
            'sticky_tracking': as_dict.get('stickyTracking', None),
            'threshold': as_dict.get('threshold', None),
            'tooltip': as_dict.get('tooltip', None),
            'turbo_threshold': as_dict.get('turboThreshold', None),
            'visible': as_dict.get('visible', None),

            'animation_limit': as_dict.get('animationLimit', None),
            'boost_blending': as_dict.get('boostBlending', None),
            'boost_threshold': as_dict.get('boostThreshold', None),
            'color_index': as_dict.get('colorIndex', None),
            'color_key': as_dict.get('colorKey', None),
            'connect_nulls': as_dict.get('connectNulls', None),
            'crisp': as_dict.get('crisp', None),
            'crop_threshold': as_dict.get('cropThreshold', None),
            'data_sorting': as_dict.get('dataSorting', None),
            'find_nearest_point_by': as_dict.get('findNearestPointBy', None),
            'get_extremes_from_all': as_dict.get('getExtremesFromAll', None),
            'linecap': as_dict.get('linecap', None),
            'line_width': as_dict.get('lineWidth', None),
            'relative_x_value': as_dict.get('relativeXValue', None),
            'shadow': as_dict.get('shadow', None),
            'soft_threshold': as_dict.get('softThreshold', None),
            'step': as_dict.get('step', None),
            'zone_axis': as_dict.get('zoneAxis', None),
            'zones': as_dict.get('zones', None),

            'color_axis': as_dict.get('colorAxis', None),
            'connect_ends': as_dict.get('connectEnds', None),
            'drag_drop': as_dict.get('dragDrop', None),
            'negative_color': as_dict.get('negativeColor', None),
            'point_interval': as_dict.get('pointInterval', None),
            'point_interval_unit': as_dict.get('pointIntervalUnit', None),
            'point_placement': as_dict.get('pointPlacement', None),
            'point_start': as_dict.get('pointStart', None),
            'stacking': as_dict.get('stacking', None),

            'compare_start': as_dict.get('compareStart', None),
            'compare_to_main': as_dict.get('compareToMain', None),
            'cumulative': as_dict.get('cumulative', None),
            'data_as_columns': as_dict.get('dataAsColumns', None),
            'data_grouping': as_dict.get('dataGrouping', None),
            'gap_size': as_dict.get('gapSize', None),
            'gap_unit': as_dict.get('gapUnit', None),
            'last_price': as_dict.get('lastPrice', None),
            'last_visible_price': as_dict.get('lastVisiblePrice', None),
            'name': as_dict.get('name', None),
            'params': as_dict.get('params', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'compareStart': self.compare_start,
            'compareToMain': self.compare_to_main,
            'cumulative': self.cumulative,
            'dataAsColumns': self.data_as_columns,
            'dataGrouping': self.data_grouping,
            'gapSize': self.gap_size,
            'gapUnit': self.gap_unit,
            'lastPrice': self.last_price,
            'lastVisiblePrice': self.last_visible_price,
            'name': self.name,
            'params': self.params,
        }

        parent_as_dict = super()._to_untrimmed_dict(in_cls = in_cls)

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed

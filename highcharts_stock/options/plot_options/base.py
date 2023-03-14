from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts_core import constants
from highcharts_core.decorators import class_sensitive
from highcharts_core.metaclasses import HighchartsMeta

from highcharts_stock import errors
from highcharts_stock.options.navigator import Navigator
from highcharts_stock.utility_classes.data_grouping import DataGroupingOptions
from highcharts_stock.utility_classes.last_price import LastPriceOptions


class StockBaseOptions(HighchartsMeta):
    """Base class for Stock Plot Options."""

    def __init__(self, **kwargs):
        self._compare_start = None
        self._cumulative = None
        self._data_as_columns = None
        self._data_grouping = None
        self._gap_size = None
        self._gap_unit = None
        self._last_price = None
        self._last_visible_price = None

        try:
            self.compare_start = kwargs.get('compare_start', None)
        except AttributeError:
            pass

        self.cumulative = kwargs.get('cumulative', None)
        self.data_as_columns = kwargs.get('data_as_columns', None)
        self.data_grouping = kwargs.get('data_grouping', None)
        self.gap_size = kwargs.get('gap_size', None)
        self.gap_unit = kwargs.get('gap_unit', None)
        self.last_price = kwargs.get('last_price', None)
        self.last_visible_price = kwargs.get('last_visible_price', None)

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

            * :meth:`.last_visible_price <highcharts_stock.options.plot_options.indicators.IndicatorOptions.last_visible_price>`


        :rtype: :class:`LastPriceOptions <highcharts_stock.utility_classes.last_price.LastPriceOptions>`
          or :obj:`None <python:None>`
        """
        return self._last_price

    @last_price.setter
    @class_sensitive(LastPriceOptions)
    def last_price(self, value):
        self._last_price = value

    @property
    def last_visible_price(self) -> Optional[LastPriceOptions]:
        """Configuration of a line marking the last price from all visible data points.
        Defaults to :obj:`None <python:None>`.

          .. seealso::

            * :meth:`.last_price <highcharts_stock.options.plot_options.indicators.IndicatorOptions.last_price>`

        :rtype: :class:`LastPriceOptions <highcharts_stock.utility_classes.last_visible_price.LastPriceOptions>`
          or :obj:`None <python:None>`
        """
        return self._last_visible_price

    @last_visible_price.setter
    @class_sensitive(LastPriceOptions)
    def last_visible_price(self, value):
        self._last_visible_price = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'compare_start': as_dict.get('compareStart', None),
            'cumulative': as_dict.get('cumulative', None),
            'data_as_columns': as_dict.get('dataAsColumns', None),
            'data_grouping': as_dict.get('dataGrouping', None),
            'gap_size': as_dict.get('gapSize', None),
            'gap_unit': as_dict.get('gapUnit', None),
            'last_price': as_dict.get('lastPrice', None),
            'last_visible_price': as_dict.get('lastVisiblePrice', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        try:
            compare_start = self.compare_start
        except AttributeError:
            compare_start = None

        untrimmed = {
            'compareStart': compare_start,
            'cumulative': self.cumulative,
            'dataAsColumns': self.data_as_columns,
            'dataGrouping': self.data_grouping,
            'gapSize': self.gap_size,
            'gapUnit': self.gap_unit,
            'lastPrice': self.last_price,
            'lastVisiblePrice': self.last_visible_price,
        }

        return untrimmed


class NonIndicatorOptions(StockBaseOptions):
    """Base class for Stock Plot Options, with navigator options."""

    def __init__(self, **kwargs):
        self._compare = None
        self._compare_base = None
        self._navigator_options = None
        self._point_range = None
        self._show_in_navigator = None

        self.compare = kwargs.get('compare', None)
        self.compare_base = kwargs.get('compare_base', None)
        self.navigator_options = kwargs.get('navigator_options', None)
        self.poing_range = kwargs.get('point_range', None)
        self.show_in_navigator = kwargs.get('show_in_navigator', None)

        super().__init__(**kwargs)

    @property
    def compare(self) -> Optional[str]:
        """Determines whether to display the ``'percent'`` or the ``'value'`` of the
        indicator's comparison against the main series. Defaults to
        :obj:`None <python:None>`, which does not calculate the comparison.

        Accepts:

          * ``'percent'`` - returns the percentage calculation for the indicator
          * ``'value'`` - returns the axis value calculation for the indicator

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._compare

    @compare.setter
    def compare(self, value):
        if not value:
            self._compare = None
        else:
            value = validators.string(value, allow_empty = True)
            value = value.lower()
            if value not in ['percent', 'value']:
                raise errors.HighchartsValueError(f'compare expects either "percent", or '
                                                  f'"value". Received: "{value}"')

            self._compare = value

    @property
    def compare_base(self) -> Optional[int]:
        """When
        :meth:`.compare <highcharts_stock.options.plot_options.indicators.ComparableIndicatorOptions.compare>`
        is set to ``'percent'``, this option determines whether to use ``0`` or ``100`` as
        the basis of comparison. Defaults to ``0``.

        Accepts:

          * ``0``
          * ``100``

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._compare_base

    @compare_base.setter
    def compare_base(self, value):
        if value is None:
            self._compare_base = None
        else:
            value = validators.integer(value)
            if value not in [0, 100]:
                raise errors.HighchartsValueError(f'compare_base expects either 0 or 100.'
                                                  f'Received: {value}.')

            self._compare_base = value

    @property
    def navigator_options(self) -> Optional[Navigator]:
        """Options for the corresponding :term:`navigator` series if
        :meth:`.show_in_navigator <highcharts_stock.options.plot_options.base.StockBaseWithNavigatorOptions.show_in_navigator>`
        is ``True`` for this series. Defaults to :obj:`None <python:None>`

        .. note::

          These options are merged with options in ``navigator.series``, and will take
          precedence if the same option is defined both places.

        :rtype: :class:`NavigatorOptions <highcharts_stock.navigator.Navigator>` or
          :obj:`None <python:None>`
        """
        return self._navigator_options

    @navigator_options.setter
    @class_sensitive(Navigator)
    def navigator_options(self, value):
        self._navigator_options = value

    @property
    def point_range(self) -> Optional[constants.EnforcedNullType | int | float | Decimal]:
        """The X axis range that each point is valid for, which determines the width of
        the column. Defaults to ``EnforcedNull``, which computes the range automatically.

        On a categorized axis, the range will be ``1`` by default (one category unit). On
        linear and datetime axes, the range will be computed as the distance between the
        two closest data points.

        The default ``EnforcedNull`` means it is computed automatically, but the setting
        can be used to override the default value.

        .. note::

          If :meth:`data_sorting <AreaOptions.data_sorting>` is enabled, the default value
          is implicitly adjusted to ``1``.

        :rtype: numeric or :class:`EnforcedNullType` or :obj:`None <python:None>`
        """
        return self._point_range

    @point_range.setter
    def point_range(self, value):
        if isinstance(value, constants.EnforcedNullType):
            self._point_range = constants.EnforcedNull
        else:
            self._point_range = validators.numeric(value, allow_empty = True)

    @property
    def show_in_navigator(self) -> Optional[bool]:
        """If ``True``, shows the series in the :term:`navigator`. Defaults to
        :obj:`None <python:None>`.

        .. note::

          Takes precedence over
          :meth:`Navigator.base_series <highcharts_stock.navigator.Navigator.base_series>`
          if provided.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._show_in_navigator

    @show_in_navigator.setter
    def show_in_navigator(self, value):
        if value is None:
            self._show_in_navigator = None
        else:
            self._show_in_navigator = bool(value)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'compare_start': as_dict.get('compareStart', None),
            'cumulative': as_dict.get('cumulative', None),
            'data_as_columns': as_dict.get('dataAsColumns', None),
            'data_grouping': as_dict.get('dataGrouping', None),
            'gap_size': as_dict.get('gapSize', None),
            'gap_unit': as_dict.get('gapUnit', None),
            'last_price': as_dict.get('lastPrice', None),
            'last_visible_price': as_dict.get('lastVisiblePrice', None),

            'compare': as_dict.get('compare', None),
            'compare_base': as_dict.get('compareBase', None),
            'navigator_options': as_dict.get('navigatorOptions', None),
            'point_range': as_dict.get('pointRange', None),
            'show_in_navigator': as_dict.get('showInNavigator', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'compare': self.compare,
            'compareBase': self.compare_base,
            'navigatorOptions': self.navigator_options,
            'pointRange': self.point_range,
            'showInNavigator': self.show_in_navigator,
        }

        return untrimmed


class NavigatorIndicatorOptions(HighchartsMeta):
    """Set of options to mix in when an indicator supports a presence in the Navigator."""

    def __init__(self, **kwargs):
        self._navigator_options = None
        self._show_in_navigator = None

        self.navigator_options = kwargs.get('navigator_options', None)
        self.show_in_navigator = kwargs.get('show_in_navigator', None)

        super().__init__(**kwargs)

    @property
    def navigator_options(self) -> Optional[Navigator]:
        """Options for the corresponding :term:`navigator` series if
        :meth:`.show_in_navigator <highcharts_stock.options.plot_options.base.StockBaseWithNavigatorOptions.show_in_navigator>`
        is ``True`` for this series. Defaults to :obj:`None <python:None>`

        .. note::

          These options are merged with options in ``navigator.series``, and will take
          precedence if the same option is defined both places.

        :rtype: :class:`NavigatorOptions <highcharts_stock.navigator.Navigator>` or
          :obj:`None <python:None>`
        """
        return self._navigator_options

    @navigator_options.setter
    @class_sensitive(Navigator)
    def navigator_options(self, value):
        self._navigator_options = value

    @property
    def show_in_navigator(self) -> Optional[bool]:
        """If ``True``, shows the series in the :term:`navigator`. Defaults to
        :obj:`None <python:None>`.

        .. note::

          Takes precedence over
          :meth:`Navigator.base_series <highcharts_stock.navigator.Navigator.base_series>`
          if provided.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._show_in_navigator

    @show_in_navigator.setter
    def show_in_navigator(self, value):
        if value is None:
            self._show_in_navigator = None
        else:
            self._show_in_navigator = bool(value)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'navigator_options': as_dict.get('navigatorOptions', None),
            'show_in_navigator': as_dict.get('showInNavigator', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'navigatorOptions': self.navigator_options,
            'showInNavigator': self.show_in_navigator,
        }

        return untrimmed

from typing import Optional

from validator_collection import validators

from highcharts_core.decorators import class_sensitive
from highcharts_core.metaclasses import HighchartsMeta
from highcharts_core.options.plot_options.series import SeriesOptions

from highcharts_stock import errors
from highcharts_stock.options.plot_options.base import StockBaseOptions
from highcharts_stock.utility_functions import mro__to_untrimmed_dict


class ParameterBase(HighchartsMeta):
    """Base class for parameters used to calculate technical indicators."""

    def __init__(self, **kwargs):
        self._index = None
        self._period = None

        try:
            self.index = kwargs.get('index', None)
        except AttributeError:
            pass
        try:
            self.period = kwargs.get('period', None)
        except AttributeError:
            pass

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


class IndicatorOptions(SeriesOptions, StockBaseOptions):
    """Options for series that can be used as
    :term:`technical indicators <technical indicator>` in **Highcharts Stock for Python**.
    """

    def __init__(self, **kwargs):
        self._compare_start = None
        self._compare_to_main = None
        self._name = None
        self._params = None

        try:
            self.compare_start = kwargs.get('compare_start', None)
        except AttributeError:
            pass

        self.compare_to_main = kwargs.get('compare_to_main', None)
        self.name = kwargs.get('name', None)
        self.params = kwargs.get('params', None)

        super().__init__(**kwargs)

    @property
    def _dot_path(self) -> Optional[str]:
        """The dot-notation path to the options key for the current class.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return f'plotOptions.{self.type}'
    
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
            'legend_symbol': as_dict.get('legendSymbol', None),
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
            'sonification': as_dict.get('sonification', None),
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
            'inactive_other_points': as_dict.get('inactiveOtherPoints', None),
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
            'point_description_format': as_dict.get('pointDescriptionFormat', None),
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
        try:
            compare_start = self.compare_start
        except AttributeError:
            compare_start = None

        untrimmed = {
            'compareStart': compare_start,
            'compareToMain': self.compare_to_main,
            'name': self.name,
            'params': self.params,
        }

        parent_as_dict = mro__to_untrimmed_dict(self, in_cls = in_cls)

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed


class ComparableIndicatorOptions(IndicatorOptions):
    """Options for :term:`series` that can be used as
    :term:`technical indicators <techincal indicator>` in **Highcharts for Python**, but
    which provide for more extensive comparisons against the main series.
    """

    def __init__(self, **kwargs):
        self._compare = None
        self._compare_base = None

        self.compare = kwargs.get('compare', None)
        self.compare_base = kwargs.get('compare_base', None)

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
            'legend_symbol': as_dict.get('legendSymbol', None),
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
            'sonification': as_dict.get('sonification', None),
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
            'inactive_other_points': as_dict.get('inactiveOtherPoints', None),
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
            'point_description_format': as_dict.get('pointDescriptionFormat', None),
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

            'compare': as_dict.get('compare', None),
            'compare_base': as_dict.get('compareBase', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'compare': self.compare,
            'compareBase': self.compare_base
        }

        parent_as_dict = mro__to_untrimmed_dict(self, in_cls = in_cls)

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed

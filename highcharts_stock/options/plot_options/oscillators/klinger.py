from typing import Optional

from validator_collection import validators

from highcharts_core.decorators import class_sensitive
from highcharts_core.metaclasses import HighchartsMeta

from highcharts_stock.options.plot_options.indicators import ComparableIndicatorOptions
from highcharts_stock.utility_classes.line_styles import LineStylesColorWidth
from highcharts_stock.options.plot_options.momentum import OBVParameters


class KlingerParameters(OBVParameters):

    def __init__(self, **kwargs):
        self._fast_avg_period = None
        self._signal_period = None
        self._slow_avg_period = None

        self.fast_avg_period = kwargs.get('fast_avg_period', None)
        self.signal_period = kwargs.get('signal_period', None)
        self.slow_avg_period = kwargs.get('slow_avg_period', None)

        super().__init__(**kwargs)

    @property
    def fast_avg_period(self) -> Optional[int]:
        """The fast period for indicator calculations. Defaults to ``34``.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._fast_avg_period

    @fast_avg_period.setter
    def fast_avg_period(self, value):
        self._fast_avg_period = validators.integer(value,
                                                   allow_empty = True,
                                                   minimum = 0)

    @property
    def signal_period(self) -> Optional[int]:
        """The signal period for indicator calculations. Defaults to ``9``.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._signal_period

    @signal_period.setter
    def signal_period(self, value):
        self._signal_period = validators.integer(value,
                                                 allow_empty = True,
                                                 minimum = 0)

    @property
    def slow_avg_period(self) -> Optional[int]:
        """The slow period for indicator calculations. Defaults to ``55``.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._slow_avg_period

    @slow_avg_period.setter
    def slow_avg_period(self, value):
        self._slow_avg_period = validators.integer(value,
                                                   allow_empty = True,
                                                   minimum = 0)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'volume_series_id': as_dict.get('volumeSeriesID', None),
            'fast_avg_period': as_dict.get('fastAvgPeriod', None),
            'signal_period': as_dict.get('signalPeriod', None),
            'slow_avg_period': as_dict.get('slowAvgPeriod', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'fastAvgPeriod': self.fast_avg_period,
            'signalPeriod': self.signal_period,
            'slowAvgPeriod': self.slow_avg_period,
            'volumeSeriesID': self.volume_series_id,
        }

        return untrimmed


class KlingerLineOptions(HighchartsMeta):
    """Options for styling Klinger lines."""

    def __init__(self, **kwargs):
        self._styles = None
        self._zones = None

        self.styles = kwargs.get('styles', None)
        self.zones = kwargs.get('zones', None)

    @property
    def styles(self) -> Optional[LineStylesColorWidth]:
        """Styles to apply to the line itself.

        :rtype: :class:`LineStylesColorWidth <highcharts_stock.utility_classes.line_styles.LineStylesColorWidth>`
          or :obj:`None <python:None>`
        """
        return self._styles

    @styles.setter
    @class_sensitive(LineStylesColorWidth)
    def styles(self, value):
        self._styles = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'styles': as_dict.get('styles', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'styles': self.styles,
        }

        return untrimmed


class KlingerOptions(ComparableIndicatorOptions):
    """Options to configure a Klinger :term:`Oscillator`, used to determine the long-term
    trend of money flow while remaining sensitive enough to detect short-term
    fluctuations.

    .. figure:: ../../../../_static/klinger-example.png
      :alt: Klinger Example Chart
      :align: center

    """

    def __init__(self, **kwargs):
        self._signal_line = None

        self.signal_line = kwargs.get('signal_line', None)

        super().__init__(**kwargs)

    @property
    def params(self) -> Optional[KlingerParameters]:
        """Parameters used in calculating the indicator's data points.

        :rtype: :class:`KlingerParameters` or :obj:`None <python:None>`
        """
        return self._params

    @params.setter
    @class_sensitive(KlingerParameters)
    def params(self, value):
        self._params = value

    @property
    def signal_line(self) -> Optional[KlingerLineOptions]:
        """Styles for configuring the Signal line.

        :rtype: :class:`KlingerLineOptions` or :obj:`None <python:None>`
        """
        return self._signal_line

    @signal_line.setter
    @class_sensitive(KlingerLineOptions)
    def signal_line(self, value):
        self._signal_line = value

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

            'signal_line': as_dict.get('signalLine', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'signalLine': self.signal_line,
        }

        parent_as_dict = super()._to_untrimmed_dict(in_cls = in_cls)

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed

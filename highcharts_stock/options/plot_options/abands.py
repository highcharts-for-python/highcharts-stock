from typing import Optional

from highcharts_core.decorators import class_sensitive
from highcharts_core.metaclasses import HighchartsMeta
from highcharts_core.utility_functions import validate_color
from highcharts_core.utility_classes.gradients import Gradient
from highcharts_core.utility_classes.patterns import Pattern

from highcharts_stock.options.plot_options.indicators import IndicatorOptions, ComparableIndicatorOptions
from highcharts_stock.options.plot_options.oscillators import WilliamsRParameters as PCParameters
from highcharts_stock.utility_classes.line_styles import LineStylesWidth
from highcharts_stock.utility_functions import mro__to_untrimmed_dict


class AbandsStyleOptions(HighchartsMeta):
    """Styles for the Aroon-Down line."""

    def __init__(self, **kwargs):
        self._styles = None

        self.styles = kwargs.get('styles', None)

    @property
    def styles(self) -> Optional[LineStylesWidth]:
        """Styles for the bottom line.

        :rtype: :class:`LineStylesWidth` or :obj:`None <python:None>`
        """
        return self._styles

    @styles.setter
    @class_sensitive(LineStylesWidth)
    def styles(self, value):
        self._styles = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'styles': as_dict.get('styles', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'styles': self.styles
        }

        return untrimmed


class AbandsOptions(IndicatorOptions):
    """Configuration for :term:`Acceleration Bands`, a :term:`technical indicator` which
    plots a trio of lines using a simple moving average for the midpoint, and the high and
    low values as the corresponding high and low bands.

    .. figure:: ../../../_static/abands-example.png
      :alt: Acceleration Bands Example Chart
      :align: center

    """

    def __init__(self, **kwargs):
        self._bottom_line = None
        self._fill_color = None
        self._top_line = None

        self.bottom_line = kwargs.get('bottom_line', None)
        self.fill_color = kwargs.get('fill_color', None)
        self.top_line = kwargs.get('top_line', None)

        super().__init__(**kwargs)

    @property
    def _dot_path(self) -> Optional[str]:
        """The dot-notation path to the options key for the current class.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return 'plotOptions.abands'

    @property
    def bottom_line(self) -> Optional[AbandsStyleOptions]:
        """Styles for the bottom line.

        :rtype: :class:`AbandsStyleOptions` or :obj:`None <python:None>`
        """
        return self._bottom_line

    @bottom_line.setter
    @class_sensitive(AbandsStyleOptions)
    def bottom_line(self, value):
        self._bottom_line = value

    @property
    def fill_color(self) -> Optional[str | Gradient | Pattern]:
        """Fill color or gradient for the bands.

        :rtype: :obj:`None <python:None>`, :class:`Gradient`, :class:`Pattern`, or
          :class:`EnforcedNullType`
        """
        return self._fill_color

    @fill_color.setter
    def fill_color(self, value):
        self._fill_color = validate_color(value)

    @property
    def top_line(self) -> Optional[AbandsStyleOptions]:
        """Styles for the top line.

        :rtype: :class:`AbandsStyleOptions` or :obj:`None <python:None>`
        """
        return self._top_line

    @top_line.setter
    @class_sensitive(AbandsStyleOptions)
    def top_line(self, value):
        self._top_line = value

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

            'bottom_line': as_dict.get('bottomLine', None),
            'fill_color': as_dict.get('fillColor', None),
            'top_line': as_dict.get('topLine', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'bottomLine': self.bottom_line,
            'fillColor': self.fill_color,
            'topLine': self.top_line,
        }

        parent_as_dict = mro__to_untrimmed_dict(self, in_cls = in_cls)

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed


class PCOptions(AbandsOptions):
    """Configuration for a Price Channel :term:`indicator <technical indicator>`.

    .. figure:: ../../../_static/price-channel-example.png
      :alt: Price Channel Example Chart
      :align: center

    """
    @property
    def _dot_path(self) -> Optional[str]:
        """The dot-notation path to the options key for the current class.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return 'plotOptions.pc'

    @property
    def params(self) -> Optional[PCParameters]:
        """Parameters used in calculating the indicator's data points.

        :rtype: :class:`PCParameters` or :obj:`None <python:None>`
        """
        return self._params

    @params.setter
    @class_sensitive(PCParameters)
    def params(self, value):
        self._params = value


class KeltnerChannelsOptions(AbandsOptions):
    """Configuration for a Keltner Channels :term:`indicator <technical indicator>`.

    .. figure:: ../../../_static/keltner-channels-example.png
      :alt: Keltner Channels Example Chart
      :align: center

    """


class BBOptions(ComparableIndicatorOptions):
    """Configuration for Bollinger Bands, a :term:`technical indicator`.

    .. figure:: ../../../_static/bollinger-bands-example.png
      :alt: Bollinger Bands Example Chart
      :align: center

    """

    def __init__(self, **kwargs):
        self._bottom_line = None
        self._fill_color = None
        self._top_line = None

        self.bottom_line = kwargs.get('bottom_line', None)
        self.fill_color = kwargs.get('fill_color', None)
        self.top_line = kwargs.get('top_line', None)

        super().__init__(**kwargs)

    @property
    def bottom_line(self) -> Optional[AbandsStyleOptions]:
        """Styles for the bottom line.

        :rtype: :class:`AbandsStyleOptions` or :obj:`None <python:None>`
        """
        return self._bottom_line

    @bottom_line.setter
    @class_sensitive(AbandsStyleOptions)
    def bottom_line(self, value):
        self._bottom_line = value

    @property
    def fill_color(self) -> Optional[str | Gradient | Pattern]:
        """Fill color or gradient for the bands.

        :rtype: :obj:`None <python:None>`, :class:`Gradient`, :class:`Pattern`, or
          :class:`EnforcedNullType`
        """
        return self._fill_color

    @fill_color.setter
    def fill_color(self, value):
        self._fill_color = validate_color(value)

    @property
    def top_line(self) -> Optional[AbandsStyleOptions]:
        """Styles for the top line.

        :rtype: :class:`AbandsStyleOptions` or :obj:`None <python:None>`
        """
        return self._top_line

    @top_line.setter
    @class_sensitive(AbandsStyleOptions)
    def top_line(self, value):
        self._top_line = value

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

            'bottom_line': as_dict.get('bottomLine', None),
            'fill_color': as_dict.get('fillColor', None),
            'top_line': as_dict.get('topLine', None),

            'compare': as_dict.get('compare', None),
            'compare_base': as_dict.get('compareBase', None),

        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'bottomLine': self.bottom_line,
            'fillColor': self.fill_color,
            'topLine': self.top_line,
        }

        parent_as_dict = super()._to_untrimmed_dict(in_cls = in_cls)

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed

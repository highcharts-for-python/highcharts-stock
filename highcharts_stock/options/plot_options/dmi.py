from typing import Optional

from highcharts_core.decorators import class_sensitive
from highcharts_core.metaclasses import HighchartsMeta

from highcharts_stock.options.plot_options.indicators import ParameterBase, ComparableIndicatorOptions
from highcharts_stock.options.plot_options.oscillators import WilliamsRParameters as DMIParameters
from highcharts_stock.utility_classes.line_styles import LineStylesColorWidth


class DMIStyleOptions(HighchartsMeta):
    """Styles for the Directional Movement Index lines."""

    def __init__(self, **kwargs):
        self._styles = None

        self.styles = kwargs.get('styles', None)

    @property
    def styles(self) -> Optional[LineStylesColorWidth]:
        """Styles for the bottom line.

        :rtype: :class:`LineStylesColorWidth` or :obj:`None <python:None>`
        """
        return self._styles

    @styles.setter
    @class_sensitive(LineStylesColorWidth)
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


class DMIOptions(ComparableIndicatorOptions):
    """Options to configure a Directional Movement Index (DMI)
    :term:`indicator <technical indicator>`, which can be used to identify whether an
    asset is trending by comparing highs and lows over time.

    .. figure:: ../../../_static/dmi-example.png
      :alt: Directional Movement Index (DMI) Example Chart
      :align: center

    """

    def __init__(self, **kwargs):
        self._minus_di_line = None
        self._plus_di_line = None

        self.minus_di_line = kwargs.get('minusDILine', None)
        self.plus_di_line = kwargs.get('plusDILine', None)

        super().__init__(**kwargs)

    @property
    def minus_di_line(self) -> Optional[DMIStyleOptions]:
        """Styles for the minus DI line.

        :rtype: :class:`DMIStyleOptions` or :obj:`None <python:None>`
        """
        return self._minus_di_line

    @minus_di_line.setter
    @class_sensitive(DMIStyleOptions)
    def minus_di_line(self, value):
        self._minus_di_line = value

    @property
    def plus_di_line(self) -> Optional[DMIStyleOptions]:
        """Styles for the plus DI line.

        :rtype: :class:`DMIStyleOptions` or :obj:`None <python:None>`
        """
        return self._plus_di_line

    @plus_di_line.setter
    @class_sensitive(DMIStyleOptions)
    def plus_di_line(self, value):
        self._plus_di_line = value

    @property
    def params(self) -> Optional[DMIParameters]:
        """Parameters used in calculating the indicator's data points.

        :rtype: :class:`DMIParameters` or :obj:`None <python:None>`
        """
        return self._params

    @params.setter
    @class_sensitive(DMIParameters)
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

            'compare': as_dict.get('compare', None),
            'compare_base': as_dict.get('compareBase', None),

            'minus_di_line': as_dict.get('minusDILine', None),
            'plus_di_line': as_dict.get('plusDILine', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'minusDILine': self.minus_di_line,
            'plusDILine': self.plus_di_line,
        }

        parent_as_dict = super()._to_untrimmed_dict(in_cls = in_cls)

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed

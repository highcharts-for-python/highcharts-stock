from typing import Optional

from validator_collection import validators

from highcharts_core.options.plot_options.bar import BaseBarOptions
from highcharts_core.utility_functions import mro__to_untrimmed_dict, validate_color
from highcharts_core.utility_classes.gradients import Gradient
from highcharts_core.utility_classes.patterns import Pattern

from highcharts_stock import errors
from highcharts_stock.options.plot_options.base import NonIndicatorOptions


class CandlestickOptions(BaseBarOptions, NonIndicatorOptions):
    """General options to apply to all Candlestick series types. A candlestick chart is a
    style of financial chart used to describe price movements over time.

    .. figure:: ../../../_static/candlestick-example.png
      :alt: Candlestick Example Chart
      :align: center

    """

    def __init__(self, **kwargs):
        self._point_val_key = None
        self._up_color = None
        self._up_line_color = None

        self.point_val_key = kwargs.get('point_val_key', None)
        self.up_color = kwargs.get('up_color', None)
        self.up_line_color = kwargs.get('up_line_color', None)

        super().__init__(**kwargs)

    @property
    def _dot_path(self) -> Optional[str]:
        """The dot-notation path to the options key for the current class.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return 'plotOptions.candlestick'

    @property
    def point_val_key(self) -> Optional[str]:
        """Indicates which value position should be represented as the y-axis value of the
        data point. Defaults to ``'close'``.

        Accepts:

          * ``'high'``
          * ``'low'``
          * ``'close'``

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._point_val_key

    @point_val_key.setter
    def point_val_key(self, value):
        if not value:
            self._point_val_key = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['high', 'low', 'close']:
                raise errors.HighchartsValueError(f'point_val_key expects either "high", '
                                                  f'"low", or "close". Received: '
                                                  f'"{value}"')
            self._point_val_key = value

    @property
    def up_color(self) -> Optional[str | Gradient | Pattern]:
        """The fill color of the candlestick when values are rising. Defaults to
        ``'#ffffff'``.

        :rtype: :obj:`None <python:None>`, :class:`Gradient`, :class:`Pattern`, or
          :class:`str <python:str>`
        """
        return self._up_color

    @up_color.setter
    def up_color(self, value):
        self._up_color = validate_color(value)

    @property
    def up_line_color(self) -> Optional[str | Gradient | Pattern]:
        """The specific line color for up candle sticks. If :obj:`None <python:None>`,
        inherits the general
        :meth:`.line_color <highcharts_stock.options.plot_options.candlestick.CandlestickOptions.line_color>`
        setting. Defaults to :obj:`None <python:None>`.

        :rtype: :obj:`None <python:None>`, :class:`Gradient`, :class:`Pattern`, or
          :class:`str <python:str>`
        """
        return self._up_line_color

    @up_line_color.setter
    def up_line_color(self, value):
        self._up_line_color = validate_color(value)

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
            'color_axis': as_dict.get('colorAxis', None),
            'color_index': as_dict.get('colorIndex', None),
            'color_key': as_dict.get('colorKey', None),
            'connect_ends': as_dict.get('connectEnds', None),
            'connect_nulls': as_dict.get('connectNulls', None),
            'crisp': as_dict.get('crisp', None),
            'crop_threshold': as_dict.get('cropThreshold', None),
            'data_sorting': as_dict.get('dataSorting', None),
            'drag_drop': as_dict.get('dragDrop', None),
            'find_nearest_point_by': as_dict.get('findNearestPointBy', None),
            'get_extremes_from_all': as_dict.get('getExtremesFromAll', None),
            'inactive_other_points': as_dict.get('inactiveOtherPoints', None),
            'linecap': as_dict.get('linecap', None),
            'line_width': as_dict.get('lineWidth', None),
            'negative_color': as_dict.get('negativeColor', None),
            'point_description_format': as_dict.get('pointDescriptionFormat', None),
            'point_interval': as_dict.get('pointInterval', None),
            'point_interval_unit': as_dict.get('pointIntervalUnit', None),
            'point_placement': as_dict.get('pointPlacement', None),
            'point_start': as_dict.get('pointStart', None),
            'relative_x_value': as_dict.get('relativeXValue', None),
            'shadow': as_dict.get('shadow', None),
            'soft_threshold': as_dict.get('softThreshold', None),
            'stacking': as_dict.get('stacking', None),
            'step': as_dict.get('step', None),
            'zone_axis': as_dict.get('zoneAxis', None),
            'zones': as_dict.get('zones', None),

            # Commenting out properties that are ignored in Candlestick charts but which
            # are inherited.
            # 'border_color': as_dict.get('borderColor', None),
            # 'border_radius': as_dict.get('borderRadius', None),
            # 'border_width': as_dict.get('borderWidth', None),
            'center_in_category': as_dict.get('centerInCategory', None),
            'color_by_point': as_dict.get('colorByPoint', None),
            'colors': as_dict.get('colors', None),
            'grouping': as_dict.get('grouping', None),
            'group_padding': as_dict.get('groupPadding', None),
            'max_point_width': as_dict.get('maxPointWidth', None),
            'min_point_length': as_dict.get('minPointLength', None),
            'point_padding': as_dict.get('pointPadding', None),
            'point_range': as_dict.get('pointRange', None),
            'point_width': as_dict.get('pointWidth', None),

            'compare_start': as_dict.get('compareStart', None),
            'cumulative': as_dict.get('cumulative', None),
            'data_as_columns': as_dict.get('dataAsColumns', None),
            'data_grouping': as_dict.get('dataGrouping', None),
            # 'gap_size': as_dict.get('gapSize', None),
            # 'gap_unit': as_dict.get('gapUnit', None),
            'last_price': as_dict.get('lastPrice', None),
            'last_visible_price': as_dict.get('lastVisiblePrice', None),

            'compare': as_dict.get('compare', None),
            'compare_base': as_dict.get('compareBase', None),
            'navigator_options': as_dict.get('navigatorOptions', None),
            'show_in_navigator': as_dict.get('showInNavigator', None),

            'point_val_key': as_dict.get('pointValKey', None),
            'up_color': as_dict.get('upColor', None),
            'up_line_color': as_dict.get('upLineColor', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'pointValKey': self.point_val_key,
            'upColor': self.up_color,
            'upLineColor': self.up_line_color,
        }
        parent_as_dict = mro__to_untrimmed_dict(self, in_cls = in_cls) or {}

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed


class HollowCandlestickOptions(CandlestickOptions):
    """General options to apply to Hollow Candlestick series types. A candlestick chart is
    a style of financial chart used to describe price movements over time.

    .. figure:: ../../../_static/hollow-candlestick-example.png
      :alt: Hollow Candlestick Example Chart
      :align: center

    """
    @property
    def _dot_path(self) -> Optional[str]:
        """The dot-notation path to the options key for the current class.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return 'plotOptions.hollowcandlestick'


class HeikinAshiOptions(CandlestickOptions):
    """General options to apply to Heikin Ashi series types, which are visualized
    similarly to :class:`CandlestickSeries <options.series.candlestick.CandlestickSeries>`
    but which feature a smoother line by tracking ranges of movement rather than
    individual movements.

    .. figure:: ../../../_static/heikin-ashi-example.png
      :alt: Heikin Ashi Example Chart
      :align: center

    """
    @property
    def _dot_path(self) -> Optional[str]:
        """The dot-notation path to the options key for the current class.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return 'plotOptions.heikinashi'

from typing import Optional

from validator_collection import validators

from highcharts_core.decorators import class_sensitive
from highcharts_core.metaclasses import HighchartsMeta
from highcharts_core.utility_classes.gradients import Gradient
from highcharts_core.utility_classes.patterns import Pattern
from highcharts_core.utility_functions import validate_color

from highcharts_stock.options.plot_options.indicators import IndicatorOptions
from highcharts_stock.options.plot_options.oscillators import WilliamsRParameters
from highcharts_stock.utility_classes.line_styles import LineStylesColorWidth


class IKHParameters(WilliamsRParameters):

    def __init__(self, **kwargs):
        self._period_senkou_span_b = None
        self._period_tenkan = None

        self.period_senkou_span_b = kwargs.get('period_senkou_span_b', None)
        self.period_tenkan = kwargs.get('period_tenkan', None)

        super().__init__(**kwargs)

    @property
    def period_senkou_span_b(self) -> Optional[int]:
        """The base period for Senkou Span B calculations. Defaults to ``52``.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._period_senkou_span_b

    @period_senkou_span_b.setter
    def period_senkou_span_b(self, value):
        self._period_senkou_span_b = validators.integer(value,
                                               allow_empty = True,
                                               minimum = 0)

    @property
    def period_tenkan(self) -> Optional[int]:
        """The base period for Tenkan calculations. Defaults to ``9``.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._period_tenkan

    @period_tenkan.setter
    def period_tenkan(self, value):
        self._period_tenkan = validators.integer(value,
                                                allow_empty = True,
                                                minimum = 0)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'period': as_dict.get('period', None),

            'period_senkou_span_b': as_dict.get('periodSenkouSpanB', None),
            'period_tenkan': as_dict.get('periodTenkan', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'period': self.period,
            'periodSenkouSpanB': self.period_senkou_span_b,
            'periodTenkan': self.period_tenkan,
        }

        return untrimmed


class IKHLineOptions(HighchartsMeta):
    """Options for styling IKH lines."""

    def __init__(self, **kwargs):
        self._styles = None

        self.styles = kwargs.get('styles', None)

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


class SenkouSpanOptions(HighchartsMeta):
    """Configuration options for a senkou span."""

    def __init__(self, **kwargs):
        self._color = None
        self._negative_color = None

        self.color = kwargs.get('color', None)
        self.negative_color = kwargs.get('negative_color', None)

    @property
    def color(self) -> Optional[str | Gradient | Pattern]:
        """Color of the area between Senkou Span A and B, when Senkou Span A is above
        Senkou Span B. Defaults to :obj:`None <python:None>`.

        .. note::

          If a ``style.fill`` is defined, the ``color`` takes precedence and the
          ``style.fill`` is ignored.

        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern``, or
          :obj:`None <python:None>`

        """
        return self._color

    @color.setter
    def color(self, value):
        self._color = validate_color(value)

    @property
    def negative_color(self) -> Optional[str | Gradient | Pattern]:
        """Color of the area between Senkou Span A and B, when Senkou Span A is below
        Senkou Span B. Defaults to :obj:`None <python:None>`.

        .. note::

          If a ``style.fill`` is defined, the ``negative_color`` takes precedence and the
          ``style.fill`` is ignored.

        :rtype: :class:`str <python:str>`, :class:`Gradient`, :class:`Pattern``, or
          :obj:`None <python:None>`

        """
        return self._negative_color

    @negative_color.setter
    def negative_color(self, value):
        self._negative_color = validate_color(value)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'color': as_dict.get('color', None),
            'negative_color': as_dict.get('negativeColor', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'color': self.color,
            'negativeColor': self.negative_color,
        }

        return untrimmed


class IKHOptions(IndicatorOptions):
    """Options to configure a Ichimoku Kinko Hyo (IKH, or "ichimoku"), a momentum
    :term:`indicator <techincal indicator>`.

    .. figure:: ../../../../_static/ikh-example.png
      :alt: Ichimoku Kinko Hyo (IKH) Example Chart
      :align: center

    """

    def __init__(self, **kwargs):
        self._chikou_line = None
        self._kijun_line = None
        self._senkou_span = None
        self._senkou_span_a = None
        self._senkou_span_b = None
        self._tenkan_line = None

        self.chikou_line = kwargs.get('chikou_line', None)
        self.kijun_line = kwargs.get('kijun_line', None)
        self.senkou_span = kwargs.get('senkou_span', None)
        self.senkou_span_a = kwargs.get('senkou_span_a', None)
        self.senkou_span_b = kwargs.get('senkou_span_b', None)
        self.tenkan_line = kwargs.get('tenkan_line', None)

        super().__init__(**kwargs)

    @property
    def chikou_line(self) -> Optional[IKHLineOptions]:
        """Styles for configuring the IKH Chikou Line.

        :rtype: :class:`IKHLineOptions` or :obj:`None <python:None>`
        """
        return self._chikou_line

    @chikou_line.setter
    @class_sensitive(IKHLineOptions)
    def chikou_line(self, value):
        self._chikou_line = value

    @property
    def kijun_line(self) -> Optional[IKHLineOptions]:
        """Styles for configuring the IKH kijun Line.

        :rtype: :class:`IKHLineOptions` or :obj:`None <python:None>`
        """
        return self._kijun_line

    @kijun_line.setter
    @class_sensitive(IKHLineOptions)
    def kijun_line(self, value):
        self._kijun_line = value

    @property
    def params(self) -> Optional[IKHParameters]:
        """Parameters used in calculating the indicator's data points.

        :rtype: :class:`IKHParameters` or :obj:`None <python:None>`
        """
        return self._params

    @params.setter
    @class_sensitive(IKHParameters)
    def params(self, value):
        self._params = value

    @property
    def senkou_span(self) -> Optional[SenkouSpanOptions]:
        """Configuration options for the senkou span.

        :rtype: :class:`SenkouSpanOptions` or :obj:`None <python:None>`
        """
        return self._senkou_span

    @senkou_span.setter
    @class_sensitive(SenkouSpanOptions)
    def senkou_span(self, value):
        self._senkou_span = value

    @property
    def senkou_span_a(self) -> Optional[IKHLineOptions]:
        """Styles for configuring the IKH Senkou Span A.

        :rtype: :class:`IKHLineOptions` or :obj:`None <python:None>`
        """
        return self._senkou_span_a

    @senkou_span_a.setter
    @class_sensitive(IKHLineOptions)
    def senkou_span_a(self, value):
        self._senkou_span_a = value

    @property
    def senkou_span_b(self) -> Optional[IKHLineOptions]:
        """Styles for configuring the IKH Senkou Span B.

        :rtype: :class:`IKHLineOptions` or :obj:`None <python:None>`
        """
        return self._senkou_span_b

    @senkou_span_b.setter
    @class_sensitive(IKHLineOptions)
    def senkou_span_b(self, value):
        self._senkou_span_b = value

    @property
    def tenkan_line(self) -> Optional[IKHLineOptions]:
        """Styles for configuring the IKH Tenkan Line.

        :rtype: :class:`IKHLineOptions` or :obj:`None <python:None>`
        """
        return self._tenkan_line

    @tenkan_line.setter
    @class_sensitive(IKHLineOptions)
    def tenkan_line(self, value):
        self._tenkan_line = value

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

            'chikou_line': as_dict.get('chikouLine', None),
            'kijun_line': as_dict.get('kijunLine', None),
            'senkou_span': as_dict.get('senkouSpan', None),
            'senkou_span_a': as_dict.get('senkouSpanA', None),
            'senkou_span_b': as_dict.get('senkouSpanB', None),
            'tenkan_line': as_dict.get('tenkanLine', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'chikouLine': self.chikou_line,
            'kijunLine': self.kijun_line,
            'senkouSpan': self.senkou_span,
            'senkouSpanA': self.senkou_span_a,
            'senkouSpanB': self.senkou_span_b,
            'tenkanLine': self.tenkan_line,
        }

        parent_as_dict = super()._to_untrimmed_dict(in_cls = in_cls)

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed

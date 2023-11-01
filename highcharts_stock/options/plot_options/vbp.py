from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts_core.decorators import class_sensitive
from highcharts_core.metaclasses import HighchartsMeta

from highcharts_stock.options.plot_options.indicators import ComparableIndicatorOptions
from highcharts_stock.options.plot_options.momentum import OBVParameters
from highcharts_stock.utility_functions import mro__to_untrimmed_dict


class VBPParameters(OBVParameters):

    def __init__(self, **kwargs):
        self._ranges = None

        self.ranges = kwargs.get('ranges', None)

        super().__init__(**kwargs)

    @property
    def ranges(self) -> Optional[int]:
        """The number of price zones/bands. Defaults to ``12``.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._ranges

    @ranges.setter
    def ranges(self, value):
        self._ranges = validators.integer(value,
                                          allow_empty = True,
                                          minimum = 1)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'ranges': as_dict.get('ranges', None),
            'volume_series_id': as_dict.get('volumeSeriesID', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'ranges': self.ranges,
            'volumeSeriesID': self.volume_series_id,
        }

        return untrimmed


class VolumeDivisionStyles(HighchartsMeta):
    """Styles to apply to the positive and negative bars."""

    def __init__(self, **kwargs):
        self._negative_color = None
        self._positive_color = None

        self.negative_color = kwargs.get('negative_color', None)
        self.positive_color = kwargs.get('positive_color', None)

    @property
    def negative_color(self) -> Optional[str]:
        """The color of negative volume bars. Defaults to ``'rgba(244, 91, 91, 0.8)'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._negative_color

    @negative_color.setter
    def negative_color(self, value):
        self._negative_color = validators.string(value, allow_empty = True)

    @property
    def positive_color(self) -> Optional[str]:
        """The color of positive volume bars. Defaults to ``'rgba(144, 237, 125, 0.8)'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._positive_color

    @positive_color.setter
    def positive_color(self, value):
        self._positive_color = validators.string(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'negative_color': as_dict.get('negativeColor', None),
            'positive_color': as_dict.get('positiveColor', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'negativeColor': self.negative_color,
            'positiveColor': self.positive_color,
        }

        return untrimmed


class VolumeDivisionOptions(HighchartsMeta):
    """Configuration of the bars when volume is divided into positive and negative."""

    def __init__(self, **kwargs):
        self._enabled = None
        self._styles = None

        self.enabled = kwargs.get('enabled', None)
        self.styles = kwargs.get('styles', None)

    @property
    def enabled(self) -> Optional[bool]:
        """If ``True``, displays volume divided into price zones/bands. Defaults to
        ``True``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        if value is None:
            self._enabled = None
        else:
            self._enabled = bool(value)

    @property
    def styles(self) -> Optional[VolumeDivisionStyles]:
        """Styles to apply to negative and positive bars.

        :rtype: :class:`VolumeDivisionStyles` or :obj:`None <python:None>`
        """
        return self._styles

    @styles.setter
    @class_sensitive(VolumeDivisionStyles)
    def styles(self, value):
        self._styles = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'enabled': as_dict.get('enabled', None),
            'styles': as_dict.get('styles', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'enabled': self.enabled,
            'styles': self.styles,
        }

        return untrimmed


class ZoneLinesOptions(HighchartsMeta):
    """Configuration of the lines which divide volume into price zones/bands."""

    def __init__(self, **kwargs):
        self._enabled = None
        self._styles = None

        self.enabled = kwargs.get('enabled', None)
        self.styles = kwargs.get('styles', None)

    @property
    def enabled(self) -> Optional[bool]:
        """If ``True``, displays lines dividing the volume into zones/bands. Defaults to
        ``True``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        if value is None:
            self._enabled = None
        else:
            self._enabled = bool(value)

    @property
    def styles(self) -> Optional[str]:
        """Styles to apply to the price band lines. Defaults to
        ``'{"color": "#0A9AC9", "dashStyle": "LongDash", "lineWidth": 1}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._styles

    @styles.setter
    def styles(self, value):
        self._styles = validators.string(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'enabled': as_dict.get('enabled', None),
            'styles': as_dict.get('styles', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'enabled': self.enabled,
            'styles': self.styles,
        }

        return untrimmed


class VBPOptions(ComparableIndicatorOptions):
    """Options to configure a Volume-by-Price (VBP)
    :term:`indicator <technical indicator>`, which can be used to analyze volumes traded
    within various price bands.

    .. figure:: ../../../_static/vbp-example.png
      :alt: Volume-by-Price (VBP) Example Chart
      :align: center

    """

    def __init__(self, **kwargs):
        self._point_padding = None
        self._volume_division = None
        self._zone_lines = None

        self.point_padding = kwargs.get('point_padding', None)
        self.volume_division = kwargs.get('volume_division', None)
        self.zone_lines = kwargs.get('zone_lines', None)

        super().__init__(**kwargs)

    @property
    def compare_start(self):
        """Does not apply, so raises an :exc:`AttributeError <python:AttributeError>`."""
        raise AttributeError(f"{self.__class__.__name__} has no attribute "
                             f"'compare_start'")

    @compare_start.setter
    def compare_start(self, value):
        raise AttributeError(f"{self.__class__.__name__} has no attribute "
                             f"'compare_start'")

    @property
    def params(self) -> Optional[VBPParameters]:
        """Parameters used in calculating the indicator's data points.

        :rtype: :class:`VBPParameters` or :obj:`None <python:None>`
        """
        return self._params

    @params.setter
    @class_sensitive(VBPParameters)
    def params(self, value):
        self._params = value

    @property
    def point_padding(self) -> Optional[int | float | Decimal]:
        """Padding between each bar, in x axis units. Defaults to ``0``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._point_padding

    @point_padding.setter
    def point_padding(self, value):
        self._point_padding = validators.numeric(value,
                                                 allow_empty = True,
                                                 minimum = 0)

    @property
    def volume_division(self) -> Optional[VolumeDivisionOptions]:
        """The styles to apply to the bars when volume is divided into positive and
        negative.

        :rtype: :class:`VolumeDivisionOptions` or :obj:`None <python:None>`
        """
        return self._volume_division

    @volume_division.setter
    @class_sensitive(VolumeDivisionOptions)
    def volume_division(self, value):
        self._volume_division = value

    @property
    def zone_lines(self) -> Optional[ZoneLinesOptions]:
        """The styles to apply to the lines that demarcate price zones/bands.

        :rtype: :class:`ZoneLinesOptions` or :obj:`None <python:None>`
        """
        return self._zone_lines

    @zone_lines.setter
    @class_sensitive(ZoneLinesOptions)
    def zone_lines(self, value):
        self._zone_lines = value

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

            'point_padding': as_dict.get('pointPadding', None),
            'volume_division': as_dict.get('volumeDivision', None),
            'zone_lines': as_dict.get('zoneLines', None),

        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'pointPadding': self.point_padding,
            'volumeDivision': self.volume_division,
            'zoneLines': self.zone_lines,
        }

        parent_as_dict = mro__to_untrimmed_dict(self, in_cls = in_cls)

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed

from typing import Optional

from validator_collection import validators

from highcharts_stock.options.series.area import AreaSeries
from highcharts_stock.options.plot_options.bellcurve import BellCurveOptions
from highcharts_stock.utility_functions import mro__to_untrimmed_dict


class BellCurveSeries(AreaSeries, BellCurveOptions):
    """Options to configure a Bell Curve series.

    A bell curve is an areaspline series which represents the probability density
    function of the normal distribution. It calculates mean and standard deviation of
    the base series data and plots the curve according to the calculated parameters.

    .. figure:: ../../../_static/bellcurve-example.png
      :alt: Bell Curve Example Chart
      :align: center

    """

    def __init__(self, **kwargs):
        self._base_series = None

        self.base_series = kwargs.get('base_series', None)

        super().__init__(**kwargs)

    @property
    def data(self) -> None:
        """The collection of data points for the series. Defaults to
        :obj:`None <python:None>`.

        .. warning::

          All Bell Curve Series by definition return :obj:`None <python:None>` for their
          data. They are a special series, drawn in relationship to the
          :meth:`base_series <BellCurveSeries.base_series>` specified, and do not receive
          independent data points of their own.

        :rtype: :obj:`None <python:None>`
        """
        return None

    @data.setter
    def data(self, value):
        pass

    @property
    def base_series(self) -> Optional[int | str]:
        """An integer identifying the index to use for the base series, or a string
        representing the id of the series. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`int <python:int>` or :class:`str <python:str>` or
          :obj:`None <python:None>`
        """
        return self._base_series

    @base_series.setter
    def base_series(self, value):
        if value is None:
            self._base_series = None
        else:
            try:
                value = validators.string(value)
            except (TypeError, ValueError):
                value = validators.integer(value)

            self._base_series = value

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
            'fill_color': as_dict.get('fillColor', None),
            'fill_opacity': as_dict.get('fillOpacity', None),
            'find_nearest_point_by': as_dict.get('findNearestPointBy', None),
            'get_extremes_from_all': as_dict.get('getExtremesFromAll', None),
            'linecap': as_dict.get('linecap', None),
            'line_color': as_dict.get('lineColor', None),
            'line_width': as_dict.get('lineWidth', None),
            'negative_color': as_dict.get('negativeColor', None),
            'negative_fill_color': as_dict.get('negativeFillColor', None),
            'point_interval': as_dict.get('pointInterval', None),
            'point_interval_unit': as_dict.get('pointIntervalUnit', None),
            'point_placement': as_dict.get('pointPlacement', None),
            'point_start': as_dict.get('pointStart', None),
            'relative_x_value': as_dict.get('relativeXValue', None),
            'shadow': as_dict.get('shadow', None),
            'soft_threshold': as_dict.get('softThreshold', None),
            'stacking': as_dict.get('stacking', None),
            'step': as_dict.get('step', None),
            'track_by_area': as_dict.get('trackByArea', None),
            'zone_axis': as_dict.get('zoneAxis', None),
            'zones': as_dict.get('zones', None),

            'data': as_dict.get('data', None),
            'id': as_dict.get('id', None),
            'index': as_dict.get('index', None),
            'legend_index': as_dict.get('legendIndex', None),
            'name': as_dict.get('name', None),
            'stack': as_dict.get('stack', None),
            'x_axis': as_dict.get('xAxis', None),
            'y_axis': as_dict.get('yAxis', None),
            'z_index': as_dict.get('zIndex', None),

            'intervals': as_dict.get('intervals', None),

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

            'base_series': as_dict.get('baseSeries', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'baseSeries': self.base_series,
            'data': self.data
        }

        parents_as_dict = mro__to_untrimmed_dict(self, in_cls = in_cls) or {}
        for key in parents_as_dict:
            untrimmed[key] = parents_as_dict[key]

        return untrimmed


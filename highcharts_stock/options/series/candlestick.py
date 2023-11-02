from typing import Optional, List
from highcharts_stock.utility_functions import mro__to_untrimmed_dict, is_ndarray

from highcharts_stock.options.series.base import SeriesBase
from highcharts_stock.options.plot_options.candlestick import CandlestickOptions
from highcharts_stock.options.series.data.candlestick import CandlestickData, CandlestickDataCollection


class CandlestickSeries(SeriesBase, CandlestickOptions):
    """General options to apply to all Candlestick series types. A candlestick chart is a
    style of financial chart used to describe price movements over time.

    .. figure:: ../../../_static/candlestick-example.png
      :alt: Candlestick Example Chart
      :align: center

    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def data(self) -> Optional[List[CandlestickData] | CandlestickDataCollection]:
        """Collection of data that represents the series. Defaults to
        :obj:`None <python:None>`.

        While the series type returns a collection of :class:`CandlestickData` instances,
        it accepts as input three different types of data:

        .. tabs::

          .. tab:: 5D Collection

            .. code-block::

              series = CandlestickSeries()
              series.data = [
                  [1463753252, 7, 2, 0, 4],
                  [1563753252, 1, 4, 2, 8],
                  [1663753252, 3, 3, 9, 3]
              ]

            A five-dimensional collection of numerical values representing (in order) the
            ``x`` value, the ``open`` value, the ``high`` value, the ``low`` value, and
            the ``close`` value.

            .. tip::

              The ``x`` value is always expected to be a timestamp expressed in
              milliseconds since 1970. If a :class:`datetime <python:datetime.datetime>`
              or coercable is supplied, **Highcharts for Python** will automatically
              coerce it to a POSIX timestamp (milliseconds since 1970).

          .. tab:: 4D Collection

            .. code-block::

              series = CandlestickSeries()
              series.data = [
                  [7, 2, 0, 4],
                  [1, 4, 2, 8],
                  [3, 3, 9, 3]
              ]

            A four-dimensional collection of numerical values. The members represent the
            ``open`` value, the ``high`` value, the ``low`` value, and the ``close``
            value, respectively.

            .. note::

              The ``x`` value in this case will be automatically calculated either
              starting from ``0`` and incremented by ``1`` or from
              :meth:`.point_start <highcharts_stock.options.series.candlestick.CandlestickSeries.point_start>`
              and
              :meth:`.point_interval <highcharts_stock.options.series.candlestick.CandlestickSeries.point_interval>`
              in the series or plot options.

          .. tab:: Object Collection

            A one-dimensional collection of :class:`CandlestickData` objects, or objects
            coercable.

        :rtype: :class:`list <python:list>` of :class:`CandlestickData` or
          :class:`CandlestickDataCollection` or
          :obj:`None <python:None>`
        """
        return self._data

    @data.setter
    def data(self, value):
        if not is_ndarray(value) and not value:
            self._data = None
        else:
            self._data = CandlestickData.from_array(value)

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
            'gap_size': as_dict.get('gapSize', None),
            'gap_unit': as_dict.get('gapUnit', None),
            'last_price': as_dict.get('lastPrice', None),
            'last_visible_price': as_dict.get('lastVisiblePrice', None),

            'compare': as_dict.get('compare', None),
            'compare_base': as_dict.get('compareBase', None),
            'navigator_options': as_dict.get('navigatorOptions', None),
            'show_in_navigator': as_dict.get('showInNavigator', None),

            'point_val_key': as_dict.get('pointValKey', None),
            'up_color': as_dict.get('upColor', None),
            'up_line_color': as_dict.get('upLineColor', None),

            'data': as_dict.get('data', None),
            'id': as_dict.get('id', None),
            'index': as_dict.get('index', None),
            'legend_index': as_dict.get('legendIndex', None),
            'name': as_dict.get('name', None),
            'stack': as_dict.get('stack', None),
            'x_axis': as_dict.get('xAxis', None),
            'y_axis': as_dict.get('yAxis', None),
            'z_index': as_dict.get('zIndex', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = mro__to_untrimmed_dict(self, in_cls = in_cls) or {}

        return untrimmed

    @classmethod
    def _data_collection_class(cls):
        """Returns the class object used for the data collection.
        
        :rtype: :class:`DataPointCollection <highcharts_core.options.series.data.collections.DataPointCollection>`
          descendent
        """
        return CandlestickDataCollection

    @classmethod
    def _data_point_class(cls):
        """Returns the class object used for individual data points.
        
        :rtype: :class:`DataBase <highcharts_core.options.series.data.base.DataBase>` 
          descendent
        """
        return CandlestickData


class HollowCandlestickSeries(CandlestickSeries):
    """General options to apply to Hollow Candlestick series types. A candlestick chart is
    a style of financial chart used to describe price movements over time.

    .. figure:: ../../../_static/hollow-candlestick-example.png
      :alt: Hollow Candlestick Example Chart
      :align: center

    """
    pass


class HeikinAshiSeries(CandlestickSeries):
    """General options to apply to Heikin Ashi series types, which are visualized
    similarly to :class:`CandlestickSeries <options.series.candlestick.CandlestickSeries>`
    but which feature a smoother line by tracking ranges of movement rather than
    individual movements.

    .. figure:: ../../../_static/heikin-ashi-example.png
      :alt: Heikin Ashi Example Chart
      :align: center

    """
    pass

from typing import Optional, List

from highcharts_stock.utility_functions import mro__to_untrimmed_dict, is_ndarray

from highcharts_stock.options.series.base import NavigatorIndicatorSeries
from highcharts_stock.options.plot_options.flags import FlagsOptions
from highcharts_stock.options.series.data.flags import (FlagData, 
                                                        FlagDataCollection)


class FlagsSeries(NavigatorIndicatorSeries, FlagsOptions):
    """Flags are used to mark events in **Highcharts Stock for Python**. They can be added
    on the timeline, or attached to a specific series.

    .. figure:: ../../../_static/flags-example.png
      :alt: Flags Example
      :align: center

    """

    def __init__(self, **kwargs):
        self._data = None
        
        self.data = kwargs.get('data', None)
        
        super().__init__(**kwargs)
        
    @property
    def data(self) -> Optional[List[FlagData] | FlagDataCollection]:
        """Collection of data that represents the series. Defaults to
        :obj:`None <python:None>`.

        While the series type returns a collection of :class:`SingleXData` instances
        or an :class:`SingleXDataCollection` instance, it accepts as input 
        two different types of data:

        .. tabs::

          .. tab:: 1D Collection

            .. code-block::

              series = FlagSeries()
              series.data = [
                  [1463753252],
                  [1563753252],
                  [1663753252]
              ]

            A one-dimensional collection of values, corresponding to the position of
            each flag on the x-axis. 

          .. tab:: Object Collection

            A one-dimensional collection of :class:`SingleXData` objects, or objects
            coercable.

        :rtype: :class:`list <python:list>` of :class:`SingleXData` or
          :class:`SingleXDataCollection` or :obj:`None <python:None>`
        """
        return self._data

    @data.setter
    def data(self, value):
        if not is_ndarray(value) and not value:
            self._data = None
        else:
            self._data = self._data_point_class().from_array(value)

    @classmethod
    def _data_collection_class(cls):
        """Returns the class object used for the data collection.
        
        :rtype: :class:`DataPointCollection <highcharts_core.options.series.data.collections.DataPointCollection>`
          descendent
        """
        return FlagDataCollection
    
    @classmethod
    def _data_point_class(cls):
        """Returns the class object used for individual data points.
        
        :rtype: :class:`DataBase <highcharts_core.options.series.data.base.DataBase>` 
          descendent
        """
        return FlagData

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

            'allow_overlap_x': as_dict.get('allowOverlapX', None),
            'center_in_category': as_dict.get('centerInCategory', None),
            'colors': as_dict.get('colors', None),
            'fill_color': as_dict.get('fillColor', None),
            'group_padding': as_dict.get('groupPadding', None),
            'grouping': as_dict.get('grouping', None),
            'height': as_dict.get('height', None),
            'line_color': as_dict.get('lineColor', None),
            'max_point_width': as_dict.get('maxPointWidth', None),
            'min_point_length': as_dict.get('minPointLength', None),
            'on_key': as_dict.get('onKey', None),
            'on_series': as_dict.get('onSeries', None),
            'shape': as_dict.get('shape', None),
            'stack_distance': as_dict.get('stackDistance', None),
            'style': as_dict.get('style', None),
            'text_align': as_dict.get('textAlign', None),
            'title': as_dict.get('title', None),
            'use_html': as_dict.get('useHTML', None),
            'width': as_dict.get('width', None),
            'y': as_dict.get('y', None),

            'id': as_dict.get('id', None),
            'index': as_dict.get('index', None),
            'legend_index': as_dict.get('legendIndex', None),
            'name': as_dict.get('name', None),
            'stack': as_dict.get('stack', None),
            'x_axis': as_dict.get('xAxis', None),
            'y_axis': as_dict.get('yAxis', None),
            'z_index': as_dict.get('zIndex', None),

            'data': as_dict.get('data', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'data': self.data
        }
        untrimmed_parents = mro__to_untrimmed_dict(self, in_cls = in_cls) or {}
        for key in untrimmed_parents:
            if key not in untrimmed:
                untrimmed[key] = untrimmed_parents[key]

        return untrimmed

from typing import Optional, List

from highcharts_stock.options.series.pie import PieSeries
from highcharts_stock.options.plot_options.item import ItemOptions
from highcharts_stock.options.series.data.single_point import SinglePointData, SinglePointDataCollection
from highcharts_stock.utility_functions import mro__to_untrimmed_dict, is_ndarray


class ItemSeries(PieSeries, ItemOptions):
    """Options to configure an Item series.

    An item chart is an infographic chart where a number of items are laid out in
    either a rectangular or circular pattern. It can be used to visualize counts
    within a group, or for the circular pattern, typically a parliament.

    The circular layout has much in common with a pie chart. Many of the item series
    options, like ``center``, ``size`` and data label positioning, are inherited from
    the :meth:`PlotOptions.pie` series and don't apply for rectangular layouts.

    .. tabs::

      .. tab:: Circular Item Chart

        .. figure:: ../../../_static/item-example-circular.png
          :alt: Circular Item Example Chart
          :align: center

      .. tab:: Rectangular Item Chart

        .. figure:: ../../../_static/item-example-rectangular.png
          :alt: Rectangular Item Example Chart
          :align: center

      .. tab:: Item Chart with Symbols

        .. figure:: ../../../_static/item-example-symbols.png
          :alt: Item Example Chart with Symbols
          :align: center

    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def data(self) -> Optional[List[SinglePointData] | SinglePointDataCollection]:
        """Collection of data that represents the series. Defaults to
        :obj:`None <python:None>`.

        While the series type returns a collection of :class:`SinglePointData` instances,
        it accepts as input three different types of data:

        .. tabs::

          .. tab:: 1D Collection

            .. code-block::

              series = ItemSeries()
              series.data = [0, 5, 3, 5]

            A one-dimensional collection of numerical values. Each member of the
            collection will be interpreted as a :meth:`y <SinglePointData.y>` value

          .. tab:: Object Collection

            A one-dimensional collection of :class:`SinglePointData` objects.

        :rtype: :class:`list <python:list>` of :class:`SinglePointData` or
          :class:`SinglePointDataCollection` or
          :obj:`None <python:None>`
        """
        return self._data

    @data.setter
    def data(self, value):
        if not is_ndarray(value) and not value:
            self._data = None
        else:
            self._data = SinglePointData.from_array(value)

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

            'border_color': as_dict.get('borderColor', None),
            'border_width': as_dict.get('borderWidth', None),
            'center': as_dict.get('center', None),
            'color_axis': as_dict.get('colorAxis', None),
            'color_index': as_dict.get('colorIndex', None),
            'color_key': as_dict.get('colorKey', None),
            'colors': as_dict.get('colors', None),
            'depth': as_dict.get('depth', None),
            'end_angle': as_dict.get('endAngle', None),
            'fill_color': as_dict.get('fillColor', None),
            'ignore_hidden_point': as_dict.get('ignoreHiddenPoint', None),
            'inner_size': as_dict.get('innerSize', None),
            'linecap': as_dict.get('linecap', None),
            'min_size': as_dict.get('minSize', None),
            'size': as_dict.get('size', None),
            'sliced_offset': as_dict.get('slicedOffset', None),
            'start_angle': as_dict.get('startAngle', None),
            'thickness': as_dict.get('thickness', None),

            'item_padding': as_dict.get('itemPadding', None),
            'layout': as_dict.get('layout', None),
            'rows': as_dict.get('rows', None),

            'data': as_dict.get('data', None),
            'id': as_dict.get('id', None),
            'index': as_dict.get('index', None),
            'legend_index': as_dict.get('legendIndex', None),
            'name': as_dict.get('name', None),
            'stack': as_dict.get('stack', None),
            'x_axis': as_dict.get('xAxis', None),
            'y_axis': as_dict.get('yAxis', None),
            'z_index': as_dict.get('zIndex', None),

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
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = mro__to_untrimmed_dict(self, in_cls = in_cls)

        return untrimmed

    @classmethod
    def _data_collection_class(cls):
        """Returns the class object used for the data collection.
        
        :rtype: :class:`DataPointCollection <highcharts_core.options.series.data.collections.DataPointCollection>`
          descendent
        """
        return SinglePointDataCollection
    
    @classmethod
    def _data_point_class(cls):
        """Returns the class object used for individual data points.
        
        :rtype: :class:`DataBase <highcharts_core.options.series.data.base.DataBase>` 
          descendent
        """
        return SinglePointData

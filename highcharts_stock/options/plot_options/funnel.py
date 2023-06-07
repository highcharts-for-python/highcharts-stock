from highcharts_core.options.plot_options.funnel import (FunnelOptions as FunnelBase,
                                                           Funnel3DOptions as Funnel3DBase)
from highcharts_core.utility_functions import mro__to_untrimmed_dict

from highcharts_stock.options.plot_options.base import NonIndicatorOptions


class FunnelOptions(FunnelBase, NonIndicatorOptions):
    """General options to apply to all Funnel series types.

    Funnel charts are a type of chart often used to visualize stages in a sales
    project, where the top are the initial stages with the most clients.

    .. warning::

      Funnel charts require that the ``modules/funnel.js`` file is loaded client-side.

    .. figure:: ../../../_static/funnel-example.png
      :alt: Funnel Example Chart
      :align: center

    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

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

            'border_radius': as_dict.get('borderRadius', None),
            'height': as_dict.get('height', None),
            'neck_height': as_dict.get('neckHeight', None),
            'neck_width': as_dict.get('neckWidth', None),
            'reversed': as_dict.get('reversed', None),
            'width': as_dict.get('width', None),

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
        untrimmed = {}
        parent_as_dict = mro__to_untrimmed_dict(self, in_cls = in_cls) or {}

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed


class Funnel3DOptions(Funnel3DBase, NonIndicatorOptions):
    """General options to apply to all Funnel 3D series types.

    A Funnel 3D chart is a three-dimensional version of funnel series type. Funnel
    charts are a type of chart often used to visualize stages in a sales project,
    where the top are the initial stages with the most clients.

    .. warning::

      Funnel 3D charts require that the following files are all loaded client-side:

        * ``highcharts-3d.js``,
        * ``cylinder.js`` and
        * ``funnel3d.js``

    .. figure:: ../../../_static/funnel_3d-example.png
      :alt: Funnel 3D Example Chart
      :align: center

    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {}
        mro = cls.mro()
        parent_kwargs = [x._get_kwargs_from_dict(as_dict) for x in mro[1:2]]
        for kwarg_set in parent_kwargs:
            for key in kwarg_set:
                kwargs[key] = kwarg_set[key]

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {}
        parent_as_dict = mro__to_untrimmed_dict(self, in_cls = in_cls) or {}

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed

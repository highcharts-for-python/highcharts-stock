from highcharts_core.options.plot_options.sunburst import SunburstOptions as SunburstBase
from highcharts_core.utility_functions import mro__to_untrimmed_dict

from highcharts_stock.options.plot_options.base import NonIndicatorOptions


class SunburstOptions(SunburstBase, NonIndicatorOptions):
    """General options to apply to all Sunburst series types.

    A Sunburst displays hierarchical data, where a level in the hierarchy is
    represented by a circle. The center represents the root node of the tree. The
    visualization bears a resemblance to both treemap and pie charts.

    .. figure:: ../../../_static/sunburst-example.png
      :alt: Sunburst Example Chart
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

            'allow_traversing_tree': as_dict.get('allowTraversingTree', None),
            'border_color': as_dict.get('borderColor', None),
            'border_width': as_dict.get('borderWidth', None),
            'breadcrumbs': as_dict.get('breadcrumbs', None),
            'center': as_dict.get('center', None),
            'color_by_point': as_dict.get('colorByPoint', None),
            'color_index': as_dict.get('colorIndex', None),
            'crisp': as_dict.get('crisp', None),
            'fill_color': as_dict.get('fillColor', None),
            'level_is_constant': as_dict.get('levelIsConstant', None),
            'levels': as_dict.get('levels', None),
            'level_size': as_dict.get('levelSize', None),
            'root_id': as_dict.get('rootId', None),
            'shadow': as_dict.get('shadow', None),
            'size': as_dict.get('size', None),
            'sliced_offset': as_dict.get('slicedOffset', None),
            'start_angle': as_dict.get('startAngle', None),

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

from highcharts_core.options.plot_options.wordcloud import (RotationOptions,
                                                              WordcloudOptions as WordcloudBase)
from highcharts_core.utility_functions import mro__to_untrimmed_dict

from highcharts_stock.options.plot_options.base import NonIndicatorOptions


class WordcloudOptions(WordcloudBase, NonIndicatorOptions):
    """General options to apply to all Wordcloud series types.

    A word cloud is a visualization of a set of words, where the size and placement of
    a word is determined by how it is weighted.

    .. figure:: ../../../_static/wordcloud-example.png
      :alt: Wordcloud Example Chart
      :align: center

    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        """Convenience method which returns the keyword arguments used to initialize the
        class from a Highcharts Javascript-compatible :class:`dict <python:dict>` object.

        :param as_dict: The HighCharts JS compatible :class:`dict <python:dict>`
          representation of the object.
        :type as_dict: :class:`dict <python:dict>`

        :returns: The keyword arguments that would be used to initialize an instance.
        :rtype: :class:`dict <python:dict>`

        """
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

            # Copied from SeriesOptions
            'animation_limit': as_dict.get('animationLimit', None),
            'color_index': as_dict.get('colorIndex', None),
            'color_key': as_dict.get('colorKey', None),
            'relative_x_value': as_dict.get('relativeXValue', None),

            # Copied from BaseBarOptions
            'border_color': as_dict.get('borderColor', None),
            'border_radius': as_dict.get('borderRadius', None),
            'border_width': as_dict.get('borderWidth', None),
            'center_in_category': as_dict.get('centerInCategory', None),
            'color_by_point': as_dict.get('colorByPoint', None),
            'colors': as_dict.get('colors', None),
            'edge_width': as_dict.get('edgeWidth', None),

            # Native to WordcloudOptions
            'allow_extend_playing_field': as_dict.get('allowExtendPlayingField', None),
            'max_font_size': as_dict.get('maxFontSize', None),
            'min_font_size': as_dict.get('minFontSize', None),
            'placement_strategy': as_dict.get('placementStrategy', None),
            'rotation': as_dict.get('rotation', None),
            'spiral': as_dict.get('spiral', None),

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

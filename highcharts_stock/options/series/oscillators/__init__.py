from highcharts_stock.utility_functions import mro__to_untrimmed_dict

from highcharts_stock.options.series.base import (IndicatorSeriesBase,
                                                  NavigatorIndicatorSeries)
from highcharts_stock.options.plot_options.oscillators import (AroonOscillatorOptions,
                                                               APOOptions,
                                                               CCIOptions,
                                                               ChaikinOptions,
                                                               CMOOptions,
                                                               DPOOptions,
                                                               TRIXOptions,
                                                               WilliamsROptions)


class AroonOscillatorSeries(IndicatorSeriesBase, AroonOscillatorOptions):
    """Options to configure an Aroon Oscillator series, which is an :term:`oscillator`
    that is used to gauge the strength of a current trend and the likelihood that it will
    continue.

    .. figure:: ../../../../_static/aroon-oscillator-example.png
      :alt: Aroon Oscillator Example Chart
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

            'id': as_dict.get('id', None),
            'index': as_dict.get('index', None),
            'legend_index': as_dict.get('legendIndex', None),
            'stack': as_dict.get('stack', None),
            'x_axis': as_dict.get('xAxis', None),
            'y_axis': as_dict.get('yAxis', None),
            'z_index': as_dict.get('zIndex', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = mro__to_untrimmed_dict(self, in_cls = in_cls) or {}

        return untrimmed


class APOSeries(IndicatorSeriesBase, APOOptions):
    """Options to configure a Absolute Price
    :term:`Oscillator <oscillator>` (APO), which is an :term:`oscillator` that displays
    the difference between two exponential moving averages of an asset's price expressed
    as an absolute value

    .. figure:: ../../../../_static/apo-example.png
      :alt: Absolute Price Oscillator Example Chart
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

            'id': as_dict.get('id', None),
            'index': as_dict.get('index', None),
            'legend_index': as_dict.get('legendIndex', None),
            'stack': as_dict.get('stack', None),
            'x_axis': as_dict.get('xAxis', None),
            'y_axis': as_dict.get('yAxis', None),
            'z_index': as_dict.get('zIndex', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = mro__to_untrimmed_dict(self, in_cls = in_cls) or {}

        return untrimmed


class CCISeries(NavigatorIndicatorSeries, CCIOptions):
    """Options to configure a Commodity Channel Index
    :term:`indicator <technical indicator>`, which is an :term:`oscillator` that measures
    the difference between the current price and the historical average price using a
    look-back
    period determined by the configuration of
    :meth:`.params <highcharts_stock.options.plot_options.atr.CCIOptions.params`.

    .. figure:: ../../../../_static/cci-example.png
      :alt: CCI Example Chart
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

            'id': as_dict.get('id', None),
            'index': as_dict.get('index', None),
            'legend_index': as_dict.get('legendIndex', None),
            'stack': as_dict.get('stack', None),
            'x_axis': as_dict.get('xAxis', None),
            'y_axis': as_dict.get('yAxis', None),
            'z_index': as_dict.get('zIndex', None),

            'navigator_options': as_dict.get('navigatorOptions', None),
            'show_in_navigator': as_dict.get('showInNavigator', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = mro__to_untrimmed_dict(self, in_cls = in_cls) or {}

        return untrimmed


class ChaikinSeries(IndicatorSeriesBase, ChaikinOptions):
    """Options to configure a Chaikin :term:`oscillator`, which measures the
    accummulation-distribution line of moving average convergence-divergence by
    subtracting a 10-day exponential moving average from a 3-day moving average of the
    accumulation-distribution line.

    .. figure:: ../../../../_static/chaikin-example.png
      :alt: Chaikin Oscillator Example Chart
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

            'id': as_dict.get('id', None),
            'index': as_dict.get('index', None),
            'legend_index': as_dict.get('legendIndex', None),
            'stack': as_dict.get('stack', None),
            'x_axis': as_dict.get('xAxis', None),
            'y_axis': as_dict.get('yAxis', None),
            'z_index': as_dict.get('zIndex', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = mro__to_untrimmed_dict(self, in_cls = in_cls) or {}

        return untrimmed


class CMOSeries(NavigatorIndicatorSeries, CMOOptions):
    """Options to configure a Chande Momentum :term:`Oscillator`, which uses momentum to
    identify relative strength or weakness in a market.

    .. caution::

      The chosen time frame - configured by
      :meth:`.params.period <highcharts_stock.options.plot_options.atr.CCIOptions.params`
      and defaulting to a value of ``20`` - has a significant impact on the signals
      generated by the indicator.

    .. figure:: ../../../../_static/cmo-example.png
      :alt: Chande Momentum Oscillator Example Chart
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

            'id': as_dict.get('id', None),
            'index': as_dict.get('index', None),
            'legend_index': as_dict.get('legendIndex', None),
            'stack': as_dict.get('stack', None),
            'x_axis': as_dict.get('xAxis', None),
            'y_axis': as_dict.get('yAxis', None),
            'z_index': as_dict.get('zIndex', None),

            'navigator_options': as_dict.get('navigatorOptions', None),
            'show_in_navigator': as_dict.get('showInNavigator', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = mro__to_untrimmed_dict(self, in_cls = in_cls) or {}

        return untrimmed


class DPOSeries(IndicatorSeriesBase, DPOOptions):
    """Options to configure a Detrended Price :term:`Oscillator`, which
    strips out price trends in an effort to estimate the length of price cycles.

    .. figure:: ../../../../_static/dpo-example.png
      :alt: DPO Example Chart
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

            'id': as_dict.get('id', None),
            'index': as_dict.get('index', None),
            'legend_index': as_dict.get('legendIndex', None),
            'stack': as_dict.get('stack', None),
            'x_axis': as_dict.get('xAxis', None),
            'y_axis': as_dict.get('yAxis', None),
            'z_index': as_dict.get('zIndex', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = mro__to_untrimmed_dict(self, in_cls = in_cls) or {}

        return untrimmed


class TRIXSeries(IndicatorSeriesBase, TRIXOptions):
    """Options to configure a Triple Exponential Average :term:`Oscillator`, which
    can be used to suggest increasing or decreasing momentum.

    .. figure:: ../../../../_static/trix-example.png
      :alt: TRIX Example Chart
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

            'id': as_dict.get('id', None),
            'index': as_dict.get('index', None),
            'legend_index': as_dict.get('legendIndex', None),
            'stack': as_dict.get('stack', None),
            'x_axis': as_dict.get('xAxis', None),
            'y_axis': as_dict.get('yAxis', None),
            'z_index': as_dict.get('zIndex', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = mro__to_untrimmed_dict(self, in_cls = in_cls) or {}

        return untrimmed


class WilliamsRSeries(IndicatorSeriesBase, WilliamsROptions):
    """Options to configure a Williams %R :term:`oscillator`, which uses the current
    closing price in relation to the high and low of the past ``n`` days to indicate
    overbought and oversold levels.

    .. figure:: ../../../../_static/williamsr-example.png
      :alt: Williams %R Example Chart
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

            'id': as_dict.get('id', None),
            'index': as_dict.get('index', None),
            'legend_index': as_dict.get('legendIndex', None),
            'stack': as_dict.get('stack', None),
            'x_axis': as_dict.get('xAxis', None),
            'y_axis': as_dict.get('yAxis', None),
            'z_index': as_dict.get('zIndex', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = mro__to_untrimmed_dict(self, in_cls = in_cls) or {}

        return untrimmed

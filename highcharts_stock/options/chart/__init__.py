from typing import Optional

from highcharts_python.options.chart import (PanningOptions,
                                             ChartOptions as ChartOptionsBase)

from highcharts_stock.decorators import class_sensitive
from highcharts_stock.options.chart.zooming import ZoomingOptions


class ChartOptions(ChartOptionsBase):
    """Configuration settings that apply to a chart."""

    def __init__(self, **kwargs):
        self._zooming = None

        self.zooming = kwargs.get('zooming', None)

        super().__init__(**kwargs)

    @property
    def zooming(self) -> Optional[ZoomingOptions]:
        """Chart zooming configuration.

        :rtype: :class:`ZoomingOptions <highcharts_stock.options.chart.zooming.ZoomingOptions>`
          or :obj:`None <python:None>`
        """
        return self._zooming

    @zooming.setter
    @class_sensitive(ZoomingOptions)
    def zooming(self, value):
        self._zooming = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'align_thresholds': as_dict.get('alignThresholds', None),
            'align_ticks': as_dict.get('alignTicks', None),
            'allow_mutating_data': as_dict.get('allowMutatingData', None),
            'animation': as_dict.get('animation', None),
            'background_color': as_dict.get('backgroundColor', None),
            'border_color': as_dict.get('borderColor', None),
            'border_radius': as_dict.get('borderRadius', None),
            'border_width': as_dict.get('borderWidth', None),
            'class_name': as_dict.get('className', None),
            'color_count': as_dict.get('colorCount', None),
            'display_errors': as_dict.get('displayErrors', None),
            'events': as_dict.get('events', None),
            'height': as_dict.get('height', None),
            'ignore_hidden_series': as_dict.get('ignoreHiddenSeries', None),
            'inverted': as_dict.get('inverted', None),
            'margin': as_dict.get('margin', None),
            'margin_bottom': as_dict.get('marginBottom', None),
            'margin_left': as_dict.get('marginLeft', None),
            'margin_right': as_dict.get('marginRight', None),
            'margin_top': as_dict.get('marginTop', None),
            'number_formatter': as_dict.get('numberFormatter', None),
            'options_3d': as_dict.get('options3d', None),
            'pan_key': as_dict.get('panKey', None),
            'panning': as_dict.get('panning', None),
            'parallel_axes': as_dict.get('parallelAxes', None),
            'parallel_coordinates': as_dict.get('parallelCoordinates', None),
            'pinch_type': as_dict.get('pinchType', None),
            'plot_background_color': as_dict.get('plotBackgroundColor', None),
            'plot_background_image': as_dict.get('plotBackgroundImage', None),
            'plot_border_color': as_dict.get('plotBorderColor', None),
            'plot_border_width': as_dict.get('plotBorderWidth', None),
            'plot_shadow': as_dict.get('plotShadow', None),
            'polar': as_dict.get('polar', None),
            'reflow': as_dict.get('reflow', None),
            'render_to': as_dict.get('renderTo', None),
            'reset_zoom_button': as_dict.get('resetZoomButton', None),
            'scrollable_plot_area': as_dict.get('scrollablePlotArea', None),
            'selection_marker_fill': as_dict.get('selectionMarkerFill', None),
            'shadow': as_dict.get('shadow', None),
            'show_axes': as_dict.get('showAxes', None),
            'spacing': as_dict.get('spacing', None),
            'spacing_bottom': as_dict.get('spacingBottom', None),
            'spacing_left': as_dict.get('spacingLeft', None),
            'spacing_top': as_dict.get('spacingTop', None),
            'spacing_right': as_dict.get('spacingRight', None),
            'style': as_dict.get('style', None),
            'styled_mode': as_dict.get('styledMode', None),
            'type': as_dict.get('type', None),
            'width': as_dict.get('width', None),
            'zoom_by_single_touch': as_dict.get('zoomBySingleTouch', None),
            'zoom_key': as_dict.get('zoomKey', None),
            'zoom_type': as_dict.get('zoomType', None),

            'zooming': as_dict.get('zooming', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'zooming': self.zooming
        }

        parent_as_dict = super()._to_untrimmed_dict(in_cls = in_cls)

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed

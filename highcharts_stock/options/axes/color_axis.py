from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts_core.options.axes.color_axis import ColorAxis as ColorAxisBase


class ColorAxis(ColorAxisBase):

    def __init__(self, **kwargs):
        self._max_range = None
        self._overscroll = None
        self._range = None
        self._resize = None

        self.max_range = kwargs.get('max_range', None)
        self.overscroll = kwargs.get('overscroll', None)
        self.range = kwargs.get('range', None)
        self.resize = kwargs.get('resize', None)

        super().__init__(**kwargs)

    @property
    def max_range(self) -> Optional[int | float | Decimal]:
        """Maximum range which can be set using the navigator's handles. Defaults to
        :obj:`None <python:None>`.

        .. note::

          This setting is the opposite of
          :meth:`.min_range <Highcharts_Stock.options.axes.color_axis.ColorAxis.min_range>`

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._max_range

    @max_range.setter
    def max_range(self, value):
        self._max_range = validators.numeric(value, allow_empty = True)

    @property
    def overscroll(self) -> Optional[int]:
        """Additional range on the right side of the x-axis. Works similar to
        :meth:`.max_padding <highcharts_stock.options.axes.color_axis.ColorAxis.max_padding>`, but
        value is set in milliseconds. Defaults to ``0``.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._overscroll

    @overscroll.setter
    def overscroll(self, value):
        self._overscroll = validators.integer(value,
                                              allow_empty = True,
                                              minimum = 0)

    @property
    def range(self) -> Optional[int | float | Decimal]:
        """The minimum range to display on this axis. Defaults to
        :obj:`None <python:None>`.

        .. note::

          The entire axis will not be allowed to span over a smaller interval than this.
          For example, for a datetime axis the main unit is milliseconds. If ``min_range``
          is set to ``3600000``, you can't zoom in more than to one hour.

          On a logarithmic axis, the unit for the range is the power. So a ``range`` of
          ``1`` means that the axis can be zoomed to 10-100, 100-1,000, 1,000-10,000 etc.

        .. note::

          For the x-axis, when :obj:`None <python:None>`, defaults to five times the
          smallest interval between any of the data points.

        .. caution::

          The :meth:`min_padding <highcharts_stock.options.axes.color_axis.ColorAxis.min_padding>`,
          :meth:`max_padding <highcharts_stock.options.axes.color_axis.ColorAxis.max_padding>`,
          :meth:`start_on_tick <highcharts_stock.options.axes.color_axis.ColorAxis.start_on_tick>`,
          and :meth:`end_on_tick <highcharts_stock.options.axes.color_axis.ColorAxis.end_on_tick>`
          settings also affect how the extremes of the axis are computed.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._range

    @range.setter
    def range(self, value):
        self._range = validators.numeric(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'accessibility': as_dict.get('accessibility', None),
            'angle': as_dict.get('angle', None),
            'ceiling': as_dict.get('ceiling', None),
            'class_name': as_dict.get('className', None),
            'end_on_tick': as_dict.get('endOnTick', None),
            'events': as_dict.get('events', None),
            'floor': as_dict.get('floor', None),
            'grid_line_color': as_dict.get('gridLineColor', None),
            'grid_line_dash_style': as_dict.get('gridLineDashStyle', None),
            'grid_line_interpolation': as_dict.get('gridLineInterpolation', None),
            'grid_line_width': as_dict.get('gridLineWidth', None),
            'grid_z_index': as_dict.get('gridZIndex', None),
            'id': as_dict.get('id', None),
            'labels': as_dict.get('labels', None),
            'margin': as_dict.get('margin', None),
            'max': as_dict.get('max', None),
            'max_padding': as_dict.get('maxPadding', None),
            'min': as_dict.get('min', None),
            'minor_grid_line_color': as_dict.get('minorGridLineColor', None),
            'minor_grid_line_dash_style': as_dict.get('minorGridLineDashStyle', None),
            'minor_grid_line_width': as_dict.get('minorGridLineWidth', None),
            'minor_tick_color': as_dict.get('minorTickColor', None),
            'minor_tick_interval': as_dict.get('minorTickInterval', None),
            'minor_tick_length': as_dict.get('minorTickLength', None),
            'minor_tick_position': as_dict.get('minorTickPosition', None),
            'minor_ticks': as_dict.get('minorTicks', None),
            'minor_tick_width': as_dict.get('minorTickWidth', None),
            'min_padding': as_dict.get('minPadding', None),
            'panning_enabled': as_dict.get('panningEnabled', None),
            'reversed': as_dict.get('reversed', None),
            'show_first_label': as_dict.get('showFirstLabel', None),
            'show_last_label': as_dict.get('showLastLabel', None),
            'soft_max': as_dict.get('softMax', None),
            'soft_min': as_dict.get('softMin', None),
            'start_of_week': as_dict.get('startOfWeek', None),
            'start_on_tick': as_dict.get('startOnTick', None),
            'tick_amount': as_dict.get('tickAmount', None),
            'tick_color': as_dict.get('tickColor', None),
            'tick_interval': as_dict.get('tickInterval', None),
            'tick_length': as_dict.get('tickLength', None),
            'tickmark_placement': as_dict.get('tickmarkPlacement', None),
            'tick_pixel_interval': as_dict.get('tickPixelInterval', None),
            'tick_position': as_dict.get('tickPosition', None),
            'tick_positioner': as_dict.get('tickPositioner', None),
            'tick_positions': as_dict.get('tickPositions', None),
            'tick_width': as_dict.get('tickWidth', None),
            'type': as_dict.get('type', None),
            'unique_names': as_dict.get('uniqueNames', None),
            'units': as_dict.get('units', None),
            'visible': as_dict.get('visible', None),
            'z_index': as_dict.get('zIndex', None),

            'data_class_color': as_dict.get('dataClassColor', None),
            'data_classes': as_dict.get('dataClasses', None),
            'layout': as_dict.get('layout', None),
            'line_color': as_dict.get('lineColor', None),
            'marker': as_dict.get('marker', None),
            'max_color': as_dict.get('maxColor', None),
            'min_color': as_dict.get('minColor', None),
            'show_in_legend': as_dict.get('showInLegend', None),
            'stops': as_dict.get('stops', None),

            'crosshair': as_dict.get('crosshair', None),
            'height': as_dict.get('height', None),
            'left': as_dict.get('left', None),
            'line_width': as_dict.get('lineWidth', None),
            'show_empty': as_dict.get('showEmpty', None),
            'top': as_dict.get('top', None),
            'width': as_dict.get('width', None),

            'stack_labels': as_dict.get('stackLabels', None),
            'tooltip_value_format': as_dict.get('tooltipValueFormat', None),

            'max_range': as_dict.get('maxRange', None),
            'overscroll': as_dict.get('overscroll', None),
            'range': as_dict.get('range', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'maxRange': self.max_range,
            'overscroll': self.overscroll,
            'range': self.range,
        }

        parent_as_dict = super()._to_untrimmed_dict(in_cls = in_cls)
        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed

from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts_core.options.axes.y_axis import YAxis as YAxisBase

from highcharts_stock import errors
from highcharts_stock.decorators import class_sensitive
from highcharts_stock.options.axes.resize import ResizeOptions
from highcharts_stock.options.scrollbar import Scrollbar


class YAxis(YAxisBase):

    def __init__(self, **kwargs):
        self._max_length = None
        self._max_range = None
        self._min_length = None
        self._range = None
        self._resize = None
        self._scrollbar = None

        self.max_length = kwargs.get('max_length', None)
        self.max_range = kwargs.get('max_range', None)
        self.min_length = kwargs.get('min_length', None)
        self.range = kwargs.get('range', None)
        self.resize = kwargs.get('resize', None)
        self.scrollbar = kwargs.get('scrollbar', None)

        super().__init__(**kwargs)

    @property
    def max_length(self) -> Optional[str | int | float | Decimal]:
        """Maximum size of a resizable axis, expressed either as a percentage of the plot
        area in a string or in pixels as a number. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`str <python:str>` or :class:`int <python:int>` or
          :obj:`None <python:None>`
        """
        return self._max_length

    @max_length.setter
    def max_length(self, value):
        if not value:
            self._max_length = None
        else:
            try:
                value = validators.string(value)
                if '%' not in value:
                    raise errors.HighchartsValueError('max_length accepts strings as '
                                                      'a percentage of plot area. No '
                                                      '"%" character found.')
                self._max_length = value
            except (TypeError):
                self._max_length = validators.numeric(value,
                                                      allow_empty = True,
                                                      minimum = 0)

    @property
    def max_range(self) -> Optional[int | float | Decimal]:
        """Maximum range which can be set using the navigator's handles. Defaults to
        :obj:`None <python:None>`.

        .. note::

          This setting is the opposite of
          :meth:`.min_range <Highcharts_Stock.options.axes.y_axis.YAxis.min_range>`

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._max_range

    @max_range.setter
    def max_range(self, value):
        self._max_range = validators.numeric(value, allow_empty = True)

    @property
    def min_length(self) -> Optional[str | int | float | Decimal]:
        """Minimum size of a resizable axis, expressed either as a percentage of the plot
        area in a string or in pixels as a number. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`str <python:str>` or :class:`int <python:int>` or
          :obj:`None <python:None>`
        """
        return self._min_length

    @min_length.setter
    def min_length(self, value):
        if not value:
            self._min_length = None
        else:
            try:
                value = validators.string(value)
                if '%' not in value:
                    raise errors.HighchartsValueError('min_length accepts strings as '
                                                      'a percentage of plot area. No '
                                                      '"%" character found.')
                self._min_length = value
            except (TypeError):
                self._min_length = validators.numeric(value,
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

          The :meth:`min_padding <highcharts_stock.options.axes.y_axis.YAxis.min_padding>`,
          :meth:`max_padding <highcharts_stock.options.axes.y_axis.YAxis.max_padding>`,
          :meth:`start_on_tick <highcharts_stock.options.axes.y_axis.YAxis.start_on_tick>`,
          and :meth:`end_on_tick <highcharts_stock.options.axes.y_axis.YAxis.end_on_tick>`
          settings also affect how the extremes of the axis are computed.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._range

    @range.setter
    def range(self, value):
        self._range = validators.numeric(value, allow_empty = True)

    @property
    def resize(self) -> Optional[ResizeOptions]:
        """Options for axis resizing. Defaults to :obj:`None <python:None>`.

        .. note:

          It adds a thick line between panes which the user can drag in order to resize
          the panes.

        :rtype: :class:`ResizeOptions <highcharts_stock.options.axes.resize.ResizeOptions>`
          or :obj:`None <python:None>`
        """
        return self._resize

    @resize.setter
    @class_sensitive(ResizeOptions)
    def resize(self, value):
        self._resize = value

    @property
    def scrollbar(self) -> Optional[Scrollbar]:
        """An optional scrollbar to display on the Y axis in response to limiting the
        minimum and maximum of the axis values. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`Scrollbar <highcharts_stock.options.axes.scrollbar.Scrollbar>` or
          :obj:`None <python:None>`
        """
        return self._scrollbar

    @scrollbar.setter
    @class_sensitive(Scrollbar)
    def scrollbar(self, value):
        self._scrollbar = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'accessibility': as_dict.get('accessibility', None),
            'align_ticks': as_dict.get('alignTicks', None),
            'allow_decimals': as_dict.get('allowDecimals', None),
            'alternate_grid_color': as_dict.get('alternateGridColor', None),
            'angle': as_dict.get('angle', None),
            'breaks': as_dict.get('breaks', None),
            'categories': as_dict.get('categories', None),
            'ceiling': as_dict.get('ceiling', None),
            'class_name': as_dict.get('className', None),
            'crossing': as_dict.get('crossing', None),
            'date_time_label_formats': as_dict.get('dateTimeLabelFormats', None),
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
            'linked_to': as_dict.get('linkedTo', None),
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
            'min_range': as_dict.get('minRange', None),
            'min_tick_interval': as_dict.get('minTickInterval', None),
            'offset': as_dict.get('offset', None),
            'opposite': as_dict.get('opposite', None),
            'pane': as_dict.get('pane', None),
            'panning_enabled': as_dict.get('panningEnabled', None),
            'plot_bands': as_dict.get('plotBands', None),
            'plot_lines': as_dict.get('plotLines', None),
            'reversed': as_dict.get('reversed', None),
            'reversed_stacks': as_dict.get('reversedStacks', None),
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
            'title': as_dict.get('title', None),
            'type': as_dict.get('type', None),
            'unique_names': as_dict.get('uniqueNames', None),
            'units': as_dict.get('units', None),
            'visible': as_dict.get('visible', None),
            'z_index': as_dict.get('zIndex', None),
            'zoom_enabled': as_dict.get('zoomEnabled', None),

            'crosshair': as_dict.get('crosshair', None),
            'height': as_dict.get('height', None),
            'left': as_dict.get('left', None),
            'line_color': as_dict.get('lineColor', None),
            'line_width': as_dict.get('lineWidth', None),
            'show_empty': as_dict.get('showEmpty', None),
            'top': as_dict.get('top', None),
            'width': as_dict.get('width', None),

            'max_color': as_dict.get('maxColor', None),
            'min_color': as_dict.get('minColor', None),
            'stack_labels': as_dict.get('stackLabels', None),
            'stops': as_dict.get('stops', None),
            'tooltip_value_format': as_dict.get('tooltipValueFormat', None),

            'max_length': as_dict.get('maxLength', None),
            'max_range': as_dict.get('maxRange', None),
            'min_length': as_dict.get('minLength', None),
            'range': as_dict.get('range', None),
            'resize': as_dict.get('resize', None),
            'scrollbar': as_dict.get('scrollbar', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'maxLength': self.max_length,
            'maxRange': self.max_range,
            'minLength': self.min_length,
            'range': self.range,
            'resize': self.resize,
            'scrollbar': self.scrollbar,
        }

        parent_as_dict = super()._to_untrimmed_dict(in_cls = in_cls)
        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed

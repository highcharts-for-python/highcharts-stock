from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts_core import errors
from highcharts_core.decorators import class_sensitive
from highcharts_core.utility_classes.gradients import Gradient
from highcharts_core.utility_classes.patterns import Pattern
from highcharts_core.options.plot_options.drag_drop import DragDropOptions
from highcharts_core.options.plot_options.series import SeriesBaseOptions as SeriesBase
from highcharts_core.utility_functions import mro__to_untrimmed_dict

from highcharts_stock.options.plot_options.base import NonIndicatorOptions


class SeriesBaseOptions(SeriesBase, NonIndicatorOptions):
    """General options to apply to all series types."""

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


class SeriesOptions(SeriesBaseOptions):
    """General options to apply to all (core) series types."""

    def __init__(self, **kwargs):
        self._color_axis = None
        self._connect_ends = None
        self._drag_drop = None
        self._negative_color = None
        self._point_interval = None
        self._point_interval_unit = None
        self._point_placement = None
        self._point_start = None
        self._stacking = None

        self.color_axis = kwargs.get('color_axis', None)
        self.connect_ends = kwargs.get('connect_ends', None)
        self.drag_drop = kwargs.get('drag_drop', None)
        self.negative_color = kwargs.get('negative_color', None)
        self.point_interval = kwargs.get('point_interval', None)
        self.point_interval_unit = kwargs.get('point_interval_unit', None)
        self.point_placement = kwargs.get('point_placement', None)
        self.point_start = kwargs.get('point_start', None)
        self.stacking = kwargs.get('stacking', None)

        super().__init__(**kwargs)

    @property
    def color_axis(self) -> Optional[str | int | bool]:
        """When using dual or multiple color axes, this setting defines which
        :term:`color axis` the particular series is connected to. It refers to either the
        :meth:`ColorAxis.id` or the index of the axis in the :class:`ColorAxis` array,
        with ``0`` being the first. Set this option to ``False`` to prevent a series from
        connecting to the default color axis.

        Defaults to ``0``.

        :rtype: :obj:`None <python:None>` or :class:`str <python:str>` or
          :class:`int <python:int>` or :class:`bool <python:bool>`
        """
        return self._color_axis

    @color_axis.setter
    def color_axis(self, value):
        if value is None:
            self._color_axis = None
        elif value is False:
            self._color_axis = False
        else:
            try:
                self._color_axis = validators.string(value)
            except TypeError:
                self._color_axis = validators.integer(value,
                                                      minimum = 0)

    @property
    def connect_ends(self) -> Optional[bool]:
        """If ``True``, connect the ends of a line series plot across the extremes.
        Defaults to :obj:`None <python:None>`.

        .. warning::

          Applies to :term:`polar charts <polar chart>` only.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._connect_ends

    @connect_ends.setter
    def connect_ends(self, value):
        if value is None:
            self._connect_ends = None
        else:
            self._connect_ends = bool(value)

    @property
    def drag_drop(self) -> Optional[DragDropOptions]:
        """The draggable-points module allows points to be moved around or modified in the
        chart.

        In addition to the options mentioned under the dragDrop API structure, the module
        fires three (JavaScript) events:

          * ``point.dragStart``
          * ``point.drag``
          * ``point.drop``

        :rtype: :class:`DragDropOptions` or :obj:`None <python:None>`
        """
        return self._drag_drop

    @drag_drop.setter
    @class_sensitive(DragDropOptions)
    def drag_drop(self, value):
        self._drag_drop = value

    @property
    def negative_color(self) -> Optional[str | Gradient | Pattern]:
        """The color for the parts of the graph or points that are below the
        :meth:`AreaOptions.threshold`.

        .. note::

          :meth:`Zones <AreaOptions.zones>` take precedence over the negative color.
          Using ``negative_color`` is equivalent to applying a zone with value of 0.

        :rtype: :obj:`None <python:None>`, :class:`Gradient`, :class:`Pattern`, or
          :class:`str <python:str>`
        """
        return self._negative_color

    @negative_color.setter
    def negative_color(self, value):
        from highcharts_core import utility_functions
        self._negative_color = utility_functions.validate_color(value)

    @property
    def point_interval(self) -> Optional[int | float | Decimal]:
        """If no x values are given for the points in a series, ``point_interval`` defines
        the interval of the x values. Defaults to ``1``.

        For example, if a series contains one value every decade starting from year 0, set
        ``point_interval`` to ``10``. In true datetime axes, the ``point_interval`` is set
        in milliseconds.

        .. hint::

          ``point_interval`` can be also be combined with
          :meth:`point_interval_unit <AreaOptions.point_interval_unit>` to draw irregular
          time intervals.

        .. note::

          If combined with :meth:`relative_x_value <AreaOptions.relative_x_value>`, an x
          value can be set on each point, and the ``point_interval`` is added x times to
          the :meth:`point_start <AreaOptions.point_start>` setting.

        .. warning::

          This options applies to the series data, not the interval of the axis ticks,
          which is independent.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._point_interval

    @point_interval.setter
    def point_interval(self, value):
        self._point_interval = validators.numeric(value,
                                                  allow_empty = True,
                                                  minimum = 0)

    @property
    def point_interval_unit(self) -> Optional[str]:
        """On datetime series, this allows for setting the
        :meth:`point_interval <AreaOptions.point_interval>` to irregular time units, day,
        month, and year.

        A day is usually the same as 24 hours, but ``point_interval_unit`` also takes the
        DST crossover into consideration when dealing with local time.

        Combine this option with :meth:`point_interval <AreaOptions.point_interval>` to
        draw weeks, quarters, 6 month periods, 10 year periods, etc.

        .. warning::

          This options applies to the series data, not the interval of the axis ticks,
          which is independent.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._point_interval_unit

    @point_interval_unit.setter
    def point_interval_unit(self, value):
        self._point_interval_unit = validators.string(value, allow_empty = True)

    @property
    def point_placement(self) -> Optional[str | int | float | Decimal]:
        """Used to determine the placement of the point in relation to tick marks on the
        X axis. Defaults to :obj:`None <python:None>`, which behaves as undefined in
        :term:`cartesian charts`, and ``"between"`` in polar charts.

        Accepts possible values:

          * ``'on'`` - where the point will not create any padding of the X axis. In a
            polar column chart this means that the first column points directly
            north.
          * ``"between"`` - where the columns will be laid out between ticks. This is
            useful for example for visualising an amount between two points in time or in
            a certain sector of a polar chart.
          * a numeric value - where ``0`` is on the axis value, ``-0.5`` is between this
            value and the previous, and ``0.5`` is between this value and the next. Unlike
            the textual options, numeric point placement options won't affect axis
            padding.

        .. warning::

          Requires :meth:`point_range <AreaOptions.point_range>` to work. For
          column series this is computed, but for line-type series it needs to be set.

        .. note::

          For the xrange series type and gantt charts, if the Y axis is a category axis,
          the ``point_placement`` applies to the Y axis rather than the (typically
          datetime) X axis.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._point_placement

    @point_placement.setter
    def point_placement(self, value):
        if value is None:
            self._point_placement = None
        else:
            try:
                self._point_placement = validators.numeric(value,
                                                           minimum = -0.5,
                                                           maximum = 0.5)
            except (TypeError, ValueError):
                value = validators.string(value)
                value = value.lower()
                if value not in ['on', 'between']:
                    raise errors.HighchartsValueError(f'point_placement must be a number,'
                                                      f' "on", or "between". Was: '
                                                      f'{value}')
                self._point_placement = value

    @property
    def point_start(self) -> Optional[int | float | Decimal]:
        """If no x values are given for the points in a series, ``point_start`` defines
        on what value to start. For example, if a series contains one yearly value
        starting from 1945, set ``point_start`` to ``1945``. Defaults to ``0``.

        .. note::

          If combined with :meth:`relative_x_value <AreaOptions.relative_x_value>`, an x
          value can be set on each point. The x value from the point options is multiplied
          by :meth:`point_interval <AreaOptions.point_interval>` and added to
          ``point_start`` to produce a modified x value.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._point_start

    @point_start.setter
    def point_start(self, value):
        self._point_start = validators.numeric(value, allow_empty = True)

    @property
    def stacking(self) -> Optional[str]:
        """Whether to stack the values of each series on top of each other. Defaults to
        :obj:`None <python:None>`.

        Acceptable values are:

          * :obj:`None <python:None>` to disable stacking,
          * ``"normal"`` to stack by value or
          * ``"percent"``
          * ``'stream'`` (for streamgraph series type only)
          * ``'overlap'`` (for waterfall series type only)

        .. note::

          When stacking is enabled, data must be sorted in ascending X order.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._stacking

    @stacking.setter
    def stacking(self, value):
        if not value:
            self._stacking = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['normal', 'percent', 'stream', 'overlap']:
                raise errors.HighchartsValueError(f'stacking expects a valid stacking '
                                                  f'value. However, received: {value}')
            self._stacking = value

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
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'colorAxis': self.color_axis,
            'connectEnds': self.connect_ends,
            'dragDrop': self.drag_drop,
            'negativeColor': self.negative_color,
            'pointInterval': self.point_interval,
            'pointIntervalUnit': self.point_interval_unit,
            'pointPlacement': self.point_placement,
            'pointStart': self.point_start,
            'stacking': self.stacking,
        }
        parent_as_dict = mro__to_untrimmed_dict(self, in_cls = in_cls) or {}

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed

from typing import Optional, List
from decimal import Decimal

from validator_collection import validators

from highcharts_core.options.plot_options.bar import SeriesOptions as SeriesBase
from highcharts_core.utility_classes.gradients import Gradient
from highcharts_core.utility_classes.patterns import Pattern
from highcharts_core.utility_functions import mro__to_untrimmed_dict, validate_color

from highcharts_stock import errors
from highcharts_stock.options.plot_options.base import NonIndicatorOptions


class FlagsOptions(SeriesBase, NonIndicatorOptions):
    """Flags are used to mark events in **Highcharts Stock for Python**. They can be added
    on the timeline, or attached to a specific series.

    .. figure:: ../../../_static/flags-example.png
      :alt: Flags Example
      :align: center

    """

    def __init__(self, **kwargs):
        self._allow_overlap_x = None
        self._center_in_category = None
        self._colors = None
        self._fill_color = None
        self._group_padding = None
        self._grouping = None
        self._height = None
        self._line_color = None
        self._max_point_width = None
        self._min_point_length = None
        self._on_key = None
        self._on_series = None
        self._shape = None
        self._stack_distance = None
        self._style = None
        self._text_align = None
        self._title = None
        self._use_html = None
        self._width = None
        self._y = None

        self.allow_overlap_x = kwargs.get('allow_overlap_x', None)
        self.center_in_category = kwargs.get('center_in_category', None)
        self.colors = kwargs.get('colors', None)
        self.fill_color = kwargs.get('fill_color', None)
        self.group_padding = kwargs.get('group_padding', None)
        self.grouping = kwargs.get('grouping', None)
        self.height = kwargs.get('height', None)
        self.line_color = kwargs.get('line_color', None)
        self.max_point_width = kwargs.get('max_point_width', None)
        self.min_point_length = kwargs.get('min_point_length', None)
        self.on_key = kwargs.get('on_key', None)
        self.on_series = kwargs.get('on_series', None)
        self.shape = kwargs.get('shape', None)
        self.stack_distance = kwargs.get('stack_distance', None)
        self.style = kwargs.get('style', None)
        self.text_align = kwargs.get('text_align', None)
        self.title = kwargs.get('title', None)
        self.use_html = kwargs.get('use_html', None)
        self.width = kwargs.get('width', None)
        self.y = kwargs.get('y', None)

        super().__init__(**kwargs)

    @property
    def allow_overlap_x(self) -> Optional[bool]:
        """If ``True``, the flags are allowed to overlap sideways. If ``False``, the flags
        are moved sideways using an algorithm that seeks to place every flag as close as
        possible to its original position. Defaults to ``False``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._allow_overlap_x

    @allow_overlap_x.setter
    def allow_overlap_x(self, value):
        if value is None:
            self._allow_overlap_x = None
        else:
            self._allow_overlap_x = bool(value)

    @property
    def center_in_category(self) -> Optional[bool]:
        """If ``True``, the columns will center in the category, ignoring null or missing
        points. When ``False``, space will be reserved for null or missing points.
        Defaults to ``False``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._center_in_category

    @center_in_category.setter
    def center_in_category(self, value):
        if value is None:
            self._center_in_category = None
        else:
            self._center_in_category = bool(value)

    @property
    def colors(self) -> Optional[List[str | Gradient | Pattern]]:
        """A series-specific or series type-specific color set to apply instead of the
        global colors when :meth:`FlagsOptions.color_by_point` is ``True``.

        :rtype: :class:`list <python:list>` of :class:`str <python:str>`,
          :class:`Gradient`, or :class:`Pattern` OR :obj:`None <python:None>`
        """
        return self._colors

    @colors.setter
    def colors(self, value):
        if not value:
            self._colors = None
        else:
            value = validators.iterable(value)
            self._colors = [validate_color(x) for x in value]

    @property
    def fill_color(self) -> Optional[str | Gradient | Pattern]:
        """Fill color or gradient for the flag. Defaults to ``'#ffffff'``.

        :rtype: :obj:`None <python:None>`, :class:`Gradient`, :class:`Pattern`, or
          :class:`EnforcedNullType`
        """
        return self._fill_color

    @fill_color.setter
    def fill_color(self, value):
        self._fill_color = validate_color(value)

    @property
    def grouping(self) -> Optional[bool]:
        """If ``True``, groups non-stacked columns. If ``False``, renders them
        independent of each other. Non-grouped columns will be laid out individually and
        overlap each other.

        Defaults to ``True``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._grouping

    @grouping.setter
    def grouping(self, value):
        if value is None:
            self._grouping = None
        else:
            self._grouping = bool(value)

    @property
    def group_padding(self) -> Optional[int | float | Decimal]:
        """Padding between each value group, in x axis units. Defaults to ``0.2``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._group_padding

    @group_padding.setter
    def group_padding(self, value):
        self._group_padding = validators.numeric(value,
                                                 allow_empty = True,
                                                 minimum = 0)

    @property
    def height(self) -> Optional[int | float | Decimal]:
        """Fixed height of the flag's shape, expressed in pixels. If
        :obj:`None <python:None>`, height is autocalculated according to the flag's title.
        Defaults ot :obj:`None <python:None>`

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._height

    @height.setter
    def height(self, value):
        self._height = validators.numeric(value, allow_empty = True)

    @property
    def line_color(self) -> Optional[str | Gradient | Pattern]:
        """The color of the line/border of the flag. Defaults to ``'#000000'``.

        :rtype: :obj:`None <python:None>`, :class:`Gradient`, :class:`Pattern`, or
          :class:`str <python:str>`
        """
        return self._line_color

    @line_color.setter
    def line_color(self, value):
        self._line_color = validate_color(value)

    @property
    def max_point_width(self) -> Optional[int | float | Decimal]:
        """The maximum allowed pixel width for a column, translated to the height of a bar
        in a bar chart. This prevents the columns from becoming too wide when there is a
        small number of points in the chart. Defaults to :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._max_point_width

    @max_point_width.setter
    def max_point_width(self, value):
        self._max_point_width = validators.numeric(value,
                                                   allow_empty = True,
                                                   minimum = 0)

    @property
    def min_point_length(self) -> Optional[int | float | Decimal]:
        """The minimal height for a column or width for a bar. Defaults to ``0``.

        By default, ``0`` values are not shown. To visualize a ``0`` (or close to zero)
        point, set the minimal point length to a pixel value like ``3``.

        .. warning::

          In stacked column charts, ``min_point_length`` might not be respected for
          tightly packed values.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._min_point_length

    @min_point_length.setter
    def min_point_length(self, value):
        self._min_point_length = validators.numeric(value,
                                                    allow_empty = True,
                                                    minimum = 0)

    @property
    def on_key(self) -> Optional[str]:
        """If the flag is placed on a :term:`series`, on what point key to place it. Line
        and column :term:`series` have one key: ``'y'``. In range or OHLC-type series,
        however, the flag can optionally be placed on the ``'open'``, ``'high'``,
        ``'low'``, or ``'close'`` key. Defaults to ``'y'``.

        Accepts:

          * ``'y'`` (default)
          * ``'open'``
          * ``'high'``
          * ``'low'``
          * ``'close'``

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._on_key

    @on_key.setter
    def on_key(self, value):
        if not value:
            self._on_key = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['y', 'open', 'high', 'low', 'close']:
                raise errors.HighchartsValueError(f'on_key expects either "y", "open", '
                                                  f'"high", "low", or "close". Received: '
                                                  f'"{value}"')

            self._on_key = value

    @property
    def on_series(self) -> Optional[str]:
        """The id of another series in the chart that the flags are projected on. Defaults
        to :obj:`None <python:None>`.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._on_series

    @on_series.setter
    def on_series(self, value):
        self._on_series = validators.string(value, allow_empty = True)

    @property
    def shape(self) -> Optional[str]:
        """The shape of the marker. Defaults to ``'flag'``.

        .. note::

          Individual shapes can also be set for each point.

        Accepts:

          * ``'flag'``
          * ``'circlepin'``
          * ``'squarepin'``, or
          * an image of the format ``'url(/path-to-image.jpg)'``.

        :returns: The shape to use for the flags.
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._shape

    @shape.setter
    def shape(self, value):
        if not value:
            self._shape = None
        else:
            value = validators.string(value, allow_empty = False)
            value = value.lower()
            if value not in ['flag', 'circlepin', 'squarepin']:
                if not value.startswith('url(') or not value.endswith(')'):
                    raise errors.HighchartsValueError(f'shape expects a supported flag '
                                                      f'shape. Was: {value}')

            self._shape = value

    @property
    def stack_distance(self) -> Optional[int | float | Decimal]:
        """When multiple flags in the same series fall on the same value, this number
        determines the vertical offset between them. Defaults to ``12``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._stack_distance

    @stack_distance.setter
    def stack_distance(self, value):
        self._stack_distance = value

    @property
    def style(self) -> Optional[str]:
        """The text styles of the flag. Defaults to
        ``'{"fontSize": "11px", "fontWeight": "bold"}'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._style

    @style.setter
    def style(self, value):
        self._style = validators.string(value, allow_empty = True)

    @property
    def text_align(self) -> Optional[str]:
        """The text alignment for the text inside the flag. Defaults to ``'center'``.

        Possible values are:

          * ``'left'``
          * ``'center'``
          * ``'right'``

        :rtype: :class:`str <python:str>`
        """
        return self._text_align

    @text_align.setter
    def text_align(self, value):
        if not value:
            self._text_align = None
        else:
            value = validators.string(value, allow_empty = False)
            value = value.lower()
            if value not in ['left', 'center', 'right']:
                raise errors.HighchartsValueError(f'text_align must be either "left", '
                                                  f'"center", or "right". Was: {value}')

            self._text_align = value

    @property
    def title(self) -> Optional[str]:
        """The text to display on each flag. Defaults to ``'A'``.

        .. note::

          This can be defined on series level, or individually for each point.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._title

    @title.setter
    def title(self, value):
        self._title = validators.string(value, allow_empty = True)

    @property
    def use_html(self) -> Optional[bool]:
        """If ``True``, will use HTML to render the label. If ``False``, will
        use SVG or WebGL as applicable.

        Defaults to ``False``.

        :returns: Flag indicating whether to render data labels using HTML.
        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._use_html

    @use_html.setter
    def use_html(self, value):
        if value is None:
            self._use_html = None
        else:
            self._use_html = bool(value)

    @property
    def width(self) -> Optional[int | float | Decimal]:
        """Fixed width of the flag's shape, expressed in pixels. If
        :obj:`None <python:None>`, width is autocalculated according to the flag's title.
        Defaults ot :obj:`None <python:None>`

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._width

    @width.setter
    def width(self, value):
        self._width = validators.numeric(value, allow_empty = True)

    @property
    def y(self) -> Optional[int | float | Decimal]:
        """The y-position of the top left corner of the flag, relative to either the
        x-axis or (if
        :meth:`.on_series <highcharts_stock.options.plot_options.flags.FlagsOptions.on_series>`
        is specified) the series. Defaults to ``-30``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._y

    @y.setter
    def y(self, value):
        self._y = validators.numeric(value, allow_empty = True)

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
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'allowOverlapX': self.allow_overlap_x,
            'centerInCategory': self.center_in_category,
            'colors': self.colors,
            'fillColor': self.fill_color,
            'groupPadding': self.group_padding,
            'grouping': self.grouping,
            'height': self.height,
            'lineColor': self.line_color,
            'maxPointWidth': self.max_point_width,
            'minPointLength': self.min_point_length,
            'onKey': self.on_key,
            'onSeries': self.on_series,
            'shape': self.shape,
            'stackDistance': self.stack_distance,
            'style': self.style,
            'textAlign': self.text_align,
            'title': self.title,
            'useHTML': self.use_html,
            'width': self.width,
            'y': self.y,
        }
        parent_as_dict = mro__to_untrimmed_dict(self, in_cls = in_cls) or {}

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed

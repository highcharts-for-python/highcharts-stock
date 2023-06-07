from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts_stock.metaclasses import HighchartsMeta
from highcharts_stock.utility_classes.gradients import Gradient
from highcharts_stock.utility_classes.patterns import Pattern
from highcharts_stock.utility_functions import validate_color


class Scrollbar(HighchartsMeta):
    """The scrollbar is a means of panning over the X axis of a stock chart.

    .. tip::

      Scrollbars can also be applied to other types of axes.

    .. tip::

      Another approach to scrollable charts is the
      :meth:`ChartOptions.scrollable_plot_area <highcharts_stock.options.chart.ChartOptions.scrollable_plot_area>`
      setting that is especially suitable for simpler charts on mobile.

    """

    def __init__(self, **kwargs):
        self._bar_background_color = None
        self._bar_border_color = None
        self._bar_border_radius = None
        self._bar_border_width = None
        self._button_arrow_color = None
        self._button_background_color = None
        self._button_border_color = None
        self._button_border_radius = None
        self._button_border_width = None
        self._buttons_enabled = None
        self._enabled = None
        self._height = None
        self._live_redraw = None
        self._margin = None
        self._min_width = None
        self._rifle_color = None
        self._show_full = None
        self._track_background_color = None
        self._track_border_color = None
        self._track_border_radius = None
        self._track_border_width = None
        self._z_index = None

        self.bar_background_color = kwargs.get('bar_background_color', None)
        self.bar_border_color = kwargs.get('bar_border_color', None)
        self.bar_border_radius = kwargs.get('bar_border_radius', None)
        self.bar_border_width = kwargs.get('bar_border_width', None)
        self.button_arrow_color = kwargs.get('button_arrow_color', None)
        self.button_background_color = kwargs.get('button_background_color', None)
        self.button_border_color = kwargs.get('button_border_color', None)
        self.button_border_radius = kwargs.get('button_border_radius', None)
        self.button_border_width = kwargs.get('button_border_width', None)
        self.buttons_enabled = kwargs.get('buttons_enabled', None)
        self.enabled = kwargs.get('enabled', None)
        self.height = kwargs.get('height', None)
        self.live_redraw = kwargs.get('live_redraw', None)
        self.margin = kwargs.get('margin', None)
        self.min_width = kwargs.get('min_width', None)
        self.rifle_color = kwargs.get('rifle_color', None)
        self.show_full = kwargs.get('show_full', None)
        self.track_background_color = kwargs.get('track_background_color', None)
        self.track_border_color = kwargs.get('track_border_color', None)
        self.track_border_radius = kwargs.get('track_border_radius', None)
        self.track_border_width = kwargs.get('track_border_width', None)
        self.z_index = kwargs.get('z_index', None)

    @property
    def _dot_path(self) -> Optional[str]:
        """The dot-notation path to the options key for the current class.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return 'scrollbar'

    @property
    def bar_background_color(self) -> Optional[str | Gradient | Pattern]:
        """The backgorund color of the scrollbar itself. Defaults to
        ``'#cccccc'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._bar_background_color

    @bar_background_color.setter
    def bar_background_color(self, value):
        self._bar_background_color = validate_color(value)

    @property
    def bar_border_color(self) -> Optional[str | Gradient | Pattern]:
        """The color of scrollbar's border. Defaults to ``'#cccccc'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._bar_border_color

    @bar_border_color.setter
    def bar_border_color(self, value):
        self._bar_border_color = validate_color(value)

    @property
    def bar_border_radius(self) -> Optional[int | float | Decimal]:
        """The corner radius of the border surrounding the scrollbar. Defaults to
        ``0``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._bar_border_radius

    @bar_border_radius.setter
    def bar_border_radius(self, value):
        self._bar_border_radius = validators.numeric(value,
                                                     allow_empty = True,
                                                     minimum = 0)

    @property
    def bar_border_width(self) -> Optional[int | float | Decimal]:
        """The width of the border surrounding the scrollbar. Defaults to ``1``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._bar_border_width

    @bar_border_width.setter
    def bar_border_width(self, value):
        self._bar_border_width = validators.numeric(value,
                                                    allow_empty = True,
                                                    minimum = 0)

    @property
    def button_arrow_color(self) -> Optional[str | Gradient | Pattern]:
        """The color of the small arrow inside the scrollbar buttons. Defaults to
        ``'#333333'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._button_arrow_color

    @button_arrow_color.setter
    def button_arrow_color(self, value):
        self._button_arrow_color = validate_color(value)

    @property
    def button_background_color(self) -> Optional[str | Gradient | Pattern]:
        """The backgorund color of the scrollbar buttons. Defaults to
        ``'#e6e6e6'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._button_background_color

    @button_background_color.setter
    def button_background_color(self, value):
        self._button_background_color = validate_color(value)

    @property
    def button_border_color(self) -> Optional[str | Gradient | Pattern]:
        """The color of scrollbar buttons' border. Defaults to ``'#cccccc'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._button_border_color

    @button_border_color.setter
    def button_border_color(self, value):
        self._button_border_color = validate_color(value)

    @property
    def button_border_radius(self) -> Optional[int | float | Decimal]:
        """The corner radius of the border surrounding the scrollbar buttons. Defaults to
        ``0``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._button_border_radius

    @button_border_radius.setter
    def button_border_radius(self, value):
        self._button_border_radius = validators.numeric(value,
                                                        allow_empty = True,
                                                        minimum = 0)

    @property
    def button_border_width(self) -> Optional[int | float | Decimal]:
        """The width of the border surrounding the scrollbar buttons. Defaults to ``1``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._button_border_width

    @button_border_width.setter
    def button_border_width(self, value):
        self._button_border_width = validators.numeric(value,
                                                       allow_empty = True,
                                                       minimum = 0)

    @property
    def buttons_enabled(self) -> Optional[bool]:
        """If ``True``, will display buttons at the start/end of the scrollbar. Defaults to ``True``.
        
        .. versionadded:: Highcharts Stock for Python v.2.0.0 + Highcharts Stock (JS) v.11

        :rtype: :class:`bool <python:bool>`
        """
        return self._buttons_enabled

    @buttons_enabled.setter
    def buttons_enabled(self, value):
        if value is None:
            self._buttons_enabled = None
        else:
            self._buttons_enabled = bool(value)

    @property
    def enabled(self) -> Optional[bool]:
        """If ``True``, displays the scrollbar. If ``False``, does not display the
        scrollbar. Defaults to ``True``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        if value is None:
            self._enabled = None
        else:
            self._enabled = bool(value)

    @property
    def height(self) -> Optional[int | float | Decimal]:
        """The height of the scrollbar and the height/width of the scroll buttons (so that
        they are always square). If :obj:`None <python:None>`, defaults to ``20`` for
        touch devices and ``14`` for mouse devices. Defaults to :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._height

    @height.setter
    def height(self, value):
        self._height = validators.numeric(value,
                                          allow_empty = True,
                                          minimum = 0)

    @property
    def live_redraw(self) -> Optional[bool]:
        """If ``True``, redraws the main chart as the scrollbar or the navigator zoomed
        window is moved. If :obj:`None <python:None>`, defaults to ``True`` in modern
        browsers and ``False`` in legacy IE browsers and mobile devices. Defaults to
        :obj:`None <python:None>`.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._live_redraw

    @live_redraw.setter
    def live_redraw(self, value):
        if value is None:
            self._live_redraw = None
        else:
            self._live_redraw = bool(value)

    @property
    def margin(self) -> Optional[int | float | Decimal]:
        """The margin (in pixels) between the scrollbar and its axis when the scrollbar is
        applied directly to an axis. Defaults to ``10``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._margin

    @margin.setter
    def margin(self, value):
        self._margin = validators.numeric(value, allow_empty = True)

    @property
    def min_width(self) -> Optional[int | float | Decimal]:
        """The minimum width of the scrollbar. Defaults to ``6``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._min_width

    @min_width.setter
    def min_width(self, value):
        self._min_width = validators.numeric(value, allow_empty = True)

    @property
    def rifle_color(self) -> Optional[str | Gradient | Pattern]:
        """The color of the small rifles in the middle of the scrollbar. Defaults to
        ``'#333333'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._rifle_color

    @rifle_color.setter
    def rifle_color(self, value):
        self._rifle_color = validate_color(value)

    @property
    def show_full(self) -> Optional[bool]:
        """If ``True``, will show the scrollbar even when zoomed content is scrolled out
        to the its fullest extent. If ``False``, will hide the scrollbar when content
        is zoomed out all the way. Defaults to ``True``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._show_full

    @show_full.setter
    def show_full(self, value):
        if value is None:
            self._show_full = None
        else:
            self._show_full = bool(value)

    @property
    def track_background_color(self) -> Optional[str | Gradient | Pattern]:
        """The background color of the scrollbar track. Defaults to
        ``'#f2f2f2'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._track_background_color

    @track_background_color.setter
    def track_background_color(self, value):
        self._track_background_color = validate_color(value)

    @property
    def track_border_color(self) -> Optional[str | Gradient | Pattern]:
        """The color of scrollbar track's border. Defaults to ``'#f2f2f2'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._track_border_color

    @track_border_color.setter
    def track_border_color(self, value):
        self._track_border_color = validate_color(value)

    @property
    def track_border_radius(self) -> Optional[int | float | Decimal]:
        """The corner radius of the border surrounding the scrollbar track. Defaults to
        ``0``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._track_border_radius

    @track_border_radius.setter
    def track_border_radius(self, value):
        self._track_border_radius = validators.numeric(value,
                                                       allow_empty = True,
                                                       minimum = 0)

    @property
    def track_border_width(self) -> Optional[int | float | Decimal]:
        """The width of the border surrounding the scrollbar track. Defaults to ``1``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._track_border_width

    @track_border_width.setter
    def track_border_width(self, value):
        self._track_border_width = validators.numeric(value,
                                                      allow_empty = True,
                                                      minimum = 0)

    @property
    def z_index(self) -> Optional[int]:
        """The Z-Index for the scrollbar. Defaults to ``3``.

        :returns: The z-index for the scrollbar.
        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._z_index

    @z_index.setter
    def z_index(self, value):
        self._z_index = validators.integer(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'bar_background_color': as_dict.get('barBackgroundColor', None),
            'bar_border_color': as_dict.get('barBorderColor', None),
            'bar_border_radius': as_dict.get('barBorderRadius', None),
            'bar_border_width': as_dict.get('barBorderWidth', None),
            'button_arrow_color': as_dict.get('buttonArrowColor', None),
            'button_background_color': as_dict.get('buttonBackgroundColor', None),
            'button_border_color': as_dict.get('buttonBorderColor', None),
            'button_border_radius': as_dict.get('buttonBorderRadius', None),
            'button_border_width': as_dict.get('buttonBorderWidth', None),
            'buttons_enabled': as_dict.get('buttonsEnabled', None),
            'enabled': as_dict.get('enabled', None),
            'height': as_dict.get('height', None),
            'live_redraw': as_dict.get('liveRedraw', None),
            'margin': as_dict.get('margin', None),
            'min_width': as_dict.get('minWidth', None),
            'rifle_color': as_dict.get('rifleColor', None),
            'show_full': as_dict.get('showFull', None),
            'track_background_color': as_dict.get('trackBackgroundColor', None),
            'track_border_color': as_dict.get('trackBorderColor', None),
            'track_border_radius': as_dict.get('trackBorderRadius', None),
            'track_border_width': as_dict.get('trackBorderWidth', None),
            'z_index': as_dict.get('zIndex', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'barBackgroundColor': self.bar_background_color,
            'barBorderColor': self.bar_border_color,
            'barBorderRadius': self.bar_border_radius,
            'barBorderWidth': self.bar_border_width,
            'buttonArrowColor': self.button_arrow_color,
            'buttonBackgroundColor': self.button_background_color,
            'buttonBorderColor': self.button_border_color,
            'buttonBorderRadius': self.button_border_radius,
            'buttonBorderWidth': self.button_border_width,
            'buttonsEnabled': self.buttons_enabled,
            'enabled': self.enabled,
            'height': self.height,
            'liveRedraw': self.live_redraw,
            'margin': self.margin,
            'minWidth': self.min_width,
            'rifleColor': self.rifle_color,
            'showFull': self.show_full,
            'trackBackgroundColor': self.track_background_color,
            'trackBorderColor': self.track_border_color,
            'trackBorderRadius': self.track_border_radius,
            'trackBorderWidth': self.track_border_width,
            'zIndex': self.z_index,
        }

        return untrimmed

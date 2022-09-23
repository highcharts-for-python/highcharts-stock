from typing import Optional, List
from decimal import Decimal

from validator_collection import validators


from highcharts_stock import constants, errors
from highcharts_stock.decorators import class_sensitive
from highcharts_stock.metaclasses import HighchartsMeta


class ControlledAxis(HighchartsMeta):
    """Axes that are controlled by the control line of the axis."""

    def __init__(self, **kwargs):
        self._next = None
        self._prev = None

        self.next = kwargs.get('next', None)
        self.prev = kwargs.get('prev', None)

    @property
    def next(self) -> Optional[List[int | str]]:
        """Array of axes that should move out of the way of resizing being done for the
        current axis. If not set, the next axis will be used. If
        :obj:`None <python:None>`, defaults to an empty array.

        :rtype: :class:`list <python:list>` of :class:`int <python:int>` or
          :class:`str <python:str>`, or :class:`None <python:None>`
        """
        return self._next

    @next.setter
    def next(self, value):
        if value is None:
            self._next = None
        else:
            value = validators.iterable(value, allow_empty = True)
            processed_value = []
            for item in value:
                try:
                    item = validators.integer(item)
                except (ValueError, TypeError):
                    item = validators.string(item)

                processed_value.append(item)

            self._next = [x for x in processed_value]

    @property
    def prev(self) -> Optional[List[int | str]]:
        """Array of axes that should move with the current axis during resizing.

        :rtype: :class:`list <python:list>` of :class:`int <python:int>` or
          :class:`str <python:str>`, or :class:`None <python:None>`
        """
        return self._prev

    @prev.setter
    def prev(self, value):
        if value is None:
            self._prev = None
        else:
            value = validators.iterable(value, allow_empty = True)
            processed_value = []
            for item in value:
                try:
                    item = validators.integer(item)
                except (ValueError, TypeError):
                    item = validators.string(item)

                processed_value.append(item)

            self._prev = [x for x in processed_value]

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'next': as_dict.get('next', None),
            'prev': as_dict.get('prev', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'next': self.next,
            'prev': self.prev,
        }

        return untrimmed


class ResizeOptions(HighchartsMeta):
    """Options for axis resizing.

    .. note::

      It adds a thick line between panes which the user can drag in order to resize the
      panes.

    """

    def __init__(self, **kwargs):
        self._controlled_axis = None
        self._cursor = None
        self._enabled = None
        self._line_color = None
        self._line_dash_style = None
        self._line_width = None
        self._x = None
        self._y = None

        self.controlled_axis = kwargs.get('controlled_axis', None)
        self.cursor = kwargs.get('cursor', None)
        self.enabled = kwargs.get('enabled', None)
        self.line_color = kwargs.get('line_color', None)
        self.line_dash_style = kwargs.get('line_dash_style', None)
        self.line_width = kwargs.get('line_width', None)
        self.x = kwargs.get('x', None)
        self.y = kwargs.get('y', None)

    @property
    def controlled_axis(self) -> Optional[ControlledAxis]:
        """Axes that are controlled by the control line of the axis.

        :rtype: :class:`ControlledAxis` or :obj:`None <python:None>`
        """
        return self._controlled_axis

    @controlled_axis.setter
    @class_sensitive(ControlledAxis)
    def controlled_axis(self, value):
        self._controlled_axis = value

    @property
    def cursor(self) -> Optional[str]:
        """Cursor style for the control line. Defaults to ``'ns-resize'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._cursor

    @cursor.setter
    def cursor(self, value):
        self._cursor = validators.string(value, allow_empty = True)

    @property
    def enabled(self) -> Optional[bool]:
        """If ``True``, enable resizing of the axis by dragging. Defaults to ``False``.

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
    def line_color(self) -> Optional[str]:
        """Color of the control line. Defaults to ``'#cccccc'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._line_color

    @line_color.setter
    def line_color(self, value):
        self._line_color = validators.string(value, allow_empty = True)

    @property
    def line_dash_style(self) -> Optional[str]:
        """Name of the dash style to use for the control line. Defaults to ``'Solid'``.

        Accepts the following values:

          * ``'Solid'``
          * ``'ShortDash'``
          * ``'ShortDot'``
          * ``'ShortDashDot'``
          * ``'ShortDashDotDot'``
          * ``'Dot'``
          * ``'Dash'``
          * ``'LongDash'``
          * ``'DashDot'``
          * ``'LongDashDot'``
          * ``'LongDashDotDot'``

        :returns: The name of the dash style to apply to the control line.
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._line_dash_style

    @line_dash_style.setter
    def line_dash_style(self, value):
        value = validators.string(value, allow_empty = True)
        if not value:
            self._dash_style = None
        else:
            if value not in constants.SHAPES_ALLOWED_DASH_STYLES:
                raise errors.HighchartsValueError(f'dash_style expects a supported value.'
                                                  f' Received: {value}')
            self._line_dash_style = value

    @property
    def line_width(self) -> Optional[int | float | Decimal]:
        """Pixel width of the control line. Defaults to ``4``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._line_width

    @line_width.setter
    def line_width(self, value):
        self._line_width = validators.numeric(value,
                                              allow_empty = True,
                                              minimum = 0)

    @property
    def x(self) -> Optional[int | float | Decimal]:
        """Horizontal offset of the control line. Defaults to ``0``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._x

    @x.setter
    def x(self, value):
        self._x = validators.numeric(value, allow_empty = True)

    @property
    def y(self) -> Optional[int | float | Decimal]:
        """Vertical offset of the control line. Defaults to ``0``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._y

    @y.setter
    def y(self, value):
        self._y = validators.numeric(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'controlled_axis': as_dict.get('controlledAxis', None),
            'cursor': as_dict.get('cursor', None),
            'enabled': as_dict.get('enabled', None),
            'line_color': as_dict.get('lineColor', None),
            'line_dash_style': as_dict.get('lineDashStyle', None),
            'line_width': as_dict.get('lineWidth', None),
            'x': as_dict.get('x', None),
            'y': as_dict.get('y', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'controlledAxis': self.controlled_axis,
            'cursor': self.cursor,
            'enabled': self.enabled,
            'lineColor': self.line_color,
            'lineDashStyle': self.line_dash_style,
            'lineWidth': self.line_width,
            'x': self.x,
            'y': self.y,
        }

        return untrimmed

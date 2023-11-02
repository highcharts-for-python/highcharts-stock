from typing import Optional, List
from decimal import Decimal

from validator_collection import validators

from highcharts_core.decorators import class_sensitive
from highcharts_core.metaclasses import HighchartsMeta

from highcharts_stock import errors
from highcharts_stock.options.annotations.stock_tools.type_options.line import LineFillOnly, LineStrokeWidthStroke
from highcharts_stock.options.annotations.stock_tools.type_options.points import StockToolsPoint, StockToolsXPoint
from highcharts_stock.options.annotations.label_options import LabelOptions


class FibonacciTypeOptions(HighchartsMeta):
    """Additional options for :term:`fibonacci` annotations."""

    def __init__(self, **kwargs):
        self._background_colors = None
        self._height = None
        self._labels = None
        self._line = None
        self._line_color = None
        self._line_colors = None
        self._points = None
        self._x_axis = None
        self._y_axis = None
        self._reversed = None

        self.background_colors = kwargs.get('background_colors', None)
        self.height = kwargs.get('height', None)
        self.labels = kwargs.get('labels', None)
        self.line = kwargs.get('line', None)
        self.line_color = kwargs.get('line_color', None)
        self.line_colors = kwargs.get('line_colors', None)
        self.points = kwargs.get('points', None)
        self.x_axis = kwargs.get('x_axis', None)
        self.y_axis = kwargs.get('y_axis', None)
        self.reversed = kwargs.get('reversed', None)

    @property
    def background_colors(self) -> Optional[List[str]]:
        """An array of colors to apply to the backgorund of fibonacci annotations.

        Defaults to:

        .. code-block:: python

          [
              'rgba(130, 170, 255, 0.4)',
              'rgba(139, 191, 216, 0.4)',
              'rgba(150, 216, 192, 0.4)',
              'rgba(156, 229, 161, 0.4)',
              'rgba(162, 241, 130, 0.4)',
              'rgba(169, 255, 101, 0.4)'
          ]

        :rtype: :class:`list <python:list>` of :class:`str <python:str>`, or
          :obj:`None <python:None>`
        """
        return self._background_colors

    @background_colors.setter
    def background_colors(self, value):
        if not value:
            self._background_colors = None
        else:
            value = validators.iterable(value, allow_empty = True)
            self._background_colors = [validators.string(x) for x in value]

    @property
    def height(self) -> Optional[int | float | Decimal]:
        """The height of the fibonacci annotation, expressed in pixels. Defaults to ``2``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._height

    @height.setter
    def height(self, value):
        self._height = validators.numeric(value, allow_empty = True)

    @property
    def labels(self) -> Optional[List[LabelOptions]]:
        """An array of options for the labels.

        :rtype: :class:`list <python:list>` of
          :class:`LabelOptions <highcharts_stock.options.annotations.label_options.LabelOptions>`
          instances, or :obj:`None <python:None>`
        """
        return self._labels

    @labels.setter
    @class_sensitive(LabelOptions, force_iterable = True)
    def labels(self, value):
        self._labels = value

    @property
    def line(self) -> Optional[LineFillOnly]:
        """Line configuration settings.

        :rtype: :class:`LineFillOnly <highcharts_stock.options.annotations.stock_tools.type_options.line.LineFillOnly>`
          or :obj:`None <python:None>`
        """
        return self._line

    @line.setter
    @class_sensitive(LineFillOnly)
    def line(self, value):
        self._line = value

    @property
    def line_color(self) -> Optional[str]:
        """The color of the line. Defaults to ``'#999999'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._line_color

    @line_color.setter
    def line_color(self, value):
        self._line_color = validators.string(value, allow_empty = True)

    @property
    def line_colors(self) -> Optional[List[str]]:
        """Array of colors for the lines.

        :rtype: :class:`list <python:list>` of :class:`str <python:str>`, or
          :obj:`None <python:None>`
        """
        return self._line_colors

    @line_colors.setter
    def line_colors(self, value):
        if not value:
            self._line_colors = None
        else:
            value = validators.iterable(value, allow_empty = True)
            self._line_colors = [validators.string(x) for x in value]

    @property
    def points(self) -> Optional[List[StockToolsPoint]]:
        """Collection of annotation points for the stock tool type.

        :rtype: :class:`list <python:list>` of
          :class:`StockToolsPoint <highcharts_stock.options.annotations.stock_tools.type_options.points.StockToolsPoint>`
          instances, or :obj:`None <python:None>`
        """
        return self._points

    @points.setter
    @class_sensitive(StockToolsPoint, force_iterable = True)
    def points(self, value):
        self._points = value

    @property
    def reversed(self) -> Optional[bool]:
        """Flag which determines whether the annotation levels should be reversed. 
        Defaults to ``False``, meaning that they go from ``0`` to ``1``.
        
        :rtype: :class:`bool <python:bool>`
        """
        return self._reversed
    
    @reversed.setter
    def reversed(self, value):
        if value is None:
            self._reversed = None
        else:
            self._reversed = bool(value)

    @property
    def x_axis(self) -> Optional[str | int]:
        """This number defines which xAxis the point is connected to.

        It refers to either the axis id (as a :class:`str <python:str>`) or the index of
        the axis in the xAxis array (as an :class:`int <python:int>`).

        If the option is not configured or the axis is not found the point's x coordinate
        refers to the chart pixels.

        :rtype: :class:`str <python:str>` or :class:`int <python:int>`, or
          :obj:`None <python:None>`
        """
        return self._x_axis

    @x_axis.setter
    def x_axis(self, value):
        if value is None or value == '':
            self._x_axis = None
        else:
            try:
                try:
                    self._x_axis = validators.integer(value)
                except (ValueError, TypeError):
                    self._x_axis = validators.string(value)
            except ValueError:
                raise errors.HighchartsValueError('Unable to resolve value to a '
                                                  'supported type.')

    @property
    def y_axis(self) -> Optional[str | int]:
        """This number defines which yAxis the point is connected to.

        It refers to either the axis id (as a :class:`str <python:str>`) or the index of
        the axis in the yAxis array (as an :class:`int <python:int>`).

        If the option is not configured or the axis is not found the point's y coordinate
        refers to the chart pixels.

        :rtype: :class:`str <python:str>` or :class:`int <python:int>`, or
          :obj:`None <python:None>`
        """
        return self._y_axis

    @y_axis.setter
    def y_axis(self, value):
        if value is None or value == '':
            self._y_axis = None
        else:
            try:
                try:
                    self._y_axis = validators.integer(value)
                except (ValueError, TypeError):
                    self._y_axis = validators.string(value)
            except ValueError:
                raise errors.HighchartsValueError('Unable to resolve value to a '
                                                  'supported type.')

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'background_colors': as_dict.get('backgroundColors', None),
            'height': as_dict.get('height', None),
            'labels': as_dict.get('labels', None),
            'line': as_dict.get('line', None),
            'line_color': as_dict.get('lineColor', None),
            'line_colors': as_dict.get('lineColors', None),
            'points': as_dict.get('points', None),
            'reversed': as_dict.get('reversed', None),
            'x_axis': as_dict.get('xAxis', None),
            'y_axis': as_dict.get('yAxis', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'backgroundColors': self.background_colors,
            'height': self.height,
            'labels': self.labels,
            'line': self.line,
            'lineColor': self.line_color,
            'lineColors': self.line_colors,
            'points': self.points,
            'reversed': self.reversed,
            'xAxis': self.x_axis,
            'yAxis': self.y_axis,
        }

        return untrimmed


class FibonacciTimeZonesTypeOptions(HighchartsMeta):
    """Additional options for :term:`fibonacci` annotations."""

    def __init__(self, **kwargs):
        self._line = None
        self._points = None
        self._x_axis = None
        self._y_axis = None

        self.line = kwargs.get('line', None)
        self.points = kwargs.get('points', None)
        self.x_axis = kwargs.get('x_axis', None)
        self.y_axis = kwargs.get('y_axis', None)

    @property
    def line(self) -> Optional[LineStrokeWidthStroke]:
        """Line configuration settings.

        :rtype: :class:`LineStrokeWidthStroke <highcharts_stock.options.annotations.stock_tools.type_options.line.LineStrokeWidthStroke>`
          or :obj:`None <python:None>`
        """
        return self._line

    @line.setter
    @class_sensitive(LineStrokeWidthStroke)
    def line(self, value):
        self._line = value

    @property
    def points(self) -> Optional[List[StockToolsXPoint]]:
        """Collection of annotation points for the stock tool type.

        :rtype: :class:`list <python:list>` of
          :class:`StockToolsXPoint <highcharts_stock.options.annotations.stock_tools.type_options.points.StockToolsXPoint>`
          instances, or :obj:`None <python:None>`
        """
        return self._points

    @points.setter
    @class_sensitive(StockToolsXPoint, force_iterable = True)
    def points(self, value):
        self._points = value

    @property
    def x_axis(self) -> Optional[str | int]:
        """This number defines which xAxis the point is connected to.

        It refers to either the axis id (as a :class:`str <python:str>`) or the index of
        the axis in the xAxis array (as an :class:`int <python:int>`).

        If the option is not configured or the axis is not found the point's x coordinate
        refers to the chart pixels.

        :rtype: :class:`str <python:str>` or :class:`int <python:int>`, or
          :obj:`None <python:None>`
        """
        return self._x_axis

    @x_axis.setter
    def x_axis(self, value):
        if value is None or value == '':
            self._x_axis = None
        else:
            try:
                try:
                    self._x_axis = validators.integer(value)
                except (ValueError, TypeError):
                    self._x_axis = validators.string(value)
            except ValueError:
                raise errors.HighchartsValueError('Unable to resolve value to a '
                                                  'supported type.')

    @property
    def y_axis(self) -> Optional[str | int]:
        """This number defines which yAxis the point is connected to.

        It refers to either the axis id (as a :class:`str <python:str>`) or the index of
        the axis in the yAxis array (as an :class:`int <python:int>`).

        If the option is not configured or the axis is not found the point's y coordinate
        refers to the chart pixels.

        :rtype: :class:`str <python:str>` or :class:`int <python:int>`, or
          :obj:`None <python:None>`
        """
        return self._y_axis

    @y_axis.setter
    def y_axis(self, value):
        if value is None or value == '':
            self._y_axis = None
        else:
            try:
                try:
                    self._y_axis = validators.integer(value)
                except (ValueError, TypeError):
                    self._y_axis = validators.string(value)
            except ValueError:
                raise errors.HighchartsValueError('Unable to resolve value to a '
                                                  'supported type.')

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'line': as_dict.get('line', None),
            'points': as_dict.get('points', None),
            'x_axis': as_dict.get('xAxis', None),
            'y_axis': as_dict.get('yAxis', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'line': self.line,
            'points': self.points,
            'xAxis': self.x_axis,
            'yAxis': self.y_axis,
        }

        return untrimmed

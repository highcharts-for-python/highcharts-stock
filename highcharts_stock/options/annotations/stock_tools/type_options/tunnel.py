from typing import Optional, List
from decimal import Decimal

from validator_collection import validators

from highcharts_core.decorators import class_sensitive
from highcharts_core.metaclasses import HighchartsMeta
from highcharts_core.options.annotations.control_point_options import AnnotationControlPointOption

from highcharts_stock import errors
from highcharts_stock.options.annotations.stock_tools.type_options.line import LineStrokeWidth
from highcharts_stock.options.annotations.stock_tools.type_options.points import StockToolsPoint


class TunnelTypeOptions(HighchartsMeta):
    """Additional options for :term:`tunnel` annotations."""

    def __init__(self, **kwargs):
        self._background = None
        self._height = None
        self._height_control_point = None
        self._line = None
        self._points = None
        self._x_axis = None
        self._y_axis = None

        self.background = kwargs.get('background', None)
        self.height = kwargs.get('height', None)
        self.height_control_point = kwargs.get('height_control_point', None)
        self.line = kwargs.get('line', None)
        self.points = kwargs.get('points', None)
        self.x_axis = kwargs.get('x_axis', None)
        self.y_axis = kwargs.get('y_axis', None)

    @property
    def background(self) -> Optional[LineStrokeWidth]:
        """Background options.

        :rtype: :class:`LineStrokeWidth <highcharts_stock.options.annotations.stock_tools.type_options.line.LineStrokeWidth>`
          or :obj:`None <python:None>`
        """
        return self._background

    @background.setter
    @class_sensitive(LineStrokeWidth)
    def background(self, value):
        self._background = value

    @property
    def height(self) -> Optional[int | float | Decimal]:
        """The height of the annotation in terms of the y-axis. Defaults to ``-2``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._height

    @height.setter
    def height(self, value):
        self._height = validators.numeric(value, allow_empty = True)

    @property
    def height_control_point(self) -> Optional[AnnotationControlPointOption]:
        """The control point configuration for the annotation's height.

        :rtype: :class:`AnnotationControlPointOption <highcharts_core.options.annotations.control_point_options.AnnotationControlPointOption>`
          or :obj:`None <python:None>`
        """
        return self._height_control_point

    @height_control_point.setter
    @class_sensitive(AnnotationControlPointOption)
    def height_control_point(self, value):
        self._height_control_point = value

    @property
    def line(self) -> Optional[LineStrokeWidth]:
        """Line configuration settings.

        :rtype: :class:`LineStrokeWidth <highcharts_stock.options.annotations.stock_tools.type_options.line.LineStrokeWidth>`
          or :obj:`None <python:None>`
        """
        return self._line

    @line.setter
    @class_sensitive(LineStrokeWidth)
    def line(self, value):
        self._line = value

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
            'background': as_dict.get('background', None),
            'height': as_dict.get('height', None),
            'height_control_point': as_dict.get('heightControlPoint', None),
            'line': as_dict.get('line', None),
            'points': as_dict.get('points', None),
            'x_axis': as_dict.get('xAxis', None),
            'y_axis': as_dict.get('yAxis', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'background': self.background,
            'height': self.height,
            'heightControlPoint': self.height_control_point,
            'line': self.line,
            'points': self.points,
            'xAxis': self.x_axis,
            'yAxis': self.y_axis,
        }

        return untrimmed

from typing import Optional, List
from decimal import Decimal

from validator_collection import validators

from highcharts_core.decorators import class_sensitive
from highcharts_core.metaclasses import HighchartsMeta
from highcharts_core.options.axes.crosshair import CrosshairOptions
from highcharts_core.utility_classes.javascript_functions import CallbackFunction

from highcharts_stock import errors
from highcharts_stock.options.annotations.stock_tools.type_options.line import LineFillOnly, LineStrokeWidthStroke
from highcharts_stock.options.annotations.stock_tools.type_options.points import StockToolsPoint


class MeasureLabelStyle(HighchartsMeta):
    """Configuration of style properties for the :term:`measure` stock tools annotation
    label."""

    def __init__(self, **kwargs):
        self._color = None
        self._font_size = None

        self.color = kwargs.get('color', None)
        self.font_size = kwargs.get('font_size', None)

    @property
    def color(self) -> Optional[str]:
        """The color to apply to the measure label. Defaults to '#666666'.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._color

    @color.setter
    def color(self, value):
        self._color = validators.string(value, allow_empty = True)

    @property
    def font_size(self) -> Optional[str | int | float | Decimal]:
        """The font size to apply to the label. Defaults to ``11px``.

        :rtype: numeric or :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._font_size

    @font_size.setter
    def font_size(self, value):
        if value is None or value == '':
            self._font_size = None
        else:
            try:
                self._font_size = validators.string(value)
            except (ValueError, TypeError):
                self._font_size = validators.numeric(value)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'color': as_dict.get('color', None),
            'font_size': as_dict.get('fontSize', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'color': self.color,
            'fontSize': self.font_size,
        }

        return untrimmed


class MeasureLabelOptions(HighchartsMeta):
    """Configuration for the label in a :term:`measure` stock tools annotations which
    displays:

      * min
      * max
      * average
      * bins

    values.
    """

    def __init__(self, **kwargs):
        self._enabled = None
        self._formatter = None
        self._style = None

        self.enabled = kwargs.get('enabled', None)
        self.formatter = kwargs.get('formatter', None)
        self.style = kwargs.get('style', None)

    @property
    def enabled(self) -> Optional[bool]:
        """If ``True``, enables the label text. If ``False``, disables the label text.

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
    def formatter(self) -> Optional[CallbackFunction]:
        """JavaScript formatter function for the label text. Defaults to
        :obj:`None <python:None>`.

        Available data within the JavaScript context are:

          * ``this.min`` - the minimum value of points in the selected range
          * ``this.max`` - the maximum value of points in the selected range
          * ``this.average`` - the average value of points in the selected range
          * ``this.bins`` - the number of points in the selected range

        :rtype: :class:`CallbackFunction <highcharts_stock.utility_classes.javascript_functions.CallbackFunction>`
          or :obj:`None <python:None>`
        """
        return self._formatter

    @formatter.setter
    @class_sensitive(CallbackFunction)
    def formatter(self, value):
        self._formatter = value

    @property
    def style(self) -> Optional[MeasureLabelStyle]:
        """Style configuration applied to the label.

        :rtype: :class:`MeasureLabelStyle` or :obj:`None <python:None>`
        """
        return self._style

    @style.setter
    @class_sensitive(MeasureLabelStyle)
    def style(self, value):
        self._style = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'enabled': as_dict.get('enabled', None),
            'formatter': as_dict.get('formatter', None),
            'style': as_dict.get('style', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'enabled': self.enabled,
            'formatter': self.formatter,
            'style': self.style
        }

        return untrimmed


class MeasureTypeOptions(HighchartsMeta):
    """Additional options for :term:`measure` annotations."""

    def __init__(self, **kwargs):
        self._background = None
        self._crosshair_x = None
        self._crosshair_y = None
        self._label = None
        self._line = None
        self._points = None
        self._select_type = None
        self._x_axis = None
        self._y_axis = None

        self.background = kwargs.get('background', None)
        self.crosshair_x = kwargs.get('crosshair_x', None)
        self.crosshair_y = kwargs.get('crosshair_y', None)
        self.label = kwargs.get('label', None)
        self.line = kwargs.get('line', None)
        self.points = kwargs.get('points', None)
        self.select_type = kwargs.get('select_type', None)
        self.x_axis = kwargs.get('x_axis', None)
        self.y_axis = kwargs.get('y_axis', None)

    @property
    def background(self) -> Optional[LineStrokeWidthStroke]:
        """Style properties for the annotation box.

        :rtype: :class:`LineStrokeWidthStroke <highcharts_stock.options.annotations.stock_tools.type_options.line.LineStrokeWidthStroke>`
          or :obj:`None <python:None>`
        """
        return self._background

    @background.setter
    @class_sensitive(LineStrokeWidthStroke)
    def background(self, value):
        self._background = value

    @property
    def crosshair_x(self) -> Optional[CrosshairOptions]:
        """The crosshair that is horizontally placed in the middle of the rectangle.

        :rtype: :class:`CrosshairOptions <highcharts_stock.options.axes.crosshair.CrosshairOptions>`
          or :obj:`None <python:None>`
        """
        return self._crosshair_x

    @crosshair_x.setter
    @class_sensitive(CrosshairOptions)
    def crosshair_x(self, value):
        self._crosshair_x = value

    @property
    def crosshair_y(self) -> Optional[CrosshairOptions]:
        """The crosshair that is vertically placed in the middle of the rectangle.

        :rtype: :class:`CrosshairOptions <highcharts_stock.options.axes.crosshair.CrosshairOptions>`
          or :obj:`None <python:None>`
        """
        return self._crosshair_y

    @crosshair_y.setter
    @class_sensitive(CrosshairOptions)
    def crosshair_y(self, value):
        self._crosshair_y = value

    @property
    def label(self) -> Optional[MeasureLabelOptions]:
        """Configuration for the label displayed for the :term:`measure stock tool`.

        :rtype: :class:`MeasureLabelOptions <highcharts_stock.options.annotations.stock_tools.measure.MeasureLabelOptions>`
          or :obj:`None <python:None>`
        """
        return self._label

    @label.setter
    @class_sensitive(MeasureLabelOptions)
    def label(self, value):
        self._label = value

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
    def select_type(self) -> Optional[str]:
        """Decides in what dimensions the user can resize by dragging the mouse. Defaults
        to ``'xy'``.

        Accepts either:

          * ``'x'``
          * ``'xy'``
          * ``'y'``


        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._select_type

    @select_type.setter
    def select_type(self, value):
        if not value:
            self._select_type = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['x', 'xy', 'y']:
                raise errors.HighchartsValueError(f'select_type expects either "x", "xy",'
                                                  f' or "y". Received: "{value}".')
            self._select_type = value

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
            'crosshair_x': as_dict.get('crosshairX', None),
            'crosshair_y': as_dict.get('crosshairY', None),
            'label': as_dict.get('label', None),
            'line': as_dict.get('line', None),
            'points': as_dict.get('points', None),
            'select_type': as_dict.get('selectType', None),
            'x_axis': as_dict.get('xAxis', None),
            'y_axis': as_dict.get('yAxis', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'background': self.background,
            'crosshairX': self.crosshair_x,
            'crosshairY': self.crosshair_y,
            'label': self.label,
            'line': self.line,
            'points': self.points,
            'selectType': self.select_type,
            'xAxis': self.x_axis,
            'yAxis': self.y_axis,
        }

        return untrimmed

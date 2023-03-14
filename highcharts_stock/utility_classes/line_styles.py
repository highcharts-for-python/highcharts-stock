from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts_stock import constants, errors
from highcharts_stock.metaclasses import HighchartsMeta


class LineStylesWidth(HighchartsMeta):
    """Line styles with line width."""

    def __init__(self, **kwargs):
        self._line_width = None

        self.line_width = kwargs.get('line_width', None)

    @property
    def line_width(self) -> Optional[int | float | Decimal]:
        """The thickness of the line, expressed in pixels.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._line_width

    @line_width.setter
    def line_width(self, value):
        self._line_width = validators.numeric(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'line_width': as_dict.get('lineWidth', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'lineWidth': self.line_width,
        }

        return untrimmed


class LineStylesColorWidth(LineStylesWidth):
    """Line styles with line width and color."""

    def __init__(self, **kwargs):
        self._line_color = None

        self.line_color = kwargs.get('line_color', None)

        super().__init__(**kwargs)

    @property
    def line_color(self) -> Optional[str]:
        """The color to apply to the line, expressed as a color string.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._line_color

    @line_color.setter
    def line_color(self, value):
        self._line_color = validators.string(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'line_width': as_dict.get('lineWidth', None),
            'line_color': as_dict.get('lineColor', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'lineWidth': self.line_width,
            'lineColor': self.line_color,
        }

        return untrimmed


class LineStylesColorWidthDash(LineStylesColorWidth):
    """Line styles with line width and color."""

    def __init__(self, **kwargs):
        self._dash_style = None

        self.dash_style = kwargs.get('dash_style', None)

        super().__init__(**kwargs)

    @property
    def dash_style(self) -> Optional[str]:
        """Name of the dash style to use for the shape's stroke.

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

        :returns: The name of the dash style to apply to the shape's stroke.
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._dash_style

    @dash_style.setter
    def dash_style(self, value):
        value = validators.string(value, allow_empty = True)
        if not value:
            self._dash_style = None
        else:
            if value not in constants.SHAPES_ALLOWED_DASH_STYLES:
                raise errors.HighchartsValueError(f'dash_style expects a supported value.'
                                                  f' Received: {value}')
            self._dash_style = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'line_width': as_dict.get('lineWidth', None),

            'line_color': as_dict.get('lineColor', None),

            'dash_style': as_dict.get('dashStyle', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'dashStyle': self.dash_style,
            'lineColor': self.line_color,
            'lineWidth': self.line_width,
        }

        return untrimmed

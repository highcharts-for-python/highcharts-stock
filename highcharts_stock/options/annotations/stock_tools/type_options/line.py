from typing import Optional

from validator_collection import validators

from highcharts_core.metaclasses import HighchartsMeta


class LineFillOnly(HighchartsMeta):
    """Line object with only a fill property."""

    def __init__(self, **kwargs):
        self._fill = None

        self.fill = kwargs.get('fill', None)

    @property
    def fill(self) -> Optional[str]:
        """Setting for the fill color.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._fill

    @fill.setter
    def fill(self, value):
        self._fill = validators.string(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'fill': as_dict.get('fill', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'fill': self.fill
        }

        return untrimmed


class LineStrokeWidth(LineFillOnly):
    """Line object a fill and stroke width properties."""

    def __init__(self, **kwargs):
        self._stroke_width = None

        self.stroke_width = kwargs.get('stroke_width', None)

        super().__init__(**kwargs)

    @property
    def stroke_width(self) -> Optional[int]:
        """Setting for the line's stroke width.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._stroke_width

    @stroke_width.setter
    def stroke_width(self, value):
        self._stroke_width = validators.integer(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'fill': as_dict.get('fill', None),
            'stroke_width': as_dict.get('strokeWidth', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'fill': self.fill,
            'strokeWidth': self.stroke_width,
        }

        return untrimmed


class LineStrokeWidthStroke(LineStrokeWidth):
    """Line object a fill and stroke width properties."""

    def __init__(self, **kwargs):
        self._stroke = None

        self.stroke = kwargs.get('stroke', None)

        super().__init__(**kwargs)

    @property
    def stroke(self) -> Optional[str]:
        """Setting for the line's stroke color. Defaults to
        ``'rgba(0, 0, 0, 0.75)'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._stroke

    @stroke.setter
    def stroke(self, value):
        self._stroke = validators.string(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'fill': as_dict.get('fill', None),
            'stroke': as_dict.get('stroke', None),
            'stroke_width': as_dict.get('strokeWidth', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'fill': self.fill,
            'stroke': self.stroke,
            'strokeWidth': self.stroke_width,
        }

        return untrimmed

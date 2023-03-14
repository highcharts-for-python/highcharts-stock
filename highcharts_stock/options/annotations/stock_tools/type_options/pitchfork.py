from typing import Optional

from validator_collection import validators

from highcharts_core.decorators import class_sensitive
from highcharts_core.options.annotations.shape_options import ShapeOptionsBase

from highcharts_stock.options.annotations.stock_tools.type_options.crooked_line import CrookedLineTypeOptions


class PitchforkTypeOptions(CrookedLineTypeOptions):
    """Configuration options for the :term:`pitchfork` stock tool type annotation."""

    def __init__(self, **kwargs):
        self._inner_background = None
        self._outer_background = None

        self.inner_background = kwargs.get('inner_background', None)
        self.outer_background = kwargs.get('outer_background', None)

        super().__init__(**kwargs)

    @property
    def inner_background(self) -> Optional[ShapeOptionsBase]:
        """Options for the inner background of the :term:`pitchfork` stock tool
        annotation.

        :rtype: :class:`ShapeOptionsBase <highcharts_stock.options.annotations.shape_options.ShapeOptionsBase>`
          or :obj:`None <python:None>`
        """
        return self._inner_background

    @inner_background.setter
    @class_sensitive(ShapeOptionsBase)
    def inner_background(self, value):
        self._inner_background = value

    @property
    def outer_background(self) -> Optional[ShapeOptionsBase]:
        """Options for the outer background of the :term:`pitchfork` stock tool
        annotation.

        :rtype: :class:`ShapeOptionsBase <highcharts_stock.options.annotations.shape_options.ShapeOptionsBase>`
          or :obj:`None <python:None>`
        """
        return self._outer_background

    @outer_background.setter
    @class_sensitive(ShapeOptionsBase)
    def outer_background(self, value):
        self._outer_background = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'inner_background': as_dict.get('innerBackground', None),
            'line': as_dict.get('line', None),
            'outer_background': as_dict.get('outerBackground', None),
            'points': as_dict.get('points', None),
            'x_axis': as_dict.get('xAxis', None),
            'y_axis': as_dict.get('yAxis', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'innerBackground': self.inner_background,
            'line': self.line,
            'outerBackground': self.outer_background,
            'points': self.points,
            'xAxis': self.x_axis,
            'yAxis': self.y_axis,
        }

        return untrimmed

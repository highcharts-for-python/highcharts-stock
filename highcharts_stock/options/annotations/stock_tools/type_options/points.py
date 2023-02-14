from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts_core.decorators import class_sensitive
from highcharts_core.metaclasses import HighchartsMeta
from highcharts_stock.options.annotations.label_options import LabelOptions


class StockToolsPoint(HighchartsMeta):
    """Point configuration for a Stock Tools annotation."""

    def __init__(self, **kwargs):
        self._control_point = None
        self._x = None
        self._y = None

        self.control_point = kwargs.get('control_point', None)
        self.x = kwargs.get('x', None)
        self.y = kwargs.get('y', None)

    @property
    def control_point(self) -> Optional[int]:
        """The number of the control point. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._control_point

    @control_point.setter
    def control_point(self, value):
        self._control_point = validators.integer(value, allow_empty = True)

    @property
    def x(self) -> Optional[int | float | Decimal]:
        """The x position of the point.

        Units can be either in axis or chart pixel coordinates.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._x

    @x.setter
    def x(self, value):
        self._x = validators.numeric(value, allow_empty = True)

    @property
    def y(self) -> Optional[int | float | Decimal]:
        """The y position of the point.

        Units can be either in axis or chart pixel coordinates.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._y

    @y.setter
    def y(self, value):
        self._y = validators.numeric(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'control_point': as_dict.get('controlPoint', None),
            'x': as_dict.get('x', None),
            'y': as_dict.get('y', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'controlPoint': self.control_point,
            'x': self.x,
            'y': self.y
        }

        return untrimmed


class LabeledStockToolsPoint(StockToolsPoint):
    """Point configuration for a Stock Tools annotation with a label."""

    def __init__(self, **kwargs):
        self._label = None

        self.label = kwargs.get('label', None)

        super().__init__(**kwargs)

    @property
    def label(self) -> Optional[LabelOptions]:
        """Configuration options for the labels.

        :rtype: :class:`LabelOptions <highcharts_stock.options.annotations.label_options.LabelOptions>`
          or :obj:`None <python:None>`
        """
        return self._label

    @label.setter
    @class_sensitive(LabelOptions)
    def label(self, value):
        self._label = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'control_point': as_dict.get('controlPoint', None),
            'x': as_dict.get('x', None),
            'y': as_dict.get('y', None),

            'label': as_dict.get('label', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'label': self.label
        }

        parent_as_dict = super()._to_untrimmed_dict(in_cls = in_cls)

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed


class StockToolsXPoint(HighchartsMeta):
    """Point configuration for a Stock Tools annotation."""

    def __init__(self, **kwargs):
        self._control_point = None
        self._x = None

        self.control_point = kwargs.get('control_point', None)
        self.x = kwargs.get('x', None)

    @property
    def control_point(self) -> Optional[int]:
        """The number of the control point. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._control_point

    @control_point.setter
    def control_point(self, value):
        self._control_point = validators.integer(value, allow_empty = True)

    @property
    def x(self) -> Optional[int | float | Decimal]:
        """The x position of the point.

        Units can be either in axis or chart pixel coordinates.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._x

    @x.setter
    def x(self, value):
        self._x = validators.numeric(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'control_point': as_dict.get('controlPoint', None),
            'x': as_dict.get('x', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'controlPoint': self.control_point,
            'x': self.x,
        }

        return untrimmed

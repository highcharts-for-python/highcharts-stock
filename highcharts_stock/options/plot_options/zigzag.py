from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts_core.decorators import class_sensitive

from highcharts_stock.options.plot_options.indicators import ParameterBase, ComparableIndicatorOptions


class ZigZagParameters(ParameterBase):
    """Parameters for
    :class:`ZigZagOptions <highcharts_stock.options.plot_options.zigzag.ZigZagOptions>`
    """

    def __init__(self, **kwargs):
        self._deviation = None
        self._high_index = None
        self._low_index = None

        self.deviation = kwargs.get('deviation', None)
        self.high_index = kwargs.get('high_index', None)
        self.low_index = kwargs.get('low_index', None)

    @property
    def index(self):
        """Does not apply, so raises an :exc:`AttributeError <python:AttributeError>`."""
        raise AttributeError(f"{self.__class__.__name__} has no attribute 'index'")

    @index.setter
    def index(self, value):
        raise AttributeError(f"{self.__class__.__name__} has no attribute 'index'")

    @property
    def period(self):
        """Does not apply, so raises an :exc:`AttributeError <python:AttributeError>`."""
        raise AttributeError(f"{self.__class__.__name__} has no attribute 'period'")

    @period.setter
    def period(self, value):
        raise AttributeError(f"{self.__class__.__name__} has no attribute 'period'")

    @property
    def deviation(self) -> Optional[int | float | Decimal]:
        """The threshold used for the value change. Defaults to ``1``, which means the
        indicator will ignore all value movements less than 1%.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._deviation

    @deviation.setter
    def deviation(self, value):
        self._deviation = validators.numeric(value, allow_empty = True)

    @property
    def high_index(self) -> Optional[int]:
        """The point index which will be used for the high value in calculating the
        indicator. Defaults to ``1``, which means that in OHLC data the high index will be
        based using the High value point.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._high_index

    @high_index.setter
    def high_index(self, value):
        self._high_index = validators.integer(value,
                                              allow_empty = True,
                                              minimum = 0)

    @property
    def low_index(self) -> Optional[int]:
        """The point index which will be used for the low value in calculating the
        indicator. Defaults to ``2``, which means that in OHLC data the low index will be
        based using the Low value point.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._low_index

    @low_index.setter
    def low_index(self, value):
        self._low_index = validators.integer(value,
                                             allow_empty = True,
                                             minimum = 0)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'deviation': as_dict.get('deviation', None),
            'high_index': as_dict.get('highIndex', None),
            'low_index': as_dict.get('lowIndex', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'deviation': self.deviation,
            'highIndex': self.high_index,
            'lowIndex': self.low_index
        }

        return untrimmed


class ZigZagOptions(ComparableIndicatorOptions):
    """Options to configure a ZigZag :term:`indicator`.

    .. figure:: ../../../_static/zigzag-example.png
      :alt: ZigZag Example Chart
      :align: center

    """
    @property
    def params(self) -> Optional[ZigZagParameters]:
        """Parameters used in calculating the indicator's data points.

        :rtype: :class:`ZigZagParameters` or :obj:`None <python:None>`
        """
        return self._params

    @params.setter
    @class_sensitive(ZigZagParameters)
    def params(self, value):
        self._params = value

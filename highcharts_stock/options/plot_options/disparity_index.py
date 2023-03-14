from typing import Optional

from validator_collection import validators

from highcharts_core.decorators import class_sensitive

from highcharts_stock import errors
from highcharts_stock.options.plot_options.indicators import ComparableIndicatorOptions, ParameterBase


class DisparityIndexParameters(ParameterBase):

    def __init__(self, **kwargs):
        self._average = None

        self.average = kwargs.get('average', None)

        super().__init__(**kwargs)

    @property
    def average(self) -> Optional[str]:
        """The average used to calculate the Disparity Index indicator. Defaults to
        ``sma``.

        Accepts the following values:

          * ``'sma'`` - for a Simple Moving Average
          * ``'ema'`` - for an Exponential Moving Average
          * ``'dema'`` - for a Double Exponential Moving Average
          * ``'tema'`` - for a Triple Exponential Moving Average
          * ``'wma'`` - for a Weighted Moving Average

        .. caution::

          To use averages other than ``'sma'`` and ``'ema'``, the relevant JavaScript
          module must be loaded. For exapmle, to use ``'tema'``, the
          ``stock/indicators/tema.js`` module must be loaded.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._average

    @average.setter
    def average(self, value):
        if not value:
            self._average = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['sma', 'ema', 'dema', 'tema', 'wma']:
                raise errors.HighchartsValueError(f'average expects a recognized average '
                                                  f'indicator. Received: "{value}"')

            self._average = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'index': as_dict.get('index', None),
            'period': as_dict.get('period', None),

            'average': as_dict.get('average', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'index': self.index,
            'period': self.period,

            'average': self.average
        }

        return untrimmed


class DisparityIndexOptions(ComparableIndicatorOptions):
    """Options to configure a Disparity Index :term:`indicator`, which measures the
    relative position of the most-recent value to a selected moving average, expressed as
    a percentage.

    .. figure:: ../../../_static/disparity-index-example.png
      :alt: Disparity Index Example Chart
      :align: center

    """

    @property
    def params(self) -> Optional[DisparityIndexParameters]:
        """Parameters used in calculating the indicator's data points.

        :rtype: :class:`DisparityIndexParameters` or :obj:`None <python:None>`
        """
        return self._params

    @params.setter
    @class_sensitive(DisparityIndexParameters)
    def params(self, value):
        self._params = value

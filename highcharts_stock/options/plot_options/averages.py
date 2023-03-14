from typing import Optional

from validator_collection import validators

from highcharts_core.decorators import class_sensitive

from highcharts_stock.options.plot_options.indicators import ParameterBase, IndicatorOptions, ComparableIndicatorOptions


class VWAPParameters(ParameterBase):

    def __init__(self, **kwargs):
        self._period = None
        self._volume_series_id = None

        self.period = kwargs.get('period', None)
        self.volume_series_id = kwargs.get('volume_series_id', None)

        super().__init__(**kwargs)

    @property
    def index(self):
        """Does not apply, so raises an :exc:`AttributeError <python:AttributeError>`."""
        raise AttributeError(f"{self.__class__.__name__} has no attribute 'index'")

    @index.setter
    def index(self, value):
        raise AttributeError(f"{self.__class__.__name__} has no attribute 'index'")

    @property
    def volume_series_id(self) -> Optional[str]:
        """The id of :term:`series` containing volume data. Defaults to ``'volume'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._volume_series_id

    @volume_series_id.setter
    def volume_series_id(self, value):
        self._volume_series_id = validators.string(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'period': as_dict.get('period', None),
            'volume_series_id': as_dict.get('volumeSeriesID', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'period': self.period,
            'volumeSeriesID': self.volume_series_id,
        }

        return untrimmed


class DEMAOptions(IndicatorOptions):
    """Options to configure a Double Exponential Moving Average :term:`indicator`, which
    is often used to reduce the "noise" produced on a simple moving average.

    .. figure:: ../../../_static/dema-example.png
      :alt: DEMA Example Chart
      :align: center

    """
    pass


class EMAOptions(ComparableIndicatorOptions):
    """Options to configure an Exponential Moving Average :term:`indicator`, which
    is used to give greater weight to recent values.

    .. figure:: ../../../_static/ema-example.png
      :alt: Exponential Moving Average Example Chart
      :align: center

    """
    pass


class SMAOptions(ComparableIndicatorOptions):
    """Options to configure a Simple Moving Average :term:`indicator`.

    .. figure:: ../../../_static/sma-example.png
      :alt: Simple Moving Average Example Chart
      :align: center

    """
    pass


class TEMAOptions(IndicatorOptions):
    """Options to configure a Triple Exponential Moving Average :term:`indicator`, which
    is often used to reduce the "noise" produced on a simple moving average.

    .. figure:: ../../../_static/tema-example.png
      :alt: TEMA Example Chart
      :align: center

    """
    pass


class VWAPOptions(ComparableIndicatorOptions):
    """Options to configure a Volume Weighted Average Price (VWAP) :term:`indicator`.

    .. figure:: ../../../_static/vwap-example.png
      :alt: Volume Weighted Average Price Example Chart
      :align: center

    """
    @property
    def params(self) -> Optional[VWAPParameters]:
        """Parameters used in calculating the indicator's data points.

        :rtype: :class:`VWAPParameters` or :obj:`None <python:None>`
        """
        return self._params

    @params.setter
    @class_sensitive(VWAPParameters)
    def params(self, value):
        self._params = value


class WMAOptions(ComparableIndicatorOptions):
    """Options to configure a Weighted Moving Average :term:`indicator`.

    .. figure:: ../../../_static/wma-example.png
      :alt: Weighted Moving Average Example Chart
      :align: center

    """
    pass

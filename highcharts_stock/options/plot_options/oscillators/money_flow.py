from typing import Optional

from validator_collection import validators

from highcharts_core.decorators import class_sensitive

from highcharts_stock.options.plot_options.indicators import ParameterBase, ComparableIndicatorOptions
from highcharts_stock.options.plot_options.ad import ADParameters as CMFParameters


class MFIParameters(ParameterBase):

    def __init__(self, **kwargs):
        self._decimals = None
        self._volume_series_id = None

        self.decimals = kwargs.get('decimals', None)
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
    def decimals(self) -> Optional[int]:
        """The number of maximum digits after the decimal to use in calculating the MFI.
        Defaults to ``4``.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._decimals

    @decimals.setter
    def decimals(self, value):
        self._decimals = validators.integer(value,
                                            allow_empty = True,
                                            minimum = 0)

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

            'decimals': as_dict.get('decimals', None),
            'volume_series_id': as_dict.get('volumeSeriesID', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'period': self.period,

            'decimals': self.decimals,
            'volumeSeriesID': self.volume_series_id,
        }

        return untrimmed


class MFIOptions(ComparableIndicatorOptions):
    """Options to configure a Money Flow Index :term:`oscillator`, which uses price and
    volume data to identify over-bought or over-sold signals in an asset.

    .. figure:: ../../../../_static/mfi-example.png
      :alt: Money Flow Index Example Chart
      :align: center

    """
    @property
    def params(self) -> Optional[MFIParameters]:
        """Parameters used in calculating the indicator's data points.

        :rtype: :class:`MFIParameters` or :obj:`None <python:None>`
        """
        return self._params

    @params.setter
    @class_sensitive(MFIParameters)
    def params(self, value):
        self._params = value


class CMFOptions(ComparableIndicatorOptions):
    """Options to configure a Chaikin Money Flow :term:`indicator <technical indicator>`,
    which uses price and
    volume data to identify over-bought or over-sold signals in an asset.

    .. figure:: ../../../../_static/cmf-example.png
      :alt: Chaikin Money Flow Example Chart
      :align: center

    """
    @property
    def params(self) -> Optional[CMFParameters]:
        """Parameters used in calculating the indicator's data points.

        :rtype: :class:`CMFParameters` or :obj:`None <python:None>`
        """
        return self._params

    @params.setter
    @class_sensitive(CMFParameters)
    def params(self, value):
        self._params = value

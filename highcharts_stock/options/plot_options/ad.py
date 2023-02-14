from typing import Optional

from validator_collection import validators

from highcharts_core.decorators import class_sensitive

from highcharts_stock.options.plot_options.indicators import ParameterBase, ComparableIndicatorOptions


class ADParameters(ParameterBase):

    def __init__(self, **kwargs):
        self._volume_series_id = None

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


class ADOptions(ComparableIndicatorOptions):
    """Options to configure an Accumulation/Distribution
    :term:`indicator <techincal indicator>`, which is a cumulative indicator that uses
    volume and price to assess whether a stock is being accumulated or distributed

    .. figure:: ../../../_static/ad-example.png
      :alt: Accumulation/Distribution Example Chart
      :align: center

    """
    @property
    def params(self) -> Optional[ADParameters]:
        """Parameters used in calculating the indicator's data points.

        :rtype: :class:`ADParameters` or :obj:`None <python:None>`
        """
        return self._params

    @params.setter
    @class_sensitive(ADParameters)
    def params(self, value):
        self._params = value

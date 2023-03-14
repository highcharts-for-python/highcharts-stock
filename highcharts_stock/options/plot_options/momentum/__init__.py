from typing import Optional

from validator_collection import validators

from highcharts_core.decorators import class_sensitive

from highcharts_stock.options.plot_options.indicators import ParameterBase, ComparableIndicatorOptions


class OBVParameters(ParameterBase):

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
    def period(self):
        """Does not apply, so raises an :exc:`AttributeError <python:AttributeError>`."""
        raise AttributeError(f"{self.__class__.__name__} has no attribute 'period'")

    @period.setter
    def period(self, value):
        raise AttributeError(f"{self.__class__.__name__} has no attribute 'period'")

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
            'volume_series_id': as_dict.get('volumeSeriesID', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'volumeSeriesID': self.volume_series_id,
        }

        return untrimmed


class RSIParameters(ParameterBase):
    """Parameters for
    :class:`RSIOptions <highcharts_stock.options.plot_options.momentum.RSIOptions>`"""

    def __init__(self, **kwargs):
        self._decimals = None

        self.decimals = kwargs.get('decimals', None)

        super().__init__(**kwargs)

    @property
    def decimals(self) -> Optional[int]:
        """The number of maximum digits after the decimal to use in calculating the RSI.
        Defaults to ``4``.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._decimals

    @decimals.setter
    def decimals(self, value):
        self._decimals = validators.integer(value,
                                            allow_empty = True,
                                            minimum = 0)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'index': as_dict.get('index', None),
            'period': as_dict.get('period', None),

            'decimals': as_dict.get('decimals', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'index': self.index,
            'period': self.period,

            'decimals': self.decimals,
        }

        return untrimmed


class MomentumOptions(ComparableIndicatorOptions):
    """Options to configure a Momentum :term:`indicator <techincal indicator>`.

    .. figure:: ../../../../_static/momentum-example.png
      :alt: Momentum Example Chart
      :align: center

    """
    pass


class OBVOptions(ComparableIndicatorOptions):
    """Options to configure an On-Balance Volume :term:`indicator <techincal indicator>`,
    which uses volume flow to predict changes.

    .. figure:: ../../../../_static/obv-example.png
      :alt: OBV Example Chart
      :align: center

    """
    @property
    def params(self) -> Optional[OBVParameters]:
        """Parameters used in calculating the indicator's data points.

        :rtype: :class:`OBVParameters` or :obj:`None <python:None>`
        """
        return self._params

    @params.setter
    @class_sensitive(OBVParameters)
    def params(self, value):
        self._params = value


class ROCOptions(ComparableIndicatorOptions):
    """Options to configure a Rate of Change :term:`indicator <techincal indicator>`.

    .. figure:: ../../../../_static/roc-example.png
      :alt: Rate of Change Example Chart
      :align: center

    The indicator value for each point is calculated using:

    .. code-block::

      (C - Cn)/ Cn * 100

    where:

      * ``C`` is the close value of the point of the same x in the linked series, and
      * ``Cn`` is the close value of the point ``n`` periods ago, where ``n`` is
        determined via
        :meth:`.params.period <highcharts_stock.options.plot_options.momentum.ROCOptions.params>`

    """
    pass


class RSIOptions(ComparableIndicatorOptions):
    """Options to configure a Relative Strength Index, a momentum
    :term:`indicator <techincal indicator>` that measures the speed and magnitude of
    recent value changes to evaluate over-valued or under-valued conditions.

    .. figure:: ../../../../_static/rsi-example.png
      :alt: Relative Strength Index Example Chart
      :align: center

    """
    @property
    def params(self) -> Optional[RSIParameters]:
        """Parameters used in calculating the indicator's data points.

        :rtype: :class:`RSIParameters` or :obj:`None <python:None>`
        """
        return self._params

    @params.setter
    @class_sensitive(RSIParameters)
    def params(self, value):
        self._params = value

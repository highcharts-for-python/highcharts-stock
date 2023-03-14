from typing import Optional, List

from validator_collection import validators

from highcharts_core.decorators import class_sensitive

from highcharts_stock.options.plot_options.indicators import ParameterBase, ComparableIndicatorOptions


class PPOParameters(ParameterBase):

    def __init__(self, **kwargs):
        self._index = None
        self._periods = None

        self.index = kwargs.get('index', None)
        self.periods = kwargs.get('periods', None)

    @property
    def period(self):
        """Does not apply, so raises an :exc:`AttributeError <python:AttributeError>`."""
        raise AttributeError(f"{self.__class__.__name__} has no attribute 'period'")

    @period.setter
    def period(self, value):
        raise AttributeError(f"{self.__class__.__name__} has no attribute 'period'")

    @property
    def periods(self) -> Optional[List[int]]:
        """The periods to use when calculating the Percentage Price Oscillator. Defaults
        to ``[12, 26]``.

        .. note::

          Expects a two-member iterable of :class:`int <python:int>` instances.

        :rtype: :class:`list <python:list>` of :class:`int <python:int>`, or
          :obj:`None <python:None>`
        """
        return self._periods

    @periods.setter
    def periods(self, value):
        if not value:
            self._periods = None
        else:
            value = validators.iterable(value)
            self._periods = [validators.integer(x, minimum = 0) for x in value]

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'index': as_dict.get('index', None),
            'periods': as_dict.get('periods', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'index': self.index,
            'periods': self.periods,
        }

        return untrimmed


class PPOOptions(ComparableIndicatorOptions):
    """Options to configure a Percentage Price :term:`Oscillator`, which shows the
    relationship between two moving averages in percentage terms.

    .. note::

      Defaults to comparing a 26-period and 12-period exponential moving average, though
      this can be adjusted using
      :meth:`.params.period <highcharts_stock.options.plot_options.oscillators.PPOOptions.params`.

    .. figure:: ../../../../_static/cmo-example.png
      :alt: Chande Momentum Oscillator Example Chart
      :align: center

    """
    @property
    def params(self) -> Optional[PPOParameters]:
        """Parameters used in calculating the indicator's data points.

        :rtype: :class:`PPOParameters` or :obj:`None <python:None>`
        """
        return self._params

    @params.setter
    @class_sensitive(PPOParameters)
    def params(self, value):
        self._params = value

from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts_core.decorators import class_sensitive

from highcharts_stock.options.plot_options.indicators import ParameterBase, ComparableIndicatorOptions


class PSARParameters(ParameterBase):

    def __init__(self, **kwargs):
        self._decimals = None
        self._increment = None
        self._initial_acceleration_factor = None
        self._max_acceleration_factor = None

        self.decimals = kwargs.get('decimals', None)
        self.increment = kwargs.get('increment', None)
        self.initial_acceleration_factor = kwargs.get('initial_acceleration_factor', None)
        self.max_acceleration_factor = kwargs.get('max_acceleration_factor', None)

        super().__init__(**kwargs)

    @property
    def period(self):
        """Does not apply, so raises an :exc:`AttributeError <python:AttributeError>`."""
        raise AttributeError(f"{self.__class__.__name__} has no attribute 'period'")

    @period.setter
    def period(self, value):
        raise AttributeError(f"{self.__class__.__name__} has no attribute 'period'")

    @property
    def decimals(self) -> Optional[int]:
        """The number of maximum digits after the decimal to use in calculating the PSAR.
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
    def increment(self) -> Optional[int | float | Decimal]:
        """The acceleration factor increases by this value each time the extreme point
        makes a new high. Defaults to ``0.02``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._increment

    @increment.setter
    def increment(self, value):
        self._increment = validators.numeric(value, allow_empty = True)

    @property
    def initial_acceleration_factor(self) -> Optional[int | float | Decimal]:
        """The initial value for the acceleration factor. Defaults to ``0.02``.

        The acceleration factor starts with this value and increases by specified
        :meth:`.increment <highcharts_stock.options.plot_options.psar.PSARParameters.increment>`
        each time the extreme point makes a new high up to the value of
        :meth:`.max_acceleration_factor <highcharts_stock.options.plot_options.psar.PSARParameters.max_acceleration_factor>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._initial_acceleration_factor

    @initial_acceleration_factor.setter
    def initial_acceleration_factor(self, value):
        self._initial_acceleration_factor = validators.numeric(value, allow_empty = True)

    @property
    def max_acceleration_factor(self) -> Optional[int | float | Decimal]:
        """The maximum value at which the acceleration factor is capped. Defaults to
        ``0.2``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._max_acceleration_factor

    @max_acceleration_factor.setter
    def max_acceleration_factor(self, value):
        self._max_acceleration_factor = validators.numeric(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'index': as_dict.get('index', None),

            'decimals': as_dict.get('decimals', None),
            'increment': as_dict.get('increment', None),
            'initial_acceleration_factor': as_dict.get('initialAccelerationFactor', None),
            'max_acceleration_factor': as_dict.get('maxAccelerationFactor', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'index': self.index,

            'decimals': self.decimals,
            'increment': self.increment,
            'initialAccelerationFactor': self.initial_acceleration_factor,
            'maxAccelerationFactor': self.max_acceleration_factor,
        }

        return untrimmed


class PSAROptions(ComparableIndicatorOptions):
    """Options to configure a Parabolic SAR :term:`indicator <techincal indicator>`,
    which can be used to determine the direction in which a trend is moving.

    .. figure:: ../../../_static/psar-example.png
      :alt: Parabolic SAR Example Chart
      :align: center

    """
    @property
    def params(self) -> Optional[PSARParameters]:
        """Parameters used in calculating the indicator's data points.

        :rtype: :class:`PSARParameters` or :obj:`None <python:None>`
        """
        return self._params

    @params.setter
    @class_sensitive(PSARParameters)
    def params(self, value):
        self._params = value

from typing import Optional

from validator_collection import validators

from highcharts_core.decorators import class_sensitive

from highcharts_stock import errors
from highcharts_stock.options.plot_options.indicators import ParameterBase, ComparableIndicatorOptions


class PivotPointsParameters(ParameterBase):

    def __init__(self, **kwargs):
        self._algorithm = None

        self.algorithm = kwargs.get('algorithm', None)

        super().__init__(**kwargs)

    @property
    def index(self):
        """Does not apply, so raises an :exc:`AttributeError <python:AttributeError>`."""
        raise AttributeError(f"{self.__class__.__name__} has no attribute 'index'")

    @index.setter
    def index(self, value):
        raise AttributeError(f"{self.__class__.__name__} has no attribute 'index'")

    @property
    def algorithm(self) -> Optional[str]:
        """Algorithm used to calculate ressistance and support lines based on pivot
        points. Defaults to ``'standard'``.

        Supports the following values:

          * ``'standard'``
          * ``'fibonacci'``
          * ``'camarilla'``

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._algorithm

    @algorithm.setter
    def algorithm(self, value):
        if not value:
            self._algorithm = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['standard', 'fibonacci', 'camarilla']:
                raise errors.HighchartsValueError(f'algorithm expects either "standard", '
                                                  f'"fibonacci", or "camarilla". '
                                                  f'Received: "{value}"')

            self._algorithm = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'period': as_dict.get('period', None),

            'algorithm': as_dict.get('algorithm', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'period': self.period,

            'algorithm': self.algorithm,
        }

        return untrimmed


class PivotPointsOptions(ComparableIndicatorOptions):
    """Options to configure a Pivot Points :term:`indicator <techincal indicator>`,
    which are typically used to identify trends and reversals in intraday trading.

    .. figure:: ../../../_static/pivot-points-example.png
      :alt: Pivot Points Example Chart
      :align: center

    """
    @property
    def params(self) -> Optional[PivotPointsParameters]:
        """Parameters used in calculating the indicator's data points.

        :rtype: :class:`PivotPointsParameters` or :obj:`None <python:None>`
        """
        return self._params

    @params.setter
    @class_sensitive(PivotPointsParameters)
    def params(self, value):
        self._params = value

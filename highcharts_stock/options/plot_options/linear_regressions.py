from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts_core.decorators import class_sensitive

from highcharts_stock.options.plot_options.indicators import ParameterBase, ComparableIndicatorOptions


class LinearRegressionParameters(ParameterBase):

    def __init__(self, **kwargs):
        self._x_axis_unit = None

        self.x_axis_unit = kwargs.get('x_axis_unit', None)

        super().__init__(**kwargs)

    @property
    def x_axis_unit(self) -> Optional[int | float | Decimal]:
        """Unit (in milliseconds) for the x-axis distances used to compute the regression
        line parameters (slope & intercept) for every range.

        .. note::

          In Highcharts Stock, the x-axis values are always represented in milliseconds
          which may cause distances between points to be large integer values.

          Highcharts Stock's linear regression algorithm (least squares method) will
          utilize these "big" integers to find the slope and the intercept of the
          regression line for each period. As a result, the value of ``.x_axis_unit``
          may be a very "small" decimal number that's hard to interpret by a human.

          For example, setting ``.x_axis_unit`` to ``86400000`` (1 day, expressed in
          milliseconds) forces the algorithm to treat 86400000 as 1 while computing the
          slope and the intercept. This may enchance the legiblitity of the indicator's
          values.

        If :obj:`None <python:None>`, defaults to behave as if set to (JavaScript)
        ``null``, which then is evaluated as the closest distance between two data points.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._x_axis_unit

    @x_axis_unit.setter
    def x_axis_unit(self, value):
        self._x_axis_unit = validators.numeric(value,
                                               allow_empty = True,
                                               minimum = 0)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'index': as_dict.get('index', None),
            'period': as_dict.get('period', None),

            'x_axis_unit': as_dict.get('xAxisUnit', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'index': self.index,
            'period': self.period,

            'xAxisUnit': self.x_axis_unit,
        }

        return untrimmed


class TrendlineParameters(ParameterBase):

    def __init__(self, **kwargs):
        self._index = None

        self.index = kwargs.get('index', None)

    @property
    def period(self):
        """Does not apply, so raises an :exc:`AttributeError <python:AttributeError>`."""
        raise AttributeError(f"{self.__class__.__name__} has no attribute 'period'")

    @period.setter
    def period(self, value):
        raise AttributeError(f"{self.__class__.__name__} has no attribute 'period'")

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'index': as_dict.get('index', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'index': self.index,
        }

        return untrimmed


class LinearRegressionOptions(ComparableIndicatorOptions):
    """Options to configure a Linear Regression :term:`indicator`, which calculates a
    linear regression for a given set of values.

    .. figure:: ../../../_static/linear-regression-example.png
      :alt: Linear Regression Example Chart
      :align: center

    """
    @property
    def params(self) -> Optional[LinearRegressionParameters]:
        """Parameters used in calculating the indicator's data points.

        :rtype: :class:`LinearRegressionParameters` or :obj:`None <python:None>`
        """
        return self._params

    @params.setter
    @class_sensitive(LinearRegressionParameters)
    def params(self, value):
        self._params = value


class LinearRegressionAngleOptions(LinearRegressionOptions):
    """Options to configure a Linear Regression Angle :term:`indicator`, which is a
    directional movement indicator which defines a trend at the moment of its birth and
    can be used to identify trend weakening.

    .. figure:: ../../../_static/linear-regression-angle-example.png
      :alt: Linear Regression Angle Example Chart
      :align: center

    """
    pass


class LinearRegressionInterceptOptions(LinearRegressionOptions):
    """Options to configure a Linear Regression Intercept :term:`indicator`.

    .. figure:: ../../../_static/linear-regression-intercept-example.png
      :alt: Linear Regression Intercept Example Chart
      :align: center

    """
    pass


class LinearRegressionSlopeOptions(LinearRegressionOptions):
    """Options to configure a Linear Regression Slope :term:`indicator`.

    .. figure:: ../../../_static/linear-regression-slope-example.png
      :alt: Linear Regression Slope Example Chart
      :align: center

    """
    pass


class TrendlineOptions(ComparableIndicatorOptions):
    """Options to configure a Trendline :term:`indicator`, which fits a straight line to
    the linked data using the Sum of Least Squares method.

    .. figure:: ../../../_static/trendline-example.png
      :alt: Trendline Example Chart
      :align: center

    """
    @property
    def params(self) -> Optional[TrendlineParameters]:
        """Parameters used in calculating the indicator's data points.

        :rtype: :class:`TrendlineParameters` or :obj:`None <python:None>`
        """
        return self._params

    @params.setter
    @class_sensitive(TrendlineParameters)
    def params(self, value):
        self._params = value

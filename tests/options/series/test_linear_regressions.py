"""Tests for ``highcharts.no_data``."""

import pytest

from json.decoder import JSONDecodeError

from highcharts_stock.options.series.linear_regressions import LinearRegressionSeries as cls
from highcharts_stock.options.series.linear_regressions import LinearRegressionAngleSeries as cls2
from highcharts_stock.options.series.linear_regressions import LinearRegressionInterceptSeries as cls3
from highcharts_stock.options.series.linear_regressions import LinearRegressionSlopeSeries as cls4
from highcharts_stock.options.series.linear_regressions import TrendlineSeries as cls5

from highcharts_stock import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal

STANDARD_PARAMS = [
    ({}, None),
]


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_LinearRegressionSeries__init__(kwargs, error):
    Class__init__(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_LinearRegressionSeries__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_LinearRegressionSeries_from_dict(kwargs, error):
    Class_from_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_LinearRegressionSeries_to_dict(kwargs, error):
    Class_to_dict(cls, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('series/linear_regressions/01.js', False, None),
    ('series/linear_regressions/error-01.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('series/linear_regressions/01.js', True, None),
    ('series/linear_regressions/error-01.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

])
def test_LinearRegressionSeries_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls, input_files, filename, as_file, error)


#### NEXT CLASS

@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_LinearRegressionAngleSeries__init__(kwargs, error):
    Class__init__(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_LinearRegressionAngleSeries__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_LinearRegressionAngleSeries_from_dict(kwargs, error):
    Class_from_dict(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_LinearRegressionAngleSeries_to_dict(kwargs, error):
    Class_to_dict(cls2, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('series/linear_regressions/02.js', False, None),
    ('series/linear_regressions/error-02.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('series/linear_regressions/02.js', True, None),
    ('series/linear_regressions/error-02.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

])
def test_LinearRegressionAngleSeries_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls2, input_files, filename, as_file, error)

#### NEXT CLASS

@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_LinearRegressionInterceptSeries__init__(kwargs, error):
    Class__init__(cls3, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_LinearRegressionInterceptSeries__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls3, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_LinearRegressionInterceptSeries_from_dict(kwargs, error):
    Class_from_dict(cls3, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_LinearRegressionInterceptSeries_to_dict(kwargs, error):
    Class_to_dict(cls3, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('series/linear_regressions/03.js', False, None),
    ('series/linear_regressions/error-03.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('series/linear_regressions/03.js', True, None),
    ('series/linear_regressions/error-03.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

])
def test_LinearRegressionInterceptSeries_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls3, input_files, filename, as_file, error)


#### NEXT CLASS

@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_LinearRegressionSlopeSeries__init__(kwargs, error):
    Class__init__(cls4, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_LinearRegressionSlopeSeries__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls4, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_LinearRegressionSlopeSeries_from_dict(kwargs, error):
    Class_from_dict(cls4, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_LinearRegressionSlopeSeries_to_dict(kwargs, error):
    Class_to_dict(cls4, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('series/linear_regressions/04.js', False, None),
    ('series/linear_regressions/error-04.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('series/linear_regressions/04.js', True, None),
    ('series/linear_regressions/error-04.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

])
def test_LinearRegressionSlopeSeries_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls4, input_files, filename, as_file, error)


#### NEXT CLASS

@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_TrendlineSeries__init__(kwargs, error):
    Class__init__(cls5, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_TrendlineSeries__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls5, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_TrendlineSeries_from_dict(kwargs, error):
    Class_from_dict(cls5, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_TrendlineSeries_to_dict(kwargs, error):
    Class_to_dict(cls5, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('series/linear_regressions/05.js', False, None),
    ('series/linear_regressions/error-05.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('series/linear_regressions/05.js', True, None),
    ('series/linear_regressions/error-05.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

])
def test_TrendlineSeries_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls5, input_files, filename, as_file, error)

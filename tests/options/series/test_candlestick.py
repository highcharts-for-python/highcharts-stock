"""Tests for ``highcharts.no_data``."""

import pytest

from json.decoder import JSONDecodeError

from highcharts_stock.options.series.candlestick import CandlestickSeries as cls
from highcharts_stock.options.series.candlestick import HollowCandlestickSeries as cls2
from highcharts_stock.options.series.candlestick import HeikinAshiSeries as cls3
from highcharts_stock import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal

STANDARD_PARAMS = [
    ({}, None),
]


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_CandlestickSeries__init__(kwargs, error):
    Class__init__(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_CandlestickSeries__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_CandlestickSeries_from_dict(kwargs, error):
    Class_from_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_CandlestickSeries_to_dict(kwargs, error):
    Class_to_dict(cls, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('series/candlestick/01.js', False, None),
    ('series/candlestick/error-01.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('series/candlestick/01.js', True, None),
    ('series/candlestick/error-01.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

])
def test_CandlestickSeries_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls, input_files, filename, as_file, error)

##### NEXT CLASS


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_HollowCandlestickSeries__init__(kwargs, error):
    Class__init__(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_HollowCandlestickSeries__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_HollowCandlestickSeries_from_dict(kwargs, error):
    Class_from_dict(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_HollowCandlestickSeries_to_dict(kwargs, error):
    Class_to_dict(cls2, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('series/candlestick/02.js', False, None),
    ('series/candlestick/error-02.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('series/candlestick/02.js', True, None),
    ('series/candlestick/error-02.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

])
def test_HollowCandlestickSeries_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls2, input_files, filename, as_file, error)


####### NEXT CLASS


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_HeikinAshiSeries__init__(kwargs, error):
    Class__init__(cls3, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_HeikinAshiSeries__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls3, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_HeikinAshiSeries_from_dict(kwargs, error):
    Class_from_dict(cls3, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_HeikinAshiSeries_to_dict(kwargs, error):
    Class_to_dict(cls3, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('series/candlestick/03.js', False, None),
    ('series/candlestick/error-03.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('series/candlestick/03.js', True, None),
    ('series/candlestick/error-03.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

])
def test_HeikinAshiSeries_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls3, input_files, filename, as_file, error)

"""Tests for ``highcharts.no_data``."""

import pytest

from json.decoder import JSONDecodeError

from highcharts_stock.options.annotations.stock_tools import CrookedLineAnnotation as cls1
from highcharts_stock.options.annotations.stock_tools import ElliottWaveAnnotation as cls2
from highcharts_stock.options.annotations.stock_tools import FibonacciAnnotation as cls3
from highcharts_stock.options.annotations.stock_tools import FibonacciTimeZonesAnnotation as cls4
from highcharts_stock.options.annotations.stock_tools import InfinityLineAnnotation as cls5
from highcharts_stock.options.annotations.stock_tools import MeasureAnnotation as cls6
from highcharts_stock.options.annotations.stock_tools import PitchforkAnnotation as cls7
from highcharts_stock.options.annotations.stock_tools import TimeCyclesAnnotation as cls8
from highcharts_stock.options.annotations.stock_tools import TunnelAnnotation as cls9
from highcharts_stock.options.annotations.stock_tools import VerticalLineAnnotation as cls10
from highcharts_stock import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal

STANDARD_PARAMS = [
    ({}, None),
]


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_cls1__init__(kwargs, error):
    Class__init__(cls1, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_cls1__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls1, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_cls1_from_dict(kwargs, error):
    Class_from_dict(cls1, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_cls1_to_dict(kwargs, error):
    Class_to_dict(cls1, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('annotations/stock_tools/01.js', False, None),

    ('annotations/stock_tools/error-01.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('annotations/stock_tools/01.js', True, None),

    ('annotations/stock_tools/error-01.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

])
def test_cls1_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls1, input_files, filename, as_file, error)


####### NEXT CLASS

@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_cls2__init__(kwargs, error):
    Class__init__(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_cls2__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_cls2_from_dict(kwargs, error):
    Class_from_dict(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_cls2_to_dict(kwargs, error):
    Class_to_dict(cls2, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('annotations/stock_tools/02.js', False, None),

    ('annotations/stock_tools/error-02.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('annotations/stock_tools/02.js', True, None),

    ('annotations/stock_tools/error-02.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

])
def test_cls2_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls2, input_files, filename, as_file, error)


####### NEXT CLASS

@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_cls3__init__(kwargs, error):
    Class__init__(cls3, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_cls3__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls3, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_cls3_from_dict(kwargs, error):
    Class_from_dict(cls3, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_cls3_to_dict(kwargs, error):
    Class_to_dict(cls3, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('annotations/stock_tools/03.js', False, None),

    ('annotations/stock_tools/error-03.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('annotations/stock_tools/03.js', True, None),

    ('annotations/stock_tools/error-03.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

])
def test_cls3_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls3, input_files, filename, as_file, error)


####### NEXT CLASS

@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_cls4__init__(kwargs, error):
    Class__init__(cls4, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_cls4__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls4, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_cls4_from_dict(kwargs, error):
    Class_from_dict(cls4, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_cls4_to_dict(kwargs, error):
    Class_to_dict(cls4, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('annotations/stock_tools/04.js', False, None),

    ('annotations/stock_tools/error-04.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('annotations/stock_tools/04.js', True, None),

    ('annotations/stock_tools/error-04.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

])
def test_cls4_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls4, input_files, filename, as_file, error)


####### NEXT CLASS

@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_cls5__init__(kwargs, error):
    Class__init__(cls5, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_cls5__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls5, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_cls5_from_dict(kwargs, error):
    Class_from_dict(cls5, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_cls5_to_dict(kwargs, error):
    Class_to_dict(cls5, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('annotations/stock_tools/05.js', False, None),

    ('annotations/stock_tools/error-05.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('annotations/stock_tools/05.js', True, None),

    ('annotations/stock_tools/error-05.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

])
def test_cls5_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls5, input_files, filename, as_file, error)


####### NEXT CLASS

@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_cls6__init__(kwargs, error):
    Class__init__(cls6, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_cls6__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls6, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_cls6_from_dict(kwargs, error):
    Class_from_dict(cls6, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_cls6_to_dict(kwargs, error):
    Class_to_dict(cls6, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('annotations/stock_tools/06.js', False, None),

    ('annotations/stock_tools/error-06.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('annotations/stock_tools/06.js', True, None),

    ('annotations/stock_tools/error-06.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

])
def test_cls6_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls6, input_files, filename, as_file, error)


####### NEXT CLASS

@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_cls7__init__(kwargs, error):
    Class__init__(cls7, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_cls7__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls7, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_cls7_from_dict(kwargs, error):
    Class_from_dict(cls7, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_cls7_to_dict(kwargs, error):
    Class_to_dict(cls7, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('annotations/stock_tools/07.js', False, None),

    ('annotations/stock_tools/error-07.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('annotations/stock_tools/07.js', True, None),

    ('annotations/stock_tools/error-07.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

])
def test_cls7_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls7, input_files, filename, as_file, error)


####### NEXT CLASS

@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_cls8__init__(kwargs, error):
    Class__init__(cls8, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_cls8__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls8, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_cls8_from_dict(kwargs, error):
    Class_from_dict(cls8, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_cls8_to_dict(kwargs, error):
    Class_to_dict(cls8, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('annotations/stock_tools/08.js', False, None),

    ('annotations/stock_tools/error-08.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('annotations/stock_tools/08.js', True, None),

    ('annotations/stock_tools/error-08.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

])
def test_cls8_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls8, input_files, filename, as_file, error)


####### NEXT CLASS

@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_cls9__init__(kwargs, error):
    Class__init__(cls9, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_cls9__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls9, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_cls9_from_dict(kwargs, error):
    Class_from_dict(cls9, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_cls9_to_dict(kwargs, error):
    Class_to_dict(cls9, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('annotations/stock_tools/09.js', False, None),

    ('annotations/stock_tools/error-09.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('annotations/stock_tools/09.js', True, None),

    ('annotations/stock_tools/error-09.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

])
def test_cls9_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls9, input_files, filename, as_file, error)


####### NEXT CLASS

@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_cls10__init__(kwargs, error):
    Class__init__(cls10, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_cls10__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls10, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_cls10_from_dict(kwargs, error):
    Class_from_dict(cls10, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_cls10_to_dict(kwargs, error):
    Class_to_dict(cls10, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('annotations/stock_tools/10.js', False, None),

    ('annotations/stock_tools/error-10.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('annotations/stock_tools/10.js', True, None),

    ('annotations/stock_tools/error-10.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

])
def test_cls10_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls10, input_files, filename, as_file, error)

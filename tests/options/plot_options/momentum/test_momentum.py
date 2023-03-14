"""Tests for ``highcharts.no_data``."""

import pytest

from json.decoder import JSONDecodeError

from highcharts_stock.options.plot_options.momentum import MomentumOptions as cls
from highcharts_stock.options.plot_options.momentum import OBVOptions as cls2
from highcharts_stock.options.plot_options.momentum import ROCOptions as cls3
from highcharts_stock.options.plot_options.momentum import RSIOptions as cls4

from highcharts_stock import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal

STANDARD_PARAMS = [
    ({}, None),
]


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_MomentumOptions__init__(kwargs, error):
    Class__init__(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_MomentumOptions__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_MomentumOptions_from_dict(kwargs, error):
    Class_from_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_MomentumOptions_to_dict(kwargs, error):
    Class_to_dict(cls, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('plot_options/momentum/momentum/01.js', False, None),
    ('plot_options/momentum/momentum/error-01.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('plot_options/momentum/momentum/01.js', True, None),
    ('plot_options/momentum/momentum/error-01.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

])
def test_MomentumOptions_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls, input_files, filename, as_file, error)


#### NEXT CLASS

@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_OBVOptions__init__(kwargs, error):
    Class__init__(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_OBVOptions__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_OBVOptions_from_dict(kwargs, error):
    Class_from_dict(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_OBVOptions_to_dict(kwargs, error):
    Class_to_dict(cls2, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('plot_options/momentum/momentum/02.js', False, None),
    ('plot_options/momentum/momentum/error-02.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('plot_options/momentum/momentum/02.js', True, None),
    ('plot_options/momentum/momentum/error-02.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

])
def test_OBVOptions_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls2, input_files, filename, as_file, error)

#### NEXT CLASS

@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_ROCOptions__init__(kwargs, error):
    Class__init__(cls3, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_ROCOptions__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls3, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_ROCOptions_from_dict(kwargs, error):
    Class_from_dict(cls3, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_ROCOptions_to_dict(kwargs, error):
    Class_to_dict(cls3, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('plot_options/momentum/momentum/03.js', False, None),
    ('plot_options/momentum/momentum/error-03.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('plot_options/momentum/momentum/03.js', True, None),
    ('plot_options/momentum/momentum/error-03.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

])
def test_ROCOptions_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls3, input_files, filename, as_file, error)


#### NEXT CLASS

@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_RSIOptions__init__(kwargs, error):
    Class__init__(cls4, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_RSIOptions__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls4, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_RSIOptions_from_dict(kwargs, error):
    Class_from_dict(cls4, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_RSIOptions_to_dict(kwargs, error):
    Class_to_dict(cls4, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('plot_options/momentum/momentum/04.js', False, None),
    ('plot_options/momentum/momentum/error-04.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('plot_options/momentum/momentum/04.js', True, None),
    ('plot_options/momentum/momentum/error-04.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

])
def test_RSIOptions_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls4, input_files, filename, as_file, error)

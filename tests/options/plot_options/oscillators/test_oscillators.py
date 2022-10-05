"""Tests for ``highcharts.no_data``."""

import pytest

from json.decoder import JSONDecodeError

from highcharts_stock.options.plot_options.oscillators import AroonOscillatorOptions as cls
from highcharts_stock.options.plot_options.oscillators import APOOptions as cls2
from highcharts_stock.options.plot_options.oscillators import CCIOptions as cls3
from highcharts_stock.options.plot_options.oscillators import ChaikinOptions as cls4
from highcharts_stock.options.plot_options.oscillators import CMOOptions as cls5
from highcharts_stock.options.plot_options.oscillators import DPOOptions as cls6
from highcharts_stock.options.plot_options.oscillators import TRIXOptions as cls7
from highcharts_stock.options.plot_options.oscillators import WilliamsROptions as cls8

from highcharts_stock import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal

STANDARD_PARAMS = [
    ({}, None),
]


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_AroonOscillatorOptions__init__(kwargs, error):
    Class__init__(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_AroonOscillatorOptions__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_AroonOscillatorOptions_from_dict(kwargs, error):
    Class_from_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_AroonOscillatorOptions_to_dict(kwargs, error):
    Class_to_dict(cls, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('plot_options/oscillators/oscillators/01.js', False, None),
    ('plot_options/oscillators/oscillators/error-01.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('plot_options/oscillators/oscillators/01.js', True, None),
    ('plot_options/oscillators/oscillators/error-01.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

])
def test_AroonOscillatorOptions_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls, input_files, filename, as_file, error)


#### NEXT CLASS

@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_APOOptions__init__(kwargs, error):
    Class__init__(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_APOOptions__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_APOOptions_from_dict(kwargs, error):
    Class_from_dict(cls2, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_APOOptions_to_dict(kwargs, error):
    Class_to_dict(cls2, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('plot_options/oscillators/oscillators/02.js', False, None),
    ('plot_options/oscillators/oscillators/error-02.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('plot_options/oscillators/oscillators/02.js', True, None),
    ('plot_options/oscillators/oscillators/error-02.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

])
def test_APOOptions_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls2, input_files, filename, as_file, error)

#### NEXT CLASS

@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_CCIOptions__init__(kwargs, error):
    Class__init__(cls3, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_CCIOptions__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls3, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_CCIOptions_from_dict(kwargs, error):
    Class_from_dict(cls3, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_CCIOptions_to_dict(kwargs, error):
    Class_to_dict(cls3, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('plot_options/oscillators/oscillators/03.js', False, None),
    ('plot_options/oscillators/oscillators/error-03.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('plot_options/oscillators/oscillators/03.js', True, None),
    ('plot_options/oscillators/oscillators/error-03.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

])
def test_CCIOptions_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls3, input_files, filename, as_file, error)


#### NEXT CLASS

@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_ChaikinOptions__init__(kwargs, error):
    Class__init__(cls4, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_ChaikinOptions__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls4, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_ChaikinOptions_from_dict(kwargs, error):
    Class_from_dict(cls4, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_ChaikinOptions_to_dict(kwargs, error):
    Class_to_dict(cls4, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('plot_options/oscillators/oscillators/04.js', False, None),
    ('plot_options/oscillators/oscillators/error-04.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('plot_options/oscillators/oscillators/04.js', True, None),
    ('plot_options/oscillators/oscillators/error-04.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

])
def test_ChaikinOptions_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls4, input_files, filename, as_file, error)


#### NEXT CLASS

@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_CMOOptions__init__(kwargs, error):
    Class__init__(cls5, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_CMOOptions__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls5, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_CMOOptions_from_dict(kwargs, error):
    Class_from_dict(cls5, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_CMOOptions_to_dict(kwargs, error):
    Class_to_dict(cls5, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('plot_options/oscillators/oscillators/05.js', False, None),
    ('plot_options/oscillators/oscillators/error-05.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('plot_options/oscillators/oscillators/05.js', True, None),
    ('plot_options/oscillators/oscillators/error-05.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

])
def test_CMOOptions_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls5, input_files, filename, as_file, error)


#### NEXT CLASS

@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_DPOOptions__init__(kwargs, error):
    Class__init__(cls6, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_DPOOptions__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls6, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_DPOOptions_from_dict(kwargs, error):
    Class_from_dict(cls6, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_DPOOptions_to_dict(kwargs, error):
    Class_to_dict(cls6, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('plot_options/oscillators/oscillators/06.js', False, None),
    ('plot_options/oscillators/oscillators/error-06.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('plot_options/oscillators/oscillators/06.js', True, None),
    ('plot_options/oscillators/oscillators/error-06.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

])
def test_DPOOptions_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls6, input_files, filename, as_file, error)


#### NEXT CLASS

@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_TRIXOptions__init__(kwargs, error):
    Class__init__(cls7, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_TRIXOptions__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls7, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_TRIXOptions_from_dict(kwargs, error):
    Class_from_dict(cls7, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_TRIXOptions_to_dict(kwargs, error):
    Class_to_dict(cls7, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('plot_options/oscillators/oscillators/07.js', False, None),
    ('plot_options/oscillators/oscillators/error-07.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('plot_options/oscillators/oscillators/07.js', True, None),
    ('plot_options/oscillators/oscillators/error-07.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

])
def test_TRIXOptions_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls7, input_files, filename, as_file, error)


#### NEXT CLASS

@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_WilliamsROptions__init__(kwargs, error):
    Class__init__(cls8, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_WilliamsROptions__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls8, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_WilliamsROptions_from_dict(kwargs, error):
    Class_from_dict(cls8, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_WilliamsROptions_to_dict(kwargs, error):
    Class_to_dict(cls8, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('plot_options/oscillators/oscillators/08.js', False, None),
    ('plot_options/oscillators/oscillators/error-08.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('plot_options/oscillators/oscillators/08.js', True, None),
    ('plot_options/oscillators/oscillators/error-08.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

])
def test_WilliamsROptions_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls8, input_files, filename, as_file, error)

"""Tests for ``highcharts.no_data``."""

import pytest

from json.decoder import JSONDecodeError

from highcharts_stock.options.series.flags import FlagsSeries as cls
from highcharts_stock import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal

STANDARD_PARAMS = [
    ({}, None),
]


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_FlagsSeries__init__(kwargs, error):
    Class__init__(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test_FlagsSeries__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_FlagsSeries_from_dict(kwargs, error):
    Class_from_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_FlagsSeries_to_dict(kwargs, error):
    Class_to_dict(cls, kwargs, error)


@pytest.mark.parametrize('filename, as_file, error', [
    ('series/flags/01.js', False, None),
    ('series/flags/error-01.js',
     False,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

    ('series/flags/01.js', True, None),
    ('series/flags/error-01.js',
     True,
     (errors.HighchartsValueError,
      errors.HighchartsParseError,
      JSONDecodeError,
      TypeError,
      ValueError)),

])
def test_FlagsSeries_from_js_literal(input_files, filename, as_file, error):
    Class_from_js_literal(cls, input_files, filename, as_file, error)


def test_FlagsSeries_to_js_literal():
    data_points = [{'x': 1635255000000, 'title': 'Sell', 'text': '1st text'},
                   {'x': 1635427800000, 'title': 'Sell', 'text': '2nd text'},
                   {'x': 1636119000000, 'title': 'Buy', 'text': '3rd text'},
                   {'x': 1636381800000, 'title': 'Buy', 'text': '4th text'},
                   {'x': 1636468200000, 'title': 'Sell', 'text': '5th text'}]
    flag_series = cls(data = data_points,
                      on_series = 'dataseries',
                      shape = 'squarepin',
                      name = 'Flags on series')
    assert flag_series is not None
    assert isinstance(flag_series, cls) is True
    
    result = flag_series.to_js_literal()
    assert result is not None
    assert isinstance(result, str) is True
    assert 'data:' in result
    assert 'Sell' in result
    assert '1st text' in result
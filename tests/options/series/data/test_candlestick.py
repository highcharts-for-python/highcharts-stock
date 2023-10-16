"""Tests for ``highcharts.no_data``."""

import pytest

from json.decoder import JSONDecodeError

from highcharts_stock.options.series.data.candlestick import CandlestickData as cls
from highcharts_stock import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal

STANDARD_PARAMS = [
    ({}, None),
]


def test_bugfix40_CandlestickData_serialization():
    from highcharts_stock.chart import Chart
    
    ohlcv = [[1665504000000, 20, 21, 19, 20],
             [1665590400000, 21, 23, 21, 22]]
    my_chart = Chart.from_array(ohlcv, series_type='candlestick')
    
    assert my_chart is not None
    assert len(my_chart.options.series) == 1
    assert len(my_chart.options.series[0].data) == len(ohlcv)
    for data_point in my_chart.options.series[0].data:
        assert data_point.open is not None
        
        as_js_literal = my_chart.options.series[0].data[0].to_js_literal()
        assert as_js_literal is not None
        assert 'null' not in as_js_literal

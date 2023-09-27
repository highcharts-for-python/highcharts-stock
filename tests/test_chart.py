"""Tests for ``highcharts.no_data``."""

import pytest

from json.decoder import JSONDecodeError

from highcharts_stock.chart import Chart as cls
from highcharts_stock import errors
from tests.fixtures import input_files, check_input_file, to_camelCase, to_js_dict, \
    Class__init__, Class__to_untrimmed_dict, Class_from_dict, Class_to_dict, \
    Class_from_js_literal, Class_from_js_literal_with_expected, run_pandas_tests

STANDARD_PARAMS = [
    ({}, None),
]


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test__init__(kwargs, error):
    Class__init__(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error', STANDARD_PARAMS)
def test__to_untrimmed_dict(kwargs, error):
    Class__to_untrimmed_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_from_dict(kwargs, error):
    Class_from_dict(cls, kwargs, error)


@pytest.mark.parametrize('kwargs, error',  STANDARD_PARAMS)
def test_to_dict(kwargs, error):
    Class_to_dict(cls, kwargs, error)


@pytest.mark.parametrize('input_filename, expected_filename, as_file, error', [
    ('chart_obj/01-input.js',
     'chart_obj/01-expected.js',
     False,
     None),
    ('chart_obj/01-input.js',
     'chart_obj/01-expected.js',
     False,
     None),
])
def test_from_js_literal(input_files, input_filename, expected_filename, as_file, error):
    Class_from_js_literal_with_expected(cls,
                                        input_files,
                                        input_filename,
                                        expected_filename,
                                        as_file,
                                        error)


@pytest.mark.parametrize('kwargs, expected_series, expected_data_points, error', [
    ({}, 0, [], None),

    ({
        'series': [
            {
                'data': [[1, 2], [3, 4]],
                'type': 'line'
            }
        ]
    }, 1, [(0, 2)], None),
    ({
        'series': {
            'data': [[1, 2], [3, 4]],
            'type': 'line'
        }
    }, 1, [(0, 2)], None),
    
    ({
        'data': [[1, 2], [3, 4]],
        'series_type': 'line'
    }, 1, [(0, 2)], None),

    ({
        'data': [[1, 2], [3, 4]],
    }, 1, [(0, 2)], errors.HighchartsValueError),

])
def test_issue90_one_shot_creation(kwargs, expected_series, expected_data_points, error):
    if not error:
        result = cls(**kwargs)
        assert result is not None
        if kwargs:
            assert getattr(result, 'options') is not None
            assert getattr(result.options, 'series') is not None
            assert len(result.options.series) == expected_series
            for item in expected_data_points:
                assert len(result.options.series[item[0]].data) == item[1]
    else:
        with pytest.raises(error):
            result = cls(**kwargs)
            

@pytest.mark.parametrize('filename, error', [
    ('test-data-files/nst-est2019-01.csv', None),
])
def test_from_pandas_in_rows(run_pandas_tests, input_files, filename, error):
    if not run_pandas_tests:
        return

    import pandas
    
    input_file = check_input_file(input_files, filename)
    df = pandas.read_csv(input_file, header = 0, thousands = ',')
    df.index = df['Geographic Area']
    df = df.drop(columns = ['Geographic Area'])
    print(df)
    
    if not error:
        result = cls.from_pandas_in_rows(df)
        assert result is not None
        assert isinstance(result, cls)
        assert len(result.options.series) == len(df)
        for series in result.options.series:
            assert series.data is not None
            assert len(series.data) == len(df.columns)
    else:
        with pytest.raises(error):
            result = cls.from_pandas_in_rows(df)


def prep_df(df):
    df.index = df['Geographic Area']
    df = df.drop(columns = ['Geographic Area'])
    
    return df


def reduce_to_two_columns(df):
    df = df[['Geographic Area', '2010']]
    
    return df


@pytest.mark.parametrize('filename, kwargs, pre_test_df_func, expected_series, expected_data_points, error', [
    # SCENARIO 0: Series in Rows
    ('test-data-files/nst-est2019-01.csv',
     {
         'series_in_rows': True
     },
     prep_df,
     57,
     10,
     None),
    
    # SCENARIO 1a: Has Property Map, Single Series
    ('test-data-files/nst-est2019-01.csv',
     {
         'property_map': {
             'name': 'Geographic Area',
         },
         'series_in_rows': False
     },
     None,
     1,
     57,
     None),

    # SCENARIO 1b: Has Property Map, Multiple Series
    ('test-data-files/nst-est2019-01.csv',
     {
         'property_map': {
             'x': ['Geographic Area', '2010']
         },
         'series_in_rows': False
     },
     None,
     2,
     57,
     None),
    
    # SCENARIO 2a: Single Property in KWARGS
    ('test-data-files/nst-est2019-01.csv',
     {
         'x': 'Geographic Area',
         'y': '2010'
     },
     None,
     1,
     57,
     None),
    
    # SCENARIO 3a: Exact Match on Column Count
    ('test-data-files/nst-est2019-01.csv',
     {},
     reduce_to_two_columns,
     1,
     57,
     None),
    
    # SCENARIO 3b: Multiple Series, Multipled Columns
    ('test-data-files/nst-est2019-01.csv',
     {},
     prep_df,
     5,
     57,
     None),

    # SCENARIO 4: Mismatched Columns
    # NOTE: On SeriesBase, this will actually return one series per column.
    # This is because SeriesBase supports 1D arrays.
    ('test-data-files/nst-est2019-01.csv',
     {},
     None,
     11,
     57,
     None),
    
])
def test_from_pandas(run_pandas_tests,
                     input_files,
                     filename,
                     kwargs,
                     pre_test_df_func,
                     expected_series,
                     expected_data_points,
                     error):
    if not run_pandas_tests:
        return

    import pandas

    input_file = check_input_file(input_files, filename)
    df = pandas.read_csv(input_file, header = 0, thousands = ',')
    if pre_test_df_func:
        df = pre_test_df_func(df)
    print(df)

    if not error:
        result = cls.from_pandas(df, **kwargs)
        assert result is not None
        assert isinstance(result, cls)
        assert len(result.options.series) == expected_series
        for series in result.options.series:
            assert series.data is not None
            assert len(series.data) == expected_data_points
    else:
        with pytest.raises(error):
            result = cls.from_pandas(df, **kwargs)



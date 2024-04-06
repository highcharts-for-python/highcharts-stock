"""Defines a set of constants that are used throughout the library."""
from highcharts_core.constants import *

STOCK_INCLUDE_LIBS = [x for x in INCLUDE_LIBS]
STOCK_INCLUDE_LIBS.extend([
    'https://code.highcharts.com/stock/modules/stock.js',
    'https://code.highcharts.com/stock/modules/heikinashi.js',
    'https://code.highcharts.com/stock/modules/hollowcandlestick.js',
    'https://code.highcharts.com/stock/indicators/indicators-all.js',
    'https://code.highcharts.com/modules/price-indicator.js',
    'https://code.highcharts.com/modules/full-screen.js',
])


STOCK_INCLUDE_STR = INCLUDE_STR + """
    <script src="https://code.highcharts.com/stock/modules/stock.js"/>
    <script src="https://code.highcharts.com/stock/modules/heikinashi.js"/>
    <script src="https://code.highcharts.com/stock/modules/hollowcandlestick.js"/>
    <script src="https://code.highcharts.com/stock/indicators/indicators-all.js"/>
    <script src="https://code.highcharts.com/modules/price-indicator.js"/>
    <script src="https://code.highcharts.com/modules/full-screen.js"/>
    <script src="https://code.highcharts.com/modules/stock-tools.js"/>
"""


STOCK_TOOLS_INCLUDE_LIBS = [
    'https://code.highcharts.com/css/stocktools/gui.css',
    'https://code.highcharts.com/css/annotations/popup.css',
    'https://code.highcharts.com/modules/stock-tools.js'
]

STOCK_TOOLS_INCLUDE_STR = """
    <link rel="stylesheet" type="text/css" href="https://code.highcharts.com/css/stocktools/gui.css">
    <link rel="stylesheet" type="text/css" href="https://code.highcharts.com/css/annotations/popup.css">
"""


RANGE_SELECTOR_BUTTON_TYPES = [
    'all',
    'millisecond',
    'second',
    'minute',
    'hour',
    'day',
    'week',
    'month',
    'ytd',
    'year',
]
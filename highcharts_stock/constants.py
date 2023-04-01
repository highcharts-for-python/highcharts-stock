"""Defines a set of constants that are used throughout the library."""
from highcharts_core.constants import *

STOCK_INCLUDE_LIBS = INCLUDE_LIBS + [
    'https://code.highcharts.com/stock/modules/stock.js',
    'https://code.highcharts.com/stock/modules/heikinashi.js',
    'https://code.highcharts.com/stock/modules/hollowcandlestick.js',
    'https://code.highcharts.com/stock/indicators/indicators-all.js',
    'https://code.highcharts.com/modules/price-indicator.js',
    'https://code.highcharts.com/modules/full-screen.js',
    'https://code.highcharts.com/modules/stock-tools.js',
]


STOCK_INCLUDE_STR = INCLUDE_STR + """
    <script src="https://code.highcharts.com/stock/modules/stock.js"/>
    <script src="https://code.highcharts.com/stock/modules/heikinashi.js"/>
    <script src="https://code.highcharts.com/stock/modules/hollowcandlestick.js"/>
    <script src="https://code.highcharts.com/stock/indicators/indicators-all.js"/>
    <script src="https://code.highcharts.com/modules/price-indicator.js"/>
    <script src="https://code.highcharts.com/modules/full-screen.js"/>
    <script src="https://code.highcharts.com/modules/stock-tools.js"/>
"""

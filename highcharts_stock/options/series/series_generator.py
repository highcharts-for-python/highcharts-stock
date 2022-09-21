from typing import Optional

import json

from validator_collection import validators, checkers

from highcharts_python import errors

from highcharts_python.options.series.base import SeriesBase
from highcharts_python.options.series.arcdiagram import ArcDiagramSeries
from highcharts_python.options.series.area import AreaSeries
from highcharts_python.options.series.area import AreaRangeSeries
from highcharts_python.options.series.area import AreaSplineSeries
from highcharts_python.options.series.area import AreaSplineRangeSeries
from highcharts_python.options.series.area import LineSeries
from highcharts_python.options.series.area import StreamGraphSeries
from highcharts_python.options.series.bar import BarSeries
from highcharts_python.options.series.bar import ColumnSeries
from highcharts_python.options.series.bar import ColumnPyramidSeries
from highcharts_python.options.series.bar import ColumnRangeSeries
from highcharts_python.options.series.bar import CylinderSeries
from highcharts_python.options.series.bar import VariwideSeries
from highcharts_python.options.series.bar import WaterfallSeries
from highcharts_python.options.series.bar import WindBarbSeries
from highcharts_python.options.series.bar import XRangeSeries
from highcharts_python.options.series.bellcurve import BellCurveSeries
from highcharts_python.options.series.boxplot import BoxPlotSeries
from highcharts_python.options.series.boxplot import ErrorBarSeries
from highcharts_python.options.series.bubble import BubbleSeries
from highcharts_python.options.series.bullet import BulletSeries
from highcharts_python.options.series.dependencywheel import DependencyWheelSeries
from highcharts_python.options.series.dumbbell import DumbbellSeries
from highcharts_python.options.series.dumbbell import LollipopSeries
from highcharts_python.options.series.funnel import FunnelSeries
from highcharts_python.options.series.funnel import Funnel3DSeries
from highcharts_python.options.series.gauge import GaugeSeries
from highcharts_python.options.series.gauge import SolidGaugeSeries
from highcharts_python.options.series.heatmap import HeatmapSeries
from highcharts_python.options.series.heatmap import TilemapSeries
from highcharts_python.options.series.histogram import HistogramSeries
from highcharts_python.options.series.item import ItemSeries
from highcharts_python.options.series.networkgraph import NetworkGraphSeries
from highcharts_python.options.series.organization import OrganizationSeries
from highcharts_python.options.series.packedbubble import PackedBubbleSeries
from highcharts_python.options.series.pareto import ParetoSeries
from highcharts_python.options.series.pie import PieSeries
from highcharts_python.options.series.pie import VariablePieSeries
from highcharts_python.options.series.polygon import PolygonSeries
from highcharts_python.options.series.pyramid import PyramidSeries
from highcharts_python.options.series.pyramid import Pyramid3DSeries
from highcharts_python.options.series.sankey import SankeySeries
from highcharts_python.options.series.scatter import ScatterSeries
from highcharts_python.options.series.scatter import Scatter3DSeries
from highcharts_python.options.series.spline import SplineSeries
from highcharts_python.options.series.sunburst import SunburstSeries
from highcharts_python.options.series.timeline import TimelineSeries
from highcharts_python.options.series.treemap import TreemapSeries
from highcharts_python.options.series.vector import VectorSeries
from highcharts_python.options.series.venn import VennSeries
from highcharts_python.options.series.wordcloud import WordcloudSeries

# Highcharts Stock-specific Series
from highcharts_stock.options.series.base import IndicatorSeriesBase
from highcharts_stock.options.series.abands import (AbandsSeries,
                                                    PCSeries,
                                                    KeltnerChannelsSeries,
                                                    BBSeries)
from highcharts_stock.options.series.ad import ADSeries
from highcharts_stock.options.series.aroon import AroonSeries
from highcharts_stock.options.series.atr import ATRSeries, NATRSeries
from highcharts_stock.options.series.averages import (DEMASeries,
                                                      EMASeries,
                                                      SMASeries,
                                                      TEMASeries,
                                                      VWAPSeries,
                                                      WMASeries)
from highcharts_stock.options.series.candlestick import (CandlestickSeries,
                                                         HollowCandlestickSeries,
                                                         HeikinAshiSeries)
from highcharts_stock.options.series.disparity_index import DisparityIndexSeries
from highcharts_stock.options.series.dmi import DMISeries
from highcharts_stock.options.series.flags import FlagsSeries
from highcharts_stock.options.series.hlc import (HLCSeries,
                                                       OHLCSeries)
from highcharts_stock.options.series.linear_regressions import (LinearRegressionSeries,
                                                                LinearRegressionAngleSeries,
                                                                LinearRegressionInterceptSeries,
                                                                LinearRegressionSlopeSeries,
                                                                TrendlineSeries)
from highcharts_stock.options.series.pivot_points import PivotPointsSeries
from highcharts_stock.options.series.price_envelopes import PriceEnvelopesSeries
from highcharts_stock.options.series.psar import PSARSeries
from highcharts_stock.options.series.vbp import VBPSeries
from highcharts_stock.options.series.zigzag import ZigZagSeries
from highcharts_stock.options.series.momentum import (MomentumSeries,
                                                            OBVSeries,
                                                            ROCSeries,
                                                            RSISeries)
from highcharts_stock.options.series.momentum.ikh import IKHSeries
from highcharts_stock.options.series.momentum.macd import MACDSeries
from highcharts_stock.options.series.momentum.supertrend import SupertrendSeries
from highcharts_stock.options.series.oscillators import (AroonOscillatorSeries,
                                                         APOSeries,
                                                         CCISeries,
                                                         ChaikinSeries,
                                                         CMOSeries,
                                                         DPOSeries,
                                                         TRIXSeries,
                                                         WilliamsRSeries)
from highcharts_stock.options.series.oscillators.ao import AOSeries
from highcharts_stock.options.series.oscillators.klinger import KlingerSeries
from highcharts_stock.options.series.oscillators.money_flow import (MFISeries,
                                                                          CMFSeries)
from highcharts_stock.options.series.oscillators.ppo import PPOSeries
from highcharts_stock.options.series.oscillators.stochastic import (StochasticSeries,
                                                                    SlowStochasticSeries)


SERIES_CLASSES = {
    'arcdiagram': ArcDiagramSeries,
    'areaseries': AreaSeries,
    'arearange': AreaRangeSeries,
    'areaspline': AreaSplineSeries,
    'areasplinerange': AreaSplineRangeSeries,
    'line': LineSeries,
    'streamgraph': StreamGraphSeries,
    'bar': BarSeries,
    'column': ColumnSeries,
    'columnpyramid': ColumnPyramidSeries,
    'columnrange': ColumnRangeSeries,
    'cylinder': CylinderSeries,
    'variwide': VariwideSeries,
    'waterfall': WaterfallSeries,
    'windbarb': WindBarbSeries,
    'xrange': XRangeSeries,
    'bellcurve': BellCurveSeries,
    'boxplot': BoxPlotSeries,
    'errorbar': ErrorBarSeries,
    'bubble': BubbleSeries,
    'bullet': BulletSeries,
    'dependencywheel': DependencyWheelSeries,
    'dumbbell': DumbbellSeries,
    'lollipop': LollipopSeries,
    'funnel': FunnelSeries,
    'funnel3d': Funnel3DSeries,
    'gauge': GaugeSeries,
    'solidgauge': SolidGaugeSeries,
    'heatmap': HeatmapSeries,
    'tilemap': TilemapSeries,
    'histogram': HistogramSeries,
    'item': ItemSeries,
    'networkgraph': NetworkGraphSeries,
    'organization': OrganizationSeries,
    'packedbubble': PackedBubbleSeries,
    'pareto': ParetoSeries,
    'pie': PieSeries,
    'variablepie': VariablePieSeries,
    'polygon': PolygonSeries,
    'pyramid': PyramidSeries,
    'pyramid3d': Pyramid3DSeries,
    'sankey': SankeySeries,
    'scatter': ScatterSeries,
    'scatter3d': Scatter3DSeries,
    'spline': SplineSeries,
    'sunburst': SunburstSeries,
    'timeline': TimelineSeries,
    'treemap': TreemapSeries,
    'vector': VectorSeries,
    'venn': VennSeries,
    'wordcloud': WordcloudSeries,

    # Highcharts for Stock Series Types
    'abands': AbandsSeries,
    'ad': ADSeries,
    'ao': AOSeries,
    'apo': APOSeries,
    'aroon': AroonSeries,
    'aroonoscillator': AroonOscillatorSeries,
    'atr': ATRSeries,
    'bb': BBSeries,
    'candlestick': CandlestickSeries,
    'cci': CCISeries,
    'chaikin': ChaikinSeries,
    'cmf': CMFSeries,
    'cmo': CMOSeries,
    'dema': DEMASeries,
    'disparityindex': DisparityIndexSeries,
    'dmi': DMISeries,
    'dpo': DPOSeries,
    'ema': EMASeries,
    'flags': FlagsSeries,
    'heikinashi': HeikinAshiSeries,
    'hlc': HLCSeries,
    'hollowcandlestick': HollowCandlestickSeries,
    'ikh': IKHSeries,
    'keltnerchannels': KeltnerChannelsSeries,
    'klinger': KlingerSeries,
    'linearregression': LinearRegressionSeries,
    'linearregressionngle': LinearRegressionAngleSeries,
    'linearregressionintercept': LinearRegressionInterceptSeries,
    'linearregressionslope': LinearRegressionSlopeSeries,
    'macd': MACDSeries,
    'mfi': MFISeries,
    'momentum': MomentumSeries,
    'natr': NATRSeries,
    'obv': OBVSeries,
    'ohlc': OHLCSeries,
    'pc': PCSeries,
    'pivotpoints': PivotPointsSeries,
    'ppo': PPOSeries,
    'priceenvelopes': PriceEnvelopesSeries,
    'psar': PSARSeries,
    'roc': ROCSeries,
    'rsi': RSISeries,
    'slowstochastic': SlowStochasticSeries,
    'sma': SMASeries,
    'stochastic': StochasticSeries,
    'supertrend': SupertrendSeries,
    'tema': TEMASeries,
    'trendline': TrendlineSeries,
    'trix': TRIXSeries,
    'vbp': VBPSeries,
    'vwap': VWAPSeries,
    'williamsr': WilliamsRSeries,
    'wma': WMASeries,
    'zigzag': ZigZagSeries,
}

STOCK_SERIES_LIST = [
    # Highcharts for Stock Series Types
    'abands',
    'ad',
    'ao',
    'apo',
    'aroon',
    'aroonoscillator',
    'atr',
    'bb',
    'candlestick',
    'cci',
    'chaikin',
    'cmf',
    'cmo',
    'dema',
    'disparityindex',
    'dmi',
    'dpo',
    'ema',
    'flags',
    'heikinashi',
    'hlc',
    'hollowcandlestick',
    'ikh',
    'keltnerchannels',
    'klinger',
    'linearregression',
    'linearregressionngle',
    'linearregressionintercept',
    'linearregressionslope',
    'macd',
    'mfi',
    'momentum',
    'natr',
    'obv',
    'ohlc',
    'pc',
    'pivotpoints',
    'ppo',
    'priceenvelopes',
    'psar',
    'roc',
    'rsi',
    'slowstochastic',
    'sma',
    'stochastic',
    'supertrend',
    'tema',
    'trendline',
    'trix',
    'vbp',
    'vwap',
    'williamsr',
    'wma',
    'zigzag',
]


def create_series_obj(value, default_type = None) -> Optional[SeriesBase | IndicatorSeriesBase]:
    """Create an instance descended from :class:`SeriesBase` or
    :class:`IndicatorSeriesBase`.

    :param value: The input that should be de-serialized to a :class:`SeriesBase`
      instance. Expected to be either a :class:`SeriesBase` instance, a
      :class:`dict <python:dict>`, or a JSON :class:`str <python:str>`

    :param default_type: The default series type to apply if not specified in
      ``value``. Defaults to :obj:`None <python:None>`
    :type default_type: :class:`str <python:str>` or :obj:`None <python:None>`

    :returns: A :class:`SeriesBase` or :class:`IndicatorSeriesBase`(descendant) instance
    :rtype: :class:`SeriesBase` or :class:`IndicatorSeriesBase` or
      :obj:`None <python:None>`
    """
    if not value:
        return None

    if isinstance(value, (SeriesBase, IndicatorSeriesBase)):
        return value

    if isinstance(value, dict):
        type_ = value.get('type', default_type)
        if not type_:
            raise errors.HighchartsValueError('To instantiate a Series, the "type" must '
                                              'be provided. No "type" key was found.')
        cls = SERIES_CLASSES.get(type_, default_type)
        if not cls:
            raise errors.HighchartsValueError(f'create_series_obj expects a value with '
                                              f'a recognized "type". However, received a '
                                              f'"type" value that was not recognized: '
                                              f'{type_}')

        instance = cls.from_dict(value)
    elif isinstance(value, str):
        if 'data:' in value:
            try:
                preliminary = SeriesBase.from_js_literal(value)
                type_ = preliminary.type
            except errors.HighchartsParseError:
                preliminary_as_dict = json.loads(value)

                type_ = preliminary_as_dict.get('type', default_type)
        else:
            try:
                preliminary = IndicatorSeriesBase.from_js_literal(value)
                type_ = preliminary.type
            except errors.HighchartsParseError:
                preliminary_as_dict = json.loads(value)

                type_ = preliminary_as_dict.get('type', default_type)

        if not type_:
            raise errors.HighchartsValueError('To instantiate a Series, the "type" must '
                                              'be provided. No "type" key was found.')
        cls = SERIES_CLASSES.get(type_, default_type)
        if not cls:
            raise errors.HighchartsValueError(f'create_series_obj expects a value with '
                                              f'a recognized "type". However, received a '
                                              f'"type" value that was not recognized: '
                                              f'{type_}')

        try:
            instance = cls.from_js_literal(value)
        except errors.HighchartsParseError:
            instance = cls.from_json(value)

    return instance

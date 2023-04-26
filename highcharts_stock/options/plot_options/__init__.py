from typing import Optional

from highcharts_core.decorators import class_sensitive
from highcharts_core.options.plot_options import PlotOptions as PlotOptionsBase

from highcharts_stock.options.plot_options.arcdiagram import ArcDiagramOptions
from highcharts_stock.options.plot_options.area import AreaOptions
from highcharts_stock.options.plot_options.area import AreaRangeOptions
from highcharts_stock.options.plot_options.area import AreaSplineOptions
from highcharts_stock.options.plot_options.area import AreaSplineRangeOptions
from highcharts_stock.options.plot_options.bar import BarOptions
from highcharts_stock.options.plot_options.bellcurve import BellCurveOptions
from highcharts_stock.options.plot_options.boxplot import BoxPlotOptions
from highcharts_stock.options.plot_options.bubble import BubbleOptions
from highcharts_stock.options.plot_options.bullet import BulletOptions
from highcharts_stock.options.plot_options.bar import ColumnOptions
from highcharts_stock.options.plot_options.bar import ColumnPyramidOptions
from highcharts_stock.options.plot_options.bar import ColumnRangeOptions
from highcharts_stock.options.plot_options.bar import CylinderOptions
from highcharts_stock.options.plot_options.dependencywheel import DependencyWheelOptions
from highcharts_stock.options.plot_options.dumbbell import DumbbellOptions
from highcharts_stock.options.plot_options.boxplot import ErrorBarOptions
from highcharts_stock.options.plot_options.funnel import FunnelOptions
from highcharts_stock.options.plot_options.funnel import Funnel3DOptions
from highcharts_stock.options.plot_options.gauge import GaugeOptions
from highcharts_stock.options.plot_options.heatmap import HeatmapOptions
from highcharts_stock.options.plot_options.histogram import HistogramOptions
from highcharts_stock.options.plot_options.item import ItemOptions
from highcharts_stock.options.plot_options.area import LineOptions
from highcharts_stock.options.plot_options.dumbbell import LollipopOptions
from highcharts_stock.options.plot_options.networkgraph import NetworkGraphOptions
from highcharts_stock.options.plot_options.organization import OrganizationOptions
from highcharts_stock.options.plot_options.packedbubble import PackedBubbleOptions
from highcharts_stock.options.plot_options.pareto import ParetoOptions
from highcharts_stock.options.plot_options.pictorial import PictorialOptions
from highcharts_stock.options.plot_options.pie import PieOptions
from highcharts_stock.options.plot_options.polygon import PolygonOptions
from highcharts_stock.options.plot_options.pyramid import PyramidOptions
from highcharts_stock.options.plot_options.pyramid import Pyramid3DOptions
from highcharts_stock.options.plot_options.sankey import SankeyOptions
from highcharts_stock.options.plot_options.scatter import ScatterOptions
from highcharts_stock.options.plot_options.scatter import Scatter3DOptions
from highcharts_stock.options.plot_options.series import SeriesOptions
from highcharts_stock.options.plot_options.gauge import SolidGaugeOptions
from highcharts_stock.options.plot_options.spline import SplineOptions
from highcharts_stock.options.plot_options.area import StreamGraphOptions
from highcharts_stock.options.plot_options.sunburst import SunburstOptions
from highcharts_stock.options.plot_options.heatmap import TilemapOptions
from highcharts_stock.options.plot_options.timeline import TimelineOptions
from highcharts_stock.options.plot_options.treegraph import TreegraphOptions
from highcharts_stock.options.plot_options.treemap import TreemapOptions
from highcharts_stock.options.plot_options.pie import VariablePieOptions
from highcharts_stock.options.plot_options.bar import VariwideOptions
from highcharts_stock.options.plot_options.vector import VectorOptions
from highcharts_stock.options.plot_options.venn import VennOptions
from highcharts_stock.options.plot_options.bar import WaterfallOptions
from highcharts_stock.options.plot_options.bar import WindBarbOptions
from highcharts_stock.options.plot_options.wordcloud import WordcloudOptions
from highcharts_stock.options.plot_options.bar import XRangeOptions

# Highcharts Stock Plot Options
from highcharts_stock.options.plot_options.abands import (AbandsOptions,
                                                          PCOptions,
                                                          KeltnerChannelsOptions,
                                                          BBOptions)
from highcharts_stock.options.plot_options.ad import ADOptions
from highcharts_stock.options.plot_options.aroon import AroonOptions
from highcharts_stock.options.plot_options.atr import ATROptions, NATROptions
from highcharts_stock.options.plot_options.averages import (DEMAOptions,
                                                            EMAOptions,
                                                            SMAOptions,
                                                            TEMAOptions,
                                                            VWAPOptions,
                                                            WMAOptions)
from highcharts_stock.options.plot_options.candlestick import (CandlestickOptions,
                                                               HollowCandlestickOptions,
                                                               HeikinAshiOptions)
from highcharts_stock.options.plot_options.disparity_index import DisparityIndexOptions
from highcharts_stock.options.plot_options.dmi import DMIOptions
from highcharts_stock.options.plot_options.flags import FlagsOptions
from highcharts_stock.options.plot_options.hlc import (HLCOptions,
                                                       OHLCOptions)
from highcharts_stock.options.plot_options.linear_regressions import (LinearRegressionOptions,
                                                                      LinearRegressionAngleOptions,
                                                                      LinearRegressionInterceptOptions,
                                                                      LinearRegressionSlopeOptions,
                                                                      TrendlineOptions)
from highcharts_stock.options.plot_options.pivot_points import PivotPointsOptions
from highcharts_stock.options.plot_options.price_envelopes import PriceEnvelopesOptions
from highcharts_stock.options.plot_options.psar import PSAROptions
from highcharts_stock.options.plot_options.vbp import VBPOptions
from highcharts_stock.options.plot_options.zigzag import ZigZagOptions
from highcharts_stock.options.plot_options.momentum import (MomentumOptions,
                                                            OBVOptions,
                                                            ROCOptions,
                                                            RSIOptions)
from highcharts_stock.options.plot_options.momentum.ikh import IKHOptions
from highcharts_stock.options.plot_options.momentum.macd import MACDOptions
from highcharts_stock.options.plot_options.momentum.supertrend import SupertrendOptions
from highcharts_stock.options.plot_options.oscillators import (AroonOscillatorOptions,
                                                               APOOptions,
                                                               CCIOptions,
                                                               ChaikinOptions,
                                                               CMOOptions,
                                                               DPOOptions,
                                                               TRIXOptions,
                                                               WilliamsROptions)
from highcharts_stock.options.plot_options.oscillators.ao import AOOptions
from highcharts_stock.options.plot_options.oscillators.klinger import KlingerOptions
from highcharts_stock.options.plot_options.oscillators.money_flow import (MFIOptions,
                                                                          CMFOptions)
from highcharts_stock.options.plot_options.oscillators.ppo import PPOOptions
from highcharts_stock.options.plot_options.oscillators.stochastic import (StochasticOptions,
                                                                          SlowStochasticOptions)


class PlotOptions(PlotOptionsBase):
    """A wrapper object for configurations applied to each series type.

    The config objects for each series can also be overridden for each series item as
    given in the series array.

    Configuration options for the series are given in three levels:

      * Options for all series in a chart are given in the
        :meth:`series <PlotOptions.series>` property.
      * Options for all series of a specific type are given in the corresponding
        property for that type, for example
        :meth:`plot_options.line <PlotOptions.line>`.
      * Finally, options for one single series are given in the
        :meth:`Options.series <Options.series>` array.

    """

    def __init__(self, **kwargs):
        self._abands = None
        self._ad = None
        self._ao = None
        self._apo = None
        self._aroon = None
        self._aroonoscillator = None
        self._atr = None
        self._bb = None
        self._candlestick = None
        self._cci = None
        self._chaikin = None
        self._cmf = None
        self._cmo = None
        self._dema = None
        self._disparityindex = None
        self._dmi = None
        self._dpo = None
        self._ema = None
        self._flags = None
        self._heikinashi = None
        self._hlc = None
        self._hollowcandlestick = None
        self._ikh = None
        self._keltnerchannels = None
        self._klinger = None
        self._linearregression = None
        self._linearregressionangle = None
        self._linearregressionintercept = None
        self._linearregressionslope = None
        self._macd = None
        self._mfi = None
        self._momentum = None
        self._natr = None
        self._obv = None
        self._ohlc = None
        self._pc = None
        self._pivotpoints = None
        self._ppo = None
        self._priceenvelopes = None
        self._psar = None
        self._roc = None
        self._rsi = None
        self._slowstochastic = None
        self._sma = None
        self._stochastic = None
        self._supertrend = None
        self._tema = None
        self._trendline = None
        self._trix = None
        self._vbp = None
        self._vwap = None
        self._williamsr = None
        self._wma = None
        self._zigzag = None

        self.abands = kwargs.get('abands', None)
        self.ad = kwargs.get('ad', None)
        self.ao = kwargs.get('ao', None)
        self.apo = kwargs.get('apo', None)
        self.aroon = kwargs.get('aroon', None)
        self.aroonoscillator = kwargs.get('aroonoscillator', None)
        self.atr = kwargs.get('atr', None)
        self.bb = kwargs.get('bb', None)
        self.candlestick = kwargs.get('candlestick', None)
        self.cci = kwargs.get('cci', None)
        self.chaikin = kwargs.get('chaikin', None)
        self.cmf = kwargs.get('cmf', None)
        self.cmo = kwargs.get('cmo', None)
        self.dema = kwargs.get('dema', None)
        self.disparityindex = kwargs.get('disparityindex', None)
        self.dmi = kwargs.get('dmi', None)
        self.dpo = kwargs.get('dpo', None)
        self.ema = kwargs.get('ema', None)
        self.flags = kwargs.get('flags', None)
        self.heikinashi = kwargs.get('heikinashi', None)
        self.hlc = kwargs.get('hlc', None)
        self.hollowcandlestick = kwargs.get('hollowcandlestick', None)
        self.ikh = kwargs.get('ikh', None)
        self.keltnerchannels = kwargs.get('keltnerchannels', None)
        self.klinger = kwargs.get('klinger', None)
        self.linearregression = kwargs.get('linearregression', None)
        self.linearregressionangle = kwargs.get('linearregressionangle', None)
        self.linearregressionintercept = kwargs.get('linearregressionintercept', None)
        self.linearregressionslope = kwargs.get('linearregressionslope', None)
        self.macd = kwargs.get('macd', None)
        self.mfi = kwargs.get('mfi', None)
        self.momentum = kwargs.get('momentum', None)
        self.natr = kwargs.get('natr', None)
        self.obv = kwargs.get('obv', None)
        self.ohlc = kwargs.get('ohlc', None)
        self.pc = kwargs.get('pc', None)
        self.pivotpoints = kwargs.get('pivotpoints', None)
        self.ppo = kwargs.get('ppo', None)
        self.priceenvelopes = kwargs.get('priceenvelopes', None)
        self.psar = kwargs.get('psar', None)
        self.roc = kwargs.get('roc', None)
        self.rsi = kwargs.get('rsi', None)
        self.slowstochastic = kwargs.get('slowstochastic', None)
        self.sma = kwargs.get('sma', None)
        self.stochastic = kwargs.get('stochastic', None)
        self.supertrend = kwargs.get('supertrend', None)
        self.tema = kwargs.get('tema', None)
        self.trendline = kwargs.get('trendline', None)
        self.trix = kwargs.get('trix', None)
        self.vbp = kwargs.get('vbp', None)
        self.vwap = kwargs.get('vwap', None)
        self.williamsr = kwargs.get('williamsr', None)
        self.wma = kwargs.get('wma', None)
        self.zigzag = kwargs.get('zigzag', None)

        super().__init__(**kwargs)

    # Highcharts Stock Properties

    @property
    def abands(self) -> Optional[AbandsOptions]:
        """Configuration for :term:`Acceleration Bands`, a :term:`technical indicator` which
        plots a trio of lines using a simple moving average for the midpoint, and the high and
        low values as the corresponding high and low bands.

        .. figure:: ../../../_static/abands-example.png
          :alt: Acceleration Bands Example Chart
          :align: center

        :rtype: :class:`AbandsOptions` or :obj:`None <python:None>`
        """
        return self._abands

    @abands.setter
    @class_sensitive(AbandsOptions)
    def abands(self, value):
        self._abands = value

    @property
    def ad(self) -> Optional[ADOptions]:
        """Options to configure an Accumulation/Distribution
        :term:`indicator <techincal indicator>`, which is a cumulative indicator that uses
        volume and price to assess whether a stock is being accumulated or distributed

        .. figure:: ../../../_static/ad-example.png
          :alt: Accumulation/Distribution Example Chart
          :align: center

        :rtype: :class:`ADOptions` or :obj:`None <python:None>`
        """
        return self._ad

    @ad.setter
    @class_sensitive(ADOptions)
    def ad(self, value):
        self._ad = value

    @property
    def ao(self) -> Optional[AOOptions]:
        """General options to configure Awesome :term:`Oscillators <oscillator>`, used
        within the financial markets to confirm or disprove trends on price charts.

        .. figure:: ../../../_static/awesome-oscillator-example.png
          :alt: Awesome Oscillator (AO) Example Chart
          :align: center

        :rtype: :class:`AOOptions` or :obj:`None <python:None>`
        """
        return self._ao

    @ao.setter
    @class_sensitive(AOOptions)
    def ao(self, value):
        self._ao = value

    @property
    def apo(self) -> Optional[APOOptions]:
        """General options to configure Absolute Price
        :term:`Oscillators <oscillator>` (APO), which is an :term:`oscillator` that
        displays the difference between two exponential moving averages of an asset's
        price expressed as an absolute value

        .. figure:: ../../../_static/apo-example.png
          :alt: Absolute Price Oscillator Example Chart
          :align: center

        :rtype: :class:`APOOptions` or :obj:`None <python:None>`
        """
        return self._apo

    @apo.setter
    @class_sensitive(APOOptions)
    def apo(self, value):
        self._apo = value

    @property
    def aroon(self) -> Optional[AroonOptions]:
        """General options for the Aroon indicator, which is a
        :term:`technical indicator` used to identify a change in the trend of the value of
        an asset.

        .. figure:: ../../../_static/aroon-example.png
          :alt: Aroon Example Chart
          :align: center

        :rtype: :class:`AroonOptions` or :obj:`None <python:None>`
        """
        return self._aroon

    @aroon.setter
    @class_sensitive(AroonOptions)
    def aroon(self, value):
        self._aroon = value

    @property
    def aroonoscillator(self) -> Optional[AroonOscillatorOptions]:
        """General options to configure an Aroon Oscillator series, which is an
        :term:`oscillator` that is used to gauge the strength of a current trend and the
        likelihood that it will continue.

        .. figure:: ../../../_static/aroon-oscillator-example.png
          :alt: Aroon Oscillator Example Chart
          :align: center

        :rtype: :class:`AroonOscillatorOptions` or :obj:`None <python:None>`
        """
        return self._aroonoscillator

    @aroonoscillator.setter
    @class_sensitive(AroonOscillatorOptions)
    def aroonoscillator(self, value):
        self._aroonoscillator = value

    @property
    def atr(self) -> Optional[ATROptions]:
        """General options to configure an Average True Range :term:`indicator <technical indicator>`,
        which is a measure of the degree of volatility in a value over time using a look-back
        period determined by the configuration of
        :meth:`.params <highcharts_stock.options.plot_options.atr.ATROptions.params`.

        .. figure:: ../../../_static/atr-example.png
          :alt: ATR Example Chart
          :align: center

        :rtype: :class:`ATROptions` or :obj:`None <python:None>`
        """
        return self._atr

    @atr.setter
    @class_sensitive(ATROptions)
    def atr(self, value):
        self._atr = value

    @property
    def bb(self) -> Optional[BBOptions]:
        """General options for Bollinger Bands, a :term:`technical indicator`.

        .. figure:: ../../../_static/bollinger-bands-example.png
          :alt: Bollinger Bands Example Chart
          :align: center

        :rtype: :class:`BBOptions` or :obj:`None <python:None>`
        """
        return self._bb

    @bb.setter
    @class_sensitive(BBOptions)
    def bb(self, value):
        self._bb = value

    @property
    def candlestick(self) -> Optional[CandlestickOptions]:
        """General options to apply to all Candlestick series types. A candlestick chart
        is a style of financial chart used to describe price movements over time.

        .. figure:: ../../../_static/candlestick-example.png
          :alt: Candlestick Example Chart
          :align: center

        :rtype: :class:`CandlestickOptions` or :obj:`None <python:None>`
        """
        return self._candlestick

    @candlestick.setter
    @class_sensitive(CandlestickOptions)
    def candlestick(self, value):
        self._candlestick = value

    @property
    def cci(self) -> Optional[CCIOptions]:
        """General options to configure a Commodity Channel Index
        :term:`indicator <technical indicator>`, which is an :term:`oscillator` that measures
        the difference between the current price and the historical average price using a
        look-back
        period determined by the configuration of
        :meth:`.params <highcharts_stock.options.plot_options.atr.CCIOptions.params`.

        .. figure:: ../../../_static/cci-example.png
          :alt: CCI Example Chart
          :align: center

        :rtype: :class:`CCIOptions` or :obj:`None <python:None>`
        """
        return self._cci

    @cci.setter
    @class_sensitive(CCIOptions)
    def cci(self, value):
        self._cci = value

    @property
    def chaikin(self) -> Optional[ChaikinOptions]:
        """General options to configure a Chaikin :term:`oscillator`, which measures the
        accummulation-distribution line of moving average convergence-divergence by
        subtracting a 10-day exponential moving average from a 3-day moving average of the
        accumulation-distribution line.

        .. figure:: ../../../_static/chaikin-example.png
          :alt: Chaikin Oscillator Example Chart
          :align: center

        :rtype: :class:`ChaikinOptions` or :obj:`None <python:None>`
        """
        return self._chaikin

    @chaikin.setter
    @class_sensitive(ChaikinOptions)
    def chaikin(self, value):
        self._chaikin = value

    @property
    def cmf(self) -> Optional[CMFOptions]:
        """General options to configure a Chaikin Money Flow :term:`indicator <technical indicator>`,
        which uses price and
        volume data to identify over-bought or over-sold signals in an asset.

        .. figure:: ../../../_static/cmf-example.png
          :alt: Chaikin Money Flow Example Chart
          :align: center

        :rtype: :class:`CMFOptions` or :obj:`None <python:None>`
        """
        return self._cmf

    @cmf.setter
    @class_sensitive(CMFOptions)
    def cmf(self, value):
        self._cmf = value

    @property
    def cmo(self) -> Optional[CMOOptions]:
        """General options to configure a Chande Momentum :term:`Oscillator`, which uses momentum to
        identify relative strength or weakness in a market.

        .. caution::

          The chosen time frame - configured by
          :meth:`.params.period <highcharts_stock.options.plot_options.atr.CCIOptions.params`
          and defaulting to a value of ``20`` - has a significant impact on the signals
          generated by the indicator.

        .. figure:: ../../../_static/cmo-example.png
          :alt: Chande Momentum Oscillator Example Chart
          :align: center

        :rtype: :class:`CMOOptions` or :obj:`None <python:None>`
        """
        return self._cmo

    @cmo.setter
    @class_sensitive(CMOOptions)
    def cmo(self, value):
        self._cmo = value

    @property
    def dema(self) -> Optional[DEMAOptions]:
        """General options to configure a Double Exponential Moving Average :term:`indicator`, which
        is often used to reduce the "noise" produced on a simple moving average.

        .. figure:: ../../../_static/dema-example.png
          :alt: DEMA Example Chart
          :align: center

        :rtype: :class:`DEMAOptions` or :obj:`None <python:None>`
        """
        return self._dema

    @dema.setter
    @class_sensitive(DEMAOptions)
    def dema(self, value):
        self._dema = value

    @property
    def disparityindex(self) -> Optional[DisparityIndexOptions]:
        """General options to configure a Disparity Index :term:`indicator`, which measures the
        relative position of the most-recent value to a selected moving average, expressed as
        a percentage.

        .. figure:: ../../../_static/disparity-index-example.png
          :alt: Disparity Index Example Chart
          :align: center

        :rtype: :class:`DisparityIndexOptions` or :obj:`None <python:None>`
        """
        return self._disparityindex

    @disparityindex.setter
    @class_sensitive(DisparityIndexOptions)
    def disparityindex(self, value):
        self._disparityindex = value

    @property
    def dmi(self) -> Optional[DMIOptions]:
        """General options to configure a Directional Movement Index (DMI)
        :term:`indicator <technical indicator>`, which can be used to identify whether an
        asset is trending by comparing highs and lows over time.

        .. figure:: ../../../_static/dmi-example.png
          :alt: Directional Movement Index (DMI) Example Chart
          :align: center

        :rtype: :class:`DMIOptions` or :obj:`None <python:None>`
        """
        return self._dmi

    @dmi.setter
    @class_sensitive(DMIOptions)
    def dmi(self, value):
        self._dmi = value

    @property
    def dpo(self) -> Optional[DPOOptions]:
        """General options to configure a Detrended Price :term:`Oscillator`, which
        strips out price trends in an effort to estimate the length of price cycles.

        .. figure:: ../../../_static/dpo-example.png
          :alt: DPO Example Chart
          :align: center

        :rtype: :class:`DPOOptions` or :obj:`None <python:None>`
        """
        return self._dpo

    @dpo.setter
    @class_sensitive(DPOOptions)
    def dpo(self, value):
        self._dpo = value

    @property
    def ema(self) -> Optional[EMAOptions]:
        """General options to configure an Exponential Moving Average :term:`indicator`, which
        is used to give greater weight to recent values.

        .. figure:: ../../../_static/ema-example.png
          :alt: Exponential Moving Average Example Chart
          :align: center

        :rtype: :class:`EMAOptions` or :obj:`None <python:None>`
        """
        return self._ema

    @ema.setter
    @class_sensitive(EMAOptions)
    def ema(self, value):
        self._ema = value

    @property
    def flags(self) -> Optional[FlagsOptions]:
        """General options to configure flags, which are used to mark events in **Highcharts Stock for Python**. They can be added
        on the timeline, or attached to a specific series.

        .. figure:: ../../../_static/flags-example.png
          :alt: Flags Example
          :align: center

        :rtype: :class:`FlagsOptions` or :obj:`None <python:None>`
        """
        return self._flags

    @flags.setter
    @class_sensitive(FlagsOptions)
    def flags(self, value):
        self._flags = value

    @property
    def heikinashi(self) -> Optional[HeikinAshiOptions]:
        """General options to apply to Heikin Ashi series types, which are visualized
        similarly to :class:`CandlestickSeries <options.series.candlestick.CandlestickSeries>`
        but which feature a smoother line by tracking ranges of movement rather than
        individual movements.

        .. figure:: ../../../_static/heikin-ashi-example.png
          :alt: Heikin Ashi Example Chart
          :align: center

        :rtype: :class:`HeikinAshiOptions` or :obj:`None <python:None>`
        """
        return self._heikinashi

    @heikinashi.setter
    @class_sensitive(HeikinAshiOptions)
    def heikinashi(self, value):
        self._heikinashi = value

    @property
    def hlc(self) -> Optional[HLCOptions]:
        """General options to apply to all :term:`HLC` series types. An HLC chart is a
        style of financial chart used to describe price movements over time.

        .. figure:: ../../../_static/hlc-example.png
          :alt: HLC Example Chart
          :align: center

        :rtype: :class:`HLCOptions` or :obj:`None <python:None>`
        """
        return self._hlc

    @hlc.setter
    @class_sensitive(HLCOptions)
    def hlc(self, value):
        self._hlc = value

    @property
    def hollowcandlestick(self) -> Optional[HollowCandlestickOptions]:
        """General options to apply to Hollow Candlestick series types. A candlestick chart is
        a style of financial chart used to describe price movements over time.

        .. figure:: ../../../_static/hollow-candlestick-example.png
          :alt: Hollow Candlestick Example Chart
          :align: center

        :rtype: :class:`HollowCandlestickOptions` or :obj:`None <python:None>`
        """
        return self._hollowcandlestick

    @hollowcandlestick.setter
    @class_sensitive(HollowCandlestickOptions)
    def hollowcandlestick(self, value):
        self._hollowcandlestick = value

    @property
    def ikh(self) -> Optional[IKHOptions]:
        """General options to configure a Ichimoku Kinko Hyo (IKH, or "ichimoku"), a momentum
        :term:`indicator <techincal indicator>`.

        .. figure:: ../../../_static/ikh-example.png
          :alt: Ichimoku Kinko Hyo (IKH) Example Chart
          :align: center

        :rtype: :class:`IKHOptions` or :obj:`None <python:None>`
        """
        return self._ikh

    @ikh.setter
    @class_sensitive(IKHOptions)
    def ikh(self, value):
        self._ikh = value

    @property
    def keltnerchannels(self) -> Optional[KeltnerChannelsOptions]:
        """General options to configure Keltner Channels :term:`indicator <technical indicator>`.

        .. figure:: ../../../_static/keltner-channels-example.png
          :alt: Keltner Channels Example Chart
          :align: center

        :rtype: :class:`KeltnerChannelsOptions` or :obj:`None <python:None>`
        """
        return self._keltnerchannels

    @keltnerchannels.setter
    @class_sensitive(KeltnerChannelsOptions)
    def keltnerchannels(self, value):
        self._keltnerchannels = value

    @property
    def klinger(self) -> Optional[KlingerOptions]:
        """General options to configure a Klinger :term:`Oscillator`, used to determine the long-term
        trend of money flow while remaining sensitive enough to detect short-term
        fluctuations.

        .. figure:: ../../../_static/klinger-example.png
          :alt: Klinger Example Chart
          :align: center

        :rtype: :class:`KlingerOptions` or :obj:`None <python:None>`
        """
        return self._klinger

    @klinger.setter
    @class_sensitive(KlingerOptions)
    def klinger(self, value):
        self._klinger = value

    @property
    def linearregression(self) -> Optional[LinearRegressionOptions]:
        """General options to configure a Linear Regression :term:`indicator`, which calculates a
        linear regression for a given set of values.

        .. figure:: ../../../_static/linear-regression-example.png
          :alt: Linear Regression Example Chart
          :align: center

        :rtype: :class:`LinearRegressionOptions` or :obj:`None <python:None>`
        """
        return self._linearregression

    @linearregression.setter
    @class_sensitive(LinearRegressionOptions)
    def linearregression(self, value):
        self._linearregression = value

    @property
    def linearregressionangle(self) -> Optional[LinearRegressionAngleOptions]:
        """General options to configure a Linear Regression Angle :term:`indicator`, which is a
        directional movement indicator which defines a trend at the moment of its birth and
        can be used to identify trend weakening.

        .. figure:: ../../../_static/linear-regression-angle-example.png
          :alt: Linear Regression Angle Example Chart
          :align: center

        :rtype: :class:`LinearRegressionAngleOptions` or :obj:`None <python:None>`
        """
        return self._linearregressionangle

    @linearregressionangle.setter
    @class_sensitive(LinearRegressionAngleOptions)
    def linearregressionangle(self, value):
        self._linearregressionangle = value

    @property
    def linearregressionintercept(self) -> Optional[LinearRegressionInterceptOptions]:
        """General options to configure a Linear Regression Intercept :term:`indicator`.

        .. figure:: ../../../_static/linear-regression-intercept-example.png
          :alt: Linear Regression Intercept Example Chart
          :align: center

        :rtype: :class:`LinearRegressionInterceptOptions` or :obj:`None <python:None>`
        """
        return self._linearregressionintercept

    @linearregressionintercept.setter
    @class_sensitive(LinearRegressionInterceptOptions)
    def linearregressionintercept(self, value):
        self._linearregressionintercept = value

    @property
    def linearregressionslope(self) -> Optional[LinearRegressionSlopeOptions]:
        """General options to configure a Linear Regression Slope :term:`indicator`.

        .. figure:: ../../../_static/linear-regression-slope-example.png
          :alt: Linear Regression Slope Example Chart
          :align: center

        :rtype: :class:`LinearRegressionSlopeOptions` or :obj:`None <python:None>`
        """
        return self._linearregressionslope

    @linearregressionslope.setter
    @class_sensitive(LinearRegressionSlopeOptions)
    def linearregressionslope(self, value):
        self._linearregressionslope = value

    @property
    def macd(self) -> Optional[MACDOptions]:
        """General options to configure a Moving Average Convergence/Divergence, a momentum
        :term:`indicator <techincal indicator>`.

        .. figure:: ../../../_static/macd-example.png
          :alt: Moving Average Convergence/Divergence (MACD) Example Chart
          :align: center

        :rtype: :class:`MACDOptions` or :obj:`None <python:None>`
        """
        return self._macd

    @macd.setter
    @class_sensitive(MACDOptions)
    def macd(self, value):
        self._macd = value

    @property
    def mfi(self) -> Optional[MFIOptions]:
        """General options to configure a Money Flow Index :term:`oscillator`, which uses price and
        volume data to identify over-bought or over-sold signals in an asset.

        .. figure:: ../../../_static/mfi-example.png
          :alt: Money Flow Index Example Chart
          :align: center

        :rtype: :class:`MFIOptions` or :obj:`None <python:None>`
        """
        return self._mfi

    @mfi.setter
    @class_sensitive(MFIOptions)
    def mfi(self, value):
        self._mfi = value

    @property
    def momentum(self) -> Optional[MomentumOptions]:
        """General options to configure a Momentum :term:`indicator <techincal indicator>`.

        .. figure:: ../../../_static/momentum-example.png
          :alt: Momentum Example Chart
          :align: center

        :rtype: :class:`MomentumOptions` or :obj:`None <python:None>`
        """
        return self._momentum

    @momentum.setter
    @class_sensitive(MomentumOptions)
    def momentum(self, value):
        self._momentum = value

    @property
    def natr(self) -> Optional[NATROptions]:
        """General options to configure a Normalized Average True Range
        :term:`indicator <technical indicator>`.

        .. figure:: ../../../_static/natr-example.png
          :alt: NATR Example Chart
          :align: center

        :rtype: :class:`NATROptions` or :obj:`None <python:None>`
        """
        return self._natr

    @natr.setter
    @class_sensitive(NATROptions)
    def natr(self, value):
        self._natr = value

    @property
    def obv(self) -> Optional[OBVOptions]:
        """General options to configure a Normalized Average True Range
        :term:`indicator <technical indicator>`.

        .. figure:: ../../../_static/obv-example.png
          :alt: OBV Example Chart
          :align: center

        :rtype: :class:`OBVOptions` or :obj:`None <python:None>`
        """
        return self._obv

    @obv.setter
    @class_sensitive(OBVOptions)
    def obv(self, value):
        self._obv = value

    @property
    def ohlc(self) -> Optional[OHLCOptions]:
        """General options to apply to a :term:`OHLC` series type. An OHLC chart is a
        sub-type of :term:`HLC` charts which displays the open, high, low, and close values
        of an asset over time.

        .. figure:: ../../../_static/ohlc-example.png
          :alt: OHLC Example Chart
          :align: center

        :rtype: :class:`OHLCOptions` or :obj:`None <python:None>`
        """
        return self._ohlc

    @ohlc.setter
    @class_sensitive(OHLCOptions)
    def ohlc(self, value):
        self._ohlc = value

    @property
    def pc(self) -> Optional[PCOptions]:
        """General options for a Price Channel :term:`indicator <technical indicator>`.

        .. figure:: ../../../_static/price-channel-example.png
          :alt: Price Channel Example Chart
          :align: center

        :rtype: :class:`PCOptions` or :obj:`None <python:None>`
        """
        return self._pc

    @pc.setter
    @class_sensitive(PCOptions)
    def pc(self, value):
        self._pc = value

    @property
    def pivotpoints(self) -> Optional[PivotPointsOptions]:
        """General options to configure a Pivot Points :term:`indicator <techincal indicator>`,
        which are typically used to identify trends and reversals in intraday trading.

        .. figure:: ../../../_static/pivot-points-example.png
          :alt: Pivot Points Example Chart
          :align: center

        :rtype: :class:`PivotPointsOptions` or :obj:`None <python:None>`
        """
        return self._pivotpoints

    @pivotpoints.setter
    @class_sensitive(PivotPointsOptions)
    def pivotpoints(self, value):
        self._pivotpoints = value

    @property
    def ppo(self) -> Optional[PPOOptions]:
        """General options to configure a Percentage Price :term:`Oscillator`, which shows the
        relationship between two moving averages in percentage terms.

        .. note::

          Defaults to comparing a 26-period and 12-period exponential moving average, though
          this can be adjusted using
          :meth:`.params.period <highcharts_stock.options.plot_options.oscillators.PPOOptions.params`.

        .. figure:: ../../../_static/cmo-example.png
          :alt: Chande Momentum Oscillator Example Chart
          :align: center

        :rtype: :class:`PPOOptions` or :obj:`None <python:None>`
        """
        return self._ppo

    @ppo.setter
    @class_sensitive(PPOOptions)
    def ppo(self, value):
        self._ppo = value

    @property
    def priceenvelopes(self) -> Optional[PriceEnvelopesOptions]:
        """General options for for :term:`Price Envelopes`, a :term:`technical indicator` based on
        simple moving averages.

        .. figure:: ../../../_static/price-envelopes-example.png
          :alt: Price Envelopes Example Chart
          :align: center

        :rtype: :class:`PriceEnvelopesOptions` or :obj:`None <python:None>`
        """
        return self._priceenvelopes

    @priceenvelopes.setter
    @class_sensitive(PriceEnvelopesOptions)
    def priceenvelopes(self, value):
        self._priceenvelopes = value

    @property
    def psar(self) -> Optional[PSAROptions]:
        """General options to configure a Parabolic SAR :term:`indicator <techincal indicator>`,
        which can be used to determine the direction in which a trend is moving.

        .. figure:: ../../../_static/psar-example.png
          :alt: Parabolic SAR Example Chart
          :align: center

        :rtype: :class:`PSAROptions` or :obj:`None <python:None>`
        """
        return self._psar

    @psar.setter
    @class_sensitive(PSAROptions)
    def psar(self, value):
        self._psar = value

    @property
    def roc(self) -> Optional[ROCOptions]:
        """General options to configure a Rate of Change :term:`indicator <techincal indicator>`.

        .. figure:: ../../../_static/roc-example.png
          :alt: Rate of Change Example Chart
          :align: center

        The indicator value for each point is calculated using:

        .. code-block::

          (C - Cn)/ Cn * 100

        where:

          * ``C`` is the close value of the point of the same x in the linked series, and
          * ``Cn`` is the close value of the point ``n`` periods ago, where ``n`` is
            determined via
            :meth:`.params.period <highcharts_stock.options.plot_options.momentum.ROCOptions.params>`

        :rtype: :class:`ROCOptions` or :obj:`None <python:None>`
        """
        return self._roc

    @roc.setter
    @class_sensitive(ROCOptions)
    def roc(self, value):
        self._roc = value

    @property
    def rsi(self) -> Optional[RSIOptions]:
        """General options to configure a Relative Strength Index, a momentum
        :term:`indicator <techincal indicator>` that measures the speed and magnitude of
        recent value changes to evaluate over-valued or under-valued conditions.

        .. figure:: ../../../_static/rsi-example.png
          :alt: Relative Strength Index Example Chart
          :align: center

        :rtype: :class:`RSIOptions` or :obj:`None <python:None>`
        """
        return self._rsi

    @rsi.setter
    @class_sensitive(RSIOptions)
    def rsi(self, value):
        self._rsi = value

    @property
    def slowstochastic(self) -> Optional[SlowStochasticOptions]:
        """General configuration for Stochastic :term:`Oscillators <oscillator>`.

        .. figure:: ../../../_static/stochastic-example.png
          :alt: Stochsatic Oscillator Example Chart
          :align: center

        :rtype: :class:`SlowStochasticOptions` or :obj:`None <python:None>`
        """
        return self._slowstochastic

    @slowstochastic.setter
    @class_sensitive(SlowStochasticOptions)
    def slowstochastic(self, value):
        self._slowstochastic = value

    @property
    def sma(self) -> Optional[SMAOptions]:
        """General options to configure a Simple Moving Average :term:`indicator`.

        .. figure:: ../../../_static/sma-example.png
          :alt: Simple Moving Average Example Chart
          :align: center

        :rtype: :class:`SMAOptions` or :obj:`None <python:None>`
        """
        return self._sma

    @sma.setter
    @class_sensitive(SMAOptions)
    def sma(self, value):
        self._sma = value

    @property
    def stochastic(self) -> Optional[StochasticOptions]:
        """General options for Stochastic :term:`Oscillators <oscillator>`.

        .. figure:: ../../../_static/stochastic-example.png
          :alt: Stochsatic Oscillator Example Chart
          :align: center

        :rtype: :class:`StochasticOptions` or :obj:`None <python:None>`
        """
        return self._stochastic

    @stochastic.setter
    @class_sensitive(StochasticOptions)
    def stochastic(self, value):
        self._stochastic = value

    @property
    def supertrend(self) -> Optional[SupertrendOptions]:
        """General options to configure a Supertrend, a momentum
        :term:`indicator <techincal indicator>` used to help identify buy/sell signals.

        .. figure:: ../../../_static/supertrend-example.png
          :alt: Supertrend Example Chart
          :align: center

        :rtype: :class:`SupertrendOptions` or :obj:`None <python:None>`
        """
        return self._supertrend

    @supertrend.setter
    @class_sensitive(SupertrendOptions)
    def supertrend(self, value):
        self._supertrend = value

    @property
    def tema(self) -> Optional[TEMAOptions]:
        """General options to configure a Triple Exponential Moving Average :term:`indicator`, which
        is often used to reduce the "noise" produced on a simple moving average.

        .. figure:: ../../../_static/tema-example.png
          :alt: TEMA Example Chart
          :align: center

        :rtype: :class:`TEMAOptions` or :obj:`None <python:None>`
        """
        return self._tema

    @tema.setter
    @class_sensitive(TEMAOptions)
    def tema(self, value):
        self._tema = value

    @property
    def trendline(self) -> Optional[TrendlineOptions]:
        """General options to configure a Trendline :term:`indicator`, which fits a straight line to
        the linked data using the Sum of Least Squares method.

        .. figure:: ../../../_static/trendline-example.png
          :alt: Trendline Example Chart
          :align: center

        :rtype: :class:`TrendlineOptions` or :obj:`None <python:None>`
        """
        return self._trendline

    @trendline.setter
    @class_sensitive(TrendlineOptions)
    def trendline(self, value):
        self._trendline = value

    @property
    def trix(self) -> Optional[TRIXOptions]:
        """General options to configure a Triple Exponential Average :term:`Oscillator`, which
        can be used to suggest increasing or decreasing momentum.

        .. figure:: ../../../_static/trix-example.png
          :alt: TRIX Example Chart
          :align: center

        :rtype: :class:`TRIXOptions` or :obj:`None <python:None>`
        """
        return self._trix

    @trix.setter
    @class_sensitive(TRIXOptions)
    def trix(self, value):
        self._trix = value

    @property
    def vbp(self) -> Optional[VBPOptions]:
        """General options to configure a Volume-by-Price (VBP)
        :term:`indicator <technical indicator>`, which can be used to analyze volumes traded
        within various price bands.

        .. figure:: ../../../_static/vbp-example.png
          :alt: Volume-by-Price (VBP) Example Chart
          :align: center

        :rtype: :class:`VBPOptions` or :obj:`None <python:None>`
        """
        return self._vbp

    @vbp.setter
    @class_sensitive(VBPOptions)
    def vbp(self, value):
        self._vbp = value

    @property
    def vwap(self) -> Optional[VWAPOptions]:
        """General options to configure a Volume Weighted Average Price (VWAP) :term:`indicator`.

        .. figure:: ../../../_static/vwap-example.png
          :alt: Volume Weighted Average Price Example Chart
          :align: center

        :rtype: :class:`VWAPOptions` or :obj:`None <python:None>`
        """
        return self._vwap

    @vwap.setter
    @class_sensitive(VWAPOptions)
    def vwap(self, value):
        self._vwap = value

    @property
    def williamsr(self) -> Optional[WilliamsROptions]:
        """General options to configure a Williams %R :term:`oscillator`, which uses the current
        closing price in relation to the high and low of the past ``n`` days to indicate
        overbought and oversold levels.

        .. figure:: ../../../_static/williamsr-example.png
          :alt: Williams %R Example Chart
          :align: center

        :rtype: :class:`WilliamsROptions` or :obj:`None <python:None>`
        """
        return self._williamsr

    @williamsr.setter
    @class_sensitive(WilliamsROptions)
    def williamsr(self, value):
        self._williamsr = value

    @property
    def wma(self) -> Optional[WMAOptions]:
        """General options to configure a Weighted Moving Average :term:`indicator`.

        .. figure:: ../../../_static/wma-example.png
          :alt: Weighted Moving Average Example Chart
          :align: center

        :rtype: :class:`WMAOptions` or :obj:`None <python:None>`
        """
        return self._wma

    @wma.setter
    @class_sensitive(WMAOptions)
    def wma(self, value):
        self._wma = value

    @property
    def zigzag(self) -> Optional[ZigZagOptions]:
        """General options to configure a ZigZag :term:`indicator`.

        .. figure:: ../../../_static/zigzag-example.png
          :alt: ZigZag Example Chart
          :align: center

        :rtype: :class:`ZigZagOptions` or :obj:`None <python:None>`
        """
        return self._zigzag

    @zigzag.setter
    @class_sensitive(ZigZagOptions)
    def zigzag(self, value):
        self._zigzag = value

    # Highcharts Properties

    @property
    def arcdiagram(self) -> Optional[ArcDiagramOptions]:
        """Arc diagram series is a chart drawing style in which the vertices of the chart
        are positioned along a line on the Euclidean plane and the edges are drawn as a
        semicircle in one of the two half-planes delimited by the line, or as smooth
        curves formed by sequences of semicircles.

        .. figure:: ../../../_static/arcdiagram-example.png
          :alt: Arc Diagram Example Chart
          :align: center

        :rtype: :class:`ArcDiagramOptions` or :obj:`None <python:None>`
        """
        return self._arcdiagram

    @arcdiagram.setter
    @class_sensitive(ArcDiagramOptions)
    def arcdiagram(self, value):
        self._arcdiagram = value

    @property
    def area(self) -> Optional[AreaOptions]:
        """General options to apply to all Area series types.

        .. figure:: ../../../_static/area-example.png
          :alt: Area Example Chart
          :align: center

        :rtype: :class:`AreaOptions` or :obj:`None <python:None>`
        """
        return self._area

    @area.setter
    @class_sensitive(AreaOptions)
    def area(self, value):
        self._area = value

    @property
    def arearange(self) -> Optional[AreaRangeOptions]:
        """General options to apply to all AreaRange series types. The area range series
        is a carteseian series with higher and lower values for each point along an X
        axis, where the area between the values is shaded.

        .. figure:: ../../../_static/arearange-example.png
          :alt: AreaRange Example Chart
          :align: center

        :rtype: :class:`AreaRangeOptions` or :obj:`None <python:None>`
        """
        return self._arearange

    @arearange.setter
    @class_sensitive(AreaRangeOptions)
    def arearange(self, value):
        self._arearange = value

    @property
    def areaspline(self) -> Optional[AreaSplineOptions]:
        """General options to apply to all AreaSpline series types. The area spline series
        is an area series where the graph between the points is smoothed into a spline.

        .. figure:: ../../../_static/areaspline-example.png
          :alt: AreaSpline Example Chart
          :align: center

        :rtype: :class:`AreaSplineOptions` or :obj:`None <python:None>`
        """
        return self._areaspline

    @areaspline.setter
    @class_sensitive(AreaSplineOptions)
    def areaspline(self, value):
        self._areaspline = value

    @property
    def areasplinerange(self) -> Optional[AreaSplineRangeOptions]:
        """General options to apply to all AreaSplineRange series types. The area spline
        range series is a carteseian series type with higher and lower Y values along an X
        axis. The area inside the range is colored, and the graph outlining the area is a
        smoothed spline.

        :rtype: :class:`AreaSplineRangeOptions` or :obj:`None <python:None>`
        """
        return self._areasplinerange

    @areasplinerange.setter
    @class_sensitive(AreaSplineRangeOptions)
    def areasplinerange(self, value):
        self._areasplinerange = value

    @property
    def bar(self) -> Optional[BarOptions]:
        """General options to apply to all Bar series types. A bar series is a special
        type of column series where the columns are horizontal.

        .. figure:: ../../../_static/bar-example.png
          :alt: Bar Example Chart
          :align: center

        :rtype: :class:`BarOptions` or :obj:`None <python:None>`
        """
        return self._bar

    @bar.setter
    @class_sensitive(BarOptions)
    def bar(self, value):
        self._bar = value

    @property
    def bellcurve(self) -> Optional[BellCurveOptions]:
        """General options to apply to all Bell Curve series types.

        A bell curve is an areaspline series which represents the probability density
        function of the normal distribution. It calculates mean and standard deviation of
        the base series data and plots the curve according to the calculated parameters.

        .. figure:: ../../../_static/bellcurve-example.png
          :alt: Bell Curve Example Chart
          :align: center

        :rtype: :class:`BellCurveOptions` or :obj:`None <python:None>`
        """
        return self._bellcurve

    @bellcurve.setter
    @class_sensitive(BellCurveOptions)
    def bellcurve(self, value):
        self._bellcurve = value

    @property
    def boxplot(self) -> Optional[BoxPlotOptions]:
        """General options to apply to all Box Plot series types.

        A box plot is a convenient way of depicting groups of data through their
        five-number summaries:

          * the smallest observation (sample minimum),
          * lower quartile (Q1),
          * median (Q2),
          * upper quartile (Q3), and
          * largest observation (sample maximum).

        .. figure:: ../../../_static/boxplot-example.png
          :alt: Box Plot Example Chart
          :align: center

        :rtype: :class:`BoxPlotOptions` or :obj:`None <python:None>`
        """
        return self._boxplot

    @boxplot.setter
    @class_sensitive(BoxPlotOptions)
    def boxplot(self, value):
        self._boxplot = value

    @property
    def bubble(self) -> Optional[BubbleOptions]:
        """General options to apply to all Bubble series types.

        A bubble series is a three dimensional series type where each point renders an X,
        Y, and Z value. Each points is drawn as a bubble where the position along the X
        and Y axes mark the X and Y values, and the size of the bubble relates to the Z
        value.

        .. figure:: ../../../_static/bubble-example.png
          :alt: Bubble Example Chart
          :align: center

        :rtype: :class:`BubbleOptions` or :obj:`None <python:None>`
        """
        return self._bubble

    @bubble.setter
    @class_sensitive(BubbleOptions)
    def bubble(self, value):
        self._bubble = value

    @property
    def bullet(self) -> Optional[BulletOptions]:
        """General options to apply to all Bullet series types.

        A bullet graph is a variation of a bar graph. The bullet graph features a single
        measure, compares it to a target, and displays it in the context of qualitative
        ranges of performance that could be set using :meth:`YAxis.plot_bands`.

        .. figure:: ../../../_static/bullet-example.png
          :alt: Bullet Example Chart
          :align: center

        :rtype: :class:`BulletOptions` or :obj:`None <python:None>`
        """
        return self._bullet

    @bullet.setter
    @class_sensitive(BulletOptions)
    def bullet(self, value):
        self._bullet = value

    @property
    def column(self) -> Optional[ColumnOptions]:
        """General options to apply to all Column series types.

        Column series display one column per value along an X axis.

        .. figure:: ../../../_static/column-example.png
          :alt: Column Example Chart
          :align: center

        :rtype: :class:`ColumnOptions` or :obj:`None <python:None>`
        """
        return self._column

    @column.setter
    @class_sensitive(ColumnOptions)
    def column(self, value):
        self._column = value

    @property
    def columnpyramid(self) -> Optional[ColumnPyramidOptions]:
        """General options to apply to all Column Pyramid series types.

        Column Pyramid series display one pyramid per value along an X axis.

        .. hint::

          To display horizontal pyramids, set :meth:`Chart.inverted` to ``True``.

        .. tabs::

          .. tab:: Standard

            .. figure:: ../../../_static/columnpyramid-example.png
              :alt: ColumnPyramid Example Chart
              :align: center

          .. tab:: Stacked

            .. figure:: ../../../_static/columnpyramid-example-stacked.png
              :alt: Stacked Column Pyramid Example Chart
              :align: center

          .. tab:: Stacked + Inverted

            .. figure:: ../../../_static/columnpyramid-example-stacked-horizontal.png
              :alt: Stacked and Inverted Column Pyramid Example Chart
              :align: center

        :rtype: :class:`ColumnPyramidOptions` or :obj:`None <python:None>`
        """
        return self._columnpyramid

    @columnpyramid.setter
    @class_sensitive(ColumnPyramidOptions)
    def columnpyramid(self, value):
        self._columnpyramid = value

    @property
    def columnrange(self) -> Optional[ColumnRangeOptions]:
        """General options to apply to all Column Range series types.

        The column range is a cartesian series type with higher and lower Y values along
        an X axis.

        .. hint::

          To display horizontal bars, set :meth:`Chart.inverted` to ``True``.

        .. tabs::

          .. tab:: Standard

            .. figure:: ../../../_static/columnrange-example.png
              :alt: ColumnRange Example Chart
              :align: center

          .. tab:: Horizontal

            .. figure:: ../../../_static/columnrange-example-horizontal.png
              :alt: Inverted Column Range Example Chart
              :align: center

        :rtype: :class:`ColumnRangeOptions` or :obj:`None <python:None>`
        """
        return self._columnrange

    @columnrange.setter
    @class_sensitive(ColumnRangeOptions)
    def columnrange(self, value):
        self._columnrange = value

    @property
    def cylinder(self) -> Optional[CylinderOptions]:
        """General options to apply to all Cylinder series types.

        A cylinder graph is a variation of a 3d column graph. The cylinder graph features
        cylindrical points.

        .. figure:: ../../../_static/cylinder-example.png
          :alt: Cylinder Example Chart
          :align: center

        :rtype: :class:`CylinderOptions` or :obj:`None <python:None>`
        """
        return self._cylinder

    @cylinder.setter
    @class_sensitive(CylinderOptions)
    def cylinder(self, value):
        self._cylinder = value

    @property
    def dependencywheel(self) -> Optional[DependencyWheelOptions]:
        """General options to apply to all Dependency Wheel series types.

        A dependency wheel chart is a type of flow diagram, where all nodes are laid out
        in a circle, and the flow between the are drawn as link bands.

        .. figure:: ../../../_static/dependencywheel-example.png
          :alt: Dependency Wheel Example Chart
          :align: center

        :rtype: :class:`DependencyWheelOptions` or :obj:`None <python:None>`
        """
        return self._dependencywheel

    @dependencywheel.setter
    @class_sensitive(DependencyWheelOptions)
    def dependencywheel(self, value):
        self._dependencywheel = value

    @property
    def dumbbell(self) -> Optional[DumbbellOptions]:
        """General options to apply to all Dumbbell series types.

        The dumbbell series is a cartesian series with higher and lower values for each
        point along an X axis, connected with a line between the values.

        .. figure:: ../../../_static/dumbbell-example.png
          :alt: Dumbbell Example Chart
          :align: center

        .. warning::

          Requires ``highcharts-more.js`` and ``modules/dumbbell.js`` be loaded
          client-side.

        :rtype: :class:`DumbbellOptions` or :obj:`None <python:None>`
        """
        return self._dumbbell

    @dumbbell.setter
    @class_sensitive(DumbbellOptions)
    def dumbbell(self, value):
        self._dumbbell = value

    @property
    def errorbar(self) -> Optional[ErrorBarOptions]:
        """General options to apply to all Error Bar series types.

        Error bars are a graphical representation of the variability of data and are used
        on graphs to indicate the error, or uncertainty in a reported measurement.

        .. figure:: ../../../_static/errorbar-example.png
          :alt: Error Bar Example Chart
          :align: center

        :rtype: :class:`ErrorBarOptions` or :obj:`None <python:None>`
        """
        return self._errorbar

    @errorbar.setter
    @class_sensitive(ErrorBarOptions)
    def errorbar(self, value):
        self._errorbar = value

    @property
    def funnel(self) -> Optional[FunnelOptions]:
        """General options to apply to all Funnel series types.

        Funnel charts are a type of chart often used to visualize stages in a sales
        project, where the top are the initial stages with the most clients.

        .. warning::

          Funnel charts require that the ``modules/funnel.js`` file is loaded client-side.

        .. figure:: ../../../_static/funnel-example.png
          :alt: Funnel Example Chart
          :align: center

        :rtype: :class:`FunnelOptions` or :obj:`None <python:None>`
        """
        return self._funnel

    @funnel.setter
    @class_sensitive(FunnelOptions)
    def funnel(self, value):
        self._funnel = value

    @property
    def funnel_3d(self) -> Optional[Funnel3DOptions]:
        """General options to apply to all Funnel 3D series types.

        A Funnel 3D chart is a three-dimensional version of funnel series type. Funnel
        charts are a type of chart often used to visualize stages in a sales project,
        where the top are the initial stages with the most clients.

        .. warning::

          Funnel 3D charts require that the following files are all loaded client-side:

            * ``highcharts-3d.js``,
            * ``cylinder.js`` and
            * ``funnel3d.js``

        .. figure:: ../../../_static/funnel_3d-example.png
          :alt: Funnel 3D Example Chart
          :align: center

        :rtype: :class:`FunnelOptions` or :obj:`None <python:None>`
        """
        return self._funnel_3d

    @funnel_3d.setter
    @class_sensitive(Funnel3DOptions)
    def funnel_3d(self, value):
        self._funnel_3d = value

    @property
    def gauge(self) -> Optional[GaugeOptions]:
        """General options to apply to all Gauge series types.

        Gauges are circular plots displaying one or more values with a dial pointing to
        values along the perimeter.

        .. figure:: ../../../_static/gauge-example.png
          :alt: Gauge Example Chart
          :align: center

        :rtype: :class:`GaugeOptions` or :obj:`None <python:None>`
        """
        return self._gauge

    @gauge.setter
    @class_sensitive(GaugeOptions)
    def gauge(self, value):
        self._gauge = value

    @property
    def heatmap(self) -> Optional[HeatmapOptions]:
        """General options to apply to all Heatmap series types.

        A heatmap is a graphical representation of data where the individual values
        contained in a matrix are represented as colors.

        .. warning::

          Heatmaps require that ``modules/heatmap`` is loaded client-side.

        .. figure:: ../../../_static/heatmap-example.png
          :alt: Heatmap Example Chart
          :align: center

        :rtype: :class:`HeatmapOptions` or :obj:`None <python:None>`
        """
        return self._heatmap

    @heatmap.setter
    @class_sensitive(HeatmapOptions)
    def heatmap(self, value):
        self._heatmap = value

    @property
    def histogram(self) -> Optional[HistogramOptions]:
        """General options to apply to all Histogram series types.

        A histogram is a column series which represents the distribution of the data set
        in the base series. Histogram splits data into bins and shows their frequencies.

        .. figure:: ../../../_static/histogram-example.png
          :alt: Histogram Example Chart
          :align: center

        :rtype: :class:`HistogramOptions` or :obj:`None <python:None>`
        """
        return self._histogram

    @histogram.setter
    @class_sensitive(HistogramOptions)
    def histogram(self, value):
        self._histogram = value

    @property
    def item(self) -> Optional[ItemOptions]:
        """General options to apply to all Item series types.

        An item chart is an infographic chart where a number of items are laid out in
        either a rectangular or circular pattern. It can be used to visualize counts
        within a group, or for the circular pattern, typically a parliament.

        The circular layout has much in common with a pie chart. Many of the item series
        options, like ``center``, ``size`` and data label positioning, are inherited from
        the :meth:`PlotOptions.pie` series and don't apply for rectangular layouts.

        .. tabs::

          .. tab:: Circular Item Chart

            .. figure:: ../../../_static/item-example-circular.png
              :alt: Circular Item Example Chart
              :align: center

          .. tab:: Rectangular Item Chart

            .. figure:: ../../../_static/item-example-rectangular.png
              :alt: Rectangular Item Example Chart
              :align: center

          .. tab:: Item Chart with Symbols

            .. figure:: ../../../_static/item-example-symbols.png
              :alt: Item Example Chart with Symbols
              :align: center

        :rtype: :class:`ItemOptions` or :obj:`None <python:None>`
        """
        return self._item

    @item.setter
    @class_sensitive(ItemOptions)
    def item(self, value):
        self._item = value

    @property
    def line(self) -> Optional[LineOptions]:
        """General options to apply to all Line series types.

        A line series displays information as a series of data points connected by
        straight line segments.

        .. figure:: ../../../_static/line-example.png
          :alt: Line Example Chart
          :align: center

        :rtype: :class:`LineOptions` or :obj:`None <python:None>`
        """
        return self._line

    @line.setter
    @class_sensitive(LineOptions)
    def line(self, value):
        self._line = value

    @property
    def lollipop(self) -> Optional[LollipopOptions]:
        """General options to apply to all Lollipop series types.

        The lollipop series is a carteseian series with a line anchored from the x axis
        and a dot at the end to mark the value.

        .. warning::

          Requires ``highcharts-more.js``, ``modules/dumbbell.js``, and
          ``modules/lollipop.js`` to be loaded client-side.

        .. figure:: ../../../_static/lollipop-example.png
          :alt: Lollipop Example Chart
          :align: center

        :rtype: :class:`LollipopOptions` or :obj:`None <python:None>`
        """
        return self._lollipop

    @lollipop.setter
    @class_sensitive(LollipopOptions)
    def lollipop(self, value):
        self._lollipop = value

    @property
    def networkgraph(self) -> Optional[NetworkGraphOptions]:
        """General options to apply to all Network Graph series types.

        A network graph is a type of relationship chart, where connnections (links)
        attract nodes (points) and other nodes repulse each other.

        .. figure:: ../../../_static/networkgraph-example.png
          :alt: NetworkGraph Example Chart
          :align: center

        :rtype: :class:`NetworkGraphOptions` or :obj:`None <python:None>`
        """
        return self._networkgraph

    @networkgraph.setter
    @class_sensitive(NetworkGraphOptions)
    def networkgraph(self, value):
        self._networkgraph = value

    @property
    def organization(self) -> Optional[OrganizationOptions]:
        """General options to apply to all Organization series types.

        An organization chart is a diagram that shows the structure of an organization and
        the relationships and relative ranks of its parts and positions.

        .. tabs::

          .. tab:: Standard Organization Chart

            .. figure:: ../../../_static/organization-example.png
              :alt: Organization Example Chart
              :align: center

          .. tab:: Horizontal Organization Chart

            .. figure:: ../../../_static/organization-example-horizontal.png
              :alt: Horizontal Organization Example Chart
              :align: center

        :rtype: :class:`OrganizationOptions` or :obj:`None <python:None>`
        """
        return self._organization

    @organization.setter
    @class_sensitive(OrganizationOptions)
    def organization(self, value):
        self._organization = value

    @property
    def packedbubble(self) -> Optional[PackedBubbleOptions]:
        """General options to apply to all Packed Bubble series types.

        A packed bubble series is a two dimensional series type, where each point renders
        a value in X, Y position. Each point is drawn as a bubble where the bubbles don't
        overlap with each other and the radius of the bubble relates to the value.

        .. tabs::

          .. tab:: Standard Packed Bubble

            .. figure:: ../../../_static/packedbubble-example.png
              :alt: Split Packed Bubble Example Chart
              :align: center

          .. tab:: Split Packed Bubble

            .. figure:: ../../../_static/packedbubble-example-split.png
              :alt: Split Packed Bubble Example Chart
              :align: center

        :rtype: :class:`PackedBubbleOptions` or :obj:`None <python:None>`
        """
        return self._packedbubble

    @packedbubble.setter
    @class_sensitive(PackedBubbleOptions)
    def packedbubble(self, value):
        self._packedbubble = value

    @property
    def pareto(self) -> Optional[ParetoOptions]:
        """General options to apply to all Pareto series types.

        A pareto diagram is a type of chart that contains both bars and a line graph,
        where individual values are represented in descending order by bars, and the
        cumulative total is represented by the line.

        .. figure:: ../../../_static/pareto-example.png
          :alt: Pareto Example Chart
          :align: center

        :rtype: :class:`ParetoOptions` or :obj:`None <python:None>`
        """
        return self._pareto

    @pareto.setter
    @class_sensitive(ParetoOptions)
    def pareto(self, value):
        self._pareto = value

    @property
    def pictorial(self) -> Optional[PictorialOptions]:
        """General options to apply to all Pictorial series types.

        A pictorial series uses vector images to represent the data, with the data's shape
        determined by the ``path`` parameter.

        .. figure:: ../../../_static/pictorial-example.png
          :alt: Pictorial Example Chart
          :align: center


        :rtype: :class:`PictorialOptions <highcharts_stock.options.plot_options.pictorial.PictorialOptions>` or
          :obj:`None <python:None>`
        """
        return self._pictorial

    @pictorial.setter
    @class_sensitive(PictorialOptions)
    def pictorial(self, value):
        self._pictorial = value

    @property
    def pie(self) -> Optional[PieOptions]:
        """General options to apply to all Pie series types.

        A pie chart is a circular graphic which is divided into slices to illustrate
        numerical proportion.

        .. tabs::

          .. tab:: Pie Chart

            .. figure:: ../../../_static/pie-example.png
              :alt: Pie Example Chart
              :align: center

          .. tab:: Donut Chart

            .. figure:: ../../../_static/pie-example-donut.png
              :alt: Donut Example Chart
              :align: center

        :rtype: :class:`PieOptions` or :obj:`None <python:None>`
        """
        return self._pie

    @pie.setter
    @class_sensitive(PieOptions)
    def pie(self, value):
        self._pie = value

    @property
    def polygon(self) -> Optional[PolygonOptions]:
        """General options to apply to all Polygon series types.

        A polygon series can be used to draw any freeform shape in the cartesian
        coordinate system. A fill is applied with the :meth:`PolygonOptions.color`
        setting, and stroke is applied through :meth:`PolygonOptions.line_width` and
        :meth:`PolygonOptions.line_color`.

        .. figure:: ../../../_static/polygon-example.png
          :alt: Polygon Example Chart
          :align: center

        :rtype: :class:`PolygonOptions` or :obj:`None <python:None>`
        """
        return self._polygon

    @polygon.setter
    @class_sensitive(PolygonOptions)
    def polygon(self, value):
        self._polygon = value

    @property
    def pyramid(self) -> Optional[PyramidOptions]:
        """General options to apply to all Pyramid series types.

        A pyramid series is a special type of funnel, without neck and reversed by
        default.

        .. figure:: ../../../_static/pyramid-example.png
          :alt: Pyramid Example Chart
          :align: center

        :rtype: :class:`PyramidOptions` or :obj:`None <python:None>`
        """
        return self._pyramid

    @pyramid.setter
    @class_sensitive(PyramidOptions)
    def pyramid(self, value):
        self._pyramid = value

    @property
    def pyramid_3d(self) -> Optional[Pyramid3DOptions]:
        """General options to apply to all Pyramid 3D series types.

        A pyramid 3d series is a special type of funnel, without neck and reversed by
        default.

        .. figure:: ../../../_static/pyramid_3d-example.png
          :alt: Pyramid 3D Example Chart
          :align: center

        :rtype: :class:`Pyramid3DOptions` or :obj:`None <python:None>`
        """
        return self._pyramid_3d

    @pyramid_3d.setter
    @class_sensitive(Pyramid3DOptions)
    def pyramid_3d(self, value):
        self._pyramid_3d = value

    @property
    def sankey(self) -> Optional[SankeyOptions]:
        """General options to apply to all Sankey series types.

        A sankey diagram is a type of flow diagram, in which the width of the link between
        two nodes is shown proportionally to the flow quantity.

        .. tabs::

          .. tab:: Standard Sankey

            .. figure:: ../../../_static/sankey-example.png
              :alt: Sankey Example Chart
              :align: center

          .. tab:: Inverted Sankey

            .. figure:: ../../../_static/sankey-example-inverted.png
              :alt: Inverted Sankey Example Chart
              :align: center

          .. tab:: Sankey with Outgoing Links

            .. figure:: ../../../_static/sankey-example-outgoing.png
              :alt: Sankey Example Chart with Outgoing Links
              :align: center

        :rtype: :class:`SankeyOptions` or :obj:`None <python:None>`
        """
        return self._sankey

    @sankey.setter
    @class_sensitive(SankeyOptions)
    def sankey(self, value):
        self._sankey = value

    @property
    def scatter(self) -> Optional[ScatterOptions]:
        """General options to apply to all Scatter series types.

        A scatter plot uses cartesian coordinates to display values for two variables for
        a set of data.

        .. figure:: ../../../_static/scatter-example.png
          :alt: Scatter Example Chart
          :align: center

        :rtype: :class:`ScatterOptions` or :obj:`None <python:None>`
        """
        return self._scatter

    @scatter.setter
    @class_sensitive(ScatterOptions)
    def scatter(self, value):
        self._scatter = value

    @property
    def scatter_3d(self) -> Optional[Scatter3DOptions]:
        """General options to apply to all Scatter 3D series types.

        A 3D scatter plot uses x, y and z coordinates to display values for three
        variables for a set of data.

        .. figure:: ../../../_static/scatter_3d-example.png
          :alt: Scatter 3D Example Chart
          :align: center

        :rtype: :class:`Scatter3DOptions` or :obj:`None <python:None>`
        """
        return self._scatter_3d

    @scatter_3d.setter
    @class_sensitive(Scatter3DOptions)
    def scatter_3d(self, value):
        self._scatter_3d = value

    @property
    def series(self) -> Optional[SeriesOptions]:
        """General options to apply to all series types.

        :rtype: :class:`ScatterOptions` or :obj:`None <python:None>`
        """
        return self._series

    @series.setter
    @class_sensitive(SeriesOptions)
    def series(self, value):
        self._series = value

    @property
    def solidgauge(self) -> Optional[SolidGaugeOptions]:
        """General options to apply to all Solid Gauge series types.

        A solid gauge is a circular gauge where the value is indicated by a filled arc,
        and the color of the arc may variate with the value.

        .. figure:: ../../../_static/solidgauge-example.png
          :alt: SolidGauge Example Chart
          :align: center

        :rtype: :class:`SolidGaugeOptions` or :obj:`None <python:None>`
        """
        return self._solidgauge

    @solidgauge.setter
    @class_sensitive(SolidGaugeOptions)
    def solidgauge(self, value):
        self._solidgauge = value

    @property
    def spline(self) -> Optional[SplineOptions]:
        """General options to apply to all Spline series types.

        A spline series is a special type of line series, where the segments between the
        data points are smoothed.

        .. figure:: ../../../_static/spline-example.png
          :alt: Spline Example Chart
          :align: center

        :rtype: :class:`SplineOptions` or :obj:`None <python:None>`
        """
        return self._spline

    @spline.setter
    @class_sensitive(SplineOptions)
    def spline(self, value):
        self._spline = value

    @property
    def streamgraph(self) -> Optional[StreamGraphOptions]:
        """General options to apply to all Stream Graph series types.

        A streamgraph is a type of stacked area graph which is displaced around a central
        axis, resulting in a flowing, organic shape.

        .. figure:: ../../../_static/streamgraph-example.png
          :alt: StreamGraph Example Chart
          :align: center

        :rtype: :class:`StreamGraphOptions` or :obj:`None <python:None>`
        """
        return self._streamgraph

    @streamgraph.setter
    @class_sensitive(StreamGraphOptions)
    def streamgraph(self, value):
        self._streamgraph = value

    @property
    def sunburst(self) -> Optional[SunburstOptions]:
        """General options to apply to all Sunburst series types.

        A Sunburst displays hierarchical data, where a level in the hierarchy is
        represented by a circle. The center represents the root node of the tree. The
        visualization bears a resemblance to both treemap and pie charts.

        .. figure:: ../../../_static/sunburst-example.png
          :alt: Sunburst Example Chart
          :align: center

        :rtype: :class:`SunburstOptions` or :obj:`None <python:None>`
        """
        return self._sunburst

    @sunburst.setter
    @class_sensitive(SunburstOptions)
    def sunburst(self, value):
        self._sunburst = value

    @property
    def tilemap(self) -> Optional[TilemapOptions]:
        """General options to apply to all Tilemap series types.

        A tilemap series is a type of heatmap where the tile shapes are configurable.

        .. tabs::

          .. tab:: Honeycomb Tilemap

            .. figure:: ../../../_static/tilemap-example.png
              :alt: Honeycomb Tilemap Example Chart
              :align: center

          .. tab:: Circle Tilemap

            .. figure:: ../../../_static/tilemap-example-circle.png
              :alt: Tilemap Example Chart
              :align: center

          .. tab:: Diamond Tilemap

            .. figure:: ../../../_static/tilemap-example-diamond.png
              :alt: Tilemap Example Chart
              :align: center

        :rtype: :class:`TilemapOptions` or :obj:`None <python:None>`
        """
        return self._tilemap

    @tilemap.setter
    @class_sensitive(TilemapOptions)
    def tilemap(self, value):
        self._tilemap = value

    @property
    def timeline(self) -> Optional[TimelineOptions]:
        """General options to apply to all Timeline series types.

        The timeline series presents given events along a drawn line.

        .. tabs::

          .. tab:: Standard Timeline

            .. figure:: ../../../_static/timeline-example.png
              :alt: Timeline Example Chart
              :align: center

          .. tab:: Inverted Timeline

            .. figure:: ../../../_static/timeline-example-inverted.png
              :alt: Inverted Timeline Example Chart
              :align: center

          .. tab:: With True Datetime Axis

            .. figure:: ../../../_static/timeline-example-datetime.png
              :alt: Timeline Example Chart with Datetime Axis
              :align: center

        :rtype: :class:`TimelineOptions` or :obj:`None <python:None>`
        """
        return self._timeline

    @timeline.setter
    @class_sensitive(TimelineOptions)
    def timeline(self, value):
        self._timeline = value

    @property
    def treegraph(self) -> Optional[TreegraphOptions]:
        """General options to apply to all :term:`Treegraph` series types.
        
        A treegraph visualizes a relationship between ancestors and descendants with a clear parent-child relationship,
        e.g. a family tree or a directory structure.
        
        .. figure:: ../../../_static/treegraph-example.png
          :alt: Treegraph Example Chart
          :align: center
        
        :rtype: :class:`TreegraphOptions <highcharts_stock.options.plot_options.treegraph.TreegraphOptions>` or 
          :obj:`None <python:None>`
        """
        return self._treegraph
    
    @treegraph.setter
    @class_sensitive(TreegraphOptions)
    def treegraph(self, value):
        self._treegraph = value

    @property
    def treemap(self) -> Optional[TreemapOptions]:
        """General options to apply to all Treemap series types.

        A treemap displays hierarchical data using nested rectangles. The data can be laid
        out in varying ways depending on options.

        .. figure:: ../../../_static/treemap-example.png
          :alt: Treemap Example Chart
          :align: center

        :rtype: :class:`TreemapOptions` or :obj:`None <python:None>`
        """
        return self._treemap

    @treemap.setter
    @class_sensitive(TreemapOptions)
    def treemap(self, value):
        self._treemap = value

    @property
    def variablepie(self) -> Optional[VariablePieOptions]:
        """General options to apply to all Variable Pie series types.

        A variable pie series is a two dimensional series type, where each point renders
        an Y and Z value. Each point is drawn as a pie slice where the size (arc) of the
        slice relates to the Y value and the radius of pie slice relates to the Z value.

        .. figure:: ../../../_static/variablepie-example.png
          :alt: Variable Pie Example Chart
          :align: center

        :rtype: :class:`VariablePieOptions` or :obj:`None <python:None>`
        """
        return self._variablepie

    @variablepie.setter
    @class_sensitive(VariablePieOptions)
    def variablepie(self, value):
        self._variablepie = value

    @property
    def variwide(self) -> Optional[VariwideOptions]:
        """General options to apply to all Variwide series types.

        A variwide chart (related to marimekko chart) is a column chart with a variable
        width expressing a third dimension.

        .. tabs::

          .. tab:: Standard Variwide

            .. figure:: ../../../_static/variwide-example.png
              :alt: Variwide Example Chart
              :align: center

          .. tab:: Inverted Variwide

            .. figure:: ../../../_static/variwide-example-inverted.png
              :alt: Variwide Example Chart
              :align: center

          .. tab:: with Datetime Axis

            .. figure:: ../../../_static/variwide-example-datetime.png
              :alt: Variwide Example Chart
              :align: center

        :rtype: :class:`VariwideOptions` or :obj:`None <python:None>`
        """
        return self._variwide

    @variwide.setter
    @class_sensitive(VariwideOptions)
    def variwide(self, value):
        self._variwide = value

    @property
    def vector(self) -> Optional[VectorOptions]:
        """General options to apply to all Vector series types.

        A vector plot is a type of cartesian chart where each point has an X and Y
        position, a length and a direction. Vectors are drawn as arrows.

        .. figure:: ../../../_static/vector-example.png
          :alt: Vector Example Chart
          :align: center

        :rtype: :class:`VectorOptions` or :obj:`None <python:None>`
        """
        return self._vector

    @vector.setter
    @class_sensitive(VectorOptions)
    def vector(self, value):
        self._vector = value

    @property
    def venn(self) -> Optional[VennOptions]:
        """General options to apply to all Venn series types.

        A Venn diagram displays all possible logical relations between a collection of
        different sets. The sets are represented by circles, and the relation between the
        sets are displayed by the overlap or lack of overlap between them. The venn
        diagram is a special case of Euler diagrams, which can also be displayed by this
        series type.

        .. tabs::

          .. tab:: Venn Diagram

            .. figure:: ../../../_static/venn-example.png
              :alt: Venn Example Chart
              :align: center

          .. tab:: Euler Diagram

            .. figure:: ../../../_static/venn-example-euler.png
              :alt: Euler Example Chart
              :align: center

        :rtype: :class:`VennOptions` or :obj:`None <python:None>`
        """
        return self._venn

    @venn.setter
    @class_sensitive(VennOptions)
    def venn(self, value):
        self._venn = value

    @property
    def waterfall(self) -> Optional[WaterfallOptions]:
        """General options to apply to all Waterfall series types.

        A waterfall chart displays sequentially introduced positive or negative values in
        cumulative columns.

        .. tabs::

          .. tab:: Standard Waterfall

            .. figure:: ../../../_static/waterfall-example.png
              :alt: Waterfall Example Chart
              :align: center

          .. tab:: Horizontal (Inverted) Waterfall

            .. figure:: ../../../_static/waterfall-example-inverted.png
              :alt: Waterfall Example Chart
              :align: center

          .. tab:: Stacked Waterfall

            .. figure:: ../../../_static/waterfall-example-stacked.png
              :alt: Waterfall Example Chart
              :align: center

        :rtype: :class:`WaterfallOptions` or :obj:`None <python:None>`
        """
        return self._waterfall

    @waterfall.setter
    @class_sensitive(WaterfallOptions)
    def waterfall(self, value):
        self._waterfall = value

    @property
    def windbarb(self) -> Optional[WindBarbOptions]:
        """General options to apply to all Wind Barb series types.

        Wind barbs are a convenient way to represent wind speed and direction in one
        graphical form. Wind direction is given by the stem direction, and wind speed by
        the number and shape of barbs.

        .. figure:: ../../../_static/windbarb-example.png
          :alt: Wind Barb Example Chart
          :align: center

        :rtype: :class:`WindBarbOptions` or :obj:`None <python:None>`
        """
        return self._windbarb

    @windbarb.setter
    @class_sensitive(WindBarbOptions)
    def windbarb(self, value):
        self._windbarb = value

    @property
    def wordcloud(self) -> Optional[WordcloudOptions]:
        """General options to apply to all Wordcloud series types.

        A word cloud is a visualization of a set of words, where the size and placement of
        a word is determined by how it is weighted.

        .. figure:: ../../../_static/wordcloud-example.png
          :alt: Wordcloud Example Chart
          :align: center

        :rtype: :class:`WordcloudOptions` or :obj:`None <python:None>`
        """
        return self._wordcloud

    @wordcloud.setter
    @class_sensitive(WordcloudOptions)
    def wordcloud(self, value):
        self._wordcloud = value

    @property
    def xrange(self) -> Optional[XRangeOptions]:
        """General options to apply to all X-Range series types.

        The X-range series displays ranges on the X axis, typically time intervals with a
        start and end date.

        .. tabs::

          .. tab:: Standard X-Range

            .. figure:: ../../../_static/xrange-example.png
              :alt: X-Range Example Chart
              :align: center

          .. tab:: Inverted X-Range

            .. figure:: ../../../_static/xrange-example-inverted.png
              :alt: Inverted X-Range Example Chart
              :align: center

        :rtype: :class:`XRangeOptions` or :obj:`None <python:None>`
        """
        return self._xrange

    @xrange.setter
    @class_sensitive(XRangeOptions)
    def xrange(self, value):
        self._xrange = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'arcdiagram': as_dict.get('arcdiagram', None),
            'area': as_dict.get('area', None),
            'arearange': as_dict.get('arearange', None),
            'areaspline': as_dict.get('areaspline', None),
            'areasplinerange': as_dict.get('areasplinerange', None),
            'bar': as_dict.get('bar', None),
            'bellcurve': as_dict.get('bellcurve', None),
            'boxplot': as_dict.get('boxplot', None),
            'bubble': as_dict.get('bubble', None),
            'bullet': as_dict.get('bullet', None),
            'column': as_dict.get('column', None),
            'columnpyramid': as_dict.get('columnpyramid', None),
            'columnrange': as_dict.get('columnrange', None),
            'cylinder': as_dict.get('cylinder', None),
            'dependencywheel': as_dict.get('dependencywheel', None),
            'dumbbell': as_dict.get('dumbbell', None),
            'errorbar': as_dict.get('errorbar', None),
            'funnel': as_dict.get('funnel', None),
            'funnel_3d': as_dict.get('funnel3d', None),
            'gauge': as_dict.get('gauge', None),
            'heatmap': as_dict.get('heatmap', None),
            'histogram': as_dict.get('histogram', None),
            'item': as_dict.get('item', None),
            'line': as_dict.get('line', None),
            'lollipop': as_dict.get('lollipop', None),
            'networkgraph': as_dict.get('networkgraph', None),
            'organization': as_dict.get('organization', None),
            'packedbubble': as_dict.get('packedbubble', None),
            'pareto': as_dict.get('pareto', None),
            'pictorial': as_dict.get('pictorial', None),
            'pie': as_dict.get('pie', None),
            'polygon': as_dict.get('polygon', None),
            'pyramid': as_dict.get('pyramid', None),
            'pyramid_3d': as_dict.get('pyramid3d', None),
            'sankey': as_dict.get('sankey', None),
            'scatter': as_dict.get('scatter', None),
            'scatter_3d': as_dict.get('scatter3d', None),
            'series': as_dict.get('series', None),
            'solidgauge': as_dict.get('solidgauge', None),
            'spline': as_dict.get('spline', None),
            'streamgraph': as_dict.get('streamgraph', None),
            'sunburst': as_dict.get('sunburst', None),
            'tilemap': as_dict.get('tilemap', None),
            'timeline': as_dict.get('timeline', None),
            'treegraph': as_dict.get('treegraph', None),
            'treemap': as_dict.get('treemap', None),
            'variablepie': as_dict.get('variablepie', None),
            'variwide': as_dict.get('variwide', None),
            'vector': as_dict.get('vector', None),
            'venn': as_dict.get('venn', None),
            'waterfall': as_dict.get('waterfall', None),
            'windbarb': as_dict.get('windbarb', None),
            'wordcloud': as_dict.get('wordcloud', None),
            'xrange': as_dict.get('xrange', None),

            'abands': as_dict.get('abands', None),
            'ad': as_dict.get('ad', None),
            'ao': as_dict.get('ao', None),
            'apo': as_dict.get('apo', None),
            'aroon': as_dict.get('aroon', None),
            'aroonoscillator': as_dict.get('aroonoscillator', None),
            'atr': as_dict.get('atr', None),
            'bb': as_dict.get('bb', None),
            'candlestick': as_dict.get('candlestick', None),
            'cci': as_dict.get('cci', None),
            'chaikin': as_dict.get('chaikin', None),
            'cmf': as_dict.get('cmf', None),
            'cmo': as_dict.get('cmo', None),
            'dema': as_dict.get('dema', None),
            'disparityindex': as_dict.get('disparityindex', None),
            'dmi': as_dict.get('dmi', None),
            'dpo': as_dict.get('dpo', None),
            'ema': as_dict.get('ema', None),
            'flags': as_dict.get('flags', None),
            'heikinashi': as_dict.get('heikinashi', None),
            'hlc': as_dict.get('hlc', None),
            'hollowcandlestick': as_dict.get('hollowcandlestick', None),
            'ikh': as_dict.get('ikh', None),
            'keltnerchannels': as_dict.get('keltnerchannels', None),
            'klinger': as_dict.get('klinger', None),
            'linearregression': as_dict.get('linearregression', None),
            'linearregressionangle': as_dict.get('linearregressionangle', None),
            'linearregressionintercept': as_dict.get('linearregressionintercept', None),
            'linearregressionslope': as_dict.get('linearregressionslope', None),
            'macd': as_dict.get('macd', None),
            'mfi': as_dict.get('mfi', None),
            'momentum': as_dict.get('momentum', None),
            'natr': as_dict.get('natr', None),
            'obv': as_dict.get('obv', None),
            'ohlc': as_dict.get('ohlc', None),
            'pc': as_dict.get('pc', None),
            'pivotpoints': as_dict.get('pivotpoints', None),
            'ppo': as_dict.get('ppo', None),
            'priceenvelopes': as_dict.get('priceenvelopes', None),
            'psar': as_dict.get('psar', None),
            'roc': as_dict.get('roc', None),
            'rsi': as_dict.get('rsi', None),
            'slowstochastic': as_dict.get('slowstochastic', None),
            'sma': as_dict.get('sma', None),
            'stochastic': as_dict.get('stochastic', None),
            'supertrend': as_dict.get('supertrend', None),
            'tema': as_dict.get('tema', None),
            'trendline': as_dict.get('trendline', None),
            'trix': as_dict.get('trix', None),
            'vbp': as_dict.get('vbp', None),
            'vwap': as_dict.get('vwap', None),
            'williamsr': as_dict.get('williamsr', None),
            'wma': as_dict.get('wma', None),
            'zigzag': as_dict.get('zigzag', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'abands': self.abands,
            'ad': self.ad,
            'ao': self.ao,
            'apo': self.apo,
            'aroon': self.aroon,
            'aroonoscillator': self.aroonoscillator,
            'atr': self.atr,
            'bb': self.bb,
            'candlestick': self.candlestick,
            'cci': self.cci,
            'chaikin': self.chaikin,
            'cmf': self.cmf,
            'cmo': self.cmo,
            'dema': self.dema,
            'disparityindex': self.disparityindex,
            'dmi': self.dmi,
            'dpo': self.dpo,
            'ema': self.ema,
            'flags': self.flags,
            'heikinashi': self.heikinashi,
            'hlc': self.hlc,
            'hollowcandlestick': self.hollowcandlestick,
            'ikh': self.ikh,
            'keltnerchannels': self.keltnerchannels,
            'klinger': self.klinger,
            'linearregression': self.linearregression,
            'linearregressionangle': self.linearregressionangle,
            'linearregressionintercept': self.linearregressionintercept,
            'linearregressionslope': self.linearregressionslope,
            'macd': self.macd,
            'mfi': self.mfi,
            'momentum': self.momentum,
            'natr': self.natr,
            'obv': self.obv,
            'ohlc': self.ohlc,
            'pc': self.pc,
            'pivotpoints': self.pivotpoints,
            'ppo': self.ppo,
            'priceenvelopes': self.priceenvelopes,
            'psar': self.psar,
            'roc': self.roc,
            'rsi': self.rsi,
            'slowstochastic': self.slowstochastic,
            'sma': self.sma,
            'stochastic': self.stochastic,
            'supertrend': self.supertrend,
            'tema': self.tema,
            'trendline': self.trendline,
            'trix': self.trix,
            'vbp': self.vbp,
            'vwap': self.vwap,
            'williamsr': self.williamsr,
            'wma': self.wma,
            'zigzag': self.zigzag,

            'arcdiagram': self.arcdiagram,
            'area': self.area,
            'arearange': self.arearange,
            'areaspline': self.areaspline,
            'areasplinerange': self.areasplinerange,
            'bar': self.bar,
            'bellcurve': self.bellcurve,
            'boxplot': self.boxplot,
            'bubble': self.bubble,
            'bullet': self.bullet,
            'column': self.column,
            'columnpyramid': self.columnpyramid,
            'columnrange': self.columnrange,
            'cylinder': self.cylinder,
            'dependencywheel': self.dependencywheel,
            'dumbbell': self.dumbbell,
            'errorbar': self.errorbar,
            'funnel': self.funnel,
            'funnel3d': self.funnel_3d,
            'gauge': self.gauge,
            'heatmap': self.heatmap,
            'histogram': self.histogram,
            'item': self.item,
            'line': self.line,
            'lollipop': self.lollipop,
            'networkgraph': self.networkgraph,
            'organization': self.organization,
            'packedbubble': self.packedbubble,
            'pareto': self.pareto,
            'pictorial': self.pictorial,
            'pie': self.pie,
            'polygon': self.polygon,
            'pyramid': self.pyramid,
            'pyramid3d': self.pyramid_3d,
            'sankey': self.sankey,
            'scatter': self.scatter,
            'scatter3d': self.scatter_3d,
            'series': self.series,
            'solidgauge': self.solidgauge,
            'spline': self.spline,
            'streamgraph': self.streamgraph,
            'sunburst': self.sunburst,
            'tilemap': self.tilemap,
            'timeline': self.timeline,
            'treegraph': self.treegraph,
            'treemap': self.treemap,
            'variablepie': self.variablepie,
            'variwide': self.variwide,
            'vector': self.vector,
            'venn': self.venn,
            'waterfall': self.waterfall,
            'windbarb': self.windbarb,
            'wordcloud': self.wordcloud,
            'xrange': self.xrange
        }

        return untrimmed

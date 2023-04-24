################################################################
:mod:`.series <highcharts_stock.options.series>`
################################################################

.. contents:: Module Contents
  :local:
  :depth: 3
  :backlinks: entry

.. toctree::
  :titlesonly:

  abands
  ad
  arcdiagram
  area
  aroon
  atr
  averages
  bar
  base
  bellcurve
  boxplot
  bubble
  bullet
  candlestick
  data/index
  dependencywheel
  disparity_index
  dmi
  dumbbell
  flags
  funnel
  gauge
  heatmap
  histogram
  hlc
  item
  labels
  linear_regressions
  momentum/index
  networkgraph
  oscillators/index
  organization
  packedbubble
  pareto
  pictorial
  pie
  pivot_points
  points
  polygon
  price_envelopes
  psar
  pyramid
  sankey
  scatter
  series_generator
  spline
  sunburst
  timeline
  treegraph
  treemap
  vbp
  vector
  venn
  wordcloud
  zigzag

-------------------------

***************************
Sub-components
***************************

.. list-table::
  :widths: 60 40
  :header-rows: 1

  * - Module
    - Classes / Functions
  * - :mod:`.options.series <highcharts_stock.options.series>`
    -
  * - :mod:`.options.series.abands <highcharts_stock.options.series.abands>`
    - :class:`AbandsSeries <highcharts_stock.options.series.abands.AbandsSeries>`
      :class:`BBSeries <highcharts_stock.options.series.abands.BBSeries>`
      :class:`KeltnerChannelsSeries <highcharts_stock.options.series.abands.KeltnerChannelsSeries>`
      :class:`PCSeries <highcharts_stock.options.series.abands.PCSeries>`
  * - :mod:`.options.series.ad <highcharts_stock.options.series.ad>`
    - :class:`ADSeries <highcharts_stock.options.series.ad.ADSeries>`
  * - :mod:`.options.series.arcdiagram <highcharts_stock.options.series.arcdiagram>`
    - :class:`ArcDiagramSeries <highcharts_stock.options.series.arcdiagram.ArcDiagramSeries>`
  * - :mod:`.options.series.area <highcharts_stock.options.series.area>`
    - :class:`AreaSeries <highcharts_stock.options.series.area.AreaSeries>`
      :class:`AreaRangeSeries <highcharts_stock.options.series.area.AreaRangeSeries>`
      :class:`AreaSplineSeries <highcharts_stock.options.series.area.AreaSplineSeries>`
      :class:`AreaSplineRangeSeries <highcharts_stock.options.series.area.AreaSplineRangeSeries>`
      :class:`LineSeries <highcharts_stock.options.series.area.LineSeries>`
      :class:`StreamGraphSeries <highcharts_stock.options.series.area.StreamGraphSeries>`
  * - :mod:`.options.series.aroon <highcharts_stock.options.series.aroon>`
    - :class:`AroonSeries <highcharts_stock.options.series.aroon.AroonSeries>`
  * - :mod:`.options.series.atr <highcharts_stock.options.series.atr>`
    - :class:`ATRSeries <highcharts_stock.options.series.atr.ATRSeries>`
      :class:`NATRSeries <highcharts_stock.options.series.atr.NATRSeries>`
  * - :mod:`.options.series.averages <highcharts_stock.options.series.averages>`
    - :class:`DEMASeries <highcharts_stock.options.series.averages.DEMASeries>`
      :class:`EMASeries <highcharts_stock.options.series.averages.EMASeries>`
      :class:`SMASeries <highcharts_stock.options.series.averages.SMASeries>`
      :class:`TEMASeries <highcharts_stock.options.series.averages.TEMASeries>`
      :class:`VWAPSeries <highcharts_stock.options.series.averages.VWAPSeries>`
      :class:`WMASeries <highcharts_stock.options.series.averages.WMASeries>`
  * - :mod:`.options.series.bar <highcharts_stock.options.series.bar>`
    - :class:`BarSeries <highcharts_stock.options.series.bar.BarSeries>`
      :class:`ColumnSeries <highcharts_stock.options.series.bar.ColumnSeries>`
      :class:`ColumnPyramidSeries <highcharts_stock.options.series.bar.ColumnPyramidSeries>`
      :class:`ColumnRangeSeries <highcharts_stock.options.series.bar.ColumnRangeSeries>`
      :class:`CylinderSeries <highcharts_stock.options.series.bar.CylinderSeries>`
      :class:`VariwideSeries <highcharts_stock.options.series.bar.VariwideSeries>`
      :class:`WaterfallSeries <highcharts_stock.options.series.bar.WaterfallSeries>`
      :class:`WindBarbSeries <highcharts_stock.options.series.bar.WindBarbSeries>`
      :class:`XRangeSeries <highcharts_stock.options.series.bar.XRangeSeries>`
      :class:`BaseBarSeries <highcharts_stock.options.series.bar.BaseBarSeries>`
  * - :mod:`.options.series.base <highcharts_stock.options.series.base>`
    - :class:`SeriesBase <highcharts_stock.options.series.base.SeriesBase>`
      :class:`IndicatorSeriesBase <highcharts_stock.options.series.base.IndicatorSeriesBase>`
      :class:`NavigatorIndicatorSeries <highcharts_stock.options.series.base.NavigatorIndicatorSeries>`
      :class:`IndicatorFactoryMixin <highcharts_stock.options.series.base.IndicatorFactoryMixin>`
  * - :mod:`.options.series.bellcurve <highcharts_stock.options.series.bellcurve>`
    - :class:`BellCurveSeries <highcharts_stock.options.series.bellcurve.BellCurveSeries>`
  * - :mod:`.options.series.boxplot <highcharts_stock.options.series.boxplot>`
    - :class:`BoxPlotSeries <highcharts_stock.options.series.boxplot.BoxPlotSeries>`
      :class:`ErrorBarSeries <highcharts_stock.options.series.boxplot.ErrorBarSeries>`
  * - :mod:`.options.series.bubble <highcharts_stock.options.series.bubble>`
    - :class:`BubbleSeries <highcharts_stock.options.series.bubble.BubbleSeries>`
  * - :mod:`.options.series.bullet <highcharts_stock.options.series.bullet>`
    - :class:`BulletSeries <highcharts_stock.options.series.bullet.BulletSeries>`
  * - :mod:`.options.series.candlestick <highcharts_stock.options.series.candlestick>`
    - :class:`CandlestickSeries <highcharts_stock.options.series.candlestick.CandlestickSeries>`
      :class:`HollowCandlestickSeries <highcharts_stock.options.series.candlestick.HollowCandlestickSeries>`
      :class:`HeikinAshiSeries <highcharts_stock.options.series.candlestick.HeikinAshiSeries>`
  * - :mod:`.options.series.data <highcharts_stock.options.series.data>`
    -
  * - :mod:`.options.series.data.accessibility <highcharts_stock.options.series.data.accessibility>`
    - :class:`DataPointAccessibility <highcharts_stock.options.series.data.accessibility.DataPointAccessibility>`
  * - :mod:`.options.series.data.arcdiagram <highcharts_stock.options.series.data.arcdiagram>`
    - :class:`ArcDiagramData <highcharts_stock.options.series.data.arcdiagram.ArcDiagramData>`
  * - :mod:`.options.series.data.bar <highcharts_stock.options.series.data.bar>`
    - :class:`BarData <highcharts_stock.options.series.data.bar.BarData>`
      :class:`WaterfallData <highcharts_stock.options.series.data.bar.WaterfallData>`
      :class:`WindBarbData <highcharts_stock.options.series.data.bar.WindBarbData>`
      :class:`XRangeData <highcharts_stock.options.series.data.bar.XRangeData>`
  * - :mod:`.options.series.data.base <highcharts_stock.options.series.data.base>`
    - :class:`DataBase <highcharts_stock.options.series.data.base.DataBase>`
  * - :mod:`.options.series.data.boxplot <highcharts_stock.options.series.data.boxplot>`
    - :class:`BoxPlotData <highcharts_stock.options.series.data.boxplot.BoxPlotData>`
  * - :mod:`.options.series.data.bullet <highcharts_stock.options.series.data.bullet>`
    - :class:`BulletData <highcharts_stock.options.series.data.bullet.BulletData>`
  * - :mod:`.options.series.data.candlestick <highcharts_stock.options.series.data.candlestick>`
    - :class:`CandlestickData <highcharts_stock.options.series.data.candlestick.CandlestickData>`
  * - :mod:`.options.series.data.cartesian <highcharts_stock.options.series.data.cartesian>`
    - :class:`CartesianData <highcharts_stock.options.series.data.cartesian.CartesianData>`
      :class:`Cartesian3DData <highcharts_stock.options.series.data.cartesian.Cartesian3DData>`
      :class:`CartesianValueData <highcharts_stock.options.series.data.cartesian.CartesianValueData>`
  * - :mod:`.options.series.data.connections <highcharts_stock.options.series.data.connections>`
    - :class:`ConnectionData <highcharts_stock.options.series.data.connections.ConnectionData>`
      :class:`WeightedConnectionData <highcharts_stock.options.series.data.connections.WeightedConnectionData>`
      :class:`OutgoingWeightedConnectionData <highcharts_stock.options.series.data.connections.OutgoingWeightedConnectionData>`
      :class:`ConnectionBase <highcharts_stock.options.series.data.connections.ConnectionBase>`
  * - :mod:`.options.series.data.hlc <highcharts_stock.options.series.data.hlc>`
    - :class:`HLCData <highcharts_stock.options.series.data.hlc.HLCData>`
      :class:`OHLCData <highcharts_stock.options.series.data.hlc.OHLCData>`
  * - :mod:`.options.series.data.pie <highcharts_stock.options.series.data.pie>`
    - :class:`PieData <highcharts_stock.options.series.data.pie.PieData>`
      :class:`VariablePieData <highcharts_stock.options.series.data.pie.VariablePieData>`
  * - :mod:`.options.series.data.range <highcharts_stock.options.series.data.range>`
    - :class:`RangeData <highcharts_stock.options.series.data.range.RangeData>`
      :class:`ConnectedRangeData <highcharts_stock.options.series.data.range.ConnectedRangeData>`
  * - :mod:`.options.series.data.single_point <highcharts_stock.options.series.data.single_point>`
    - :class:`SinglePointData <highcharts_stock.options.series.data.single_point.SinglePointData>`
      :class:`SingleValueData <highcharts_stock.options.series.data.single_point.SingleValueData>`
      :class:`SingleXData <highcharts_stock.options.series.data.single_point.SingleXData>`
      :class:`LabeledSingleXData <highcharts_stock.options.series.data.single_point.LabeledSingleXData>`
      :class:`ConnectedSingleXData <highcharts_stock.options.series.data.single_point.ConnectedSingleXData>`
      :class:`SinglePointBase <highcharts_stock.options.series.data.single_point.SinglePointBase>`
  * - :mod:`.options.series.data.sunburst <highcharts_stock.options.series.data.sunburst>`
    - :class:`SunburstData <highcharts_stock.options.series.data.sunburst.SunburstData>`
  * - :mod:`.options.series.data.treegraph <highcharts_stock.options.series.data.treegraph>`
    - :class:`TreegraphData <highcharts_stock.options.series.data.treegraph.TreegraphData>`
  * - :mod:`.options.series.data.treemap <highcharts_stock.options.series.data.treemap>`
    - :class:`TreemapData <highcharts_stock.options.series.data.treemap.TreemapData>`
  * - :mod:`.options.series.data.vector <highcharts_stock.options.series.data.vector>`
    - :class:`VectorData <highcharts_stock.options.series.data.vector.VectorData>`
  * - :mod:`.options.series.data.venn <highcharts_stock.options.series.data.venn>`
    - :class:`VennData <highcharts_stock.options.series.data.venn.VennData>`
  * - :mod:`.options.series.data.wordcloud <highcharts_stock.options.series.data.wordcloud>`
    - :class:`WordcloudData <highcharts_stock.options.series.data.wordcloud.WordcloudData>`
  * - :mod:`.options.series.dependencywheel <highcharts_stock.options.series.dependencywheel>`
    - :class:`DependencyWheelSeries <highcharts_stock.options.series.dependencywheel.DependencyWheelSeries>`
  * - :mod:`.options.series.disparity_index <highcharts_stock.options.series.disparity_index>`
    - :class:`DisparityIndexSeries <highcharts_stock.options.series.disparity_index.DisparityIndexSeries>`
  * - :mod:`.options.series.dmi <highcharts_stock.options.series.dmi>`
    - :class:`DMISeries <highcharts_stock.options.series.dmi.DMISeries>`
  * - :mod:`.options.series.dumbbell <highcharts_stock.options.series.dumbbell>`
    - :class:`DumbbellSeries <highcharts_stock.options.series.dumbbell.DumbbellSeries>`
      :class:`LollipopSeries <highcharts_stock.options.series.dumbbell.LollipopSeries>`
  * - :mod:`.options.series.flags <highcharts_stock.options.series.flags>`
    - :class:`FlagsSeries <highcharts_stock.options.series.flags.FlagsSeries>`
  * - :mod:`.options.series.funnel <highcharts_stock.options.series.funnel>`
    - :class:`FunnelSeries <highcharts_stock.options.series.funnel.FunnelSeries>`
      :class:`Funnel3DSeries <highcharts_stock.options.series.funnel.Funnel3DSeries>`
  * - :mod:`.options.series.gauge <highcharts_stock.options.series.gauge>`
    - :class:`GaugeSeries <highcharts_stock.options.series.gauge.GaugeSeries>`
      :class:`SolidGaugeSeries <highcharts_stock.options.series.gauge.SolidGaugeSeries>`
  * - :mod:`.options.series.heatmap <highcharts_stock.options.series.heatmap>`
    - :class:`HeatmapSeries <highcharts_stock.options.series.heatmap.HeatmapSeries>`
      :class:`TilemapSeries <highcharts_stock.options.series.heatmap.TilemapSeries>`
  * - :mod:`.options.series.histogram <highcharts_stock.options.series.histogram>`
    - :class:`HistogramSeries <highcharts_stock.options.series.histogram.HistogramSeries>`
  * - :mod:`.options.series.hlc <highcharts_stock.options.series.hlc>`
    - :class:`HLCSeries <highcharts_stock.options.series.hlc.HLCSeries>`
      :class:`OHLCSeries <highcharts_stock.options.series.hlc.OHLCSeries>`
  * - :mod:`.options.series.item <highcharts_stock.options.series.item>`
    - :class:`ItemSeries <highcharts_stock.options.series.item.ItemSeries>`
  * - :mod:`.options.series.labels <highcharts_stock.options.series.labels>`
    - :class:`SeriesLabel <highcharts_stock.options.series.labels.SeriesLabel>`
      :class:`Box <highcharts_stock.options.series.labels.Box>`
  * - :mod:`.options.series.linear_regressions <highcharts_stock.options.series.linear_regressions>`
    - :class:`LinearRegressionSeries <highcharts_stock.options.series.linear_regressions.LinearRegressionSeries>`
      :class:`LinearRegressionAngleSeries <highcharts_stock.options.series.linear_regressions.LinearRegressionAngleSeries>`
      :class:`LinearRegressionInterceptSeries <highcharts_stock.options.series.linear_regressions.LinearRegressionInterceptSeries>`
      :class:`LinearRegressionSlopeSeries <highcharts_stock.options.series.linear_regressions.LinearRegressionSlopeSeries>`
      :class:`TrendlineSeries <highcharts_stock.options.series.linear_regressions.TrendlineSeries>`
  * - :mod:`.options.series.momentum <highcharts_stock.options.series.momentum>`
    - :class:`MomentumSeries <highcharts_stock.options.series.momentum.MomentumSeries>`
      :class:`OBVSeries <highcharts_stock.options.series.momentum.OBVSeries>`
      :class:`ROCSeries <highcharts_stock.options.series.momentum.ROCSeries>`
      :class:`RSISeries <highcharts_stock.options.series.momentum.RSISeries>`
  * - :mod:`.options.series.momentum.ikh <highcharts_stock.options.series.momentum.ikh>`
    - :class:`IKHSeries <highcharts_stock.options.series.momentum.ikh.IKHSeries>`
  * - :mod:`.options.series.momentum.macd <highcharts_stock.options.series.momentum.macd>`
    - :class:`MACDSeries <highcharts_stock.options.series.momentum.macd.MACDSeries>`
  * - :mod:`.options.series.momentum.supertrend <highcharts_stock.options.series.momentum.supertrend>`
    - :class:`SupertrendSeries <highcharts_stock.options.series.momentum.supertrend.SupertrendSeries>`
  * - :mod:`.options.series.networkgraph <highcharts_stock.options.series.networkgraph>`
    - :class:`NetworkGraphSeries <highcharts_stock.options.series.networkgraph.NetworkGraphSeries>`
  * - :mod:`.options.series.organization <highcharts_stock.options.series.organization>`
    - :class:`OrganizationSeries <highcharts_stock.options.series.organization.OrganizationSeries>`
  * - :mod:`.options.series.oscillators <highcharts_stock.options.series.oscillators>`
    - :class:`AroonOscillatorSeries <highcharts_stock.options.series.oscillators.AroonOscillatorSeries>`
      :class:`APOSeries <highcharts_stock.options.series.oscillators.APOSeries>`
      :class:`CCISeries <highcharts_stock.options.series.oscillators.CCISeries>`
      :class:`ChaikinSeries <highcharts_stock.options.series.oscillators.ChaikinSeries>`
      :class:`CMOSeries <highcharts_stock.options.series.oscillators.CMOSeries>`
      :class:`DPOSeries <highcharts_stock.options.series.oscillators.DPOSeries>`
      :class:`TRIXSeries <highcharts_stock.options.series.oscillators.TRIXSeries>`
      :class:`WilliamsRSeries <highcharts_stock.options.series.oscillators.WilliamsRSeries>`
  * - :mod:`.options.series.oscillators.ao <highcharts_stock.options.series.oscillators.ao>`
    - :class:`AOSeries <highcharts_stock.options.series.oscillators.ao.AOSeries>`
  * - :mod:`.options.series.oscillators.klinger <highcharts_stock.options.series.oscillators.klinger>`
    - :class:`KlingerSeries <highcharts_stock.options.series.oscillators.klinger.KlingerSeries>`
  * - :mod:`.options.series.oscillators.money_flow <highcharts_stock.options.series.oscillators.money_flow>`
    - :class:`MFISeries <highcharts_stock.options.series.oscillators.money_flow.MFISeries>`
      :class:`CMFSeries <highcharts_stock.options.series.oscillators.money_flow.CMFSeries>`
  * - :mod:`.options.series.oscillators.ppo <highcharts_stock.options.series.oscillators.ppo>`
    - :class:`PPOSeries <highcharts_stock.options.series.oscillators.ppo.PPOSeries>`
  * - :mod:`.options.series.oscillators.stochastic <highcharts_stock.options.series.oscillators.stochastic>`
    - :class:`StochasticSeries <highcharts_stock.options.series.oscillators.stochastic.StochasticSeries>`
      :class:`SlowStochasticSeries <highcharts_stock.options.series.oscillators.stochastic.SlowStochasticSeries>`
  * - :mod:`.options.series.packedbubble <highcharts_stock.options.series.packedbubble>`
    - :class:`PackedBubbleSeries <highcharts_stock.options.series.packedbubble.PackedBubbleSeries>`
  * - :mod:`.options.series.pareto <highcharts_stock.options.series.pareto>`
    - :class:`ParetoSeries <highcharts_stock.options.series.pareto.ParetoSeries>`
  * - :mod:`.options.series.pictorial <highcharts_stock.options.series.pictorial>`
    - :class:`PictorialSeries <highcharts_stock.options.series.pictorial.PictorialSeries>`
      :class:`PictorialPaths <highcharts_stock.options.series.pictorial.PictorialPaths>`
  * - :mod:`.options.series.pie <highcharts_stock.options.series.pie>`
    - :class:`PieSeries <highcharts_stock.options.series.pie.PieSeries>`
      :class:`VariablePieSeries <highcharts_stock.options.series.pie.VariablePieSeries>`
  * - :mod:`.options.series.pivot_points <highcharts_stock.options.series.pivot_points>`
    - :class:`PivotPointsSeries <highcharts_stock.options.series.pivot_points.PivotPointsSeries>`
  * - :mod:`.options.series.polygon <highcharts_stock.options.series.polygon>`
    - :class:`PolygonSeries <highcharts_stock.options.series.polygon.PolygonSeries>`
  * - :mod:`.options.series.price_envelopes <highcharts_stock.options.series.price_envelopes>`
    - :class:`PriceEnvelopesSeries <highcharts_stock.options.series.price_envelopes.PriceEnvelopesSeries>`
  * - :mod:`.options.series.psar <highcharts_stock.options.series.psar>`
    - :class:`PSARSeries <highcharts_stock.options.series.psar.PSARSeries>`
  * - :mod:`.options.series.pyramid <highcharts_stock.options.series.pyramid>`
    - :class:`PyramidSeries <highcharts_stock.options.series.pyramid.PyramidSeries>`
      :class:`Pyramid3DSeries <highcharts_stock.options.series.pyramid.Pyramid3DSeries>`
  * - :mod:`.options.series.sankey <highcharts_stock.options.series.sankey>`
    - :class:`SankeySeries <highcharts_stock.options.series.sankey.SankeySeries>`
  * - :mod:`.options.series.scatter <highcharts_stock.options.series.scatter>`
    - :class:`ScatterSeries <highcharts_stock.options.series.scatter.ScatterSeries>`
      :class:`Scatter3DSeries <highcharts_stock.options.series.scatter.Scatter3DSeries>`
  * - :mod:`.options.series.series_generator <highcharts_stock.options.series.series_generator>`
    - :func:`create_series_obj() <highcharts_stock.options.series.series_generator.create_series_obj>`
  * - :mod:`.options.series.spline <highcharts_stock.options.series.spline>`
    - :class:`SplineSeries <highcharts_stock.options.series.spline.SplineSeries>`
  * - :mod:`.options.series.sunburst <highcharts_stock.options.series.sunburst>`
    - :class:`SunburstSeries <highcharts_stock.options.series.sunburst.SunburstSeries>`
  * - :mod:`.options.series.timeline <highcharts_stock.options.series.timeline>`
    - :class:`TimelineSeries <highcharts_stock.options.series.timeline.TimelineSeries>`
  * - :mod:`.options.series.treegraph <highcharts_stock.options.series.treegraph>`
    - :class:`TreegraphSeries <highcharts_stock.options.series.treegraph.TreegraphSeries>`
  * - :mod:`.options.series.treemap <highcharts_stock.options.series.treemap>`
    - :class:`TreemapSeries <highcharts_stock.options.series.treemap.TreemapSeries>`
  * - :mod:`.options.series.vbp <highcharts_stock.options.series.vbp>`
    - :class:`VBPSeries <highcharts_stock.options.series.vbp.VBPSeries>`
  * - :mod:`.options.series.vector <highcharts_stock.options.series.vector>`
    - :class:`VectorSeries <highcharts_stock.options.series.vector.VectorSeries>`
  * - :mod:`.options.series.venn <highcharts_stock.options.series.venn>`
    - :class:`VennSeries <highcharts_stock.options.series.venn.VennSeries>`
  * - :mod:`.options.series.wordcloud <highcharts_stock.options.series.wordcloud>`
    - :class:`WordcloudSeries <highcharts_stock.options.series.wordcloud.WordcloudSeries>`
  * - :mod:`.options.series.zigzag <highcharts_stock.options.series.zigzag>`
    - :class:`ZigZagSeries <highcharts_stock.options.series.zigzag.ZigZagSeries>`

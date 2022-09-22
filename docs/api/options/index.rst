##############################################################
:mod:`.options <highcharts_stock.options>`
##############################################################

.. contents:: Module Contents
  :local:
  :depth: 3
  :backlinks: entry

.. toctree::
  :titlesonly:

  accessibility/index
  annotations/index
  axes/index
  boost
  caption
  chart/index
  credits
  data
  defs
  drilldown
  exporting/index
  legend/index
  loading
  navigation/index
  navigator
  no_data
  pane
  plot_options/index
  responsive
  series/index
  subtitle
  time
  title
  tooltips

--------------

.. module:: highcharts_stock.options

****************************************************************************************
class: :class:`HighchartsOptions <highcharts_stock.options.HighchartsOptions>`
****************************************************************************************

.. autoclass:: HighchartsOptions
  :members:
  :inherited-members:

-----------------------

****************************************************************************************
class: :class:`Options <highcharts_stock.options.Options>`
****************************************************************************************

.. autoclass:: Options
  :members:
  :inherited-members:

-----------------------

***************************
Sub-components
***************************

.. list-table::
  :widths: 60 40
  :header-rows: 1

  * - Module
    - Classes / Functions
  * - :mod:`.options <highcharts_stock.options>`
    - :class:`HighchartsOptions <highcharts_stock.options.HighchartsOptions>`
      :class:`Options <highcharts_stock.options.Options>`
  * - :mod:`.options.accessibility <highcharts_stock.options.accessibility>`
    - :class:`Accessibility <highcharts_stock.options.accessibility.Accessibility>`
      :class:`CustomAccessibilityComponents <highcharts_stock.options.accessibility.CustomAccessibilityComponents>`
  * - :mod:`.options.accessibility.announce_new_data <highcharts_stock.options.accessibility.announce_new_data>`
    - :class:`AnnounceNewData <highcharts_stock.options.accessibility.announce_new_data.AnnounceNewData>`
  * - :mod:`.options.accessibility.keyboard_navigation <highcharts_stock.options.accessibility.keyboard_navigation>`
    - :class:`KeyboardNavigation <highcharts_stock.options.accessibility.keyboard_navigation.KeyboardNavigation>`
  * - :mod:`.options.accessibility.keyboard_navigation.focus_border <highcharts_stock.options.accessibility.keyboard_navigation.focus_border>`
    - :class:`FocusBorder <highcharts_stock.options.accessibility.keyboard_navigation.focus_border.FocusBorder>`
      :class:`FocusBorderStyle <highcharts_stock.options.accessibility.keyboard_navigation.focus_border.FocusBorderStyle>`
  * - :mod:`.options.accessibility.keyboard_navigation.series_navigation <highcharts_stock.options.accessibility.keyboard_navigation.series_navigation>`
    - :class:`SeriesNavigation <highcharts_stock.options.accessibility.keyboard_navigation.series_navigation.SeriesNavigation>`
  * - :mod:`options.accessibility.point <highcharts_stock.options.accessibility.point>`
    - :class:`AccessibilityPoint <highcharts_stock.options.accessibility.point.AccessibilityPoint>`
  * - :mod:`options.accessibility.screen_reader_section <highcharts_stock.options.accessibility.screen_reader_section>`
    - :class:`ScreenReaderSection <highcharts_stock.options.accessibility.screen_reader_section.ScreenReaderSection>`
  * - :mod:`options.accessibility.series <highcharts_stock.options.accessibility.series>`
    - :class:`SeriesAccessibility <highcharts_stock.options.accessibility.series.SeriesAccessibility>`
  * - :mod:`.options.annotations <highcharts_stock.options.annotations>`
    - :class:`Annotation <highcharts_stock.options.annotations.Annotation>`
  * - :mod:`.options.annotations.animation <highcharts_stock.options.annotations.animation>`
    - :class:`AnnotationAnimation <highcharts_stock.options.annotations.animation.AnnotationAnimation>`
  * - :mod:`.options.annotations.control_point_options <highcharts_stock.options.annotations.control_point_options>`
    - :class:`AnnotationControlPointOption <highcharts_stock.options.annotations.control_point_options.AnnotationControlPointOption>`
  * - :mod:`.options.annotations.events <highcharts_stock.options.annotations.events>`
    - :class:`AnnotationEvent <highcharts_stock.options.annotations.events.AnnotationEvent>`
  * - :mod:`.options.annotations.label_options <highcharts_stock.options.annotations.label_options>`
    - :class:`AnnotationLabel <highcharts_stock.options.annotations.label_options.AnnotationLabel>`
      :class:`AnnotationLabelOptionAccessibility <highcharts_stock.options.annotations.label_options.AnnotationLabelOptionAccessibility>`
      :class:`LabelOptions <highcharts_stock.options.annotations.label_options.LabelOptions>`
  * - :mod:`.options.annotations.options.annotations.points <highcharts_stock.options.annotations.points>`
    - :class:`AnnotationPoint <highcharts_stock.options.annotations.points.AnnotationPoint>`
  * - :mod:`.options.annotations.shape_options <highcharts_stock.options.annotations.shape_options>`
    - :class:`AnnotationShape <highcharts_stock.options.annotations.shape_options.AnnotationShape>`
      :class:`ShapeOptions <highcharts_stock.options.annotations.shape_options.ShapeOptions>`
  * - :mod:`.options.axes <highcharts_stock.options.axes>`
    -
  * - :mod:`.options.axes.accessibility <highcharts_stock.options.axes.accessibility>`
    - :class:`AxisAccessibility <highcharts_stock.options.axes.accessibility.AxisAccessibility>`
  * - :mod:`.options.axes.breaks <highcharts_stock.options.axes.breaks>`
    - :class:`AxisBreak <highcharts_stock.options.axes.breaks.AxisBreak>`
  * - :mod:`.options.axes.color_axis <highcharts_stock.options.axes.color_axis>`
    - :class:`ColorAxis <highcharts_stock.options.axes.color_axis.ColorAxis>`
  * - :mod:`.options.axes.crosshair <highcharts_stock.options.axes.crosshair>`
    - :class:`CrosshairOptions <highcharts_stock.options.axes.crosshair.CrosshairOptions>`
  * - :mod:`.options.axes.data_classes <highcharts_stock.options.axes.data_classes>`
    - :class:`DataClass <highcharts_stock.options.axes.data_classes.DataClass>`
  * - :mod:`.options.axes.generic <highcharts_stock.options.axes.generic>`
    - :class:`GenericAxis <highcharts_stock.options.axes.generic.GenericAxis>`
  * - :mod:`.options.axes.labels <highcharts_stock.options.axes.labels>`
    - :class:`AxisLabelOptions <highcharts_stock.options.axes.labels.AxisLabelOptions>`
      :class:`PlotBandLabel <highcharts_stock.options.axes.labels.PlotBandLabel>`
      :class:`PlotLineLabel <highcharts_stock.options.axes.labels.PlotLineLabel>`
  * - :mod:`.options.axes.markers <highcharts_stock.options.axes.markers>`
    - :class:`AxisMarker <highcharts_stock.options.axes.markers.AxisMarker>`
  * - :mod:`.options.axes.numeric <highcharts_stock.options.axes.numeric>`
    - :class:`NumericAxis <highcharts_stock.options.axes.numeric.NumericAxis>`
  * - :mod:`.options.axes.parallel_axes <highcharts_stock.options.axes.parallel_axes>`
    - :class:`ParallelAxesOptions <highcharts_stock.options.axes.parallel_axes.ParallelAxesOptions>`
  * - :mod:`.options.axes.plot_bands <highcharts_stock.options.axes.plot_bands>`
    - :class:`PlotBand <highcharts_stock.options.axes.plot_bands.PlotBand>`
      :class:`PlotLine <highcharts_stock.options.axes.plot_bands.PlotLine>`
  * - :mod:`.options.axes.title <highcharts_stock.options.axes.title>`
    - :class:`AxisTitle <highcharts_stock.options.axes.title.AxisTitle>`
  * - :mod:`.options.axes.x_axis <highcharts_stock.options.axes.x_axis>`
    - :class:`XAxis <highcharts_stock.options.axes.x_axis.XAxis>`
  * - :mod:`.options.axes.y_axis <highcharts_stock.options.axes.y_axis>`
    - :class:`YAxis <highcharts_stock.options.axes.y_axis.YAxis>`
  * - :mod:`.options.axes.z_axis <highcharts_stock.options.axes.z_axis>`
    - :class:`ZAxis <highcharts_stock.options.axes.z_axis.ZAxis>`
  * - :mod:`.options.boost <highcharts_stock.options.boost>`
    - :class:`Boost <highcharts_stock.options.boost.Boost>`
      :class:`BoostDebug <highcharts_stock.options.boost.BoostDebug>`
  * - :mod:`.options.caption <highcharts_stock.options.caption>`
    - :class:`Caption <highcharts_stock.options.caption.Caption>`
  * - :mod:`.options.chart <highcharts_stock.options.chart>`
    - :class:`ChartOptions <highcharts_stock.options.chart.ChartOptions>`
      :class:`PanningOptions <highcharts_stock.options.chart.PanningOptions>`
  * - :mod:`.chart.options_3d <highcharts_stock.options.chart.options_3d>`
    - :class:`Options3D <highcharts_stock.options.chart.options_3d.Options3D>`
      :class:`Frame <highcharts_stock.options.chart.options_3d.Frame>`
      :class:`PanelOptions <highcharts_stock.options.chart.options_3d.PanelOptions>`
  * - :mod:`.chart.reset_zoom_button <highcharts_stock.options.chart.reset_zoom_button>`
    - :class:`ResetZoomButtonOptions <highcharts_stock.options.chart.reset_zoom_button.ResetZoomButtonOptions>`
  * - :mod:`.chart.scrollable_plot_area <highcharts_stock.options.chart.scrollable_plot_area>`
    - :class:`ScrollablePlotArea <highcharts_stock.options.chart.scrollable_plot_area.ScrollablePlotArea>`
  * - :mod:`.options.credits <highcharts_stock.options.credits>`
    - :class:`Credits <highcharts_stock.options.credits.Credits>`
      :class:`CreditStyleOptions <highcharts_stock.options.credits.CreditStyleOptions>`
  * - :mod:`.options.data <highcharts_stock.options.data>`
    - :class:`Data <highcharts_stock.options.data.Data>`
  * - :mod:`.options.defs <highcharts_stock.options.defs>`
    - :class:`MarkerDefinition <highcharts_stock.options.defs.MarkerDefinition>`
      :class:`MarkerASTNode <highcharts_stock.options.defs.MarkerASTNode>`
      :class:`MarkerAttributeObject <highcharts_stock.options.defs.MarkerAttributeObject>`
  * - :mod:`.options.drilldown <highcharts_stock.options.drilldown>`
    - :class:`Drilldown <highcharts_stock.options.drilldown.Drilldown>`
  * - :mod:`.options.exporting <highcharts_stock.options.exporting>`
    - :class:`Exporting <highcharts_stock.options.exporting.Exporting>`
      :class:`ExportingAccessibilityOptions <highcharts_stock.options.exporting.ExportingAccessibilityOptions>`
  * - :mod:`.options.exporting.csv <highcharts_stock.options.exporting.csv>`
    - :class:`ExportingCSV <highcharts_stock.options.exporting.csv.ExportingCSV>`
      :class:`CSVAnnotationOptions <highcharts_stock.options.exporting.csv.CSVAnnotationOptions>`
  * - :mod:`.options.exporting.exporting.pdf_font <highcharts_stock.options.exporting.pdf_font>`
    - :class:`PDFFontOptions <highcharts_stock.options.exporting.pdf_font.PDFFontOptions>`
  * - :mod:`.options.legend <highcharts_stock.options.legend>`
    - :class:`Legend <highcharts_stock.options.legend.Legend>`
  * - :mod:`.options.legend.accessibility <highcharts_stock.options.legend.accessibility>`
    - :class:`LegendAccessibilityOptions <highcharts_stock.options.legend.accessibility.LegendAccessibilityOptions>`
      :class:`LegendKeyboardNavigation <highcharts_stock.options.legend.accessibility.LegendKeyboardNavigation>`
  * - :mod:`.options.legend.bubble_legend <highcharts_stock.options.legend.bubble_legend>`
    - :class:`BubbleLegend <highcharts_stock.options.legend.bubble_legend.BubbleLegend>`
      :class:`BubbleLegendRange <highcharts_stock.options.legend.bubble_legend.BubbleLegendRange>`
      :class:`BubbleLegendLabelOptions <highcharts_stock.options.legend.bubble_legend.BubbleLegendLabelOptions>`
  * - :mod:`.options.legend.navigation <highcharts_stock.options.legend.navigation>`
    - :class:`LegendNavigation <highcharts_stock.options.legend.navigation.LegendNavigation>`
  * - :mod:`.options.legend.title <highcharts_stock.options.legend.title>`
    - :class:`LegendTitle <highcharts_stock.options.legend.title.LegendTitle>`
  * - :mod:`.options.loading <highcharts_stock.options.loading>`
    - :class:`Loading <highcharts_stock.options.loading.Loading>`
  * - :mod:`.options.navigation <highcharts_stock.options.navigation>`
    - :class:`Navigation <highcharts_stock.options.navigation.Navigation>`
  * - :mod:`.options.navigation.bindings <highcharts_stock.options.navigation.bindings>`
    - :class:`Bindings <highcharts_stock.options.navigation.bindings.Bindings>`
      :class:`RectangleAnnotationBinding <highcharts_stock.options.navigation.bindings.RectangleAnnotationBinding>`
      :class:`LabelAnnotationBinding <highcharts_stock.options.navigation.bindings.LabelAnnotationBinding>`
      :class:`EllipseAnnotationBinding <highcharts_stock.options.navigation.bindings.EllipseAnnotationBinding>`
      :class:`CircleAnnotationBinding <highcharts_stock.options.navigation.bindings.CircleAnnotationBinding>`
      :class:`Binding <highcharts_stock.options.navigation.bindings.Binding>`
  * - :mod:`.options.no_data <highcharts_stock.options.no_data>`
    - :class:`NoData <highcharts_stock.options.no_data.NoData>`
  * - :mod:`.options.pane <highcharts_stock.options.pane>`
    - :class:`Pane <highcharts_stock.options.pane.Pane>`
      :class:`PaneBackground <highcharts_stock.options.pane.PaneBackground>`
  * - :mod:`.options.plot_options <highcharts_stock.options.plot_options>`
    - :class:`PlotOptions <highcharts_stock.options.plot_options.PlotOptions>`
  * - :mod:`.options.plot_options.accessibility <highcharts_stock.options.plot_options.accessibility>`
    - :class:`TypeOptionsAccessibility <highcharts_stock.options.plot_options.accessibility.TypeOptionsAccessibility>`
      :class:`SeriesKeyboardNavigation <highcharts_stock.options.plot_options.accessibility.SeriesKeyboardNavigation>`
  * - :mod:`.options.plot_options.arcdiagram <highcharts_stock.options.plot_options.arcdiagram>`
    - :class:`ArcDiagramOptions <highcharts_stock.options.plot_options.arcdiagram.ArcDiagramOptions>`
  * - :mod:`.options.plot_options.area <highcharts_stock.options.plot_options.area>`
    - :class:`AreaOptions <highcharts_stock.options.plot_options.area.AreaOptions>`
      :class:`AreaRangeOptions <highcharts_stock.options.plot_options.area.AreaRangeOptions>`
      :class:`AreaSplineOptions <highcharts_stock.options.plot_options.area.AreaSplineOptions>`
      :class:`AreaSplineRangeOptions <highcharts_stock.options.plot_options.area.AreaSplineRangeOptions>`
      :class:`LineOptions <highcharts_stock.options.plot_options.area.LineOptions>`
      :class:`StreamGraphOptions <highcharts_stock.options.plot_options.area.StreamGraphOptions>`
  * - :mod:`.options.plot_options.bar <highcharts_stock.options.plot_options.bar>`
    - :class:`BarOptions <highcharts_stock.options.plot_options.bar.BarOptions>`
      :class:`ColumnOptions <highcharts_stock.options.plot_options.bar.ColumnOptions>`
      :class:`ColumnPyramidOptions <highcharts_stock.options.plot_options.bar.ColumnPyramidOptions>`
      :class:`ColumnRangeOptions <highcharts_stock.options.plot_options.bar.ColumnRangeOptions>`
      :class:`CylinderOptions <highcharts_stock.options.plot_options.bar.CylinderOptions>`
      :class:`VariwideOptions <highcharts_stock.options.plot_options.bar.VariwideOptions>`
      :class:`WaterfallOptions <highcharts_stock.options.plot_options.bar.WaterfallOptions>`
      :class:`WindBarbOptions <highcharts_stock.options.plot_options.bar.WindBarbOptions>`
      :class:`XRangeOptions <highcharts_stock.options.plot_options.bar.XRangeOptions>`
      :class:`BaseBarOptions <highcharts_stock.options.plot_options.bar.BaseBarOptions>`
  * - :mod:`.options.plot_options.bellcurve <highcharts_stock.options.plot_options.bellcurve>`
    - :class:`BellCurveOptions <highcharts_stock.options.plot_options.bellcurve.BellCurveOptions>`
  * - :mod:`.options.plot_options.boxplot <highcharts_stock.options.plot_options.boxplot>`
    - :class:`BoxPlotOptions <highcharts_stock.options.plot_options.boxplot.BoxPlotOptions>`
      :class:`ErrorBarOptions <highcharts_stock.options.plot_options.boxplot.ErrorBarOptions>`
  * - :mod:`.options.plot_options.bubble <highcharts_stock.options.plot_options.bubble>`
    - :class:`BubbleOptions <highcharts_stock.options.plot_options.bubble.BubbleOptions>`
  * - :mod:`.options.plot_options.bullet <highcharts_stock.options.plot_options.bullet>`
    - :class:`BulletOptions <highcharts_stock.options.plot_options.bullet.BulletOptions>`
      :class:`TargetOptions <highcharts_stock.options.plot_options.bullet.TargetOptions>`
  * - :mod:`.options.plot_options.data_sorting <highcharts_stock.options.plot_options.data_sorting>`
    - :class:`DataSorting <highcharts_stock.options.plot_options.data_sorting.DataSorting>`
  * - :mod:`.options.plot_options.dependencywheel <highcharts_stock.options.plot_options.dependencywheel>`
    - :class:`DependencyWheelOptions <highcharts_stock.options.plot_options.dependencywheel.DependencyWheelOptions>`
  * - :mod:`.options.plot_options.drag_drop <highcharts_stock.options.plot_options.drag_drop>`
    - :class:`DragDropOptions <highcharts_stock.options.plot_options.drag_drop.DragDropOptions>`
      :class:`HighLowDragDropOptions <highcharts_stock.options.plot_options.drag_drop.HighLowDragDropOptions>`
      :class:`BoxPlotDragDropOptions <highcharts_stock.options.plot_options.drag_drop.BoxPlotDragDropOptions>`
      :class:`BulletDragDropOptions <highcharts_stock.options.plot_options.drag_drop.BulletDragDropOptions>`
      :class:`GuideBox <highcharts_stock.options.plot_options.drag_drop.GuideBox>`
      :class:`GuideBoxOptions <highcharts_stock.options.plot_options.drag_drop.GuideBoxOptions>`
      :class:`DragHandle <highcharts_stock.options.plot_options.drag_drop.DragHandle>`
  * - :mod:`.options.plot_options.dumbbell <highcharts_stock.options.plot_options.dumbbell>`
    - :class:`DumbbellOptions <highcharts_stock.options.plot_options.dumbbell.DumbbellOptions>`
      :class:`LollipopOptions <highcharts_stock.options.plot_options.dumbbell.LollipopOptions>`
  * - :mod:`.options.plot_options.funnel <highcharts_stock.options.plot_options.funnel>`
    - :class:`FunnelOptions <highcharts_stock.options.plot_options.funnel.FunnelOptions>`
      :class:`Funnel3DOptions <highcharts_stock.options.plot_options.funnel.Funnel3DOptions>`
  * - :mod:`.options.plot_options.gauge <highcharts_stock.options.plot_options.gauge>`
    - :class:`GaugeOptions <highcharts_stock.options.plot_options.gauge.GaugeOptions>`
      :class:`SolidGaugeOptions <highcharts_stock.options.plot_options.gauge.SolidGaugeOptions>`
  * - :mod:`.options.plot_options.generic <highcharts_stock.options.plot_options.generic>`
    - :class:`GenericTypeOptions <highcharts_stock.options.plot_options.generic.GenericTypeOptions>`
  * - :mod:`.options.plot_options.Heatmap <highcharts_stock.options.plot_options.Heatmap>`
    - :class:`HeatmapOptions <highcharts_stock.options.plot_options.Heatmap.HeatmapOptions>`
      :class:`TilemapOptions <highcharts_stock.options.plot_options.Tilemap.TilemapOptions>`
  * - :mod:`.options.plot_options.histogram <highcharts_stock.options.plot_options.histogram>`
    - :class:`HistogramOptions <highcharts_stock.options.plot_options.histogram.HistogramOptions>`
  * - :mod:`.options.plot_options.item <highcharts_stock.options.plot_options.item>`
    - :class:`ItemOptions <highcharts_stock.options.plot_options.item.ItemOptions>`
  * - :mod:`.options.plot_options.levels <highcharts_stock.options.plot_options.levels>`
    - :class:`LevelOptions <highcharts_stock.options.plot_options.levels.LevelOptions>`
      :class:`SunburstLevelOptions <highcharts_stock.options.plot_options.levels.SunburstLevelOptions>`
      :class:`TreemapLevelOptions <highcharts_stock.options.plot_options.levels.TreemapLevelOptions>`
      :class:`LevelSize <highcharts_stock.options.plot_options.levels.LevelSize>`
      :class:`ColorVariation <highcharts_stock.options.plot_options.levels.ColorVariation>`
      :class:`BaseLevelOptions <highcharts_stock.options.plot_options.levels.BaseLevelOptions>`
  * - :mod:`.options.plot_options.link <highcharts_stock.options.plot_options.link>`
    - :class:`LinkOptions <highcharts_stock.options.plot_options.link.LinkOptions>`
  * - :mod:`.options.plot_options.networkgraph <highcharts_stock.options.plot_options.networkgraph>`
    - :class:`NetworkGraphOptions <highcharts_stock.options.plot_options.networkgraph.NetworkGraphOptions>`
      :class:`LayoutAlgorithm <highcharts_stock.options.plot_options.networkgraph.LayoutAlgorithm>`
  * - :mod:`.options.plot_options.organization <highcharts_stock.options.plot_options.organization>`
    - :class:`OrganizationOptions <highcharts_stock.options.plot_options.organization.OrganizationOptions>`
  * - :mod:`.options.plot_options.packedbubble <highcharts_stock.options.plot_options.packedbubble>`
    - :class:`PackedBubbleOptions <highcharts_stock.options.plot_options.packedbubble.PackedBubbleOptions>`
      :class:`ParentNodeOptions <highcharts_stock.options.plot_options.packedbubble.ParentNodeOptions>`
  * - :mod:`.options.plot_options.pareto <highcharts_stock.options.plot_options.pareto>`
    - :class:`ParetoOptions <highcharts_stock.options.plot_options.pareto.ParetoOptions>`
  * - :mod:`.options.plot_options.pie <highcharts_stock.options.plot_options.pie>`
    - :class:`PieOptions <highcharts_stock.options.plot_options.pie.PieOptions>`
      :class:`VariablePieOptions <highcharts_stock.options.plot_options.pie.VariablePieOptions>`
  * - :mod:`.options.plot_options.points <highcharts_stock.options.plot_options.points>`
    - :class:`Point <highcharts_stock.options.plot_options.points.Point>`
      :class:`OnPointOptions <highcharts_stock.options.plot_options.points.OnPointOptions>`
      :class:`ConnectorOptions <highcharts_stock.options.plot_options.points.ConnectorOptions>`
  * - :mod:`.options.plot_options.polygon <highcharts_stock.options.plot_options.polygon>`
    - :class:`PolygonOptions <highcharts_stock.options.plot_options.polygon.PolygonOptions>`
  * - :mod:`.options.plot_options.pyramid <highcharts_stock.options.plot_options.pyramid>`
    - :class:`PyramidOptions <highcharts_stock.options.plot_options.pyramid.PyramidOptions>`
      :class:`Pyramid3DOptions <highcharts_stock.options.plot_options.pyramid.Pyramid3DOptions>`
  * - :mod:`.options.plot_options.sankey <highcharts_stock.options.plot_options.sankey>`
    - :class:`SankeyOptions <highcharts_stock.options.plot_options.sankey.SankeyOptions>`
  * - :mod:`.options.plot_options.scatter <highcharts_stock.options.plot_options.scatter>`
    - :class:`ScatterOptions <highcharts_stock.options.plot_options.scatter.ScatterOptions>`
      :class:`Scatter3DOptions <highcharts_stock.options.plot_options.scatter.Scatter3DOptions>`
  * - :mod:`.options.plot_options.series <highcharts_stock.options.plot_options.series>`
    - :class:`SeriesOptions <highcharts_stock.options.plot_options.series.SeriesOptions>`
  * - :mod:`.options.plot_options.spline <highcharts_stock.options.plot_options.spline>`
    - :class:`SplineOptions <highcharts_stock.options.plot_options.spline.SplineOptions>`
  * - :mod:`.options.plot_options.sunburst <highcharts_stock.options.plot_options.sunburst>`
    - :class:`SunburstOptions <highcharts_stock.options.plot_options.sunburst.SunburstOptions>`
  * - :mod:`.options.plot_options.timeline <highcharts_stock.options.plot_options.timeline>`
    - :class:`TimelineOptions <highcharts_stock.options.plot_options.timeline.TimelineOptions>`
  * - :mod:`.options.plot_options.treemap <highcharts_stock.options.plot_options.treemap>`
    - :class:`TreemapOptions <highcharts_stock.options.plot_options.treemap.TreemapOptions>`
  * - :mod:`.options.plot_options.vector <highcharts_stock.options.plot_options.vector>`
    - :class:`VectorOptions <highcharts_stock.options.plot_options.vector.VectorOptions>`
  * - :mod:`.options.plot_options.venn <highcharts_stock.options.plot_options.venn>`
    - :class:`VennOptions <highcharts_stock.options.plot_options.venn.VennOptions>`
  * - :mod:`.options.plot_options.wordcloud <highcharts_stock.options.plot_options.wordcloud>`
    - :class:`WordcloudOptions <highcharts_stock.options.plot_options.wordcloud.WordcloudOptions>`
      :class:`RotationOptions <highcharts_stock.options.plot_options.wordcloud.RotationOptions>`
  * - :mod:`.options.responsive <highcharts_stock.options.responsive>`
    - :class:`Responsive <highcharts_stock.options.responsive.Responsive>`
      :class:`ResponsiveRules <highcharts_stock.options.responsive.ResponsiveRules>`
      :class:`Condition <highcharts_stock.options.responsive.Condition>`
  * - :mod:`.options.series <highcharts_stock.options.series>`
    -
  * - :mod:`.options.series.arcdiagram <highcharts_stock.options.series.arcdiagram>`
    - :class:`ArcDiagramSeries <highcharts_stock.options.series.arcdiagram.ArcDiagramSeries>`
  * - :mod:`.options.series.area <highcharts_stock.options.series.area>`
    - :class:`AreaSeries <highcharts_stock.options.series.area.AreaSeries>`
      :class:`AreaRangeSeries <highcharts_stock.options.series.area.AreaRangeSeries>`
      :class:`AreaSplineSeries <highcharts_stock.options.series.area.AreaSplineSeries>`
      :class:`AreaSplineRangeSeries <highcharts_stock.options.series.area.AreaSplineRangeSeries>`
      :class:`LineSeries <highcharts_stock.options.series.area.LineSeries>`
      :class:`StreamGraphSeries <highcharts_stock.options.series.area.StreamGraphSeries>`
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
  * - :mod:`.options.series.bellcurve <highcharts_stock.options.series.bellcurve>`
    - :class:`BellCurveSeries <highcharts_stock.options.series.bellcurve.BellCurveSeries>`
  * - :mod:`.options.series.boxplot <highcharts_stock.options.series.boxplot>`
    - :class:`BoxPlotSeries <highcharts_stock.options.series.boxplot.BoxPlotSeries>`
      :class:`ErrorBarSeries <highcharts_stock.options.series.boxplot.ErrorBarSeries>`
  * - :mod:`.options.series.bubble <highcharts_stock.options.series.bubble>`
    - :class:`BubbleSeries <highcharts_stock.options.series.bubble.BubbleSeries>`
  * - :mod:`.options.series.bullet <highcharts_stock.options.series.bullet>`
    - :class:`BulletSeries <highcharts_stock.options.series.bullet.BulletSeries>`
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
  * - :mod:`.options.series.data.cartesian <highcharts_stock.options.series.data.cartesian>`
    - :class:`CartesianData <highcharts_stock.options.series.data.cartesian.CartesianData>`
      :class:`Cartesian3DData <highcharts_stock.options.series.data.cartesian.Cartesian3DData>`
      :class:`CartesianValueData <highcharts_stock.options.series.data.cartesian.CartesianValueData>`
  * - :mod:`.options.series.data.connections <highcharts_stock.options.series.data.connections>`
    - :class:`ConnectionData <highcharts_stock.options.series.data.connections.ConnectionData>`
      :class:`WeightedConnectionData <highcharts_stock.options.series.data.connections.WeightedConnectionData>`
      :class:`OutgoingWeightedConnectionData <highcharts_stock.options.series.data.connections.OutgoingWeightedConnectionData>`
      :class:`ConnectionBase <highcharts_stock.options.series.data.connections.ConnectionBase>`
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
  * - :mod:`.options.series.dumbbell <highcharts_stock.options.series.dumbbell>`
    - :class:`DumbbellSeries <highcharts_stock.options.series.dumbbell.DumbbellSeries>`
      :class:`LollipopSeries <highcharts_stock.options.series.dumbbell.LollipopSeries>`
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
  * - :mod:`.options.series.item <highcharts_stock.options.series.item>`
    - :class:`ItemSeries <highcharts_stock.options.series.item.ItemSeries>`
  * - :mod:`.options.series.labels <highcharts_stock.options.series.labels>`
    - :class:`SeriesLabel <highcharts_stock.options.series.labels.SeriesLabel>`
      :class:`Box <highcharts_stock.options.series.labels.Box>`
  * - :mod:`.options.series.networkgraph <highcharts_stock.options.series.networkgraph>`
    - :class:`NetworkGraphSeries <highcharts_stock.options.series.networkgraph.NetworkGraphSeries>`
  * - :mod:`.options.series.organization <highcharts_stock.options.series.organization>`
    - :class:`OrganizationSeries <highcharts_stock.options.series.organization.OrganizationSeries>`
  * - :mod:`.options.series.packedbubble <highcharts_stock.options.series.packedbubble>`
    - :class:`PackedBubbleSeries <highcharts_stock.options.series.packedbubble.PackedBubbleSeries>`
  * - :mod:`.options.series.pareto <highcharts_stock.options.series.pareto>`
    - :class:`ParetoSeries <highcharts_stock.options.series.pareto.ParetoSeries>`
  * - :mod:`.options.series.pie <highcharts_stock.options.series.pie>`
    - :class:`PieSeries <highcharts_stock.options.series.pie.PieSeries>`
      :class:`VariablePieSeries <highcharts_stock.options.series.pie.VariablePieSeries>`
  * - :mod:`.options.series.polygon <highcharts_stock.options.series.polygon>`
    - :class:`PolygonSeries <highcharts_stock.options.series.polygon.PolygonSeries>`
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
  * - :mod:`.options.series.treemap <highcharts_stock.options.series.treemap>`
    - :class:`TreemapSeries <highcharts_stock.options.series.treemap.TreemapSeries>`
  * - :mod:`.options.series.vector <highcharts_stock.options.series.vector>`
    - :class:`VectorSeries <highcharts_stock.options.series.vector.VectorSeries>`
  * - :mod:`.options.series.venn <highcharts_stock.options.series.venn>`
    - :class:`VennSeries <highcharts_stock.options.series.venn.VennSeries>`
  * - :mod:`.options.series.wordcloud <highcharts_stock.options.series.wordcloud>`
    - :class:`WordcloudSeries <highcharts_stock.options.series.wordcloud.WordcloudSeries>`
  * - :mod:`.options.subtitle <highcharts_stock.options.subtitle>`
    - :class:`Subtitle <highcharts_stock.options.subtitle.Subtitle>`
  * - :mod:`.options.time <highcharts_stock.options.time>`
    - :class:`Time <highcharts_stock.options.time.Time>`
  * - :mod:`.options.title <highcharts_stock.options.title>`
    - :class:`Title <highcharts_stock.options.title.Title>`
  * - :mod:`.options.tooltips <highcharts_stock.options.tooltips>`
    - :class:`Tooltip <highcharts_stock.options.tooltips.Tooltip>`

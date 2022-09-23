################################################################
:mod:`.annotations <highcharts_stock.options.annotations>`
################################################################

.. contents:: Module Contents
  :local:
  :depth: 3
  :backlinks: entry

.. toctree::
  :titlesonly:

  animation
  control_point_options
  events
  label_options
  points
  shape_options
  stock_tools/index

--------------

.. module:: highcharts_stock.options.annotations

****************************************************************************************
class: :class:`Annotation <highcharts_stock.options.annotations.Annotation>`
****************************************************************************************

.. autoclass:: Annotation
  :members:
  :inherited-members:

  .. collapse:: Class Inheritance

    .. inheritance-diagram:: Annotation
      :top-classes: highcharts_stock.metaclasses.HighchartsMeta
      :parts: -1

  |

-----------------------

***************************
Sub-components
***************************

.. list-table::
  :widths: 60 40
  :header-rows: 1

  * - Module
    - Classes / Functions
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
  * - :mod:`.options.annotations.stock_tools <highcharts_stock.options.annotations.stock_tools>`
    - :class:`CrookedLineAnnotation <highcharts_stock.options.annotations.stock_tools.CrookedLineAnnotation>`
      :class:`ElliottWaveAnnotation <highcharts_stock.options.annotations.stock_tools.ElliottWaveAnnotation>`
      :class:`FibonacciAnnotation <highcharts_stock.options.annotations.stock_tools.FibonacciAnnotation>`
      :class:`FibonacciTimeZonesAnnotation <highcharts_stock.options.annotations.stock_tools.FibonacciTimeZonesAnnotation>`
      :class:`InfinityLineAnnotation <highcharts_stock.options.annotations.stock_tools.InfinityLineAnnotation>`
      :class:`MeasureAnnotation <highcharts_stock.options.annotations.stock_tools.MeasureAnnotation>`
      :class:`PitchforkAnnotation <highcharts_stock.options.annotations.stock_tools.PitchforkAnnotation>`
      :class:`TimeCyclesAnnotation <highcharts_stock.options.annotations.stock_tools.TimeCyclesAnnotation>`
      :class:`TunnelAnnotation <highcharts_stock.options.annotations.stock_tools.TunnelAnnotation>`
      :class:`VerticalLineAnnotation <highcharts_stock.options.annotations.stock_tools.VerticalLineAnnotation>`
  * - :mod:`.options.annotations.stock_tools.crooked_line <highcharts_stock.options.annotations.stock_tools.crooked_line>`
    - :class:`CrookedLineTypeOptions <highcharts_stock.options.annotations.stock_tools.crooked_line.CrookedLineTypeOptions>`
      :class:`InfinityLineTypeOptions <highcharts_stock.options.annotations.stock_tools.crooked_line.InfinityLineTypeOptions>`
  * - :mod:`.options.annotations.stock_tools.elliot_wave <highcharts_stock.options.annotations.stock_tools.elliott_wave>`
    - :class:`ElliottWaveTypeOptions <highcharts_stock.options.annotations.stock_tools.elliott_wave.ElliottWaveTypeOptions>`
  * - :mod:`.options.annotations.stock_tools.fibonacci <highcharts_stock.options.annotations.stock_tools.fibonacci>`
    - :class:`FibonacciTypeOptions <highcharts_stock.options.annotations.stock_tools.fibonacci.FibonacciTypeOptions>`
      :class:`FibonacciTimeZonesTypeOptions <highcharts_stock.options.annotations.stock_tools.fibonacci.FibonacciTimeZonesTypeOptions>`
  * - :mod:`.options.annotations.stock_tools.measure <highcharts_stock.options.annotations.stock_tools.measure>`
    - :class:`MeasureTypeOptions <highcharts_stock.options.annotations.stock_tools.measure.MeasureTypeOptions>`
      :class:`MeasureLabelOptions <highcharts_stock.options.annotations.stock_tools.measure.MeasureLabelOptions>`
      :class:`MeasureLabelStyle <highcharts_stock.options.annotations.stock_tools.measure.MeasureLabelStyle>`
  * - :mod:`.options.annotations.stock_tools.pitchfork <highcharts_stock.options.annotations.stock_tools.pitchfork>`
    - :class:`PitchforkTypeOptions <highcharts_stock.options.annotations.stock_tools.pitchfork.PitchforkTypeOptions>`
  * - :mod:`.options.annotations.stock_tools.time_cycles <highcharts_stock.options.annotations.stock_tools.time_cycles>`
    - :class:`TimeCyclesTypeOptions <highcharts_stock.options.annotations.stock_tools.time_cycles.TimeCyclesTypeOptions>`
  * - :mod:`.options.annotations.stock_tools.tunnel <highcharts_stock.options.annotations.stock_tools.tunnel>`
    - :class:`TunnelTypeOptions <highcharts_stock.options.annotations.stock_tools.tunnel.TunnelTypeOptions>`
  * - :mod:`.options.annotations.stock_tools.vertical_line <highcharts_stock.options.annotations.stock_tools.vertical_line>`
    - :class:`VerticalLineTypeOptions <highcharts_stock.options.annotations.stock_tools.vertical_line.VerticalLineTypeOptions>`
      :class:`VerticalLineConnector <highcharts_stock.options.annotations.stock_tools.vertical_line.VerticalLineConnector>`
  * - :mod:`.options.annotations.stock_tools.type_options <highcharts_stock.options.annotations.stock_tools.type_options>`
    -
  * - :mod:`.options.annotations.stock_tools.type_options.line <highcharts_stock.options.annotations.stock_tools.type_options.line>`
    - :class:`LineFillOnly <highcharts_stock.options.annotations.stock_tools.type_options.line.LineFillOnly>`
      :class:`LineStrokeWidth <highcharts_stock.options.annotations.stock_tools.type_options.line.LineStrokeWidth>`
      :class:`LineStrokeWidthStroke <highcharts_stock.options.annotations.stock_tools.type_options.line.LineStrokeWidthStroke>`
  * - :mod:`.options.annotations.stock_tools.type_options.points <highcharts_stock.options.annotations.stock_tools.type_options.points>`
    - :class:`StockToolsPoint <highcharts_stock.options.annotations.stock_tools.type_options.points.StockToolsPoint>`
      :class:`LabeledStockToolsPoint <highcharts_stock.options.annotations.stock_tools.type_options.points.LabeledStockToolsPoint>`
      :class:`StockToolsXPoint <highcharts_stock.options.annotations.stock_tools.type_options.points.StockToolsXPoint>`

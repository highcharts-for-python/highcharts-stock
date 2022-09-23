from typing import Optional

from highcharts_stock.decorators import class_sensitive
from highcharts_stock.metaclasses import HighchartsMeta
from highcharts_stock.options.annotations.shape_options import ShapeOptions
from highcharts_stock.options.annotations.label_options import LabelOptions
from highcharts_stock.options.annotations.control_point_options import AnnotationControlPointOption
from highcharts_stock.options.annotations.stock_tools.type_options.crooked_line import CrookedLineTypeOptions
from highcharts_stock.options.annotations.stock_tools.type_options.elliott_wave import ElliottWaveTypeOptions
from highcharts_stock.options.annotations.stock_tools.type_options.fibonacci import FibonacciTypeOptions
from highcharts_stock.options.annotations.stock_tools.type_options.fibonacci import FibonacciTimeZonesTypeOptions
from highcharts_stock.options.annotations.stock_tools.type_options.crooked_line import InfinityLineTypeOptions
from highcharts_stock.options.annotations.stock_tools.type_options.measure import MeasureTypeOptions
from highcharts_stock.options.annotations.stock_tools.type_options.pitchfork import PitchforkTypeOptions
from highcharts_stock.options.annotations.stock_tools.type_options.time_cycles import TimeCyclesTypeOptions
from highcharts_stock.options.annotations.stock_tools.type_options.tunnel import TunnelTypeOptions
from highcharts_stock.options.annotations.stock_tools.type_options.vertical_line import VerticalLineTypeOptions


class CrookedLineAnnotation(HighchartsMeta):
    """Annotation options for a :term:`crooked line` analysis."""

    def __init__(self, **kwargs):
        self._control_point_options = None
        self._label_options = None
        self._shape_options = None
        self._type_options = None

        self.control_point_options = kwargs.get('control_point_options', None)
        self.label_options = kwargs.get('label_options', None)
        self.shape_options = kwargs.get('shape_options', None)
        self.type_options = kwargs.get('type_options', None)

    @property
    def control_point_options(self) -> Optional[AnnotationControlPointOption]:
        """Additional options for an annotation of the given control point.

        :rtype: :class:`AnnotationControlPointOption <highcharts_stock.options.annotations.control_point_options.AnnotationControlPointOption>`
          or :obj:`None <python:None>`
        """
        return self._control_point_options

    @control_point_options.setter
    @class_sensitive(AnnotationControlPointOption)
    def control_point_options(self, value):
        self._control_point_options = value

    @property
    def label_options(self) -> Optional[LabelOptions]:
        """Additional options for an annotation of the given label.

        :rtype: :class:`LabelOptions <highcharts_stock.options.annotations.label_options.LabelOptions>`
          or :obj:`None <python:None>`
        """
        return self._label_options

    @label_options.setter
    @class_sensitive(LabelOptions)
    def label_options(self, value):
        self._label_options = value

    @property
    def shape_options(self) -> Optional[ShapeOptions]:
        """Additional options for an annotation of the given shape.

        :rtype: :class:`ShapeOptions <highcharts_stock.options.annotations.shape_options.ShapeOptions>`
          or :obj:`None <python:None>`
        """
        return self._shape_options

    @shape_options.setter
    @class_sensitive(ShapeOptions)
    def shape_options(self, value):
        self._shape_options = value

    @property
    def type_options(self) -> Optional[CrookedLineTypeOptions]:
        """Additional options for an annotation of the given type.

        :rtype: :class:`CrookedLineTypeOptions` or :obj:`None <python:None>`
        """
        return self._type_options

    @type_options.setter
    @class_sensitive(CrookedLineTypeOptions)
    def type_options(self, value):
        self._type_options = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'control_point_options': as_dict.get('controlPointOptions', None),
            'label_options': as_dict.get('labelOptions', None),
            'shape_options': as_dict.get('shapeOptions', None),
            'type_options': as_dict.get('typeOptions', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'controlPointOptions': self.control_point_options,
            'labelOptions': self.label_options,
            'shapeOptions': self.shape_options,
            'typeOptions': self.type_options
        }

        return untrimmed


class ElliottWaveAnnotation(HighchartsMeta):
    """Annotation options for an :term:`elliott wave` analysis."""

    def __init__(self, **kwargs):
        self._control_point_options = None
        self._label_options = None
        self._shape_options = None
        self._type_options = None

        self.control_point_options = kwargs.get('control_point_options', None)
        self.label_options = kwargs.get('label_options', None)
        self.shape_options = kwargs.get('shape_options', None)
        self.type_options = kwargs.get('type_options', None)

    @property
    def control_point_options(self) -> Optional[AnnotationControlPointOption]:
        """Additional options for an annotation of the given control point.

        :rtype: :class:`AnnotationControlPointOption <highcharts_stock.options.annotations.control_point_options.AnnotationControlPointOption>`
          or :obj:`None <python:None>`
        """
        return self._control_point_options

    @control_point_options.setter
    @class_sensitive(AnnotationControlPointOption)
    def control_point_options(self, value):
        self._control_point_options = value

    @property
    def label_options(self) -> Optional[LabelOptions]:
        """Additional options for an annotation of the given label.

        :rtype: :class:`LabelOptions <highcharts_stock.options.annotations.label_options.LabelOptions>`
          or :obj:`None <python:None>`
        """
        return self._label_options

    @label_options.setter
    @class_sensitive(LabelOptions)
    def label_options(self, value):
        self._label_options = value

    @property
    def shape_options(self) -> Optional[ShapeOptions]:
        """Additional options for an annotation of the given shape.

        :rtype: :class:`ShapeOptions <highcharts_stock.options.annotations.shape_options.ShapeOptions>`
          or :obj:`None <python:None>`
        """
        return self._shape_options

    @shape_options.setter
    @class_sensitive(ShapeOptions)
    def shape_options(self, value):
        self._shape_options = value

    @property
    def type_options(self) -> Optional[ElliottWaveTypeOptions]:
        """Additional options for an annotation of the given type.

        :rtype: :class:`ElliottWaveTypeOptions` or :obj:`None <python:None>`
        """
        return self._type_options

    @type_options.setter
    @class_sensitive(ElliottWaveTypeOptions)
    def type_options(self, value):
        self._type_options = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'control_point_options': as_dict.get('controlPointOptions', None),
            'label_options': as_dict.get('labelOptions', None),
            'shape_options': as_dict.get('shapeOptions', None),
            'type_options': as_dict.get('typeOptions', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'controlPointOptions': self.control_point_options,
            'labelOptions': self.label_options,
            'shapeOptions': self.shape_options,
            'typeOptions': self.type_options
        }

        return untrimmed


class FibonacciAnnotation(HighchartsMeta):
    """Annotation options for a :term:`fibonacci` analysis."""

    def __init__(self, **kwargs):
        self._control_point_options = None
        self._label_options = None
        self._shape_options = None
        self._type_options = None

        self.control_point_options = kwargs.get('control_point_options', None)
        self.label_options = kwargs.get('label_options', None)
        self.shape_options = kwargs.get('shape_options', None)
        self.type_options = kwargs.get('type_options', None)

    @property
    def control_point_options(self) -> Optional[AnnotationControlPointOption]:
        """Additional options for an annotation of the given control point.

        :rtype: :class:`AnnotationControlPointOption <highcharts_stock.options.annotations.control_point_options.AnnotationControlPointOption>`
          or :obj:`None <python:None>`
        """
        return self._control_point_options

    @control_point_options.setter
    @class_sensitive(AnnotationControlPointOption)
    def control_point_options(self, value):
        self._control_point_options = value

    @property
    def label_options(self) -> Optional[LabelOptions]:
        """Additional options for an annotation of the given label.

        :rtype: :class:`LabelOptions <highcharts_stock.options.annotations.label_options.LabelOptions>`
          or :obj:`None <python:None>`
        """
        return self._label_options

    @label_options.setter
    @class_sensitive(LabelOptions)
    def label_options(self, value):
        self._label_options = value

    @property
    def shape_options(self) -> Optional[ShapeOptions]:
        """Additional options for an annotation of the given shape.

        :rtype: :class:`ShapeOptions <highcharts_stock.options.annotations.shape_options.ShapeOptions>`
          or :obj:`None <python:None>`
        """
        return self._shape_options

    @shape_options.setter
    @class_sensitive(ShapeOptions)
    def shape_options(self, value):
        self._shape_options = value

    @property
    def type_options(self) -> Optional[FibonacciTypeOptions]:
        """Additional options for an annotation of the given type.

        :rtype: :class:`FibonacciTypeOptions` or :obj:`None <python:None>`
        """
        return self._type_options

    @type_options.setter
    @class_sensitive(FibonacciTypeOptions)
    def type_options(self, value):
        self._type_options = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'control_point_options': as_dict.get('controlPointOptions', None),
            'label_options': as_dict.get('labelOptions', None),
            'shape_options': as_dict.get('shapeOptions', None),
            'type_options': as_dict.get('typeOptions', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'controlPointOptions': self.control_point_options,
            'labelOptions': self.label_options,
            'shapeOptions': self.shape_options,
            'typeOptions': self.type_options
        }

        return untrimmed


class FibonacciTimeZonesAnnotation(HighchartsMeta):
    """Annotation options for a :term:`fibonacci time zones` analysis."""

    def __init__(self, **kwargs):
        self._control_point_options = None
        self._label_options = None
        self._shape_options = None
        self._type_options = None

        self.control_point_options = kwargs.get('control_point_options', None)
        self.label_options = kwargs.get('label_options', None)
        self.shape_options = kwargs.get('shape_options', None)
        self.type_options = kwargs.get('type_options', None)

    @property
    def control_point_options(self) -> Optional[AnnotationControlPointOption]:
        """Additional options for an annotation of the given control point.

        :rtype: :class:`AnnotationControlPointOption <highcharts_stock.options.annotations.control_point_options.AnnotationControlPointOption>`
          or :obj:`None <python:None>`
        """
        return self._control_point_options

    @control_point_options.setter
    @class_sensitive(AnnotationControlPointOption)
    def control_point_options(self, value):
        self._control_point_options = value

    @property
    def label_options(self) -> Optional[LabelOptions]:
        """Additional options for an annotation of the given label.

        :rtype: :class:`LabelOptions <highcharts_stock.options.annotations.label_options.LabelOptions>`
          or :obj:`None <python:None>`
        """
        return self._label_options

    @label_options.setter
    @class_sensitive(LabelOptions)
    def label_options(self, value):
        self._label_options = value

    @property
    def shape_options(self) -> Optional[ShapeOptions]:
        """Additional options for an annotation of the given shape.

        :rtype: :class:`ShapeOptions <highcharts_stock.options.annotations.shape_options.ShapeOptions>`
          or :obj:`None <python:None>`
        """
        return self._shape_options

    @shape_options.setter
    @class_sensitive(ShapeOptions)
    def shape_options(self, value):
        self._shape_options = value

    @property
    def type_options(self) -> Optional[FibonacciTimeZonesTypeOptions]:
        """Additional options for an annotation of the given type.

        :rtype: :class:`FibonacciTimeZonesTypeOptions` or :obj:`None <python:None>`
        """
        return self._type_options

    @type_options.setter
    @class_sensitive(FibonacciTimeZonesTypeOptions)
    def type_options(self, value):
        self._type_options = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'control_point_options': as_dict.get('controlPointOptions', None),
            'label_options': as_dict.get('labelOptions', None),
            'shape_options': as_dict.get('shapeOptions', None),
            'type_options': as_dict.get('typeOptions', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'controlPointOptions': self.control_point_options,
            'labelOptions': self.label_options,
            'shapeOptions': self.shape_options,
            'typeOptions': self.type_options
        }

        return untrimmed


class InfinityLineAnnotation(HighchartsMeta):
    """Annotation options for an :term:`infinity line` analysis."""

    def __init__(self, **kwargs):
        self._control_point_options = None
        self._label_options = None
        self._shape_options = None
        self._type_options = None

        self.control_point_options = kwargs.get('control_point_options', None)
        self.label_options = kwargs.get('label_options', None)
        self.shape_options = kwargs.get('shape_options', None)
        self.type_options = kwargs.get('type_options', None)

    @property
    def control_point_options(self) -> Optional[AnnotationControlPointOption]:
        """Additional options for an annotation of the given control point.

        :rtype: :class:`AnnotationControlPointOption <highcharts_stock.options.annotations.control_point_options.AnnotationControlPointOption>`
          or :obj:`None <python:None>`
        """
        return self._control_point_options

    @control_point_options.setter
    @class_sensitive(AnnotationControlPointOption)
    def control_point_options(self, value):
        self._control_point_options = value

    @property
    def label_options(self) -> Optional[LabelOptions]:
        """Additional options for an annotation of the given label.

        :rtype: :class:`LabelOptions <highcharts_stock.options.annotations.label_options.LabelOptions>`
          or :obj:`None <python:None>`
        """
        return self._label_options

    @label_options.setter
    @class_sensitive(LabelOptions)
    def label_options(self, value):
        self._label_options = value

    @property
    def shape_options(self) -> Optional[ShapeOptions]:
        """Additional options for an annotation of the given shape.

        :rtype: :class:`ShapeOptions <highcharts_stock.options.annotations.shape_options.ShapeOptions>`
          or :obj:`None <python:None>`
        """
        return self._shape_options

    @shape_options.setter
    @class_sensitive(ShapeOptions)
    def shape_options(self, value):
        self._shape_options = value

    @property
    def type_options(self) -> Optional[InfinityLineTypeOptions]:
        """Additional options for an annotation of the given type.

        :rtype: :class:`InfinityLineTypeOptions` or :obj:`None <python:None>`
        """
        return self._type_options

    @type_options.setter
    @class_sensitive(InfinityLineTypeOptions)
    def type_options(self, value):
        self._type_options = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'control_point_options': as_dict.get('controlPointOptions', None),
            'label_options': as_dict.get('labelOptions', None),
            'shape_options': as_dict.get('shapeOptions', None),
            'type_options': as_dict.get('typeOptions', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'controlPointOptions': self.control_point_options,
            'labelOptions': self.label_options,
            'shapeOptions': self.shape_options,
            'typeOptions': self.type_options
        }

        return untrimmed


class MeasureAnnotation(HighchartsMeta):
    """Annotation options for a :term:`measure` analysis."""

    def __init__(self, **kwargs):
        self._control_point_options = None
        self._label_options = None
        self._shape_options = None
        self._type_options = None

        self.control_point_options = kwargs.get('control_point_options', None)
        self.label_options = kwargs.get('label_options', None)
        self.shape_options = kwargs.get('shape_options', None)
        self.type_options = kwargs.get('type_options', None)

    @property
    def control_point_options(self) -> Optional[AnnotationControlPointOption]:
        """Additional options for an annotation of the given control point.

        :rtype: :class:`AnnotationControlPointOption <highcharts_stock.options.annotations.control_point_options.AnnotationControlPointOption>`
          or :obj:`None <python:None>`
        """
        return self._control_point_options

    @control_point_options.setter
    @class_sensitive(AnnotationControlPointOption)
    def control_point_options(self, value):
        self._control_point_options = value

    @property
    def label_options(self) -> Optional[LabelOptions]:
        """Additional options for an annotation of the given label.

        :rtype: :class:`LabelOptions <highcharts_stock.options.annotations.label_options.LabelOptions>`
          or :obj:`None <python:None>`
        """
        return self._label_options

    @label_options.setter
    @class_sensitive(LabelOptions)
    def label_options(self, value):
        self._label_options = value

    @property
    def shape_options(self) -> Optional[ShapeOptions]:
        """Additional options for an annotation of the given shape.

        :rtype: :class:`ShapeOptions <highcharts_stock.options.annotations.shape_options.ShapeOptions>`
          or :obj:`None <python:None>`
        """
        return self._shape_options

    @shape_options.setter
    @class_sensitive(ShapeOptions)
    def shape_options(self, value):
        self._shape_options = value

    @property
    def type_options(self) -> Optional[MeasureTypeOptions]:
        """Additional options for an annotation of the given type.

        :rtype: :class:`MeasureTypeOptions` or :obj:`None <python:None>`
        """
        return self._type_options

    @type_options.setter
    @class_sensitive(MeasureTypeOptions)
    def type_options(self, value):
        self._type_options = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'control_point_options': as_dict.get('controlPointOptions', None),
            'label_options': as_dict.get('labelOptions', None),
            'shape_options': as_dict.get('shapeOptions', None),
            'type_options': as_dict.get('typeOptions', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'controlPointOptions': self.control_point_options,
            'labelOptions': self.label_options,
            'shapeOptions': self.shape_options,
            'typeOptions': self.type_options
        }

        return untrimmed


class PitchforkAnnotation(HighchartsMeta):
    """Annotation options for a :term:`pitchfork` analysis."""

    def __init__(self, **kwargs):
        self._control_point_options = None
        self._label_options = None
        self._shape_options = None
        self._type_options = None

        self.control_point_options = kwargs.get('control_point_options', None)
        self.label_options = kwargs.get('label_options', None)
        self.shape_options = kwargs.get('shape_options', None)
        self.type_options = kwargs.get('type_options', None)

    @property
    def control_point_options(self) -> Optional[AnnotationControlPointOption]:
        """Additional options for an annotation of the given control point.

        :rtype: :class:`AnnotationControlPointOption <highcharts_stock.options.annotations.control_point_options.AnnotationControlPointOption>`
          or :obj:`None <python:None>`
        """
        return self._control_point_options

    @control_point_options.setter
    @class_sensitive(AnnotationControlPointOption)
    def control_point_options(self, value):
        self._control_point_options = value

    @property
    def label_options(self) -> Optional[LabelOptions]:
        """Additional options for an annotation of the given label.

        :rtype: :class:`LabelOptions <highcharts_stock.options.annotations.label_options.LabelOptions>`
          or :obj:`None <python:None>`
        """
        return self._label_options

    @label_options.setter
    @class_sensitive(LabelOptions)
    def label_options(self, value):
        self._label_options = value

    @property
    def shape_options(self) -> Optional[ShapeOptions]:
        """Additional options for an annotation of the given shape.

        :rtype: :class:`ShapeOptions <highcharts_stock.options.annotations.shape_options.ShapeOptions>`
          or :obj:`None <python:None>`
        """
        return self._shape_options

    @shape_options.setter
    @class_sensitive(ShapeOptions)
    def shape_options(self, value):
        self._shape_options = value

    @property
    def type_options(self) -> Optional[PitchforkTypeOptions]:
        """Additional options for an annotation of the given type.

        :rtype: :class:`PitchforkTypeOptions` or :obj:`None <python:None>`
        """
        return self._type_options

    @type_options.setter
    @class_sensitive(PitchforkTypeOptions)
    def type_options(self, value):
        self._type_options = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'control_point_options': as_dict.get('controlPointOptions', None),
            'label_options': as_dict.get('labelOptions', None),
            'shape_options': as_dict.get('shapeOptions', None),
            'type_options': as_dict.get('typeOptions', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'controlPointOptions': self.control_point_options,
            'labelOptions': self.label_options,
            'shapeOptions': self.shape_options,
            'typeOptions': self.type_options
        }

        return untrimmed


class TimeCyclesAnnotation(HighchartsMeta):
    """Annotation options for a :term:`time cycles` analysis."""

    def __init__(self, **kwargs):
        self._control_point_options = None
        self._label_options = None
        self._shape_options = None
        self._type_options = None

        self.control_point_options = kwargs.get('control_point_options', None)
        self.label_options = kwargs.get('label_options', None)
        self.shape_options = kwargs.get('shape_options', None)
        self.type_options = kwargs.get('type_options', None)

    @property
    def control_point_options(self) -> Optional[AnnotationControlPointOption]:
        """Additional options for an annotation of the given control point.

        :rtype: :class:`AnnotationControlPointOption <highcharts_stock.options.annotations.control_point_options.AnnotationControlPointOption>`
          or :obj:`None <python:None>`
        """
        return self._control_point_options

    @control_point_options.setter
    @class_sensitive(AnnotationControlPointOption)
    def control_point_options(self, value):
        self._control_point_options = value

    @property
    def label_options(self) -> Optional[LabelOptions]:
        """Additional options for an annotation of the given label.

        :rtype: :class:`LabelOptions <highcharts_stock.options.annotations.label_options.LabelOptions>`
          or :obj:`None <python:None>`
        """
        return self._label_options

    @label_options.setter
    @class_sensitive(LabelOptions)
    def label_options(self, value):
        self._label_options = value

    @property
    def shape_options(self) -> Optional[ShapeOptions]:
        """Additional options for an annotation of the given shape.

        :rtype: :class:`ShapeOptions <highcharts_stock.options.annotations.shape_options.ShapeOptions>`
          or :obj:`None <python:None>`
        """
        return self._shape_options

    @shape_options.setter
    @class_sensitive(ShapeOptions)
    def shape_options(self, value):
        self._shape_options = value

    @property
    def type_options(self) -> Optional[TimeCyclesTypeOptions]:
        """Additional options for an annotation of the given type.

        :rtype: :class:`TimeCyclesTypeOptions` or :obj:`None <python:None>`
        """
        return self._type_options

    @type_options.setter
    @class_sensitive(TimeCyclesTypeOptions)
    def type_options(self, value):
        self._type_options = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'control_point_options': as_dict.get('controlPointOptions', None),
            'label_options': as_dict.get('labelOptions', None),
            'shape_options': as_dict.get('shapeOptions', None),
            'type_options': as_dict.get('typeOptions', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'controlPointOptions': self.control_point_options,
            'labelOptions': self.label_options,
            'shapeOptions': self.shape_options,
            'typeOptions': self.type_options
        }

        return untrimmed


class TunnelAnnotation(HighchartsMeta):
    """Annotation options for a :term:`tunnel` analysis."""

    def __init__(self, **kwargs):
        self._control_point_options = None
        self._label_options = None
        self._shape_options = None
        self._type_options = None

        self.control_point_options = kwargs.get('control_point_options', None)
        self.label_options = kwargs.get('label_options', None)
        self.shape_options = kwargs.get('shape_options', None)
        self.type_options = kwargs.get('type_options', None)

    @property
    def control_point_options(self) -> Optional[AnnotationControlPointOption]:
        """Additional options for an annotation of the given control point.

        :rtype: :class:`AnnotationControlPointOption <highcharts_stock.options.annotations.control_point_options.AnnotationControlPointOption>`
          or :obj:`None <python:None>`
        """
        return self._control_point_options

    @control_point_options.setter
    @class_sensitive(AnnotationControlPointOption)
    def control_point_options(self, value):
        self._control_point_options = value

    @property
    def label_options(self) -> Optional[LabelOptions]:
        """Additional options for an annotation of the given label.

        :rtype: :class:`LabelOptions <highcharts_stock.options.annotations.label_options.LabelOptions>`
          or :obj:`None <python:None>`
        """
        return self._label_options

    @label_options.setter
    @class_sensitive(LabelOptions)
    def label_options(self, value):
        self._label_options = value

    @property
    def shape_options(self) -> Optional[ShapeOptions]:
        """Additional options for an annotation of the given shape.

        :rtype: :class:`ShapeOptions <highcharts_stock.options.annotations.shape_options.ShapeOptions>`
          or :obj:`None <python:None>`
        """
        return self._shape_options

    @shape_options.setter
    @class_sensitive(ShapeOptions)
    def shape_options(self, value):
        self._shape_options = value

    @property
    def type_options(self) -> Optional[TunnelTypeOptions]:
        """Additional options for an annotation of the given type.

        :rtype: :class:`TunnelTypeOptions` or :obj:`None <python:None>`
        """
        return self._type_options

    @type_options.setter
    @class_sensitive(TunnelTypeOptions)
    def type_options(self, value):
        self._type_options = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'control_point_options': as_dict.get('controlPointOptions', None),
            'label_options': as_dict.get('labelOptions', None),
            'shape_options': as_dict.get('shapeOptions', None),
            'type_options': as_dict.get('typeOptions', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'controlPointOptions': self.control_point_options,
            'labelOptions': self.label_options,
            'shapeOptions': self.shape_options,
            'typeOptions': self.type_options
        }

        return untrimmed


class VerticalLineAnnotation(HighchartsMeta):
    """Annotation options for a :term:`vertical line` analysis."""

    def __init__(self, **kwargs):
        self._control_point_options = None
        self._label_options = None
        self._shape_options = None
        self._type_options = None

        self.control_point_options = kwargs.get('control_point_options', None)
        self.label_options = kwargs.get('label_options', None)
        self.shape_options = kwargs.get('shape_options', None)
        self.type_options = kwargs.get('type_options', None)

    @property
    def control_point_options(self) -> Optional[AnnotationControlPointOption]:
        """Additional options for an annotation of the given control point.

        :rtype: :class:`AnnotationControlPointOption <highcharts_stock.options.annotations.control_point_options.AnnotationControlPointOption>`
          or :obj:`None <python:None>`
        """
        return self._control_point_options

    @control_point_options.setter
    @class_sensitive(AnnotationControlPointOption)
    def control_point_options(self, value):
        self._control_point_options = value

    @property
    def label_options(self) -> Optional[LabelOptions]:
        """Additional options for an annotation of the given label.

        :rtype: :class:`LabelOptions <highcharts_stock.options.annotations.label_options.LabelOptions>`
          or :obj:`None <python:None>`
        """
        return self._label_options

    @label_options.setter
    @class_sensitive(LabelOptions)
    def label_options(self, value):
        self._label_options = value

    @property
    def shape_options(self) -> Optional[ShapeOptions]:
        """Additional options for an annotation of the given shape.

        :rtype: :class:`ShapeOptions <highcharts_stock.options.annotations.shape_options.ShapeOptions>`
          or :obj:`None <python:None>`
        """
        return self._shape_options

    @shape_options.setter
    @class_sensitive(ShapeOptions)
    def shape_options(self, value):
        self._shape_options = value

    @property
    def type_options(self) -> Optional[VerticalLineTypeOptions]:
        """Additional options for an annotation of the given type.

        :rtype: :class:`VerticalLineTypeOptions` or :obj:`None <python:None>`
        """
        return self._type_options

    @type_options.setter
    @class_sensitive(VerticalLineTypeOptions)
    def type_options(self, value):
        self._type_options = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'control_point_options': as_dict.get('controlPointOptions', None),
            'label_options': as_dict.get('labelOptions', None),
            'shape_options': as_dict.get('shapeOptions', None),
            'type_options': as_dict.get('typeOptions', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'controlPointOptions': self.control_point_options,
            'labelOptions': self.label_options,
            'shapeOptions': self.shape_options,
            'typeOptions': self.type_options
        }

        return untrimmed

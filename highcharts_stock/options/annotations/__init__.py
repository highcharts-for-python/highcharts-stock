from typing import Optional


from highcharts_core.options.annotations import Annotation as AnnotationBase

from highcharts_stock.decorators import class_sensitive
from highcharts_stock.options.annotations.stock_tools import CrookedLineAnnotation
from highcharts_stock.options.annotations.stock_tools import ElliottWaveAnnotation
from highcharts_stock.options.annotations.stock_tools import FibonacciAnnotation
from highcharts_stock.options.annotations.stock_tools import FibonacciTimeZonesAnnotation
from highcharts_stock.options.annotations.stock_tools import InfinityLineAnnotation
from highcharts_stock.options.annotations.stock_tools import MeasureAnnotation
from highcharts_stock.options.annotations.stock_tools import PitchforkAnnotation
from highcharts_stock.options.annotations.stock_tools import TimeCyclesAnnotation
from highcharts_stock.options.annotations.stock_tools import TunnelAnnotation
from highcharts_stock.options.annotations.stock_tools import VerticalLineAnnotation


class NavigationAnnotationOptions(AnnotationBase):
    """Annotation that can be configured for the
    :class:`Navigation <highcharts_stock.options.navigation.Navigation>`
    """

    def __init__(self, **kwargs):
        self._fibonacci_time_zones = None
        self._time_cycles = None

        self.fibonacci_time_zones = kwargs.get('fibonacci_time_zones', None)
        self.time_cycles = kwargs.get('time_cycles', None)

        super().__init__(**kwargs)

    @property
    def _dot_path(self) -> Optional[str]:
        """The dot-notation path to the options key for the current class.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return 'navigation.annotationOptions'

    @property
    def fibonnaci_time_zones(self) -> Optional[FibonacciTimeZonesAnnotation]:
        """A :term:`Fibonacci Time Zones` annotation.

        :rtype: :class:`FibonacciTimeZonesAnnotation` or :obj:`None <python:None>`
        """
        return self._fibonnaci_time_zones

    @fibonnaci_time_zones.setter
    @class_sensitive(FibonacciTimeZonesAnnotation)
    def fibonnaci_time_zones(self, value):
        self._fibonnaci_time_zones = value

    @property
    def time_cycles(self) -> Optional[TimeCyclesAnnotation]:
        """A :term:`TimeCycles` annotation.

        :rtype: :class:`TimeCyclesAnnotation` or :obj:`None <python:None>`
        """
        return self._time_cycles

    @time_cycles.setter
    @class_sensitive(TimeCyclesAnnotation)
    def time_cycles(self, value):
        self._time_cycles = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'animation': as_dict.get('animation', None),
            'control_point_options': as_dict.get('controlPointOptions', None),
            'crop': as_dict.get('crop', None),
            'draggable': as_dict.get('draggable', None),
            'events': as_dict.get('events', None),
            'id': as_dict.get('id', None),
            'label_options': as_dict.get('labelOptions', None),
            'labels': as_dict.get('labels', None),
            'shape_options': as_dict.get('shapeOptions', None),
            'shapes': as_dict.get('shapes', None),
            'visible': as_dict.get('visible', None),
            'z_index': as_dict.get('zIndex', None),

            'fibonacci_time_zones': as_dict.get('fibonacciTimeZones', None),
            'time_cycles': as_dict.get('timeCycles', None),
        }
        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'fibonacciTimeZones': self.fibonacci_time_zones,
            'timeCycles': self.time_cycles,
        }

        parent_as_dict = super()._to_untrimmed_dict(in_cls = in_cls)

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed


class Annotation(NavigationAnnotationOptions):
    """A basic type of an annotation. It allows adding custom labels or shapes. The
    items can be tied to points, axis coordinates or chart pixel coordinates."""

    def __init__(self, **kwargs):
        self._crooked_line = None
        self._elliott_wave = None
        self._fibonacci = None
        self._infinity_line = None
        self._measure = None
        self._pitchfork = None
        self._tunnel = None
        self._vertical_line = None

        self.crooked_line = kwargs.get('crooked_line', None)
        self.elliott_wave = kwargs.get('elliott_wave', None)
        self.fibonacci = kwargs.get('fibonacci', None)
        self.infinity_line = kwargs.get('infinity_line', None)
        self.measure = kwargs.get('measure', None)
        self.pitchfork = kwargs.get('pitchfork', None)
        self.tunnel = kwargs.get('tunnel', None)
        self.vertical_line = kwargs.get('vertical_line', None)

        super().__init__(**kwargs)

    @property
    def _dot_path(self) -> Optional[str]:
        """The dot-notation path to the options key for the current class.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return 'annotations'

    @property
    def crooked_line(self) -> Optional[CrookedLineAnnotation]:
        """A :term:`crooked line` annotation.

        :rtype: :class:`CrookedLineAnnotation` or :obj:`None <python:None>`
        """
        return self._crooked_line

    @crooked_line.setter
    @class_sensitive(CrookedLineAnnotation)
    def crooked_line(self, value):
        self._crooked_line = value

    @property
    def elliott_wave(self) -> Optional[ElliottWaveAnnotation]:
        """An :term:`elliott wave` annotation.

        :rtype: :class:`ElliottWaveAnnotation` or :obj:`None <python:None>`
        """
        return self._elliott_wave

    @elliott_wave.setter
    @class_sensitive(ElliottWaveAnnotation)
    def elliott_wave(self, value):
        self._elliott_wave = value

    @property
    def fibonacci(self) -> Optional[FibonacciAnnotation]:
        """A :term:`Fibonacci` annotation.

        :rtype: :class:`FibonacciAnnotation` or :obj:`None <python:None>`
        """
        return self._fibonacci

    @fibonacci.setter
    @class_sensitive(FibonacciAnnotation)
    def fibonacci(self, value):
        self._fibonacci = value

    @property
    def infinity_line(self) -> Optional[InfinityLineAnnotation]:
        """A :term:`infinity line` annotation.

        :rtype: :class:`InfinityLineAnnotation` or :obj:`None <python:None>`
        """
        return self._infinity_line

    @infinity_line.setter
    @class_sensitive(InfinityLineAnnotation)
    def infinity_line(self, value):
        self._infinity_line = value

    @property
    def measure(self) -> Optional[MeasureAnnotation]:
        """A measure annotation.

        :rtype: :class:`MeasureAnnotation` or :obj:`None <python:None>`
        """
        return self._measure

    @measure.setter
    @class_sensitive(MeasureAnnotation)
    def measure(self, value):
        self._measure = value

    @property
    def pitchfork(self) -> Optional[PitchforkAnnotation]:
        """A :term:`pitchfork` annotation.

        :rtype: :class:`PitchforkAnnotation` or :obj:`None <python:None>`
        """
        return self._pitchfork

    @pitchfork.setter
    @class_sensitive(PitchforkAnnotation)
    def pitchfork(self, value):
        self._pitchfork = value

    @property
    def tunnel(self) -> Optional[TunnelAnnotation]:
        """A :term:`tunnel` annotation.

        :rtype: :class:`TunnelAnnotation` or :obj:`None <python:None>`
        """
        return self._tunnel

    @tunnel.setter
    @class_sensitive(TunnelAnnotation)
    def tunnel(self, value):
        self._tunnel = value

    @property
    def vertical_line(self) -> Optional[VerticalLineAnnotation]:
        """A :term:`vertical line` annotation.

        :rtype: :class:`VerticalLineAnnotation` or :obj:`None <python:None>`
        """
        return self._vertical_line

    @vertical_line.setter
    @class_sensitive(VerticalLineAnnotation)
    def vertical_line(self, value):
        self._vertical_line = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'animation': as_dict.get('animation', None),
            'control_point_options': as_dict.get('controlPointOptions', None),
            'crop': as_dict.get('crop', None),
            'draggable': as_dict.get('draggable', None),
            'events': as_dict.get('events', None),
            'id': as_dict.get('id', None),
            'label_options': as_dict.get('labelOptions', None),
            'labels': as_dict.get('labels', None),
            'shape_options': as_dict.get('shapeOptions', None),
            'shapes': as_dict.get('shapes', None),
            'visible': as_dict.get('visible', None),
            'z_index': as_dict.get('zIndex', None),

            'fibonacci_time_zones': as_dict.get('fibonacciTimeZones', None),
            'time_cycles': as_dict.get('timeCycles', None),

            'crooked_line': as_dict.get('crookedLine', None),
            'elliott_wave': as_dict.get('elliottWave', None),
            'fibonacci': as_dict.get('fibonacci', None),
            'infinity_line': as_dict.get('infinityLine', None),
            'measure': as_dict.get('measure', None),
            'pitchfork': as_dict.get('pitchfork', None),
            'tunnel': as_dict.get('tunnel', None),
            'vertical_line': as_dict.get('verticalLine', None),
        }
        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'crookedLine': self.crooked_line,
            'elliottWave': self.elliott_wave,
            'fibonacci': self.fibonacci,
            'infinityLine': self.infinity_line,
            'measure': self.measure,
            'pitchfork': self.pitchfork,
            'tunnel': self.tunnel,
            'verticalLine': self.vertical_line,
        }

        parent_as_dict = super()._to_untrimmed_dict(in_cls = in_cls)

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed

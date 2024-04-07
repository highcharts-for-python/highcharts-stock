from typing import Optional, List

from validator_collection import validators

from highcharts_stock.decorators import class_sensitive
from highcharts_stock.metaclasses import HighchartsMeta


class Definition(HighchartsMeta):
    """Definition of a symbol for a single Stock Tools button."""

    def __init__(self, **kwargs):
        self._class_name = None
        self._element_type = None
        self._symbol = None

        self.class_name = kwargs.get('class_name', None)
        self.element_type = kwargs.get('element_type', None)
        self.symbol = kwargs.get('symbol', None)

    @property
    def class_name(self) -> Optional[str]:
        """The name of the class to apply to the button. Defaults to
        ``'highcharts-fibonacci'``.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._class_name
    
    @class_name.setter
    def class_name(self, value):
        self._class_name = validators.string(value, allow_empty = True)

    @property
    def element_type(self) -> Optional[str]:
        """The element to use for the item. Defaults to ``'span'``.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._element_type
    
    @element_type.setter
    def element_type(self, value):
        self._element_type = validators.string(value, allow_empty = True)

    @property
    def symbol(self) -> Optional[str]:
        """The name of the icon to use for the button.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._symbol

    @symbol.setter
    def symbol(self, value):
        self._symbol = validators.path(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'class_name': as_dict.get('className', None),
            'element_type': as_dict.get('elementType', None),
            'symbol': as_dict.get('symbol', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'className': self.class_name,
            'elementType': self.element_type,
            'symbol': self.symbol
        }

        return untrimmed


class AdvancedDefinitions(HighchartsMeta):
    """Definition of the icons used for Advanced stock tools."""

    def __init__(self, **kwargs):
        self._items = None
        self._fibonacci = None
        self._fibonacci_time_zones = None
        self._parallel_channel = None
        self._pitchfork = None
        self._time_cycles = None

        self.items = kwargs.get('items', None)
        self.fibonacci = kwargs.get('fibonacci', None)
        self.fibonacci_time_zones = kwargs.get('fibonacci_time_zones', None)
        self.parallel_channel = kwargs.get('parallel_channel', None)
        self.pitchfork = kwargs.get('pitchfork', None)
        self.time_cycles = kwargs.get('time_cycles', None)

    @property
    def items(self) -> Optional[List[str]]:
        """A collection of strings pointing to the properties that configure the relevant
        items.

        :rtype: :class:`list <python:list>` of :class:`str <python:str>`, or
          :obj:`None <python:None>`
        """
        return self._items

    @items.setter
    def items(self, value):
        if not value:
            self._items = None
        else:
            value = validators.iterable(value)
            self._items = [validators.string(x) for x in value]

    @property
    def fibonacci(self) -> Optional[Definition]:
        """Icon configuration for the fibonacci tool. If :obj:`None <python:None>`,
        defaults to: ``{ symbol: 'fibonacci.svg' }``.

        :rtype: :class:`Definition` or :obj:`None <python:None>`
        """
        return self._fibonacci

    @fibonacci.setter
    @class_sensitive(Definition)
    def fibonacci(self, value):
        self._fibonacci = value

    @property
    def fibonacci_time_zones(self) -> Optional[Definition]:
        """Icon configuration for the fibonacci_time_zones tool. If
        :obj:`None <python:None>`, defaults to: ``{ symbol: 'fibonacci-timezone.svg' }``.

        :rtype: :class:`Definition` or :obj:`None <python:None>`
        """
        return self._fibonacci_time_zones

    @fibonacci_time_zones.setter
    @class_sensitive(Definition)
    def fibonacci_time_zones(self, value):
        self._fibonacci_time_zones = value

    @property
    def parallel_channel(self) -> Optional[Definition]:
        """Icon configuration for the parallel channel tool. If :obj:`None <python:None>`,
        defaults to: ``{ symbol: 'parallel channel.svg' }``.

        :rtype: :class:`Definition` or :obj:`None <python:None>`
        """
        return self._parallel_channel

    @parallel_channel.setter
    @class_sensitive(Definition)
    def parallel_channel(self, value):
        self._parallel_channel = value

    @property
    def pitchfork(self) -> Optional[Definition]:
        """Icon configuration for the pitchfork tool. If :obj:`None <python:None>`,
        defaults to: ``{ symbol: 'pitchfork.svg' }``.

        :rtype: :class:`Definition` or :obj:`None <python:None>`
        """
        return self._pitchfork

    @pitchfork.setter
    @class_sensitive(Definition)
    def pitchfork(self, value):
        self._pitchfork = value

    @property
    def time_cycles(self) -> Optional[Definition]:
        """Icon configuration for the time cycles tool. If :obj:`None <python:None>`,
        defaults to: ``{ symbol: 'time-cycles.svg' }``.

        :rtype: :class:`Definition` or :obj:`None <python:None>`
        """
        return self._time_cycles

    @time_cycles.setter
    @class_sensitive(Definition)
    def time_cycles(self, value):
        self._time_cycles = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'items': as_dict.get('items', None),
            'fibonacci': as_dict.get('fibonacci', None),
            'fibonacci_time_zones': as_dict.get('fibonacciTimeZones', None),
            'parallel_channel': as_dict.get('parallelChannel', None),
            'pitchfork': as_dict.get('pitchfork', None),
            'time_cycles': as_dict.get('timeCycles', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'items': self.items,
            'fibonacci': self.fibonacci,
            'fibonacciTimeZones': self.fibonacci_time_zones,
            'parallelChannel': self.parallel_channel,
            'pitchfork': self.pitchfork,
            'timeCycles': self.time_cycles,
        }

        return untrimmed


class CrookedLinesDefinitions(HighchartsMeta):
    """Definition of the icons used for the Crooked Lines stock tools."""

    def __init__(self, **kwargs):
        self._items = None
        self._crooked3 = None
        self._crooked5 = None
        self._elliott3 = None
        self._elliott5 = None

        self.items = kwargs.get('items', None)
        self.crooked3 = kwargs.get('crooked3', None)
        self.crooked5 = kwargs.get('crooked5', None)
        self.elliott3 = kwargs.get('elliott3', None)
        self.elliott5 = kwargs.get('elliott5', None)

    @property
    def items(self) -> Optional[List[str]]:
        """A collection of strings pointing to the properties that configure the relevant
        items.

        :rtype: :class:`list <python:list>` of :class:`str <python:str>`, or
          :obj:`None <python:None>`
        """
        return self._items

    @items.setter
    def items(self, value):
        if not value:
            self._items = None
        else:
            value = validators.iterable(value)
            self._items = [validators.string(x) for x in value]

    @property
    def crooked3(self) -> Optional[Definition]:
        """Icon configuration for the crooked3 tool. If :obj:`None <python:None>`,
        defaults to: ``{ symbol: 'crooked-3.svg' }``.

        :rtype: :class:`Definition` or :obj:`None <python:None>`
        """
        return self._crooked3

    @crooked3.setter
    @class_sensitive(Definition)
    def crooked3(self, value):
        self._crooked3 = value

    @property
    def crooked5(self) -> Optional[Definition]:
        """Icon configuration for the crooked5 tool. If :obj:`None <python:None>`,
        defaults to: ``{ symbol: 'crooked-5.svg' }``.

        :rtype: :class:`Definition` or :obj:`None <python:None>`
        """
        return self._crooked5

    @crooked5.setter
    @class_sensitive(Definition)
    def crooked5(self, value):
        self._crooked5 = value

    @property
    def elliott3(self) -> Optional[Definition]:
        """Icon configuration for the elliott3 tool. If :obj:`None <python:None>`,
        defaults to: ``{ symbol: 'elliott-3.svg' }``.

        :rtype: :class:`Definition` or :obj:`None <python:None>`
        """
        return self._elliott3

    @elliott3.setter
    @class_sensitive(Definition)
    def elliott3(self, value):
        self._elliott3 = value

    @property
    def elliott5(self) -> Optional[Definition]:
        """Icon configuration for the elliott5 tool. If :obj:`None <python:None>`,
        defaults to: ``{ symbol: 'elliott-5.svg' }``.

        :rtype: :class:`Definition` or :obj:`None <python:None>`
        """
        return self._elliott5

    @elliott5.setter
    @class_sensitive(Definition)
    def elliott5(self, value):
        self._elliott5 = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'items': as_dict.get('items', None),
            'crooked3': as_dict.get('crooked3', None),
            'crooked5': as_dict.get('crooked5', None),
            'elliott3': as_dict.get('elliott3', None),
            'elliott5': as_dict.get('elliott5', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'items': self.items,
            'crooked3': self.crooked3,
            'crooked5': self.crooked5,
            'elliott3': self.elliott3,
            'elliott5': self.elliott5,
        }

        return untrimmed


class FlagsDefinitions(HighchartsMeta):
    """Definition of the icons used for Flags stock tools."""

    def __init__(self, **kwargs):
        self._items = None
        self._flag_circlepin = None
        self._flag_diamondpin = None
        self._flag_simplepin = None
        self._flag_squarepin = None

        self.items = kwargs.get('items', None)
        self.flag_circlepin = kwargs.get('flag_circlepin', None)
        self.flag_diamondpin = kwargs.get('flag_diamondpin', None)
        self.flag_simplepin = kwargs.get('flag_simplepin', None)
        self.flag_squarepin = kwargs.get('flag_squarepin', None)

    @property
    def items(self) -> Optional[List[str]]:
        """A collection of strings pointing to the properties that configure the relevant
        items.

        :rtype: :class:`list <python:list>` of :class:`str <python:str>`, or
          :obj:`None <python:None>`
        """
        return self._items

    @items.setter
    def items(self, value):
        if not value:
            self._items = None
        else:
            value = validators.iterable(value)
            self._items = [validators.string(x) for x in value]

    @property
    def flag_circlepin(self) -> Optional[Definition]:
        """Icon configuration for the flag circlepin tool. If :obj:`None <python:None>`,
        defaults to: ``{ symbol: 'flag-elipse.svg' }``.

        :rtype: :class:`Definition` or :obj:`None <python:None>`
        """
        return self._flag_circlepin

    @flag_circlepin.setter
    @class_sensitive(Definition)
    def flag_circlepin(self, value):
        self._flag_circlepin = value

    @property
    def flag_diamondpin(self) -> Optional[Definition]:
        """Icon configuration for the flag diamondpin tool. If :obj:`None <python:None>`,
        defaults to: ``{ symbol: 'flag-diamond.svg' }``.

        :rtype: :class:`Definition` or :obj:`None <python:None>`
        """
        return self._flag_diamondpin

    @flag_diamondpin.setter
    @class_sensitive(Definition)
    def flag_diamondpin(self, value):
        self._flag_diamondpin = value

    @property
    def flag_simplepin(self) -> Optional[Definition]:
        """Icon configuration for the flag simplepin tool. If :obj:`None <python:None>`,
        defaults to: ``{ symbol: 'flag-basic.svg' }``.

        :rtype: :class:`Definition` or :obj:`None <python:None>`
        """
        return self._flag_simplepin

    @flag_simplepin.setter
    @class_sensitive(Definition)
    def flag_simplepin(self, value):
        self._flag_simplepin = value

    @property
    def flag_squarepin(self) -> Optional[Definition]:
        """Icon configuration for the flag squarepin tool. If :obj:`None <python:None>`,
        defaults to: ``{ symbol: 'flag_trapeze.svg' }``.

        :rtype: :class:`Definition` or :obj:`None <python:None>`
        """
        return self._flag_squarepin

    @flag_squarepin.setter
    @class_sensitive(Definition)
    def flag_squarepin(self, value):
        self._flag_squarepin = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'items': as_dict.get('items', None),
            'flag_circlepin': as_dict.get('flagCirclepin', None),
            'flag_diamondpin': as_dict.get('flagDiamondpin', None),
            'flag_simplepin': as_dict.get('flagSimplepin', None),
            'flag_squarepin': as_dict.get('flagSquarepin', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'items': self.items,
            'flagCirclepin': self.flag_circlepin,
            'flagDiamondpin': self.flag_diamondpin,
            'flagSimplepin': self.flag_simplepin,
            'flagSquarepin': self.flag_squarepin,
        }

        return untrimmed


class LinesDefinitions(HighchartsMeta):
    """Definition of the icons used for Lines stock tools."""

    def __init__(self, **kwargs):
        self._items = None
        self._arrow_infinity_line = None
        self._arrow_ray = None
        self._arrow_segment = None
        self._horizontal_line = None
        self._line = None
        self._ray = None
        self._segment = None
        self._vertical_line = None

        self.items = kwargs.get('items', None)
        self.arrow_infinity_line = kwargs.get('arrow_infinity_line', None)
        self.arrow_ray = kwargs.get('arrow_ray', None)
        self.arrow_segment = kwargs.get('arrow_segment', None)
        self.horizontal_line = kwargs.get('horizontal_line', None)
        self.line = kwargs.get('line', None)
        self.ray = kwargs.get('ray', None)
        self.segment = kwargs.get('segment', None)
        self.vertical_line = kwargs.get('vertical_line', None)

    @property
    def items(self) -> Optional[List[str]]:
        """A collection of strings pointing to the properties that configure the relevant
        items.

        :rtype: :class:`list <python:list>` of :class:`str <python:str>`, or
          :obj:`None <python:None>`
        """
        return self._items

    @items.setter
    def items(self, value):
        if not value:
            self._items = None
        else:
            value = validators.iterable(value)
            self._items = [validators.string(x) for x in value]

    @property
    def arrow_infinity_line(self) -> Optional[Definition]:
        """Icon configuration for the arrow_infinity_line tool. If
        :obj:`None <python:None>`, defaults to: ``{ symbol: 'arrow-line.svg' }``.

        :rtype: :class:`Definition` or :obj:`None <python:None>`
        """
        return self._arrow_infinity_line

    @arrow_infinity_line.setter
    @class_sensitive(Definition)
    def arrow_infinity_line(self, value):
        self._arrow_infinity_line = value

    @property
    def arrow_ray(self) -> Optional[Definition]:
        """Icon configuration for the arrow_ray tool. If :obj:`None <python:None>`,
        defaults to: ``{ symbol: 'arrow-ray.svg' }``.

        :rtype: :class:`Definition` or :obj:`None <python:None>`
        """
        return self._arrow_ray

    @arrow_ray.setter
    @class_sensitive(Definition)
    def arrow_ray(self, value):
        self._arrow_ray = value

    @property
    def arrow_segment(self) -> Optional[Definition]:
        """Icon configuration for the arrow segment tool. If :obj:`None <python:None>`,
        defaults to: ``{ symbol: 'arrow-segment.svg' }``.

        :rtype: :class:`Definition` or :obj:`None <python:None>`
        """
        return self._arrow_segment

    @arrow_segment.setter
    @class_sensitive(Definition)
    def arrow_segment(self, value):
        self._arrow_segment = value

    @property
    def horizontal_line(self) -> Optional[Definition]:
        """Icon configuration for the horizontal_line tool. If :obj:`None <python:None>`,
        defaults to: ``{ symbol: 'horizontal-line.svg' }``.

        :rtype: :class:`Definition` or :obj:`None <python:None>`
        """
        return self._horizontal_line

    @horizontal_line.setter
    @class_sensitive(Definition)
    def horizontal_line(self, value):
        self._horizontal_line = value

    @property
    def line(self) -> Optional[Definition]:
        """Icon configuration for the line tool. If :obj:`None <python:None>`,
        defaults to: ``{ symbol: 'line.svg' }``.

        :rtype: :class:`Definition` or :obj:`None <python:None>`
        """
        return self._line

    @line.setter
    @class_sensitive(Definition)
    def line(self, value):
        self._line = value

    @property
    def ray(self) -> Optional[Definition]:
        """Icon configuration for the ray tool. If :obj:`None <python:None>`,
        defaults to: ``{ symbol: 'ray.svg' }``.

        :rtype: :class:`Definition` or :obj:`None <python:None>`
        """
        return self._ray

    @ray.setter
    @class_sensitive(Definition)
    def ray(self, value):
        self._ray = value

    @property
    def segment(self) -> Optional[Definition]:
        """Icon configuration for the segment tool. If :obj:`None <python:None>`,
        defaults to: ``{ symbol: 'segment.svg' }``.

        :rtype: :class:`Definition` or :obj:`None <python:None>`
        """
        return self._segment

    @segment.setter
    @class_sensitive(Definition)
    def segment(self, value):
        self._segment = value

    @property
    def vertical_line(self) -> Optional[Definition]:
        """Icon configuration for the vertical line tool. If :obj:`None <python:None>`,
        defaults to: ``{ symbol: 'vertical-line.svg' }``.

        :rtype: :class:`Definition` or :obj:`None <python:None>`
        """
        return self._vertical_line

    @vertical_line.setter
    @class_sensitive(Definition)
    def vertical_line(self, value):
        self._vertical_line = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'items': as_dict.get('items', None),
            'arrow_infinity_line': as_dict.get('arrowInfinityLine', None),
            'arrow_ray': as_dict.get('arrowRay', None),
            'arrow_segment': as_dict.get('arrowSegment', None),
            'horizontal_line': as_dict.get('horizontalLine', None),
            'line': as_dict.get('line', None),
            'ray': as_dict.get('ray', None),
            'segment': as_dict.get('segment', None),
            'vertical_line': as_dict.get('verticalLine', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'items': self.items,
            'arrowInfinityLine': self.arrow_infinity_line,
            'arrowRay': self.arrow_ray,
            'arrowSegment': self.arrow_segment,
            'horizontalLine': self.horizontal_line,
            'line': self.line,
            'ray': self.ray,
            'segment': self.segment,
            'verticalLine': self.vertical_line,
        }

        return untrimmed


class MeasureDefinitions(HighchartsMeta):
    """Definition of the icons used for Measure stock tools."""

    def __init__(self, **kwargs):
        self._items = None
        self._measure_x = None
        self._measure_xy = None
        self._measure_y = None

        self.items = kwargs.get('items', None)
        self.measure_x = kwargs.get('measure_x', None)
        self.measure_xy = kwargs.get('measure_xy', None)
        self.measure_y = kwargs.get('measure_y', None)

    @property
    def items(self) -> Optional[List[str]]:
        """A collection of strings pointing to the properties that configure the relevant
        items.

        :rtype: :class:`list <python:list>` of :class:`str <python:str>`, or
          :obj:`None <python:None>`
        """
        return self._items

    @items.setter
    def items(self, value):
        if not value:
            self._items = None
        else:
            value = validators.iterable(value)
            self._items = [validators.string(x) for x in value]

    @property
    def measure_x(self) -> Optional[Definition]:
        """Icon configuration for the measure_x tool. If :obj:`None <python:None>`,
        defaults to: ``{ symbol: 'measure-x.svg' }``.

        :rtype: :class:`Definition` or :obj:`None <python:None>`
        """
        return self._measure_x

    @measure_x.setter
    @class_sensitive(Definition)
    def measure_x(self, value):
        self._measure_x = value

    @property
    def measure_xy(self) -> Optional[Definition]:
        """Icon configuration for the measure XY tool. If :obj:`None <python:None>`,
        defaults to: ``{ symbol: 'measure-xy.svg' }``.

        :rtype: :class:`Definition` or :obj:`None <python:None>`
        """
        return self._measure_xy

    @measure_xy.setter
    @class_sensitive(Definition)
    def measure_xy(self, value):
        self._measure_xy = value

    @property
    def measure_y(self) -> Optional[Definition]:
        """Icon configuration for the measure y tool. If :obj:`None <python:None>`,
        defaults to: ``{ symbol: 'measure-y.svg' }``.

        :rtype: :class:`Definition` or :obj:`None <python:None>`
        """
        return self._measure_y

    @measure_y.setter
    @class_sensitive(Definition)
    def measure_y(self, value):
        self._measure_y = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'items': as_dict.get('items', None),
            'measure_x': as_dict.get('measureX', None),
            'measure_xy': as_dict.get('measureXY', None),
            'measure_y': as_dict.get('measureY', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'items': self.items,
            'measureX': self.measure_x,
            'measureXY': self.measure_xy,
            'measureY': self.measure_y,
        }

        return untrimmed


class SimpleShapesDefinitions(HighchartsMeta):
    """Definition of the icons used for Simple Shapes stock tools."""

    def __init__(self, **kwargs):
        self._items = None
        self._circle = None
        self._ellipse = None
        self._label = None
        self._rectangle = None

        self.items = kwargs.get('items', None)
        self.circle = kwargs.get('circle', None)
        self.ellipse = kwargs.get('ellipse', None)
        self.label = kwargs.get('label', None)
        self.rectangle = kwargs.get('rectangle', None)

    @property
    def items(self) -> Optional[List[str]]:
        """A collection of strings pointing to the properties that configure the relevant
        items.

        :rtype: :class:`list <python:list>` of :class:`str <python:str>`, or
          :obj:`None <python:None>`
        """
        return self._items

    @items.setter
    def items(self, value):
        if not value:
            self._items = None
        else:
            value = validators.iterable(value)
            self._items = [validators.string(x) for x in value]

    @property
    def circle(self) -> Optional[Definition]:
        """Icon configuration for the circle tool. If :obj:`None <python:None>`,
        defaults to: ``{ symbol: 'circle.svg' }``.

        :rtype: :class:`Definition` or :obj:`None <python:None>`
        """
        return self._circle

    @circle.setter
    @class_sensitive(Definition)
    def circle(self, value):
        self._circle = value

    @property
    def ellipse(self) -> Optional[Definition]:
        """Icon configuration for the ellipse tool. If :obj:`None <python:None>`,
        defaults to: ``{ symbol: 'ellipse.svg' }``.

        :rtype: :class:`Definition` or :obj:`None <python:None>`
        """
        return self._ellipse

    @ellipse.setter
    @class_sensitive(Definition)
    def ellipse(self, value):
        self._ellipse = value

    @property
    def label(self) -> Optional[Definition]:
        """Icon configuration for the label tool. If :obj:`None <python:None>`,
        defaults to: ``{ symbol: 'label.svg' }``.

        :rtype: :class:`Definition` or :obj:`None <python:None>`
        """
        return self._label

    @label.setter
    @class_sensitive(Definition)
    def label(self, value):
        self._label = value

    @property
    def rectangle(self) -> Optional[Definition]:
        """Icon configuration for the rectangle tool. If :obj:`None <python:None>`,
        defaults to: ``{ symbol: 'rectangle.svg' }``.

        :rtype: :class:`Definition` or :obj:`None <python:None>`
        """
        return self._rectangle

    @rectangle.setter
    @class_sensitive(Definition)
    def rectangle(self, value):
        self._rectangle = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'items': as_dict.get('items', None),
            'circle': as_dict.get('circle', None),
            'ellipse': as_dict.get('ellipse', None),
            'label': as_dict.get('label', None),
            'rectangle': as_dict.get('rectangle', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'items': self.items,
            'circle': self.circle,
            'ellipse': self.ellipse,
            'label': self.label,
            'rectangle': self.rectangle,
        }

        return untrimmed


class TypeChangeDefinitions(HighchartsMeta):
    """Definition of the icons used for TypeChange stock tools."""

    def __init__(self, **kwargs):
        self._items = None
        self._type_candlestick = None
        self._type_heikin_ashi = None
        self._type_hlc = None
        self._type_hollow_candlestick = None
        self._type_line = None
        self._type_ohlc = None

        self.items = kwargs.get('items', None)
        self.type_candlestick = kwargs.get('type_candlestick', None)
        self.type_heikin_ashi = kwargs.get('type_heikin_ashi', None)
        self.type_hlc = kwargs.get('type_hlc', None)
        self.type_hollow_candlestick = kwargs.get('type_hollow_candlestick', None)
        self.type_line = kwargs.get('type_line', None)
        self.type_ohlc = kwargs.get('type_ohlc', None)

    @property
    def items(self) -> Optional[List[str]]:
        """A collection of strings pointing to the properties that configure the relevant
        items.

        :rtype: :class:`list <python:list>` of :class:`str <python:str>`, or
          :obj:`None <python:None>`
        """
        return self._items

    @items.setter
    def items(self, value):
        if not value:
            self._items = None
        else:
            value = validators.iterable(value)
            self._items = [validators.string(x) for x in value]

    @property
    def type_candlestick(self) -> Optional[Definition]:
        """Icon configuration for the type candlestick tool. If :obj:`None <python:None>`,
        defaults to: ``{ symbol: 'series-candlestick.svg' }``.

        :rtype: :class:`Definition` or :obj:`None <python:None>`
        """
        return self._type_candlestick

    @type_candlestick.setter
    @class_sensitive(Definition)
    def type_candlestick(self, value):
        self._type_candlestick = value

    @property
    def type_heikin_ashi(self) -> Optional[Definition]:
        """Icon configuration for the type heikin_ashi tool. If :obj:`None <python:None>`,
        defaults to: ``{ symbol: 'series-heikin-ashi.svg' }``.

        :rtype: :class:`Definition` or :obj:`None <python:None>`
        """
        return self._type_heikin_ashi

    @type_heikin_ashi.setter
    @class_sensitive(Definition)
    def type_heikin_ashi(self, value):
        self._type_heikin_ashi = value

    @property
    def type_hlc(self) -> Optional[Definition]:
        """Icon configuration for the type hlc tool. If :obj:`None <python:None>`,
        defaults to: ``{ symbol: 'series-hlc.svg' }``.

        :rtype: :class:`Definition` or :obj:`None <python:None>`
        """
        return self._type_hlc

    @type_hlc.setter
    @class_sensitive(Definition)
    def type_hlc(self, value):
        self._type_hlc = value

    @property
    def type_hollow_candlestick(self) -> Optional[Definition]:
        """Icon configuration for the type hollow_candlestick tool. If
        :obj:`None <python:None>`, defaults to:
        ``{ symbol: 'series-hollow-candlestick.svg' }``.

        :rtype: :class:`Definition` or :obj:`None <python:None>`
        """
        return self._type_hollow_candlestick

    @type_hollow_candlestick.setter
    @class_sensitive(Definition)
    def type_hollow_candlestick(self, value):
        self._type_hollow_candlestick = value

    @property
    def type_line(self) -> Optional[Definition]:
        """Icon configuration for the type line tool. If :obj:`None <python:None>`,
        defaults to: ``{ symbol: 'series-line.svg' }``.

        :rtype: :class:`Definition` or :obj:`None <python:None>`
        """
        return self._type_line

    @type_line.setter
    @class_sensitive(Definition)
    def type_line(self, value):
        self._type_line = value

    @property
    def type_ohlc(self) -> Optional[Definition]:
        """Icon configuration for the type ohlc tool. If :obj:`None <python:None>`,
        defaults to: ``{ symbol: 'series-ohlc.svg' }``.

        :rtype: :class:`Definition` or :obj:`None <python:None>`
        """
        return self._type_ohlc

    @type_ohlc.setter
    @class_sensitive(Definition)
    def type_ohlc(self, value):
        self._type_ohlc = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'items': as_dict.get('items', None),
            'type_candlestick': as_dict.get('typeCandlestick', None),
            'type_heikin_ashi': as_dict.get('typeHeikinAshi', None),
            'type_hlc': as_dict.get('typeHLC', None),
            'type_hollow_candlestick': as_dict.get('typeHollowCandlestick', None),
            'type_line': as_dict.get('typeLine', None),
            'type_ohlc': as_dict.get('typeOHLC', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'items': self.items,
            'typeCandlestick': self.type_candlestick,
            'typeHeikinAshi': self.type_heikin_ashi,
            'typeHLC': self.type_hlc,
            'typeHollowCandlestick': self.type_hollow_candlestick,
            'typeLine': self.type_line,
            'typeOHLC': self.type_ohlc,
        }

        return untrimmed


class VerticalLabelsDefinitions(HighchartsMeta):
    """Definition of the icons used for VerticalLabels stock tools."""

    def __init__(self, **kwargs):
        self._items = None
        self._vertical_arrow = None
        self._vertical_counter = None
        self._vertical_label = None

        self.items = kwargs.get('items', None)
        self.vertical_arrow = kwargs.get('vertical_arrow', None)
        self.vertical_counter = kwargs.get('vertical_counter', None)
        self.vertical_label = kwargs.get('vertical_label', None)

    @property
    def items(self) -> Optional[List[str]]:
        """A collection of strings pointing to the properties that configure the relevant
        items.

        :rtype: :class:`list <python:list>` of :class:`str <python:str>`, or
          :obj:`None <python:None>`
        """
        return self._items

    @items.setter
    def items(self, value):
        if not value:
            self._items = None
        else:
            value = validators.iterable(value)
            self._items = [validators.string(x) for x in value]

    @property
    def vertical_arrow(self) -> Optional[Definition]:
        """Icon configuration for the vertical arrow tool. If :obj:`None <python:None>`,
        defaults to: ``{ symbol: 'vertical-arrow.svg' }``.

        :rtype: :class:`Definition` or :obj:`None <python:None>`
        """
        return self._vertical_arrow

    @vertical_arrow.setter
    @class_sensitive(Definition)
    def vertical_arrow(self, value):
        self._vertical_arrow = value

    @property
    def vertical_counter(self) -> Optional[Definition]:
        """Icon configuration for the vertical counter tool. If :obj:`None <python:None>`,
        defaults to: ``{ symbol: 'vertical-counter.svg' }``.

        :rtype: :class:`Definition` or :obj:`None <python:None>`
        """
        return self._vertical_counter

    @vertical_counter.setter
    @class_sensitive(Definition)
    def vertical_counter(self, value):
        self._vertical_counter = value

    @property
    def vertical_label(self) -> Optional[Definition]:
        """Icon configuration for the vertical label tool. If :obj:`None <python:None>`,
        defaults to: ``{ symbol: 'vertical-label.svg' }``.

        :rtype: :class:`Definition` or :obj:`None <python:None>`
        """
        return self._vertical_label

    @vertical_label.setter
    @class_sensitive(Definition)
    def vertical_label(self, value):
        self._vertical_label = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'items': as_dict.get('items', None),
            'vertical_arrow': as_dict.get('verticalArrow', None),
            'vertical_counter': as_dict.get('verticalCounter', None),
            'vertical_label': as_dict.get('verticalLabel', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'items': self.items,
            'verticalArrow': self.vertical_arrow,
            'verticalCounter': self.vertical_counter,
            'verticalLabel': self.vertical_label,
        }

        return untrimmed


class ZoomChangeDefinitions(HighchartsMeta):
    """Definition of the icons used for ZoomChange stock tools."""

    def __init__(self, **kwargs):
        self._items = None
        self._zoom_x = None
        self._zoom_xy = None
        self._zoom_y = None

        self.items = kwargs.get('items', None)
        self.zoom_x = kwargs.get('zoom_x', None)
        self.zoom_xy = kwargs.get('zoom_xy', None)
        self.zoom_y = kwargs.get('zoom_y', None)

    @property
    def items(self) -> Optional[List[str]]:
        """A collection of strings pointing to the properties that configure the relevant
        items.

        :rtype: :class:`list <python:list>` of :class:`str <python:str>`, or
          :obj:`None <python:None>`
        """
        return self._items

    @items.setter
    def items(self, value):
        if not value:
            self._items = None
        else:
            value = validators.iterable(value)
            self._items = [validators.string(x) for x in value]

    @property
    def zoom_x(self) -> Optional[Definition]:
        """Icon configuration for the zoom_x tool. If :obj:`None <python:None>`,
        defaults to: ``{ symbol: 'zoom-x.svg' }``.

        :rtype: :class:`Definition` or :obj:`None <python:None>`
        """
        return self._zoom_x

    @zoom_x.setter
    @class_sensitive(Definition)
    def zoom_x(self, value):
        self._zoom_x = value

    @property
    def zoom_xy(self) -> Optional[Definition]:
        """Icon configuration for the zoom XY tool. If :obj:`None <python:None>`,
        defaults to: ``{ symbol: 'zoom-xy.svg' }``.

        :rtype: :class:`Definition` or :obj:`None <python:None>`
        """
        return self._zoom_xy

    @zoom_xy.setter
    @class_sensitive(Definition)
    def zoom_xy(self, value):
        self._zoom_xy = value

    @property
    def zoom_y(self) -> Optional[Definition]:
        """Icon configuration for the zoom y tool. If :obj:`None <python:None>`,
        defaults to: ``{ symbol: 'zoom-y.svg' }``.

        :rtype: :class:`Definition` or :obj:`None <python:None>`
        """
        return self._zoom_y

    @zoom_y.setter
    @class_sensitive(Definition)
    def zoom_y(self, value):
        self._zoom_y = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'items': as_dict.get('items', None),
            'zoom_x': as_dict.get('zoomX', None),
            'zoom_xy': as_dict.get('zoomXY', None),
            'zoom_y': as_dict.get('zoomY', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'items': self.items,
            'zoomX': self.zoom_x,
            'zoomXY': self.zoom_xy,
            'zoomY': self.zoom_y,
        }

        return untrimmed


class StockToolsDefinitions(HighchartsMeta):
    """Configuration of the icons to use for the default Stock Tools GUI."""

    def __init__(self, **kwargs):
        self._advanced = None
        self._crooked_lines = None
        self._current_price_indicator = None
        self._flags = None
        self._full_screen = None
        self._indicators = None
        self._lines = None
        self._measure = None
        self._save_chart = None
        self._separator = None
        self._simple_shapes = None
        self._toggle_annotations = None
        self._type_change = None
        self._vertical_labels = None
        self._zoom_change = None

        self.advanced = kwargs.get('advanced', None)
        self.crooked_lines = kwargs.get('crooked_lines', None)
        self.current_price_indicator = kwargs.get('current_price_indicator', None)
        self.flags = kwargs.get('flags', None)
        self.full_screen = kwargs.get('full_screen', None)
        self.indicators = kwargs.get('indicators', None)
        self.lines = kwargs.get('lines', None)
        self.measure = kwargs.get('measure', None)
        self.save_chart = kwargs.get('save_chart', None)
        self.separator = kwargs.get('separator', None)
        self.simple_shapes = kwargs.get('simple_shapes', None)
        self.toggle_annotations = kwargs.get('toggle_annotations', None)
        self.type_change = kwargs.get('type_change', None)
        self.vertical_labels = kwargs.get('vertical_labels', None)
        self.zoom_change = kwargs.get('zoom_change', None)

    @property
    def advanced(self) -> Optional[AdvancedDefinitions]:
        """Configuration of the icons for the **Advanced** stock tools. Defaults to
        :obj:`None <python:None>`.

        :rtype: :class:`AdvancedDefinitions` or :obj:`None <python:None>`
        """
        return self._advanced

    @advanced.setter
    @class_sensitive(AdvancedDefinitions)
    def advanced(self, value):
        self._advanced = value

    @property
    def crooked_lines(self) -> Optional[CrookedLinesDefinitions]:
        """Configuration of the icons for the **CrookedLines** stock tools. Defaults to
        :obj:`None <python:None>`.

        :rtype: :class:`CrookedLinesDefinitions` or :obj:`None <python:None>`
        """
        return self._crooked_lines

    @crooked_lines.setter
    @class_sensitive(CrookedLinesDefinitions)
    def crooked_lines(self, value):
        self._crooked_lines = value

    @property
    def current_price_indicator(self) -> Optional[Definition]:
        """Icon configuration for the Current Price Indicator tool. If
        :obj:`None <python:None>`, defaults to: ``{ symbol: 'current-price-show.svg' }``.

        :rtype: :class:`Definition` or :obj:`None <python:None>`
        """
        return self._current_price_indicator

    @current_price_indicator.setter
    @class_sensitive(Definition)
    def current_price_indicator(self, value):
        self._current_price_indicator = value

    @property
    def flags(self) -> Optional[FlagsDefinitions]:
        """Configuration of the icons for the **Flags** stock tools. Defaults to
        :obj:`None <python:None>`.

        :rtype: :class:`FlagsDefinitions` or :obj:`None <python:None>`
        """
        return self._flags

    @flags.setter
    @class_sensitive(FlagsDefinitions)
    def flags(self, value):
        self._flags = value

    @property
    def full_screen(self) -> Optional[Definition]:
        """Icon configuration for the Full Screen tool. If
        :obj:`None <python:None>`, defaults to: ``{ symbol: 'fullscreen.svg' }``.

        :rtype: :class:`Definition` or :obj:`None <python:None>`
        """
        return self._full_screen

    @full_screen.setter
    @class_sensitive(Definition)
    def full_screen(self, value):
        self._full_screen = value

    @property
    def indicators(self) -> Optional[Definition]:
        """Icon configuration for the Indicators tool. If
        :obj:`None <python:None>`, defaults to: ``{ symbol: 'indicators.svg' }``.

        :rtype: :class:`Definition` or :obj:`None <python:None>`
        """
        return self._indicators

    @indicators.setter
    @class_sensitive(Definition)
    def indicators(self, value):
        self._indicators = value

    @property
    def lines(self) -> Optional[LinesDefinitions]:
        """Configuration of the icons for the **Lines** stock tools. Defaults to
        :obj:`None <python:None>`.

        :rtype: :class:`LinesDefinitions` or :obj:`None <python:None>`
        """
        return self._lines

    @lines.setter
    @class_sensitive(LinesDefinitions)
    def lines(self, value):
        self._lines = value

    @property
    def measure(self) -> Optional[MeasureDefinitions]:
        """Configuration of the icons for the **Measure** stock tools. Defaults to
        :obj:`None <python:None>`.

        :rtype: :class:`MeasureDefinitions` or :obj:`None <python:None>`
        """
        return self._measure

    @measure.setter
    @class_sensitive(MeasureDefinitions)
    def measure(self, value):
        self._measure = value

    @property
    def save_chart(self) -> Optional[Definition]:
        """Icon configuration for the Indicators tool. If
        :obj:`None <python:None>`, defaults to: ``{ symbol: 'save-chart.svg' }``.

        :rtype: :class:`Definition` or :obj:`None <python:None>`
        """
        return self._save_chart

    @save_chart.setter
    @class_sensitive(Definition)
    def save_chart(self, value):
        self._save_chart = value

    @property
    def separator(self) -> Optional[Definition]:
        """Icon configuration for the Indicators tool. If
        :obj:`None <python:None>`, defaults to: ``{ symbol: 'separator.svg' }``.

        :rtype: :class:`Definition` or :obj:`None <python:None>`
        """
        return self._separator

    @separator.setter
    @class_sensitive(Definition)
    def separator(self, value):
        self._separator = value

    @property
    def simple_shapes(self) -> Optional[SimpleShapesDefinitions]:
        """Configuration of the icons for the **Simple Shapes** stock tools. Defaults to
        :obj:`None <python:None>`.

        :rtype: :class:`MeasureDefinitions` or :obj:`None <python:None>`
        """
        return self._simple_shapes

    @simple_shapes.setter
    @class_sensitive(SimpleShapesDefinitions)
    def simple_shapes(self, value):
        self._simple_shapes = value

    @property
    def toggle_annotations(self) -> Optional[Definition]:
        """Icon configuration for the toggle annotations tool. If
        :obj:`None <python:None>`, defaults to: ``{ symbol: 'annotations-visible.svg' }``.

        :rtype: :class:`Definition` or :obj:`None <python:None>`
        """
        return self._toggle_annotations

    @toggle_annotations.setter
    @class_sensitive(Definition)
    def toggle_annotations(self, value):
        self._toggle_annotations = value

    @property
    def type_change(self) -> Optional[TypeChangeDefinitions]:
        """Configuration of the icons for the **TypeChange** stock tools. Defaults to
        :obj:`None <python:None>`.

        :rtype: :class:`TypeChangeDefinitions` or :obj:`None <python:None>`
        """
        return self._type_change

    @type_change.setter
    @class_sensitive(TypeChangeDefinitions)
    def type_change(self, value):
        self._type_change = value

    @property
    def vertical_labels(self) -> Optional[VerticalLabelsDefinitions]:
        """Configuration of the icons for the **VerticalLabels** stock tools. Defaults to
        :obj:`None <python:None>`.

        :rtype: :class:`VerticalLabelsDefinitions` or :obj:`None <python:None>`
        """
        return self._vertical_labels

    @vertical_labels.setter
    @class_sensitive(VerticalLabelsDefinitions)
    def vertical_labels(self, value):
        self._vertical_labels = value

    @property
    def zoom_change(self) -> Optional[ZoomChangeDefinitions]:
        """Configuration of the icons for the **ZoomChange** stock tools. Defaults to
        :obj:`None <python:None>`.

        :rtype: :class:`ZoomChangeDefinitions` or :obj:`None <python:None>`
        """
        return self._zoom_change

    @zoom_change.setter
    @class_sensitive(ZoomChangeDefinitions)
    def zoom_change(self, value):
        self._zoom_change = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'advanced': as_dict.get('advanced', None),
            'crooked_lines': as_dict.get('crookedLines', None),
            'current_price_indicator': as_dict.get('currentPriceIndicator', None),
            'flags': as_dict.get('flags', None),
            'full_screen': as_dict.get('fullScreen', None),
            'indicators': as_dict.get('indicators', None),
            'lines': as_dict.get('lines', None),
            'measure': as_dict.get('measure', None),
            'save_chart': as_dict.get('saveChart', None),
            'separator': as_dict.get('separator', None),
            'simple_shapes': as_dict.get('simpleShapes', None),
            'toggle_annotations': as_dict.get('toggleAnnotations', None),
            'type_change': as_dict.get('typeChange', None),
            'vertical_labels': as_dict.get('verticalLabels', None),
            'zoom_change': as_dict.get('zoomChange', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'advanced': self.advanced,
            'crookedLines': self.crooked_lines,
            'currentPriceIndicator': self.current_price_indicator,
            'flags': self.flags,
            'fullScreen': self.full_screen,
            'indicators': self.indicators,
            'lines': self.lines,
            'measure': self.measure,
            'saveChart': self.save_chart,
            'separator': self.separator,
            'simpleShapes': self.simple_shapes,
            'toggleAnnotations': self.toggle_annotations,
            'typeChange': self.type_change,
            'verticalLabels': self.vertical_labels,
            'zoomChange': self.zoom_change,
        }

        return untrimmed

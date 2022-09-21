from typing import Optional

from validator_collection import validators

from highcharts_stock.metaclasses import HighchartsMeta
from highcharts_stock.decorators import class_sensitive


class StockToolsGUI(HighchartsMeta):
    """Language settings for the :term:`stock tools`."""

    def __init__(self, **kwargs):
        self._advanced = None
        self._arrow_infinity_line = None
        self._arrow_ray = None
        self._arrow_segment = None
        self._circle = None
        self._crooked3 = None
        self._crooked5 = None
        self._crooked_lines = None
        self._current_price_indicator = None
        self._elliott3 = None
        self._elliott5 = None
        self._ellipse = None
        self._fibonacci = None
        self._fibonacci_time_zones = None
        self._flag_circlepin = None
        self._flag_diamondpin = None
        self._flags = None
        self._flag_simplepin = None
        self._flag_squarepin = None
        self._fullscreen = None
        self._horizontal_line = None
        self._indicators = None
        self._infinity_line = None
        self._label = None
        self._line = None
        self._lines = None
        self._measure = None
        self._measure_x = None
        self._measure_xy = None
        self._measure_y = None
        self._parallel_channel = None
        self._pitchfork = None
        self._ray = None
        self._rectangle = None
        self._save_chart = None
        self._segment = None
        self._simple_shapes = None
        self._time_cycles = None
        self._toggle_annotations = None
        self._type_candlestick = None
        self._type_change = None
        self._type_heikin_ashi = None
        self._type_hlc = None
        self._type_hollow_candlestick = None
        self._type_line = None
        self._type_ohlc = None
        self._vertical_arrow = None
        self._vertical_counter = None
        self._vertical_label = None
        self._vertical_labels = None
        self._vertical_line = None
        self._zoom_change = None
        self._zoom_x = None
        self._zoom_xy = None
        self._zoom_y = None

        self.advanced = kwargs.get('advanced', None)
        self.arrow_infinity_line = kwargs.get('arrow_infinity_line', None)
        self.arrow_ray = kwargs.get('arrow_ray', None)
        self.arrow_segment = kwargs.get('arrow_segment', None)
        self.circle = kwargs.get('circle', None)
        self.crooked3 = kwargs.get('crooked3', None)
        self.crooked5 = kwargs.get('crooked5', None)
        self.crooked_lines = kwargs.get('crooked_lines', None)
        self.current_price_indicator = kwargs.get('current_price_indicator', None)
        self.elliott3 = kwargs.get('elliott3', None)
        self.elliott5 = kwargs.get('elliott5', None)
        self.ellipse = kwargs.get('ellipse', None)
        self.fibonacci = kwargs.get('fibonacci', None)
        self.fibonacci_time_zones = kwargs.get('fibonacci_time_zones', None)
        self.flag_circlepin = kwargs.get('flag_circlepin', None)
        self.flag_diamondpin = kwargs.get('flag_diamondpin', None)
        self.flags = kwargs.get('flags', None)
        self.flag_simplepin = kwargs.get('flag_simplepin', None)
        self.flag_squarepin = kwargs.get('flag_squarepin', None)
        self.fullscreen = kwargs.get('fullscreen', None)
        self.horizontal_line = kwargs.get('horizontal_line', None)
        self.indicators = kwargs.get('indicators', None)
        self.infinity_line = kwargs.get('infinity_line', None)
        self.label = kwargs.get('label', None)
        self.line = kwargs.get('line', None)
        self.lines = kwargs.get('lines', None)
        self.measure = kwargs.get('measure', None)
        self.measure_x = kwargs.get('measure_x', None)
        self.measure_xy = kwargs.get('measure_xy', None)
        self.measure_y = kwargs.get('measure_y', None)
        self.parallel_channel = kwargs.get('parallel_channel', None)
        self.pitchfork = kwargs.get('pitchfork', None)
        self.ray = kwargs.get('ray', None)
        self.rectangle = kwargs.get('rectangle', None)
        self.save_chart = kwargs.get('save_chart', None)
        self.segment = kwargs.get('segment', None)
        self.simple_shapes = kwargs.get('simple_shapes', None)
        self.time_cycles = kwargs.get('time_cycles', None)
        self.toggle_annotations = kwargs.get('toggle_annotations', None)
        self.type_candlestick = kwargs.get('type_candlestick', None)
        self.type_change = kwargs.get('type_change', None)
        self.type_heikin_ashi = kwargs.get('type_heikin_ashi', None)
        self.type_hlc = kwargs.get('type_hlc', None)
        self.type_hollow_candlestick = kwargs.get('type_hollow_candlestick', None)
        self.type_line = kwargs.get('type_line', None)
        self.type_ohlc = kwargs.get('type_ohlc', None)
        self.vertical_arrow = kwargs.get('vertical_arrow', None)
        self.vertical_counter = kwargs.get('vertical_counter', None)
        self.vertical_label = kwargs.get('vertical_label', None)
        self.vertical_labels = kwargs.get('vertical_labels', None)
        self.vertical_line = kwargs.get('vertical_line', None)
        self.zoom_change = kwargs.get('zoom_change', None)
        self.zoom_x = kwargs.get('zoom_x', None)
        self.zoom_xy = kwargs.get('zoom_xy', None)
        self.zoom_y = kwargs.get('zoom_y', None)

    @property
    def advanced(self) -> Optional[str]:
        """Defaults to ``'Advanced'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._advanced

    @advanced.setter
    def advanced(self, value):
        self._advanced = validators.string(value, allow_empty = True)

    @property
    def arrow_infinity_line(self) -> Optional[str]:
        """Defaults to ``'Arrow line'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._arrow_infinity_line

    @arrow_infinity_line.setter
    def arrow_infinity_line(self, value):
        self._arrow_infinity_line = validators.string(value, allow_empty = True)

    @property
    def arrow_ray(self) -> Optional[str]:
        """Defaults to ``'Arrow ray'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._arrow_ray

    @arrow_ray.setter
    def arrow_ray(self, value):
        self._arrow_ray = validators.string(value, allow_empty = True)

    @property
    def arrow_segment(self) -> Optional[str]:
        """Defaults to ``'Arrow segment'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._arrow_segment

    @arrow_segment.setter
    def arrow_segment(self, value):
        self._arrow_segment = validators.string(value, allow_empty = True)

    @property
    def circle(self) -> Optional[str]:
        """Defaults to ``'Circle'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._circle

    @circle.setter
    def circle(self, value):
        self._circle = validators.string(value, allow_empty = True)

    @property
    def crooked3(self) -> Optional[str]:
        """Defaults to ``'Crooked 3 line'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._crooked3

    @crooked3.setter
    def crooked3(self, value):
        self._crooked3 = validators.string(value, allow_empty = True)

    @property
    def crooked5(self) -> Optional[str]:
        """Defaults to ``'Crooked 5 line'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._crooked5

    @crooked5.setter
    def crooked5(self, value):
        self._crooked5 = validators.string(value, allow_empty = True)

    @property
    def crooked_lines(self) -> Optional[str]:
        """Defaults to ``'Crooked lines'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._crooked_lines

    @crooked_lines.setter
    def crooked_lines(self, value):
        self._crooked_lines = validators.string(value, allow_empty = True)

    @property
    def current_price_indicator(self) -> Optional[str]:
        """Defaults to ``'Current Price Indicators'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._current_price_indicator

    @current_price_indicator.setter
    def current_price_indicator(self, value):
        self._current_price_indicator = validators.string(value, allow_empty = True)

    @property
    def elliott3(self) -> Optional[str]:
        """Defaults to ``'Elliott 3 line'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._elliott3

    @elliott3.setter
    def elliott3(self, value):
        self._elliott3 = validators.string(value, allow_empty = True)

    @property
    def elliott5(self) -> Optional[str]:
        """Defaults to ``'Elliott 5 line'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._elliott5

    @elliott5.setter
    def elliott5(self, value):
        self._elliott5 = validators.string(value, allow_empty = True)

    @property
    def ellipse(self) -> Optional[str]:
        """Defaults to ``'Ellipse'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._ellipse

    @ellipse.setter
    def ellipse(self, value):
        self._ellipse = validators.string(value, allow_empty = True)

    @property
    def fibonacci(self) -> Optional[str]:
        """Defaults to ``'Fibonacci'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._fibonacci

    @fibonacci.setter
    def fibonacci(self, value):
        self._fibonacci = validators.string(value, allow_empty = True)

    @property
    def fibonacci_time_zones(self) -> Optional[str]:
        """Defaults to ``'Fibonacci Time Zones'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._fibonacci_time_zones

    @fibonacci_time_zones.setter
    def fibonacci_time_zones(self, value):
        self._fibonacci_time_zones = validators.string(value, allow_empty = True)

    @property
    def flag_circlepin(self) -> Optional[str]:
        """Defaults to ``'Flag circle'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._flag_circlepin

    @flag_circlepin.setter
    def flag_circlepin(self, value):
        self._flag_circlepin = validators.string(value, allow_empty = True)

    @property
    def flag_diamondpin(self) -> Optional[str]:
        """Defaults to ``'Flag diamond'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._flag_diamondpin

    @flag_diamondpin.setter
    def flag_diamondpin(self, value):
        self._flag_diamondpin = validators.string(value, allow_empty = True)

    @property
    def flags(self) -> Optional[str]:
        """Defaults to ``'Flags'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._flags

    @flags.setter
    def flags(self, value):
        self._flags = validators.string(value, allow_empty = True)

    @property
    def flag_simplepin(self) -> Optional[str]:
        """Defaults to ``'Flag simple'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._flag_simplepin

    @flag_simplepin.setter
    def flag_simplepin(self, value):
        self._flag_simplepin = validators.string(value, allow_empty = True)

    @property
    def flag_squarepin(self) -> Optional[str]:
        """Defaults to ``'Flag square'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._flag_squarepin

    @flag_squarepin.setter
    def flag_squarepin(self, value):
        self._flag_squarepin = validators.string(value, allow_empty = True)

    @property
    def fullscreen(self) -> Optional[str]:
        """Defaults to ``'Fullscreen'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._fullscreen

    @fullscreen.setter
    def fullscreen(self, value):
        self._fullscreen = validators.string(value, allow_empty = True)

    @property
    def horizontal_line(self) -> Optional[str]:
        """Defaults to ``'Horizontal line'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._horizontal_line

    @horizontal_line.setter
    def horizontal_line(self, value):
        self._horizontal_line = validators.string(value, allow_empty = True)

    @property
    def indicators(self) -> Optional[str]:
        """Defaults to ``'Indicators'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._indicators

    @indicators.setter
    def indicators(self, value):
        self._indicators = validators.string(value, allow_empty = True)

    @property
    def infinity_line(self) -> Optional[str]:
        """Defaults to ``'Infinity line'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._infinity_line

    @infinity_line.setter
    def infinity_line(self, value):
        self._infinity_line = validators.string(value, allow_empty = True)

    @property
    def label(self) -> Optional[str]:
        """Defaults to ``'Label'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._label

    @label.setter
    def label(self, value):
        self._label = validators.string(value, allow_empty = True)

    @property
    def line(self) -> Optional[str]:
        """Defaults to ``'Line'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._line

    @line.setter
    def line(self, value):
        self._line = validators.string(value, allow_empty = True)

    @property
    def lines(self) -> Optional[str]:
        """Defaults to ``'Lines'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._lines

    @lines.setter
    def lines(self, value):
        self._lines = validators.string(value, allow_empty = True)

    @property
    def measure(self) -> Optional[str]:
        """Defaults to ``'Measure'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._measure

    @measure.setter
    def measure(self, value):
        self._measure = validators.string(value, allow_empty = True)

    @property
    def measure_x(self) -> Optional[str]:
        """Defaults to ``'Measure X'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._measure_x

    @measure_x.setter
    def measure_x(self, value):
        self._measure_x = validators.string(value, allow_empty = True)

    @property
    def measure_xy(self) -> Optional[str]:
        """Defaults to ``'Measure XY'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._measure_xy

    @measure_xy.setter
    def measure_xy(self, value):
        self._measure_xy = validators.string(value, allow_empty = True)

    @property
    def measure_y(self) -> Optional[str]:
        """Defaults to ``'Measure Y'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._measure_y

    @measure_y.setter
    def measure_y(self, value):
        self._measure_y = validators.string(value, allow_empty = True)

    @property
    def parallel_channel(self) -> Optional[str]:
        """Defaults to ``'Parallel Channel'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._parallel_channel

    @parallel_channel.setter
    def parallel_channel(self, value):
        self._parallel_channel = validators.string(value, allow_empty = True)

    @property
    def pitchfork(self) -> Optional[str]:
        """Defaults to ``'Pitchfork'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._pitchfork

    @pitchfork.setter
    def pitchfork(self, value):
        self._pitchfork = validators.string(value, allow_empty = True)

    @property
    def ray(self) -> Optional[str]:
        """Defaults to ``'Ray'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._ray

    @ray.setter
    def ray(self, value):
        self._ray = validators.string(value, allow_empty = True)

    @property
    def rectangle(self) -> Optional[str]:
        """Defaults to ``'Rectangle'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._rectangle

    @rectangle.setter
    def rectangle(self, value):
        self._rectangle = validators.string(value, allow_empty = True)

    @property
    def save_chart(self) -> Optional[str]:
        """Defaults to ``'Save chart'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._save_chart

    @save_chart.setter
    def save_chart(self, value):
        self._save_chart = validators.string(value, allow_empty = True)

    @property
    def segment(self) -> Optional[str]:
        """Defaults to ``'Segment'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._segment

    @segment.setter
    def segment(self, value):
        self._segment = validators.string(value, allow_empty = True)

    @property
    def simple_shapes(self) -> Optional[str]:
        """Defaults to ``'Simple shapes'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._simple_shapes

    @simple_shapes.setter
    def simple_shapes(self, value):
        self._simple_shapes = validators.string(value, allow_empty = True)

    @property
    def time_cycles(self) -> Optional[str]:
        """Defaults to ``'Time Cycles'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._time_cycles

    @time_cycles.setter
    def time_cycles(self, value):
        self._time_cycles = validators.string(value, allow_empty = True)

    @property
    def toggle_annotations(self) -> Optional[str]:
        """Defaults to ``'Toggle annotations'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._toggle_annotations

    @toggle_annotations.setter
    def toggle_annotations(self, value):
        self._toggle_annotations = validators.string(value, allow_empty = True)

    @property
    def type_candlestick(self) -> Optional[str]:
        """Defaults to ``'Candlestick'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._type_candlestick

    @type_candlestick.setter
    def type_candlestick(self, value):
        self._type_candlestick = validators.string(value, allow_empty = True)

    @property
    def type_change(self) -> Optional[str]:
        """Defaults to ``'Type change'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._type_change

    @type_change.setter
    def type_change(self, value):
        self._type_change = validators.string(value, allow_empty = True)

    @property
    def type_heikin_ashi(self) -> Optional[str]:
        """Defaults to ``'Heikin Ashi'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._type_heikin_ashi

    @type_heikin_ashi.setter
    def type_heikin_ashi(self, value):
        self._type_heikin_ashi = validators.string(value, allow_empty = True)

    @property
    def type_hlc(self) -> Optional[str]:
        """Defaults to ``'HLC'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._type_hlc

    @type_hlc.setter
    def type_hlc(self, value):
        self._type_hlc = validators.string(value, allow_empty = True)

    @property
    def type_hollow_candlestick(self) -> Optional[str]:
        """Defaults to ``'Hollow Candlestick'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._type_hollow_candlestick

    @type_hollow_candlestick.setter
    def type_hollow_candlestick(self, value):
        self._type_hollow_candlestick = validators.string(value, allow_empty = True)

    @property
    def type_line(self) -> Optional[str]:
        """Defaults to ``'Line'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._type_line

    @type_line.setter
    def type_line(self, value):
        self._type_line = validators.string(value, allow_empty = True)

    @property
    def type_ohlc(self) -> Optional[str]:
        """Defaults to ``'OHLC'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._type_ohlc

    @type_ohlc.setter
    def type_ohlc(self, value):
        self._type_ohlc = validators.string(value, allow_empty = True)

    @property
    def vertical_arrow(self) -> Optional[str]:
        """Defaults to ``'Vertical arrow'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._vertical_arrow

    @vertical_arrow.setter
    def vertical_arrow(self, value):
        self._vertical_arrow = validators.string(value, allow_empty = True)

    @property
    def vertical_counter(self) -> Optional[str]:
        """Defaults to ``'Vertical counter'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._vertical_counter

    @vertical_counter.setter
    def vertical_counter(self, value):
        self._vertical_counter = validators.string(value, allow_empty = True)

    @property
    def vertical_label(self) -> Optional[str]:
        """Defaults to ``'Vertical label'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._vertical_label

    @vertical_label.setter
    def vertical_label(self, value):
        self._vertical_label = validators.string(value, allow_empty = True)

    @property
    def vertical_labels(self) -> Optional[str]:
        """Defaults to ``'Vertical labels'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._vertical_labels

    @vertical_labels.setter
    def vertical_labels(self, value):
        self._vertical_labels = validators.string(value, allow_empty = True)

    @property
    def vertical_line(self) -> Optional[str]:
        """Defaults to ``'Vertical line'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._vertical_line

    @vertical_line.setter
    def vertical_line(self, value):
        self._vertical_line = validators.string(value, allow_empty = True)

    @property
    def zoom_change(self) -> Optional[str]:
        """Defaults to ``'Zoom change'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._zoom_change

    @zoom_change.setter
    def zoom_change(self, value):
        self._zoom_change = validators.string(value, allow_empty = True)

    @property
    def zoom_x(self) -> Optional[str]:
        """Defaults to ``'Zoom X'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._zoom_x

    @zoom_x.setter
    def zoom_x(self, value):
        self._zoom_x = validators.string(value, allow_empty = True)

    @property
    def zoom_xy(self) -> Optional[str]:
        """Defaults to ``'Zoom XY'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._zoom_xy

    @zoom_xy.setter
    def zoom_xy(self, value):
        self._zoom_xy = validators.string(value, allow_empty = True)

    @property
    def zoom_y(self) -> Optional[str]:
        """Defaults to ``'Zoom Y'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._zoom_y

    @zoom_y.setter
    def zoom_y(self, value):
        self._zoom_y = validators.string(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'advanced': as_dict.get('advanced', None),
            'arrow_infinity_line': as_dict.get('arrowInfinityLine', None),
            'arrow_ray': as_dict.get('arrowRay', None),
            'arrow_segment': as_dict.get('arrowSegment', None),
            'circle': as_dict.get('circle', None),
            'crooked3': as_dict.get('crooked3', None),
            'crooked5': as_dict.get('crooked5', None),
            'crooked_lines': as_dict.get('crookedLines', None),
            'current_price_indicator': as_dict.get('currentPriceIndicator', None),
            'elliott3': as_dict.get('elliott3', None),
            'elliott5': as_dict.get('elliott5', None),
            'ellipse': as_dict.get('ellipse', None),
            'fibonacci': as_dict.get('fibonacci', None),
            'fibonacci_time_zones': as_dict.get('fibonacciTimeZones', None),
            'flag_circlepin': as_dict.get('flagCirclepin', None),
            'flag_diamondpin': as_dict.get('flagDiamondpin', None),
            'flags': as_dict.get('flags', None),
            'flag_simplepin': as_dict.get('flagSimplepin', None),
            'flag_squarepin': as_dict.get('flagSquarepin', None),
            'fullscreen': as_dict.get('fullscreen', None),
            'horizontal_line': as_dict.get('horizontalLine', None),
            'indicators': as_dict.get('indicators', None),
            'infinity_line': as_dict.get('infinityLine', None),
            'label': as_dict.get('label', None),
            'line': as_dict.get('line', None),
            'lines': as_dict.get('lines', None),
            'measure': as_dict.get('measure', None),
            'measure_x': as_dict.get('measureX', None),
            'measure_xy': as_dict.get('measureXY', None),
            'measure_y': as_dict.get('measureY', None),
            'parallel_channel': as_dict.get('parallelChannel', None),
            'pitchfork': as_dict.get('pitchfork', None),
            'ray': as_dict.get('ray', None),
            'rectangle': as_dict.get('rectangle', None),
            'save_chart': as_dict.get('saveChart', None),
            'segment': as_dict.get('segment', None),
            'simple_shapes': as_dict.get('simpleShapes', None),
            'time_cycles': as_dict.get('timeCycles', None),
            'toggle_annotations': as_dict.get('toggleAnnotations', None),
            'type_candlestick': as_dict.get('typeCandlestick', None),
            'type_change': as_dict.get('typeChange', None),
            'type_heikin_ashi': as_dict.get('typeHeikinAshi', None),
            'type_hlc': as_dict.get('typeHLC', None),
            'type_hollow_candlestick': as_dict.get('typeHollowCandlestick', None),
            'type_line': as_dict.get('typeLine', None),
            'type_ohlc': as_dict.get('typeOHLC', None),
            'vertical_arrow': as_dict.get('verticalArrow', None),
            'vertical_counter': as_dict.get('verticalCounter', None),
            'vertical_label': as_dict.get('verticalLabel', None),
            'vertical_labels': as_dict.get('verticalLabels', None),
            'vertical_line': as_dict.get('verticalLine', None),
            'zoom_change': as_dict.get('zoomChange', None),
            'zoom_x': as_dict.get('zoomX', None),
            'zoom_xy': as_dict.get('zoomXY', None),
            'zoom_y': as_dict.get('zoomY', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'advanced': self.advanced,
            'arrowInfinityLine': self.arrow_infinity_line,
            'arrowRay': self.arrow_ray,
            'arrowSegment': self.arrow_segment,
            'circle': self.circle,
            'crooked3': self.crooked3,
            'crooked5': self.crooked5,
            'crookedLines': self.crooked_lines,
            'currentPriceIndicator': self.current_price_indicator,
            'elliott3': self.elliott3,
            'elliott5': self.elliott5,
            'ellipse': self.ellipse,
            'fibonacci': self.fibonacci,
            'fibonacciTimeZones': self.fibonacci_time_zones,
            'flagCirclepin': self.flag_circlepin,
            'flagDiamondpin': self.flag_diamondpin,
            'flags': self.flags,
            'flagSimplepin': self.flag_simplepin,
            'flagSquarepin': self.flag_squarepin,
            'fullscreen': self.fullscreen,
            'horizontalLine': self.horizontal_line,
            'indicators': self.indicators,
            'infinityLine': self.infinity_line,
            'label': self.label,
            'line': self.line,
            'lines': self.lines,
            'measure': self.measure,
            'measureX': self.measure_x,
            'measureXY': self.measure_xy,
            'measureY': self.measure_y,
            'parallelChannel': self.parallel_channel,
            'pitchfork': self.pitchfork,
            'ray': self.ray,
            'rectangle': self.rectangle,
            'saveChart': self.save_chart,
            'segment': self.segment,
            'simpleShapes': self.simple_shapes,
            'timeCycles': self.time_cycles,
            'toggleAnnotations': self.toggle_annotations,
            'typeCandlestick': self.type_candlestick,
            'typeChange': self.type_change,
            'typeHeikinAshi': self.type_heikin_ashi,
            'typeHLC': self.type_hlc,
            'typeHollowCandlestick': self.type_hollow_candlestick,
            'typeLine': self.type_line,
            'typeOHLC': self.type_ohlc,
            'verticalArrow': self.vertical_arrow,
            'verticalCounter': self.vertical_counter,
            'verticalLabel': self.vertical_label,
            'verticalLabels': self.vertical_labels,
            'verticalLine': self.vertical_line,
            'zoomChange': self.zoom_change,
            'zoomX': self.zoom_x,
            'zoomXY': self.zoom_xy,
            'zoomY': self.zoom_y,
        }

        return untrimmed


class StockToolsLanguageOptions(HighchartsMeta):
    """Language settings for the :term:`stock tools`."""

    def __init__(self, **kwargs):
        self._gui = None

        self.gui = kwargs.get('gui', None)

    @property
    def gui(self) -> Optional[StockToolsGUI]:
        """Language settings for the :term:`stock tools`.

        :rtype: :class:`StockToolsGUI <highcharts_stock.global_options.language.stock_tools.StockToolsGUI>`
          or :obj:`None <python:None>`
        """
        return self._gui

    @gui.setter
    @class_sensitive(StockToolsGUI)
    def gui(self, value):
        self._gui = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'gui': as_dict.get('gui', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'gui': self.gui,
        }

        return untrimmed

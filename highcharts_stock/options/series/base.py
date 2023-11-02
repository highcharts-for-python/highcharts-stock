from typing import Optional
from decimal import Decimal

from validator_collection import validators

from highcharts_core.options.series.base import SeriesBase as OriginalSeriesBase

from highcharts_stock import errors
from highcharts_stock.decorators import validate_types
from highcharts_stock.utility_functions import mro__to_untrimmed_dict
from highcharts_stock.options.plot_options.series import SeriesOptions
from highcharts_stock.options.plot_options.base import NavigatorIndicatorOptions


class IndicatorFactoryMixin(object):
    """Mix-in used to add the ``.add_indicator()`` and ``.get_indicator()`` methods to
    series object."""

    def add_indicator(self, chart, indicator_name, indicator_kwargs = None):
        """Adds a :term:`technical indicator` linked to the current series to the
        ``chart``.

        :param chart: The chart object in which the series is rendered and to which the
          indicator should be appended.

          .. warning::

            If ``chart`` already contains a series with the same
            :meth:`.id <highcharts_stock.options.series.base.SeriesBase.id>` as ``self``,
            that series in ``chart`` will be *replaced* by ``self``.

        :type chart: :class:`Chart <highcharts_stock.chart.Chart>`

        :param indicator_name: The name of the indicator that should be added to the
          series and chart. For the list of supported indicators, please review the
          :ref:`Indicator List <indicator_list>`.
        :type indicator_name: :class:`str <python:str>`

        :param indicator_kwargs: Keyword arguments to apply when instantiating the new
          indicator series. Defaults to :obj:`None <python:None>`.
        :type indicator_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`

        :returns: ``chart`` with a new indicator series included in its list of configured
          series.
        :rtype: :class:`Chart <highcharts_stock.chart.Chart>`
        """
        from highcharts_stock.chart import Chart
        from highcharts_stock.options import HighchartsStockOptions

        if not self.id:
            raise errors.HighchartsValueError('series does not have an .id '
                                              'specified. Cannot add an '
                                              'indicator.')

        chart = validate_types(chart, Chart)
        if chart.options and chart.options.series:
            series_list = [x for x in chart.options.series
                           if x.id != self.id]
        elif chart.options:
            series_list = []
        else:
            chart.options = HighchartsStockOptions()
            series_list = []

        indicator = self.get_indicator(indicator_name,
                                       indicator_kwargs = indicator_kwargs)
        series_list.append(self)
        series_list.append(indicator)

        chart.options.series = series_list

        return chart

    def get_indicator(self, indicator_name, indicator_kwargs = None):
        """Retrieve a :term:`technical indicator` :term:`series` instance linked to the
        current series.

        :param indicator_name: The name of the indicator that should be added to the
          series and chart. For the list of supported indicators, please review the
          :ref:`Indicator List <technical_indicators>`.
          
          .. note::
          
            ``indicator_name`` is case-insensitive, and you can use either:
            
              * the full indicator name as provided in the 
                :ref:`Indicator List <technical_indicators>`, or
              * the abbreviated form that precedes ``Series`` in the series class name

        :type indicator_name: :class:`str <python:str>`

        :param indicator_kwargs: Keyword arguments to apply when instantiating the new
          indicator series. Defaults to :obj:`None <python:None>`.
        :type indicator_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`

        :returns: The :term:`technical indicator` series instance
        :rtype: :class:`IndicatorSeriesBase <highcharts_stock.options.series.base.IndicatorSeriesBase>`
          descendant corresponding to ``indicator_name``
        """
        from highcharts_stock.options.series.series_generator import INDICATOR_LIST

        if not self.id:
            raise errors.HighchartsValueError('series does not have an .id '
                                              'specified. Cannot add an '
                                              'indicator.')

        indicator_name = validators.string(indicator_name, allow_empty = False)
        indicator_name = indicator_name.lower()
        if indicator_name not in INDICATOR_LIST:
            raise errors.HighchartsValueError(f'indicator_name expects a valid '
                                              f'indicator name. Did not recognize: '
                                              f'"{indicator_name}"')

        indicator_kwargs = validators.dict(indicator_kwargs, allow_empty = True) or {}

        indicator_cls = INDICATOR_LIST.get(indicator_name)
        indicator = indicator_cls(**indicator_kwargs)
        indicator.linked_to = self.id

        return indicator


class SeriesBase(OriginalSeriesBase, IndicatorFactoryMixin):
    """Generic base class for specific series configurations."""

    def convert_to(self, series_type):
        """Creates a new series of ``series_type`` from the current series.
        
        :param series_type: The series type that should be returned.
        :type series_type: :class:`str <python:str>` or
          :class:`SeriesBase <highcharts_core.options.series.base.SeriesBase>`-descended
          
        .. warning::
        
          This operation is *not* guaranteed to work converting between all series 
          types. This is because some series types have different properties, different
          logic / functionality for their properties, and may have entirely different
          data requirements.
          
          In general, this method is expected to be *lossy* in nature, meaning that when
          the series can be converted "close enough" the series will be converted. 
          However, if the target ``series_type`` does not support certain properties set
          on the original instance, then those settings will *not* be propagated to the 
          new series.
          
          In certain cases, this method may raise an 
          :exc:`HighchartsSeriesConversionError <highcharts_core.errors.HighchartsSeriesConversionError>`
          if the method is unable to convert (even losing some data) the original into 
          ``series_type``.
        
        :returns: A new series of ``series_type``, maintaining relevant properties and
          data from the original instance.
        :rtype: ``series_type``
          :class:`SeriesBase <highcharts_core.options.series.base.SeriesBase>` descendant
          
        :raises HighchartsSeriesConversionError: if unable to convert (even after losing 
          some data) the original instance into an instance of ``series_type``.
        :raises HighchartsValueError: if ``series_type`` is not a recognized series type

        """
        from highcharts_stock.options.series.series_generator import SERIES_CLASSES
        if isinstance(series_type, str):
            series_type = series_type.lower()
            if series_type not in SERIES_CLASSES:
                raise errors.HighchartsValueError(f'series_type expects a valid Highcharts '
                                                  f'series type. Received: {series_type}')
            series_type_name = series_type
            series_type = SERIES_CLASSES.get(series_type)
        elif not issubclass(series_type, OriginalSeriesBase):
            raise errors.HighchartsValueError(f'series_type expects a valid Highcharts '
                                              f'series type. Received: {series_type}')
        else:
            series_type_name = series_type.__name__

        as_js_literal = self.to_js_literal()
        try:
            target = series_type.from_js_literal(as_js_literal)
        except (ValueError, TypeError):
            raise errors.HighchartsSeriesConversionError(f'Unable to convert '
                                                         f'{self.__class__.__name__} instance '
                                                         f'to {series_type_name}')
        
        return target


class IndicatorSeriesBase(SeriesOptions, IndicatorFactoryMixin):
    """Generic base class for specific :term:`technical indicator` series
    configurations."""

    def __init__(self, **kwargs):
        self._id = None
        self._index = None
        self._legend_index = None
        self._name = None
        self._stack = None
        self._x_axis = None
        self._y_axis = None
        self._z_index = None

        self.id = kwargs.get('id', None)
        self.index = kwargs.get('index', None)
        self.legend_index = kwargs.get('legend_index', None)
        self.name = kwargs.get('name', None)
        self.stack = kwargs.get('stack', None)
        self.x_axis = kwargs.get('x_axis', None)
        self.y_axis = kwargs.get('y_axis', None)
        self.z_index = kwargs.get('z_index', None)

        super().__init__(**kwargs)

    @property
    def _dot_path(self) -> Optional[str]:
        """The dot-notation path to the options key for the current class.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return f'series.{self.type}'

    @property
    def id(self) -> Optional[str]:
        """An id for the series. Defaults to :obj:`None <python:None>`.

        .. hint::

          This can be used (in JavaScript) after render time to get a pointer to the
          series object through ``chart.get()``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._id

    @id.setter
    def id(self, value):
        self._id = validators.string(value, allow_empty = True)

    @property
    def index(self) -> Optional[int]:
        """The index for the series in the chart, affecting the internal index in the
        (JavaScript) ``chart.series`` array, the visible Z-index, and the order of the
        series in the legend. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._index

    @index.setter
    def index(self, value):
        self._index = validators.integer(value,
                                         allow_empty = True,
                                         minimum = 0)

    @property
    def legend_index(self) -> Optional[int]:
        """The sequential index for the series in the legend. Defaults to
        :obj:`None <python:None>`.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._legend_index

    @legend_index.setter
    def legend_index(self, value):
        self._legend_index = validators.integer(value,
                                                allow_empty = True,
                                                minimum = 0)

    @property
    def name(self) -> Optional[str]:
        """The name of the series as shown in the legend, tooltip, etc. Defaults to
        :obj:`None <python:None>`.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._name

    @name.setter
    def name(self, value):
        self._name = validators.string(value, allow_empty = True)

    @property
    def stack(self) -> Optional[str]:
        """Indicates the "stack" into which the series should be grouped, if the chart
        groups series into stacks. Defaults to :obj:`None <python:None>`.

        .. note::

          The value can be a string or a numeric value, provided that series in the same
          stack all have the same value when converted to a string. For ease of ues,
          Highcharts for Python will attempt to force the conversion of the relevant value
          to a string.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._stack

    @stack.setter
    def stack(self, value):
        if not value:
            self._stack = None
        else:
            self._stack = validators.string(value,
                                            coerce_value = True)

    @property
    def x_axis(self) -> Optional[str | int]:
        """When using multiple X-axes, this setting determines on which axis the series
        should be drawn. Its value should be either a numerical index position in the
        :meth:`Options.x_axis` array (starting at 0), or a :class:`str <python:str>`
        indicating the :meth:`id <XAxis.id>` of the axis to which the series should be
        connected. Defaults to :obj:`None <python:None>`, which behaves as if the value
        were set to ``0``.

        :rtype: :class:`str <python:str>`, :class:`int <python:int>`, or
          :obj:`None <python:None>`
        """
        return self._x_axis

    @x_axis.setter
    def x_axis(self, value):
        if value is None:
            self._x_axis = None
        else:
            try:
                value = validators.integer(value, minimum = 0)
            except (ValueError, TypeError):
                value = validators.string(value)

            self._x_axis = value

    @property
    def y_axis(self) -> Optional[str | int]:
        """When using multiple Y-axes, this setting determines on which axis the series
        should be drawn. Its value should be either a numerical index position in the
        :meth:`Options.y_axis` array (starting at 0), or a :class:`str <python:str>`
        indicating the :meth:`id <YAxis.id>` of the axis to which the series should be
        connected. Defaults to :obj:`None <python:None>`, which behaves as if the value
        were set to ``0``.

        :rtype: :class:`str <python:str>`, :class:`int <python:int>`, or
          :obj:`None <python:None>`
        """
        return self._y_axis

    @y_axis.setter
    def y_axis(self, value):
        if value is None:
            self._y_axis = None
        else:
            try:
                value = validators.integer(value, minimum = 0)
            except (ValueError, TypeError):
                value = validators.string(value)

            self._y_axis = value

    @property
    def z_index(self) -> Optional[int | float | Decimal]:
        """The visual z-index of the series. Defaults to :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._z_index

    @z_index.setter
    def z_index(self, value):
        if value is None:
            self._z_index = None
        else:
            self._z_index = validators.numeric(value)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'accessibility': as_dict.get('accessibility', None),
            'allow_point_select': as_dict.get('allowPointSelect', None),
            'animation': as_dict.get('animation', None),
            'class_name': as_dict.get('className', None),
            'clip': as_dict.get('clip', None),
            'color': as_dict.get('color', None),
            'cursor': as_dict.get('cursor', None),
            'custom': as_dict.get('custom', None),
            'dash_style': as_dict.get('dashStyle', None),
            'data_labels': as_dict.get('dataLabels', None),
            'description': as_dict.get('description', None),
            'enable_mouse_tracking': as_dict.get('enableMouseTracking', None),
            'events': as_dict.get('events', None),
            'include_in_data_export': as_dict.get('includeInDataExport', None),
            'keys': as_dict.get('keys', None),
            'label': as_dict.get('label', None),
            'legend_symbol': as_dict.get('legendSymbol', None),
            'linked_to': as_dict.get('linkedTo', None),
            'marker': as_dict.get('marker', None),
            'on_point': as_dict.get('onPoint', None),
            'opacity': as_dict.get('opacity', None),
            'point': as_dict.get('point', None),
            'point_description_formatter': as_dict.get('pointDescriptionFormatter', None),
            'selected': as_dict.get('selected', None),
            'show_checkbox': as_dict.get('showCheckbox', None),
            'show_in_legend': as_dict.get('showInLegend', None),
            'skip_keyboard_navigation': as_dict.get('skipKeyboardNavigation', None),
            'sonification': as_dict.get('sonification', None),
            'states': as_dict.get('states', None),
            'sticky_tracking': as_dict.get('stickyTracking', None),
            'threshold': as_dict.get('threshold', None),
            'tooltip': as_dict.get('tooltip', None),
            'turbo_threshold': as_dict.get('turboThreshold', None),
            'visible': as_dict.get('visible', None),

            'animation_limit': as_dict.get('animationLimit', None),
            'boost_blending': as_dict.get('boostBlending', None),
            'boost_threshold': as_dict.get('boostThreshold', None),
            'color_axis': as_dict.get('colorAxis', None),
            'color_index': as_dict.get('colorIndex', None),
            'color_key': as_dict.get('colorKey', None),
            'connect_ends': as_dict.get('connectEnds', None),
            'connect_nulls': as_dict.get('connectNulls', None),
            'crisp': as_dict.get('crisp', None),
            'crop_threshold': as_dict.get('cropThreshold', None),
            'data_sorting': as_dict.get('dataSorting', None),
            'drag_drop': as_dict.get('dragDrop', None),
            'find_nearest_point_by': as_dict.get('findNearestPointBy', None),
            'get_extremes_from_all': as_dict.get('getExtremesFromAll', None),
            'inactive_other_points': as_dict.get('inactiveOtherPoints', None),
            'linecap': as_dict.get('linecap', None),
            'line_width': as_dict.get('lineWidth', None),
            'negative_color': as_dict.get('negativeColor', None),
            'point_description_format': as_dict.get('pointDescriptionFormat', None),
            'point_interval': as_dict.get('pointInterval', None),
            'point_interval_unit': as_dict.get('pointIntervalUnit', None),
            'point_placement': as_dict.get('pointPlacement', None),
            'point_start': as_dict.get('pointStart', None),
            'relative_x_value': as_dict.get('relativeXValue', None),
            'shadow': as_dict.get('shadow', None),
            'soft_threshold': as_dict.get('softThreshold', None),
            'stacking': as_dict.get('stacking', None),
            'step': as_dict.get('step', None),
            'zone_axis': as_dict.get('zoneAxis', None),
            'zones': as_dict.get('zones', None),

            'id': as_dict.get('id', None),
            'index': as_dict.get('index', None),
            'legend_index': as_dict.get('legendIndex', None),
            'name': as_dict.get('name', None),
            'stack': as_dict.get('stack', None),
            'x_axis': as_dict.get('xAxis', None),
            'y_axis': as_dict.get('yAxis', None),
            'z_index': as_dict.get('zIndex', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'id': self.id,
            'index': self.index,
            'legendIndex': self.legend_index,
            'name': self.name,
            'stack': self.stack,
            'xAxis': self.x_axis,
            'yAxis': self.y_axis,
            'zIndex': self.z_index,
        }
        parent_as_dict = mro__to_untrimmed_dict(self, in_cls = in_cls) or {}

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed


class NavigatorIndicatorSeries(IndicatorSeriesBase, NavigatorIndicatorOptions):
    """Set of options to mix in when an indicator supports a presence in the Navigator."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'accessibility': as_dict.get('accessibility', None),
            'allow_point_select': as_dict.get('allowPointSelect', None),
            'animation': as_dict.get('animation', None),
            'class_name': as_dict.get('className', None),
            'clip': as_dict.get('clip', None),
            'color': as_dict.get('color', None),
            'cursor': as_dict.get('cursor', None),
            'custom': as_dict.get('custom', None),
            'dash_style': as_dict.get('dashStyle', None),
            'data_labels': as_dict.get('dataLabels', None),
            'description': as_dict.get('description', None),
            'enable_mouse_tracking': as_dict.get('enableMouseTracking', None),
            'events': as_dict.get('events', None),
            'include_in_data_export': as_dict.get('includeInDataExport', None),
            'keys': as_dict.get('keys', None),
            'label': as_dict.get('label', None),
            'legend_symbol': as_dict.get('legendSymbol', None),
            'linked_to': as_dict.get('linkedTo', None),
            'marker': as_dict.get('marker', None),
            'on_point': as_dict.get('onPoint', None),
            'opacity': as_dict.get('opacity', None),
            'point': as_dict.get('point', None),
            'point_description_formatter': as_dict.get('pointDescriptionFormatter', None),
            'selected': as_dict.get('selected', None),
            'show_checkbox': as_dict.get('showCheckbox', None),
            'show_in_legend': as_dict.get('showInLegend', None),
            'skip_keyboard_navigation': as_dict.get('skipKeyboardNavigation', None),
            'sonification': as_dict.get('sonification', None),
            'states': as_dict.get('states', None),
            'sticky_tracking': as_dict.get('stickyTracking', None),
            'threshold': as_dict.get('threshold', None),
            'tooltip': as_dict.get('tooltip', None),
            'turbo_threshold': as_dict.get('turboThreshold', None),
            'visible': as_dict.get('visible', None),

            'animation_limit': as_dict.get('animationLimit', None),
            'boost_blending': as_dict.get('boostBlending', None),
            'boost_threshold': as_dict.get('boostThreshold', None),
            'color_axis': as_dict.get('colorAxis', None),
            'color_index': as_dict.get('colorIndex', None),
            'color_key': as_dict.get('colorKey', None),
            'connect_ends': as_dict.get('connectEnds', None),
            'connect_nulls': as_dict.get('connectNulls', None),
            'crisp': as_dict.get('crisp', None),
            'crop_threshold': as_dict.get('cropThreshold', None),
            'data_sorting': as_dict.get('dataSorting', None),
            'drag_drop': as_dict.get('dragDrop', None),
            'find_nearest_point_by': as_dict.get('findNearestPointBy', None),
            'get_extremes_from_all': as_dict.get('getExtremesFromAll', None),
            'inactive_other_points': as_dict.get('inactiveOtherPoints', None),
            'linecap': as_dict.get('linecap', None),
            'line_width': as_dict.get('lineWidth', None),
            'negative_color': as_dict.get('negativeColor', None),
            'point_description_format': as_dict.get('pointDescriptionFormat', None),
            'point_interval': as_dict.get('pointInterval', None),
            'point_interval_unit': as_dict.get('pointIntervalUnit', None),
            'point_placement': as_dict.get('pointPlacement', None),
            'point_start': as_dict.get('pointStart', None),
            'relative_x_value': as_dict.get('relativeXValue', None),
            'shadow': as_dict.get('shadow', None),
            'soft_threshold': as_dict.get('softThreshold', None),
            'stacking': as_dict.get('stacking', None),
            'step': as_dict.get('step', None),
            'zone_axis': as_dict.get('zoneAxis', None),
            'zones': as_dict.get('zones', None),

            'id': as_dict.get('id', None),
            'index': as_dict.get('index', None),
            'legend_index': as_dict.get('legendIndex', None),
            'name': as_dict.get('name', None),
            'stack': as_dict.get('stack', None),
            'x_axis': as_dict.get('xAxis', None),
            'y_axis': as_dict.get('yAxis', None),
            'z_index': as_dict.get('zIndex', None),

            'navigator_options': as_dict.get('navigatorOptions', None),
            'show_in_navigator': as_dict.get('showInNavigator', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = mro__to_untrimmed_dict(self, in_cls = in_cls) or {}

        return untrimmed

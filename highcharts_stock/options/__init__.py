"""Implements the :class:`HighchartsOptions` class."""
from typing import Optional, List

from validator_collection import validators

from highcharts_python import utility_functions
from highcharts_python.metaclasses import HighchartsMeta
from highcharts_python.decorators import class_sensitive
from highcharts_python.utility_classes.gradients import Gradient
from highcharts_python.utility_classes.patterns import Pattern
from highcharts_python.options.series.series_generator import create_series_obj

from highcharts_python.options.accessibility import Accessibility
from highcharts_python.options.annotations import Annotation
from highcharts_python.options.boost import Boost
from highcharts_python.options.caption import Caption
from highcharts_python.options.chart import ChartOptions
from highcharts_python.options.axes.color_axis import ColorAxis
from highcharts_python.options.credits import Credits
from highcharts_python.options.data import Data
from highcharts_python.options.defs import MarkerDefinition
from highcharts_python.options.drilldown import Drilldown
from highcharts_python.options.exporting import Exporting
from highcharts_python.global_options.language import Language
from highcharts_python.options.legend import Legend
from highcharts_python.options.loading import Loading
from highcharts_python.options.navigation import Navigation
from highcharts_python.options.no_data import NoData
from highcharts_python.options.pane import Pane
from highcharts_python.options.plot_options import PlotOptions
from highcharts_python.options.plot_options.generic import GenericTypeOptions
from highcharts_python.options.responsive import Responsive
from highcharts_python.options.subtitle import Subtitle
from highcharts_python.options.time import Time
from highcharts_python.options.title import Title
from highcharts_python.options.tooltips import Tooltip
from highcharts_python.options.axes.x_axis import XAxis
from highcharts_python.options.axes.y_axis import YAxis
from highcharts_python.options.axes.z_axis import ZAxis

# Highcharts Stock Classes
from highcharts_python.options.navigator import Navigator
from highcharts_python.range_selector import RangeSelector
from highcharts_python.scrollbar import Scrollbar
from highcharts_python.stock_tools import StockTools

# Highcharts Maps Classes
from highcharts_python.options.map_navigation import MapNavigation
from highcharts_python.options.map_view import MapView


class HighchartsStockOptions(HighchartsOptions):
    """The Python representation of the
    `Highcharts Stock <https://api.highcharts.com/highstock/>`_ configuration object."""

    def __init__(self, **kwargs):
        self._boost = None
        self._navigator = None
        self._no_data = None
        self._range_selector = None
        self._scrollbar = None
        self._stock_tools = None

        self.boost = kwargs.get('boost', None)
        self.navigator = kwargs.get('navigator', None)
        self.no_data = kwargs.get('no_data', None)
        self.range_selector = kwargs.get('range_selector', None)
        self.scrollbar = kwargs.get('scrollbar', None)
        self.stock_tools = kwargs.get('stock_tools', None)

        super().__init__(**kwargs)

    @property
    def boost(self) -> Optional[Boost]:
        """Options for the Boost module.

        The Boost module allows certain series types to be rendered by WebGL instead of
        the default SVG. This allows hundreds of thousands of data points to be rendered
        in milliseconds. In addition to the WebGL rendering it saves time by skipping
        processing and inspection of the data wherever possible.

        .. warning::

          This introduces some limitations to what features are available in boost mode.
          See
          `the docs <https://www.highcharts.com/docs/advanced-chart-features/boost-module>`_
          for details.

        .. note:

          In addition to the global boost option, each series has a ``boostThreshold``
          that defines when the boost should kick in.

        :returns: The :class:`Boost <Boost>` object.
        :rtype: :class:`Boost <highcharts.boost.Boost>`

        """
        return self._boost

    @boost.setter
    @class_sensitive(Boost)
    def boost(self, value):
        self._boost = value

    @property
    def navigator(self) -> Optional[Navigator]:
        """The navigator is a small series below the main series, displaying a view of the
        entire data set. It provides tools to zoom in and out on parts of the data as well
        as panning across the dataset.

        :returns: Configuration instructions for the :class:`Navigator` functionality.
        :rtype: :class:`Navigator` or :obj:`None <python:None>`
        """
        return self._navigator

    @navigator.setter
    @class_sensitive(Navigator)
    def navigator(self, value):
        self._navigator = value

    @property
    def no_data(self) -> Optional[NoData]:
        """Options for displaying a message like "No data to display".

        .. warning::

          This feature requires the file ``no-data-to-display.js`` to be loaded in the
          page.

        .. tip::

          The actual text to display is set in the :meth:`language <Options.language>`
          options.

        :returns: Configuration of how to display a no data message.
        :rtype: :class:`NoData` or :obj:`None <python:None>`
        """
        return self._no_data

    @no_data.setter
    @class_sensitive(NoData)
    def no_data(self, value):
        self._no_data = value

    @property
    def range_selector(self) -> Optional[RangeSelector]:
        """The range selector is a tool for selecting ranges to display within the chart.
        It provides buttons to select preconfigured ranges in the chart, like 1 day, 1
        week, 1 month etc. It also provides input boxes where min and max dates can be
        manually input.

        :returns: Configuration instructions for the Range Selector functionality.
        :rtype: :class:`RangeSelector` or :obj:`None <python:None>`
        """
        return self._range_selector

    @range_selector.setter
    @class_sensitive(RangeSelector)
    def range_selector(self, value):
        self._range_selector = value

    @property
    def scrollbar(self) -> Optional[Scrollbar]:
        """The scrollbar is a means of panning over the X axis of a stock chart.

        .. note::

          Scrollbars can also be applied to other types of axes.

        .. note::

          Another approach to scrollable charts is the :meth:`Chart.scrollable_plot_area`
          option that is especially suitable for simpler cartesian charts on mobile.

        In styled mode, all the presentational options for the scrollbar are replaced by
        the classes ``.highcharts-scrollbar-thumb``, ``.highcharts-scrollbar-arrow``,
        ``.highcharts-scrollbar-button``, ``.highcharts-scrollbar-rifles`` and
        ``.highcharts-scrollbar-track``.

        :returns: The configuration options for the Scrollbar functionality.
        :rtype: :class:`Scrollbar` or :obj:`None <python:None>`
        """
        return self._scrollbar

    @scrollbar.setter
    @class_sensitive(Scrollbar)
    def scrollbar(self, value):
        self._scrollbar = value

    @property
    def stock_tools(self) -> Optional[StockTools]:
        """Configure the **stockTools** GUI strings in the chart.

        .. warning::

          Requires the `stockTools module <https://api.highcharts.com/highstock/>`_` to be
          loaded in the client/browser.

        .. seealso::

          For a description of the module and information on its features, see
          `Highcharts StockTools <https://api.highcharts.com/highstock/>`_.

        :returns: The configuration options for the StockTools functionality.
        :rtype: :class:`StockTools` or :obj:`None <python:None>`
        """
        return self._stock_tools

    @stock_tools.setter
    @class_sensitive(StockTools)
    def stock_tools(self, value):
        self._stock_tools = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        as_dict = validators.dict(as_dict, allow_empty = True) or {}
        kwargs_dict = {
            'accessibility': as_dict.get('accessibility', None),
            'annotations': as_dict.get('annotations', None),
            'boost': as_dict.get('boost', None),
            'caption': as_dict.get('caption', None),
            'chart': as_dict.get('chart', None),
            'color_axis': as_dict.get('colorAxis', None),
            'colors': as_dict.get('colors', None),
            'credits': as_dict.get('credits', None),
            'data': as_dict.get('data', None),
            'defs': as_dict.get('defs', None),
            'exporting': as_dict.get('exporting', None),
            'language': as_dict.get('lang', None),
            'legend': as_dict.get('legend', None),
            'loading': as_dict.get('loading', None),
            'navigation': as_dict.get('navigation', None),
            'navigator': as_dict.get('navigator', None),
            'no_data': as_dict.get('noData', None),
            'plot_options': as_dict.get('plotOptions', None),
            'range_selector': as_dict.get('rangeSelector', None),
            'responsive': as_dict.get('responsive', None),
            'scrollbar': as_dict.get('scrollbar', None),
            'series': as_dict.get('series', None),
            'stock_tools': as_dict.get('stockTools', None),
            'subtitle': as_dict.get('subtitle', None),
            'time': as_dict.get('time', None),
            'title': as_dict.get('title', None),
            'tooltip': as_dict.get('tooltip', None),
            'x_axis': as_dict.get('xAxis', None),
            'y_axis': as_dict.get('yAxis', None)
        }

        return cls(**kwargs_dict)

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'accessibility': self.accessibility,
            'annotations': self.annotations,
            'boost': self.boost,
            'caption': self.caption,
            'chart': self.chart,
            'colorAxis': self.color_axis,
            'colors': self.colors,
            'credits': self.credits,
            'data': self.data,
            'defs': self.defs,
            'exporting': self.exporting,
            'lang': self.language,
            'legend': self.legend,
            'loading': self.loading,
            'navigation': self.navigation,
            'navigator': self.navigator,
            'noData': self.no_data,
            'plotOptions': self.plot_options,
            'rangeSelector': self.range_selector,
            'responsive': self.responsive,
            'scrollbar': self.scrollbar,
            'series': self.series,
            'stockTools': self.stock_tools,
            'subtitle': self.subtitle,
            'time': self.time,
            'title': self.title,
            'tooltip': self.tooltip,
            'xAxis': self.x_axis,
            'yAxis': self.y_axis,
        }

        return untrimmed

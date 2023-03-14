
The structure of the **Highcharts Stock for Python** library closely matches the structure
of the `Highcharts Stock <https://www.highcharts.com/products/stock/>`__ options object (see the relevant
`reference documentation <https://api.highcharts.com/highstock/>`_).

At the root of the library - importable from ``highcharts_stock`` - you will find the
:mod:`highcharts_stock.highcharts` module. This module is a catch-all importable module,
which allows you to easily access the most-commonly-used Highcharts Stock for Python
classes and modules.

.. note::

  Whlie you can access all of the **Highcharts Stock for Python** classes from
  ``highcharts_stock.highcharts``, if you want to more precisely navigate to specific
  class definitions you can do fairly easily using the module organization and naming
  conventions used in the library.

  In the root of the ``highcharts_stock`` library you can find universally-shared
  class definitions, like :mod:`.metaclasses <highcharts_stock.metaclasses>` which
  contains the :class:`HighchartsMeta <highcharts_stock.metaclasses.HighchartsMeta>`
  and :class:`JavaScriptDict <highcharts_stock.metaclasses.JavaScriptDict>`
  definitions, or :mod:`.decorators <highcharts_stock.decorators>` which define
  method/property decorators that are used throughout the library.

  The :mod:`.utility_classes <highcharts_stock.utility_classes>` module contains class
  definitions for classes that are referenced or used throughout the other class
  definitions.

  And you can find the Highcharts Stock ``options`` object and all of its
  properties defined in the :mod:`.options <highcharts_stock.options>` module, with
  specific (complicated or extensive) sub-modules providing property-specific classes
  (e.g. the :mod:`.options.plot_options <highcharts_stock.options.plot_options>`
  module defines all of the different configuration options for different series types,
  while the :mod:`.options.series <highcharts_stock.options.series>` module defines all
  of the classes that represent :term:`series` of data in a given chart).

.. tip::

  To keep things simple, we recommend importing classes you need directly from the
  :mod:`highcharts_stock.highcharts` module. There are two paths to do so easily:

  .. code-block:: python

    # APPROACH #1: Import the highcharts module, and access its child classes directly.
    #              for example by now calling highcharts.Chart().
    from highcharts_core import highcharts

    my_chart = highcharts.Chart()
    my_shared_options = highcharts.SharedStockOptions()

    my_line_series = highcharts.options.series.area.LineSeries()

    # APPROACH #2: Import a specific class or module by name from the "highcharts" module.
    from highcharts_stock.highcharts import Chart, SharedStockOptions, options

    my_chart = Chart()
    my_shared_options = SharedStockOptions()
    my_line_series = options.series.area.LineSeries()

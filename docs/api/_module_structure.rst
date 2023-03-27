
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
  
  *This is the recommended best practice to maximize performance*.

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
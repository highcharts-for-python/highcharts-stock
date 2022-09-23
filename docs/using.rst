#####################################
Using Highcharts Stock for Python
#####################################

.. contents::
  :depth: 3
  :backlinks: entry

--------------

*******************************************************************
Introduction to Highcharts Stock and Highcharts stock for Python
*******************************************************************

.. sidebar:: The Highcharts for Python Toolkit

  The **Highcharts Stock for Python** library is part of the broader
  `Highcharts for Python <https://highcharts-python.readthedocs.io/>`_ toolkit. The core
  library provides Python wrappers for
  `Highcharts JS <https://www.highcharts.com/products/highcharts/>`__, while
  **Highcharts Stock for Python** extends the core library with support for
  `Highcharts Stock <https://www.highcharts.com/products/stock>`__ in the same way that
  Highcharts Stock extends Highcharts JS.

  .. note::

    **Highcharts Stock for Python** is an *additive* extension to
    **Highcharts for Python**. This means that it includes the full set of functionality
    from Highcharts for Python, is fully bakcwards-compatible with Highcharts for Python,
    and exposes the exact same API for you to use. This makes it easy to for you to
    combine visualization from the core
    `Highcharts JS <https://www.highcharts.com/products/highcharts/>`__ library *and* the
    `Highcharts Stock <https://www.highcharts.com/products/stock/>`_ library without
    wrangling multiple similar dependencies in your Python code.

`Highcharts Stock <https://www.highcharts.com/products/stock/>`__  is the gold-standard
in JavaScript data visualization libraries for time-series and stock price data,
enabling you to design rich, beautiful, and highly interactive data visualizations of
(almost) any kind imaginable, and to render those visualizations in your web or mobile
applications. Take a look at some of their
`customer showcases <https://www.highcharts.com/blog/posts/highcharts-stock+use-cases/>`_
and their own `demo gallery <https://www.highcharts.com/products/stock/demo>`_ to see what
you can do with Highcharts Stock.

**Highcharts Stock for Python** is a Python wrapper for the
`Highcharts Stock <https://www.highcharts.com/products/stock/>`__ JavaScript library,
which means that it is designed to give developers working in Python a simple and Pythonic
way of interacting with Highcharts Stock. Highcharts Stock for Python will *not* render
data visualizations itself - that's what Highcharts Stock does - but it *will* allow you
to:

  #. Configure your data visualizations in Python.
  #. Supply data you have in Python to your data visualizations.
  #. Programmatically produce the Highcharts Stock JavaScript code that will actually
     render your data visualization.
  #. Programmatically download a static version of your visualization (as needed) within
     Python.

.. tip::

  Think of **Highcharts Stock for Python** as a translator to bridge your data
  visualization needs between Python and JavaScript.

-------------------

*****************************************************
Key Design Patterns in Highcharts Stock for Python
*****************************************************

`Highcharts JS <https://www.highcharts.com>`__ is a large, robust, and complicated
JavaScript library. If in doubt, take a look at their extensive
`documentation <https://www.highcharts.com/docs/index>`_ and in
particular their `API reference`_. Because **Highcharts for Python** and
**Highcharts Stock for Python** wrap the Highcharts API, their design is heavily shaped by
Highcharts JS' own design - as one should expect.

However, one of the main goals of the **Highcharts for Python** toolkit is to make the
Highcharts JS library a little more Pythonic in terms of its design to make it easier for
Python developers to leverage it. Here are the notable design patterns that have been
adopted that you should be aware of:

Code Style: Python vs JavaScript Naming Conventions
=======================================================

.. include:: using/_code_style_naming_conventions.rst

Standard Methods
=======================================

Every single object supported by the Highcharts Stock API corresponds to a Python class in
**Highcharts Stock for Python**. You can find the complete list in our comprehensive
:doc:`Highcharts Stock for Python API Reference <api>`.

These classes generally inherit from the
:class:`HighchartsMeta <highcharts_stock.metaclasses.HighchartsMeta>` metaclass, which
provides each class with a number of standard methods. These methods are the "workhorses"
of the **Highcharts for Python** toolkit and you will be relying heavily on them when
using the library. Thankfully, their signatures and behavior is generally consistent -
even if what happens "under the hood" is class-specific at times.

The standard methods exposed by the classes are:

.. _using_deserialization_methods:

Deserialization Methods
---------------------------

.. include:: api/_deserialization_methods.rst

.. _using_serialization_methods:

Serialization Methods
--------------------------

.. include:: api/_serialization_methods.rst

.. _using_other_methods:

Other Convenience Methods
------------------------------

.. include:: api/_other_convenience_methods.rst

.. _handling_defaults:

Handling Default Values
===============================

.. include:: api/_handling_defaults.rst

Module Structure
=====================

.. include:: api/_module_structure.rst

Class Structures and Inheritance
====================================

.. include:: api/_class_structures.rst

.. warning::

  Certain sections of the **Highcharts Stock for Python** library - in particular the
  :mod:`options.series <highcharts_stock.options.series>` classes - rely heavily on
  multiple inheritance. This is a known anti-pattern in Python development as it runs the
  risk of encountering the :term:`diamond of death` inheritance problem. This complicates
  the process of inheriting methods or properties from parent classes when properties or
  methods share names across multiple parents.

  I know this is an anti-pattern, but it was a necessary one to minimize code duplication
  and maximize consistency. For that reason, I implemented it properly *despite* the
  anti-pattern, using some advanced Python concepts to navigate the Python MRO
  (Method Resolution Order) system cleanly. However, an awareness of the pattern used
  may prove helpful if your code inherits from the Highcharts for Python classes.

  .. seealso::

    For a more in-depth discussion of how the anti-pattern was implemented safely and
    reliably, please review the :doc:`Contributor Guidelines <contributing>`.

--------------------------

*******************************************************
Organizing Your Highcharts Stock for Python Project
*******************************************************

**Highcharts Stock for Python** is a utility that can integrate with - quite literally -
any frontend framework. Whether your Python application is relying on iPython (e.g.
`Jupyter Notebook`_ or `Jupyter Labs`_),
`Flask <https://flask.palletsprojects.com/en/2.2.x/>`_,
`Django <https://www.djangoproject.com/>`_,  `FastAPI <https://fastapi.tiangolo.com/>`_,
`Pyramid <https://trypyramid.com/>`_, `Tornado <https://www.tornadoweb.org/en/stable/>`_,
or some completely home-grown solution all Highcharts Stock for
Python needs is a place where
`Highcharts Stock <https://www.highcharts.com/products/stock/>`__ JavaScript code can be executed.

All of those frameworks I mentioned have their own best practices for organizing their
application structures, and those should *always* take priority. Even in a data-centric
application that will be relying heavily on **Highcharts Stock for Python**, your
application's core business logic will be doing most of the heavy lifting and so your
project's organization should reflect that.

However, there are a number of best practices that we recommend for organizing your
files and code to work with **Highcharts Stock for Python**:

  .. warning::

      *There are nine and sixty ways of constructing a tribal lay, and every single one of
      them is right!* -- Rudyard Kipling, *In the Neolithic Age*

    The organizational model described below is just a suggestion, and you can (and likely
    will) depart from its principles and practices as you gain more experience using
    **Highcharts Stock for Python**. There's nothing wrong with that! It's just a set of
    best practices that we've found work for us and which we therefore recommend.

.. _shared_options:

Use Shared Options
========================

One of the most challenging aspects of
`Highcharts JS <https://www.highcharts.com/products/highcharts/>`__ and
`Highcharts Stock <https://www.highcharts.com/products/stock/>`__ are their sheer breadth
of functionality and configurability. That's simultaneously their greatest strength,
and their greatest weakness. This is because it can be quite challenging to wrangle
thousands of properties - especially when one single visualization can use thousands
of properties!

This is a challenge that the developers of `Highcharts JS <https://www.highcharts.com>`__
are keenly aware of, and one which we've given some thought to throughout the
**Highcharts for Python** toolkit. A core principle you should use throughout your project
is to practice :iabbr:`DRY (Do Not Repeat Yourself)` programming. If your application will
be generating multiple visualizations, they will likely need some consistent
configurations.

For example, you will want their title position to be consistent, their color schemes to
be consistent, their font sizing to be consistent, etc. In your code you want these
configuration settings to be defined *once* and then applied to all of the visualizations
you are producing.

This can be facilitated using the
:class:`SharedStockOptions <highcharts_stock.global_options.shared_options.SharedStockOptions>`
class. This generates a single set of global options which - when serialized to
JavaScript - apply its configuration settings consistently across all data
visualizations on the same page.

.. warning::

  :class:`SharedStockOptions <highcharts_stock.global_options.shared_options.SharedStockOptions>`
  is a sub-class of
  :class:`SharedOptions <highcharts_stock.global_options.shared_options.SharedOptions>`
  which extends its properties and methods with properties/methods that are only available
  in the `Highcharts Stock API <https://api.highcharts.com/highstock/>`__.

  However, this class is fully backwards-compatible with the
  `Highcharts JS API <https://api.highcharts.com/highcharts/>`__ if you leave the
  Stock-specific methods and properties set to :obj:`None <python:None>` (their default).

As with all **Highcharts for Python** objects, you can instantiate them in several ways:

.. tabs::

  .. tab:: with JS Literal

    .. tip::

      **Best practice!**

      We really like to use JS literals written as separate files in our codebase. It
      makes it super simple to instantiate a
      :class:`SharedStockOptions <highcharts_stock.global_options.shared_options.SharedStockOptions>`
      instance with one method call.

    Let's say you organize your files like so:

      .. line-block::

        my_repository/
        | --- docs/
        | --- my_project/
        | ------ project_resources/
        | --------- image_files/
        | --------- data_files/
        | ------------ data-file-01.csv
        | ------------ data-file-02.csv
        | ------------ data-file-03.csv
        | --------- **highcharts_config/**
        | ------------ **shared_options.js**
        | ------------ bar-template-01.js
        | ------------ bar-template-02.js
        | ------------ line-template.js
        | ------------ packed-bubble-template.js
        | ------ some_package/
        | --------- __init__.py
        | --------- package_module.py
        | --------- another_module.py
        | ------ __init__.py
        | ------ __version__.py
        | ------ some_module.py
        | --- tests/
        | --- .gitignore
        | --- requirements.txt

    You'll notice that the organization has a ``project_resources`` folder. This is where
    you would put the various files that your application wlil reference, like your static
    images, or the files that contain data you might be using in your application. It also
    contains a **highcharts_config** folder, which contains several files with a ``.js``
    extension. Of particular note is the file in bold, ``shared_options.js``. This file
    should contain a
    :term:`JavaScript object literal <JavaScript object literal notation>`
    version of the configuration settings you want to apply to *all* of your
    visualizations. This file might look something like this:

      .. literalinclude:: _static/shared_options.js
        :language: javascript

    Now with this file, you can easily create a
    :class:`SharedStockOptions <highcharts_stock.global_options.shared_options.SharedStockOptions>`
    instance by executing:

      .. code-block:: python

        from highcharts_stock.highcharts import SharedStockOptions

        my_shared_options = SharedStockOptions.from_js_literal('../../project_resources/highcharts_config/shared_options.js')

    And that's it! Now you have a
    :class:`SharedStockOptions <highcharts_stock.global_options.shared_options.SharedStockOptions>`
    instance that can be used to apply your configuration standards to all of your charts.
    You can do that by delivering its JavaScript output to your front-end by calling:

      .. code-block:: python

        js_code_snippet = my_shared_options.to_js_literal()

    which will produce a string as follows:

      .. literalinclude:: _static/shared_options_output.js
        :language: javascript

    And now you can deliver ``js_code_snippet`` to your HTML template or wherever it will
    be rendered.

  .. tab:: with JSON

    You can use the same exact pattern as using a JS literal with a JSON file instead.
    We don't really think there's an advantage to this - but there might be one
    significant disadvantage: JSON files cannot be used to provide JavaScript functions
    to your Highcharts configuration. This means that formatters, event handlers, etc.
    will not be applied through your shared options if you use a JSON file.

    If your shared options don't require JavaScript functions? Then by all means, feel
    free to use a JSON file and the ``.from_json()`` method instead.

    With a file structure like:

      .. line-block::

        my_repository/
        | --- docs/
        | --- my_project/
        | ------ project_resources/
        | --------- image_files/
        | --------- data_files/
        | ------------ data-file-01.csv
        | ------------ data-file-02.csv
        | ------------ data-file-03.csv
        | --------- **highcharts_config/**
        | ------------ **shared_options.json**
        | ------------ bar-template.json
        | ------------ line-template.json
        | ------------ packed-bubble-template.json
        | ------ some_package/
        | --------- __init__.py
        | --------- package_module.py
        | --------- another_module.py
        | ------ __init__.py
        | ------ __version__.py
        | ------ some_module.py
        | --- tests/
        | --- .gitignore
        | --- requirements.txt

    You can leverage shared options that read from
    ``my_project/project_resources/highcharts_config/shared_options.json`` by executing:

      .. code-block:: python

        from highcharts_stock.highcharts import SharedStockOptions

        my_shared_options = SharedStockOptions.from_js_literal(
            '../../project_resources/highcharts_config/shared_options.json'
        )

        json_code_snippet = my_shared_options.to_js_literal()

  .. tab:: with ``dict``

    If you are hoping to configure a simple set of options, one of the fastest ways to do
    so in your Python code is to instantiate your
    :class:`SharedStockOptions <highcharts_stock.global_options.shared_options.SharedStockOptions>`
    instance from a simple :class:`dict <python:dict>`:

      .. code-block:: python

        as_dict = {
            'chart': {
                'backgroundColor': '#fff',
                'borderWidth': 2,
                'plotBackgroundColor': 'rgba(255, 255, 255, 0.9)',
                'plotBorderWidth': 1
            }
        }

        my_shared_options = SharedStockOptions.from_dict(as_dict)

        js_code_snippet = my_shared_options.to_js_literal()

      .. tip::

        This method is particularly helpful and easy to maintain if you are only using a
        *very* small subset of the `Highcharts JS <https://www.highcharts.com>`__
        configuration options.

  .. tab:: with ``__init__()``

    You can also instantiate a
    :class:`SharedStockOptions <highcharts_stock.global_options.shared_options.SharedStockOptions>`
    instance directly using keywords in the constructor:

      .. code-block:: python

        from highcharts_stock.highcharts import ChartOptions, SharedStockOptions

        my_shared_options = SharedStockOptions(chart = ChartOptions(background_color = '#fff',
                                                                    border_width = 2,
                                                                    plot_background_color = 'rgba(255, 255, 255, 0.9)',
                                                                    plot_border_width = 1))

        js_code_snippet = my_shared_options.to_js_literal()

      .. note::

        You can also supply :class:`dict <python:dict>` representations as keyword argument
        values in the object constructors.

      .. tip::

        **Best practice!**

        While you can create a
        :class:`SharedStockOptions <highcharts_stock.global_options.shared_options.SharedStockOptions>`
        instance and then modify its properties after the fact, that's not exactly the best
        code style. It makes things a bit verbose, and a little harder to reason about.

        Instead, it's recommended that you instantiate your object with all of its
        properties in one go. If you need to change them later, you can do so using Python
        easily - but best to create it all at once.

Use Templates to Get Started
==================================

While :ref:`shared options <shared_options>` are applied to all charts that are rendered
on the same web page with the shared options JS code, certain types of visualizations
may need special treatment. Sure, you can use the
:meth:`plot_options <SharedOptions.plot_options>` settings to configure chart
type-specific options, but how can you efficiently use multiple charts of the same type
that have different settings?

For example, let's say you used :ref:`shared options <shared_options>` to set universal
bar chart settings. But what happens if you know you'll have different data shown in
different bar charts? You can use a similar templating pattern for different sub-types
of your charts.

.. tabs::

  .. tab:: with JS Literal

    .. tip::

      **Best practice!**

      We really like to use JS literals written as separate files in our codebase. It
      makes it super simple to instantiate a **Highcharts Stock for Python** instance with
      one method call.

    Let's say you organize your files like so:

      .. line-block::

        my_repository/
        | --- docs/
        | --- my_project/
        | ------ project_resources/
        | --------- image_files/
        | --------- data_files/
        | ------------ data-file-01.csv
        | ------------ data-file-02.csv
        | ------------ data-file-03.csv
        | --------- **highcharts_config/**
        | ------------ shared_options.js
        | ------------ **hlc-template-01.js**
        | ------------ **hlc-template-02.js**
        | ------------ line-template.js
        | ------------ packed-bubble-template.js
        | ------ some_package/
        | --------- __init__.py
        | --------- package_module.py
        | --------- another_module.py
        | ------ __init__.py
        | ------ __version__.py
        | ------ some_module.py
        | --- tests/
        | --- .gitignore
        | --- requirements.txt

    As you can see, there are two JS literal files named ``hlc-template-01.js`` and
    ``hlc-template-02.js`` respectively. These template files can be used to significantly
    accelerate the configuration of our bar charts. Each template corresponds to one
    sub-type of bar chart that we know we will need. These sub-types may have different
    event functions, or more frequently use different formatting functions to make the
    data look the way we want it to look.

    Now with these template files, we can easily create a pair of
    :class:`Chart <highcharts_stock.chart.Chart>` instances by executing:

      .. code-block:: python

        from highcharts_stock.highcharts import Chart
        from highcharts_stock.options.series.hlc import HLCSeries

        type_1_chart = Chart.from_js_literal(
            '../../project_resources/highcharts_config/hlc-template-01.js'
        )
        type_2_chart = Chart.from_js_literal(
            '../../project_resources/highcharts_config/hlc-template-02.js'
        )

    And that's it! Now you have two chart instances which you can further modify. For
    example, you can add data to them by calling:

      .. code-block:: python

        type_1_chart.container = 'chart1_div'
        type_2_chart.container = 'chart2_div'

        type_1_chart.add_series(HLCSeries.from_csv('../../project_resources/data_files/data-file-01.csv'))
        type_2_chart.add_series(HLCSeries.from_csv('../../project_resources/data_files/data-file-02.csv'))

    And then you can create the relevant JavaScript code to render the chart using:

      .. code-block:: python

        type_1_chart_js = type_1_chart.to_js_literal()
        type_2_chart_js = type_2_chart.to_js_literal()

    And now you can deliver ``type_1_chart_js`` and ``type_2_chart_js`` to your HTML
    template or wherever it will be rendered.

  .. tab:: with JSON

    You can use the same exact pattern as using a JS literal with a JSON file instead.
    We don't really think there's an advantage to this - but there might be one
    significant disadvantage: JSON files cannot be used to provide JavaScript functions
    to your Highcharts configuration. This means that formatters, event handlers, etc.
    will not be applied through your shared options if you use a JSON file.

    If your chart templates don't require JavaScript functions? Then by all means, feel
    free to use a JSON file and the ``.from_json()`` method instead of the
    ``.from_js_literal()`` method.

    .. tip::

      In practice, we find that most chart templates differ in their formatter functions
      and event handlers. This makes JSON a particularly weak tool for templating those
      charts. We strongly prefer the JS literal method described above.

  .. tab:: with ``dict``

    If you are hoping to configure a simple set of template settings, one of the fastest
    ways to do so in your Python code is to instantiate your
    :class:`Chart <highcharts_stock.chart.Chart>` instance from a simple
    :class:`dict <python:dict>` using the ``.from_dict()`` method.

      .. tip::

        This method is particularly helpful and easy to maintain if you are only using a
        *very* small subset of the `Highcharts JS <https://www.highcharts.com>`__ configuration options.

  .. tab:: with ``.copy()``

    If you have an existing **Highcharts for Python** instance, you can copy its
    properties to another object using the ``.copy()`` method. You can therefore set up
    one chart, and then copy its properties to other chart objects with one method call.

      .. code-block:: python

        type_1_chart = Chart.from_js_literal('../../project_resources/highcharts_config/hlc-template-01.js')
        other_chart = type_1_chart.copy(other_chart, overwrite = True)

      .. tip::

        The :meth:`Chart.copy() <highcharts_stock.chart.Chart.copy>` method supports a
        special keyword argument, ``preverse_data`` which if set to ``True`` will copy
        properties (unless ``overwrite = False``) but will *not* overwrite any data. This
        can be very useful to replicating the configuration of your chart across multiple
        charts that have different series and data.

          .. code-block:: python

            other_chart = Chart()
            other_chart.add_series(
              HLCSeries.from_csv('../../project_resources/data_files/data-file-02.csv')
            )

            other_chart = type_1_chart.copy(other_chart,
                                            preserve_data = True)

-----------------

*************************************************
Working with Highcharts Stock Features
*************************************************

`Highcharts Stock <https://www.highcharts.com/products/stock>`__ adds numerous
significant features to
`Highcharts JS <https://www.highcharts.com/products/highcharts/>`__ which add significant
interactivity to your visualizations. These key features are:

.. tabs::

  .. tab:: Stock Tools

    Stock tools are a custom toolbar that can be displayed on your chart which allows your
    users to interact with your chart in various ways. Using event bindings tied to the
    stock tools, you can toggle annotations, toggle
    :term:`technical indicators <technical indicator>`, or control the chart's zoom level.

      .. figure:: _static/stock-tools-example.png
        :alt: Stock Tools Example
        :align: center

    To display the stock tools in your chart, you can use the
    :meth:`HighchartsStockOptions.stock_tools <highcharts_stock.options.HighchartsStockOptions.stock_tools>`
    setting, which can be configured using a
    :class:`StockTools <highcharts_stock.options.stock_tools.StockTools>` instance.

      .. code-block:: python

        my_stock_tools = StockTools(gui = { 'enabled': True })
        my_options = HighchartsStockOptions(stock_tools = my_stock_tools)
        my_chart = Chart.from_options(my_options)

      .. seealso::

        * :class:`StockTools <highcharts_stock.options.stock_tools.StockTools>`
        * :class:`StockToolsGUI <highcharts_stock.options.stock_tools.StockToolsGUI>`

  .. tab:: Navigator

    The :term:`Navigator` is a small series shown below the main series which displays a
    zoomed-out view of the entire dataset. It allows you to zoom in / out or jump to a
    particular range of time in the chart.

      .. figure:: _static/navigator-example.png
        :alt: Navigator
        :align: center

    The navigator is enabled by default in :class:`Chart <highcharts_stock.chart.Chart>`
    instances where :meth:`.is_stock_chart <highcharts_stock.chart.Chart.is_stock_chart>`
    is ``True`` or whose :meth:`.options <highcharts_stock.chart.Chart.options>` contain
    a :class:`HighchartsStockOptions <highcharts_stock.options.HighchartsStockOptions>`
    instance.

    You can configure how the navigator is rendered using several different methods:

      * You can configure whether individual series are shown in the navigator by setting
        their ``.show_in_navigator`` property to ``True`` (to show) or ``False`` (to hide)
      * You can configure how the series is rendered within the navigator by setting their
        ``.navigator_options`` property.
      * You can set general navigator options for the series type by setting their
        ``PlotOptions.<SERIES TYPE>.show_in_navigator`` and
        ``PlotOptions.<SERIES TYPE>.navigator_options`` properties.
      * You can set overall configuration settings for the entire navigator using the
        :meth:`HighchartsStockOptions.navigator <highcharts_stock.HighchartsStockOptions.navigator>`
        setting.

    .. seealso::

      * :class:`Navigator <highcharts_stock.options.navigator.Navigator>`

  .. tab:: Range Selector

    The :term:`Range Selector` is a small tool displayed above (or beside) the
    visualization which allows the user to pre-select the time range that is displayed
    on the chart.

      .. figure:: _static/range-selector-example.png
        :alt: Range Selector Example
        :align: center

    Based upon its configuration (via the
    :meth:`HighchartsStockOptions.options.range_selector <highcharts_stock.options.HighchartsStockOptions.options.range_selector>`
    property), it can display a series of buttons that allow the user to zoom to a
    specific granularity (e.g. display one day's worth of data, display one week's worth
    of data, display one month's worth of data, etc.) and can provide the user with inputs
    to select the range (start date / end date) which should be displayed.

    .. note::

      By default, the range selector is rendered in a responsive fashion. If there is not
      enough room to display the entire selector in a single row, it will collapse into a
      dropdown configuration based on the
      :meth:`RangeSelector.dropdown <highcharts_stock.options.range_selector.RangeSelector.dropdown>`
      setting.

    .. seealso::

      * :class:`RangeSelector <highcharts_stock.options.range_selector.RangeSelector>`
      * :meth:`HighchartsStockOptions.range_selector <highcharts_stock.options.HighchartsStockOptions.range_selector>`


-----------------

.. _working_with_data:

**************************************
Working with Data
**************************************

Obviously, if you are going to use **Highcharts Stock for Python** and
`Highcharts Stock <https://www.highcharts.com/product/stock/>`__ you will
need to have data to visualize. Python is rapidly becoming the *lingua franca* in the
world of data manipulation, transformation, and analysis and
**Highcharts Stock for Python** is specifically designed to play well within that
ecosystem to make it easy to visualize data from CSV files, from `pandas`_ dataframes, or
`PySpark`_ dataframes.

How Data is Represented
==================================

`Highcharts JS <https://www.highcharts.com>`__ supports two different ways of representing
data: as an individual :term:`series` comprised of individual data points, and as a set of
instructions to read data dynamically from a CSV file or an HTML table.

  .. seealso::

    * :class:`DataBase <highcharts_stock.options.series.data.base.DataBase>` class
    * :class:`options.Data <highcharts_stock.options.data.Data>` class

`Highcharts JS <https://www.highcharts.com>`__ organizes data into :term:`series`. You can
think of a series as a single line on a graph that shows a set of values. The set of
values that make up the series are :term:`data points <data point>`, which are defined by
a set of properties that indicate the data point's position on one or more axes. As a
result, `Highcharts JS <https://www.highcharts.com>`__ and **Highcharts for Python** both
represent the data points in series as a list of data point objects in the ``data``
property within the series:

.. list-table::
  :widths: 50 50
  :header-rows: 1

  * - Highcharts JS
    - Highcharts for Python
  * - .. code-block:: javascript

        // Example Series Object
        // (for a Line series type):
        {
          data: [
            {
              id: 'first-data-point',
              x: 1,
              y: 123,
              // ...
              // optional additional properties
              // for styling/behavior go here
              // ...
            },
            {
              id: 'second-data-point',
              x: 2,
              y: 456,
              // ...
              // optional additional properties
              // for styling/behavior go here
              // ...
            },
            {
              id: 'third-data-point',
              x: 3,
              y: 789,
              // ...
              // optional additional properties
              // for styling/behavior go here
              // ...
            }
          ],
          // ...
          // other Series properties go here
          // to configure styling/behavior
        }
    - .. code-block:: python

        # Corresponding LineSeries object
        my_series = Series(data = [
            CartesianData(id = 'first-data-point1',
                          x = 1,
                          y = 123),
            CartesianData(id = 'second-data-point1',
                          x = 2,
                          y = 456),
            CartesianData(id = 'third-data-point1',
                          x = 3,
                          y = 789),
        ])

As you can see, **Highcharts for Python** represents its data the same way that
`Highcharts JS <https://www.highcharts.com>`__ does. That should be expected. However,
constructing tens, hundreds, or possibly thousands of data points individually in your
code would be a nightmare. For that reason, the **Highcharts for Python** toolkit provides
a number of convenience methods to make it easier to populate your series.

.. warning::

  **PLEASE TAKE NOTE!**

  **Highcharts Stock for Python** and
  `Highcharts Stock <https://www.highcharts.com/products/stock/>`__ support over 40
  different :term:`technical indicators <technical indicator>`, which are visualizations
  that are derived from *other* :term:`series` on your chart. These technical indicators
  are a special kind of series, however they do not have a ``.data`` property and thus
  cannot be given their own data points. Their data points are calculated automatically by
  `Highcharts Stock <https://www.highcharts.com/products/stock/>`__ from the
  related :term:`series` indicated in their
  :meth:`.linked_to <highcharts_stock.options.series.base.IndicatorSeriesBase.linked_to>`
  properties.

.. _populating_series_data:

Populating Series Data
===========================

Every single :term:`Series` class in **Highcharts for Python** features several different
methods to either instantiate data points directly, load data (to an existing series
instance), or to create a new series instance with data already loaded.

.. tabs::

  .. tab:: Direct Instantiation

    .. warning::

      :term:`Technical indicators <technical indicator>` provided by
      **Highcharts Stock for Python** do not support the ``.from_array()`` method because
      their data gets populated dynamically based on the series indicated in their
      :meth:`.linked_to <highcharts_stock.options.series.base.IndicatorSeriesBase.linked_to>`
      property.

      .. seealso::

        * :doc:`Using Highcharts Stock for Python <using>` > :ref:`Using Technical Indicators <using_technical_indicators>`

    When working with a :term:`series` instance, you can instantiate data points directly.
    These data points are stored in the
    :meth:`.data <highcharts_stock.options.series.base.SeriesBase.data>` setting, which
    always accepts/expects a list of data point instances (descended from
    :class:`DataBase <highcharts_stock.options.series.data.base.DataBase>`).

    Data points all have the same standard **Highcharts for Python**
    :ref:`deserialization methods <deserialization_methods>`, so those make things very easy.
    However, they also have a special data point-specific deserialization method:

      .. method:: from_array(cls, value)
        :classmethod:

        Creates a collection of data point instances, parsing the contents of ``value`` as an
        array (iterable). This method is specifically used to parse data that is input to
        **Highcharts for Python** without property names, in an array-organized structure as
        described in the `Highcharts JS <https://www.highcharts.com>`__ documentation.

        .. seealso::

          The specific structure of the expected array is highly dependent on the type of data
          point that the series needs, which itself is dependent on the series type itself.

          Please review the detailed :ref:`series documentation <series_documentation>` for
          series type-specific details of relevant array structures.

        .. note::

          An example of how this works for a simple
          :class:`LineSeries <highcharts_stock.options.series.area.LineSeries>` (which uses
          :class:`CartesianData <highcharts_stock.options.series.data.cartesian.CartesianData>`
          data points) would be:

          .. code-block:: python

            my_series = LineSeries()

            # A simple array of numerical values which correspond to the Y value of the data
            # point
            my_series.data = [0, 5, 3, 5]

            # An array containing 2-member arrays (corresponding to the X and Y values of the
            # data point)
            my_series.data = [
                [0, 0],
                [1, 5],
                [2, 3],
                [3, 5]
            ]

            # An array of dict with named values
            my_series.data = [
              {
                  'x': 0,
                  'y': 0,
                  'name': 'Point1',
                  'color': '#00FF00'
              },
              {
                  'x': 1,
                  'y': 5,
                  'name': 'Point2',
                  'color': '#CCC'
              },
              {
                  'x': 2,
                  'y': 3,
                  'name': 'Point3',
                  'color': '#999'
              },
              {
                  'x': 3,
                  'y': 5,
                  'name': 'Point4',
                  'color': '#000'
              }
            ]

        :param value: The value that should contain the data which will be converted into data
          point instances.

          .. note::

            If ``value`` is not an iterable, it will be converted into an iterable to be
            further de-serialized correctly.

        :type value: iterable

        :returns: Collection of :term:`data point` instances (descended from
          :class:`DataBase <highcharts_stock.options.series.data.base.DataBase>`)
        :rtype: :class:`list <python:list>` of
          :class:`DataBase <highcharts_stock.options.series.data.base.DataBase>`-descendant
          instances

  .. tab:: Load to Existing Series

    .. warning::

      :term:`Technical indicators <technical indicator>` provided by
      **Highcharts Stock for Python** do not support the ``.load_from_*`` methods because
      their data gets populated dynamically based on the series indicated in their
      :meth:`.linked_to <highcharts_stock.options.series.base.IndicatorSeriesBase.linked_to>`
      property.

      .. seealso::

        * :doc:`Using Highcharts Stock for Python <using>` > :ref:`Using Technical Indicators <using_technical_indicators>`

    .. method:: .load_from_csv(self, as_string_or_file, property_column_map, has_header_row = True, delimiter = ',', null_text = 'None', wrapper_character = "'", line_terminator = '\r\n', wrap_all_strings = False, double_wrapper_character_when_nested = False, escape_character = '\\')

      Updates the series instance with a collection of data points (descending from
      :class:`DataBase <highcharts_stock.options.series.data.base.DataBase>`) from
      ``as_string_or_file`` by traversing the rows of data and extracting the values from
      the columns indicated in ``property_column_map``.

        .. warning::

          This method will overwrite the contents of the series instance's
          :meth:`data <highcharts_stock.options.series.base.SeriesBase>` property.

        .. note::

          For an example
          :class:`LineSeries <highcharts_stock.options.series.area.LineSeries>`, the
          minimum code required would be:

            .. code-block:: python

              my_series = LineSeries()
              my_series.load_from_csv('some-csv-file.csv',
                                      property_column_map = {
                                          'x': 0,
                                          'y': 3,
                                          'id': 'id'
                                      })

          As the example above shows, data is loaded into the ``my_series`` instance from
          the CSV file with a filename ``some-csv-file.csv``. The
          :meth:`x <CartesianData.x>`
          values for each data point will be taken from the first (index 0) column in the
          CSV file. The :meth:`y <CartesianData.y>` values will be taken from the fourth
          (index 3) column in the CSV file. And the :meth:`id <CartesianData.id>` values
          will be taken from a column whose header row is labeled ``'id'`` (regardless of
          its index).

      :param as_string_or_file: The CSV data to load, either as a :class:`str <python:str>`
        or as the name of a file in the runtime envirnoment. If a file, data will be read
        from the file.

        .. tip::

          Unwrapped empty column values are automatically interpreted as null
          (:obj:`None <python:None>`).

      :type as_string_or_file: :class:`str <python:str>` or Path-like

      :param property_column_map: A :class:`dict <python:dict>` used to indicate which
        data point property should be set to which CSV column. The keys in the
        :class:`dict <python:dict>` should correspond to properties in the data point class,
        while the value can either be a numerical index (starting with 0) or a
        :class:`str <python:str>` indicating the label for the CSV column.

        .. warning::

          If the ``property_column_map`` uses :class:`str <python:str>` values, the CSV file
          *must* have a header row (this is expected, by default). If there is no header row
          and a :class:`str <python:str>` value is found, a
          :exc:`HighchartsDeserializationError` will be raised.

      :type property_column_map: :class:`dict <python:dict>`

      :param has_header_row: If ``True``, indicates that the first row of
        ``as_string_or_file`` contains column labels, rather than actual data. Defaults to
        ``True``.
      :type has_header_row: :class:`bool <python:bool>`

      :param delimiter: The delimiter used between columns. Defaults to ``,``.
      :type delimiter: :class:`str <python:str>`

      :param wrapper_character: The string used to wrap string values when
        wrapping is applied. Defaults to ``'``.
      :type wrapper_character: :class:`str <python:str>`

      :param null_text: The string used to indicate an empty value if empty
        values are wrapped. Defaults to `None`.
      :type null_text: :class:`str <python:str>`

      :param line_terminator: The string used to indicate the end of a line/record in the
        CSV data. Defaults to ``'\r\n'``.

        .. warning::

          The Python :mod:`csv <python:csv>` module currently ignores the
          ``line_terminator`` parameter and always applies ``'\r\n'``, by design. The Python
          docs say this may change in the future, so for future backwards compatibility we
          are including it here.

      :type line_terminator: :class:`str <python:str>`

      :param wrap_all_strings: If ``True``, indicates that the CSV file has all string data
        values wrapped in quotation marks. Defaults to ``False``.

        .. warning::

          If set to ``True``, the :mod:`csv <python:csv>` module will try to coerce any
          value that is *not* wrapped in quotation marks to a :class:`float <python:float>`.
          This can cause unexpected behavior, and typically we recommend leaving this as
          ``False`` and then re-casting values after they have been parsed.

      :type wrap_all_strings: :class:`bool <python:bool>`

      :param double_wrapper_character_when_nested: If ``True``, quote character is doubled
        when appearing within a string value. If ``False``, the ``escape_character`` is used
        to prefix quotation marks. Defaults to ``False``.
      :type double_wrapper_character_when_nested: :class:`bool <python:bool>`

      :param escape_character: A one-character string that indicates the character used to
        escape quotation marks if they appear within a string value that is already wrapped
        in quotation marks. Defaults to ``\\`` (which is Python for ``'\'``, which is
        Python's native escape character).
      :type escape_character: :class:`str <python:str>`

      :returns: A collection of data points descended from
        :class:`DataBase <highcharts_stock.options.series.data.base.DataBase>` as
        appropriate for the series class.
      :rtype: :class:`list <python:list>` of instances descended from
        :class:`DataBase <highcharts_stock.options.series.data.base.DataBase>`

      :raises HighchartsDeserializationError: if unable to parse the CSV data correctly

    .. method:: .load_from_pandas(self, df, property_map)

      Replace the contents of the
      :meth:`.data <highcharts_stock.options.series.base.SeriesBase.data>` property
      with data points populated from a `pandas`_
      :class:`DataFrame <pandas:DataFrame>`.

      :param df: The :class:`DataFrame <pandas:DataFrame>` from which data should be
        loaded.
      :type df: :class:`DataFrame <pandas:DataFrame>`

      :param property_map: A :class:`dict <python:dict>` used to indicate which
        data point property should be set to which column in ``df``. The keys in the
        :class:`dict <python:dict>` should correspond to properties in the data point
        class, while the value should indicate the label for the
        :class:`DataFrame <pandas:DataFrame>` column.
      :type property_map: :class:`dict <python:dict>`

      :raises HighchartsPandasDeserializationError: if ``property_map`` references
        a column that does not exist in the data frame
      :raises HighchartsDependencyError: if `pandas`_ is
        not available in the runtime environment

    .. method:: .load_from_pyspark(self, df, property_map)

      Replaces the contents of the
      :meth:`.data <highcharts_stock.options.series.base.SeriesBase.data>` property
      with values from a `PySpark <https://spark.apache.org/docs/latest/api/python/>`_
      :class:`DataFrame <pyspark:pyspark.sql.DataFrame>`.

      :param df: The :class:`DataFrame <pyspark:pyspark.sql.DataFrame>` from which data
        should be loaded.
      :type df: :class:`DataFrame <pyspark:pyspark.sql.DataFrame>`

      :param property_map: A :class:`dict <python:dict>` used to indicate which
        data point property should be set to which column in ``df``. The keys in the
        :class:`dict <python:dict>` should correspond to properties in the data point
        class, while the value should indicate the label for the
        :class:`DataFrame <pyspark:pyspark.sql.DataFrame>` column.
      :type property_map: :class:`dict <python:dict>`

      :raises HighchartsPySparkDeserializationError: if ``property_map`` references
        a column that does not exist in the data frame
      :raises HighchartsDependencyError: if
        `PySpark <https://spark.apache.org/docs/latest/api/python/>`_ is not available
        in the runtime environment

  .. tab:: Create a New Series

    .. warning::

      :term:`Technical indicators <technical indicator>` provided by
      **Highcharts Stock for Python** do not support the ``.from_csv()``,
      ``.from_pandas()``, and ``.from_pyspark()`` methods because their data gets populated
      dynamically based on the series indicated in their
      :meth:`.linked_to <highcharts_stock.options.series.base.IndicatorSeriesBase.linked_to>`
      property.

      .. seealso::

        * :doc:`Using Highcharts Stock for Python <using>` > :ref:`Using Technical Indicators <using_technical_indicators>`



    .. method:: .from_csv(cls, as_string_or_file, property_column_map, series_kwargs = None, has_header_row = True, delimiter = ',', null_text = 'None', wrapper_character = "'", line_terminator = '\r\n', wrap_all_strings = False, double_wrapper_character_when_nested = False, escape_character = '\\')
      :classmethod:

      Create a new :term:`series` instance with a
      :meth:`.data <highcharts_stock.options.series.base.SeriesBase.data>` property
      populated from data in a CSV string or file.

        .. note::

          For an example
          :class:`LineSeries <highcharts_stock.options.series.area.LineSeries>`, the
          minimum code required would be:

            .. code-block:: python

              my_series = LineSeries.from_csv('some-csv-file.csv',
                                              property_column_map = {
                                                  'x': 0,
                                                    'y': 3,
                                                  'id': 'id'
                                              })

          As the example above shows, data is loaded into the ``my_series`` instance
          from the CSV file with a filename ``some-csv-file.csv``. The
          :meth:`x <CartesianData.x>`
          values for each data point will be taken from the first (index 0) column in
          the CSV file. The :meth:`y <CartesianData.y>` values will be taken from the
          fourth (index 3) column in the CSV file. And the :meth:`id <CartesianData.id>`
          values will be taken from a column whose header row is labeled ``'id'``
          (regardless of its index).

      :param as_string_or_file: The CSV data to use to pouplate data. Accepts either
        the raw CSV data as a :class:`str <python:str>` or a path to a file in the
        runtime environment that contains the CSV data.

        .. tip::

          Unwrapped empty column values are automatically interpreted as null
          (:obj:`None <python:None>`).

      :type as_string_or_file: :class:`str <python:str>` or Path-like

      :param property_column_map: A :class:`dict <python:dict>` used to indicate which
        data point property should be set to which CSV column. The keys in the
        :class:`dict <python:dict>` should correspond to properties in the data point
        class, while the value can either be a numerical index (starting with 0) or a
        :class:`str <python:str>` indicating the label for the CSV column.

        .. warning::

          If the ``property_column_map`` uses :class:`str <python:str>` values, the CSV
          file *must* have a header row (this is expected, by default). If there is no
          header row and a :class:`str <python:str>` value is found, a
          :exc:`HighchartsCSVDeserializationError` will be raised.

      :type property_column_map: :class:`dict <python:dict>`

      :param has_header_row: If ``True``, indicates that the first row of
        ``as_string_or_file`` contains column labels, rather than actual data. Defaults
        to ``True``.
      :type has_header_row: :class:`bool <python:bool>`

      :param series_kwargs: An optional :class:`dict <python:dict>` containing keyword
        arguments that should be used when instantiating the series instance. Defaults
        to :obj:`None <python:None>`.

        .. warning::

          If ``series_kwargs`` contains a ``data`` key, its value will be *overwritten*.
          The ``data`` value will be created from the CSV file instead.

      :type series_kwargs: :class:`dict <python:dict>`

      :param delimiter: The delimiter used between columns. Defaults to ``,``.
      :type delimiter: :class:`str <python:str>`

      :param wrapper_character: The string used to wrap string values when
        wrapping is applied. Defaults to ``'``.
      :type wrapper_character: :class:`str <python:str>`

      :param null_text: The string used to indicate an empty value if empty
        values are wrapped. Defaults to `None`.
      :type null_text: :class:`str <python:str>`

      :param line_terminator: The string used to indicate the end of a line/record in
        the CSV data. Defaults to ``'\r\n'``.
      :type line_terminator: :class:`str <python:str>`

      :param line_terminator: The string used to indicate the end of a line/record in the
        CSV data. Defaults to ``'\r\n'``.

        .. note::

          The Python :mod:`csv <python:csv>` currently ignores the ``line_terminator``
          parameter and always applies ``'\r\n'``, by design. The Python docs say this may
          change in the future, so for future backwards compatibility we are including it
          here.

      :type line_terminator: :class:`str <python:str>`

      :param wrap_all_strings: If ``True``, indicates that the CSV file has all string data
        values wrapped in quotation marks. Defaults to ``False``.

        .. warning::

          If set to ``True``, the :mod:`csv <python:csv>` module will try to coerce any
          value that is *not* wrapped in quotation marks to a :class:`float <python:float>`.
          This can cause unexpected behavior, and typically we recommend leaving this as
          ``False`` and then re-casting values after they have been parsed.

      :type wrap_all_strings: :class:`bool <python:bool>`

      :param double_wrapper_character_when_nested: If ``True``, quote character is doubled
        when appearing within a string value. If ``False``, the ``escape_character`` is used
        to prefix quotation marks. Defaults to ``False``.
      :type double_wrapper_character_when_nested: :class:`bool <python:bool>`

      :param escape_character: A one-character string that indicates the character used to
        escape quotation marks if they appear within a string value that is already wrapped
        in quotation marks. Defaults to ``\\`` (which is Python for ``'\'``, which is
        Python's native escape character).
      :type escape_character: :class:`str <python:str>`

      :returns: A :term:`series` instance (descended from
        :class:`SeriesBase <highcharts_stock.options.series.base.SeriesBase>`) with its
        :meth:`.data <highcharts_stock.options.series.base.SeriesBase.data>` property
        populated from the CSV data in ``as_string_or_file``.
      :rtype: :class:`list <python:list>` of series instances (descended from
        :class:`SeriesBase <highcharts_stock.options.series.base.SeriesBase>`)

      :raises HighchartsCSVDeserializationError: if ``property_column_map`` references
        CSV columns by their label, but the CSV data does not contain a header row

    .. method:: .from_pandas(cls, df, property_map, series_kwargs = None)
      :classmethod:

      Create a :term:`series` instance whose
      :meth:`.data <highcharts_stock.options.series.base.SeriesBase.data>` property
      is populated from a `pandas`_
      :class:`DataFrame <pandas:DataFrame>`.

      :param df: The :class:`DataFrame <pandas:DataFrame>` from which data should be
        loaded.
      :type df: :class:`DataFrame <pandas:DataFrame>`

      :param property_map: A :class:`dict <python:dict>` used to indicate which
        data point property should be set to which column in ``df``. The keys in the
        :class:`dict <python:dict>` should correspond to properties in the data point
        class, while the value should indicate the label for the
        :class:`DataFrame <pandas:DataFrame>` column.
      :type property_map: :class:`dict <python:dict>`

      :param series_kwargs: An optional :class:`dict <python:dict>` containing keyword
        arguments that should be used when instantiating the series instance. Defaults
        to :obj:`None <python:None>`.

        .. warning::

          If ``series_kwargs`` contains a ``data`` key, its value will be *overwritten*.
          The ``data`` value will be created from ``df`` instead.

      :type series_kwargs: :class:`dict <python:dict>`

      :returns: A :term:`series` instance (descended from
        :class:`SeriesBase <highcharts_stock.options.series.base.SeriesBase>`) with its
        :meth:`.data <highcharts_stock.options.series.base.SeriesBase.data>` property
        populated from the data in ``df``.
      :rtype: :class:`list <python:list>` of series instances (descended from
        :class:`SeriesBase <highcharts_stock.options.series.base.SeriesBase>`)

      :raises HighchartsPandasDeserializationError: if ``property_map`` references
        a column that does not exist in the data frame
      :raises HighchartsDependencyError: if `pandas`_ is
        not available in the runtime environment

    .. method:: .from_pyspark(cls, df, property_map, series_kwargs = None)
      :classmethod:

      Create a :term:`series` instance whose
      :meth:`.data <highcharts_stock.options.series.base.SeriesBase.data>` property
      is populated from a `PySpark <https://spark.apache.org/docs/latest/api/python/>`_
      :class:`DataFrame <pyspark:pyspark.sql.DataFrame>`.

      :param df: The :class:`DataFrame <pyspark:pyspark.sql.DataFrame>` from which data
        should be loaded.
      :type df: :class:`DataFrame <pyspark:pyspark.sql.DataFrame>`

      :param property_map: A :class:`dict <python:dict>` used to indicate which
        data point property should be set to which column in ``df``. The keys in the
        :class:`dict <python:dict>` should correspond to properties in the data point
        class, while the value should indicate the label for the
        :class:`DataFrame <pyspark:pyspark.sql.DataFrame>` column.
      :type property_map: :class:`dict <python:dict>`

      :param series_kwargs: An optional :class:`dict <python:dict>` containing keyword
        arguments that should be used when instantiating the series instance. Defaults
        to :obj:`None <python:None>`.

        .. warning::

          If ``series_kwargs`` contains a ``data`` key, its value will be *overwritten*.
          The ``data`` value will be created from ``df`` instead.

      :type series_kwargs: :class:`dict <python:dict>`

      :returns: A :term:`series` instance (descended from
        :class:`SeriesBase <highcharts_stock.options.series.base.SeriesBase>`) with its
        :meth:`.data <highcharts_stock.options.series.base.SeriesBase.data>` property
        populated from the data in ``df``.
      :rtype: :class:`list <python:list>` of series instances (descended from
        :class:`SeriesBase <highcharts_stock.options.series.base.SeriesBase>`)

      :raises HighchartsPySparkDeserializationError: if ``property_map`` references
        a column that does not exist in the data frame
      :raises HighchartsDependencyError: if
        `PySpark <https://spark.apache.org/docs/latest/api/python/>`_ is not available
        in the runtime environment

.. _adding_series_to_charts:

Adding Series to Charts
=============================

Now that you have constructed your :term:`series` instances, you can add them to
:term:`charts` very easily. First, **Highcharts for Python** represents visualizations as
instances of the :class:`Chart <highcharts_stock.chart.Chart>` class. This class contains
an :meth:`options <highcharts_stock.chart.Chart.options>` property, which itself contains
an instance of
:class:`HighchartsStockOptions <highcharts_stock.options.HighchartsStockOptions>`.

  .. note::

    The :class:`HighchartsStockOptions <highcharts_stock.options.HighchartsStockOptions>`
    is a sub-class of the **Highcharts for Python**
    :class:`HighchartsOptions <highcharts_stock.options.HighchartsOptions>` class, and is
    fully backwards-compatible with it. This means that you can use them interchangably
    when using **Highcharts Stock for Python**, as the
    :class:`HighchartsStockOptions <highcharts_stock.options.HighchartsStockOptions>`
    class merely extends its parent with a number of methods and properties that are
    specifically supported by
    `Highcharts Stock <https://www.highcharts.com/products/stock>`__.

  .. note::

    This structure - where the chart object contains an options object - is a little
    nested for my tastes, but it is the structure which
    `Highcharts JS <https://www.highcharts.com>`__ has adopted and
    so for the sake of consistency the **Highcharts for Python** toolkit uses it as well.

To be visualized on your chart, you will need to add your series instances to the
:meth:`Chart.options.series <highcharts_stock.options.HighchartsOptions.series>`
property. You can do this in several ways:

.. tabs::

  .. tab:: Directly on the Property

    .. code-block:: python

      my_chart = Chart(options = {})
      my_series1 = LineSeries()
      my_series2 = BarSeries()
      my_chart.options.series = [my_series1, my_series2]

      my_series3 = LineSeries()
      my_chart.options.series.append(my_series3)

  .. tab:: Using ``.add_series()``

    .. note::

      ``.add_series()`` is supported by both the
      :class:`Chart <highcharts_stock.chart.Chart>` and
      :class:`HighchartsStockOptions <highcharts_stock.options.HighchartsStockOptions>`
      classes

    .. code-block:: python

      my_chart = Chart()
      my_chart.add_series(my_series1, my_series2)

      my_series3 = LineSeries()
      my_chart.add_series(my_series3)

    .. method:: .add_series(self, *series)
      :noindex:

      Adds ``series`` to the
      :meth:`Chart.options.series <highcharts_stock.options.HighchartsStockOptions.series>`
      property.

      :param series: One or more :term:`series` instances (descended from
        :class:`SeriesBase <highcharts_stock.options.series.base.SeriesBase>`) or an
        instance (e.g. :class:`dict <python:dict>`, :class:`str <python:str>`, etc.)
        coercable to one
      :type series: :class:`SeriesBase <highcharts_stock.options.series.base.SeriesBase>`
        or coercable

  .. tab:: Using ``.from_series()``

    .. note::

      ``.from_series()`` is supported by both the
      :class:`Chart <highcharts_stock.chart.Chart>` and
      :class:`HighchartsStockOptions <highcharts_stock.options.HighchartsStockOptions>`
      classes

    .. code-block:: python

      my_series1 = LineSeries()
      my_series2 = BarSeries()

      my_chart = Chart.from_series(my_series1, my_series2, options = None)

    .. method:: .from_series(cls, *series, kwargs = None)
      :noindex:

      Creates a new :class:`Chart <highcharts_stock.chart.Chart>` instance populated
      with ``series``.

      :param series: One or more :term:`series` instances (descended from
        :class:`SeriesBase <highcharts_stock.options.series.base.SeriesBase>`) or an
        instance (e.g. :class:`dict <python:dict>`, :class:`str <python:str>`, etc.)
        coercable to one
      :type series: :class:`SeriesBase <highcharts_stock.options.series.base.SeriesBase>`
        or coercable

      :param kwargs: Other properties to use as keyword arguments for the instance to be
        created.

        .. warning::

          If ``kwargs`` sets the
          :meth:`options.series <highcharts_stock.options.HighchartsStockOptions.series>`
          property, that setting will be *overridden* by the contents of ``series``.

      :type kwargs: :class:`dict <python:dict>`

      :returns: A new :class:`Chart <highcharts_stock.chart.Chart>` instance
      :rtype: :class:`Chart <highcharts_stock.chart.Chart>`

.. _using_technical_indicators:

Using Technical Indicators
=============================

One of the most valuable aspects of
`Highcharts Stock <https://www.highcharts.com/products/stock/>`__ is the inclusion of over
40 :term:`technical indicators <technical indicator>`. These are additional analytical
tools which can be overlaid on your visualization to provide insights into the data you
are looking at.

For example, are you hoping to understand whether the trajectory of a stock price is about
to change? Or do you want to determine whether a given asset has been under-or-over sold?
Or maybe you want to plot a simple linear regression against your primary series? You can
do all of these and more using the technical indicators provided by
`Highcharts Stock <https://www.highcharts.com/products/stock>`__.

Technical indicators are :term:`series` in their own right, and can be added to your
chart the same as you would add any other series. However, unlike traditional series they
do *not* have a ``.data`` property, since they do not receive any data points. Instead,
they reference the primary series whose data should be used to calculate the indicator via
their :meth:`.linked_to <highcharts_stock.options.series.base.IndicatorSeries.linked_to>`
property.

You can add a series using the following methods:

.. tabs::

  .. tab:: ``Series.add_indicator()``

    All standard :term:`series` (descending from
    :class:`SeriesBase <highcharts_stock.options.series.base.SeriesBase>`) have an
    :meth:`.add_indicator() <highcharts_stock.options.series.base.SeriesBase>` method
    which can be used to easily configure a new indicator tied to the series in question.

    You can call the method very simply:

    .. code-block:: python

      my_chart = Chart(series = [my_series])

      # Adds a new Simple Moving Average indicator to the chart, based off of the
      # "my_series" series.

      my_chart = my_series.add_indicator(my_chart, 'sma')

    The method has a straightforward signature:

    .. method:: .add_indicator(chart, indicator_name, indicator_kwargs = None)

      :param chart: The chart object in which the series is rendered and to which the
        indicator should be appended.
      :type chart: :class:`Chart <highcharts_stock.chart.Chart>`

      :param indicator_name: The name of the indicator that should be added to the series
        and chart. For the list of supported indicators, please review the
        :ref:`Indicator List <indicator_list>`.
      :type indicator_name: :class:`str <python:str>`

      :param indicator_kwargs: Keyword arguments to apply when instantiating the new
        indicator series. Defaults to :obj:`None <python:None>`.
      :type indicator_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`

      :returns: ``chart`` with a new indicator series included in its list of configured
        series.
      :rtype: :class:`Chart <highcharts_stock.chart.Chart>`

  .. tab:: ``Chart.add_indicator()``

    You can also add an indicator directly to the
    :class:`Chart <highcharts_stock.chart.Chart>` object using the
    :meth:`Chart.add_series() <highcharts_stock.chart.Chart.add_indicator>` method.

    .. code-block:: python

      # Adds a Simple Moving Average indicator to the series with the ID "my-series-id"
      my_chart.add_indicator('sma', series = 'my-series-id')

      # Adds a Simple Moving Average indicator AND the series with the ID "my-series-id"
      my_chart.add_indicator('sma', series = my_series)

    The :meth:`Chart.add_series() <highcharts_stock.chart.Chart.add_indicator>` method
    has a straightforward signature:

    .. method:: .add_series(indicator_name, series, indicator_kwargs = None)

      Creates a :class:`IndicatorSeriesBase` (descendant) that calculates the
      ``indicator_name`` :term:`technical indicator` for the series provided in
      ``series``, and adds it to the chart's
      :meth:`.options.series <highcharts_stock.options.HighchartsStockOptions.series>`.

      :param indicator_name: The name of the indicator that should be added to the series
        and chart. For the list of supported indicators, please review the
        :ref:`Indicator List <indicator_list>`.
      :type indicator_name: :class:`str <python:str>`

      :param series: The series to which the indicator should be added. Accepts either a
        series' :meth:`.id <highcharts_stock.options.series.SeriesBase.id>` as a
        :class:`str <python:str>`, or a
        :class:`SeriesBase <highcharts_stock.options.series.base.SeriesBase>` (descendant)
        instance.
      :type series: :class:`str <python:str>` or
        :class:`SeriesBase <highcharts_stock.options.series.base.SeriesBase>`

      :param indicator_kwargs: Keyword arguments to apply when instantiating the new
        indicator series. Defaults to :obj:`None <python:None>`.
      :type indicator_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`

      :returns: Nothing. It simply changes the composition of the chart instance's
        series to now include a new series with the indicator.

--------------------

**************************************
Rendering Your Visualizations
**************************************

Once you have created your :class:`Chart <highcharts_stock.chart.Chart>` instance or
instances, you can render them very easily. There are really only two ways to display
your visualizations:

  #. :ref:`Render Visualizations in Web Content <web_rendering>`
  #. :ref:`Render Visualizations in Jupyter Labs / Jupyter Notebook <jupyter_rendering>`

.. _web_rendering:

Rendering Highcharts Visualizations in Web Content
========================================================

`Highcharts JS <https://www.highcharts.com>`__ is a JavaScript library specifically
designed to enable rendering high-end data visualizations in a web context. The library is
designed and optimized to operate within a web browser. The **Highcharts for Python**
toolkit therefore fully supports this capability, and we've enabled it using the
*batteries included* principle.

To render a **Highcharts Stock for Python** visualization, all you need is for the browser
to execute the output of the chart's
:meth:`.to_js_literal() <highcharts_stock.chart.Chart.to_js_literal>` method, which will
return a snippet of JavaScript code which when included in a web page will display the
chart in full.

.. warning::

  The current version of **Highcharts Stock for Python** includes all the ``<script/>``
  tags which include the `Highcharts Stock <https://www.highcharts.com/products/stock>`__
  modules. This is overkill, since most likely your visualization will not need *all* of
  these scripts to be included.

  This is likely to change in a future version of **Highcharts for Python** toolkit, where
  the library will support the production of ``<script/>`` tags dynamically based on the
  features your chart is using (see roadmap :issue:`2`).

For example:

  .. tabs::

    .. tab:: as a Highcharts Stock Chart

      .. code-block:: python

        my_chart = Chart(container = 'target_div',
                         options = {
                             'series': [
                                 HLCSeries.from_array([
                                     [2, 0, 4],
                                     [4, 2, 8],
                                     [3, 9, 3]
                                 ])
                             ]
                         },
                         variable_name = 'myChart',
                         is_stock_chart = True)

        as_js_literal = my_chart.to_js_literal()

        # This will produce a string equivalent to:
        #
        # document.addEventListener('DOMContentLoaded', function() {
        #   const myChart = Highcharts.stockChart('target_div', {
        #      series: {
        #          type: 'hlc',
        #          data: [
        #            [2, 0, 4],
        #            [4, 2, 8],
        #            [3, 9, 3]
        #          ]
        #      }
        #   });
        # });

    .. tab:: as a Highcharts JS Chart

      .. code-block:: python

        my_chart = Chart(container = 'target_div',
                         options = {
                             'series': [
                                 LineSeries.from_array([0, 5, 3, 5])
                             ]
                         },
                         variable_name = 'myChart')

        as_js_literal = my_chart.to_js_literal()

        # This will produce a string equivalent to:
        #
        # document.addEventListener('DOMContentLoaded', function() {
        #   const myChart = Highcharts.chart('target_div', {
        #      series: {
        #          type: 'line',
        #          data: [0, 5, 3, 5]
        #      }
        #   });
        # });

Now you can use whatever front-end framework you are using to insert that string into your
application's HTML output (in an appropriate ``<script/>`` tag, of course).

.. tip::

  The same principle applies to the use of
  :class:`SharedStockOptions <highcharts_stock.global_options.shared_options.SharedStockOptions>`.

  It is recommended to place the JS literal form of your shared options *before* any of
  the charts that you will be visualizing.

  .. seealso::

    * :ref:`Organizing Your Highcharts for Python Project > Use Shared Options <shared_options>`

.. _jupyter_rendering:

Rendering Highcharts for Python in Jupyter Labs or Jupyter Notebooks
======================================================================

You can also render **Highcharts Stock for Python** visualizations inside your
`Jupyter <https://jupyter.org/>`_ notebook. This is as simple as executing a single
:meth:`.display() <highcharts_stock.chart.Chart.display>` call on your
:class:`Chart <highcharts_stock.chart.Chart>` instance:

  .. code-block:: python

    my_chart = Chart(container = 'target_div',
                     options = {
                         'series': [
                             LineSeries.from_array([0, 5, 3, 5])
                         ]
                     },
                     variable_name = 'myChart',
                     is_stock_chart = True)

    my_chart.display()

    # You can also supply shared options to display to make sure that they are applied:
    my_shared_options = SharedStockOptions()
    my_chart.display(global_options = my_shared_options)

You can call the ``.display()`` method from anywhere within any notebook cell, and it
will render the resulting chart in your notebook's output. That's it!

  .. caution::

    If `iPython <https://ipython.readthedocs.io/>`_ is not available in your runtime
    environment, calling
    :meth:`.display() <highcharts_stock.chart.Chart.display>` will raise a
    :exc:`HighchartsDependencyError`.

Stock Chart vs Regular Chart
==================================

When using **Highcharts Stock for Python** you have the choice to render your charts
using the `Highcharts Stock <https://www.highcharts.com/products/stock>`__ chart
constructor or the standard
`Highcharts JS <https://www.highcharts.com/products/highcharts/>`__ chart constructor.

The difference between these two constructors relates to the features available in the
chart. The Highcharts Stock chart will be visualized including the :term:`navigator`
component, and can support time series :term:`scrollbars <scrollbar>`, even if the
specific chart you are visualizing does not need or use them. A regular Highcharts JS
chart cannot be displayed with either of these elements.

It is entirely your decision, but you should know that
`Highcharts JS <https://www.highcharts.com/products/highcharts/>`__ does not support any
of the :term:`technical indicators <technical indicator>` supported by
`Highcharts Stock <https://www.highcharts.com/products/stock>`__, and also does not
support :term:`candlestick`, :term:`HLC`, or :term:`OHLC` series types.

However, Highcharts Stock *can* visualize all of the series types offered by
`Highcharts JS <https://www.highcharts.com/products/highcharts/>`__.

When working with your :class:`Chart <highcharts_stock.chart.Chart>` object, you can set
the :meth:`.is_stock_chart <highcharts_stock.chart.Chart.is_stock_chart>` property to
``True`` to force the chart to be rendered using the (JavaScript)
``Highcharts.stockChart()`` constructor.

If you wish to force the use of the (JavaScript) ``Highcharts.chart()``
constructor, you can explicitly set
:meth:`.is_stock_chart <highcharts_stock.chart.Chart.is_stock_chart>` to ``False`` after
populating the chart's :meth:`.options <highcharts_stock.chart.Chart.options>` property.

If you do not set this property explicitly, **Highcharts Stock for Python** will make
a determination based on the contents of the
:meth:`.options <highcharts_stock.chart.Chart.options>` property. If that that property
is set to a
:class:`HighchartsStockOptions <highcharts_stock.options.HighchartsStockOptions>`
instance, the :meth:`.is_stock_chart <highcharts_stock.chart.Chart.is_stock_chart>`
property will be set to ``True``, unless explicitly overridden in your code.

---------------------------

********************************************
Downloading Your Visualizations
********************************************

.. sidebar:: Highcharts Export Server

  Highsoft - the developers of `Highcharts JS <https://www.highcharts.com>`__ - are kind
  enough to provide a rate-limited publicly available :term:`Export Server` that can be
  used by `Highcharts JS <https://www.highcharts.com>`__ license-holders. By default,
  **Highcharts Stock for Python** is configured to use this server.

  However, there are many use cases where you may be deploying your own
  :term:`Export Server` and wish to use that instead. You can do this by
  creating your own
  :class:`ExportServer <highcharts_stock.headless_export.ExportServer>` instance and
  supplying it as the ``server_instance`` keyword argument to the ``.download_chart()``
  method.

Sometimes you are not looking to produce an interactive web-based visualization of your
data, but instead are looking to produce a static image of your visualization that can
be downloaded, emailed, or embedded in some other documents.

With **Highcharts Stock for Python**, that's as simple as executing the
:meth:`Chart.download_chart() <highcharts_stock.chart.Chart.download_chart>` method.

When you have defined a :class:`Chart <highcharts_stock.chart.Chart>` instance, you can
download a static version of that chart or persist it to a file in your runtime
environment. The actual file itself is produced using a
:term:`Highcharts Export Server <Export Server>`.

  .. code-block:: python

    my_chart = Chart(container = 'target_div',
                     options = {
                         'series': [
                             LineSeries.from_array(
                                 [0, 5, 3, 5]
                             )
                         ]
                     },
                     variable_name = 'myChart',
                     is_stock_chart = True)

    my_png_image = my_chart.download_chart(
        format = 'png'
    )

    # also saves the file to "/images/my-chart-file.png"
    my_png_image = my_chart.download_chart(
        format = 'png',
        filename = '/images/my-chart-file.png'
    )

  .. method:: .download_chart(self, filename = None, format = 'png', server_instance = None, scale = 1, width = None, auth_user = None, auth_password = None, timeout = 0.5, global_options = None, **kwargs)

    Export a downloaded form of the chart using a Highcharts :term:`Export Server`.

    :param filename: The name of the file where the exported chart should (optionally)
      be persisted. Defaults to :obj:`None <python:None>`.
    :type filename: Path-like or :obj:`None <python:None>`

    :param server_instance: Provide an already-configured :class:`ExportServer`
      instance to use to programmatically produce the exported chart. Defaults to
      :obj:`None <python:None>`, which causes **Highcharts for Python** to instantiate
      a new :class:`ExportServer` instance with all applicable defaults.
    :type server_instance: :class:`ExportServer` or :obj:`None <python:None>`

    :param format: The format in which the exported chart should be returned. Defaults to
      ``'png'``.

      Accepts:

        * ``'png'``
        * ``'jpeg'``
        * ``'pdf'``
        * ``'svg'``

    :type format: :class:`str <python:str>`

    :param scale: The scale factor by which the exported chart image should be scaled. Defaults
      to ``1``.

      .. tip::

        Use this setting to improve resolution when exporting PNG or JPEG images. For
        example, setting ``scale = 2`` on a chart whose width is 600px will produce
        an image file with a width of 1200px.

      .. warning::

        If ``width`` is explicitly set, this setting will be *overridden*.

    :type scale: numeric

    :param width: The width that the exported chart should have. Defaults to
      :obj:`None <python:None>`.

      .. warning::

        If explicitly set, this setting will override ``scale``.

    :type width: numeric or :obj:`None <python:None>`

    :param auth_user: The username to use to authenticate against the
      Export Server, using :term:`basic authentication`. Defaults to
      :obj:`None <python:None>`.
    :type auth_user: :class:`str <python:str>` or :obj:`None <python:None>`

    :param auth_password: The password to use to authenticate against the Export
      Server (using :term:`basic authentication`). Defaults to
      :obj:`None <python:None>`.
    :type auth_password: :class:`str <python:str>` or :obj:`None <python:None>`

    :param timeout: The number of seconds to wait before issuing a timeout error.
      The timeout check is passed if bytes have been received on the socket in less
      than the ``timeout`` value. Defaults to ``0.5``.
    :type timeout: numeric or :obj:`None <python:None>`

    :param global_options: The global options which will be passed to the (JavaScript)
      ``Highcharts.setOptions()`` method, and which will be applied to the exported
      chart. Defaults to :obj:`None <python:None>`.

    :type global_options: :class:`HighchartsStockOptions <highcharts_stock.options.HighchartsStockOptions>`,
      :class:`HighchartsOptions <highcharts_stock.options.HighchartsOptions>` or
      :obj:`None <python:None>`

    .. note::

      All other keyword arguments are as per the :class:`ExportServer` constructor.

    :returns: The exported chart image, either as a :class:`bytes <python:bytes>`
      binary object or as a base-64 encoded string (depending on the ``use_base64``
      keyword argument).
    :rtype: :class:`bytes <python:bytes>` or :class:`str <python:str>`

-----------------------------

.. target-notes::

.. include:: links.txt

.. _`Jupyter Notebook`: https://jupyter.org
.. _`Jupyter Labs`: https://jupyter.org
.. _IPython: https://ipython.readthedocs.io/
.. _pandas: https://pandas.pydata.org
.. _PySpark: https://spark.apache.org/docs/latest/api/python/

###################################################
Highcharts Stock for Python
###################################################

**High-end time series data visualization for the Python ecosystem**

**Highcharts Stock for Python** is an extension to the 
`Highcharts Core for Python <https://core-docs.highchartspython.com>`__ library, 
providing a Python wrapper for the 
`Highcharts Stock <https://www.highcharts.com/products/stock/>`__
JavaScript data visualization library. 

**Highcharts Stock for Python** also supports

  * **Highcharts Core (JS)** - the core Highcharts data visualization library
  * The **Highcharts Export Server** - enabling the programmatic creation of static
    (downloadable) data visualizations

The library supports Highcharts (JS) v.10.2 and higher, including Highcharts (JS) v.11.3.0.

**Highcharts Stock for Python** is fully integrated with the broader Python ecosystem,
in particular:

  * **Jupyter Labs/Notebook**. You can now produce high-end and interactive plots and
    renders using the full suite of Highcharts visualization capabilities.
  * **Pandas**. Automatically produce data visualizations from your Pandas dataframes
  * **PySpark**. Automatically produce data visualizations from data in a PySpark
    dataframe.

**COMPLETE DOCUMENTATION:** https://stock-docs.highchartspython.com/en/latest/index.html

--------------------

***************************************
The Highcharts for Python Toolkit
***************************************

The **Highcharts Stock for Python** library is part of the broader 
`Highcharts for Python Toolkit <https://www.highcharts.com/integrations/python>`__, 
which together provides comprehensive support across the entire 
`Highcharts <https://www.highcharts.com>`__ suite of data visualization libraries:

.. list-table::
  :widths: 30 30 40
  :header-rows: 1

  * - Python Library
    - JavaScript Library
    - Description
  * - `Highcharts Core for Python <https://core-docs.highchartspython.com/>`__
    - `Highcharts Core (JS) <https://www.highcharts.com/products/highcharts/>`__
    - (this library) the core Highcharts data visualization library
  * - **Highcharts Stock for Python**
    - `Highcharts Stock (JS) <https://www.highcharts.com/products/stock/>`__
    - the time series visualization extension to Highcharts Core
  * - `Highcharts Maps for Python <https://maps-docs.highchartspython.com/>`__ 
    - `Highcharts Maps (JS) <https://www.highcharts.com/products/maps/>`__
    - the map visualization extension to Highcharts Core
  * - `Highcharts Gantt for Python <https://gantt-docs.highchartspython.com/>`__
    - `Highcharts Gantt (JS) <https://www.highcharts.com/products/gantt/>`__
    - the Gantt charting extension to Highcharts Core
  * - (all libraries in the Python toolkit)
    - The **Highcharts Export Server** 
    - enabling the programmatic creation of static (downloadable) data visualizations

--------------------

***************
Installation
***************

To install **Highcharts Stock for Python**, just execute:

  .. code-block:: bash

    $ pip install highcharts-stock

Before you install, please be aware of the following "hard" dependencies:

  * Python 3.10 or higher
  * Highcharts Stock (JS) v.10.2 or higher (not technically a Python dependency, but 
    it won't work with earlier versions of Highcharts Stock)
  * `Highcharts Core for Python <https://core-docs.highchartspython.com/en/latest/>`__ v.1.7 or higher
  * `esprima-python <https://github.com/Kronuz/esprima-python>`__ v.4.0 or higher
  * `requests <https://requests.readthedocs.io/en/latest/>`__ v.2.31 or higher
  * `validator-collection <https://validator-collection.readthedocs.io/en/latest/>`__
    v.1.5 or higher

You can find more information about soft and development dependencies in the
`complete documentation <https://stock-docs.highchartspython.com/en/latest/#dependencies>`__.


-------------

*********************************
Why Highcharts for Python?
*********************************

`Highcharts <https://www.highcharts.com>`__ is the world's most popular, most powerful, 
category-defining JavaScript data visualization library. If you are building a web or 
mobile app/dashboard that will be visualizing data in some fashion, you should 
absolutely take a look at the Highcharts suite of solutions. Take a peak at some 
fantastic `demo visualizations <https://www.highcharts.com/demo>`__.

As a suite of JavaScript libraries, `Highcharts <https://www.highcharts.com>`__ is 
written in JavaScript, and is used to configure and render data visualizations in a
web browser (or other JavaScript-executing) environment. As a set of JavaScript
libraries, its audience is JavaScript developers. But what about the broader ecosystem of
Python developers and data scientists?

Given Python's increasing adoption as the technology of choice for data science and for
the backends of leading enterprise-grade applications, Python is often the backend that 
delivers data and content to the front-end...which then renders it using JavaScript and 
HTML.

There are numerous Python frameworks (Django, Flask, Tornado, etc.) with specific
capabilities to simplify integration with Javascript frontend frameworks (React, Angular,
VueJS, etc.). But facilitating that with Highcharts has historically been very difficult.
Part of this difficulty is because the Highcharts JavaScript suite - while supporting JSON as a
serialization/deserialization format - leverages JavaScript object literals to expose the
full power and interactivity of its data visualizations. And while it's easy to serialize
JSON from Python, serializing and deserializing to/from JavaScript object literal notation
is much more complicated. 

This means that Python developers looking to integrate with Highcharts typically had to 
either invest a lot of effort, or were only able to leverage a small portion of Highcharts' 
rich functionality.

So we wrote the **Highcharts for Python Toolkit** to bridge that gap.

**Highcharts for Python** provides Python object representation for *all* of the
JavaScript objects defined in the
`Highcharts (JavaScript) API <https://api.highcharts.com/highcharts/>`__. It provides automatic 
data validation, and exposes simple and standardized methods for serializing those Python
objects back-and-forth to JavaScript object literal notation.

**Highcharts Stock for Python** in particular provides support for
the `Highcharts Stock <https://www.highcharts.com/products/stock/>`__ extension, which is
designed to provide rich time series data visualization capabilities optimized for
asset (e.g. stock) price data visualization, with extensive technical indicators and
robust interactivity. For ease of use, it also includes the full functionality of
`Highcharts Core for Python <https://core-docs.highchartspython.com>`__ as well.

Key Highcharts Stock for Python Features
==============================================

* **Clean and consistent API**. No reliance on "hacky" code, ``dict``
  and JSON serialization, or impossible to maintain / copy-pasted "spaghetti code".
* **Comprehensive Highcharts support**. Every single Highcharts chart type and every
  single configuration option is supported in **Highcharts Stock for Python**. This
  includes the over 70 data visualization types supported by
  `Highcharts Core <https://www.highcharts.com/product/highcharts/>`__,  the specialisted
  chart types and 50+ technical indicator visualizations available in
  `Highcharts Stock <https://www.highcharts.com/product/stock/>`__.
  
  Every Highcharts for Python library provides full support for the rich JavaScript 
  formatter (JS callback functions) capabilities that are often needed to get the most 
  out of Highcharts' visualization and interaction capabilities.

  .. note::

    **See Also:**

    * `Supported Visualizations <https://stock-docs.highchartspython.com/en/latest/visualizations.html>`__

* **Simple JavaScript Code Generation**. With one method call, produce production-ready
  JavaScript code to render your interactive visualizations using Highcharts' rich
  capabilities.
* **Easy Chart Download**. With one method call, produce high-end static
  visualizations that can be downloaded or shared as files with your audience. Produce
  static charts using the Highsoft-provided **Highcharts Export Server**, or using your 
  own private export server as needed.
* **Integration with Pandas and PySpark**. With two lines of code, produce a high-end
  interactive visualization of your Pandas or PySpark dataframe.
* **Consistent code style**. For Python developers, switching between Pythonic code
  conventions and JavaScript code conventions can be...annoying. So
  the Highcharts for Python toolkit applies Pythonic syntax with automatic conversion between
  Pythonic ``snake_case`` notation and JavaScript ``camelCase`` styles.

|

**Highcharts Stock for Python** vs Alternatives
===================================================

For a discussion of **Highcharts Stock for Python** in comparison to alternatives, please see
the **COMPLETE DOCUMENTATION:** https://stock-docs.highchartspython.com/en/latest/index.html

---------------------

********************************
Hello World, and Basic Usage
********************************

1. Import Highcharts Stock for Python
==========================================

.. code-block:: python

  # BEST PRACTICE!
  # PRECISE LOCATION PATTERN
  # This method of importing Highcharts Stock for Python objects yields the fastest
  # performance for the import statement. However, it is more verbose and requires
  # you to navigate the extensive `Highcharts Stock for Python API.

  # Import classes using precise module indications. For example:
  from highcharts_stock.chart import Chart
  from highcharts_stock.global_options.shared_options import SharedStockOptions
  from highcharts_stock.options import HighchartsStockOptions
  from highcharts_stock.options.plot_options.bar import BarOptions
  from highcharts_stock.options.series.bar import BarSeries

  # CATCH-ALL IMPORT PATTERN
  # This method of importing **Highcharts Stock for Python** classes has relatively slow
  # performance because it imports hundreds of different classes from across the entire
  # library. This performance impact may be acceptable to you in your use-case, but
  # do use at your own risk.

  # Import objects from the catch-all ".highcharts" module.
  from highcharts_stock import highcharts

  # You can now access specific classes without individual import statements.
  highcharts.Chart
  highcharts.SharedStockOptions
  highcharts.HighchartsStockOptions
  highcharts.BarOptions
  highcharts.BarSeries


2. Create Your Chart
================================

  .. code-block:: python

    # from a primitive array, using keyword arguments
    my_chart = Chart(data = [[1, 23], [2, 34], [3, 45]], 
                     series_type = 'line')

    # from a primitive array, using the .from_array() method
    my_chart = Chart.from_array([[1, 23], [2, 34], [3, 45]], 
                                series_type = 'line')

    # from a Numpy ndarray, using keyword arguments
    my_chart = Chart(data = numpy_array, series_type = 'line')

    # from a Numpy ndarray, using the .from_array() method
    my_chart = Chart.from_array(data = numpy_array, series_type = 'line')

    # from a JavaScript file
    my_chart = Chart.from_js_literal('my_js_literal.js')

    # from a JSON file
    my_chart = Chart.from_json('my_json.json')

    # from a Python dict
    my_chart = Chart.from_dict(my_dict_obj)

    # from a Pandas dataframe
    my_chart = Chart.from_pandas(df)

    # from a PySpark dataframe
    my_chart = Chart.from_pyspark(df,
                                  property_map = {
                                      'x': 'transactionDate',
                                      'y': 'invoiceAmt',
                                      'id': 'id'
                                  },
                                  series_type = 'line')

    # from a CSV
    my_chart = Chart.from_csv('/some_file_location/filename.csv')

    # from a HighchartsOptions configuration object
    my_chart = Chart.from_options(my_options)

    # from a Series configuration, using keyword arguments
    my_chart = Chart(series = my_series)

    # from a Series configuration, using .from_series()
    my_chart = Chart.from_series(my_series)
    

3. Configure Global Settings (optional)
=============================================

  .. code-block:: python

    # Import SharedStockOptions
    from highcharts_stock.global_options.shared_options import SharedStockOptions

    # from a JavaScript file
    my_global_settings = SharedStockOptions.from_js_literal('my_js_literal.js')

    # from a JSON file
    my_global_settings = SharedStockOptions.from_json('my_json.json')

    # from a Python dict
    my_global_settings = SharedStockOptions.from_dict(my_dict_obj)

    # from a HighchartsOptions configuration object
    my_global_settings = SharedStockOptions.from_options(my_options)


4. Configure Your Chart / Global Settings
================================================

  .. code-block:: python

    from highcharts_core.options.title import Title
    from highcharts_core.options.credits import Credits

    # EXAMPLE 1.
    # Using dicts
    my_chart.title = {
        'align': 'center',
        'floating': True,
        'text': 'The Title for My Chart',
        'use_html': False,
    }

    my_chart.credits = {
        'enabled': True,
        'href': 'https://www.highchartspython.com/',
        'position': {
            'align': 'center',
            'vertical_align': 'bottom',
            'x': 123,
            'y': 456
        },
        'style': {
            'color': '#cccccc',
            'cursor': 'pointer',
            'font_size': '9px'
        },
        'text': 'Chris Modzelewski'
    }

    # EXAMPLE 2.
    # Using direct objects
    from highcharts_core.options.title import Title
    from highcharts_core.options.credits import Credits

    my_title = Title(text = 'The Title for My Chart',
                     floating = True, 
                     align = 'center')
    my_chart.options.title = my_title

    my_credits = Credits(text = 'Chris Modzelewski', 
                         enabled = True, 
                         href = 'https://www.highchartspython.com')
    my_chart.options.credits = my_credits


5. Generate the JavaScript Code for Your Chart
=================================================

Now having configured your chart in full, you can easily generate the JavaScript code
that will render the chart wherever it is you want it to go:

  .. code-block:: python

    # as a string
    js_as_str = my_chart.to_js_literal()

    # to a file (and as a string)
    js_as_str = my_chart.to_js_literal(filename = 'my_target_file.js')


6. Generate the JavaScript Code for Your Global Settings (optional)
=========================================================================

  .. code-block:: python

    # as a string
    global_settings_js = my_global_settings.to_js_literal()

    # to a file (and as a string)
    global_settings_js = my_global_settings.to_js_literal('my_target_file.js')


7. Generate a Static Version of Your Chart
==============================================

  .. code-block:: python

    # as in-memory bytes
    my_image_bytes = my_chart.download_chart(format = 'png')

    # to an image file (and as in-memory bytes)
    my_image_bytes = my_chart.download_chart(filename = 'my_target_file.png',
                                             format = 'png')

8. Render Your Chart in a Jupyter Notebook
===============================================

  .. code-block:: python

    my_chart.display()

--------------

***********************
Getting Help/Support
***********************

The **Highcharts for Python Toolkit** comes with all of the great support that 
you are used to from working with the Highcharts JavaScript libraries. When you 
license the toolkit, you are welcome to use any of the following channels to get 
help using the toolkit:

  * Use the `Highcharts Forums <https://highcharts.com/forum>`__
  * Use `Stack Overflow <https://stackoverflow.com/questions/tagged/highcharts-for-python>`__ 
    with the ``highcharts-for-python`` tag
  * `Report bugs or request features <https://github.com/highcharts-for-python/highcharts-stock/issues>`__  
    in the library's Github repository
  * `File a support ticket <https://www.highchartspython.com/get-help>`__ with us
  * `Schedule a live chat or video call <https://www.highchartspython.com/get-help>`__ 
    with us

**FOR MORE INFORMATION:** https://www.highchartspython.com/get-help

-----------------

*********************
Contributing
*********************

We welcome contributions and pull requests! For more information, please see the
`Contributor Guide <https://stock-docs.highchartspython.com/en/latest/contributing.html>`__. 
And thanks to all those who've already contributed!

-------------------

*********************
Testing
*********************

We use `TravisCI <https://travisci.com>`_ for our build automation and
`ReadTheDocs <https://readthedocs.com>`_ for our documentation.

Detailed information about our test suite and how to run tests locally can be
found in our Testing Reference.

###################################################
Highcharts Stock for Python
###################################################

**High-end time series data visualization for the Python ecosystem**

**Highcharts Stock for Python** is an extension to the
`Highcharts Core for Python <https://core-docs.highchartspython.com>`__ library, and provides
a Python wrapper for the fantastic
`Highcharts Stock <https://www.highcharts.com/products/stock/>`__
JavaScript data visualization library. **Highcharts Stock for Python** also supports

  * **Highcharts JS** - the core Highcharts data visualization library
  * The **Highcharts Export Server** - enabling the programmatic creation of static
    (downloadable) data visualizations

In order to integrate **Highcharts Stock for Python** into the Python ecosystem, the
library features native integration with:

  * **Jupyter Labs/Notebook**. You can now produce high-end and interactive plots and
    renders using the full suite of Highcharts visualization capabilities.
  * **Pandas**. Automatically produce data visualizations from your Pandas dataframes
  * **PySpark**. Automatically produce data visualizations from data in a PySpark
    dataframe.

**COMPLETE DOCUMENTATION:** https://stock-docs.highchartspython.com/en/latest/index.html

--------------------

***************
Installation
***************

To install **Highcharts Stock for Python**, just execute:

  .. code-block:: bash

    $ pip install highcharts-stock

-------------

*********************************
Why Highcharts for Python?
*********************************

Odds are you are aware of
`Highcharts Stock <https://www.highcharts.com/products/stock/>`__. If not, why not?
It is the world's most popular, most powerful, category-defining JavaScript data
visualization library for time-series data and - in particular - for stock price data.

If you are building a web or mobile app/dashboard that will be
visualizing time series or stock price data in some fashion, you should absolutely take a
look at the Highcharts suite of solutions. Just take a look at some of their fantastic
`Highcharts Stock demo visualizations <https://www.highcharts.com/demo/stock>`__.

Highcharts Stock is a JavaScript library, and is an extension of the
`Highcharts JS <https://www.highcharts.com/products/highcharts/>`__ JavaScript library. It
is written in JavaScript, and is specifically used to configure and render data
visualizations in a web browser (or other JavaScript-executing, like mobile app)
environment. As a JavaScript library, its audience is JavaScript developers. But what
about the broader ecosystem of Python developers and data scientists?

Python is increasingly used as the technology of choice for data science and for
the backends of leading enterprise-grade applications. In other words, Python is
often the backend that delivers data and content to the front-end...which then renders it
using JavaScript and HTML.

There are numerous Python frameworks (Django, Flask, Tornado, etc.) with specific
capabilities to simplify integration with Javascript frontend frameworks (React, Angular,
VueJS, etc.). But facilitating that with Highcharts has historically been very difficult.
Part of this difficulty is because the Highcharts JavaScript suite - while supporting JSON as a
serialization/deserialization format - leverages
JavaScript object literals to expose the
full power and interactivity of its data visualizations. And while it's easy to serialize
JSON from Python, serializing and deserializing to/from JavaScript object literal notation
is much more complicated. This means that Python developers looking to integrate with
Highcharts typically had to either invest a lot of effort, or were only able to leverage
a small portion of Highcharts' rich functionality.

So I wrote the **Highcharts for Python** toolkit to bridge that gap, and
**Highcharts Stock for Python** to provide full support for the
`Highcharts Stock <https://www.highcharts.com/products/stock/>`__ library extension.

**Highcharts Stock for Python** provides support for
the `Highcharts Stock <https://www.highcharts.com/products/stock/>`__ extension, which is
designed to provide extensive time series data visualization capabilities optimized for
asset (e.g. stock) price data visualization, with extensive technical indicators and
robust interactivity. For ease of use, it also includes the full functionality of
**Highcharts Core for Python** as well.

Key Highcharts Stock for Python Features
==============================================

* **Clean and consistent API**. No reliance on "hacky" code, ``dict``
  and JSON serialization, or impossible to maintain / copy-pasted "spaghetti code".
* **Comprehensive Highcharts support**. Every single Highcharts chart type and every
  single configuration option is supported in **Highcharts Stock for Python**. This
  includes the over 70 data visualization types supported by
  `Highcharts Core <https://www.highcharts.com/product/highcharts/>`__ and the
  50+ technical indicator visualizations available in
  `Highcharts Stock <https://www.highcharts.com/product/stock/>`__, with full support for
  the rich JavaScript formatter (JS callback functions)
  capabilities that are often needed to get the most out of Highcharts' visualization and
  interaction capabilities.

  .. note::

    **See Also:**

    * `Supported Visualizations <https://stock-docs.highchartspython.com/en/latest/visualizations.html>`__

* **Simple JavaScript Code Generation**. With one method call, produce production-ready
  JavaScript code to render your interactive visualizations using Highcharts' rich
  capabilities.
* **Easy Chart Download**. With one method call, produce high-end static
  visualizations that can be downloaded or shared as files with your audience. Produce
  static charts using the Highsoft-provided **Highcharts Export Server**, or using your own private export
  server as needed.
* **Integration with Pandas and PySpark**. With two lines of code, produce a high-end
  interactive visualization of your Pandas or PySpark dataframe.
* **Consistent Code Style**. For Python developers, switching between Pythonic code
  conventions and JavaScript code conventions can be...annoying. So
  **Highcharts for Python** applies Pythonic syntax with automatic conversion between
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

    # from a JavaScript file
    my_chart = highcharts.Chart.from_js_literal('my_js_literal.js')

    # from a JSON file
    my_chart = highcharts.Chart.from_json('my_json.json')

    # from a Python dict
    my_chart = highcharts.Chart.from_dict(my_dict_obj)

    # from a Pandas dataframe
    my_chart = highcharts.Chart.from_pandas(df,
                                            property_map = {
                                                'x': 'transactionDate',
                                                'y': 'invoiceAmt',
                                                'id': 'id'
                                            },
                                            series_type = 'line')

    # from a PySpark dataframe
    my_chart = highcharts.Chart.from_pyspark(df,
                                             property_map = {
                                                 'x': 'transactionDate',
                                                 'y': 'invoiceAmt',
                                                 'id': 'id'
                                             },
                                             series_type = 'line')

    # from a CSV
    my_chart = highcharts.Chart.from_csv('/some_file_location/filename.csv'
                                         column_property_map = {
                                            'x': 0,
                                            'y': 4,
                                            'id': 14
                                         },
                                         series_type = 'line')

    # from a HighchartsOptions configuration object
    my_chart = highcharts.Chart.from_options(my_options)

    # from a Series configuration
    my_chart = highcharts.Chart.from_series(my_series)


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

    from highcharts_stock.options.title import Title
    from highcharts_stock.options.credits import Credits

    # Using dicts
    my_chart.title = {
        'align': 'center'
        'floating': True,
        'text': 'The Title for My Chart',
        'use_html': False,
    }

    my_chart.credits = {
        'enabled': True,
        'href': 'https://www.highcharts.com/',
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

    # Using direct objects
    from highcharts_stock.options.title import Title
    from highcharts_stock.options.credits import Credits

    my_title = Title(text = 'The Title for My Chart', floating = True, align = 'center')
    my_chart.options.title = my_title

    my_credits = Credits(text = 'Chris Modzelewski', enabled = True, href = 'https://www.highcharts.com')
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

--------------

***********************
Getting Help/Support
***********************

The **Highcharts for Python** toolkit comes with all of the great support that you are used to from working with the 
Highcharts JavaScript libraries. When you license the toolkit, you are welcome to use any of the following tools to get 
help using the toolkit. In particular, you can:

  * Use the `Highcharts Forums <https://highcharts.com/forum>`__
  * Use `Stack Overflow <https://stackoverflow.com/questions/tagged/highcharts-for-python>`__ with the 
    ``highcharts-for-python`` tag
  * `Report bugs or request features <https://github.com/highcharts-for-python/highcharts-stock/issues>`__ in the 
    library's Github repository 
  * `File a support ticket <https://www.highchartspython.com/get-help>`__ with us
  * `Schedule a live chat or video call <https://www.highchartspython.com/get-help>`__ with us

**FOR MORE INFORMATION:** https://www.highchartspython.com/get-help

-----------------

*********************
Contributing
*********************

We welcome contributions and pull requests! For more information, please see the
`Contributor Guide <https://stock-docs.highchartspython.com/en/latest/contributing.html>`__. And thanks to all those who've already contributed!

-------------------

*********************
Testing
*********************

We use `TravisCI <https://travisci.org>`_ for our build automation and
`ReadTheDocs <https://readthedocs.org>`_ for our documentation.

Detailed information about our test suite and how to run tests locally can be
found in our Testing Reference.

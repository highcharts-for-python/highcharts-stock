################################
Frequently Asked Questions
################################

.. contents::
  :depth: 2
  :backlinks: entry

-------------------

*******************************************************
Highcharts for Python vs Highcharts Stock for Python
*******************************************************

**What is the difference between Highcharts for Python and Highcharts Stock for Python?**

The `Highcharts for Python <https://highcharts-core.readthedocs.io/>`__ library supports
`Highcharts JS <https://www.highcharts.com/products/highcharts/>`__, which is the core
data visualization library developed by `Highsoft <https://www.highcharts.com/>`__. It
provides over 60 different visualization types.

**Highcharts Stock for Python** is an *extension* to **Highcharts for Python** in the same
way that `Highcharts Stock <https://www.highcharts.com/products/stock/>`__ is an
*extension* to `Highcharts JS <https://www.highcharts.com/products/highcharts/>`__. It:

  * adds new features (including a :term:`navigator`, interactive :term:`stock tools`, and
    :term:`scrollbars <scrollbar>`) to supported charts,
  * adds new series types, including :term:`candlestick`, :term:`HLC`, and :term:`OHLC`
  * adds support for over 40 :term:`technical indicators <technical indicator>` which you
    can include in your visualizations

.. tip::

  **Highcharts Stock for Python** *includes* all of the functionality from
  **Highcharts for Python** using th exact same API. As a result, the best practice is
  that if your application needs any of the features included in
  **Highcharts Stock for Python**, just use that library.

**Can I use the Navigator or Stock Tools on non-Stock charts?**

Yes, you can. If you are using the Highcharts Stock :term:`stock tools` or
:term:`navigator` features, you can still use them with non-stock charts (e.g.
:class:`Organization <highcharts_stock.options.series.organization.OrganizationSeries>`,
or :class:`Gauge <highcharts_stock.options.series.gauge.GaugeSeries>`). This can be
particualrly useful if you are using custom :term:`stock tools` and want to maintain a
consistent user experience in your application.

---------------

***********************
Licensing:
***********************

**Is Highcharts Stock for Python free?**

If you are a student using it for educational purposes, or wish to familiarize yourself
with the library, then yes - you are free to use it without paying. However, if you are
using it for a professional purpose - either to use Highcharts for your work, or to build
an application that integrates the library - then you have to pay for both
`Highcharts Stock <https://www.highcharts.com/products/stock/>`__ itself *and* for the
**Highcharts for Python** toolkit.

**How much does the Highcharts for Python toolkit cost?**

.. todo::

  Add pricing details.

**How do I license the Highcharts for Python toolkit?**

.. todo::

  Add licensing instructions.

----------------------

.. todo::

  Predict other key questions that might get asked.

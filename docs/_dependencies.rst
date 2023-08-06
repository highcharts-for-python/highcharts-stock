.. note::

  **Highcharts Stock for Python** has several types of dependencies:

    * *hard* dependencies, without which you will not be able to use the library at all,
    * *soft* dependencies, which will not produce errors but which may limit the value you
      get from the library,
    * *developer* dependencies that contributors will need in their local environment, and
    * *documentation* dependencies that are necessary if you wish to generate (this)
      documentation

.. tabs::

  .. tab:: Hard

    .. warning::

      If these hard dependencies are not available in the environment where
      **Highcharts Stock for Python** is running, then the library will simply not work.
      Besides `Highcharts Stock <https://www.highcharts.com/products/stock>`__ itself, all
      of the other hard dependencies are automatically installed when installing
      **Highcharts Stock for Python** using:

      .. code-block:: bash

        $ pip install highcharts-stock

    * `Highcharts Stock <https://www.highcharts.com/products/stock/>`__ v.10.2 or higher

      .. note::

        Not technically a Python dependency, but obviously **Highcharts Stock for Python**
        will not work properly if your rendering layer does not leverage Highcharts Stock.

    * `highcharts-core <https://core-docs.highchartspython.com>`_ v.1.3.0 or higher
    * `esprima-python <https://github.com/Kronuz/esprima-python>`_ v.4.0 or higher
    * `requests <https://requests.readthedocs.io/en/latest/>`_ v.2.31 or higher
    * `validator-collection <https://validator-collection.readthedocs.io/en/latest/>`_
      v.1.5 or higher

  .. tab:: Soft

    .. warning::

      If these soft dependencies are not available in the environment where
      **Highcharts Stock for Python** is running, then the library will throw a
      :exc:`HighchartsDependencyError <errors.HighchartsDependencyError>` exception when
      you try to use functionality that relies on them.

      No error will be thrown until you try to use dependent functionality. So if you call
      a ``from_pandas()`` method but `pandas <https://pandas.pydata.org/>`_ is not
      installed, you will get an error.

      You can install **Highcharts Stock for Python** with *all* soft dependencies using:

      .. code-block::

        $ pip install highcharts-stock[soft]

    * `IPython <https://ipython.org/>`__ v. 8.10 or higher
    * `orjson <https://github.com/ijl/orjson>`__ v.3.7.7 or higher
    * `pandas <https://pandas.pydata.org/>`_ v. 1.3 or higher
    * `pyspark <https://spark.apache.org/docs/latest/api/python/index.html>`_ v.3.3 or
      higher

  .. tab:: Developer

    .. warning::

      You will not be able to run unit tests without the Pytest test framework and a
      number of necessary extensions. To install the developer (and documentation)
      dependencies, execute:

      .. code-block:: bash

        $ pip install highcharts-stock[dev]

    * `pytest <https://docs.pytest.org/en/7.1.x/>`_ v.7.1 or higher
    * `pytest-cov <https://pytest-cov.readthedocs.io/en/latest/>`_ v.3.0 or higher
    * `pytest-xdist <https://pytest-xdist.readthedocs.io/en/latest/>`_ v.2.5 or higher
    * `python-dotenv <https://github.com/theskumar/python-dotenv>`_ v. 0.21 or higher

      .. note::

        `python-dotenv <https://github.com/theskumar/python-dotenv>`_ will fail silently if
        not available, as it will only leverage natural environment variables rather than
        a ``.env`` file in the runtime environment.

    * `pytz <https://pythonhosted.org/pytz/>`__ v.2022.1 or higher
    * `tox <https://tox.wiki/en/latest/>`__ v.4.0.0 or higher

  .. tab:: Documentation

    .. warning::

      You will not be able to generate documentation without Sphinx and a number of
      necessary extensions. To install the documentation dependencies, execute:

      .. code-block:: bash

        $ pip install highcharts-stock[docs]

    * `Sphinx <https://www.sphinx-doc.org/en/master/>`_ v.6.1.3 or higher
    * `Sphinx RTD Theme <https://sphinx-themes.org/sample-sites/sphinx-rtd-theme/>`_ v.1.2
      or higher
    * `sphinx-tabs <https://sphinx-tabs.readthedocs.io/>`_ v.3.4.1 or higher
    * `Sphinx Toolbox <https://sphinx-toolbox.readthedocs.io/en/latest/>`_ v.3.4 or higher

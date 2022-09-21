from typing import Optional

from validator_collection import validators, checkers

from highcharts_python import constants, errors
from highcharts_python.decorators import validate_types
from highcharts_python.options import HighchartsOptions
from highcharts_python.js_literal_functions import serialize_to_js_literal
from highcharts_python.headless_export import ExportServer
from highcharts_python.options.series.series_generator import (create_series_obj,
                                                               SERIES_CLASSES,
                                                               STOCK_SERIES_LIST)
from highcharts_python.global_options.shared_options import SharedStockOptions

from highcharts_stock.options import HighchartsStockOptions

from highcharts_python.chart import Chart as ChartBase


class Chart(ChartBase):
    """Python representation of a Highcharts ``Chart`` object."""

    def __init__(self, **kwargs):
        self._callback = None
        self._container = None
        self._options = None
        self._variable_name = None

        self._is_stock_chart = None

        self.callback = kwargs.get('callback', None)
        self.container = kwargs.get('container', None)
        self.options = kwargs.get('options', None)
        self.variable_name = kwargs.get('variable_name', None)

        self.is_stock_chart = kwargs.get('is_stock_chart', False)

    def _repr_html_(self):
        """Produce the HTML representation of the chart.

        .. note::

          Currently includes *all* `Highcharts JS <https://www.highcharts.com/>`__ or
          `Highcharts Stock <https://www.highcharts.com/products/stock/>`__ modules
          in the HTML. This issue will be addressed when roadmap issue :issue:`2` is
          released.

        :returns: The HTML representation of the chart.
        :rtype: :class:`str <python:str>`
        """
        if self.options.chart:
            height = self.options.chart.height or 400
        else:
            height = 400

        container_str = f"""<div id=\"{self.container}\" style=\"width:100%; height:{height};\"></div>\n"""
        as_str = self.to_js_literal()
        script_str = '<script>\n' + as_str + '\n</script>'

        html_str = container_str + script_str

        return html_str

    @property
    def options(self) -> Optional[HighchartsOptions | HighchartsStockOptions]:
        """The Python representation of the `Highcharts <https://highcharts.com>`_
        ``options`` `configuration object <https://api.highcharts.com/highcharts/>`_
        Defaults to :obj:`None <python:None>`.

        :rtype: :class:`HighchartsOptions` or :class:`HighchartsStockOptions` or
          :obj:`None <python:None>`
        """
        return self._options

    @options.setter
    def options(self, value):
        if not value:
            self._options = None
        elif self.is_stock_chart:
            self._options = validate_types(value, HighchartsStockOptions)
        else:
            if checkers.is_type(value, 'HighchartsStockOptions'):
                self._options = value
                self.is_stock_chart = True
            elif checkers.is_type(value, 'HighchartsOptions'):
                self._options = value
            elif ('navigator' in value
                  or 'scrollbar' in value
                  or 'rangeSelector' in value
                  or 'range_selector' in value
                  or 'stockTools' in value
                  or 'stock_tools' in value):
                self._options = validate_types(value, HighchartsStockOptions)
                self.is_stock_chart = True
            else:
                self._options = validate_types(value, HighchartsOptions)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'callback': as_dict.get('callback', None),
            'container': as_dict.get('container', None) or as_dict.get('renderTo', None),
            'options': as_dict.get('options', None) or as_dict.get('userOptions', None),
            'variable_name': as_dict.get('variable_name',
                                         None) or as_dict.get('variableName', None),

            'is_stock_chart': as_dict.get('is_stock_chart', False),
        }

        return kwargs

    def to_js_literal(self,
                      filename = None,
                      encoding = 'utf-8') -> Optional[str]:
        """Return the object represented as a :class:`str <python:str>` containing the
        JavaScript object literal.

        :param filename: The name of a file to which the JavaScript object literal should
          be persisted. Defaults to :obj:`None <python:None>`
        :type filename: Path-like

        :param encoding: The character encoding to apply to the resulting object. Defaults
          to ``'utf-8'``.
        :type encoding: :class:`str <python:str>`

        .. note::

          If :meth:`variable_name <Chart.variable_name>` is set, will render a string as
          a new JavaScript instance invocation in the (pseudo-code) form:

          .. code-block:: javascript

            new VARIABLE_NAME = new Chart(...);

          If :meth:`variable_name <Chart.variable_name>` is not set, will simply return
          the ``new Chart(...)`` portion in the string.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        if filename:
            filename = validators.path(filename)

        untrimmed = self._to_untrimmed_dict()
        as_dict = {}
        for key in untrimmed:
            item = untrimmed[key]
            serialized = serialize_to_js_literal(item, encoding = encoding)
            if serialized is not None:
                as_dict[key] = serialized

        signature_elements = 0

        container_as_str = ''
        if self.container:
            container_as_str = f"""renderTo = '{self.container}'"""
            signature_elements += 1

        options_as_str = ''
        if self.options:
            options_as_str = self.options.to_js_literal(encoding = encoding)
            options_as_str = f"""options = {options_as_str}"""
            signature_elements += 1

        callback_as_str = ''
        if self.callback:
            callback_as_str = self.callback.to_js_literal(encoding = encoding)
            callback_as_str = f"""callback = {callback_as_str}"""
            signature_elements += 1

        signature = """new Highcharts.chart("""
        if self.is_stock_chart:
            signature = """new Highcharts.stockChart("""
        if container_as_str:
            signature += container_as_str
            if signature_elements > 1:
                signature += ',\n'
        if options_as_str:
            signature += options_as_str
            if signature_elements > 1:
                signature += ',\n'
        if callback_as_str:
            signature += callback_as_str
        signature += ');'

        constructor_prefix = ''
        if self.variable_name:
            constructor_prefix = f'var {self.variable_name} = '

        as_str = constructor_prefix + signature

        prefix = """document.addEventListener('DOMContentLoaded', function() {\n"""
        suffix = """});"""
        as_str = prefix + as_str + '\n' + suffix

        if filename:
            with open(filename, 'w', encoding = encoding) as file_:
                file_.write(as_str)

        return as_str

    def download_chart(self,
                       format = 'png',
                       scale = 1,
                       width = None,
                       filename = None,
                       auth_user = None,
                       auth_password = None,
                       timeout = 0.5,
                       server_instance = None,
                       **kwargs):
        """Export a downloaded form of the chart using a Highcharts :term:`Export Server`.

        :param filename: The name of the file where the exported chart should (optionally)
          be persisted. Defaults to :obj:`None <python:None>`.
        :type filename: Path-like or :obj:`None <python:None>`

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

        :param server_instance: Provide an already-configured :class:`ExportServer`
          instance to use to programmatically produce the exported chart. Defaults to
          :obj:`None <python:None>`, which causes Highcharts for Python to instantiate
          a new :class:`ExportServer` instance.
        :type server_instance: :class:`ExportServer` or :obj:`None <python:None>`

        .. note::

          All other keyword arguments are as per the :class:`ExportServer` constructor.

        :returns: The exported chart image, either as a :class:`bytes <python:bytes>`
          binary object or as a base-64 encoded string (depending on the ``use_base64``
          keyword argument).
        :rtype: :class:`bytes <python:bytes>` or :class:`str <python:str>`
        """
        if self.is_stock_chart:
            constructor = 'Stock'
        else:
            constructor = 'Chart'

        if not server_instance:
            return ExportServer.get_chart(filename = filename,
                                          auth_user = auth_user,
                                          auth_password = auth_password,
                                          timeout = timeout,
                                          options = self.options,
                                          constructor = constructor,
                                          scale = scale,
                                          width = width,
                                          **kwargs)

        if not isinstance(server_instance, ExportServer):
            raise errors.HighchartsValueError(f'server_instance is expected to be an '
                                              f'ExportServer instance. Was: '
                                              f'{server_instance.__class__.__name__}')

        return server_instance.request_chart(filename = filename,
                                             auth_user = auth_user,
                                             auth_password = auth_password,
                                             timeout = timeout,
                                             options = self.options,
                                             constructor = constructor,
                                             **kwargs)

    def add_series(self, *series):
        """Adds ``series`` to the
        :meth:`Chart.options.series <highcharts_python.options.HighchartsOptions.series>`
        property.

        :param series: One or more :term:`series` instances (descended from
          :class:`SeriesBase <highcharts_python.options.series.base.SeriesBase>`) or an
          instance (e.g. :class:`dict <python:dict>`, :class:`str <python:str>`, etc.)
          coercable to one
        :type series: one or more
          :class:`SeriesBase <highcharts_python.options.series.base.SeriesBase>`
          or coercable

        """
        new_series = []
        for item in series:
            item_series = create_series_obj(item)
            new_series.append(item_series)

        if self.options and self.options.series:
            existing_series = [x for x in self.options.series]
        elif self.options:
            existing_series = []
        else:
            existing_series = []
            if self.is_stock_chart:
                self.options = HighchartsStockOptions()
            else:
                self.options = HighchartsOptions()

        updated_series = existing_series + new_series

        self.options.series = updated_series

    @classmethod
    def from_series(cls, *series, kwargs = None):
        """Creates a new :class:`Chart <highcharts_python.chart.Chart>` instance populated
        with ``series``.

        :param series: One or more :term:`series` instances (descended from
          :class:`SeriesBase <highcharts_python.options.series.base.SeriesBase>`) or an
          instance (e.g. :class:`dict <python:dict>`, :class:`str <python:str>`, etc.)
          coercable to one
        :type series: one or more
          :class:`SeriesBase <highcharts_python.options.series.base.SeriesBase>`
          or
          :class:`IndicatorSeriesBase <highcharts_stock.options.series.base.IndicatorSeriesBase>`
          coercable

        :param kwargs: Other properties to use as keyword arguments for the instance to be
          created.

          .. warning::

            If ``kwargs`` sets the
            :meth:`options.series <highcharts_python.options.HighchartsOptions.series>`
            property, that setting will be *overridden* by the contents of ``series``.

        :type kwargs: :class:`dict <python:dict>`

        :returns: A new :class:`Chart <highcharts_python.chart.Chart>` instance
        :rtype: :class:`Chart <highcharts_python.chart.Chart>`
        """
        kwargs = validators.dict(kwargs, allow_empty = True) or {}
        instance = cls(**kwargs)

        instance.add_series(series)

    def display(self, global_options = None):
        """Display the chart in `Jupyter Labs <https://jupyter.org/>`_ or
        `Jupyter Notebooks <https://jupyter.org/>`_.

        :raises HighchartsDependencyError: if
          `ipython <https://ipython.readthedocs.io/en/stable/>`_ is not available in the
          runtime environment
        """
        try:
            from IPython import display
        except ImportError:
            raise errors.HighchartsDependencyError('Unable to import IPython.display. '
                                                   'Make sure that it is available in '
                                                   'your runtime environment. To install,'
                                                   'use: pip install ipython')

        if global_options is not None:
            global_options = validate_types(global_options,
                                            types = SharedStockOptions)

        if self.is_stock_chart:
            include_str = constants.STOCK_INCLUDE_STR
        else:
            include_str = constants.INCLUDE_STR

        html_str = include_str + '\n'
        if global_options:
            html_str += global_options._repr_html_() + '\n'
        html_str += self._repr_html_()

        display.display_html(html_str, raw = True)

    @staticmethod
    def _get_options_obj(series_type, options_kwargs):
        """Return an :class:`Options` descendent based on the series type.

        :param series_type: Indicates the series type that should be created from the CSV
          data.
        :type series_type: :class:`str <python:str>`

        :param options_kwargs: A :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the :class:`Options`
          instance. Defaults to :obj:`None <python:None>`.

          .. warning::

            If ``options_kwargs`` contains a ``series`` key, the ``series`` value will be
            *overwritten*. The ``series`` value will be created from the CSV file instead.

        :type options_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`

        :returns: An :class:`Options` descendent.
        :rtype: :class:`HighchartsOptions` or :class:`HighchartsStockOptions`
        """
        series_type = validators.string(series_type, allow_empty = False)
        series_type = series_type.lower()
        if series_type not in SERIES_CLASSES:
            raise errors.HighchartsValueError(f'series_type expects a valid Highcharts '
                                              f'series type. Received: {series_type}')

        options_kwargs = validators.dict(options_kwargs, allow_empty = True) or {}

        if series_type not in STOCK_SERIES_LIST:
            options = HighchartsOptions(**options_kwargs)
        else:
            options = HighchartsStockOptions(**options_kwargs)

        return options

    @classmethod
    def from_csv(cls,
                 as_string_or_file,
                 property_column_map,
                 series_type,
                 has_header_row = True,
                 series_kwargs = None,
                 options_kwargs = None,
                 chart_kwargs = None,
                 delimiter = ',',
                 null_text = 'None',
                 wrapper_character = "'",
                 line_terminator = '\r\n',
                 wrap_all_strings = False,
                 double_wrapper_character_when_nested = False,
                 escape_character = "\\",
                 is_stock_chart = False):
        """Create a new :class:`Chart <highcharts_python.chart.Chart>` instance with
        data populated from a CSV string or file.

          .. note::

            For an example
            :class:`LineSeries <highcharts_python.options.series.area.LineSeries>`, the
            minimum code required would be:

              .. code-block:: python

                my_chart = Chart.from_csv('some-csv-file.csv',
                                          property_column_map = {
                                              'x': 0,
                                              'y': 3,
                                              'id': 'id'
                                          },
                                          series_type = 'line')

            As the example above shows, data is loaded into the ``my_chart`` instance
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

        :param series_type: Indicates the series type that should be created from the CSV
          data.
        :type series_type: :class:`str <python:str>`

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

        :type series_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`

        :param options_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the :class:`HighchartsOptions`
          instance. Defaults to :obj:`None <python:None>`.

          .. warning::

            If ``options_kwargs`` contains a ``series`` key, the ``series`` value will be
            *overwritten*. The ``series`` value will be created from the CSV file instead.

        :type options_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`

        :param chart_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the :class:`Chart` instance.
          Defaults to :obj:`None <python:None>`.

          .. warning::

            If ``chart_kwargs`` contains an ``options`` key, ``options`` will be
            *overwritten*. The ``options`` value will be created from the
            ``options_kwargs`` and CSV file instead.

        :type chart_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`

        :param delimiter: The delimiter used between columns. Defaults to ``,``.
        :type delimiter: :class:`str <python:str>`

        :param wrapper_character: The string used to wrap string values when
          wrapping is applied. Defaults to ``'``.
        :type wrapper_character: :class:`str <python:str>`

        :param null_text: The string used to indicate an empty value if empty
          values are wrapped. Defaults to `None`.
        :type null_text: :class:`str <python:str>`

        :param line_terminator: The string used to indicate the end of a line/record in
          the CSV data. Defaults to ``'\\r\\n'``.

          .. note::

            The Python :mod:`csv <python:csv>` currently ignores the ``line_terminator``
            parameter and always applies ``'\\r\\n'``, by design. The Python docs say this
            may change in the future, so for future backwards compatibility we are
            including it here.

        :type line_terminator: :class:`str <python:str>`

        :param wrap_all_strings: If ``True``, indicates that the CSV file has all string
          data values wrapped in quotation marks. Defaults to ``False``.

          .. warning::

            If set to ``True``, the :mod:`csv <python:csv>` module will try to coerce
            any value that is *not* wrapped in quotation marks to a
            :class:`float <python:float>`. This can cause unexpected behavior, and
            typically we recommend leaving this as ``False`` and then re-casting values
            after they have been parsed.

        :type wrap_all_strings: :class:`bool <python:bool>`

        :param double_wrapper_character_when_nested: If ``True``, quote character is
          doubled when appearing within a string value. If ``False``, the
          ``escape_character`` is used to prefix quotation marks. Defaults to ``False``.
        :type double_wrapper_character_when_nested: :class:`bool <python:bool>`

        :param escape_character: A one-character string that indicates the character used
          to escape quotation marks if they appear within a string value that is already
          wrapped in quotation marks. Defaults to ``\\\\`` (which is Python for ``'\\'``,
          which is Python's native escape character).
        :type escape_character: :class:`str <python:str>`

        :param is_stock_chart: If ``True``, indicates that the chart should be
          instantiated as a **Highcharts Stock for Python** chart. Defaults to ``False``.
        :type is_stock_chart: :class:`bool <python:bool>`

        :returns: A :class:`Chart <highcharts_python.chart.Chart>` instance with its
          data populated from the CSV data.
        :rtype: :class:`Chart <highcharts_python.chart.Chart>`

        :raises HighchartsCSVDeserializationError: if ``property_column_map`` references
          CSV columns by their label, but the CSV data does not contain a header row

        """
        chart_kwargs = validators.dict(chart_kwargs, allow_empty = True) or {}

        options = cls._get_options_obj(series_type, options_kwargs)

        series_cls = SERIES_CLASSES.get(series_type, None)

        series = series_cls.from_csv(as_string_or_file,
                                     property_column_map,
                                     has_header_row = has_header_row,
                                     series_kwargs = series_kwargs,
                                     delimiter = delimiter,
                                     null_text = null_text,
                                     wrapper_character = wrapper_character,
                                     line_terminator = line_terminator,
                                     wrap_all_strings = wrap_all_strings,
                                     double_wrapper_character_when_nested = double_wrapper_character_when_nested,
                                     escape_character = escape_character)

        options.series = [series]

        instance = cls(**chart_kwargs)
        instance.options = options

        return instance

    @classmethod
    def from_pandas(cls,
                    df,
                    property_map,
                    series_type,
                    series_kwargs = None,
                    options_kwargs = None,
                    chart_kwargs = None):
        """Create a :class:`Chart <highcharts_python.chart.Chart>` instance whose
        data is populated from a `pandas <https://pandas.pydata.org/>`_
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

        :param series_type: Indicates the series type that should be created from the data
          in ``df``.
        :type series_type: :class:`str <python:str>`

        :param series_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the series instance. Defaults
          to :obj:`None <python:None>`.

          .. warning::

            If ``series_kwargs`` contains a ``data`` key, its value will be *overwritten*.
            The ``data`` value will be created from ``df`` instead.

        :type series_kwargs: :class:`dict <python:dict>`

        :param options_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the :class:`HighchartsOptions`
          instance. Defaults to :obj:`None <python:None>`.

          .. warning::

            If ``options_kwargs`` contains a ``series`` key, the ``series`` value will be
            *overwritten*. The ``series`` value will be created from the data in ``df``.

        :type options_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`

        :param chart_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the :class:`Chart` instance.
          Defaults to :obj:`None <python:None>`.

          .. warning::

            If ``chart_kwargs`` contains an ``options`` key, ``options`` will be
            *overwritten*. The ``options`` value will be created from the
            ``options_kwargs`` and the data in ``df`` instead.

        :type chart_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`

        :returns: A :class:`Chart <highcharts_python.chart.Chart>` instance with its
          data populated from the data in ``df``.
        :rtype: :class:`Chart <highcharts_python.chart.Chart>`

        :raises HighchartsPandasDeserializationError: if ``property_map`` references
          a column that does not exist in the data frame
        :raises HighchartsDependencyError: if `pandas <https://pandas.pydata.org/>`_ is
          not available in the runtime environment
        """
        chart_kwargs = validators.dict(chart_kwargs, allow_empty = True) or {}

        options = cls._get_options_obj(series_type, options_kwargs)

        series_cls = SERIES_CLASSES.get(series_type, None)

        series = series_cls.from_pandas(df,
                                        property_map,
                                        series_kwargs)

        options = HighchartsOptions(**options_kwargs)
        options.series = [series]

        instance = cls(**chart_kwargs)
        instance.options = options

        return instance

    @classmethod
    def from_pyspark(cls,
                     df,
                     property_map,
                     series_type,
                     series_kwargs = None,
                     options_kwargs = None,
                     chart_kwargs = None):
        """Create a :class:`Chart <highcharts_python.chart.Chart>` instance whose
        data is populated from a
        `PySpark <https://spark.apache.org/docs/latest/api/python/>`_
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

        :param series_type: Indicates the series type that should be created from the data
          in ``df``.
        :type series_type: :class:`str <python:str>`

        :param series_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the series instance. Defaults
          to :obj:`None <python:None>`.

          .. warning::

            If ``series_kwargs`` contains a ``data`` key, its value will be *overwritten*.
            The ``data`` value will be created from ``df`` instead.

        :type series_kwargs: :class:`dict <python:dict>`

        :param options_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the :class:`HighchartsOptions`
          instance. Defaults to :obj:`None <python:None>`.

          .. warning::

            If ``options_kwargs`` contains a ``series`` key, the ``series`` value will be
            *overwritten*. The ``series`` value will be created from the data in ``df``.

        :type options_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`

        :param chart_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the :class:`Chart` instance.
          Defaults to :obj:`None <python:None>`.

          .. warning::

            If ``chart_kwargs`` contains an ``options`` key, ``options`` will be
            *overwritten*. The ``options`` value will be created from the
            ``options_kwargs`` and the data in ``df`` instead.

        :type chart_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`

        :returns: A :class:`Chart <highcharts_python.chart.Chart>` instance with its
          data populated from the data in ``df``.
        :rtype: :class:`Chart <highcharts_python.chart.Chart>`

        :raises HighchartsPySparkDeserializationError: if ``property_map`` references
          a column that does not exist in the data frame
        :raises HighchartsDependencyError: if
          `PySpark <https://spark.apache.org/docs/latest/api/python/>`_ is not available
          in the runtime environment
        """
        chart_kwargs = validators.dict(chart_kwargs, allow_empty = True) or {}

        options = cls._get_options_obj(series_type, options_kwargs)

        series_cls = SERIES_CLASSES.get(series_type, None)

        series = series_cls.from_pyspark(df,
                                         property_map,
                                         series_kwargs)

        options = HighchartsOptions(**options_kwargs)
        options.series = [series]

        instance = cls(**chart_kwargs)
        instance.options = options

        return instance

    @classmethod
    def from_options(cls,
                     options,
                     chart_kwargs = None):
        """Create a :class:`Chart <highcharts_python.chart.Chart>` instance from a
        :class:`HighchartsOptions <highcharts_python.options.HighchartsOptions>` object.

        :param options: The configuration options to use to instantiate the chart.
        :type options:
          :class:`HighchartsOptions <highcharts_python.options.HighchartsOptions>` or
          coercable

        :param chart_kwargs: An optional :class:`dict <python:dict>` containing keyword
          arguments that should be used when instantiating the instance. Defaults to
          :obj:`None <python:None>`.

          .. warning::

            If ``chart_kwargs`` contains an ``options`` key, ``options`` will be
            *overwritten* by the contents of ``options``.

        :type chart_kwargs: :class:`dict <python:dict>` or :obj:`None <python:None>`

        :returns: The :class:`Chart <highcharts_python.chart.Chart>` instance
        :rtype: :class:`Chart <highcharts_python.chart.Chart>`
        """
        chart_kwargs = validators.dict(chart_kwargs, allow_empty = True) or {}
        if checkers.is_type(options, 'HighchartsStockOptions'):
            options = options
            chart_kwargs['is_stock_chart'] = True
        elif checkers.is_type(options, 'HighchartsOptions'):
            options = options
        elif ('navigator' in options
              or 'scrollbar' in options
              or 'rangeSelector' in options
              or 'range_selector' in options
              or 'stockTools' in options
              or 'stock_tools' in options):
            options = validate_types(options, HighchartsStockOptions)
            chart_kwargs['is_stock_chart'] = True
        else:
            options = validate_types(options, HighchartsOptions)

        instance = cls(**chart_kwargs)
        instance.options = options

        return instance

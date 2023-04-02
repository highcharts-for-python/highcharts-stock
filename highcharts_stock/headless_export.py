try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass
from typing import Optional

from validator_collection import checkers

from highcharts_core.headless_export import ExportServer as ExportServerBase

from highcharts_stock.decorators import validate_types
from highcharts_stock.options import HighchartsOptions, HighchartsStockOptions
from highcharts_stock.global_options.shared_options import SharedOptions, SharedStockOptions


class ExportServer(ExportServerBase):
    """Class that provides methods for interacting with the Highcharts
    `Export Server <https://github.com/highcharts/node-export-server>`_.

    .. note::

      By default, the :class:`ExportServer` class operates using the Highcharts-provided
      export server. If you wish to use your own (or a custom) export server, you can
      configure the class using either the :meth:`url <ExportServer.url>`,
      :meth:`port <ExportServer.port>`, and
      :meth:`path <ExportServer.path>` properties explicitly or by setting
      the ``HIGHCHARTS_EXPORT_SERVER_DOMAIN`, ``HIGHCHARTS_EXPORT_SERVER_PORT``, or
      ``HIGHCHARTS_EXPORT_SERVER_PATH`` environment variables.

    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def options(self) -> Optional[HighchartsOptions | HighchartsStockOptions]:
        """The :class:`HighchartsOptions` which should be applied to render the exported
        chart. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`HighchartsOptions` or :obj:`None <pythoN:None>`
        """
        return self._options

    @options.setter
    def options(self, value):
        if not value:
            self._options = None
        elif checkers.is_type(value, ('HighchartsStockOptions', 'HighchartsOptions')):
            self._options = value
        elif ('navigator' in value
              or 'scrollbar' in value
              or 'rangeSelector' in value
              or 'range_selector' in value
              or 'stockTools' in value
              or 'stock_tools' in value):
            self._options = validate_types(value, HighchartsStockOptions)
        else:
            self._options = validate_types(value, HighchartsOptions)

    @property
    def global_options(self) -> Optional[SharedOptions | SharedStockOptions]:
        """The global options which will be passed to the (JavaScript)
        ``Highcharts.setOptions()`` method, and which will be applied to the exported
        chart. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`SharedOptions` or :class:`SharedStockOptions` or
          :obj:`None <python:None>`
        """
        return self._global_options

    @global_options.setter
    def global_options(self, value):
        if not value:
            self._global_options = None
        else:
            if checkers.is_type(value, 'SharedStockOptions'):
                self._global_options = value
            elif checkers.is_type(value, 'SharedOptions'):
                self._global_options = value
            elif ('navigator' in value
                  or 'scrollbar' in value
                  or 'rangeSelector' in value
                  or 'range_selector' in value
                  or 'stockTools' in value
                  or 'stock_tools' in value):
                self._global_options = validate_types(value, SharedStockOptions)
            else:
                self._global_options = validate_types(value, SharedOptions)

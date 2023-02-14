from typing import Optional

from validator_collection import validators

from highcharts_core.global_options.language import Language as LanguageCore

from highcharts_stock.decorators import class_sensitive
from highcharts_stock.global_options.language.stock_tools import StockToolsLanguageOptions


class LanguageBase(LanguageCore):
    """Collection of configuration settings for UI strings that can be adapted for
    display in specific languages.

    .. note::

      The :class:`Language` object is a global setting in Highcharts and it *cannot* be
      set on each chart initialization. Instead, it has to be set using (in JavaScript)
      ``Highcharts.setOptions(...)`` before any chart is initialized.

    """

    def __init__(self, **kwargs):
        self._range_selector_from = None
        self._range_selector_to = None
        self._range_selector_zoom = None

        self.range_selector_from = kwargs.get('range_selector_from', None)
        self.range_selector_to = kwargs.get('range_selector_to', None)
        self.range_selector_zoom = kwargs.get('range_selector_zoom', None)

        super().__init__(**kwargs)

    @property
    def range_selector_from(self) -> Optional[str]:
        """The text for the label for the "from" input box in the :term:`range selector`.
        Defaults to ``''`` (an empty string).

        .. note::

          By default, this string is empty as the label is not rendered by default.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._range_selector_from

    @range_selector_from.setter
    def range_selector_from(self, value):
        self._range_selector_from = validators.string(value, allow_empty = True)

    @property
    def range_selector_to(self) -> Optional[str]:
        """The text for the label for the "to" input box in the :term:`range selector`.
        Defaults to ``'→'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._range_selector_to

    @range_selector_to.setter
    def range_selector_to(self, value):
        self._range_selector_to = validators.string(value, allow_empty = True)

    @property
    def range_selector_zoom(self) -> Optional[str]:
        """The text for the label :term:`range selector` buttons. Defaults to ``'Zoom'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._range_selector_zoom

    @range_selector_zoom.setter
    def range_selector_zoom(self, value):
        self._range_selector_zoom = validators.string(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'accessibility': as_dict.get('accessibility', None),
            'context_button_title': as_dict.get('contextButtonTitle', None),
            'decimal_point': as_dict.get('decimalPoint', None),
            'download_csv': as_dict.get('downloadCSV', None),
            'download_jpeg': as_dict.get('downloadJPEG', None),
            'download_pdf': as_dict.get('downloadPDF', None),
            'download_png': as_dict.get('downloadPNG', None),
            'download_svg': as_dict.get('downloadSVG', None),
            'download_xls': as_dict.get('downloadXLS', None),
            'drillup_text': as_dict.get('drillUpText', None),
            'exit_fullscreen': as_dict.get('exitFullscreen', None),
            'export_data': as_dict.get('exportData', None),
            'hide_data': as_dict.get('hideData', None),
            'invalid_date': as_dict.get('invalidDate', None),
            'loading': as_dict.get('loading', None),
            'main_breadcrumb': as_dict.get('mainBreadcrumb', None),
            'months': as_dict.get('months', None),
            'navigation': as_dict.get('navigation', None),
            'no_data': as_dict.get('noData', None),
            'numeric_symbol_magnitude': as_dict.get('numericSymbolMagnitude', None),
            'numeric_symbols': as_dict.get('numericSymbols', None),
            'print_chart': as_dict.get('printChart', None),
            'reset_zoom': as_dict.get('resetZoom', None),
            'reset_zoom_title': as_dict.get('resetZoomTitle', None),
            'short_months': as_dict.get('shortMonths', None),
            'short_weekdays': as_dict.get('shortWeekdays', None),
            'thousands_separator': as_dict.get('thousandsSep', None),
            'view_data': as_dict.get('viewData', None),
            'view_fullscreen': as_dict.get('viewFullscreen', None),
            'weekdays': as_dict.get('weekdays',  None),

            'range_selector_from': as_dict.get('rangeSelectorFrom', None),
            'range_selector_to': as_dict.get('rangeSelectorTo', None),
            'range_selector_zoom': as_dict.get('rangeSelectorZoom', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'rangeSelectorFrom': self.range_selector_from,
            'rangeSelectorTo': self.range_selector_to,
            'rangeSelectorZoom': self.range_selector_zoom,
        }

        parent_as_dict = super()._to_untrimmed_dict(in_cls = in_cls)

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed


class Language(LanguageBase):
    """Collection of configuration settings for UI strings that can be adapted for
    display in specific languages.

    .. note::

      The :class:`Language` object is a global setting in Highcharts and it *cannot* be
      set on each chart initialization. Instead, it has to be set using (in JavaScript)
      ``Highcharts.setOptions(...)`` before any chart is initialized.

    """

    def __init__(self, **kwargs):
        self._range_selector_from = None
        self._range_selector_to = None
        self._range_selector_zoom = None
        self._stock_tools = None

        self.range_selector_from = kwargs.get('range_selector_from', None)
        self.range_selector_to = kwargs.get('range_selector_to', None)
        self.range_selector_zoom = kwargs.get('range_selector_zoom', None)
        self.stock_tools = kwargs.get('stock_tools', None)

        super().__init__(**kwargs)

    @property
    def stock_tools(self) -> Optional[StockToolsLanguageOptions]:
        """Settings to configure the :term:`Stock Tools GUI` titles (hints) in the chart.

        :rtype: :class:`StockToolLanguageOptions <highcharts_stock.global_options.language.stock_tools.StockToolsLanguageOptions>`
          or :obj:`None <python:None>`
        """
        return self._stock_tools

    @stock_tools.setter
    @class_sensitive(StockToolsLanguageOptions)
    def stock_tools(self, value):
        self._stock_tools = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'accessibility': as_dict.get('accessibility', None),
            'context_button_title': as_dict.get('contextButtonTitle', None),
            'decimal_point': as_dict.get('decimalPoint', None),
            'download_csv': as_dict.get('downloadCSV', None),
            'download_jpeg': as_dict.get('downloadJPEG', None),
            'download_pdf': as_dict.get('downloadPDF', None),
            'download_png': as_dict.get('downloadPNG', None),
            'download_svg': as_dict.get('downloadSVG', None),
            'download_xls': as_dict.get('downloadXLS', None),
            'drillup_text': as_dict.get('drillUpText', None),
            'exit_fullscreen': as_dict.get('exitFullscreen', None),
            'export_data': as_dict.get('exportData', None),
            'hide_data': as_dict.get('hideData', None),
            'invalid_date': as_dict.get('invalidDate', None),
            'loading': as_dict.get('loading', None),
            'main_breadcrumb': as_dict.get('mainBreadcrumb', None),
            'months': as_dict.get('months', None),
            'navigation': as_dict.get('navigation', None),
            'no_data': as_dict.get('noData', None),
            'numeric_symbol_magnitude': as_dict.get('numericSymbolMagnitude', None),
            'numeric_symbols': as_dict.get('numericSymbols', None),
            'print_chart': as_dict.get('printChart', None),
            'reset_zoom': as_dict.get('resetZoom', None),
            'reset_zoom_title': as_dict.get('resetZoomTitle', None),
            'short_months': as_dict.get('shortMonths', None),
            'short_weekdays': as_dict.get('shortWeekdays', None),
            'thousands_separator': as_dict.get('thousandsSep', None),
            'view_data': as_dict.get('viewData', None),
            'view_fullscreen': as_dict.get('viewFullscreen', None),
            'weekdays': as_dict.get('weekdays',  None),

            'range_selector_from': as_dict.get('rangeSelectorFrom', None),
            'range_selector_to': as_dict.get('rangeSelectorTo', None),
            'range_selector_zoom': as_dict.get('rangeSelectorZoom', None),
            'stock_tools': as_dict.get('stock_tools', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'stockTools': self.stock_tools,
        }

        parent_as_dict = super()._to_untrimmed_dict(in_cls = in_cls)

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed

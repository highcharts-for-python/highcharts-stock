from typing import Optional, List

from validator_collection import validators

from highcharts_stock.metaclasses import HighchartsMeta
from highcharts_stock.decorators import class_sensitive
from highcharts_stock.options.stock_tools.definitions import StockToolsDefinitions


class StockToolsGUI(HighchartsMeta):
    """Definitions for the buttons shown in the Stock Tools GUI."""

    def __init__(self, **kwargs):
        self._buttons = None
        self._class_name = None
        self._definitions = None
        self._enabled = None
        self._toolbar_class_name = None

        self.buttons = kwargs.get('buttons', None)
        self.class_name = kwargs.get('class_name', None)
        self.definitions = kwargs.get('definitions', None)
        self.enabled = kwargs.get('enabled', None)
        self.toolbar_class_name = kwargs.get('toolbar_class_name', None)

    @property
    def buttons(self) -> Optional[List[str]]:
        """A collection of strings pointing to configuration options for each item to be
        shown in the toolbar. Each name refers to a unique key from the
        :meth:`.definitions <highcharts_stock.options.stock_tools.StockToolsGUI.definitions`
        setting.

        Defaults to:

          .. code-block:: python

            [
                'indicators',
                'separator',
                'simpleShapes',
                'lines',
                'crookedLines',
                'measure',
                'advanced',
                'toggleAnnotations',
                'separator',
                'verticalLabels',
                'flags',
                'separator',
                'zoomChange',
                'fullScreen',
                'typeChange',
                'separator',
                'currentPriceIndicator',
                'saveChart'
            ]

        :rtype: :class:`list <python:list>` of :class:`str <python:str>`, or
          :obj:`None <python:None>`
        """
        return self._buttons

    @buttons.setter
    def buttons(self, value):
        if not value:
            self._buttons = None
        else:
            value = validators.iterable(value)
            self._buttons = [validators.string(x) for x in value]

    @property
    def class_name(self) -> Optional[str]:
        """The CSS class name to apply to the stock tools DIV element. Defaults to
        ``'highcharts-bindings-wrapper'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._class_name

    @class_name.setter
    def class_name(self, value):
        self._class_name = validators.string(value, allow_empty = True)

    @property
    def definitions(self) -> Optional[StockToolsDefinitions]:
        """Configuration of the icons to use for the default Stock Tools GUI. If
        :obj:`None <python:None>`, applies the Highcharts Stock default icons.

        :rtype: :class:`StockToolsDefinitions` or :obj:`None <python:None>`
        """
        return self._definitions

    @definitions.setter
    @class_sensitive(StockToolsDefinitions)
    def definitions(self, value):
        self._definitions = value

    @property
    def enabled(self) -> Optional[bool]:
        """If ``True``, displays the *default* stock tools GUI. If ``False``, hides the
        stock tools GUI. Defaults to ``True``.

          .. seealso::

            * :ref:`Constructing a Custom Stock Tools GUI <custom_stock_tools_gui>`

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        if value is None:
            self._enabled = None
        else:
            self._enabled = bool(value)

    @property
    def toolbar_class_name(self) -> Optional[str]:
        """The CSS class name to apply to the container that holds the stock tools
        buttons. Defaults to ``'stocktools-toolbar'``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._toolbar_class_name

    @toolbar_class_name.setter
    def toolbar_class_name(self, value):
        self._toolbar_class_name = validators.string(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'buttons': as_dict.get('buttons', None),
            'class_name': as_dict.get('className', None),
            'definitions': as_dict.get('definitions', None),
            'enabled': as_dict.get('enabled', None),
            'toolbar_class_name': as_dict.get('toolbarClassName', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'buttons': self.buttons,
            'className': self.class_name,
            'definitions': self.definitions,
            'enabled': self.enabled,
            'toolbarClassName': self.toolbar_class_name,
        }

        return untrimmed


class StockTools(HighchartsMeta):
    """Configuration for the GUI which displays various tools for working with Highcharts
    Stock visualizations."""

    def __init__(self, **kwargs):
        self._gui = None

        self.gui = kwargs.get('gui', None)

    @property
    def _dot_path(self) -> Optional[str]:
        """The dot-notation path to the options key for the current class.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return 'stockTools'

    @property
    def gui(self) -> Optional[StockToolsGUI]:
        """Definitions for the buttons shown in the Stock Tools GUI.

        :rtype: :class:`StockToolsGUI` or :obj:`None <python:None`
        """
        return self._gui

    @gui.setter
    @class_sensitive(StockToolsGUI)
    def gui(self, value):
        self._gui = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'gui': as_dict.get('gui', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'gui': self.gui
        }

        return untrimmed

from typing import Optional

from highcharts_core.utility_classes.events import *

from highcharts_stock.utility_classes.javascript_functions import CallbackFunction
from highcharts_stock.metaclasses import HighchartsMeta
from highcharts_stock.decorators import class_sensitive


class RangeSelectorEvents(HighchartsMeta):
    """Event listeners for the range selector buttons."""

    def __init__(self, **kwargs):
        self._click = None

        for attribute in dir(self):
            if attribute.startswith('_') and not attribute.startswith('__'):
                non_private_name = attribute[1:]
                setattr(self, non_private_name, kwargs.get(non_private_name, None))

    @property
    def click(self) -> Optional[CallbackFunction]:
        """JavaScript callback function that fires when the user clicks on a button in
        the :term:`range selector`. One parameter, ``event``, is passed to the JavaScript
        function, containing common event information. Defaults to
        :obj:`None <python:None>`.

          .. tip::

            In the JavaScript function, Return ``false`` to stop the button's default
            click action.

        :rtype: :class:`CallbackFunction` or :obj:`None <python:None>`
        """
        return self._click

    @click.setter
    @class_sensitive(CallbackFunction)
    def click(self, value):
        self._click = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'click': as_dict.get('click', None)
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'click': self.click
        }

        return untrimmed

from typing import Optional

from validator_collection import validators

from highcharts_stock.decorators import class_sensitive
from highcharts_stock.metaclasses import HighchartsMeta
from highcharts_stock.utility_classes.data_labels import DataLabel


class LastPriceOptions(HighchartsMeta):
    """Configuration of a line marking the last price from a set of data points."""

    def __init__(self, **kwargs):
        self._color = None
        self._enabled = None
        self._label = None

        self.color = kwargs.get('color', None)
        self.enabled = kwargs.get('enabled', None)
        self.label = kwargs.get('label', None)

    @property
    def color(self) -> Optional[str]:
        """The color of the line. If :obj:`None <python:None>`, defaults to the same color
        as the series. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._color

    @color.setter
    def color(self, value):
        self._color = validators.string(value, allow_empty = True)

    @property
    def enabled(self) -> Optional[bool]:
        """If ``True``, displays the configured last price line. Defaults to ``False``.

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
    def label(self) -> Optional[DataLabel]:
        """The label applied to the last price indicator.

        :rtype: :class:`DataLabel <highcharts_stock.utility_classes.data_labels.DataLabel>`
          or :obj:`None <python:None>`
        """
        return self._label

    @label.setter
    @class_sensitive(DataLabel)
    def label(self, value):
        self._label = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'color': as_dict.get('color', None),
            'enabled': as_dict.get('enabled', None),
            'label': as_dict.get('label', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'color': self.color,
            'enabled': self.enabled,
            'label': self.label,
        }

        return untrimmed

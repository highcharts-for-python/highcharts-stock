from typing import Optional
from decimal import Decimal

from validator_collection import validators, checkers

from highcharts_stock import constants, errors
from highcharts_stock.decorators import class_sensitive
from highcharts_stock.options.series.data.base import DataBase
from highcharts_stock.options.plot_options.drag_drop import DragDropOptions
from highcharts_stock.utility_classes.data_labels import DataLabel


class HLCData(DataBase):
    """Data point that can be visualized in a
    :class:`HLCSeries <highcharts_stock.options.series.hlc.HLCSeries>`,
    featuring an ``x`` value, a ``high`` value, a ``low`` value, and a ``close`` value.
    """

    def __init__(self, **kwargs):
        self._close = None
        self._data_labels = None
        self._drag_drop = None
        self._high = None
        self._low = None
        self._x = None

        self.close = kwargs.get('close', None)
        self.data_labels = kwargs.get('data_labels', None)
        self.drag_drop = kwargs.get('drag_drop', None)
        self.high = kwargs.get('high', None)
        self.low = kwargs.get('low', None)
        self.x = kwargs.get('x', None)

        super().__init__(**kwargs)

    @property
    def close(self) -> Optional[int | float | Decimal]:
        """The closing value of the data point. Defaults to :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._close

    @close.setter
    def close(self, value):
        self._close = validators.numeric(value, allow_empty = True)

    @property
    def data_labels(self) -> Optional[DataLabel]:
        """Individual data label for the data point.

        :rtype: :class:`DataLabel` or :obj:`None <python:None>`
        """
        return self._data_labels

    @data_labels.setter
    @class_sensitive(DataLabel)
    def data_labels(self, value):
        self._data_labels = value

    @property
    def drag_drop(self) -> Optional[DragDropOptions]:
        """The draggable-points module allows points to be moved around or modified in the
        chart.

        In addition to the options mentioned under the dragDrop API structure, the module
        fires three (JavaScript) events:

          * ``point.dragStart``
          * ``point.drag``
          * ``point.drop``

        :rtype: :class:`DragDropOptions` or :obj:`None <python:None>`
        """
        return self._drag_drop

    @drag_drop.setter
    @class_sensitive(DragDropOptions)
    def drag_drop(self, value):
        self._drag_drop = value

    @property
    def high(self) -> Optional[int | float | Decimal]:
        """The high value of the data point. Defaults to :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._high

    @high.setter
    def high(self, value):
        self._high = validators.numeric(value, allow_empty = True)

    @property
    def low(self) -> Optional[int | float | Decimal]:
        """The low value of the data point. Defaults to :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._low

    @low.setter
    def low(self, value):
        self._low = validators.numeric(value, allow_empty = True)

    @property
    def x(self) -> Optional[int | float | Decimal | type(None) | constants.EnforcedNullType]:
        """The position of the data point on the X-axis. Defaults to
        :obj:`None <python:None>`.

        .. note::

          For datetime axes, the x-value should be expressed in milliseconds since 1970.

        :rtype: numeric or :class:`EnforcedNullType` or :obj:`None <python:None>`
        """
        return self._x

    @x.setter
    def x(self, value):
        if value is None or isinstance(value, constants.EnforcedNullType):
            self._x = None
        else:
            if checkers.is_datetime(value):
                value = validators.datetime(value)
                value = value.timestamp()

            self._x = validators.numeric(value)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        """Convenience method which returns the keyword arguments used to initialize the
        class from a Highcharts Javascript-compatible :class:`dict <python:dict>` object.

        :param as_dict: The HighCharts JS compatible :class:`dict <python:dict>`
          representation of the object.
        :type as_dict: :class:`dict <python:dict>`

        :returns: The keyword arguments that would be used to initialize an instance.
        :rtype: :class:`dict <python:dict>`

        """
        kwargs = {
            'accessibility': as_dict.get('accessibility', None),
            'class_name': as_dict.get('className', None),
            'color': as_dict.get('color', None),
            'color_index': as_dict.get('colorIndex', None),
            'custom': as_dict.get('custom', None),
            'description': as_dict.get('description', None),
            'events': as_dict.get('events', None),
            'id': as_dict.get('id', None),
            'label_rank': as_dict.get('labelRank',
                                      None) or as_dict.get('labelrank',
                                                           None),
            'name': as_dict.get('name', None),
            'selected': as_dict.get('selected', None),

            'close': as_dict.get('close', None),
            'data_labels': as_dict.get('dataLabels', None),
            'drag_drop': as_dict.get('dragDrop', None),
            'high': as_dict.get('high', None),
            'low': as_dict.get('low', None),
            'x': as_dict.get('x', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'close': self.close,
            'dataLabels': self.data_labels,
            'dragDrop': self.drag_drop,
            'high': self.high,
            'low': self.low,
            'x': self.x,
        }

        parent_as_dict = super()._to_untrimmed_dict(in_cls = in_cls) or {}

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed

    @classmethod
    def from_array(cls, value):
        if not value:
            return []
        elif not checkers.is_iterable(value):
            value = [value]

        collection = []
        for item in value:
            if checkers.is_type(item, 'DataBase'):
                as_obj = item
            elif checkers.is_dict(item):
                as_obj = cls.from_dict(item)
            elif item is None or isinstance(item, constants.EnforcedNullType):
                as_obj = cls()
            elif checkers.is_iterable(item):
                if len(item) == 4:
                    as_obj = cls(x = item[0],
                                 high = item[1],
                                 low = item[2],
                                 close = item[3])
                elif len(item == 3):
                    as_obj = cls(high = item[0],
                                 low = item[1],
                                 close = item[2])
                else:
                    raise errors.HighchartsValueError(f'HLCData.from_array() '
                                                      f'expects either a 4-member '
                                                      f'iterable, a 3-member iterable, '
                                                      f'an iterable of data point '
                                                      f'objects, or instances coercable '
                                                      f'to data point objects. Received: '
                                                      f'{len(item)}-member iterable.')
            else:
                raise errors.HighchartsValueError(f'each data point supplied must either '
                                                  f'be a DataBase Data Point or be '
                                                  f'coercable to one. Could not coerce: '
                                                  f'{item}')
            collection.append(as_obj)

        return collection


class OHLCData(HLCData):
    """Data point that can be visualized in a
    :class:`OHLCSeries <highcharts_stock.options.series.hlc.OHLCSeries>`,
    featuring an ``x`` value, an ``open`` value, a ``high`` value, a ``low`` value, and a
    ``close`` value.
    """

    def __init__(self, **kwargs):
        self._open = None

        self.open = kwargs.get('open', None)

        super().__init__(**kwargs)

    @property
    def open(self) -> Optional[int | float | Decimal]:
        """The opening value of the data point. Defaults to :obj:`None <python:None>`.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._open

    @open.setter
    def open(self, value):
        self._open = validators.numeric(value, alopen_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        """Convenience method which returns the keyword arguments used to initialize the
        class from a Highcharts Javascript-compatible :class:`dict <python:dict>` object.

        :param as_dict: The HighCharts JS compatible :class:`dict <python:dict>`
          representation of the object.
        :type as_dict: :class:`dict <python:dict>`

        :returns: The keyword arguments that would be used to initialize an instance.
        :rtype: :class:`dict <python:dict>`

        """
        kwargs = {
            'accessibility': as_dict.get('accessibility', None),
            'class_name': as_dict.get('className', None),
            'color': as_dict.get('color', None),
            'color_index': as_dict.get('colorIndex', None),
            'custom': as_dict.get('custom', None),
            'description': as_dict.get('description', None),
            'events': as_dict.get('events', None),
            'id': as_dict.get('id', None),
            'label_rank': as_dict.get('labelRank',
                                      None) or as_dict.get('labelrank',
                                                           None),
            'name': as_dict.get('name', None),
            'selected': as_dict.get('selected', None),

            'close': as_dict.get('close', None),
            'data_labels': as_dict.get('dataLabels', None),
            'drag_drop': as_dict.get('dragDrop', None),
            'high': as_dict.get('high', None),
            'low': as_dict.get('low', None),
            'open': as_dict.get('open', None),
            'x': as_dict.get('x', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'open': self.open,
        }

        parent_as_dict = super()._to_untrimmed_dict(in_cls = in_cls) or {}

        for key in parent_as_dict:
            untrimmed[key] = parent_as_dict[key]

        return untrimmed

    @classmethod
    def from_array(cls, value):
        if not value:
            return []
        elif not checkers.is_iterable(value):
            value = [value]

        collection = []
        for item in value:
            if checkers.is_type(item, 'DataBase'):
                as_obj = item
            elif checkers.is_dict(item):
                as_obj = cls.from_dict(item)
            elif item is None or isinstance(item, constants.EnforcedNullType):
                as_obj = cls()
            elif checkers.is_iterable(item):
                if len(item) == 5:
                    as_obj = cls(x = item[0],
                                 open = item[1],
                                 high = item[2],
                                 low = item[3],
                                 close = item[4])
                elif len(item == 4):
                    as_obj = cls(open = item[0],
                                 high = item[1],
                                 low = item[2],
                                 close = item[3])
                else:
                    raise errors.HighchartsValueError(f'OHLCData.from_array() '
                                                      f'expects either a 5-member '
                                                      f'iterable, a 4-member iterable, '
                                                      f'an iterable of data point '
                                                      f'objects, or instances coercable '
                                                      f'to data point objects. Received: '
                                                      f'{len(item)}-member iterable.')
            else:
                raise errors.HighchartsValueError(f'each data point supplied must either '
                                                  f'be a DataBase Data Point or be '
                                                  f'coercable to one. Could not coerce: '
                                                  f'{item}')
            collection.append(as_obj)

        return collection

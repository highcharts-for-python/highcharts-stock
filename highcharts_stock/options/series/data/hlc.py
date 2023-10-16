from typing import Optional, List, Dict
from decimal import Decimal

from validator_collection import validators, checkers

from highcharts_stock import constants, errors
from highcharts_stock.decorators import class_sensitive
from highcharts_stock.options.series.data.base import DataBase
from highcharts_stock.options.series.data.collections import DataPointCollection
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
                value = value.timestamp() * 1000

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
    def _get_supported_dimensions(cls) -> List[int]:
        """Returns a list of the supported dimensions for the data point.
        
        :rtype: :class:`list <python:list>` of :class:`int <python:int>`
        """
        return [6, 5, 4, 3]

    @classmethod
    def from_ndarray(cls, value):
        """Creates a collection of data points from a `NumPy <https://numpy.org>`__ 
        :class:`ndarray <numpy:ndarray>` instance.
        
        :returns: A collection of data point values.
        :rtype: :class:`DataPointCollection <highcharts_core.options.series.data.collections.DataPointCollection>`
        """
        return HLCDataCollection.from_ndarray(value)
    
    @classmethod
    def _get_props_from_array(cls, length = None) -> List[str]:
        """Returns a list of the property names that can be set using the
        :meth:`.from_array() <highcharts_core.options.series.data.base.DataBase.from_array>`
        method.
        
        :param length: The length of the array, which may determine the properties to 
          parse. Defaults to :obj:`None <python:None>`, which returns the full list of 
          properties.
        :type length: :class:`int <python:int>` or :obj:`None <python:None>`
        
        :rtype: :class:`list <python:list>` of :class:`str <python:str>`
        """
        prop_list = {
            None: ['x', 'open', 'high', 'low', 'close', 'name'],
            6: ['x', 'open', 'high', 'low', 'close', 'name'],
            5: ['x', 'open', 'high', 'low', 'close'],
            4: ['x', 'high', 'low', 'close'],
            3: ['high', 'low', 'close'],
        }
        return cls._get_props_from_array_helper(prop_list, length)

    @classmethod
    def from_list(cls, value):
        if not value:
            return []
        elif checkers.is_string(value):
            try:
                value = validators.json(value)
            except (ValueError, TypeError):
                pass
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
                if len(item) == 6:
                    as_obj = cls(x = item[0],
                                 high = item[2],
                                 low = item[3],
                                 close = item[4])
                elif len(item) == 5:
                    as_obj = cls(x = item[0],
                                 high = item[2],
                                 low = item[3],
                                 close = item[4])
                elif len(item) == 4:
                    as_obj = cls(x = item[0],
                                 high = item[1],
                                 low = item[2],
                                 close = item[3])
                elif len(item) == 3:
                    as_obj = cls(high = item[0],
                                 low = item[1],
                                 close = item[2])
                else:
                    raise errors.HighchartsValueError(f'HLCData.from_array() '
                                                      f'expects either a 6-member '
                                                      f'iterable, a 5-member iterable ',
                                                      f'a 4-member iterable, '
                                                      f'a 3-member iterable, '
                                                      f'an iterable of data point '
                                                      f'objects, or instances coercable '
                                                      f'to data point objects. Received: '
                                                      f'{len(item)}-member iterable.')
            else:
                raise errors.HighchartsValueError(f'each data point supplied must either '
                                                  f'be a DataBase Data Point or be '
                                                  f'coercable to one. Could not coerce: '
                                                  f'{item}')
            if checkers.is_string(as_obj.x) and not as_obj.name:
                as_obj.name = as_obj.x
                as_obj.x = None

            collection.append(as_obj)

        return collection

    def to_array(self, force_object = False) -> List | Dict:
        """Generate the array representation of the data point (the inversion 
        of 
        :meth:`.from_array() <highcharts_core.options.series.data.base.DataBase.from_array>`).
        
        .. warning::
        
          If the data point *cannot* be serialized to a JavaScript array,
          this method will instead return the untrimmed :class:`dict <python:dict>`
          representation of the data point as a fallback.

        :param force_object: if ``True``, forces the return of the instance's
          untrimmed :class:`dict <python:dict>` representation. Defaults to ``False``.
        :type force_object: :class:`bool <python:bool>`

        :returns: The array representation of the data point.
        :rtype: :class:`list <python:list>` of values or :class:`dict <python:dict>`
        """
        if self.requires_js_object or force_object:
            return self._to_untrimmed_dict()
        
        if self.x is not None:
            x = self.x
        elif self.name is not None:
            x = self.name
        else:
            x = constants.EnforcedNull
            
        if self.high is not None:
            high = self.high
        else:
            high = constants.EnforcedNull

        if self.low is not None:
            low = self.low
        else:
            low = constants.EnforcedNull
            
        if self.close is not None:
            close = self.close
        else:
            close = constants.EnforcedNull
            
        if self.x is None and self.name is None:
            return [high, low, close]

        return [x, high, low, close]


class HLCDataCollection(DataPointCollection):
    """A collection of :class:`HLCData` objects.

    .. note::
    
      When serializing to JS literals, if possible, the collection is serialized to a primitive
      array to boost performance within Python *and* JavaScript. However, this may not always be
      possible if data points have non-array-compliant properties configured (e.g. adjusting their 
      style, names, identifiers, etc.). If serializing to a primitive array is not possible, the
      results are serialized as JS literal objects.

    """

    @classmethod
    def _get_data_point_class(cls):
        """The Python class to use as the underlying data point within the Collection.
        
        :rtype: class object
        """
        return HLCData


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
    def from_list(cls, value):
        if not value:
            return []
        elif checkers.is_string(value):
            try:
                value = validators.json(value)
            except (ValueError, TypeError):
                pass
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
                if len(item) == 6:
                    as_obj = cls(x = item[0],
                                 open = item[1],
                                 high = item[2],
                                 low = item[3],
                                 close = item[4])
                elif len(item) == 5:
                    as_obj = cls(x = item[0],
                                 open = item[1],
                                 high = item[2],
                                 low = item[3],
                                 close = item[4])
                elif len(item) == 4:
                    as_obj = cls(open = item[0],
                                 high = item[1],
                                 low = item[2],
                                 close = item[3])
                else:
                    raise errors.HighchartsValueError(f'OHLCData.from_array() '
                                                      f'expects either a 6-member '
                                                      f'iterable, a 5-member iterable, '
                                                      f'a 4-member iterable, '
                                                      f'an iterable of data point '
                                                      f'objects, or instances coercable '
                                                      f'to data point objects. Received: '
                                                      f'{len(item)}-member iterable.')
            else:
                raise errors.HighchartsValueError(f'each data point supplied must either '
                                                  f'be a DataBase Data Point or be '
                                                  f'coercable to one. Could not coerce: '
                                                  f'{item}')
            if checkers.is_string(as_obj.x) and not as_obj.name:
                as_obj.name = as_obj.x
                as_obj.x = None

            collection.append(as_obj)

        return collection

    @classmethod
    def _get_supported_dimensions(cls) -> List[int]:
        """Returns a list of the supported dimensions for the data point.
        
        :rtype: :class:`list <python:list>` of :class:`int <python:int>`
        """
        return [6, 5, 4]

    @classmethod
    def from_ndarray(cls, value):
        """Creates a collection of data points from a `NumPy <https://numpy.org>`__ 
        :class:`ndarray <numpy:ndarray>` instance.
        
        :returns: A collection of data point values.
        :rtype: :class:`DataPointCollection <highcharts_core.options.series.data.collections.DataPointCollection>`
        """
        return OHLCDataCollection.from_ndarray(value)

    @classmethod
    def _get_props_from_array(cls, length = None) -> List[str]:
        """Returns a list of the property names that can be set using the
        :meth:`.from_array() <highcharts_core.options.series.data.base.DataBase.from_array>`
        method.
        
        :param length: The length of the array, which may determine the properties to 
          parse. Defaults to :obj:`None <python:None>`, which returns the full list of 
          properties.
        :type length: :class:`int <python:int>` or :obj:`None <python:None>`
        
        :rtype: :class:`list <python:list>` of :class:`str <python:str>`
        """
        prop_list = {
            None: ['x', 'open', 'high', 'low', 'close', 'name'],
            6: ['x', 'open', 'high', 'low', 'close', 'name'],
            5: ['x', 'open', 'high', 'low', 'close'],
            4: ['x', 'high', 'low', 'close'],
        }
        return prop_list[length]

    def to_array(self, force_object = False) -> List | Dict:
        """Generate the array representation of the data point (the inversion 
        of 
        :meth:`.from_array() <highcharts_core.options.series.data.base.DataBase.from_array>`).
        
        .. warning::
        
          If the data point *cannot* be serialized to a JavaScript array,
          this method will instead return the untrimmed :class:`dict <python:dict>`
          representation of the data point as a fallback.

        :param force_object: if ``True``, forces the return of the instance's
          untrimmed :class:`dict <python:dict>` representation. Defaults to ``False``.
        :type force_object: :class:`bool <python:bool>`

        :returns: The array representation of the data point.
        :rtype: :class:`list <python:list>` of values or :class:`dict <python:dict>`
        """
        if self.requires_js_object or force_object:
            return self._to_untrimmed_dict()
        
        if self.x is not None:
            x = self.x
        elif self.name is not None:
            x = self.name
        else:
            x = constants.EnforcedNull
            
        if self.open is not None:
            open_ = self.open
        else:
            open_ = constants.EnforcedNull
            
        if self.high is not None:
            high = self.high
        else:
            high = constants.EnforcedNull

        if self.low is not None:
            low = self.low
        else:
            low = constants.EnforcedNull
            
        if self.close is not None:
            close = self.close
        else:
            close = constants.EnforcedNull
            
        if self.x is None and self.name is None:
            return [open_, high, low, close]

        return [x, open_, high, low, close]


class OHLCDataCollection(HLCDataCollection):
    """A collection of :class:`OHLCData` objects.

    .. note::
    
      When serializing to JS literals, if possible, the collection is serialized to a primitive
      array to boost performance within Python *and* JavaScript. However, this may not always be
      possible if data points have non-array-compliant properties configured (e.g. adjusting their 
      style, names, identifiers, etc.). If serializing to a primitive array is not possible, the
      results are serialized as JS literal objects.

    """

    @classmethod
    def _get_data_point_class(cls):
        """The Python class to use as the underlying data point within the Collection.
        
        :rtype: class object
        """
        return OHLCData



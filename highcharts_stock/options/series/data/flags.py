from typing import Optional, List, Dict

from validator_collection import validators, checkers

from highcharts_stock.options.series.data.single_point import SingleXData
from highcharts_stock.options.series.data.collections import DataPointCollection
from highcharts_stock import constants, errors


class FlagData(SingleXData):
    """Data point that features a single ``x`` point with a ``title``."""

    def __init__(self, **kwargs):
        self._title = None
        
        self.title = kwargs.get('title', None)
        
        super().__init__(**kwargs)

    @property
    def title(self) -> Optional[str]:
        """The short text to be shown on the flag.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._title

    @title.setter
    def title(self, value):
        if not value:
            self._title = None
        else:
            self._title = validators.string(value, coerce_value = True)

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
            if checkers.is_type(item, 'FlagData'):
                as_obj = item
            elif checkers.is_dict(item):
                as_obj = cls.from_dict(item)
            elif item is None or isinstance(item, constants.EnforcedNullType):
                as_obj = cls(x = None)
            elif checkers.is_numeric(item):
                as_obj = cls(x = item)
            elif checkers.is_iterable(item):
                if len(item) == 2:
                    as_obj = cls(x = item[0], title = item[1])
                elif len(item) == 1:
                    as_obj = cls(x = item[0])
                else:
                    raise errors.HighchartsValueError(f'data expects either a 1D or 2D '
                                                      f'collection. Collection received '
                                                      f'had {len(item)} dimensions.')
            else:
                raise errors.HighchartsValueError(f'each data point supplied must either '
                                                  f'be a Flag Data Point or be '
                                                  f'coercable to one. Could not coerce: '
                                                  f'{item}')
            collection.append(as_obj)

        return collection

    @classmethod
    def from_ndarray(cls, value):
        """Creates a collection of data points from a `NumPy <https://numpy.org>`__ 
        :class:`ndarray <numpy:ndarray>` instance.
        
        :returns: A collection of data point values.
        :rtype: :class:`DataPointCollection <highcharts_core.options.series.data.collections.DataPointCollection>`
        """
        return FlagDataCollection.from_ndarray(value)
    
    @classmethod
    def _get_supported_dimensions(cls) -> List[int]:
        """Returns a list of the supported dimensions for the data point.
        
        :rtype: :class:`list <python:list>` of :class:`int <python:int>`
        """
        return [1, 2]

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
            None: ['x', 'title'],
            1: ['x'],
            2: ['x', 'title']
        }
        
        return cls._get_props_from_array_helper(prop_list, length)

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
        return self._to_untrimmed_dict()

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
            'label_rank': as_dict.get('labelrank',
                                      None) or as_dict.get('labelRank',
                                                           None),
            'name': as_dict.get('name', None),
            'selected': as_dict.get('selected', None),

            'data_labels': as_dict.get('dataLabels', None),
            'drag_drop': as_dict.get('dragDrop', None),
            'drilldown': as_dict.get('drilldown', None),

            'x': as_dict.get('x', None),
            
            'title': as_dict.get('title', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'title': self.title,
            'x': self.x,

            'dataLabels': self.data_labels,
            'dragDrop': self.drag_drop,
            'drilldown': self.drilldown,

            'accessibility': self.accessibility,
            'className': self.class_name,
            'color': self.color,
            'colorIndex': self.color_index,
            'custom': self.custom,
            'description': self.description,
            'events': self.events,
            'id': self.id,
            'labelrank': self.label_rank,
            'name': self.name,
            'selected': self.selected,

        }

        return untrimmed


class FlagDataCollection(DataPointCollection):

    @property
    def requires_js_object(self) -> bool:
        """Indicates whether or not the data point *must* be serialized to a JS literal 
        object or whether it can be serialized to a primitive array.
        
        :returns: ``True`` if the data point *must* be serialized to a JS literal object.
          ``False`` if it can be serialized to an array.
        :rtype: :class:`bool <python:bool>`
        """
        return True

    @classmethod
    def _get_data_point_class(cls):
        """The Python class to use as the underlying data point within the Collection.
        
        :rtype: class object
        """
        return FlagData

from typing import Optional

from validator_collection import validators

from highcharts_core.decorators import class_sensitive
from highcharts_core.options.annotations.shape_options import ShapeOptionsBase
from highcharts_core.options.annotations.label_options import LabelOptions

from highcharts_stock.options.annotations.stock_tools.type_options.crooked_line import CrookedLineTypeOptions


class VerticalLineConnector(ShapeOptionsBase):
    """Configuration for a vertical line connector."""

    def __init__(self, **kwargs):
        self._marker_end = None

        self.marker_end = kwargs.get('marker_end', None)

        super().__init__(**kwargs)

    @property
    def marker_end(self) -> Optional[str]:
        """ID of the marker which will be drawn at the final vertex of the path.

        .. note::

          Custom markers can be defined in the :meth:`Options.defs` property.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._marker_end

    @marker_end.setter
    def marker_end(self, value):
        self._marker_end = validators.string(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'dash_style': as_dict.get('dashStyle', None),
            'fill': as_dict.get('fill', None),
            'height': as_dict.get('height', None),
            'ry': as_dict.get('ry', None),
            'snap': as_dict.get('snap', None),
            'src': as_dict.get('src', None),
            'stroke': as_dict.get('stroke', None),
            'stroke_width': as_dict.get('strokeWidth', None),
            'x_axis': as_dict.get('xAxis', None),
            'y_axis': as_dict.get('yAxis', None),

            'marker_end': as_dict.get('markerEnd', None),
        }
        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'dashStyle': self.dash_style,
            'fill': self.fill,
            'height': self.height,
            'markerEnd': self.marker_end,
            'ry': self.ry,
            'snap': self.snap,
            'src': self.src,
            'stroke': self.stroke,
            'strokeWidth': self.stroke_width,
            'xAxis': self.x_axis,
            'yAxis': self.y_axis
        }

        return untrimmed


class VerticalLineTypeOptions(CrookedLineTypeOptions):
    """Configuration options for the :term:`vertical line` stock tool type annotation."""

    def __init__(self, **kwargs):
        self._connector = None
        self._label = None

        self.connector = kwargs.get('connector', None)
        self.label = kwargs.get('label', None)

        super().__init__(**kwargs)

    @property
    def connector(self) -> Optional[VerticalLineConnector]:
        """Connector options.

        :rtype: :class:`VerticalLineConnector <highcharts_stock.options.annotations.stock_tools.vertical_line.VerticalLineConnector>`
          or :obj:`None <python:None>`
        """
        return self._connector

    @connector.setter
    @class_sensitive(VerticalLineConnector)
    def connector(self, value):
        self._connector = value

    @property
    def label(self) -> Optional[LabelOptions]:
        """Label options.

        :rtype: `LabelOptions <highcharts_stock.options.annotations.label_options.LabelOptions>`
          or :obj:`None <python:None>`
        """
        return self._label

    @label.setter
    @class_sensitive(LabelOptions)
    def label(self, value):
        self._label = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'connector': as_dict.get('connector', None),
            'label': as_dict.get('label', None),
            'line': as_dict.get('line', None),
            'points': as_dict.get('points', None),
            'x_axis': as_dict.get('xAxis', None),
            'y_axis': as_dict.get('yAxis', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'connector': self.connector,
            'label': self.label,
            'line': self.line,
            'points': self.points,
            'xAxis': self.x_axis,
            'yAxis': self.y_axis,
        }

        return untrimmed

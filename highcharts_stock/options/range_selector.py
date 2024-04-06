from typing import Optional, List
from decimal import Decimal

from validator_collection import validators

from highcharts_stock import errors, constants
from highcharts_stock.metaclasses import HighchartsMeta
from highcharts_stock.decorators import class_sensitive
from highcharts_stock.utility_classes.data_grouping import DataGroupingOptions
from highcharts_stock.utility_classes.ast import AttributeObject
from highcharts_stock.utility_classes.javascript_functions import CallbackFunction

from highcharts_stock.utility_classes.events import RangeSelectorEvents


class RangeSelectorPosition(HighchartsMeta):
    """Position for a sub-component of the
    :class:`RangeSelector <highcharts_stock.range_selector.RangeSelector>`."""

    def __init__(self, **kwargs):
        self._align = None
        self._x = None
        self._y = None

        self.align = kwargs.get('align', None)
        self.x = kwargs.get('x', None)
        self.y = kwargs.get('y', None)

    @property
    def _dot_path(self) -> Optional[str]:
        """The dot-notation path to the options key for the current class.
        
        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return 'rangeSelector'

    @property
    def align(self) -> Optional[str]:
        """The lateral alignment of the sub-component. Defaults to ``'left``` for
        buttons and ``'right'`` for the input box.

        Accepts:

          * ``'left'``
          * ``'center'``
          * ``'right'``

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._align

    @align.setter
    def align(self, value):
        value = validators.string(value, allow_empty = True)
        if not value:
            self._align = None
        else:
            value = value.lower()
            if value not in ['left', 'center', 'right']:
                raise errors.HighchartsValueError(f'align expects either "left", '
                                                  f'"center", or "right". Received: '
                                                  f'"{value}"')
            self._align = value

    @property
    def x(self) -> Optional[int | float | Decimal]:
        """Horizontal offset applied to the sub-component. Defaults to ``0``.

        :rtype: numeric
        """
        return self._x

    @x.setter
    def x(self, value):
        if value is None:
            self._x = None
        else:
            self._x = validators.numeric(value, allow_empty = True)

    @property
    def y(self) -> Optional[int | float | Decimal]:
        """Vertical offset applied to the sub-component. Defaults to ``0``.

        :rtype: numeric
        """
        return self._y

    @y.setter
    def y(self, value):
        if value is None:
            self._y = None
        else:
            self._y = validators.numeric(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'align': as_dict.get('align', None),
            'x': as_dict.get('x', None),
            'y': as_dict.get('y', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'align': self.align,
            'x': self.x,
            'y': self.y
        }

        return untrimmed


class RangeSelectorButton(HighchartsMeta):
    """Configuration settings to apply to a button in the :term:`range selector`."""

    def __init__(self, **kwargs):
        self._count = None
        self._data_grouping = None
        self._events = None
        self._offset_max = None
        self._offset_min = None
        self._preserve_data_grouping = None
        self._text = None
        self._title = None
        self._type = None

        self.count = kwargs.get('count', None)
        self.data_grouping = kwargs.get('data_grouping', None)
        self.events = kwargs.get('events', None)
        self.offset_max = kwargs.get('offset_max', None)
        self.offset_min = kwargs.get('offset_min', None)
        self.preserve_data_grouping = kwargs.get('preserve_data_grouping', None)
        self.text = kwargs.get('text', None)
        self.title = kwargs.get('title', None)
        self.type = kwargs.get('type', None)

    @property
    def count(self) -> Optional[int | float | Decimal]:
        """The number of units of the button's
        :meth:`type <highcharts_stock.range_selector.RangeSelectorButton.type>` that the
        button should span. Defaults to ``1``.

          .. note::

            For example, if
            :meth:`type <highcharts_stock.range_selector.RangeSelectorButton.type>` is
            ``'month'`` and ``'count'`` is ``3``, the button spans three months.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._count

    @count.setter
    def count(self, value):
        self._count = validators.numeric(value, allow_empty = True)

    @property
    def data_grouping(self) -> Optional[DataGroupingOptions]:
        """A custom configuration for the grouping of data that applies to a given button.

        :rtype: :class:`DataGroupingOptions <highcharts_core.utility_classes.DataGroupingOptions>`
          or :obj:`None <python:None>`
        """
        return self._data_grouping

    @data_grouping.setter
    @class_sensitive(DataGroupingOptions)
    def data_grouping(self, value):
        self._data_grouping = value

    @property
    def events(self) -> Optional[RangeSelectorEvents]:
        """Event handlers for the :term:`range selector`'s buttons.

        :rtype: :class:`RangeSelectorEvents <highcharts_stock.utility_classes.events.RangeSelectorEvents>`
          or :obj:`None <python:None>`
        """
        return self._events

    @events.setter
    @class_sensitive(RangeSelectorEvents)
    def events(self, value):
        self._events = value

    @property
    def offset_max(self) -> Optional[int]:
        """Additional range (in milliseconds) added to the end of the calculated time
        span. Defaults to ``0``.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._offset_max

    @offset_max.setter
    def offset_max(self, value):
        self._offset_max = validators.integer(value, allow_empty = True)

    @property
    def offset_min(self) -> Optional[int]:
        """Additional range (in milliseconds) added to the start of the calculated time
        span. Defaults to ``0``.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._offset_min

    @offset_min.setter
    def offset_min(self, value):
        self._offset_min = validators.integer(value, allow_empty = True)

    @property
    def preserve_data_grouping(self) -> Optional[bool]:
        """If ``False`` and
        :meth:`.data_grouping <highcharts_stock.options.series.stock.StockSeries.data_grouping>`
        is applied on a series, zooming in/out will deselect buttons and unset the applied
        grouping. If ``True``, buttons will remain selected when the bounds of the data
        shown have changed. Defaults to ``False``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._preserve_data_grouping

    @preserve_data_grouping.setter
    def preserve_data_grouping(self, value):
        if value is None:
            self._preserve_data_grouping = None
        else:
            self._preserve_data_grouping = bool(value)

    @property
    def text(self) -> Optional[str]:
        """The text displayed on the button. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._text

    @text.setter
    def text(self, value):
        self._text = validators.string(value, allow_empty = True)

    @property
    def title(self) -> Optional[str]:
        """Explanation for the button that is shown in a tooltip on hover and used by
        assistive technology.  Defaults to :obj:`None <python:None>`.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._title

    @title.setter
    def title(self, value):
        self._title = validators.string(value, allow_empty = True)

    @property
    def type(self) -> Optional[str]:
        """The time span for the button. Accepts the following values:
        
        * ``'all'``
        * ``'millisecond'``
        * ``'second'``
        * ``'minute'``
        * ``'hour'``
        * ``'day'``
        * ``'week'``
        * ``'month'``
        * ``'year'``
        * ``'ytd'``
        
        Defaults to :obj:`None <python:None>`
        
        :rtype: :class:`str <python:str>`
        """
        return self._type
    
    @type.setter
    def type(self, value):
        if not value:
            self._type = None
        else:
            value = validators.string(value, allow_empty = False)
            value = value.lower()
            if value not in constants.RANGE_SELECTOR_BUTTON_TYPES:
                raise errors.HighchartsValueError(
                    f'type expects one of {constants.RANGE_SELECTOR_BUTTON_TYPES}. Received: "{value}"'
                )
            self._type = value

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'count': as_dict.get('count', None),
            'data_grouping': as_dict.get('dataGrouping', None),
            'events': as_dict.get('events', None),
            'offset_max': as_dict.get('offsetMax', None),
            'offset_min': as_dict.get('offsetMin', None),
            'preserve_data_grouping': as_dict.get('preserveDataGrouping', None),
            'text': as_dict.get('text', None),
            'title': as_dict.get('title', None),
            'type': as_dict.get('type', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'count': self.count,
            'dataGrouping': self.data_grouping,
            'events': self.events,
            'offsetMax': self.offset_max,
            'offsetMin': self.offset_min,
            'preserveDataGrouping': self.preserve_data_grouping,
            'text': self.text,
            'title': self.title,
            'type': self.type,
        }

        return untrimmed


class RangeSelector(HighchartsMeta):
    """The range selector is a tool for selecting ranges to display within the chart. It
    provides buttons to select preconfigured ranges in the chart, like 1 day, 1 week, 1
    month, etc. It also provides input boxes where min and max dates can be manually
    input."""

    def __init__(self, **kwargs):
        self._all_buttons_enabled = None
        self._button_position = None
        self._buttons = None
        self._button_spacing = None
        self._button_theme = None
        self._dropdown = None
        self._enabled = None
        self._floating = None
        self._height = None
        self._input_box_border_color = None
        self._input_box_height = None
        self._input_box_width = None
        self._input_date_format = None
        self._input_date_parser = None
        self._input_edit_date_format = None
        self._input_enabled = None
        self._input_position = None
        self._input_spacing = None
        self._input_style = None
        self._label_style = None
        self._selected = None
        self._vertical_align = None
        self._x = None
        self._y = None

        self.all_buttons_enabled = kwargs.get('all_buttons_enabled', None)
        self.button_position = kwargs.get('button_position', None)
        self.buttons = kwargs.get('buttons', None)
        self.button_spacing = kwargs.get('button_spacing', None)
        self.button_theme = kwargs.get('button_theme', None)
        self.dropdown = kwargs.get('dropdown', None)
        self.enabled = kwargs.get('enabled', None)
        self.floating = kwargs.get('floating', None)
        self.height = kwargs.get('height', None)
        self.input_box_border_color = kwargs.get('input_box_border_color', None)
        self.input_box_height = kwargs.get('input_box_height', None)
        self.input_box_width = kwargs.get('input_box_width', None)
        self.input_date_format = kwargs.get('input_date_format', None)
        self.input_date_parser = kwargs.get('input_date_parser', None)
        self.input_edit_date_format = kwargs.get('input_edit_date_format', None)
        self.input_enabled = kwargs.get('input_enabled', None)
        self.input_position = kwargs.get('input_position', None)
        self.input_spacing = kwargs.get('input_spacing', None)
        self.input_style = kwargs.get('input_style', None)
        self.label_style = kwargs.get('label_style', None)
        self.selected = kwargs.get('selected', None)
        self.vertical_align = kwargs.get('vertical_align', None)
        self.x = kwargs.get('x', None)
        self.y = kwargs.get('y', None)

    @property
    def all_buttons_enabled(self) -> Optional[bool]:
        """If ``True``, enables all buttons when the range selector is first rendered. By
        default buttons are only enabled if the corresponding time range exists on the
        X axis, but enabling all buttons allows for dynamically loading different time
        ranges.

        Defaults to ``False``.

        :rtype: :class:`bool <python:bool>`
        """
        return self._all_buttons_enabled

    @all_buttons_enabled.setter
    def all_buttons_enabled(self, value):
        if value is None:
            self._all_buttons_enabled = None
        else:
            self._all_buttons_enabled = bool(value)

    @property
    def button_position(self) -> Optional[RangeSelectorPosition]:
        """Positioning for the button row in the range selector.

        :rtype: :class:`RangeSelectorPosition <highcharts_stock.range_selector.RangeSelectorPosition>`
        """
        return self._button_position

    @button_position.setter
    @class_sensitive(RangeSelectorPosition)
    def button_position(self, value):
        self._button_position = value

    @property
    def buttons(self) -> Optional[List[RangeSelectorButton]]:
        """A collection of configuration settings to apply to the range selector's
        buttons.

        :rtype: :class:`list <python:list>` of :class:`RangeSelectorButton` instances, or
          :obj:`None <python:None>`
        """
        return self._buttons

    @buttons.setter
    @class_sensitive(RangeSelectorButton, force_iterable = True)
    def buttons(self, value):
        self._buttons = value

    @property
    def button_spacing(self) -> Optional[int | float | Decimal]:
        """The space between buttons in the range selector, expressed in pixels. Defaults
        to ``5``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._button_spacing

    @button_spacing.setter
    def button_spacing(self, value):
        self._button_spacing = validators.numeric(value,
                                                  allow_empty = True,
                                                  minimum = 0)

    @property
    def button_theme(self) -> Optional[AttributeObject]:
        """A collection of attributes for the buttons. Defaults
        to :obj:`None <python:None>`.

        .. note::

          The object takes SVG attributes like ``fill``, ``stroke``, ``stroke-width``, as
          well as ``style``, a collection of CSS properties for the text.

          The object can also be extended with states, so you can set presentational
          options for ``hover``, ``select``, or ``disabled`` button states.

        :rtype: :class:`AttributeObject` or :obj:`None <python:None>`
        """
        return self._button_theme

    @button_theme.setter
    @class_sensitive(AttributeObject)
    def button_theme(self, value):
        self._button_theme = value

    @property
    def dropdown(self) -> Optional[str]:
        """Whether to collapse the range selector's buttons into a dropdown menu when
        there is not enough room to display the buttons in a single row or to render the
        buttons on multiple rows. Defaults to ``'responsive'``.

        Accepts the following values:

          * ``'always'`` - always collapses the buttons to a dropdown menu
          * ``'responsive'`` - only collapses the buttons to a dropdown menu when they
            will not fit on a single row
          * ``'never'`` - never collapse the buttons, wrap the line if there is not enough
            room to render them on a single line

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._dropdown

    @dropdown.setter
    def dropdown(self, value):
        if not value:
            self._dropdown = None
        else:
            value = validators.string(value, allow_empty = True)
            value = value.lower()
            if value not in ['always', 'responsive', 'never']:
                raise errors.HighchartsValueError(f'dropdown expects either "always", '
                                                  f'"responsive", or "never". Received: '
                                                  f'"{value}"')
            self._dropdown = value

    @property
    def enabled(self) -> Optional[bool]:
        """Whether the range selector is enabled and visible (``True``) or not
        (``False``). Defaults to ``True``.

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
    def floating(self) -> Optional[bool]:
        """If ``True``, the plot area does not reserve space for the range selector and it
        can be positioned anywehre relative to the chart. Defaults to ``False``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._floating

    @floating.setter
    def floating(self, value):
        if value is None:
            self._floating = None
        else:
            self._floating = bool(value)

    @property
    def input_box_border_color(self) -> Optional[str]:
        """The color to apply to the border of the date input boxes. Defaults to
        :obj:`None <python:None>`.

        :rtype: :class:`str <python:str>`
        """
        return self._input_box_border_color

    @input_box_border_color.setter
    def input_box_border_color(self, value):
        self._input_box_border_color = validators.string(value, allow_empty = True)

    @property
    def input_box_height(self) -> Optional[int | float | Decimal]:
        """The height of the date input boxes, expressed in pixels.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._input_box_height

    @input_box_height.setter
    def input_box_height(self, value):
        self._input_box_height = validators.numeric(value, allow_empty = True)

    @property
    def input_date_format(self) -> Optional[str]:
        """The (JavaScript) date format in which dates in the input boxes are displayed
        when the input boxes are *not* selected for editing. Defaults to
        ``'%b %e, %Y'``.

        .. note::

          Highcharts Stock uses this to determine which type of input to show:
          ``datetime-local``, ``date``, or ``time`` and falling back to text when the
          browser either does not support the input type or the format string contains
          milliseconds.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._input_date_format

    @input_date_format.setter
    def input_date_format(self, value):
        self._input_date_format = validators.string(value, allow_empty = True)

    @property
    def input_date_parser(self) -> Optional[CallbackFunction]:
        """A custom (JavaScript) callback function to parse values entered in the input
        boxes and return a valid JavaScript time as milliseconds since 1970. The function
        should receive two arguments: The first argument is a value to parse, and the
        second is a boolean indicating use of the UTC time. Defaults to
        :obj:`None <python:None>`.

        .. warning::

          This function will only get called for inputs of type ``text``. The input type
          is dynamically determined based on the granularity of the
          :meth:`.input_date_format <highcharts_stock.range_selector.RangeSelector.input_date_format>`
          and applicable browser support.

        :rtype: :class:`CallbackFunction <highcharts_stock.utility_classes.javascript_functions.CallbackFunction>`
          or :obj:`None <python:None>`
        """
        return self._input_date_parser

    @input_date_parser.setter
    @class_sensitive(CallbackFunction)
    def input_date_parser(self, value):
        self._input_date_parser = value

    @property
    def input_edit_date_format(self) -> Optional[str]:
        """The (JavaScript) date format to apply to the contents of the input boxes
        when they are selected for editing. Defaults to ``'%Y-%m-%d'``.

          .. note::

            This *must* be a format that is recognized by JavaScript ``Date.parse()``.

          .. warning::

            This will only be used for inputs of type ``text``. The input type is
            dynamically determined based on the granularity of the
            :meth:`.input_date_format <highcharts_stock.range_selector.RangeSelector.input_date_format>`
            setting and applicable browser support.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._input_edit_date_format

    @input_edit_date_format.setter
    def input_edit_date_format(self, value):
        self._input_edit_date_format = validators.string(value, allow_empty = True)


    @property
    def input_enabled(self) -> Optional[bool]:
        """If ``True``, enables the input date boxes in the range selector. Defaults to
        ``True``.

        :rtype: :class:`bool <python:bool>` or :obj:`None <python:None>`
        """
        return self._input_enabled

    @input_enabled.setter
    def input_enabled(self, value):
        if value is None:
            self._input_enabled = None
        else:
            self._input_enabled = bool(value)

    @property
    def input_position(self) -> Optional[RangeSelectorPosition]:
        """Positioning for the date input boxes.

        :rtype: :class:`RangeSelectorPosition` or :obj:`None <python:None>`
        """
        return self._input_position

    @input_position.setter
    @class_sensitive(RangeSelectorPosition)
    def input_position(self, value):
        self._input_position = value

    @property
    def input_spacing(self) -> Optional[int | float | Decimal]:
        """The space between the labels and the date input boxes in the range selector,
        expressed in pixels. Defaults to ``5``.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._input_spacing

    @input_spacing.setter
    def input_spacing(self, value):
        self._input_spacing = validators.numeric(value, allow_empty = True)

    @property
    def input_style(self) -> Optional[str]:
        """CSS for the HTML inputs in the range selector. Defaults to
        :obj:`None <python:None>`.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._input_style

    @input_style.setter
    def input_style(self, value):
        self._input_style = validators.string(value, allow_empty = True)

    @property
    def label_style(self) -> Optional[str]:
        """CSS for the HTML labels in the range selector - specifically the "Zoom",
        "From", and "To" texts. Defaults to :obj:`None <python:None>`.

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._label_style

    @label_style.setter
    def label_style(self, value):
        self._label_style = validators.string(value, allow_empty = True)

    @property
    def selected(self) -> Optional[int]:
        """The index of the button which should appear as pre-selected (before user
        interaction/selection). Defaults to :obj:`None <python:None>`, which leaves all
        as unselected.

        :rtype: :class:`int <python:int>` or :obj:`None <python:None>`
        """
        return self._selected

    @selected.setter
    def selected(self, value):
        self._selected = validators.integer(value, allow_empty = True)

    @property
    def vertical_align(self) -> Optional[str]:
        """The vertical alignment of the range selector box. Defaults to ``'top'``.

        Accepts:

          * ``'top'``
          * ``'middle'``
          * ``'bottom'``

        :rtype: :class:`str <python:str>` or :obj:`None <python:None>`
        """
        return self._vertical_align

    @vertical_align.setter
    def vertical_align(self, value):
        if not value:
            self._vertical_align = None
        else:
            value = validators.string(value)
            value = value.lower()
            if value not in ['top', 'middle', 'bottom']:
                raise errors.HighchartsValueError(f'vertical_align expects either "top", '
                                                  f'"middle", or "bottom". Received: '
                                                  f'"{value}".')
            self._vertical_align = value

    @property
    def x(self) -> Optional[int | float | Decimal]:
        """The x-offset of the range selector box relative to its horizontal alignment
        within (JavaScript) ``chart.spacingLeft`` and ``chart.spacingRight``. Defaults to
        ``0``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._x

    @x.setter
    def x(self, value):
        self._x = validators.numeric(value, allow_empty = True)

    @property
    def y(self) -> Optional[int | float | Decimal]:
        """The y-offset of the range selector boy relative to its horizontal alignment
        within (JavaScript) ``chart.spacingLeft`` and ``chart.spacingRight``. Defaults to
        ``0``.

        :rtype: numeric or :obj:`None <python:None>`
        """
        return self._y

    @y.setter
    def y(self, value):
        self._y = validators.numeric(value, allow_empty = True)

    @classmethod
    def _get_kwargs_from_dict(cls, as_dict):
        kwargs = {
            'all_buttons_enabled': as_dict.get('allButtonsEnabled', None),
            'button_position': as_dict.get('buttonPosition', None),
            'buttons': as_dict.get('buttons', None),
            'button_spacing': as_dict.get('buttonSpacing', None),
            'button_theme': as_dict.get('buttonTheme', None),
            'dropdown': as_dict.get('dropdown', None),
            'enabled': as_dict.get('enabled', None),
            'floating': as_dict.get('floating', None),
            'input_box_border_color': as_dict.get('inputBoxBorderColor', None),
            'input_box_height': as_dict.get('inputBoxHeight', None),
            'input_box_width': as_dict.get('inputBoxWidth', None),
            'input_date_format': as_dict.get('inputDateFormat', None),
            'input_date_parser': as_dict.get('inputDateParser', None),
            'input_edit_date_format': as_dict.get('inputEditDateFormat', None),
            'input_enabled': as_dict.get('inputEnabled', None),
            'input_position': as_dict.get('inputPosition', None),
            'input_spacing': as_dict.get('inputSpacing', None),
            'input_style': as_dict.get('inputStyle', None),
            'label_style': as_dict.get('labelStyle', None),
            'selected': as_dict.get('selected', None),
            'vertical_align': as_dict.get('verticalAlign', None),
            'x': as_dict.get('x', None),
            'y': as_dict.get('y', None),
        }

        return kwargs

    def _to_untrimmed_dict(self, in_cls = None) -> dict:
        untrimmed = {
            'allButtonsEnabled': self.all_buttons_enabled,
            'buttonPosition': self.button_position,
            'buttons': self.buttons,
            'buttonSpacing': self.button_spacing,
            'buttonTheme': self.button_theme,
            'dropdown': self.dropdown,
            'enabled': self.enabled,
            'floating': self.floating,
            'height': self.height,
            'inputBoxBorderColor': self.input_box_border_color,
            'inputBoxHeight': self.input_box_height,
            'inputBoxWidth': self.input_box_width,
            'inputDateFormat': self.input_date_format,
            'inputDateParser': self.input_date_parser,
            'inputEditDateFormat': self.input_edit_date_format,
            'inputEnabled': self.input_enabled,
            'inputPosition': self.input_position,
            'inputSpacing': self.input_spacing,
            'inputStyle': self.input_style,
            'labelStyle': self.label_style,
            'selected': self.selected,
            'verticalAlign': self.vertical_align,
            'x': self.x,
            'y': self.y,
        }

        return untrimmed

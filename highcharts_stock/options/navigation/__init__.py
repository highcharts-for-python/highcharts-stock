from typing import Optional

from highcharts_core.options.navigation import Navigation as NavigationBase

from highcharts_stock.decorators import class_sensitive
from highcharts_stock.options.annotations import NavigationAnnotationOptions


class Navigation(NavigationBase):

    @property
    def annotation_options(self) -> Optional[NavigationAnnotationOptions]:
        """Additional options to be applied to all annotations.

        :rtype: :class:`NavigationAnnotationOptions <highcharts_stock.options.annotations.NavigationAnnotationOptions>`
          or :obj:`None <python:None>`
        """
        return self._annotation_options

    @annotation_options.setter
    @class_sensitive(NavigationAnnotationOptions)
    def annotation_options(self, value):
        self._annotation_options = value

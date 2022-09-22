#################################
Library Internals
#################################

.. contents:: Section Contents
  :local:
  :depth: 3
  :backlinks: entry

--------------

.. module:: highcharts_stock.metaclasses

******************************************************************************
module: :mod:`.metaclasses <highcharts_stock.metaclasses>`
******************************************************************************

The :mod:`.metaclasses <highcharts_stock.metaclasses>` module contains - as one might
expect - :term:`metaclasses <metaclass>` that are used to ensure a consistent interface
throughout the **Highcharts Stock for Python** library.


class: :class:`HighchartsMeta <highcharts_stock.metaclasses.HighchartsMeta>`
===================================================================================

.. autoclass:: HighchartsMeta
  :members:
  :inherited-members:
  :private-members:

  .. collapse:: Class Inheritance

    .. inheritance-diagram:: HighchartsMeta
      :parts: -1

  |

class: :class:`JavaScriptDict <highcharts_stock.metaclasses.JavaScriptDict>`
====================================================================================

.. autoclass:: JavaScriptDict
  :members:
  :inherited-members:
  :private-members:

  .. collapse:: Class Inheritance

    .. inheritance-diagram:: JavaScriptDict
      :parts: -1

  |

----------------------

.. module:: highcharts_stock.decorators

******************************************************************************
module: :mod:`.decorators <highcharts_stock.decorators>`
******************************************************************************

The :mod:`.decorators <highcharts_stock.decorators>` module contains decorators and
decorator-assisting functions used throughout the **Highcharts Stock for Python** library.

decorator: :deco:`@class_sensitive <highcharts_stock.decorators.class_sensitive>`
=======================================================================================

.. autodecorator:: class_sensitive

function: :func:`validate_types() <highcharts_stock.decorators.validate_types>`
===================================================================================

.. autofunction:: validate_types

----------------------------------

.. module:: highcharts_stock.js_literal_functions

******************************************************************************************
module:: :mod:`.js_literal_functions <highcharts_stock.js_literal_functions>`
******************************************************************************************

The :mod:`.js_literal_functions <highcharts_stock.js_literal_functions>` module contains
functions that are used to parse, process, de-serialize, and serialize JavaScript literal
notation.

function: :func:`serialize_to_js_literal() <highcharts_stock.js_literal_functions.serialize_to_js_literal>`
===================================================================================================================================

.. autofunction:: serialize_to_js_literal

function: :func:`attempt_variable_declaration() <highcharts_stock.js_literal_functions.attempt_variable_declaration>`
===================================================================================================================================

.. autofunction:: attempt_variable_declaration

function: :func:`is_js_function_or_class() <highcharts_stock.js_literal_functions.is_js_function_or_class>`
===================================================================================================================================

.. autofunction:: is_js_function_or_class

function: :func:`get_js_literal() <highcharts_stock.js_literal_functions.get_js_literal>`
===================================================================================================================================

.. autofunction:: get_js_literal

function: :func:`assemble_js_literal() <highcharts_stock.js_literal_functions.assemble_js_literal>`
===================================================================================================================================

.. autofunction:: assemble_js_literal

function: :func:`convert_js_literal_to_python() <highcharts_stock.js_literal_functions.convert_js_literal_to_python>`
===================================================================================================================================

.. autofunction:: convert_js_literal_to_python

function: :func:`convert_js_property_to_python() <highcharts_stock.js_literal_functions.convert_js_property_to_python>`
===================================================================================================================================

.. autofunction:: convert_js_property_to_python

function: :func:`convert_js_to_python() <highcharts_stock.js_literal_functions.convert_js_to_python>`
===================================================================================================================================

.. autofunction:: convert_js_to_python

function: :func:`get_key_value_pairs() <highcharts_stock.js_literal_functions.get_key_value_pairs>`
===================================================================================================================================

.. autofunction:: get_key_value_pairs

-------------------------

.. module:: highcharts_stock.utility_functions

********************************************************************
:mod:`.utility_functions <highcharts_stock.utility_functions>`
********************************************************************

The :mod:`.utility_functions <highcharts_stock.utility_functions>` module contains a
small number of functions which serve as utilities across the
**Highcharts Stock for Python** library. Think of it as a function "catch all" module.

function:: :func:`mro_to_dict() <highcharts_stock.utility_functions.mro_to_dict>`
=====================================================================================================

.. autofunction:: mro_to_dict

function:: :func:`get_remaining_mro() <highcharts_stock.utility_functions.get_remaining_mro>`
=====================================================================================================

.. autofunction:: get_remaining_mro

function:: :func:`mro__to_untrimmed_dict() <highcharts_stock.utility_functions.mro__to_untrimmed_dict>`
==============================================================================================================

.. autofunction:: mro__to_untrimmed_dict

function:: :func:`validate_color() <highcharts_stock.utility_functions.validate_color>`
=====================================================================================================

.. autofunction:: validate_color

function:: :func:`to_camelCase() <highcharts_stock.utility_functions.to_camelCase>`
=====================================================================================================

.. autofunction:: to_camelCase

function:: :func:`parse_csv() <highcharts_stock.utility_functions.parse_csv>`
=====================================================================================================

.. autofunction:: parse_csv

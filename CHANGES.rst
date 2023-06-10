Release 1.2.1
=========================================

* **BUGFIX:** Fixed incorrect ``datetime`` serialization to SECONDS from Unix epoch. Now serializing to JS-compatible MILLISECONDS from Unix epoch.

------------------

Release 1.2.0
=========================================

* **ENHANCEMENT:** Align the API to **Highcharts (JS) v.11.1** (#22). In particular, this includes:

  * Changes inherited from **Highcharts Core for Python v.1.2.0**. See `here <https://core-docs.highchartspython.com/en/latest/history.html#release-1-2-0>`__.

* **ENHANCEMENT:** Added support for the inclusion of scripts based on features used in the chart (#4).
* **ENHANCEMENT:** Added ``dict`` support to ``.style`` property on labels and titles.
* **DOCS:** Various documentation updates and fixes.
* **DEPENDENCY:** Bumped ``requests`` version for security patch.

---------------------------

Release 1.1.1
=========================================

* **FIXED:** Problem when producing a JS literal, with the JS code inserting an unnecessary ``new``.
* **ENHANCEMENT:** Added more elegant error handling when something goes wrong displaying a chart in Jupyter.

---------------------------

Release 1.1.0
=========================================

* Align the API to **Highcharts (JS) v.11**. In particular, this includes:

  * Changes inherited from **Highcharts Core for Python v.1.1.0**. See `here <https://core-docs.highchartspython.com/en/latest/history.html#release-1-1-0>`__.
  * Added ``options.scrollbar.buttons_enabled`` property.

* **FIXED:** Broken heatmap and tilemap documentation links.
* **FIXED:** Fixed missing ``TreegraphOptions`` / ``TreegraphSeries`` series type.

-------------------------------

Release 1.0.1
=========================================

* **DOCUMENTATION:** Added documentation of "hard" dependencies in the README.

---------------------------

Release 1.0.0
=========================================

* **First official release!**

---------------

Release 1.0.0-rc8
=========================================

* Added demos to documentation.

---------------

Release 1.0.0-rc7
=========================================

* Added support for additional ``.from_array()`` patterns to HLC-and-related visualizations.
* Fixed Jupyter display functionality to align signature to new release of Highcharts Core for Python.

---------------

Release 1.0.0-rc6
=========================================

* Further tweaks to documentation CSS for better accessibility.

---------------

Release 1.0.0-rc5
=========================================

* Added CSS overrides to documentation for better accessibility.
* Added jQuery to documentation to address issue in Sphinx 6.0 and Sphinx RTD Theme.

-----------------------

Release 1.0.0-rc4
=========================================

* Fixed JSON deserialization in ``.from_array()``.
* Fixed dependency on ``python-dotenv``.
* Overhaul of JavaScript script inclusion in Jupyter Labs context.
* Fixed error in Stock Tools rendering.
* Fixed ``Chart.from_options()`` typo.

------------------------

Release 1.0.0-rc3
=========================================

* Revised documentation.

------------------------

Release 1.0.0-rc2
=========================================

* Revised documentation.

------------------------

Release 1.0.0-rc1
=========================================

* First public release: **Release Candidate 1**


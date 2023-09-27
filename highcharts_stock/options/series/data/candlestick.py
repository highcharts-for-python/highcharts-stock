from highcharts_stock.options.series.data.hlc import OHLCData, OHLCDataCollection


class CandlestickData(OHLCData):
    """Data point that can be visualized in a
    :class:`CandlestickSeries <highcharts_core.options.series.candlestick.CandlestickSeries>`,
    featuring an x value, a high value, an open value, a low value, and a close value.
    """

    @classmethod
    def from_ndarray(cls, value):
        """Creates a collection of data points from a `NumPy <https://numpy.org>`__ 
        :class:`ndarray <numpy:ndarray>` instance.
        
        :returns: A collection of data point values.
        :rtype: :class:`DataPointCollection <highcharts_core.options.series.data.collections.DataPointCollection>`
        """
        return CandlestickDataCollection.from_ndarray(value)


class CandlestickDataCollection(OHLCDataCollection):
    """A collection of :class:`CandlestickData` objects.

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
        return CandlestickData

# -*- coding: utf-8 -*-

from __future__ import absolute_import, division

from .validation import assert_dtype
from math import radians, cos, sin, asin, sqrt

__all__ = [
    'haversine'
]

_VALID_UNITS = {
    'km': 6372.8,
    'mi': 3959.9
}


def haversine(lon1, lat1, lon2, lat2, unit='km'):
    """Compute the great-arc distance.

    Determine the circle distance between two points on a
    sphere given their longitude and latitudes

    Parameters
    ----------
    lon1 : float
        decimal degrees

    lat1 : float
        decimal degrees

    lon2 : float
        decimal degrees

    lat2 : float
        decimal degrees

    unit : str
        Either 'km' for kilometers or 'mi' for miles

    Examples
    --------
    >>> haversine(-122.20833, 49.3, -122.22500, 49.26667, 'km')
    3.8994885745989176

    >>> haversine(-122.20833, 49.3, -122.22500, 49.26667, 'mi')
    2.423045569695307

    Returns
    -------
    dist : float
        The Haversine distance

    References
    ----------
    .. [1] TODO: Gigi add a reference link
    """
    # assert they're all floats
    assert_dtype((float, int), lon1, lat1, lon2, lat2)

    # only let km and mi pass regardless of case
    try:
        radius = _VALID_UNITS[unit]
    except KeyError:
        raise ValueError("Expected one of %s for 'unit', but got %s"
                         % (str(list(_VALID_UNITS.keys())), unit))

    # convert decimal degrees to radians
    float_radians = lambda v: float(radians(v))
    lon1, lat1, lon2, lat2 = map(float_radians, [lon1, lat1, lon2, lat2])

    # formula
    dist_lon = lon2 - lon1
    dist_lat = lat2 - lat1
    a = sin(dist_lat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dist_lon / 2) ** 2
    c = 2 * asin(sqrt(a))

    return c * radius

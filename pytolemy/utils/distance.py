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
    r"""Compute the great-arc distance.

    The haversine formula determines the great-circle distance between two
    points on a sphere given their longitude and latitudes coordinates in
    decimal degrees based on the average radius of the Earth.
    The great-circle is the largest circle you can draw from a given sphere.
    Please note this function accepts degrees for lat/lon, not radians.

    :math:`\operatorname {hav} (\theta )=\sin ^{2}\left({\frac
    {\theta }{2}}\right)={\frac {1-\cos(\theta )}{2}}`

    :math:`{\displaystyle d=2r\arcsin \left({\sqrt {\operatorname {hav}
    (\varphi _{2}-\varphi _{1})
    +\cos(\varphi _{1})\cos(\varphi _{2})\operatorname {hav}
     (\lambda _{2}-\lambda _{1})}}\right)}`

    Parameters
    ----------
    lon1 : float
        The longitude in decimal degrees of the first point.

    lat1 : float
        The latitude in decimal degrees of the first point.

    lon2 : float
        The longitude in decimal degrees of the second point.

    lat2 : float
        The latitude in decimal degrees of the second point.

    unit : str
        Either 'km' for kilometers or 'mi' for miles

    Examples
    --------
    >>> from pytolemy.utils.distance import haversine as hvsn
    >>> hvsn(-122.20833, 49.3, -122.22500, 49.26667, 'km')  # doctest: +SKIP
    3.8994885745989176

    >>> hvsn(-122.20833, 49.3, -122.22500, 49.26667, 'mi')  # doctest: +SKIP
    2.423045569695307

    Notes
    --------
    * This function assumes a spherical earth and ignores the ellipsoidal effect.
    * The mean radius is assumed to be 6372.8 km or 3959.9 mi.

    Returns
    -------
    dist : float
        The Haversine distance

    References
    ----------
    .. [1] https://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points
    .. [2] https://www.vcalc.com/wiki/vCalc/Haversine+-+Distance
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

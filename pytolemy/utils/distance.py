# -*- coding: utf-8 -*-

from __future__ import absolute_import
from math import radians, cos, sin, asin, sqrt

__all__ = [
    'haversine'
]


def haversine(lon1, lat1, lon2, lat2, unit = 'km'):
    """Determine the circle distance between two points on a sphere given their longitude and latitudes

    :param lon1: decimal degrees
    :param lat1: decimal degrees
    :param lon2: decimal degrees
    :param lat2: decimal degrees
    :param unit: string. Either km for kilometers or mi for miles
    :return: float
    """

    # don't let non string units pass
    if not isinstance(unit, str):
        return False

    if not isinstance(lon1, float):
        return False

    if not isinstance(lat1, float):
        return False

    if not isinstance(lon2, float):
        return False

    if not isinstance(lat2, float):
        return False

    # only let km and mi pass regardless of case
    if unit.lower().strip() == 'km':
        radius = 6372.8
    elif unit.lower().strip() == 'mi':
        radius = 3959.9
    else:
        return False

    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # formula
    dist_lon = lon2 - lon1
    dist_lat = lat2 - lat1
    a = sin(dist_lat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dist_lon / 2) ** 2
    c = 2 * asin(sqrt(a))

    return c * radius



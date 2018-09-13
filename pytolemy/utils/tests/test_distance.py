# -*- coding: utf-8 -*-

from __future__ import absolute_import

from pytolemy.utils.distance import haversine
from numpy.testing.utils import assert_allclose, assert_equal


def test_haversine():

    # check string input (lon lat lon lat)
    assert haversine(49.3, -122.20833, 49.26667, -122.22500, 'mi')
    assert haversine(49.3, -122.20833, 49.26667, -122.22500, 'Km')
    assert haversine(49.3, -122.20833, 49.26667, -122.22500, ' MI  ')

    # prove that strings that are not km or mi will not work
    assert not haversine(49.3, -122.20833, 49.26667, -122.22500, 'cd')
    assert not haversine(49.3, -122.20833, 49.26667, -122.22500, ' ')

    # prove that things that are not strings will not work
    assert not haversine(49.3, -122.20833, 49.26667, -122.22500, 42)

    # prove that non floats for lon/lat will not work
    assert not haversine('49.3', '-122.20833', '49.26667', '-122.22500', 42)

    # Close enough to solution 3.89839267 km
    assert_allclose(haversine(-122.20833, 49.3, -122.22500, 49.26667, 'km'), 3.8984,  rtol=1e-3, atol=0) # 3.899489

    # Close enough to solution 2.4223489 mi
    assert_allclose(haversine(-122.20833, 49.3, -122.22500, 49.26667, 'mi'), 2.4223,  rtol=1e-3, atol=0) # 3.899489


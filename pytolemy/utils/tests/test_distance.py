# -*- coding: utf-8 -*-

from __future__ import absolute_import

from pytolemy.utils.distance import haversine

from numpy.testing.utils import assert_allclose
import pytest


def test_haversine_bad_units():
    for bad_unit in ('Km', "MI", "bad key", 42):
        # To test that we expect something with fail:
        with pytest.raises(ValueError):  # the one we expect it will raise
            haversine(49.3, -122.20833, 49.26667, -122.22500, bad_unit)


def test_haversine_bad_inputs():
    with pytest.raises(AssertionError):
        haversine('49.3', '-122.20833', '49.26667', '-122.22500', 'mi')


def test_haversine():
    # Close enough to solution 3.89839267 km
    assert_allclose(haversine(-122.20833, 49.3, -122.22500, 49.26667, 'km'),
                    3.8984,  rtol=1e-3, atol=0)  # 3.899489

    # Close enough to solution 2.4223489 mi
    assert_allclose(haversine(-122.20833, 49.3, -122.22500, 49.26667, 'mi'),
                    2.4223,  rtol=1e-3, atol=0)  # 2.4223...

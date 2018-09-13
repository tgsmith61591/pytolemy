# -*- coding: utf-8 -*-

from __future__ import absolute_import

from pytolemy.utils.validation import is_iterable, assert_dtype

import numpy as np
import pytest


def test_assert_dtype():
    assert_dtype(float, 1.5)
    assert_dtype((float, int), 1.5)
    assert_dtype((float, int), 1)

    with pytest.raises(AssertionError):
        assert_dtype(str, 1.5)


def test_is_iterable():
    assert is_iterable([1, 2, 3])
    assert is_iterable((1, 2, 3))
    assert is_iterable({1, 2, 3})
    assert is_iterable({'a': 2, 'b': 4})

    # prove it works for non-native structs
    assert is_iterable(np.array([1, 2, 3]))

    # prove that strings are NOT
    assert not is_iterable('str')

    # prove that other things, like ints, are NOT
    assert not is_iterable(123)



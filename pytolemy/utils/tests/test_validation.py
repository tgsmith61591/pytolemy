# -*- coding: utf-8 -*-

from __future__ import absolute_import

from pytolemy.utils.validation import is_iterable
import numpy as np


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

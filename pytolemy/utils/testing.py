# -*- coding: utf-8 -*-
#
# Testing utilities

from __future__ import absolute_import

from functools import wraps
from ..datasets import _cache_test_data

__all__ = [
    'with_cached_test_images'
]


def with_cached_test_images(func):
    """Require a test function to use cached images.

    Parameters
    ----------
    func : callable
        The test function to decorate. Should require cached images.

    Examples
    --------
    >>> @with_cached_test_images
    >>> def some_testing_function():
    ...     assert True
    """
    @wraps(func)
    def test_wrapper(*args, **kwargs):
        _cache_test_data()
        return func(*args, **kwargs)
    return test_wrapper


# Avoid pb w nose
with_cached_test_images.__test__ = False

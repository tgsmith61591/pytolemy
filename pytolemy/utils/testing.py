# -*- coding: utf-8 -*-
#
# Testing utilities

from __future__ import absolute_import

from functools import wraps
import os

from ..datasets import _cache_test_data, get_data_home

__all__ = [
    'get_test_image_dir',
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
    >>> @with_cached_test_images  # doctest: +SKIP
    >>> def some_testing_function():
    ...     assert True
    """
    @wraps(func)
    def test_wrapper(*args, **kwargs):
        _cache_test_data()
        return func(*args, **kwargs)
    return test_wrapper


def get_test_image_dir():
    """Get the directory of the cached test images.

    Notes
    -----
    This can be iterated with ``os.walk``.

    Returns
    -------
    data_dir : str
        The location of the directory of test images.
    """
    return os.path.join(get_data_home(), '19TCG240875')


# Avoid pb w nose
get_test_image_dir.__test__ = False
with_cached_test_images.__test__ = False

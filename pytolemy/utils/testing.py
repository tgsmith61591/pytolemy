# -*- coding: utf-8 -*-
#
# Testing utilities

from __future__ import absolute_import

from functools import wraps
import os

from ..datasets import _cache_test_data, get_data_home

__all__ = [
    'get_test_image_dir',
    'get_test_image_files',
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


def get_test_image_files():
    """Get the absolute paths of the cached test images.

    Examples
    --------
    >>> get_test_image_files()  # doctest: +SKIP
    ['/Users/<user>/pytolemy_data/19TCG240875/19TCG240875.xml',
     '/Users/<user>/pytolemy_data/19TCG240875/19TCG240875.j2w',
     '/Users/<user>/pytolemy_data/19TCG240875/19TCG240875.jp2',
     '/Users/<user>/pytolemy_data/19TCG240875/19TCG240875.aux']

    Notes
    -----
    This will fail with a ValueError if the image cache has not yet been
    created. Make sure to decorate your unit tests that depend on the presence
    of the images with :func:`with_cached_test_images`.

    Returns
    -------
    data_dir : str
        The location of the directory of test images.
    """
    gen = list(os.walk(get_test_image_dir()))
    if not gen:
        raise ValueError('Test image cache does not appear to have '
                         'been created yet. Make sure to decorate your tests '
                         'that depend on the images with '
                         '`pytolemy.utils.testing.with_cached_test_images`')

    folder, _, files = gen[0]
    return list(map(lambda f: os.path.join(folder, f), files))


def get_test_image_dir():
    """Get the directory of the cached test images.

    Notes
    -----
    * This can be iterated with ``os.walk``, or the contents can be retrieved
      directly with :func:`get_test_image_files`
    * This directory is not guaranteed to exist! To ensure that it does,
      use the :func:`with_cached_test_images` decorator with your tests.

    Examples
    --------
    >>> get_test_image_dir()
    '/Users/<user>/pytolemy_data/19TCG240875'

    Returns
    -------
    data_dir : str
        The location of the directory of test images.
    """
    return os.path.join(get_data_home(), '19TCG240845')


# Avoid pb w nose
get_test_image_dir.__test__ = False
with_cached_test_images.__test__ = False

# -*- coding: utf-8 -*-

from __future__ import absolute_import

__all__ = [
    'assert_dtype',
    'is_iterable'
]


def assert_dtype(dtype, *args):
    r"""Assert that a variable number of args are of a given dtype.

    Parameters
    ----------
    dtype : type, tuple
        The type we expect the args to be, or a tuple of types
        we expect the args to be in.

    *args : var-args
        The arguments to test
    """
    for arg in args:
        assert isinstance(arg, dtype), \
            "Expected type=%s, but got type=%s (%r)" \
            % (type(dtype), type(arg), arg)


def is_iterable(x):
    """Determine whether x is iterable.

    Parameters
    ----------
    x : object
        A python object
    """
    # Python 3 added '__iter__' to strings. Since we only
    # support py3.5+, we don't need to account for unicode, etc.
    if isinstance(x, str):
        return False
    return hasattr(x, '__iter__')

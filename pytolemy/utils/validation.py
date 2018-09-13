# -*- coding: utf-8 -*-

from __future__ import absolute_import

__all__ = [
    'is_iterable'
]


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

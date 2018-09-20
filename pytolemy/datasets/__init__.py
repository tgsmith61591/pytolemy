# -*- coding: utf-8 -*-

from __future__ import absolute_import

import os
from os.path import dirname, join, abspath, exists, expanduser

import zipfile
from shutil import copy

__all__ = [
    '_cache_test_data',
    '_get_cache_location'
]


def _safe_mkdirs(loc):
    """Safely create a directory, even if it exists.

    Using ``os.makedirs`` can raise an OSError if a directory already exists.
    This safely attempts to create a directory, and passes if it already
    exists. It also safely avoids the race condition of checking for the
    directory's existence prior to creating it.

    Parameters
    ----------
    loc : str or unicode
        The absolute path to the directory to create.
    """
    try:
        os.makedirs(loc)
        return loc
    # since this is a race condition, just try to make it
    except OSError as e:
        # Anything OTHER than the dir already exists error
        if e.errno != 17:
            raise


def _get_cache_location():
    """Get the location of the Pytolemy cache.

    Returns
    -------
    path_location : str
        Return the location of the Pytolemy directory.
    """
    return os.environ.get('PYTOLEMY_DATA_DIR',
                          expanduser(join('~', 'pytolemy_data')))


def _load_and_cache_dataset(zip_key):
    """Unzip and cache a dataset from ``datasets/data``.

    Parameters
    ----------
    key : str
        The name of a dataset to unzip, and put in the cache.
    """
    # Two cases:
    # 1. the data has already been loaded/cached
    # 2. the data has NOT been unzipped
    assert zip_key.endswith('.zip'), "zip_key must be a .zip file"

    # First thing: Get/Create the cache directory
    cache = _safe_mkdirs(_get_cache_location())  # e.g., /Users/<you>/..._data

    # Check if it's already there
    output_location = join(cache, zip_key[:-4])
    if not exists(output_location):
        # Unzip it IN the cache, and then nuke the zip file
        with zipfile.ZipFile(zip_key, 'r') as zf:
            zf.extractall(output_location)  # datasets/XXX.zip -> cache/XXX/


def _get_module_path():
    """Get the location of the datasets directory"""
    return abspath(dirname(__file__))


def _cache_test_data():
    """Cache and unzip the test data (19TC....zip)"""
    _load_and_cache_dataset(
        join(_get_module_path(), 'data', '19TCG240875.zip'))

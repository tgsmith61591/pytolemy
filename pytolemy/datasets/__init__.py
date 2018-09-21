# -*- coding: utf-8 -*-

from __future__ import absolute_import

import os
from os.path import dirname, join, abspath, exists, expanduser

import zipfile
import shutil

__all__ = [
    '_cache_test_data',
    'get_data_home',
    'remove_cache'
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
    # since this is a race condition, just try to make it
    except OSError as e:
        # Anything OTHER than the dir already exists error
        if e.errno != 17:
            raise
    return loc


def remove_cache():
    """Remove the cached contents of the pytolemy data directory.

    Removes the pytolemy data directory (default=``~/pytolemy_data``) from
    disk.

    Notes
    -----
    Will *not* raise a FileNotFoundError if the cache does not exist; will
    simply do nothing.
    """
    try:
        shutil.rmtree(get_data_home())
    except FileNotFoundError:  # no cached data
        pass


def get_data_home():
    """Get the location of the Pytolemy cache.

    Return the location on disk where were cache datasets outside of
    the package. Defaults to ``~/pytolemy_data``, but can be set via
    environment variable using "PYTOLEMY_DATA_DIR".

    Returns
    -------
    path_location : str
        Return the location of the Pytolemy directory.
    """
    return os.environ.get('PYTOLEMY_DATA_DIR',
                          expanduser(join('~', 'pytolemy_data')))


def _decompress_and_cache_dataset(zip_key):
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
    cache = _safe_mkdirs(get_data_home())  # e.g., /Users/<you>/..._data

    # Check if it's already there
    filename = zip_key.split(os.sep)[-1]
    output_location = join(cache, filename[:-4])
    if not exists(output_location):
        # Unzip it from the datasets dir INTO the cache
        with zipfile.ZipFile(zip_key, 'r') as zf:
            zf.extractall(cache)  # datasets/../XXX.zip -> cache/XXX/


def _get_module_path():
    """Get the location of the datasets directory"""
    return abspath(dirname(__file__))


def _cache_test_data():
    """Cache and unzip the test data (19TC....zip)"""
    _decompress_and_cache_dataset(
        join(_get_module_path(), 'data', '19TCG240845.zip'))

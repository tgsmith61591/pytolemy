# -*- coding: utf-8 -*-

from __future__ import absolute_import

from PIL import Image
import numpy as np
import os

__all__ = [
    'jp2_to_tiff',
    'tiff_to_jp2'
]


def _check_file(path, ext):
    if not os.path.isfile(path):
        raise OSError("Specified input path does not exist: %s" % path)
    if not path.endswith(ext):
        raise ValueError("Specified path should end with '%s'")


def jp2_to_tiff(input_path, output_path=None):
    """Convert a JP2 image to a TIFF file.

    Parameters
    ----------
    input_path : str
        An absolute path to the .jp2 file on disk. If the file
        does not exist, an OSError will be raised.

    output_path : str or None, optional (default=None)
        An absolute path to where the file will be written after
        converted to a TIFF. If None (default), will be equivalent
        to the ``input_path`` with a different extension.
    """
    _check_file(input_path, 'jp2')
    # TODO: Gigi


def tiff_to_jp2(input_path, output_path=None):
    """Convert a TIFF image to a JP2 file.

    Parameters
    ----------
    input_path : str
        An absolute path to the .tiff file on disk. If the file
        does not exist, an OSError will be raised.

    output_path : str or None, optional (default=None)
        An absolute path to where the file will be written after
        converted to a JP2. If None (default), will be equivalent
        to the ``input_path`` with a different extension.
    """
    _check_file(input_path, 'tif')
    # TODO: Gigi

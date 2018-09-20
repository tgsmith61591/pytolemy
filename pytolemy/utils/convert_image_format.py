# -*- coding: utf-8 -*-

from __future__ import absolute_import
from PIL import Image
import numpy as np
import os

__all__ = [
    'jp2_to_tiff',
    'tiff_to_jp2'
]


def jp2_to_tiff(jp2_image_path):
    check_if_file_exists(jp2_image_path)


def tiff_to_jp2(tiff_image_path):
    check_if_file_exists(tiff_image_path)


def check_if_file_exists(path):
    try:
        os.path.isfile(path)
    except FileNotFoundError:
        raise IOError("File not found!")

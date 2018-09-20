# -*- coding: utf-8 -*-

from __future__ import absolute_import
from pytolemy.utils.convert_image_format import tiff_to_jp2, jp2_to_tiff
import pytest
import os


def test_jp2_to_tiff():
    path = os.getcwd() + ' "*.jp2"'
    jp2_to_tiff(path)


def test_tiff_to_jp2():
    path = os.getcwd() + ' "*.tif"'
    tiff_to_jp2(path)


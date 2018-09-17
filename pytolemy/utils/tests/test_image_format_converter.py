# -*- coding: utf-8 -*-

from __future__ import absolute_import
from pytolemy.utils.convert_image_format import tiff_to_jp2, jp2_to_tiff
import pytest


def test_jp2_to_tiff():  # Check if tiff type image
    jp2_to_tiff('19TCG240845/19TCG240845.jp2')

def test_tiff_to_jp2():# Check if tiff type image
    tiff_to_jp2('19TCG240845/19TCG240845.tif')

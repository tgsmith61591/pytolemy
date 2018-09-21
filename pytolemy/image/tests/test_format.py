# -*- coding: utf-8 -*-

from __future__ import absolute_import

from pytolemy.utils.testing import with_cached_test_images, \
    get_test_image_files
from pytolemy.image.format import tiff_to_jp2, jp2_to_tiff, \
    _check_file

import pytest


@with_cached_test_images
def test_check_file():
    # Test that if a file does NOT exist, we expect an OSError
    with pytest.raises(OSError):
        _check_file("some_file_that_doesnt_exist.jpg", "jpg")

    # Show that if a file DOES exist, but is of the wrong extension,
    # we bomb out. To do this, let's get the test image file paths
    # and snag the first one that is not jp2, and assert for jp2.
    img_path = [f for f in get_test_image_files() if not f.endswith("jp2")][0]
    with pytest.raises(ValueError):
        _check_file(img_path, "jp2")  # -> ValueError('not a jp2 file...')


# TODO: Gigi, deeper assertion after the function is actually written
@with_cached_test_images
def test_jp2_to_tiff():
    # Get the jp2 file:
    jp2_path = [f for f in get_test_image_files()
                if f.endswith("jp2")][0]
    jp2_to_tiff(input_path=jp2_path)


# TODO: Gigi, deeper assertion after the function is actually written
@with_cached_test_images
def test_tiff_to_jp2():
    # Get the tiff file:
    tif_path = [f for f in get_test_image_files()
                if f.endswith("tif")][0]
    tiff_to_jp2(input_path=tif_path)

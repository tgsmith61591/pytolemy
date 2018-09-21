# -*- coding: utf-8 -*-

from __future__ import absolute_import

from pytolemy.datasets import remove_cache
from pytolemy.utils.testing import with_cached_test_images, \
    get_test_image_files

import pytest


# Test the error case where the directory may not exist yet
@with_cached_test_images
def test_get_files_corner_case():
    # The cache DOES exist right now (due to the decorator). So remove it
    remove_cache()

    # Now try to get the file names and show we fail with a ValueError
    with pytest.raises(ValueError):
        get_test_image_files()

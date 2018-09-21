# -*- coding: utf-8 -*-

from __future__ import absolute_import

from pytolemy.datasets import remove_cache
from pytolemy.utils.testing import with_cached_test_images, get_test_image_dir

import os


@with_cached_test_images
def test_create_remove():
    assert os.path.exists(get_test_image_dir())

    # Remove now
    remove_cache()
    assert not os.path.exists(get_test_image_dir())

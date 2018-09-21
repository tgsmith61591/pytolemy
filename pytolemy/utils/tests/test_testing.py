# -*- coding: utf-8 -*-

from __future__ import absolute_import

from pytolemy.utils.testing import with_cached_test_images, get_test_image_dir

import os


@with_cached_test_images
def test_decorator():
    assert os.path.exists(get_test_image_dir())

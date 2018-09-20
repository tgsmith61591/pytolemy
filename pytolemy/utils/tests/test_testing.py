# -*- coding: utf-8 -*-

from __future__ import absolute_import

from pytolemy.utils.testing import with_cached_test_images
from pytolemy.datasets import _get_cache_location

import os


@with_cached_test_images
def test_decorator():
    assert os.path.exists(os.path.join(_get_cache_location(), '19TCG240875'))

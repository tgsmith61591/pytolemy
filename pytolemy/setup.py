# -*- coding: utf-8 -*-
# Auto-generated with bear v0.1.1


from __future__ import print_function, division, absolute_import

import os

from pytolemy._build_utils import maybe_cythonize_extensions


# DEFINE CONFIG
def configuration(parent_package='', top_path=None):
    from numpy.distutils.misc_util import Configuration

    libs = []
    if os.name == 'posix':
        libs.append('m')

    config = Configuration('pytolemy', parent_package, top_path)

    # These are build utilities that are used as a smoke test for whether we
    # end up building the Cython source correctly
    config.add_subpackage('__check_build')
    config.add_subpackage('__check_build/tests')
    config.add_subpackage('_build_utils')
    config.add_subpackage('_build_utils/tests')

    # This is where you'll add your submodules that do NOT need Cythonizing,
    # e.g.: config.add_subpackage('utils')

    # This is where you'll add your module tests -- must be added after the
    # submodules were added above!
    # config.add_subpackage('utils/tests')

    # This is where you'll add (in the same format as above) the submodules
    # that DO need further cythonizing

    # And this is where we cythonize
    maybe_cythonize_extensions(top_path, config)

    return config


if __name__ == '__main__':
    from numpy.distutils.core import setup
    setup(**configuration(top_path='').todict())

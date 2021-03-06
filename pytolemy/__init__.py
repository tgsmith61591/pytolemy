# -*- coding: utf-8 -*-
#
# Auto-generated with bear v0.1.1, (c) Taylor G Smith

__version__ = '0.1.0'

try:
    # This variable is injected in the __builtins__ by the build
    # process. It is used to enable importing subpackages of bear when
    # the binaries are not built
    __PYTOLEMY_SETUP__
except NameError:
    __PYTOLEMY_SETUP__ = False

if __PYTOLEMY_SETUP__:
    import sys as _sys
    _sys.stdout.write('Partial import of pytolemy during '
                      'the build process.\n')
    del _sys
else:
    # Global namespace imports
    # Here, you'll import submodules from your package to make them importable
    # at the top level of the package. For instance, if you want to be able to
    # import 'pytolemy.utils', you'd mark 'utils' here as follows:

    __all__ = [
        'utils'
    ]


# function for finding the package
def package_location():
    import os
    return os.path.abspath(os.path.dirname(__file__))


def setup_module(module):
    # Fixture to assure global seeding of RNG
    import numpy as np
    import random

    _random_seed = int(np.random.uniform() * (2 ** 31 - 1))
    np.random.seed(_random_seed)
    random.seed(_random_seed)

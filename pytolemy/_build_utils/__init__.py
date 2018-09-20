"""
Utilities useful during the build -- adapted from sklearn.
"""
# author: Andy Mueller, Gael Varoquaux
# license: BSD

from __future__ import division, print_function, absolute_import

from numpy.distutils.system_info import get_info
from distutils.version import LooseVersion

import os

DEFAULT_ROOT = 'pytolemy'  # also used as package name in error reporting
CYTHON_MIN_VERSION = '0.23'


def get_blas_info():
    def atlas_not_found(blas_info_):
        def_macros = blas_info.get('define_macros', [])
        for x in def_macros:
            if x[0] == "NO_ATLAS_INFO":
                # if x[1] != 1 we should have lapack
                # how do we do that now?
                return True
            if x[0] == "ATLAS_INFO":
                if "None" in x[1]:
                    # this one turned up on FreeBSD
                    return True
        return False

    blas_info = get_info('blas_opt', 0)
    if (not blas_info) or atlas_not_found(blas_info):
        cblas_libs = ['cblas']
        blas_info.pop('libraries', None)
    else:
        cblas_libs = blas_info.pop('libraries', [])

    return cblas_libs, blas_info


def build_from_c_and_cpp_files(extensions):
    """Modify the extensions to build from the .c and .cpp files.
    This is useful for releases, this way cython is not required to
    run python setup.py install.
    """
    for extension in extensions:
        sources = []
        for sfile in extension.sources:
            path, ext = os.path.splitext(sfile)
            if ext in ('.pyx', '.py'):
                if extension.language == 'c++':
                    ext = '.cpp'
                else:
                    ext = '.c'
                sfile = path + ext
            sources.append(sfile)
        extension.sources = sources


def maybe_cythonize_extensions(top_path, config):
    """Tweaks for building extensions between release and development mode."""
    is_release = os.path.exists(os.path.join(top_path, 'PKG-INFO'))

    if is_release:
        build_from_c_and_cpp_files(config.ext_modules)
    else:
        message = ('Please install cython with a version >= {0} in order '
                   'to build a {1} development version.').format(
                       CYTHON_MIN_VERSION, DEFAULT_ROOT)
        try:
            import Cython
            if LooseVersion(Cython.__version__) < CYTHON_MIN_VERSION:
                message += ' Your version of Cython was {0}.'.format(
                    Cython.__version__)
                raise ValueError(message)
            from Cython.Build import cythonize
        except ImportError as exc:
            exc.args += (message,)
            raise

        config.ext_modules = cythonize(config.ext_modules)


def check_gdal():
    # Raise a comprehensible error for a GDAL import failure
    try:
        from osgeo import gdal
    except ImportError as e:
        raise BuildError("""%s
___________________________________________________________________________
In order to install pytolemy, you must have a working GDAL distribution and
the pygdal python library.

Windows:

    https://gis.stackexchange.com/questions/2276/installing-gdal-with-python-on-windows

Mac:

    $ brew install gdal

Linux:

    $ sudo apt-get install libgdal1-dev
    
You'll also need to install a version of pygdal corresponding to your version
of GDAL. You can find your version of GDAL like so:

    $ gdal-config --version
    1.8.1
    
For version 1.8.1, to install the corresponding python package, you'd run:

    $ pip install pygdal>=1.8.1.0,<=1.8.1.999
    
See https://github.com/nextgis/pygdal for information on supported GDAL 
versions.
""" % e)


class BuildError(BaseException):
    """Used to raise errors during the build"""

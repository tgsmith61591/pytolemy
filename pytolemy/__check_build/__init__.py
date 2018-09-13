"""Module to give helpful messages to the user that did not
compile the pytolemy package properly.
"""
import os

PKG_NAME = "pytolemy"

INPLACE_MSG = """
It appears that you are importing a local {0} source tree. For
this, you need to have an inplace install. Maybe you are in the source
directory and you need to try from another location.""".format(PKG_NAME)

STANDARD_MSG = """
If you have used an installer, please check that it is suited for your
Python version, your operating system and your platform."""


def raise_build_error(e):
    # Raise a comprehensible error and list the contents of the
    # directory to help debugging on the mailing list.
    local_dir = os.path.split(__file__)[0]
    msg = STANDARD_MSG
    if local_dir == "{0}/__check_build".format(PKG_NAME):
        # Picking up the local install: this will work only if the
        # install is an 'inplace build'
        msg = INPLACE_MSG
    dir_content = list()
    for i, filename in enumerate(os.listdir(local_dir)):
        if (i + 1) % 3:
            dir_content.append(filename.ljust(26))
        else:
            dir_content.append(filename + '\n')
    raise ImportError("""%s
___________________________________________________________________________
Contents of %s:
%s
___________________________________________________________________________
It seems that pytolemy has not been built correctly.
If you have installed pytolemy from source, please do not forget
to build the package before using it: run `python setup.py install` or
`make` from the top-level directory.
%s""" % (e, local_dir, ''.join(dir_content).strip(), msg))

try:
    from ._check_build import check_build
except ImportError as ie:
    raise_build_error(ie)

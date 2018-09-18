# -*- coding: utf-8 -*-

from __future__ import absolute_import
#from osgeo import gdal
#import gdaltest
from PIL import Image

import numpy as np
import os

__all__ = [
    'jp2_to_tiff',
    'tiff_to_jp2'
]

def jp2_to_tiff(jp2_image_path):
    file_name = os.path.splitext(jp2_image_path)[0]

 #   input_image = gdal.Open(jp2_image_path)
 #   output_image = gdal.Translate('output.tif', input_image)

 #   if output_image is None:
 #       gdaltest.post_reason('got error/warning')
 #       return 'fail'


def tiff_to_jp2(tiff_image_path):
    im = Image.open(tiff_image_path)
    out = im.convert("RGB")


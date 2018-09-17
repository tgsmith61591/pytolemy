# -*- coding: utf-8 -*-

from __future__ import absolute_import

from PIL import Image
import numpy as np

__all__ = [
    'jp2_to_tiff',
    'tiff_to_jp2'
]

def jp2_to_tiff(jp2_image_path):
    im = Image.open(jp2_image_path)
    imarray = np.array(im) # converts to array
    #im.show()

def tiff_to_jp2(tiff_image_path):
    im = Image.open(tiff_image_path)
    out = im.convert("RGB")
    #out.save(outfile, "JPEG", quality=90)

#!/usr/bin/env python
# -*- coding: utf8 -*-

from gimpfu import *


def strong_black_and_white(image, drawable):
    pdb.gimp_image_undo_group_start(image)

    pdb.gimp_desaturate_full(drawable, DESATURATE_LUMINOSITY)
    layer = pdb.gimp_image_get_active_layer(image)
    layer_copy = pdb.gimp_layer_new_from_drawable(layer, image)
    pdb.gimp_image_insert_layer(image, layer_copy, None, 0)
    pdb.gimp_layer_set_mode(layer_copy, OVERLAY_MODE)
    layer_merged = pdb.gimp_image_merge_down(image, layer_copy, EXPAND_AS_NECESSARY)

    pdb.gimp_image_undo_group_end(image)


register("gimp_strong_black_and_white",
         "Strong black and white",
         "Desature layer, make copy and set overlay mode",
         "Ossi Myllymäki",
         "(©) 2020 Ossi Myllymäki",
         "2020-12-02",
         "<Image>/Filters/Extra/Strong black and white",
         'RGB*',
         [],
         '',
         strong_black_and_white)

main()

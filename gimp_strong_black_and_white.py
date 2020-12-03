#!/usr/bin/env python
# -*- coding: utf8 -*-

from utils import *


def strong_black_and_white(image, drawable):
    start_image_undo(image)

    current_active_layer = get_active_layer(image)

    layer_desaturated = copy_and_insert_layer(current_active_layer, image)
    rename_layer(layer_desaturated, "Desaturated")
    desaturate_layer(layer_desaturated)

    layer_saturated_overlay = copy_and_insert_layer(layer_desaturated, image)
    rename_layer(layer_saturated_overlay, "Desaturated overlay")
    set_overlay_mode(layer_saturated_overlay)

    _, image = new_layer_from_visible(image)

    end_image_undo(image)


register("gimp_strong_black_and_white",
         "Strong black and white",
         "Desature layer, make copy and set overlay mode",
         "Ossi Myllymäki",
         "(©) 2020 Ossi Myllymäki",
         "2020-12-03",
         "<Image>/Filters/Extra/Strong black and white",
         'RGB*',
         [],
         '',
         strong_black_and_white)

main()

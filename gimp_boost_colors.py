#!/usr/bin/env python
# -*- coding: utf8 -*-

from utils import *


def boost_colors(image, drawable, opacity):

    width, height = get_image_size(image)

    start_image_undo(image)

    active_layer = get_active_layer(image)
    active_layer = copy_and_insert_layer(active_layer, image)
    active_layer = copy_and_insert_layer(active_layer, image)

    desaturate_layer(active_layer)
    invert_colors(active_layer, image)

    active_layer = get_active_layer(image)
    horizontal_radius = 20 * width / 1000
    vertical_radius = 20 * height / 1000
    gaussian_blur(active_layer,
                  image,
                  horizontal_radius=horizontal_radius,
                  vertical_radius=vertical_radius)
    set_layer_opacity(active_layer, 35)

    layer_merged = merge_down(active_layer, image)
    set_grain_merge_mode(layer_merged)
    set_layer_opacity(layer_merged, opacity)

    final_layer, image = new_layer_from_visible(image)

    rename_layer(final_layer, "Final")
    rename_layer(layer_merged, "Color boosting")

    end_image_undo(image)


register("gimp_boost_colors",
         "Boost colors of photo",
         "Boost colors of photo",
         "Ossi Myllymäki",
         "(©) 2020 Ossi Myllymäki",
         "2020-12-03",
         "<Image>/Filters/Extra/Boost colors",
         'RGB*',
         [
             (PF_SLIDER, "opacity", "Opacity", 35, (0, 100, 1)),
         ],
         [],
         boost_colors)

main()

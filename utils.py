from gimpfu import *


def copy_and_insert_layer(input_layer, image):
    output_layer = pdb.gimp_layer_new_from_drawable(input_layer, image)
    pdb.gimp_image_insert_layer(image, output_layer, None, 0)
    return output_layer


def new_layer_from_visible(image):
    layer = pdb.gimp_layer_new_from_visible(image, image, "Final")
    pdb.gimp_image_insert_layer(image, layer, None, 0)
    return layer, image


def get_active_layer(image):
    return pdb.gimp_image_get_active_layer(image)


def rename_layer(layer, name):
    pdb.gimp_item_set_name(layer, name)


def desaturate_layer(layer):
    pdb.gimp_desaturate_full(layer, DESATURATE_LUMINOSITY)


def set_overlay_mode(layer):
    pdb.gimp_layer_set_mode(layer, OVERLAY_MODE)


def start_image_undo(image):
    pdb.gimp_image_undo_group_start(image)


def end_image_undo(image):
    pdb.gimp_image_undo_group_end(image)


def invert_colors(layer, image):
    pdb.script_fu_gm_color_invert_2(image, layer)


def gaussian_blur(layer, image, horizontal_radius=5, vertical_radius=5):
    pdb.plug_in_gauss(image, layer, horizontal_radius, vertical_radius, 1)


def get_image_size(image):
    width = pdb.gimp_image_width(image)
    height = pdb.gimp_image_height(image)
    return width, height


def set_layer_opacity(layer, opacity):
    pdb.gimp_layer_set_opacity(layer, opacity)


def merge_down(layer, image):
    layer_merged = pdb.gimp_image_merge_down(image, layer, 0)
    return layer_merged


def set_grain_merge_mode(layer):
    pdb.gimp_layer_set_mode(layer, GRAIN_MERGE_MODE)

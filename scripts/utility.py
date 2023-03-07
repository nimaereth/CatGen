import pygame
import pygame_gui
import dicts.spritedicts as spritedicts


class UICatButton(pygame_gui.elements.UIButton):
    """
    Special button class to easily call a method to update the generated cat when interacted with
    """

    def __init__(self, xy, length_xy, manager, id, container, visible, action, *args):
        """
        Initialise the ui button

        :param xy: [x, y] coordinates for the button
        :param length_xy:  [width, height] of the button
        :param manager: pygame_gui uimanager for handling the screen"s ui elements
        :param id: object id for button
        :param container: ui container to hold tab UI elements
        :param visible: handle button visibility, 0 = not visible, 1 = visible
        :param action: function to call when button is interacted with
        :param args: optional parameters for function
        """
        super().__init__(pygame.Rect(xy, length_xy), "", manager=manager, object_id=id, visible=visible,
                         container=container)
        self.action = action  # function to run when button is pressed
        self.args = args

    def run(self, cat):  # Run method on cat
        if self.action is not None:
            self.action(cat, *self.args)


def update_central_sprite(cat, pose):
    """Updates which sprite is displayed as the main sprite"""
    if pose != "adult":
        cat.active_pose = pose
    else:
        cat.active_pose = "adult longhair" if cat.pelt_length == "long" else "adult"


def update_pose(cat, step):
    """Changes the pose of the main sprite"""
    min = spritedicts.poses[cat.active_pose][0]
    max = spritedicts.poses[cat.active_pose][2]

    # Update pose
    cat.poses[cat.active_pose] = (cat.poses[cat.active_pose] + step - min) % (max - min + 1) + min


def update_pelt_colour(cat, step):
    """Changes the cat's main pelt colour"""
    cat.pelt_colour_idx = (cat.pelt_colour_idx + step) % len(spritedicts.pelt_colours)


def update_pelt_pattern(cat, step):
    """Changes the cat's main pelt pattern"""
    cat.pelt_pattern_idx = (cat.pelt_pattern_idx + step) % len(spritedicts.pelt_patterns)


def update_white_patches(cat, step):
    """Changes the cat's white patches"""
    cat.white_patch_idx = (cat.white_patch_idx + step) % len(spritedicts.white_patches)


def toggle_tortie(cat):
    """Toggles tortie on/off"""
    cat.tortie = not cat.tortie


def update_tortie_colour(cat, step):
    """Changes the cat's tortie colours"""
    cat.tortie_colour_idx = (cat.tortie_colour_idx + step) % len(spritedicts.pelt_colours)


def update_tortie_patches(cat, step):
    """Changes the cat's tortie patches"""
    cat.tortie_patch_idx = (cat.tortie_patch_idx + step) % len(spritedicts.tortie_patches)


def update_tortie_pattern(cat, step):
    """Changes the cat's tortie patterns"""
    cat.tortie_pattern_idx = (cat.tortie_pattern_idx + step) % len(spritedicts.pelt_patterns)


def update_tint(cat, step):
    """Changes the cat's pelt tint"""
    cat.tint_idx = (cat.tint_idx + step) % len(spritedicts.tint_colours)


def toggle_heterochromia(cat):
    """Toggles heterochromia on/off"""
    cat.heterochromia = not cat.heterochromia


def update_eye1_colour(cat, step):
    """Changes the cat's eye1 colour"""
    cat.eye1_idx = (cat.eye1_idx + step) % len(spritedicts.eye_colours)


def update_eye2_colour(cat, step):
    """Changes the cat's eye2 colour"""
    cat.eye2_idx = (cat.eye2_idx + step) % len(spritedicts.eye_colours)


def update_skin(cat, step):
    """Changes the cat's skin colour"""
    cat.skin_idx = (cat.skin_idx + step) % len(spritedicts.skin_colours)


def reverse_cat(cat):
    """Flips the cat"""
    cat.reverse = not cat.reverse


def update_accessory(cat, step):
    """Changes the cat's accessory"""
    cat.stored_accessories_idx[cat.accessory] = (cat.stored_accessories_idx[cat.accessory] + step) % \
                                                len(spritedicts.accessories[cat.accessory])


def shade_cat(cat):
    """Shades/unshades the cat"""
    cat.shading = not cat.shading


def update_platform(cat, step):
    """Changes the platform"""
    cat.stored_platforms_idx[cat.platform] = (cat.stored_platforms_idx[cat.platform] + step) % len(spritedicts.seasons)


def update_white_tint(cat, step):
    """Changes the white patches tint"""
    cat.white_patch_tint_idx = (cat.white_patch_tint_idx + step) % len(spritedicts.white_patch_tints)

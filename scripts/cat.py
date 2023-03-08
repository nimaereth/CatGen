import ujson
import random

import pygame
import dicts.catdicts as catdicts
import dicts.spritedicts as spritedicts
from scripts.sprites import sprites, platforms
from dicts.names import *


class Cat:
    """Class for the generated cat"""

    def __init__(self):
        """Initialise the cat as a nameless kitten"""

        # General attributes
        self.ID = ""
        self.prefix = ""
        self.suffix = ""

        self.moons = 0
        self.age = "kitten"

        self.sex = catdicts.sex[0]
        self.gender = catdicts.gender[0]

        self.status = "kit"
        self.stored_statuses = {"kit": catdicts.statuses["kit"][0],
                                "adolescent": catdicts.statuses["adolescent"][0],
                                "adult": catdicts.statuses["adult"][0],
                                "elder": catdicts.statuses["elder"][0]}

        self.backstory = catdicts.backstories[0]

        self.trait = "kit"
        self.stored_traits = {"kit": catdicts.traits["kit"][0],
                              "nonkit": catdicts.traits["nonkit"][0]}

        self.skill = "unknown"
        self.stored_skills = {"unknown": catdicts.skills["unknown"][0],
                              "med": catdicts.skills["med"][0],
                              "elder": catdicts.skills["elder"][0],
                              "standard": catdicts.skills["standard"][0]}

        # Appearance-related attributes
        self.poses = {"kit": spritedicts.poses["kit"][0],
                      "adolescent": spritedicts.poses["adolescent"][0],
                      "adult": spritedicts.poses["adult"][0],
                      "adult longhair": spritedicts.poses["adult longhair"][0],
                      "elder": spritedicts.poses["elder"][0]}
        self.active_pose = "adult"

        self.pelt_length = spritedicts.pelt_lengths[0]
        self.pelt_colour_idx = 0
        self.pelt_pattern_idx = 0

        self.white_patch_idx = 0

        self.tortie = False
        self.tortie_patch_idx = 0
        self.tortie_colour_idx = 0
        self.tortie_pattern_idx = 0

        self.heterochromia = False
        self.eye1_idx = 0
        self.eye2_idx = 0

        self.tint_idx = 0
        self.white_patch_tint_idx = 0

        self.skin_idx = 0

        # Accessory attributes
        self.accessory = "none"
        self.stored_accessories_idx = {"none": None,
                                       "plant": 0,
                                       "wild": 0,
                                       "collar": 0,
                                       "bell collar": 0,
                                       "bow collar": 0,
                                       "nylon collar": 0}

        # Scars
        self.scars = ["none", "none", "none", "none"]

        # Extras
        self.reverse = False
        self.shading = False

        # Platforms
        self.platform = "beach"
        self.stored_platforms_idx = {"none": None,
                                     "beach": 0,
                                     "forest": 0,
                                     "mountainous": 0,
                                     "plains": 0}

    def get_json_dictionary(self):
        """
        Return dictionary to be used for json exporting

        """
        attributes = {"ID": self.ID,
                      "name_prefix": self.prefix.capitalize(),
                      "name_suffix": self.suffix.lower(),
                      "gender": self.sex,
                      "gender_align": self.get_gender(),
                      "birth_cooldown": 0,
                      "status": self.stored_statuses[self.status],
                      "backstory": self.backstory,
                      "age": self.age,
                      "moons": self.moons,
                      "trait": self.stored_traits[self.trait],
                      "parent1": None,
                      "parent2": None,
                      "mentor": None,
                      "former_mentor": [],
                      "patrol_with_mentor": 0,
                      "mentor_influence": [],
                      "mate": None,
                      "dead": False,
                      "died_by": [],
                      "paralyzed": False,
                      "no_kits": False,
                      "exiled": False,
                      "pelt_name": self.get_pelt_name(),
                      "pelt_color": spritedicts.pelt_colours[self.pelt_colour_idx],
                      "pelt_white": False if self.white_patch_idx == 0 else True,
                      "pelt_length": self.pelt_length,
                      "spirit_kitten": self.poses["kit"],
                      "spirit_adolescent": self.poses["adolescent"],
                      "spirit_young_adult": self.poses["adult"] if self.pelt_length != "long" else self.poses[
                          "adult longhair"],
                      "spirit_adult": self.poses["adult"] if self.pelt_length != "long" else self.poses[
                          "adult longhair"],
                      "spirit_senior_adult": self.poses["adult"] if self.pelt_length != "long" else self.poses[
                          "adult longhair"],
                      "spirit_elder": self.poses["elder"],
                      "spirit_dead": None,
                      "eye_colour": spritedicts.eye_colours[self.eye1_idx],
                      "eye_colour2": spritedicts.eye_colours[self.eye2_idx],
                      "reverse": self.reverse,
                      "white_patches": spritedicts.white_patches[self.white_patch_idx],
                      "white_patches_tint": list(spritedicts.white_patch_tints.keys())[self.white_patch_tint_idx],
                      "pattern": spritedicts.tortie_patches[self.tortie_patch_idx] if self.tortie else None,
                      "tortie_base": spritedicts.pelt_patterns[self.pelt_pattern_idx] if self.tortie else None,
                      "tortie_color": spritedicts.pelt_colours[self.tortie_colour_idx] if self.tortie else None,
                      "tortie_pattern": spritedicts.pelt_patterns[self.tortie_pattern_idx] if self.tortie else None,
                      "skin": spritedicts.skin_colours[self.skin_idx],
                      "tint": list(spritedicts.tint_colours.keys())[self.tint_idx],
                      "skill": self.stored_skills[self.skill],
                      "scars": [scar for scar in self.scars if scar != "none"],
                      "accessory": self.get_accessory(),
                      "experience": 0,
                      "dead_moons": 0,
                      "current_apprentice": [],
                      "former_apprentices": [],
                      "possible_scar": None,
                      "scar_event": [],
                      "df": False,
                      "outside": False,
                      "corruption": 0,
                      "life_givers": [],
                      "known_life_givers": [],
                      "virtues": [],
                      "retired": False,
                      "faded_offspring": [],
                      "opacity": 100,
                      "prevent_fading": False
                      }

        return attributes

    def save_json(self):
        """
        Generate/save the json file for the cat
        Json file is exported to folder savedcats as [cat name prefix][cat name suffix][cat ID].json

        """
        json_dict = self.get_json_dictionary()

        # TESTING
        with open("savedcats/" + json_dict["name_prefix"] + json_dict["name_suffix"] + self.ID + "json" + ".json",
                  "w") as outfile:
            ujson.dump(json_dict, outfile, indent=4)

    def preview_json(self):
        """
        Get json export as a string

        """
        json_dict = self.get_json_dictionary()

        json_string = ujson.dumps(json_dict, indent=4)
        return json_string

    def get_gender(self):
        """
        Return cat gender_align based on sex/gender

        """
        if self.sex != self.gender and self.gender != "nonbinary":
            return "trans " + self.gender
        else:
            return self.gender

    def update_age(self):
        """
        Update cat age based on moons

        """
        if self.moons > 150:
            self.age = "elder"
        else:
            for age, moon_range in catdicts.age_ranges.items():
                if moon_range[0] <= self.moons <= moon_range[1]:
                    self.age = age
                    break

    def get_pelt_name(self):
        """
        Return cat pelt name based on pelt attributes

        :return: string
        """
        if self.tortie:
            if spritedicts.white_patches[self.white_patch_idx] in spritedicts.high_whites:  # large white patches
                return "Calico"
            else:
                return "Tortie"
        elif spritedicts.pelt_patterns[self.pelt_pattern_idx] == "single":
            if self.white_patch_idx == 0:  # no white patches
                return "SingleColour"
            else:
                return "TwoColour"
        else:
            return spritedicts.pelt_patterns[self.pelt_pattern_idx].capitalize()

    def get_accessory(self):
        """
        Return cat accessory name

        """
        if self.accessory != "none":
            return spritedicts.accessories[self.accessory][self.stored_accessories_idx[self.accessory]]
        else:
            return None

    def platform_sprite(self):
        """Draw platform for cat sprite"""
        platform = pygame.Surface((80, 70), pygame.HWSURFACE | pygame.SRCALPHA)
        if self.platform != "none":
            platform.blit(platforms[self.platform +
                                    spritedicts.seasons[self.stored_platforms_idx[self.platform]]], (0, 0))

        platform = pygame.transform.scale(platform, (240, 210))
        return platform

    def big_sprite(self):
        """Get the active sprite of the cat according to its active pose"""
        active_sprite = pygame.Surface((50, 50), pygame.HWSURFACE | pygame.SRCALPHA)

        # Temporary boolean for easier sprite handling
        longhair_or_elder = self.pelt_length == "long" and self.active_pose not in ["kit", "adolescent"] \
                            or self.active_pose == "elder"

        try:
            # Base coat
            if longhair_or_elder:
                active_sprite.blit(sprites.sprites[spritedicts.pelt_patterns[self.pelt_pattern_idx] + "extra" +
                                                   spritedicts.pelt_colours[self.pelt_colour_idx] +
                                                   str(self.poses[self.active_pose])], (0, 0))
            else:
                active_sprite.blit(sprites.sprites[spritedicts.pelt_patterns[self.pelt_pattern_idx] +
                                                   spritedicts.pelt_colours[self.pelt_colour_idx] +
                                                   str(self.poses[self.active_pose])], (0, 0))

            # Tortie coat
            if self.tortie:
                if longhair_or_elder:
                    tortie_patch = sprites.sprites[spritedicts.pelt_patterns[self.tortie_pattern_idx] + "extra" +
                                                   spritedicts.pelt_colours[self.tortie_colour_idx] +
                                                   str(self.poses[self.active_pose])].copy()
                    tortie_patch.blit(sprites.sprites["tortiemask" + spritedicts.tortie_patches[self.tortie_patch_idx] +
                                                      str(self.poses[self.active_pose] + 9)], (0, 0),
                                      special_flags=pygame.BLEND_RGBA_MULT)
                else:
                    tortie_patch = sprites.sprites[spritedicts.pelt_patterns[self.tortie_pattern_idx] +
                                                   spritedicts.pelt_colours[self.tortie_colour_idx] +
                                                   str(self.poses[self.active_pose])].copy()
                    tortie_patch.blit(sprites.sprites["tortiemask" + spritedicts.tortie_patches[self.tortie_patch_idx] +
                                                      str(self.poses[self.active_pose])], (0, 0),
                                      special_flags=pygame.BLEND_RGBA_MULT)

                # Add tortie patch to sprite
                active_sprite.blit(tortie_patch, (0, 0))

            # Tints
            if self.tint_idx != 0:
                # Add tint to pelt
                tint = pygame.Surface((50, 50)).convert_alpha()
                tint.fill(list(spritedicts.tint_colours.values())[self.tint_idx])
                active_sprite.blit(tint, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

            # White patches
            if self.white_patch_idx != 0:
                if longhair_or_elder:
                    patch = sprites.sprites["whiteextra" + spritedicts.white_patches[self.white_patch_idx] +
                                            str(self.poses[self.active_pose])].copy()
                else:
                    patch = sprites.sprites["white" + spritedicts.white_patches[self.white_patch_idx] +
                                            str(self.poses[self.active_pose])].copy()

                # White patch tint
                if self.white_patch_tint_idx != 0:
                    patch_tint = pygame.Surface((50, 50)).convert_alpha()
                    patch_tint.fill(list(spritedicts.white_patch_tints.values())[self.white_patch_tint_idx])
                    patch.blit(patch_tint, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

                # Blit onto sprite
                active_sprite.blit(patch, (0, 0))

            # Eyes
            if longhair_or_elder:
                active_sprite.blit(sprites.sprites["eyesextra" + spritedicts.eye_colours[self.eye1_idx] +
                                                   str(self.poses[self.active_pose])], (0, 0))
                if self.heterochromia:
                    active_sprite.blit(sprites.sprites["eyes2extra" + spritedicts.eye_colours[self.eye2_idx] +
                                                       str(self.poses[self.active_pose])], (0, 0))
            else:
                active_sprite.blit(sprites.sprites["eyes" + spritedicts.eye_colours[self.eye1_idx] +
                                                   str(self.poses[self.active_pose])], (0, 0))
                if self.heterochromia:
                    active_sprite.blit(sprites.sprites["eyes2" + spritedicts.eye_colours[self.eye2_idx] +
                                                       str(self.poses[self.active_pose])], (0, 0))

            # Scars
            if longhair_or_elder:
                for scar in self.scars:
                    if scar not in spritedicts.scars2 and scar != "none":
                        active_sprite.blit(sprites.sprites["scarsextra" + scar +
                                                           str(self.poses[self.active_pose])], (0, 0))
            else:
                for scar in self.scars:
                    if scar not in spritedicts.scars2 and scar != "none":
                        active_sprite.blit(sprites.sprites["scars" + scar +
                                                           str(self.poses[self.active_pose])], (0, 0))

            # Shading
            if self.shading:
                if longhair_or_elder:
                    active_sprite.blit(sprites.sprites["shaders" + str(self.poses[self.active_pose] + 9)], (0, 0),
                                       special_flags=pygame.BLEND_RGB_MULT)
                    active_sprite.blit(sprites.sprites["lighting" + str(self.poses[self.active_pose] + 9)], (0, 0))
                else:
                    active_sprite.blit(sprites.sprites["shaders" + str(self.poses[self.active_pose])], (0, 0),
                                       special_flags=pygame.BLEND_RGB_MULT)
                    active_sprite.blit(sprites.sprites["lighting" + str(self.poses[self.active_pose])], (0, 0))

            # Lineart
            if longhair_or_elder:
                active_sprite.blit(sprites.sprites["lines" + str(self.poses[self.active_pose] + 9)], (0, 0))
            else:
                active_sprite.blit(sprites.sprites["lines" + str(self.poses[self.active_pose])], (0, 0))

            # Skin
            if longhair_or_elder:
                active_sprite.blit(sprites.sprites["skinextra" + spritedicts.skin_colours[self.skin_idx] +
                                                   str(self.poses[self.active_pose])], (0, 0))
            else:
                active_sprite.blit(sprites.sprites["skin" + spritedicts.skin_colours[self.skin_idx] +
                                                   str(self.poses[self.active_pose])], (0, 0))

            # Scars with masking
            if longhair_or_elder:
                for scar in self.scars:
                    if scar in spritedicts.scars2:
                        active_sprite.blit(sprites.sprites["scarsextra" + scar +
                                                           str(self.poses[self.active_pose])], (0, 0),
                                           special_flags=pygame.BLEND_RGBA_MIN)
            else:
                for scar in self.scars:
                    if scar in spritedicts.scars2:
                        active_sprite.blit(sprites.sprites["scars" + scar +
                                                           str(self.poses[self.active_pose])], (0, 0),
                                           special_flags=pygame.BLEND_RGBA_MIN)
            #
            # Accessories
            if self.accessory != "none":
                if longhair_or_elder:
                    # Med cat herbs
                    if self.accessory == "plant":
                        active_sprite.blit(sprites.sprites["acc_herbsextra" +
                                                           spritedicts.accessories[self.accessory]
                                                           [self.stored_accessories_idx[self.accessory]] +
                                                           str(self.poses[self.active_pose])], (0, 0))
                    # Wild
                    elif self.accessory == "wild":
                        active_sprite.blit(sprites.sprites["acc_wildextra" +
                                                           spritedicts.accessories[self.accessory]
                                                           [self.stored_accessories_idx[self.accessory]] +
                                                           str(self.poses[self.active_pose])], (0, 0))
                    # Collars
                    elif self.accessory in ["collar", "bell collar", "bow collar", "nylon collar"]:
                        active_sprite.blit(sprites.sprites["collarsextra" +
                                                           spritedicts.accessories[self.accessory]
                                                           [self.stored_accessories_idx[self.accessory]] +
                                                           str(self.poses[self.active_pose])], (0, 0))
                else:
                    # Med cat herbs
                    if self.accessory == "plant":
                        active_sprite.blit(sprites.sprites["acc_herbs" +
                                                           spritedicts.accessories[self.accessory]
                                                           [self.stored_accessories_idx[self.accessory]] +
                                                           str(self.poses[self.active_pose])], (0, 0))
                    # Wild
                    elif self.accessory == "wild":
                        active_sprite.blit(sprites.sprites["acc_wild" +
                                                           spritedicts.accessories[self.accessory]
                                                           [self.stored_accessories_idx[self.accessory]] +
                                                           str(self.poses[self.active_pose])], (0, 0))
                    # Collars
                    elif self.accessory in ["collar", "bell collar", "bow collar", "nylon collar"]:
                        active_sprite.blit(sprites.sprites["collars" +
                                                           spritedicts.accessories[self.accessory]
                                                           [self.stored_accessories_idx[self.accessory]] +
                                                           str(self.poses[self.active_pose])], (0, 0))
        except (TypeError, KeyError):
            print("ERROR")

        # Upscale 3x
        active_sprite = pygame.transform.scale(active_sprite, (150, 150))

        # Reverse if needed
        if self.reverse:
            active_sprite = pygame.transform.flip(active_sprite, True, False)

        return active_sprite

    def small_sprites(self):
        """Return all cat sprites at all life stages"""
        # Other sprites
        other_sprites = pygame.Surface((200, 50), pygame.HWSURFACE | pygame.SRCALPHA)

        if self.pelt_length == 'long':
            lineart_list = ['kit', 'adolescent', 'adult longhair', 'elder']
        else:
            lineart_list = ['kit', 'adolescent', 'adult', 'elder']

        try:
            for idx, l in enumerate(lineart_list):
                sprite = pygame.Surface((50, 50), pygame.HWSURFACE | pygame.SRCALPHA)

                # Temporary boolean for easier sprite handling
                longhair_or_elder = l == 'adult longhair' or l == 'elder'

                # Base coat
                if longhair_or_elder:
                    sprite.blit(sprites.sprites[spritedicts.pelt_patterns[self.pelt_pattern_idx] + 'extra' +
                                                spritedicts.pelt_colours[self.pelt_colour_idx] +
                                                str(self.poses[l])], (0, 0))
                else:
                    sprite.blit(sprites.sprites[spritedicts.pelt_patterns[self.pelt_pattern_idx] +
                                                spritedicts.pelt_colours[self.pelt_colour_idx] +
                                                str(self.poses[l])], (0, 0))

                # Tortie coat
                if self.tortie:
                    if longhair_or_elder:
                        tortie_patch = sprites.sprites[spritedicts.pelt_patterns[self.tortie_pattern_idx] + 'extra' +
                                                       spritedicts.pelt_colours[self.tortie_colour_idx] +
                                                       str(self.poses[l])].copy()
                        tortie_patch.blit(sprites.sprites['tortiemask' +
                                                          spritedicts.tortie_patches[self.tortie_patch_idx] +
                                                          str(self.poses[l] + 9)], (0, 0),
                                          special_flags=pygame.BLEND_RGBA_MULT)
                    else:
                        tortie_patch = sprites.sprites[spritedicts.pelt_patterns[self.tortie_pattern_idx] +
                                                       spritedicts.pelt_colours[self.tortie_colour_idx] +
                                                       str(self.poses[l])].copy()
                        tortie_patch.blit(sprites.sprites['tortiemask' +
                                                          spritedicts.tortie_patches[self.tortie_patch_idx] +
                                                          str(self.poses[l])], (0, 0),
                                          special_flags=pygame.BLEND_RGBA_MULT)

                    # Add tortie patch to sprite
                    sprite.blit(tortie_patch, (0, 0))

                # Tints
                if self.tint_idx != 0:
                    # Add tint to pelt
                    tint = pygame.Surface((50, 50)).convert_alpha()
                    tint.fill(list(spritedicts.tint_colours.values())[self.tint_idx])
                    sprite.blit(tint, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

                # White patches
                if self.white_patch_idx != 0:
                    if longhair_or_elder:
                        patch = sprites.sprites['whiteextra' + spritedicts.white_patches[self.white_patch_idx] +
                                                str(self.poses[l])].copy()
                    else:
                        patch = sprites.sprites['white' + spritedicts.white_patches[self.white_patch_idx] +
                                                str(self.poses[l])].copy()

                    # White patch tint
                    if self.white_patch_tint_idx != 0:
                        patch_tint = pygame.Surface((50, 50)).convert_alpha()
                        patch_tint.fill(list(spritedicts.white_patch_tints.values())[self.white_patch_tint_idx])
                        patch.blit(patch_tint, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

                    # Blit onto sprite
                    sprite.blit(patch, (0, 0))

                # Eyes
                if longhair_or_elder:
                    sprite.blit(sprites.sprites['eyesextra' + spritedicts.eye_colours[self.eye1_idx] +
                                                str(self.poses[l])], (0, 0))
                    if self.heterochromia:
                        sprite.blit(sprites.sprites['eyes2extra' + spritedicts.eye_colours[self.eye2_idx] +
                                                    str(self.poses[l])], (0, 0))
                else:
                    sprite.blit(sprites.sprites['eyes' + spritedicts.eye_colours[self.eye1_idx] +
                                                str(self.poses[l])], (0, 0))
                    if self.heterochromia:
                        sprite.blit(sprites.sprites['eyes2' + spritedicts.eye_colours[self.eye2_idx] +
                                                    str(self.poses[l])], (0, 0))

                # Scars
                if longhair_or_elder:
                    for scar in self.scars:
                        if scar not in spritedicts.scars2 and scar != "none":
                            sprite.blit(sprites.sprites['scarsextra' + scar +
                                                        str(self.poses[l])], (0, 0))
                else:
                    for scar in self.scars:
                        if scar not in spritedicts.scars2 and scar != "none":
                            sprite.blit(sprites.sprites['scars' + scar +
                                                        str(self.poses[l])], (0, 0))

                # Shading
                if self.shading:
                    if longhair_or_elder:
                        sprite.blit(sprites.sprites['shaders' + str(self.poses[l] + 9)],
                                    (0, 0),
                                    special_flags=pygame.BLEND_RGB_MULT)
                        sprite.blit(sprites.sprites['lighting' + str(self.poses[l] + 9)],
                                    (0, 0))
                    else:
                        sprite.blit(sprites.sprites['shaders' + str(self.poses[l])], (0, 0),
                                    special_flags=pygame.BLEND_RGB_MULT)
                        sprite.blit(sprites.sprites['lighting' + str(self.poses[l])], (0, 0))

                # Lineart
                if longhair_or_elder:
                    sprite.blit(sprites.sprites['lines' + str(self.poses[l] + 9)], (0, 0))
                else:
                    sprite.blit(sprites.sprites['lines' + str(self.poses[l])], (0, 0))

                # Skin
                if longhair_or_elder:
                    sprite.blit(sprites.sprites['skinextra' + spritedicts.skin_colours[self.skin_idx] +
                                                str(self.poses[l])], (0, 0))
                else:
                    sprite.blit(sprites.sprites['skin' + spritedicts.skin_colours[self.skin_idx] +
                                                str(self.poses[l])], (0, 0))

                # Scars with masking
                if longhair_or_elder:
                    for scar in self.scars:
                        if scar in spritedicts.scars2:
                            sprite.blit(sprites.sprites['scarsextra' + scar +
                                                        str(self.poses[l])], (0, 0),
                                        special_flags=pygame.BLEND_RGBA_MIN)
                else:
                    for scar in self.scars:
                        if scar in spritedicts.scars2:
                            sprite.blit(sprites.sprites['scars' + scar +
                                                        str(self.poses[l])], (0, 0),
                                        special_flags=pygame.BLEND_RGBA_MIN)

                # Accessories
                if self.accessory != 'none':
                    if longhair_or_elder:
                        # Med cat herbs
                        if self.accessory == 'plant':
                            sprite.blit(sprites.sprites['acc_herbsextra' +
                                                        spritedicts.accessories[self.accessory]
                                                        [self.stored_accessories_idx[self.accessory]] +
                                                        str(self.poses[l])], (0, 0))
                        # Wild
                        elif self.accessory == 'wild':
                            sprite.blit(sprites.sprites['acc_wildextra' +
                                                        spritedicts.accessories[self.accessory]
                                                        [self.stored_accessories_idx[self.accessory]] +
                                                        str(self.poses[l])], (0, 0))
                        # Collars
                        elif self.accessory in ['collar', 'bell collar', 'bow collar', 'nylon collar']:
                            sprite.blit(sprites.sprites['collarsextra' +
                                                        spritedicts.accessories[self.accessory]
                                                        [self.stored_accessories_idx[self.accessory]] +
                                                        str(self.poses[l])], (0, 0))
                    else:
                        # Med cat herbs
                        if self.accessory == 'plant':
                            sprite.blit(sprites.sprites['acc_herbs' +
                                                        spritedicts.accessories[self.accessory]
                                                        [self.stored_accessories_idx[self.accessory]] +
                                                        str(self.poses[l])], (0, 0))
                        # Wild
                        elif self.accessory == 'wild':
                            sprite.blit(sprites.sprites['acc_wild' +
                                                        spritedicts.accessories[self.accessory]
                                                        [self.stored_accessories_idx[self.accessory]] +
                                                        str(self.poses[l])], (0, 0))
                        # Collars
                        elif self.accessory in ['collar', 'bell collar', 'bow collar', 'nylon collar']:
                            sprite.blit(sprites.sprites['collars' +
                                                        spritedicts.accessories[self.accessory]
                                                        [self.stored_accessories_idx[self.accessory]] +
                                                        str(self.poses[l])], (0, 0))

                if self.reverse:
                    sprite = pygame.transform.flip(sprite, True, False)

                other_sprites.blit(sprite, (50 * idx, 0))

        except (TypeError, KeyError):
            print('ERROR')

        return other_sprites

    def save_sprites(self, scale):
        all_sprites = self.small_sprites()
        scaling = {'1x': (80, 70),
                   '2x': (160, 140),
                   '3x': (240, 210),
                   '4x': (320, 280)}

        for i in range(4):
            image = pygame.Surface((80, 70), pygame.HWSURFACE | pygame.SRCALPHA)

            # Draw platform
            if self.platform != "none":
                image.blit(platforms[self.platform + spritedicts.seasons[self.stored_platforms_idx[self.platform]]],
                           (0, 0))

            # Cropped sprite
            cropped_sprite = pygame.Surface((50, 50), pygame.HWSURFACE | pygame.SRCALPHA)
            cropped_sprite.blit(all_sprites, (-50*i, 0))

            # Blit sprite onto platform
            image.blit(cropped_sprite, (15, 0))

            # Scaling
            image = pygame.transform.scale(image, scaling[scale])

            pygame.image.save(image, ('SavedCats/' + self.prefix + self.suffix + "sprite" + str(i+1) + '.png'))

    def randomise_info(self):
        """Only randomise cat info"""
        # Get random age
        self.age = random.choice(list(catdicts.age_ranges.keys()))
        self.moons = random.randint(list(catdicts.age_ranges[self.age])[0], list(catdicts.age_ranges[self.age])[1])

        self.sex = random.choice(catdicts.sex)
        self.gender = random.choice(catdicts.gender)

        # Get random status depending on age
        if self.age == "kitten":
            self.status = "kit"
        elif self.age == "adolescent":
            self.status = "adolescent"
        elif self.age == "elder":
            self.status = "elder"
        else:
            self.status = "adult"
        self.stored_statuses[self.status] = random.choice(catdicts.statuses[self.status])

        self.backstory = random.choice(catdicts.backstories)

        # Get random trait depending on age
        if self.age == "kitten":
            self.trait = "kit"
        else:
            self.trait = "nonkit"
        self.stored_traits[self.trait] = random.choice(catdicts.traits[self.trait])

        # Get random skill depending on age and status
        if self.age in ["kitten", "adolescent"]:
            self.skill = "unknown"
        elif self.stored_statuses[self.status] == "medicine cat":
            self.skill = "med"
        elif self.age == "elder":
            self.skill = "elder"
        else:
            self.skill = "standard"
        self.stored_skills[self.skill] = random.choice(catdicts.skills[self.skill])

        # Randomise name
        # Code taken and modified from names.py from ClanGen
        named_after_appearance = not random.getrandbits(3)
        possible_prefix_categories = []
        if not self.heterochromia:
            if spritedicts.eye_colours[self.eye1_idx] in eye_prefixes:
                possible_prefix_categories.append(eye_prefixes[spritedicts.eye_colours[self.eye1_idx]])
        if spritedicts.pelt_colours[self.pelt_colour_idx] in colour_prefixes:
            possible_prefix_categories.append(colour_prefixes[spritedicts.pelt_colours[self.pelt_colour_idx]])

        if named_after_appearance and possible_prefix_categories:
            prefix_category = random.choice(possible_prefix_categories)
            self.prefix = random.choice(prefix_category)
        else:
            self.prefix = random.choice(normal_prefixes)

        self.suffix = ""
        while self.suffix == "" or self.suffix == self.prefix.casefold() or str(self.suffix) in self.prefix.casefold():
            if self.get_pelt_name() == "SingleColour":
                self.suffix = random.choice(normal_suffixes)
            else:
                named_after_pelt = not random.getrandbits(3)
                if (named_after_pelt and self.get_pelt_name() in ["Tortie", "Calico"] and
                        spritedicts.pelt_patterns[self.tortie_pattern_idx] in tortie_pelt_suffixes):
                    self.suffix = random.choice(tortie_pelt_suffixes[spritedicts.pelt_patterns[
                        self.tortie_pattern_idx]])
                else:
                    self.suffix = random.choice(normal_suffixes)

    def randomise_appearance(self):
        """Only randomise appearance"""
        for i in self.poses.keys(): # generate random poses
            self.poses[i] = random.choice(spritedicts.poses[i])

        self.pelt_length = random.choice(spritedicts.pelt_lengths)
        # Update active pose if necessary to match pelt length
        if self.pelt_length == "long" and self.active_pose == "adult":
            self.active_pose = "adult longhair"
        elif self.pelt_length != "long" and self.active_pose == "adult longhair":
            self.active_pose = "adult"

        self.pelt_colour_idx = random.randint(0, len(spritedicts.pelt_colours)-1)
        self.pelt_pattern_idx = random.randint(0, len(spritedicts.pelt_patterns)-1)

        self.white_patch_idx = random.randint(0, len(spritedicts.white_patches)-1)
        if self.white_patch_idx != 0:
            self.white_patch_tint_idx = random.randint(0, len(spritedicts.white_patch_tints)-1)

        self.tortie = random.choices([True, False], (0.2, 0.8))[0]  # 1/5 chance of tortie
        if self.tortie:
            # Increase chances of ginger/brown tortie patches
            ginger_torties = [6, 7, 8, 9, 10]  # indexes
            brown_torties = [11, 12, 13]
            other_torties = [1, 2, 3, 4, 5, 14]

            # remove current pelt colour from whichever is relevant
            for l in [ginger_torties, brown_torties, other_torties]:
                if self.pelt_colour_idx in l:
                    l.remove(self.pelt_colour_idx)

            # bias towards ginger/brown torties
            choice = random.choices([ginger_torties, brown_torties, other_torties], [0.9, 0.09, 0.01])[0]
            choice = random.choice(choice)

            # randomise tortie
            self.tortie_patch_idx = random.randint(0, len(spritedicts.tortie_patches)-1)
            self.tortie_colour_idx = choice
            self.tortie_pattern_idx = random.randint(0, len(spritedicts.pelt_patterns)-1)

        self.heterochromia = random.choices([True, False], (0.1, 0.9))[0]  # 1/10 chance of heterochromia for balance

        self.eye1_idx = random.randint(0, len(spritedicts.eye_colours)-1)
        if self.heterochromia:
            self.eye2_idx = random.randint(0, len(spritedicts.eye_colours)-1)

        self.tint_idx = random.randint(0, len(spritedicts.tint_colours)-1)
        self.skin_idx = random.randint(0, len(spritedicts.skin_colours)-1)

        # Accessory attributes
        # 1/2 chance of having an accessory, more likely to have wild/plant accessories
        self.accessory = random.choices(list(spritedicts.accessories.keys()), [0.5, 0.2, 0.2, 0.025,
                                                                               0.025, 0.025, 0.025])[0]
        if self.accessory != "none":
            self.stored_accessories_idx[self.accessory] = random.randint(0,
                                                                         len(spritedicts.accessories[self.accessory])-1)

        # Scars
        # Randomly choose how many scars to have, biased to fewer scars
        self.scars = ["none", "none", "none", "none"]
        choice = random.choices(range(0, 5), [0.6, 0.3, 0.05, 0.04, 0.01])[0]
        for i in range(choice):
            self.scars[i] = random.choice(spritedicts.scars)

        # Extras
        self.reverse = random.choice([True, False])
        self.shading = random.choice([True, False])

        # Platforms
        self.platform = random.choice(spritedicts.biomes)
        if self.platform != "none":
            self.stored_platforms_idx[self.platform] = random.randint(0, len(spritedicts.seasons) - 1)

    def randomise_all(self):
        """Randomise everything"""
        self.randomise_appearance()
        self.randomise_info()

    def reset_info(self):
        """Only reset info"""

        # General attributes
        self.ID = ""
        self.prefix = ""
        self.suffix = ""

        self.moons = 0
        self.age = "kitten"

        self.sex = catdicts.sex[0]
        self.gender = catdicts.gender[0]

        self.status = "kit"
        self.stored_statuses = {"kit": catdicts.statuses["kit"][0],
                                "adolescent": catdicts.statuses["adolescent"][0],
                                "adult": catdicts.statuses["adult"][0],
                                "elder": catdicts.statuses["elder"][0]}

        self.backstory = catdicts.backstories[0]

        self.trait = "kit"
        self.stored_traits = {"kit": catdicts.traits["kit"][0],
                              "nonkit": catdicts.traits["nonkit"][0]}

        self.skill = "unknown"
        self.stored_skills = {"unknown": catdicts.skills["unknown"][0],
                              "med": catdicts.skills["med"][0],
                              "elder": catdicts.skills["elder"][0],
                              "standard": catdicts.skills["standard"][0]}

    def reset_appearance(self):
        """Only reset appearance"""
        # Appearance-related attributes
        self.poses = {"kit": spritedicts.poses["kit"][0],
                      "adolescent": spritedicts.poses["adolescent"][0],
                      "adult": spritedicts.poses["adult"][0],
                      "adult longhair": spritedicts.poses["adult longhair"][0],
                      "elder": spritedicts.poses["elder"][0]}
        self.active_pose = "adult"

        self.pelt_length = spritedicts.pelt_lengths[0]
        self.pelt_colour_idx = 0
        self.pelt_pattern_idx = 0

        self.white_patch_idx = 0

        self.tortie = False
        self.tortie_patch_idx = 0
        self.tortie_colour_idx = 0
        self.tortie_pattern_idx = 0

        self.heterochromia = False
        self.eye1_idx = 0
        self.eye2_idx = 0

        self.tint_idx = 0
        self.white_patch_tint_idx = 0

        self.skin_idx = 0

        # Accessory attributes
        self.accessory = "none"
        self.stored_accessories_idx = {"none": None,
                                       "plant": 0,
                                       "wild": 0,
                                       "collar": 0,
                                       "bell collar": 0,
                                       "bow collar": 0,
                                       "nylon collar": 0}

        # Scars
        self.scars = ["none", "none", "none", "none"]

        # Extras
        self.reverse = False
        self.shading = False

        # Platforms
        self.platform = "beach"
        self.stored_platforms_idx = {"none": None,
                                     "beach": 0,
                                     "forest": 0,
                                     "mountainous": 0,
                                     "plains": 0}

    def reset_all(self):
        """Reset absolutely everything"""
        self.reset_appearance()
        self.reset_info()

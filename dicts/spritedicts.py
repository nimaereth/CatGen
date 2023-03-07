"""Contains important dictionaries and lists for handling cat attributes related to sprite handling"""

# Poses
poses = {"kit": [0, 1, 2],
         "adolescent": [3, 4, 5],
         "adult": [6, 7, 8],
         "adult longhair": [0, 1, 2],
         "elder": [3, 4, 5]}

# Pelt lengths
pelt_lengths = ["short", "medium", "long"]

# Pelt colours and patterns
pelt_colours = ["WHITE", "PALEGREY", "SILVER", "GREY", "DARKGREY", "GHOST", "PALEGINGER", "GOLDEN", "GINGER",
                "DARKGINGER", "CREAM", "LIGHTBROWN", "BROWN", "DARKBROWN", "BLACK"]

pelt_patterns = ["single", "tabby", "marbled", "rosette", "smoke", "ticked", "speckled", "bengal", "mackerel",
                 "classic", "sokoke", "agouti", "singlestripe"]

# Tortie patches
tortie_patches = ["ONE", "TWO", "THREE", "FOUR", "REDTAIL", "DELILAH", "MINIMAL1", "MINIMAL2", "MINIMAL3", "MINIMAL4",
                  "OREO", "SWOOP", "MOTTLED", "SIDEMASK", "EYEDOT", "BANDANA", "PACMAN", "STREAMSTRIKE", "ORIOLE",
                  "ROBIN", "BRINDLE", "PAIGE"]

# White patches
white_patches = [None, "FULLWHITE", "ANY", "TUXEDO", "LITTLE", "COLOURPOINT", "VAN", "ANY2", "ONEEAR", "BROKEN",
                 "LIGHTTUXEDO", "BUZZARDFANG", "RAGDOLL", "LIGHTSONG", "VITILIGO", "TIP", "FANCY", "FRECKLES",
                 "RINGTAIL", "HALFFACE", "PANTS2", "GOATEE", "VITILIGO2", "TAIL", "BLAZE", "PRINCE", "BIB", "VEE",
                 "UNDERS", "PAWS", "MITAINE", "FAROFA", "DAMIEN", "MISTER", "BELLY", "TAILTIP", "TOES", "BROKENBLAZE",
                 "SCOURGE", "APRON", "CAPSADDLE", "MASKMANTLE", "SQUEAKS", "STAR", "TOESTAIL", "RAVENPAW", "HONEY",
                 "PANTS", "REVERSEPANTS", "SKUNK", "KARPATI", "HALFWHITE", "APPALOOSA", "PIEBALD", "CURVED", "HEART",
                 "LILTWO", "GLASS", "MOORISH", "SEPIAPOINT", "MINKPOINT", "SEALPOINT", "MAO", "LUNA", "CHESTSPECK",
                 "WINGS", "PAINTED", "HEART2", "BLACKSTAR"]

# White patches with high amounts of white, tortie cats with white patches in this category are classed as Calico
high_whites = ["ANY", "ANY2", "BROKEN", "FRECKLES", "RINGTAIL", "HALFFACE", "PANTS2", "GOATEE", "PRINCE", "FAROFA",
               "MISTER", "PANTS", "REVERSEPANTS", "HALFWHITE", "APPALOOSA", "PIEBALD", "CURVED", "GLASS", "MASKMANTLE",
               "MAO", "PAINTED", "VAN", "ONEEAR", "LIGHTSONG", "TAIL", "HEART", "MOORISH", "APRON", "CAPSADDLE",
               "CHESTSPECK", "BLACKSTAR", "FULLWHITE"]

# Eye colours
eye_colours = ["YELLOW", "AMBER", "HAZEL", "PALEGREEN", "GREEN", "BLUE", "DARKBLUE", "GREY", "CYAN", "EMERALD",
               "HEATHERBLUE", "SUNLITICE", "COPPER", "SAGE", "BLUE2", "PALEBLUE", "BLUEYELLOW", "BLUEGREEN",
               "PALEYELLOW", "GOLD", "GREENYELLOW"]

# Skin colours
skin_colours = ["BLACK", "RED", "PINK", "DARKBROWN", "BROWN", "LIGHTBROWN", "DARK", "DARKGREY", "GREY", "DARKSALMON",
                "SALMON", "PEACH", "DARKMARBLED", "MARBLED", "LIGHTMARBLED", "DARKBLUE", "BLUE", "LIGHTBLUE"]

# Tints
tint_colours = {"none": None,
                "pink": [253, 237, 237],
                "gray": [225, 225, 225],
                "red": [248, 226, 228],
                "black": [195, 195, 195],
                "orange": [255, 247, 235],
                "yellow": [250, 248, 225],
                "purple": [235, 225, 244],
                "blue": [218, 237, 245]}

white_patch_tints = {"none": None,
                     "darkcream": [236, 229, 208],
                     "cream": [247, 241, 225],
                     "offwhite": [238, 249, 252],
                     "gray": [208, 225, 229],
                     "pink": [252, 238, 243]}

# Accessories
accessories = {"none": None,
               "plant": ["MAPLE LEAF", "HOLLY", "BLUE BERRIES", "FORGET ME NOTS", "RYE STALK", "LAUREL", "BLUEBELLS",
                         "NETTLE", "POPPY", "LAVENDER", "HERBS", "PETALS", "OAK LEAVES", "CATMINT", "MAPLE SEED",
                         "JUNIPER", "DRY HERBS"],
               "wild": ["RED FEATHERS", "BLUE FEATHERS", "JAY FEATHERS", "MOTH WINGS", "CICADA WINGS"],
               "collar": ["CRIMSON", "BLUE", "YELLOW", "CYAN", "RED", "LIME", "GREEN", "RAINBOW", "BLACK", "SPIKES",
                          "PINK", "PURPLE", "MULTI", "INDIGO"],
               "bell collar": ["CRIMSONBELL", "BLUEBELL", "YELLOWBELL", "CYANBELL", "REDBELL", "LIMEBELL", "GREENBELL",
                               "RAINBOWBELL", "BLACKBELL", "SPIKESBELL", "PINKBELL", "PURPLEBELL", "MULTIBELL",
                               "INDIGOBELL"],
               "bow collar": ["CRIMSONBOW", "BLUEBOW", "YELLOWBOW", "CYANBOW", "REDBOW", "LIMEBOW", "GREENBOW",
                              "RAINBOWBOW", "BLACKBOW", "SPIKESBOW", "PINKBOW", "PURPLEBOW", "MULTIBOW", "INDIGOBOW"],
               "nylon collar": ["CRIMSONNYLON", "BLUENYLON", "YELLOWNYLON", "CYANNYLON", "REDNYLON", "LIMENYLON",
                                "GREENNYLON", "RAINBOWNYLON", "BLACKNYLON", "SPIKESNYLON", "WHITENYLON", "PINKNYLON",
                                "PURPLENYLON", "MULTINYLON", "INDIGONYLON"]}

# Scars
scars = ["none", "ONE", "TWO", "THREE", "LEFTEAR", "RIGHTEAR", "NOTAIL", "MANLEG", "BRIGHTHEART", "MANTAIL",
         "NOLEFTEAR", "NORIGHTEAR", "NOEAR", "BRIDGE", "RIGHTBLIND", "LEFTBLIND", "BOTHBLIND", "BURNPAWS", "BURNTAIL",
         "BURNBELLY", "BEAKCHEEK", "BEAKLOWER", "BURNRUMP", "CATBITE", "RATBITE", "TAILSCAR", "SNOUT", "CHEEK", "SIDE",
         "THROAT", "TAILBASE", "BELLY", "TOETRAP", "SNAKE", "LEGBITE", "NECKBITE", "FACE", "HALFTAIL", "NOPAW",
         "FROSTFACE", "FROSTTAIL", "FROSTMITT", "FROSTSOCK", "QUILLCHUNK", "QUILLSCRATCH"]

# Scars using masking
scars2 = ["LEFTEAR", "RIGHTEAR", "NOTAIL", "HALFTAIL", "NOPAW", "NOLEFTEAR", "NORIGHTEAR", "NOEAR"]

# Platforms
biomes = ["none", "beach", "forest", "mountainous", "plains"]

seasons = ["greenleaf_dark", "greenleaf_light", "leafbare_dark", "leafbare_light", "leaffall_dark",
           "leaffall_light", "newleaf_dark", "newleaf_light"]

"""Contains name prefixes and suffixes to use during random cat generation"""

# Name prefixes
# Prefixes that can randomly generate any time
normal_prefixes = [
    "Adder", "Alder", "Ant", "Antler", "Apple", "Apricot", "Arc", "Arch", "Aspen", "Aster",
    "Badger", "Barley", "Basil", "Bass", "Bay", "Bayou", "Beam", "Bear", "Beaver", "Bee", "Beech", "Beetle", "Berry",
    "Big", "Birch", "Bird", "Bite", "Bitter", "Bittern", "Blizzard", "Bloom",
    "Blossom", "Blotch", "Bluebell", "Bluff", "Bog", "Borage", "Bough", "Boulder", "Bounce", "Bracken", "Bramble",
    "Brave", "Breeze", "Briar", "Bright", "Brindle", "Bristle", "Broken", "Brook", "Broom", "Brush", "Bubbling", "Buck",
    "Bug", "Bumble", "Burdock", "Burr", "Bush", "Buzzard", "Carp", "Cave", "Cedar", "Chaffinch", "Chasing", "Cherry",
    "Chestnut", "Chive", "Cicada", "Claw", "Clay", "Clear", "Cliff", "Clover", "Condor",
    "Cone", "Conifer", "Cougar", "Cow", "Coyote", "Crag", "Crane", "Creek", "Cress", "Crested", "Cricket", "Crooked",
    "Crouch", "Curl", "Curlew", "Curly", "Cypress", "Dahlia", "Daisy", "Damp", "Dancing", "Dandelion", "Dapple",
    "Dappled", "Dawn", "Deer", "Dew", "Doe", "Dog", "Down", "Downy", "Drift",
    "Drizzle", "Dry", "Duck", "Dusk", "Eagle", "Echo", "Egret", "Elder", "Elm",
    "Ermine", "Falcon", "Fallen", "Falling", "Fallow", "Fawn", "Feather", "Fennel", "Fern",
    "Ferret", "Fidget", "Fin", "Finch", "Fir", "Fish", "Flail", "Flash", "Flax", "Fleck", "Fleet", "Flicker",
    "Flight", "Flint", "Flip", "Flood", "Flower", "Flutter", "Fly", "Fog", "Forest", "Freckle", "Fringe",
    "Frog", "Frond", "Furled", "Furze", "Fuzzy", "Gale", "Gander", "Gannet", "Garlic", "Goose",
    "Gorge", "Gorse", "Grass", "Gravel", "Grouse", "Gull", "Gust", "Hail", "Half", "Hare",
    "Hatch", "Haven", "Hawk", "Hay", "Hazel", "Heath", "Heavy", "Heron", "Hill", "Hollow", "Holly",
    "Honey", "Hoot", "Hop", "Hope", "Hornet", "Hound", "Iris", "Ivy", "Jackdaw", "Jagged", "Jay", "Jump", "Juniper",
    "Kestrel", "Kink", "Kite", "Lake", "Larch", "Lark", "Laurel", "Lavender", "Leaf", "Leap", "Leopard", "Lichen",
    "Light", "Lightning", "Lilac", "Lily", "Lion", "Little", "Lizard", "Locust", "Long", "Lotus", "Loud", "Low", "Lynx",
    "Mallow", "Mantis", "Maple", "Marigold", "Marsh", "Marten", "Meadow", "Midge",
    "Milk", "Milkweed", "Mink", "Minnow", "Mistle", "Mite", "Mole", "Moon", "Moor", "Morning", "Moss",
    "Mossy", "Moth", "Mottle", "Mottled", "Mouse", "Mumble", "Murk", "Myrtle", "Nectar", "Needle", "Nettle",
    "Newt", "Nut", "Oat", "Odd", "One", "Orange", "Osprey", "Pansy", "Panther", "Parsley", "Partridge", "Patch", "Peak",
    "Pear", "Peat", "Perch", "Petal", "Pheasant", "Pigeon", "Pike", "Pine", "Pink", "Piper", "Plover", "Plum", "Pod",
    "Pond", "Pool", "Poppy", "Posy", "Pounce", "Prance", "Prickle", "Prim", "Primrose", "Puddle", "Quail", "Quick",
    "Pop", "Quiet", "Quill", "Rabbit", "Raccoon", "Ragged", "Rain", "Rat", "Rattle", "Raven", "Reed",
    "Ridge", "Rift", "Ripple", "River", "Roach", "Rook", "Root", "Rose", "Rosy", "Rowan", "Rubble",
    "Running", "Rush", "Rye", "Sage", "Scorch", "Sedge", "Seed", "Shard", "Sharp", "Sheep",
    "Shell", "Shimmer", "Shining", "Shivering", "Short", "Shrew", "Shy", "Silk", "Silt", "Skip", "Sky", "Slate",
    "Sleek", "Sleet", "Slight", "Sloe", "Slope", "Small", "Snail", "Snake", "Snap", "Sneeze", "Snip", "Snook", "Soft",
    "Song", "Sorrel", "Spark", "Sparrow", "Speckle", "Spider", "Spike", "Spire", "Splash", "Spot", "Spotted", "Spring",
    "Spruce", "Squirrel", "Starling", "Stem", "Stoat", "Stork", "Stream", "Strike",
    "Stumpy", "Sunny", "Swallow", "Swamp", "Sweet", "Swift", "Sycamore", "Tall", "Talon", "Tangle", "Tansy", "Tawny",
    "Thistle", "Thorn", "Thrift", "Thrush", "Thunder", "Thyme", "Tiger", "Timber", "Tiny", "Tip", "Toad", "Torn",
    "Trout", "Tuft", "Tulip", "Tumble", "Turtle", "Vine", "Vixen", "Wasp", "Weasel", "Web", "Weed", "Wet", "Wheat",
    "Whirl", "Whisker", "Whisper", "Whispering", "Whistle", "Whorl", "Wild", "Willow", "Wind", "Wish", "Wing",
    "Wisteria", "Wolf", "Wood", "Wren", "Yarrow", "Yew"
]

# Colour prefixes based on cat"s pelt colour
colour_prefixes = {
    "WHITE": [
        "White", "White", "Pale", "Snow", "Cloud", "Cloudy", "Milk", "Hail", "Frost", "Frozen", "Freeze", "Ice", "Icy",
        "Sheep", "Blizzard", "Flurry", "Moon", "Light", "Bone", "Bright", "Swan", "Dove", "Wooly", "Cotton",
    ],
    "PALEGREY": [
        "Grey", "Silver", "Pale", "Light", "Cloud", "Cloudy", "Hail", "Frost", "Ice", "Icy", "Mouse", "Bright", "Fog",
        "Freeze", "Frozen", "Stone", "Pebble", "Dove", "Sky", "Cotton", "Heather", "Ashen"
    ],
    "SILVER": [
        "Grey", "Silver", "Cinder", "Ice", "Icy", "Frost", "Frozen", "Freeze", "Rain", "Blue",
        "River", "Blizzard", "Flurry", "Bone", "Bleak", "Stone", "Pebble", "Heather"
    ],
    "GREY": [
        "Grey", "Grey", "Ash", "Ashen", "Cinder", "Rock", "Stone", "Shade", "Mouse", "Smoke", "Smoky", "Shadow", "Fog",
        "Bone", "Bleak", "Rain", "Storm", "Soot", "Pebble", "Mist", "Misty", "Heather"
    ],
    "DARKGREY": [
        "Grey", "Shade", "Raven", "Crow", "Stone", "Dark", "Night", "Cinder", "Ash", "Ashen",
        "Smoke", "Smokey", "Shadow", "Bleak", "Rain", "Storm", "Pebble", "Mist", "Misty"
    ],
    "GHOST": [
        "Black", "Black", "Shade", "Shaded", "Crow", "Raven", "Ebony", "Dark",
        "Night", "Shadow", "Scorch", "Midnight", "Bleak", "Storm", "Violet", "Pepper", "Bat", "Fade"
    ],
    "PALEGINGER": [
        "Pale", "Ginger", "Sand", "Sandy", "Yellow", "Sun", "Sunny", "Light", "Lion", "Bright",
        "Honey", "Daisy", "Warm", "Robin"
    ],
    "GOLDEN": [
        "Gold", "Golden", "Yellow", "Sun", "Sunny", "Light", "Lightning", "Thunder",
        "Honey", "Tawny", "Lion", "Dandelion", "Marigold", "Warm"
    ],
    "GINGER": [
        "Ginger", "Ginger", "Red", "Fire", "Rust", "Flame", "Ember", "Sun", "Sunny", "Light", "Primrose", "Rose",
        "Rowan", "Fox", "Tawny", "Plum", "Orange", "Warm", "Burn", "Burnt", "Robin", "Amber"
    ],
    "DARKGINGER": [
        "Ginger", "Ginger", "Red", "Red", "Fire", "Flame", "Ember", "Oak", "Shade", "Russet",
        "Rowan", "Fox", "Orange", "Copper", "Cinnamon", "Burn", "Burnt", "Robin"
    ],
    "CREAM": [
        "Sand", "Sandy", "Yellow", "Pale", "Cream", "Light", "Milk", "Fawn",
        "Bone", "Daisy", "Branch", "Warm", "Robin", "Almond", "Acorn"
    ],
    "LIGHTBROWN": [
        "Brown", "Pale", "Light", "Mouse", "Dust", "Dusty", "Sand", "Sandy", "Bright", "Mud",
        "Hazel", "Vole", "Branch", "Warm", "Robin", "Almond", "Acorn", "Bark"
    ],
    "BROWN": [
        "Brown", "Oak", "Mouse", "Dark", "Shade", "Russet", "Dust", "Dusty", "Acorn", "Mud", "Deer", "Fawn", "Doe",
        "Stag", "Twig", "Owl", "Otter", "Log", "Vole", "Branch", "Hazel", "Robin", "Acorn", "Bark"
    ],
    "DARKBROWN": [
        "Brown", "Dark", "Shade", "Night", "Russet", "Rowan", "Mud", "Oak", "Stag", "Elk", "Twig",
        "Owl", "Otter", "Log", "Hickory", "Branch", "Robin", "Bark"
    ],
    "BLACK": [
        "Black", "Black", "Shade", "Shaded", "Crow", "Raven", "Ebony", "Dark",
        "Night", "Shadow", "Scorch", "Midnight", "Pepper", "Jet", "Bat", "Burnt"
    ]}

# Eye prefixes based on cat"s eye colour
eye_prefixes = {
    "YELLOW": ["Yellow", "Moon", "Daisy", "Honey", "Light"],
    "AMBER": ["Amber", "Sun", "Fire", "Gold", "Honey", "Scorch"],
    "HAZEL": ["Hazel", "Tawny", "Hazel", "Gold", "Daisy", "Sand"],
    "PALEGREEN": ["Pale", "Green", "Mint", "Fern", "Weed", "Olive"],
    "GREEN": ["Green", "Fern", "Weed", "Holly", "Clover", "Olive"],
    "BLUE": ["Blue", "Blue", "Ice", "Sky", "Lake", "Frost", "Water"],
    "DARKBLUE": ["Dark", "Blue", "Sky", "Lake", "Berry", "Water", "Deep"],
    "GREY": ["Grey", "Stone", "Silver", "Ripple", "Moon", "Rain", "Storm", "Heather"],
    "CYAN": ["Sky", "Blue", "River", "Rapid"],
    "EMERALD": ["Emerald", "Green", "Shine", "Blue", "Pine", "Weed"],
    "PALEBLUE": ["Pale", "Blue", "Sky", "River", "Ripple", "Day", "Cloud"],
    "PALEYELLOW": ["Pale", "Yellow", "Sun", "Gold"],
    "GOLD": ["Gold", "Golden", "Sun", "Amber", "Sap", "Honey"],
    "HEATHERBLUE": ["Heather", "Blue", "Lilac", "Rosemary", "Lavender", "Wisteria"],
    "COPPER": ["Copper", "Red", "Amber", "Brown", "Fire", "Cinnamon"],
    "SAGE": ["Sage", "Leaf", "Olive", "Bush", "Clove", "Green", "Weed"],
    "BLUE2": ["Blue", "Blue", "Ice", "Icy", "Sky", "Lake", "Frost", "Water"],
    "SUNLITICE": ["Sun", "Ice", "Icy", "Frost", "Sunrise", "Dawn", "Dusk", "Odd", "Glow"],
    "GREENYELLOW": ["Green", "Yellow", "Tawny", "Hazel", "Gold", "Daisy", "Sand", "Sandy", "Weed"]
}

# Suffixes
# Normal suffixes that can randomly generate any time
normal_suffixes = [
    "fur", "fur", "fur", "fur", "fur", "fur", "fur", "fur", "fur", "fur", "fur", "fur", "fur",
    "tuft", "tuft", "tuft", "tuft", "tuft", "tooth", "tooth", "tooth", "tooth", "tooth",
    "pelt", "pelt", "pelt", "pelt", "pelt", "pelt", "pelt", "pelt", "pelt", "pelt", "pelt", "pelt", "pelt",
    "tail", "tail", "tail", "tail", "tail", "tail", "tail", "tail", "claw", "claw", "claw", "claw", "claw", "claw",
    "claw", "foot", "foot", "foot", "foot", "foot", "whisker", "whisker", "whisker", "whisker", "whisker", "whisker",
    "heart", "heart", "heart", "heart", "heart", "heart", "heart", "heart", "heart", "heart",
    "acorn", "ash", "aster", "back", "bark", "beam", "bee", "belly", "berry", "bite", "bird", "blaze", "blink", "bloom",
    "blossom", "blotch", "bounce", "bracken", "branch", "breeze", "briar", "bright", "brook", "burr", "burrow", "bush",
    "call", "catcher", "cloud", "clover", "crawl", "creek", "cry", "dapple", "daisy", "dawn", "drift", "drop", "dusk",
    "dust", "ear", "ears", "eater", "eye", "eyes", "face", "fall", "fang", "fawn", "feather", "fern", "fin", "fire",
    "fish", "flake", "flame", "flight", "flick", "flood", "flower", "fox", "frost", "gaze", "goose", "gorse", "grass",
    "hail", "hare", "hawk", "haze", "heather", "hollow", "holly", "horse", "ice", "ivy", "jaw", "jay", "jump", "kite",
    "lake", "larch", "leaf", "leap", "leaves", "leg", "light", "lightning", "lilac", "lily", "lotus", "mask", "mark",
    "minnow", "mist", "moth", "moon", "moss", "mouse", "muzzle", "needle", "nettle", "night", "noise", "nose", "nut",
    "pad", "patch", "path", "peak", "petal", "plume", "pond", "pool", "poppy", "pounce", "puddle", "rain", "rapid",
    "ripple", "river", "roar", "rose", "rump", "run", "runner", "scar", "scratch", "seed", "shade", "shadow", "shell",
    "shine", "sight", "skip", "sky", "slip", "snout", "snow", "song", "spark", "speck", "speckle", "spirit", "splash",
    "spot", "spots", "spring", "stalk", "stem", "step", "stone", "storm", "streak", "stream", "strike", "stripe",
    "sun", "swipe", "swoop", "talon", "tooth", "thistle", "thorn", "throat", "toe", "tree", "throat", "watcher",
    "water", "wave", "whisper", "whistle", "willow", "wind", "wing", "wish"
]

# Pelt suffixes based on cat"s pelt pattern
pelt_suffixes = {
    "TwoColour": ["patch", "spot", "splash", "patch", "spots"],
    "Tabby": ["stripe", "feather", "leaf", "stripe", "shade"],
    "Marbled": ["stripe", "feather", "leaf", "stripe", "shade"],
    "Speckled": ["dapple", "speckle", "spot", "speck", "freckle"],
    "Bengal": ["dapple", "speckle", "spots", "speck", "freckle"],
    "Tortie": ["dapple", "speckle", "spot", "dapple"],
    "Rosette": ["dapple", "speckle", "spots", "dapple", "freckle"],
    "Calico": ["stripe", "dapple", "patch", "patch"],
    "Smoke": ["fade", "dusk", "dawn", "smoke"],
    "Ticked": ["spots", "pelt", "speckle", "freckle"],
    "Mackerel": ["stripe", "feather", "leaf", "stripe", "fern"],
    "Classic": ["stripe", "feather", "leaf", "stripe", "fern"],
    "Sokoke": ["stripe", "feather", "leaf", "stripe", "fern"],
    "Agouti": ["back", "pelt", "fur"],
    "Singlestripe": ["stripe", "streak", "back", "shade", "stem", "shadow"]
}

tortie_pelt_suffixes = {
    "solid": ["dapple", "speckle", "spots", "splash"],
    "tabby": ["stripe", "feather", "leaf", "stripe", "shade", "fern"],
    "bengal": ["dapple", "speckle", "spots", "speck", "fern", "freckle"],
    "marbled": ["stripe", "feather", "leaf", "stripe", "shade", "fern"],
    "ticked": ["spots", "pelt", "speckle", "freckle"],
    "smoke": ["fade", "dusk", "dawn", "smoke"],
    "rosette": ["dapple", "speckle", "spots", "dapple", "fern", "freckle"],
    "speckled": ["dapple", "speckle", "spot", "speck", "freckle"],
    "mackerel": ["stripe", "feather", "fern", "shade"],
    "classic": ["stripe", "feather", "fern"],
    "sokoke": ["stripe", "feather", "fern", "shade", "dapple"],
    "agouti": ["back", "pelt", "fur", "dapple", "splash"]
}

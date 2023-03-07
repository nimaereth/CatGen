"""Contains important dictionaries and lists for handling cat attributes"""

# Gender lists
sex = ["male", "female"]
gender = ["male", "female", "nonbinary"]

# Age range dictionary, 150+ ages handled by a method within the Cat class
age_ranges = {"kitten": (0, 5),
              "adolescent": (6, 11),
              "young adult": (12, 47),
              "adult": (48, 95),
              "senior adult": (96, 119),
              "elder": (120, 150)}

# Status dictionary, split by age
statuses = {"kit": ["kitten"],
            "adolescent": ["apprentice", "medicine cat apprentice", "mediator apprentice"],
            "adult": ["warrior", "mediator", "medicine cat", "deputy", "leader"],
            "elder": ["elder", "medicine cat", "mediator"]}

# Backstory list
backstories = ["clanborn", "halfclan1", "halfclan2", "outsider_roots1", "outsider_roots2", "loner1", "loner2",
               "kittypet1", "kittypet2", "rogue1", "rogue2", "abandoned1", "abandoned2", "abandoned3", "medicine_cat",
               "otherclan", "otherclan2", "ostracized_warrior", "disgraced", "retired_leader", "refugee",
               "tragedy_survivor", "clan_founder", "orphaned", "orphaned2", "guided1", "guided2", "guided3", "guided4"]

# Trait dictionaries, split between kit/nonkit
traits = {"kit": ["attention-seeker", "bossy", "bouncy", "bullying", "charming", "daring", "daydreamer", "impulsive",
                  "inquisitive", "insecure", "nervous", "noisy", "polite", "quiet", "sweet", "troublesome"],
          "nonkit": ["adventurous", "altruistic", "ambitious", "bloodthirsty", "bold", "calm", "careful", "charismatic",
                     "childish", "cold", "compassionate", "confident", "daring", "empathetic", "faithful", "fierce",
                     "insecure", "lonesome", "loving", "loyal", "nervous", "patient", "playful", "responsible",
                     "righteous", "shameless", "sneaky", "strange", "strict", "thoughtful", "troublesome", "vengeful",
                     "wise"]}

# Skill dictionaries, split between normal/med/elder skills and unknown skill
skills = {"standard": ["good hunter", "great hunter", "fantastic hunter", "smart", "very smart", "extremely smart",
                       "good fighter", "great fighter", "excellent fighter", "good speaker", "great speaker",
                       "excellent speaker", "strong connection to StarClan", "good teacher", "great teacher",
                       "fantastic teacher"],
          "med": ["good healer", "great healer", "fantastic healer", "omen sight", "dream walker",
                  "strong connection to StarClan", "lore keeper", "good teacher", "great teacher", "fantastic teacher",
                  "keen eye", "smart", "very smart", "extremely smart", "good mediator", "great mediator",
                  "excellent mediator", "clairvoyant", "prophet"],
          "elder": ["good storyteller", "great storyteller", "fantastic storyteller", "smart tactician",
                    "valuable tactician", "valuable insight", "good mediator", "great mediator", "excellent mediator",
                    "good teacher", "great teacher", "fantastic teacher", "strong connection to StarClan", "smart",
                    "very smart", "extremely smart", "good kitsitter", "great kitsitter", "excellent kitsitter",
                    "camp keeper", "den builder"],
          "unknown": ["???"]}

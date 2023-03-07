class Generator:
    """Generator class holding all screens as well as the generated cat"""

    def __init__(self, current_screen="menu screen", cat=None):
        """
        Initialise generator variables

        :param string current_screen: name of the currently active screen
        :param scripts.cat.Cat cat: the cat object to be updated/generated
        """
        # Record previous and current screen
        self.previous_screen = None
        self.current_screen = current_screen

        # Used to flag screen switching
        self.change_screen_flag = False

        # Dict of all screens
        self.all_screens = {}

        # Cat associated with the generator
        self.cat = cat

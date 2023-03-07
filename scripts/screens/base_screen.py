class Screen:
    """Base class for creating screens"""

    def __init__(self, name, generator, window, uimanager):
        """
        Initialise the screen variables

        :param name: screen name
        :param generator: the generator object the screen belongs to
        :param window: pygame display surface that the screen is drawn on
        :param uimanager: pygame_gui uimanager for handling the screen's ui elements
        """
        # Screen name
        self.name = name

        # Add screen to generator's screens
        self.generator = generator
        self.generator.all_screens[name] = self

        # Assign window and ui manager
        self.window = window
        self.uimanager = uimanager

    def change_screen(self, new_screen):
        """
        Called when changing to a different screen

        :param new_screen: name of the screen being switched to
        """
        # Update generator's screens
        self.generator.previous_screen = self.generator.current_screen
        self.generator.current_screen = new_screen

        # Flag the screen change
        self.generator.change_screen_flag = True

    def on_use(self):
        """
        Called while the screen is being used

        """
        pass

    def open_screen(self):
        """
        Called when the screen is opened

        """
        pass

    def handle_event(self, event):
        """
        Called when an event occurs on the screen

        :param event: the pygame event to process
        """
        pass

    def exit_screen(self):
        """
        Called when the screen is exited

        """
        pass

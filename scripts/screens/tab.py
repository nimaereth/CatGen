class Tab:
    """Base class for UI tabs"""

    def __init__(self, container=None, image=None, tab_button=None):
        """
        Initialise the tab variables

        :param container: ui container to hold tab UI elements
        :param image: ui image to display as the tab's background
        :param tab_button: ui button for selecting the tab
        """
        # Container, background image, tab_button
        self.container = container
        self.image = image
        self.tab_button = tab_button

        # Dicts to contain tab components
        self.buttons = {}
        self.textboxes = {}
        self.dropdowns = {}

    def show(self):
        """
        Show tab contents; use when tab is switched to

        """
        # Show whole container
        self.container.show()

        # Disable tab button
        self.tab_button.disable()

    def hide(self):
        """
        Hide tab contents; use when tab is switched from

        """
        # Hide whole container
        self.container.hide()

        # Enable tab button
        self.tab_button.enable()

    def kill(self):
        """
        Kill tab contents and tab button; use when tab is no longer needed

        """
        # Kill tab
        self.container.kill()
        self.tab_button.kill()

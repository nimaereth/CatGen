import pygame
from pygame_gui import UI_BUTTON_START_PRESS
from pygame_gui.elements import UIButton
from scripts.screens.base_screen import Screen


class MenuScreen(Screen):
    """Screen subclass to define the main menu screen"""

    def __init__(self, name, generator, window, uimanager):
        """
        Initialise the menu screen variables, including UI elements

        :param name: screen name
        :param generator: the generator object the screen belongs to
        :param window: pygame display surface that the screen is drawn on
        :param uimanager: pygame_gui uimanager for handling the screen's ui elements
        """
        super().__init__(name, generator, window, uimanager)

        # Main menu buttons
        self.create_button = None
        self.load_button = None
        self.quit_button = None

        # Background image
        self.menu_bg = pygame.image.load("resources/images/menu.png").convert_alpha()

    def on_use(self):
        # Draw background
        self.window.blit(self.menu_bg, (0, 0))

    def open_screen(self):
        # Draw buttons
        self.create_button = UIButton(relative_rect=(140, 350), text="Create cat", manager=self.uimanager)
        self.load_button = UIButton(relative_rect=(140, 400), text="Load cat", manager=self.uimanager)
        self.quit_button = UIButton(relative_rect=(140, 450), text="Quit", manager=self.uimanager)

        # Disable load button due to not being implemented
        self.load_button.disable()

    def handle_event(self, event):
        # Handle button events
        if event.type == UI_BUTTON_START_PRESS:
            if event.ui_element == self.create_button:  # switch to creation screen
                self.change_screen("create screen")
                self.exit_screen()
            elif event.ui_element == self.load_button:  # switch to load screen
                pass
            elif event.ui_element == self.quit_button:  # quit program
                pygame.display.quit()
                pygame.quit()
                exit()

    def exit_screen(self):
        # Kill buttons
        self.create_button.kill()
        self.load_button.kill()
        self.quit_button.kill()

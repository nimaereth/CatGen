"""Important components (window, generator, ui manager, screens, cat, etc. ) kept here"""

import pygame
import pygame_gui
from scripts.generator import Generator
from scripts.screens.menu_screen import MenuScreen
from scripts.screens.create_screen import CreateScreen

# Pygame setup
pygame.init()
pygame.display.set_caption("Cat Generator")
WINDOW = pygame.display.set_mode((800, 700))

# Pygame_gui manager setup
MANAGER = pygame_gui.ui_manager.UIManager((800, 700), "resources/theming/defaults.json")
MANAGER.add_font_paths(
    font_name="notosans",
    regular_path="resources/fonts/NotoSans-Medium.ttf",
    bold_path="resources/fonts/NotoSans-ExtraBold.ttf",
    italic_path="resources/fonts/NotoSans-MediumItalic.ttf",
    bold_italic_path="resources/fonts/NotoSans-ExtraBoldItalic.ttf"
)
MANAGER.preload_fonts([
    {"name": "notosans", "point_size": 30, "style": "regular"},
    {"name": "notosans", "point_size": 30, "style": "bold"},
    {"name": "notosans", "point_size": 30, "style": "italic"},
    {"name": "notosans", "point_size": 30, "style": "bold_italic"},
    {"name": "notosans", "point_size": 32, "style": "regular"},
    {"name": "notosans", "point_size": 32, "style": "bold"},
    {"name": "notosans", "point_size": 32, "style": "italic"},
    {"name": "notosans", "point_size": 32, "style": "bold_italic"}
])
MANAGER.get_theme().load_theme("resources/theming/defaults.json")
MANAGER.get_theme().load_theme('resources/theming/buttons.json')
MANAGER.get_theme().load_theme('resources/theming/textboxes.json')
MANAGER.get_theme().load_theme('resources/theming/dropdowns.json')
MANAGER.get_theme().load_theme('resources/theming/labels.json')

# Generator setup
GENERATOR = Generator("menu screen")

# Cat setup
from scripts.cat import Cat  # called here to avoid circular import
CAT = Cat()
GENERATOR.cat = CAT  # assign to generator

# Screens setup
MENU = MenuScreen("menu screen", GENERATOR, WINDOW, MANAGER)
CREATION = CreateScreen("create screen", GENERATOR, WINDOW, MANAGER)

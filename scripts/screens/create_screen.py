import dicts.catdicts as catdicts
from pygame_gui.core import UIContainer
from pygame_gui.elements import UIButton, UIImage, UITextEntryLine, UIDropDownMenu, UITextBox, UILabel
from pygame_gui import UI_BUTTON_START_PRESS, UI_TEXT_ENTRY_CHANGED, UI_DROP_DOWN_MENU_CHANGED
from scripts.screens.base_screen import Screen
from scripts.screens.tab import Tab
from scripts.utility import *


class CreateScreen(Screen):
    """Screen subclass to define the cat creation screen"""

    def __init__(self, name, generator, window, uimanager):
        """
        Initialise the cat creation screen variables, including UI elements

        :param name: screen name
        :param generator: the generator object the screen belongs to
        :param window: pygame display surface that the screen is drawn on
        :param uimanager: pygame_gui uimanager for handling the screen's ui elements
        """
        super().__init__(name, generator, window, uimanager)

        # Image loading
        self.images = {"general": pygame.image.load("resources/images/general.png").convert_alpha(),
                       "appearance": pygame.image.load("resources/images/appearance.png").convert_alpha(),
                       "extras": pygame.image.load("resources/images/extras.png").convert_alpha(),
                       "save": pygame.image.load("resources/images/save.png").convert_alpha()}

        # UI elements
        # -- main --
        self.back_button = None
        self.previous_pose_button = None
        self.next_pose_button = None
        self.sprite1_button = None
        self.sprite2_button = None
        self.sprite3_button = None
        self.sprite4_button = None
        self.reset_button = None
        self.randomise_button = None
        self.id_textbox = None
        self.cat_lock = None
        self.cat_lock_label = None
        self.info_lock = None
        self.info_lock_label = None
        self.cat_is_locked = False
        self.info_is_locked = False

        # -- tabs --
        # -- general --
        self.general_tab = Tab()
        self.general_tab.textboxes.update({"name prefix": None,
                                           "name suffix": None,
                                           "moons": None})
        self.general_tab.dropdowns.update({"gender": None,
                                           "gender align": None,
                                           "status": None,
                                           "backstory": None,
                                           "trait": None,
                                           "skill": None})

        # -- apearance --
        self.appearance_tab = Tab()
        self.appearance_tab.dropdowns.update({"pelt length": None})
        self.appearance_tab.buttons.update({"previous pelt": None,
                                            "next pelt": None,
                                            "previous pattern": None,
                                            "next pattern": None,
                                            "previous white patch": None,
                                            "next white patch": None,
                                            "tortie toggle": None,
                                            "previous tortie patch": None,
                                            "next tortie patch": None,
                                            "previous tortie pattern": None,
                                            "next tortie pattern": None,
                                            "previous tortie colour": None,
                                            "next tortie colour": None,
                                            "previous skin": None,
                                            "next skin": None,
                                            "heterochromia toggle": None,
                                            "previous eye1": None,
                                            "next eye1": None,
                                            "previous eye2": None,
                                            "next eye2": None,
                                            "previous tint": None,
                                            "next tint": None
                                            })

        # -- extras --
        self.extras_tab = Tab()
        self.extras_tab.dropdowns.update({"accessory type": None,
                                          "scar 1": None,
                                          "scar 2": None,
                                          "scar 3": None,
                                          "scar 4": None,
                                          "platform biome": None})
        self.extras_tab.buttons.update({"reverse toggle": None,
                                        "previous accessory": None,
                                        "next accessory": None,
                                        "shading": None,
                                        "previous platform": None,
                                        "next platform": None,
                                        "previous white tint": None,
                                        "next white tint": None})

        # -- save --
        self.save_tab = Tab()
        self.save_tab.textboxes.update({"json preview": None})
        self.save_tab.dropdowns.update({"scale": None})
        self.save_tab.buttons.update({"export": None,
                                      "save sprites": None})

        self.current_tab = None  # currently selected tab

    def on_use(self):
        # Draw platform
        self.window.blit(self.generator.cat.platform_sprite(), (280, 95))

        # Draw cat
        self.window.blit(self.generator.cat.big_sprite(), (325, 95))
        self.window.blit(self.generator.cat.small_sprites(), (300, 275))

    def open_screen(self):
        # Build containers
        self.build_containers()

        # Build all ui elements
        self.build_textboxes()
        self.build_dropdowns()
        self.build_buttons()

    def handle_event(self, event):
        # Handle events for buttons
        if event.type == UI_BUTTON_START_PRESS:
            # Handle tab switching
            for tab in [self.general_tab, self.appearance_tab, self.extras_tab, self.save_tab]:
                if event.ui_element == tab.tab_button:
                    # Hide current tab
                    self.current_tab.hide()

                    # Change current tab and show it
                    self.current_tab = tab
                    tab.show()

                    # Special case for save tab to update json preview when tab is opened to avoid alternative of
                    # updating every time the cat is changed
                    if tab == self.save_tab:
                        self.save_tab.textboxes["json preview"].set_text("json preview:\n" +
                                                                         self.generator.cat.preview_json())

            # Handle main UI buttons
            if event.ui_element == self.reset_button:  # resetting based on info/cat locking
                if self.info_is_locked and not self.cat_is_locked:
                    self.generator.cat.reset_appearance()
                elif self.cat_is_locked and not self.info_is_locked:
                    self.generator.cat.reset_info()
                elif not self.cat_is_locked and not self.info_is_locked:
                    self.generator.cat.reset_all()

                # Update/rebuild UI elements if necessary
                if not(self.info_is_locked and self.cat_is_locked):
                    self.update_textboxes()
                    self.update_dropdowns()
                    self.update_buttons()

            elif event.ui_element == self.randomise_button:  # randomising based on info/cat locking
                if self.info_is_locked and not self.cat_is_locked:
                    self.generator.cat.randomise_appearance()
                elif self.cat_is_locked and not self.info_is_locked:
                    self.generator.cat.randomise_info()
                elif not self.cat_is_locked and not self.info_is_locked:
                    self.generator.cat.randomise_all()

                # Update/rebuild necessary UI elements
                if not(self.info_is_locked and self.cat_is_locked):
                    self.update_textboxes()
                    self.update_dropdowns()
                    self.update_buttons()

            elif event.ui_element == self.back_button:  # go back to main menu
                self.change_screen("menu screen")

            elif event.ui_element == self.info_lock:
                self.info_is_locked = not self.info_is_locked  # toggle lock
                self.info_lock.kill()
                if self.info_is_locked:
                    print("Cat info has been locked")
                    self.info_lock = UIButton(pygame.Rect((680, 20), (18, 18)), "", self.uimanager,
                                              object_id="#locked_button")
                else:
                    print("Cat info has been unlocked")
                    self.info_lock = UIButton(pygame.Rect((680, 20), (18, 18)), "", self.uimanager,
                                              object_id="#unlocked_button")

            elif event.ui_element == self.cat_lock:
                self.cat_is_locked = not self.cat_is_locked  # toggle lock
                self.cat_lock.kill()
                if self.cat_is_locked:
                    print("Cat appearance has been locked")
                    self.cat_lock = UIButton(pygame.Rect((755, 20), (18, 18)), "", self.uimanager,
                                             object_id="#locked_button")
                else:
                    print("Cat appearance has been unlocked")
                    self.cat_lock = UIButton(pygame.Rect((755, 20), (18, 18)), "", self.uimanager,
                                             object_id="#unlocked_button")

            elif event.ui_element in [self.previous_pose_button, self.next_pose_button, self.sprite1_button,
                                      self.sprite2_button, self.sprite3_button, self.sprite4_button]:
                event.ui_element.run(self.generator.cat)

            elif event.ui_element in self.appearance_tab.buttons.values():  # appearance tab buttons
                event.ui_element.run(self.generator.cat)
                if event.ui_element == self.appearance_tab.buttons["tortie toggle"]:  # tortie handling
                    self.appearance_tab.buttons["tortie toggle"].kill()
                    if self.generator.cat.tortie:
                        self.appearance_tab.buttons["previous tortie patch"].enable()
                        self.appearance_tab.buttons["next tortie patch"].enable()
                        self.appearance_tab.buttons["previous tortie pattern"].enable()
                        self.appearance_tab.buttons["next tortie pattern"].enable()
                        self.appearance_tab.buttons["previous tortie colour"].enable()
                        self.appearance_tab.buttons["next tortie colour"].enable()
                        self.appearance_tab.buttons["tortie toggle"] = UICatButton((95, 155), (34, 34),
                                                                                   self.uimanager,
                                                                                   "#checked_checkbox",
                                                                                   self.appearance_tab.container,
                                                                                   True, toggle_tortie)
                    else:
                        self.appearance_tab.buttons["previous tortie patch"].disable()
                        self.appearance_tab.buttons["next tortie patch"].disable()
                        self.appearance_tab.buttons["previous tortie pattern"].disable()
                        self.appearance_tab.buttons["next tortie pattern"].disable()
                        self.appearance_tab.buttons["previous tortie colour"].disable()
                        self.appearance_tab.buttons["next tortie colour"].disable()
                        self.appearance_tab.buttons["tortie toggle"] = UICatButton((95, 155), (34, 34),
                                                                                   self.uimanager,
                                                                                   "#unchecked_checkbox",
                                                                                   self.appearance_tab.container,
                                                                                   True, toggle_tortie)

                elif event.ui_element == self.appearance_tab.buttons["heterochromia toggle"]:  # heterochromia handling
                    self.appearance_tab.buttons["heterochromia toggle"].kill()
                    if self.generator.cat.heterochromia:
                        self.appearance_tab.buttons["previous eye2"].enable()
                        self.appearance_tab.buttons["next eye2"].enable()
                        self.appearance_tab.buttons["heterochromia toggle"] = UICatButton((580, 75), (34, 34),
                                                                                          self.uimanager,
                                                                                          "#checked_checkbox",
                                                                                          self.appearance_tab.
                                                                                          container,
                                                                                          True,
                                                                                          toggle_heterochromia)
                    else:
                        self.appearance_tab.buttons["previous eye2"].disable()
                        self.appearance_tab.buttons["next eye2"].disable()
                        self.appearance_tab.buttons["heterochromia toggle"] = UICatButton((580, 75), (34, 34),
                                                                                          self.uimanager,
                                                                                          "#unchecked_checkbox",
                                                                                          self.appearance_tab.
                                                                                          container,
                                                                                          True,
                                                                                          toggle_heterochromia)

            elif event.ui_element in self.extras_tab.buttons.values():  # extras tab buttons
                event.ui_element.run(self.generator.cat)
                if event.ui_element == self.extras_tab.buttons["reverse toggle"]:  # reverse handling
                    self.extras_tab.buttons["reverse toggle"].kill()
                    if self.generator.cat.reverse:
                        self.extras_tab.buttons["reverse toggle"] = UICatButton((525, 20), (34, 34), self.uimanager,
                                                                                "#checked_checkbox",
                                                                                self.extras_tab.container, True,
                                                                                reverse_cat)
                    else:
                        self.extras_tab.buttons["reverse toggle"] = UICatButton((525, 20), (34, 34), self.uimanager,
                                                                                "#unchecked_checkbox",
                                                                                self.extras_tab.container, True,
                                                                                reverse_cat)

                elif event.ui_element == self.extras_tab.buttons["shading toggle"]:  # shading handling
                    self.extras_tab.buttons["shading toggle"].kill()
                    if self.generator.cat.shading:
                        self.extras_tab.buttons["shading toggle"] = UICatButton((680, 20), (34, 34), self.uimanager,
                                                                                "#checked_checkbox",
                                                                                self.extras_tab.container, True,
                                                                                shade_cat)
                    else:
                        self.extras_tab.buttons["shading toggle"] = UICatButton((680, 20), (34, 34), self.uimanager,
                                                                                "#unchecked_checkbox",
                                                                                self.extras_tab.container, True,
                                                                                shade_cat)

            elif event.ui_element == self.save_tab.buttons["export"]:  # export cat
                self.generator.cat.save_json()
                print("Cat successfully exported!")
            elif event.ui_element == self.save_tab.buttons["save sprites"]:  # save cat sprites
                self.generator.cat.save_sprites(self.save_tab.dropdowns['scale'].selected_option)
                print("Sprites successfully saved!")

        # Handle events for textboxes
        elif event.type == UI_TEXT_ENTRY_CHANGED:
            if event.ui_element == self.id_textbox:
                self.generator.cat.ID = self.id_textbox.get_text()

                # Update json textbox as ID may be edited while on save tab
                self.save_tab.textboxes["json preview"].set_text("json preview:\n" +
                                                                 self.generator.cat.preview_json())

            elif event.ui_element == self.general_tab.textboxes["name prefix"]:
                self.generator.cat.prefix = self.general_tab.textboxes["name prefix"].get_text()

            elif event.ui_element == self.general_tab.textboxes["name suffix"]:
                self.generator.cat.suffix = self.general_tab.textboxes["name suffix"].get_text()

            elif event.ui_element == self.general_tab.textboxes["moons"]:
                if self.general_tab.textboxes["moons"].get_text() != "":
                    self.generator.cat.moons = int(self.general_tab.textboxes["moons"].get_text())
                else:
                    self.generator.cat.moons = 0  # set as kit if moons is empty
                self.generator.cat.update_age()

                # Update dropdowns for status, skill, trait based on age
                self.switch_statusset()
                self.switch_skillset("age")
                self.switch_traitset()

        # Handle events for dropdowns
        elif event.type == UI_DROP_DOWN_MENU_CHANGED:
            if event.ui_element == self.general_tab.dropdowns["gender"]:
                self.generator.cat.sex = self.general_tab.dropdowns["gender"].selected_option
            elif event.ui_element == self.general_tab.dropdowns["gender align"]:
                self.generator.cat.gender = self.general_tab.dropdowns["gender align"].selected_option
            elif event.ui_element == self.general_tab.dropdowns["backstory"]:
                self.generator.cat.backstory = self.general_tab.dropdowns["backstory"].selected_option
            elif event.ui_element == self.general_tab.dropdowns["trait"]:
                self.generator.cat.stored_traits[self.generator.cat.trait] = self.general_tab.dropdowns["trait"]. \
                    selected_option
            elif event.ui_element == self.general_tab.dropdowns["status"]:
                self.generator.cat.stored_statuses[self.generator.cat.status] = self.general_tab.dropdowns["status"]. \
                    selected_option
                self.switch_skillset("status")
            elif event.ui_element == self.general_tab.dropdowns["skill"]:
                self.generator.cat.stored_skills[self.generator.cat.skill] = self.general_tab.dropdowns["skill"]. \
                    selected_option
            elif event.ui_element == self.extras_tab.dropdowns["accessory type"]:
                self.generator.cat.accessory = self.extras_tab.dropdowns["accessory type"].selected_option
                # Disable accessory buttons if none
                if self.generator.cat.accessory == "none":
                    self.extras_tab.buttons["previous accessory"].disable()
                    self.extras_tab.buttons["next accessory"].disable()
                else:
                    self.extras_tab.buttons["previous accessory"].enable()
                    self.extras_tab.buttons["next accessory"].enable()
            elif event.ui_element == self.extras_tab.dropdowns["scar 1"]:
                self.generator.cat.scars[0] = self.extras_tab.dropdowns["scar 1"].selected_option
            elif event.ui_element == self.extras_tab.dropdowns["scar 2"]:
                self.generator.cat.scars[1] = self.extras_tab.dropdowns["scar 2"].selected_option
            elif event.ui_element == self.extras_tab.dropdowns["scar 3"]:
                self.generator.cat.scars[2] = self.extras_tab.dropdowns["scar 3"].selected_option
            elif event.ui_element == self.extras_tab.dropdowns["scar 4"]:
                self.generator.cat.scars[3] = self.extras_tab.dropdowns["scar 4"].selected_option
            elif event.ui_element == self.extras_tab.dropdowns["platform biome"]:
                self.generator.cat.platform = self.extras_tab.dropdowns["platform biome"].selected_option
                if self.generator.cat.platform == "none":  # Disable platform buttons if none
                    self.extras_tab.buttons["previous platform"].disable()
                    self.extras_tab.buttons["next platform"].disable()
                else:
                    self.extras_tab.buttons["previous platform"].enable()
                    self.extras_tab.buttons["next platform"].enable()
            elif event.ui_element == self.appearance_tab.dropdowns["pelt length"]:
                self.generator.cat.pelt_length = self.appearance_tab.dropdowns["pelt length"].selected_option

                # Update cat lineart to match pelt length
                if self.generator.cat.active_pose == "adult" and self.generator.cat.pelt_length == "long":
                    self.generator.cat.active_pose = "adult longhair"
                elif self.generator.cat.active_pose == "adult longhair" and self.generator.cat.pelt_length != "long":
                    self.generator.cat.active_pose = "adult"

    def exit_screen(self):
        # Kill buttons
        self.back_button.kill()
        self.previous_pose_button.kill()
        self.next_pose_button.kill()
        self.sprite1_button.kill()
        self.sprite2_button.kill()
        self.sprite3_button.kill()
        self.sprite4_button.kill()
        self.id_textbox.kill()
        self.reset_button.kill()
        self.randomise_button.kill()
        self.info_lock_label.kill()
        self.cat_lock_label.kill()
        self.cat_lock.kill()
        self.info_lock.kill()

        # Reset lock conditions
        self.cat_is_locked = False
        self.info_is_locked = False

        # Kill tabs
        self.general_tab.kill()
        self.appearance_tab.kill()
        self.extras_tab.kill()
        self.save_tab.kill()

        # Reset cat
        self.generator.cat.reset_all()

    def build_containers(self):
        """For building containers (not their contents), for use when opening the screen"""

        # General tab
        self.general_tab.container = UIContainer(relative_rect=pygame.Rect((20, 428), (760, 258)),
                                                 manager=self.uimanager,
                                                 visible=True)
        self.general_tab.image = UIImage(relative_rect=pygame.Rect((0, 0), (760, 258)),
                                         image_surface=self.images["general"],
                                         manager=self.uimanager,
                                         container=self.general_tab.container)
        self.general_tab.image.disable()
        self.general_tab.tab_button = UIButton(relative_rect=pygame.Rect((33, 393), (137, 35)),
                                               text="",
                                               manager=self.uimanager,
                                               object_id="#general_tab")
        self.general_tab.tab_button.disable()
        self.current_tab = self.general_tab  # set current tab to general tab

        # Appearance tab
        self.appearance_tab.container = UIContainer(relative_rect=pygame.Rect((20, 428), (760, 258)),
                                                    manager=self.uimanager,
                                                    visible=False)
        self.appearance_tab.image = UIImage(relative_rect=pygame.Rect((0, 0), (760, 258)),
                                            image_surface=self.images["appearance"],
                                            manager=self.uimanager,
                                            container=self.appearance_tab.container)
        self.appearance_tab.image.disable()
        self.appearance_tab.tab_button = UIButton(relative_rect=pygame.Rect((179, 393), (137, 35)),
                                                  text="",
                                                  manager=self.uimanager,
                                                  object_id="#appearance_tab")

        # Extras tab
        self.extras_tab.container = UIContainer(relative_rect=pygame.Rect((20, 428), (760, 258)),
                                                manager=self.uimanager,
                                                visible=False)
        self.extras_tab.image = UIImage(relative_rect=pygame.Rect((0, 0), (760, 258)),
                                        image_surface=self.images["extras"],
                                        manager=self.uimanager,
                                        container=self.extras_tab.container)
        self.extras_tab.image.disable()
        self.extras_tab.tab_button = UIButton(relative_rect=pygame.Rect((325, 393), (137, 35)),
                                              text="",
                                              manager=self.uimanager,
                                              object_id="#extras_tab")

        # Export tab
        self.save_tab.container = UIContainer(relative_rect=pygame.Rect((20, 428), (760, 258)),
                                              manager=self.uimanager,
                                              visible=False)
        self.save_tab.img = UIImage(relative_rect=pygame.Rect((0, 0), (760, 258)),
                                    image_surface=self.images["save"],
                                    manager=self.uimanager,
                                    container=self.save_tab.container)
        self.save_tab.img.disable()
        self.save_tab.tab_button = UIButton(relative_rect=pygame.Rect((623, 393), (137, 35)),
                                            text="",
                                            manager=self.uimanager,
                                            object_id="#export_tab")

    def build_textboxes(self):
        """Build all textboxes/labels, for use when opening the screen"""

        # -- main --
        self.id_textbox = UITextEntryLine(relative_rect=pygame.Rect((375, 45), (50, 30)),
                                          manager=self.uimanager,
                                          object_id="text_entry_line",
                                          placeholder_text="ID")
        self.id_textbox.set_allowed_characters("numbers")
        self.id_textbox.set_text_length_limit(3)
        self.info_lock_label = UILabel(pygame.Rect((650, 20), (27, 23)), "info", object_id="label")
        self.cat_lock_label = UILabel(pygame.Rect((725, 20), (27, 23)), "cat", object_id="label")

        # -- general --
        self.general_tab.textboxes["name prefix"] = UITextEntryLine(relative_rect=pygame.Rect((120, 27), (100, 30)),
                                                                    manager=self.uimanager,
                                                                    container=self.general_tab.container,
                                                                    placeholder_text="prefix",
                                                                    object_id="#text_entry_line")
        self.general_tab.textboxes["name suffix"] = UITextEntryLine(relative_rect=pygame.Rect((225, 27), (100, 30)),
                                                                    manager=self.uimanager,
                                                                    container=self.general_tab.container,
                                                                    placeholder_text="suffix",
                                                                    object_id="#text_entry_line")
        self.general_tab.textboxes["moons"] = UITextEntryLine(relative_rect=pygame.Rect((120, 77), (100, 30)),
                                                              manager=self.uimanager,
                                                              container=self.general_tab.container,
                                                              placeholder_text="moons",
                                                              object_id="#text_entry_line")
        self.general_tab.textboxes["moons"].set_allowed_characters("numbers")

        # -- save --
        self.save_tab.textboxes["json preview"] = UITextBox(html_text="json preview:\n" +
                                                                      self.generator.cat.preview_json(),
                                                            relative_rect=pygame.Rect((25, 20), (450, 218)),
                                                            manager=self.uimanager, container=self.save_tab.container,
                                                            object_id="#json_box")

    def update_textboxes(self):
        """Update text within textboxes to match cat's attributes, for use when resetting/randomising cat"""

        # -- main --
        self.id_textbox.set_text(self.generator.cat.ID)

        # -- general --
        self.general_tab.textboxes["name prefix"].set_text(self.generator.cat.prefix)
        self.general_tab.textboxes["name suffix"].set_text(self.generator.cat.suffix)
        self.general_tab.textboxes["moons"].set_text(str(self.generator.cat.moons))

        # -- save --
        self.save_tab.textboxes["json preview"].set_text("json preview:\n" + self.generator.cat.preview_json())

    def build_dropdowns(self):
        """Build all dropdown menus, for use when opening the screens"""

        # -- general --
        self.general_tab.dropdowns["gender"] = UIDropDownMenu(options_list=catdicts.sex,
                                                              starting_option=self.generator.cat.sex,
                                                              relative_rect=pygame.Rect((120, 145), (150, 30)),
                                                              manager=self.uimanager,
                                                              container=self.general_tab.container,
                                                              object_id="drop_down_menu")
        self.general_tab.dropdowns["gender align"] = UIDropDownMenu(options_list=catdicts.gender,
                                                                    starting_option=self.generator.cat.gender,
                                                                    relative_rect=pygame.Rect((120, 195), (150, 30)),
                                                                    manager=self.uimanager,
                                                                    container=self.general_tab.container,
                                                                    object_id="drop_up_menu")

        self.general_tab.dropdowns["status"] = UIDropDownMenu(options_list=catdicts.statuses[self.generator.cat.status],
                                                              starting_option=self.generator.cat.stored_statuses[
                                                                  self.generator.cat.status],
                                                              relative_rect=pygame.Rect((500, 27), (220, 30)),
                                                              manager=self.uimanager,
                                                              container=self.general_tab.container,
                                                              object_id="drop_down_menu")

        self.general_tab.dropdowns["backstory"] = UIDropDownMenu(options_list=catdicts.backstories,
                                                                 starting_option=self.generator.cat.backstory,
                                                                 relative_rect=pygame.Rect((500, 77), (220, 30)),
                                                                 manager=self.uimanager,
                                                                 container=self.general_tab.container,
                                                                 object_id="drop_down_menu")

        self.general_tab.dropdowns["trait"] = UIDropDownMenu(options_list=catdicts.traits[self.generator.cat.trait],
                                                             starting_option=self.generator.cat.stored_traits[
                                                                 self.generator.cat.trait],
                                                             relative_rect=pygame.Rect((500, 145), (220, 30)),
                                                             manager=self.uimanager,
                                                             container=self.general_tab.container,
                                                             object_id="drop_up_menu")

        self.general_tab.dropdowns["skill"] = UIDropDownMenu(options_list=catdicts.skills[self.generator.cat.skill],
                                                             starting_option=self.generator.cat.stored_skills[
                                                                 self.generator.cat.skill],
                                                             relative_rect=pygame.Rect((500, 195), (220, 30)),
                                                             manager=self.uimanager,
                                                             container=self.general_tab.container,
                                                             object_id="drop_up_menu")

        # -- appearance --
        self.appearance_tab.dropdowns["pelt length"] = UIDropDownMenu(options_list=spritedicts.pelt_lengths,
                                                                      starting_option=self.generator.cat.pelt_length,
                                                                      relative_rect=pygame.Rect((560, 22),
                                                                                                (150, 30)),
                                                                      manager=self.uimanager,
                                                                      container=self.appearance_tab.container,
                                                                      object_id="drop_down_menu")

        # -- extras --
        self.extras_tab.dropdowns["accessory type"] = UIDropDownMenu(list(spritedicts.accessories.keys()),
                                                                     self.generator.cat.accessory,
                                                                     pygame.Rect((180, 23), (100, 30)),
                                                                     self.uimanager,
                                                                     self.extras_tab.container)

        self.extras_tab.dropdowns["scar 1"] = UIDropDownMenu(spritedicts.scars,
                                                             self.generator.cat.scars[0],
                                                             pygame.Rect((100, 155), (150, 30)),
                                                             self.uimanager,
                                                             self.extras_tab.container,
                                                             object_id="drop_up_menu")
        self.extras_tab.dropdowns["scar 2"] = UIDropDownMenu(spritedicts.scars,
                                                             self.generator.cat.scars[1],
                                                             pygame.Rect((270, 155), (150, 30)),
                                                             self.uimanager,
                                                             self.extras_tab.container,
                                                             object_id="drop_up_menu")
        self.extras_tab.dropdowns["scar 3"] = UIDropDownMenu(spritedicts.scars,
                                                             self.generator.cat.scars[2],
                                                             pygame.Rect((100, 200), (150, 30)),
                                                             self.uimanager,
                                                             self.extras_tab.container,
                                                             object_id="drop_up_menu")
        self.extras_tab.dropdowns["scar 4"] = UIDropDownMenu(spritedicts.scars,
                                                             self.generator.cat.scars[3],
                                                             pygame.Rect((270, 200), (150, 30)),
                                                             self.uimanager,
                                                             self.extras_tab.container,
                                                             object_id="drop_up_menu")

        self.extras_tab.dropdowns["platform biome"] = UIDropDownMenu(spritedicts.biomes,
                                                                     self.generator.cat.platform,
                                                                     pygame.Rect((595, 155), (130, 30)),
                                                                     self.uimanager,
                                                                     self.extras_tab.container,
                                                                     object_id="drop_up_menu")

        # -- save --
        self.save_tab.dropdowns["scale"] = UIDropDownMenu(["1x", "2x", "3x", "4x"], starting_option="1x",
                                                          relative_rect=pygame.Rect((600, 35), (80, 30)),
                                                          manager=self.uimanager, container=self.save_tab.container)

    def update_dropdowns(self):
        """Kill and rebuild all buttons to match cat, for use when randomising/resetting cat"""
        # Kill dropdowns
        for element in self.general_tab.dropdowns.values():
            element.kill()
        for element in self.appearance_tab.dropdowns.values():
            element.kill()
        for element in self.extras_tab.dropdowns.values():
            element.kill()
        for element in self.save_tab.dropdowns.values():
            element.kill()

        # Rebuild dropdowns
        self.build_dropdowns()

    def build_buttons(self):
        """Build all buttons, for use when opening the screen"""

        # -- main --
        self.back_button = UIButton(relative_rect=(20, 20), text="Back", manager=self.uimanager)
        self.reset_button = UIButton(pygame.Rect((740, 350), (34, 34)), "", self.uimanager, object_id="#reset_button")
        self.randomise_button = UIButton(pygame.Rect((700, 350), (34, 34)), "", self.uimanager,
                                         object_id="#random_dice_button", container=None)

        self.info_lock = UIButton(pygame.Rect((680, 20), (18, 18)), "", self.uimanager, object_id="#unlocked_button")
        self.cat_lock = UIButton(pygame.Rect((755, 20), (18, 18)), "", self.uimanager, object_id="#unlocked_button")

        self.previous_pose_button = UICatButton((250, 155), (38, 50), self.uimanager,
                                                "#left_button_fancy", None, True, update_pose, -1)
        self.next_pose_button = UICatButton((512, 155), (38, 50), self.uimanager,
                                            "#right_button_fancy", None, True, update_pose, 1)

        self.sprite1_button = UICatButton((300, 275), (50, 50), self.uimanager, "#image_button", None, 1,
                                          update_central_sprite, "kit")
        self.sprite2_button = UICatButton((350, 275), (50, 50), self.uimanager, "#image_button", None, 1,
                                          update_central_sprite, "adolescent")
        self.sprite3_button = UICatButton((400, 275), (50, 50), self.uimanager, "#image_button", None, 1,
                                          update_central_sprite, "adult")
        self.sprite4_button = UICatButton((450, 275), (50, 50), self.uimanager, "#image_button", None, 1,
                                          update_central_sprite, "elder")

        # -- appearance --
        self.appearance_tab.buttons["previous pelt"] = UICatButton((140, 22), (34, 34), self.uimanager,
                                                                   "#left_button",
                                                                   self.appearance_tab.container, True,
                                                                   update_pelt_colour, -1)
        self.appearance_tab.buttons["next pelt"] = UICatButton((180, 22), (34, 34), self.uimanager,
                                                               "#right_button", self.appearance_tab.container,
                                                               True, update_pelt_colour, 1)
        self.appearance_tab.buttons["previous pattern"] = UICatButton((325, 22), (34, 34), self.uimanager,
                                                                      "#left_button",
                                                                      self.appearance_tab.container, True,
                                                                      update_pelt_pattern, -1)
        self.appearance_tab.buttons["next pattern"] = UICatButton((365, 22), (34, 34), self.uimanager,
                                                                  "#right_button",
                                                                  self.appearance_tab.container, True,
                                                                  update_pelt_pattern, 1)
        self.appearance_tab.buttons["previous white patch"] = UICatButton((140, 75), (34, 34), self.uimanager,
                                                                          "#left_button",
                                                                          self.appearance_tab.container, True,
                                                                          update_white_patches, -1)
        self.appearance_tab.buttons["next white patch"] = UICatButton((180, 75), (34, 34), self.uimanager,
                                                                      "#right_button",
                                                                      self.appearance_tab.container, True,
                                                                      update_white_patches, 1)
        self.appearance_tab.buttons["previous tint button"] = UICatButton((325, 75), (34, 34), self.uimanager,
                                                                          "#left_button",
                                                                          self.appearance_tab.container, True,
                                                                          update_tint, -1)
        self.appearance_tab.buttons["next tint button"] = UICatButton((365, 75), (34, 34), self.uimanager,
                                                                      "#right_button",
                                                                      self.appearance_tab.container, True,
                                                                      update_tint, 1)
        self.appearance_tab.buttons["previous tortie patch"] = UICatButton((140, 205), (34, 34), self.uimanager,
                                                                           "#left_button",
                                                                           self.appearance_tab.container, True,
                                                                           update_tortie_patches, -1)
        self.appearance_tab.buttons["next tortie patch"] = UICatButton((180, 205), (34, 34), self.uimanager,
                                                                       "#right_button",
                                                                       self.appearance_tab.container, True,
                                                                       update_tortie_patches, 1)
        self.appearance_tab.buttons["previous tortie pattern"] = UICatButton((325, 205), (34, 34),
                                                                             self.uimanager,
                                                                             "#left_button",
                                                                             self.appearance_tab.container,
                                                                             True,
                                                                             update_tortie_pattern, -1)
        self.appearance_tab.buttons["next tortie pattern"] = UICatButton((365, 205), (34, 34), self.uimanager,
                                                                         "#right_button",
                                                                         self.appearance_tab.container, True,
                                                                         update_tortie_pattern, 1)
        self.appearance_tab.buttons["previous tortie colour"] = UICatButton((325, 155), (34, 34),
                                                                            self.uimanager,
                                                                            "#left_button",
                                                                            self.appearance_tab.container,
                                                                            True,
                                                                            update_tortie_colour, -1)
        self.appearance_tab.buttons["next tortie colour"] = UICatButton((365, 155), (34, 34), self.uimanager,
                                                                        "#right_button",
                                                                        self.appearance_tab.container, True,
                                                                        update_tortie_colour, 1)
        self.appearance_tab.buttons["tortie toggle"] = UICatButton((95, 155), (34, 34), self.uimanager,
                                                                   "#unchecked_checkbox",
                                                                   self.appearance_tab.container, True,
                                                                   toggle_tortie)
        self.appearance_tab.buttons["previous tortie patch"].disable()
        self.appearance_tab.buttons["next tortie patch"].disable()
        self.appearance_tab.buttons["previous tortie pattern"].disable()
        self.appearance_tab.buttons["next tortie pattern"].disable()
        self.appearance_tab.buttons["previous tortie colour"].disable()
        self.appearance_tab.buttons["next tortie colour"].disable()
        self.appearance_tab.buttons["heterochromia toggle"] = UICatButton((580, 75), (34, 34), self.uimanager,
                                                                          "#unchecked_checkbox",
                                                                          self.appearance_tab.container, True,
                                                                          toggle_heterochromia)
        self.appearance_tab.buttons["previous eye1"] = UICatButton((490, 145), (34, 34), self.uimanager,
                                                                   "#left_button",
                                                                   self.appearance_tab.container, True,
                                                                   update_eye1_colour, -1)
        self.appearance_tab.buttons["next eye1"] = UICatButton((530, 145), (34, 34), self.uimanager,
                                                               "#right_button",
                                                               self.appearance_tab.container, True,
                                                               update_eye1_colour, 1)

        self.appearance_tab.buttons["previous eye2"] = UICatButton((635, 145), (34, 34), self.uimanager,
                                                                   "#left_button",
                                                                   self.appearance_tab.container, True,
                                                                   update_eye2_colour, -1)
        self.appearance_tab.buttons["next eye2"] = UICatButton((675, 145), (34, 34), self.uimanager,
                                                               "#right_button",
                                                               self.appearance_tab.container, True,
                                                               update_eye2_colour, 1)
        self.appearance_tab.buttons["previous eye2"].disable()
        self.appearance_tab.buttons["next eye2"].disable()
        self.appearance_tab.buttons["previous skin"] = UICatButton((560, 205), (34, 34), self.uimanager,
                                                                   "#left_button",
                                                                   self.appearance_tab.container, True,
                                                                   update_skin, -1)
        self.appearance_tab.buttons["next skin"] = UICatButton((600, 205), (34, 34), self.uimanager,
                                                               "#right_button",
                                                               self.appearance_tab.container, True,
                                                               update_skin, 1)

        # -- extras --
        self.extras_tab.buttons["previous accessory"] = UICatButton((145, 73), (34, 34), self.uimanager,
                                                                    "#left_button",
                                                                    self.extras_tab.container, True,
                                                                    update_accessory, -1)

        self.extras_tab.buttons["next accessory"] = UICatButton((185, 73), (34, 34), self.uimanager,
                                                                "#right_button",
                                                                self.extras_tab.container, True,
                                                                update_accessory, 1)
        self.extras_tab.buttons["previous accessory"].disable()
        self.extras_tab.buttons["next accessory"].disable()
        self.extras_tab.buttons["reverse toggle"] = UICatButton((525, 20), (34, 34), self.uimanager,
                                                                "#unchecked_checkbox",
                                                                self.extras_tab.container, True,
                                                                reverse_cat)
        self.extras_tab.buttons["shading toggle"] = UICatButton((680, 20), (34, 34), self.uimanager,
                                                                "#unchecked_checkbox",
                                                                self.extras_tab.container, True,
                                                                shade_cat)
        self.extras_tab.buttons["previous platform"] = UICatButton((610, 200), (34, 34), self.uimanager,
                                                                   "#left_button",
                                                                   self.extras_tab.container, True,
                                                                   update_platform, -1)

        self.extras_tab.buttons["next platform"] = UICatButton((650, 200), (34, 34), self.uimanager,
                                                               "#right_button",
                                                               self.extras_tab.container, True,
                                                               update_platform, 1)

        self.extras_tab.buttons["previous white tint"] = UICatButton((620, 73), (34, 34), self.uimanager,
                                                                     "#left_button",
                                                                     self.extras_tab.container, True,
                                                                     update_white_tint, -1)

        self.extras_tab.buttons["next white tint"] = UICatButton((660, 73), (34, 34), self.uimanager,
                                                                 "#right_button",
                                                                 self.extras_tab.container, True,
                                                                 update_white_tint, 1)

        # -- save --
        self.save_tab.buttons["export"] = UIButton(relative_rect=pygame.Rect((580, 150), (134, 30)),
                                                   text="",
                                                   manager=self.uimanager,
                                                   container=self.save_tab.container,
                                                   object_id="#export_button")
        self.save_tab.buttons["save sprites"] = UIButton(relative_rect=pygame.Rect((575, 100), (143, 30)),
                                                         text="",
                                                         manager=self.uimanager,
                                                         container=self.save_tab.container,
                                                         object_id="#export_image_button")

    def update_buttons(self):
        """Rebuild toggle buttons and buttons associated with toggles, for use when resetting/randomising cat"""
        self.appearance_tab.buttons["tortie toggle"].kill()
        if self.generator.cat.tortie:
            self.appearance_tab.buttons["previous tortie patch"].enable()
            self.appearance_tab.buttons["next tortie patch"].enable()
            self.appearance_tab.buttons["previous tortie pattern"].enable()
            self.appearance_tab.buttons["next tortie pattern"].enable()
            self.appearance_tab.buttons["previous tortie colour"].enable()
            self.appearance_tab.buttons["next tortie colour"].enable()
            self.appearance_tab.buttons["tortie toggle"] = UICatButton((95, 155), (34, 34),
                                                                       self.uimanager,
                                                                       "#checked_checkbox",
                                                                       self.appearance_tab.container,
                                                                       True, toggle_tortie)
        else:
            self.appearance_tab.buttons["previous tortie patch"].disable()
            self.appearance_tab.buttons["next tortie patch"].disable()
            self.appearance_tab.buttons["previous tortie pattern"].disable()
            self.appearance_tab.buttons["next tortie pattern"].disable()
            self.appearance_tab.buttons["previous tortie colour"].disable()
            self.appearance_tab.buttons["next tortie colour"].disable()
            self.appearance_tab.buttons["tortie toggle"] = UICatButton((95, 155), (34, 34),
                                                                       self.uimanager,
                                                                       "#unchecked_checkbox",
                                                                       self.appearance_tab.container,
                                                                       True, toggle_tortie)
        self.appearance_tab.buttons["heterochromia toggle"].kill()
        if self.generator.cat.heterochromia:
            self.appearance_tab.buttons["previous eye2"].enable()
            self.appearance_tab.buttons["next eye2"].enable()
            self.appearance_tab.buttons["heterochromia toggle"] = UICatButton((580, 75), (34, 34),
                                                                              self.uimanager,
                                                                              "#checked_checkbox",
                                                                              self.appearance_tab.
                                                                              container,
                                                                              True,
                                                                              toggle_heterochromia)
        else:
            self.appearance_tab.buttons["previous eye2"].disable()
            self.appearance_tab.buttons["next eye2"].disable()
            self.appearance_tab.buttons["heterochromia toggle"] = UICatButton((580, 75), (34, 34),
                                                                              self.uimanager,
                                                                              "#unchecked_checkbox",
                                                                              self.appearance_tab.
                                                                              container,
                                                                              True,
                                                                              toggle_heterochromia)
        self.extras_tab.buttons["reverse toggle"].kill()
        if self.generator.cat.reverse:
            self.extras_tab.buttons["reverse toggle"] = UICatButton((525, 20), (34, 34), self.uimanager,
                                                                    "#checked_checkbox",
                                                                    self.extras_tab.container, True,
                                                                    reverse_cat)
        else:
            self.extras_tab.buttons["reverse toggle"] = UICatButton((525, 20), (34, 34), self.uimanager,
                                                                    "#unchecked_checkbox",
                                                                    self.extras_tab.container, True,
                                                                    reverse_cat)

        self.extras_tab.buttons["shading toggle"].kill()
        if self.generator.cat.shading:
            self.extras_tab.buttons["shading toggle"] = UICatButton((680, 20), (34, 34), self.uimanager,
                                                                    "#checked_checkbox",
                                                                    self.extras_tab.container, True,
                                                                    shade_cat)
        else:
            self.extras_tab.buttons["shading toggle"] = UICatButton((680, 20), (34, 34), self.uimanager,
                                                                    "#unchecked_checkbox",
                                                                    self.extras_tab.container, True,
                                                                    shade_cat)
        if self.generator.cat.accessory == "none":
            self.extras_tab.buttons["previous accessory"].disable()
            self.extras_tab.buttons["next accessory"].disable()
        else:
            self.extras_tab.buttons["previous accessory"].enable()
            self.extras_tab.buttons["next accessory"].enable()

        if self.generator.cat.platform == "none":
            self.extras_tab.buttons["previous platform"].disable()
            self.extras_tab.buttons["next platform"].disable()
        else:
            self.extras_tab.buttons["previous platform"].enable()
            self.extras_tab.buttons["next platform"].enable()

    def switch_skillset(self, switch_type):
        """For changing skill dropdown menu"""
        # Kill current skillset
        self.general_tab.dropdowns["skill"].kill()
        if switch_type == "age":  # age updated
            if self.generator.cat.age in ["kitten", "adolescent"]:
                # Set default skill of cat
                self.generator.cat.skill = "unknown"
                self.general_tab.dropdowns["skill"] = UIDropDownMenu(options_list=catdicts.skills["unknown"],
                                                                     starting_option=self.generator.cat.stored_skills[
                                                                         self.generator.cat.skill],
                                                                     relative_rect=pygame.Rect((500, 195), (220, 30)),
                                                                     manager=self.uimanager,
                                                                     container=self.general_tab.container,
                                                                     object_id="drop_up_menu")
            elif self.generator.cat.stored_statuses[self.generator.cat.status] == "medicine cat":
                self.generator.cat.skill = "med"
                self.general_tab.dropdowns["skill"] = UIDropDownMenu(options_list=catdicts.skills["med"],
                                                                     starting_option=self.generator.cat.stored_skills[
                                                                         self.generator.cat.skill],
                                                                     relative_rect=pygame.Rect((500, 195), (220, 30)),
                                                                     manager=self.uimanager,
                                                                     container=self.general_tab.container,
                                                                     object_id="drop_up_menu")
            elif self.generator.cat.age == "elder":
                self.generator.cat.skill = "elder"
                self.general_tab.dropdowns["skill"] = UIDropDownMenu(options_list=catdicts.skills["elder"],
                                                                     starting_option=self.generator.cat.stored_skills[
                                                                         self.generator.cat.skill],
                                                                     relative_rect=pygame.Rect((500, 195), (220, 30)),
                                                                     manager=self.uimanager,
                                                                     container=self.general_tab.container,
                                                                     object_id="drop_up_menu")
            else:
                self.generator.cat.skill = "standard"
                self.general_tab.dropdowns["skill"] = UIDropDownMenu(options_list=catdicts.skills["standard"],
                                                                     starting_option=self.generator.cat.stored_skills[
                                                                         self.generator.cat.skill],
                                                                     relative_rect=pygame.Rect((500, 195), (220, 30)),
                                                                     manager=self.uimanager,
                                                                     container=self.general_tab.container,
                                                                     object_id="drop_up_menu")
        elif switch_type == "status":  # status updated
            if self.generator.cat.stored_statuses[self.generator.cat.status] == "medicine cat":
                self.generator.cat.skill = "med"
                self.general_tab.dropdowns["skill"] = UIDropDownMenu(options_list=catdicts.skills["med"],
                                                                     starting_option=self.generator.cat.stored_skills[
                                                                         self.generator.cat.skill],
                                                                     relative_rect=pygame.Rect((500, 195), (220, 30)),
                                                                     manager=self.uimanager,
                                                                     container=self.general_tab.container,
                                                                     object_id="drop_up_menu")
            elif self.generator.cat.stored_statuses[self.generator.cat.status] == "elder":
                self.generator.cat.skill = "elder"
                self.general_tab.dropdowns["skill"] = UIDropDownMenu(options_list=catdicts.skills["elder"],
                                                                     starting_option=self.generator.cat.stored_skills[
                                                                         self.generator.cat.skill],
                                                                     relative_rect=pygame.Rect((500, 195), (220, 30)),
                                                                     manager=self.uimanager,
                                                                     container=self.general_tab.container,
                                                                     object_id="drop_up_menu")
            elif self.generator.cat.stored_statuses[self.generator.cat.status] in ["kitten", "apprentice",
                                                                                   "mediator apprentice",
                                                                                   "medicine cat apprentice"]:
                self.generator.cat.skill = "unknown"
                self.general_tab.dropdowns["skill"] = UIDropDownMenu(options_list=catdicts.skills["unknown"],
                                                                     starting_option=self.generator.cat.stored_skills[
                                                                         self.generator.cat.skill],
                                                                     relative_rect=pygame.Rect((500, 195), (220, 30)),
                                                                     manager=self.uimanager,
                                                                     container=self.general_tab.container,
                                                                     object_id="drop_up_menu")
            else:
                self.generator.cat.skill = "standard"
                self.general_tab.dropdowns["skill"] = UIDropDownMenu(options_list=catdicts.skills["standard"],
                                                                     starting_option=self.generator.cat.stored_skills[
                                                                         self.generator.cat.skill],
                                                                     relative_rect=pygame.Rect((500, 195), (220, 30)),
                                                                     manager=self.uimanager,
                                                                     container=self.general_tab.container,
                                                                     object_id="drop_up_menu")

    def switch_traitset(self):
        """For changing traitset dropdown menu"""
        # Kill current traitset
        self.general_tab.dropdowns["trait"].kill()
        if self.generator.cat.age == "kitten":
            self.generator.cat.trait = "kit"
            self.general_tab.dropdowns["trait"] = UIDropDownMenu(options_list=catdicts.traits["kit"],
                                                                 starting_option=self.generator.cat.stored_traits[
                                                                     self.generator.cat.trait],
                                                                 relative_rect=pygame.Rect((500, 145), (220, 30)),
                                                                 manager=self.uimanager,
                                                                 container=self.general_tab.container,
                                                                 object_id="drop_up_menu")
        else:
            self.generator.cat.trait = "nonkit"
            self.general_tab.dropdowns["trait"] = UIDropDownMenu(options_list=catdicts.traits["nonkit"],
                                                                 starting_option=self.generator.cat.stored_traits[
                                                                     self.generator.cat.trait],
                                                                 relative_rect=pygame.Rect((500, 145), (220, 30)),
                                                                 manager=self.uimanager,
                                                                 container=self.general_tab.container,
                                                                 object_id="drop_up_menu")

    def switch_statusset(self):
        """For changing statusset dropdown menu"""
        # Kill current status set
        self.general_tab.dropdowns["status"].kill()
        if self.generator.cat.age == "kitten":
            self.generator.cat.status = "kit"
            self.general_tab.dropdowns["status"] = UIDropDownMenu(options_list=catdicts.statuses["kit"],
                                                                  starting_option=self.generator.cat.stored_statuses[
                                                                      self.generator.cat.status],
                                                                  relative_rect=pygame.Rect((500, 27), (220, 30)),
                                                                  manager=self.uimanager,
                                                                  container=self.general_tab.container,
                                                                  object_id="drop_down_menu")
        elif self.generator.cat.age == "adolescent":
            self.generator.cat.status = "adolescent"
            self.general_tab.dropdowns["status"] = UIDropDownMenu(options_list=catdicts.statuses["adolescent"],
                                                                  starting_option=self.generator.cat.stored_statuses[
                                                                      self.generator.cat.status],
                                                                  relative_rect=pygame.Rect((500, 27), (220, 30)),
                                                                  manager=self.uimanager,
                                                                  container=self.general_tab.container,
                                                                  object_id="drop_down_menu")
        elif self.generator.cat.age == "elder":
            self.generator.cat.status = "elder"
            self.general_tab.dropdowns["status"] = UIDropDownMenu(options_list=catdicts.statuses["elder"],
                                                                  starting_option=self.generator.cat.stored_statuses[
                                                                      self.generator.cat.status],
                                                                  relative_rect=pygame.Rect((500, 27), (220, 30)),
                                                                  manager=self.uimanager,
                                                                  container=self.general_tab.container,
                                                                  object_id="drop_down_menu")
        else:
            self.generator.cat.status = "adult"
            self.general_tab.dropdowns["status"] = UIDropDownMenu(options_list=catdicts.statuses["adult"],
                                                                  starting_option=self.generator.cat.stored_statuses[
                                                                      self.generator.cat.status],
                                                                  relative_rect=pygame.Rect((500, 27), (220, 30)),
                                                                  manager=self.uimanager,
                                                                  container=self.general_tab.container,
                                                                  object_id="drop_down_menu")

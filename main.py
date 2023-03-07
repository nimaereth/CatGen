import sys
import os
from scripts.config import *

directory = os.path.dirname(__file__)
if directory:
    os.chdir(directory)

# PYGAME ------------
clock = pygame.time.Clock()
MENU.open_screen()

while True:
    time_delta = clock.tick(60)/1000

    # Screen fill
    WINDOW.fill((206, 194, 168))

    # Draw screen
    GENERATOR.all_screens[GENERATOR.current_screen].on_use()

    # Event handling
    for event in pygame.event.get():
        GENERATOR.all_screens[GENERATOR.current_screen].handle_event(event)

        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()

        MANAGER.process_events(event)

    MANAGER.update(time_delta)

    if GENERATOR.change_screen_flag:
        GENERATOR.all_screens[GENERATOR.previous_screen].exit_screen()
        GENERATOR.all_screens[GENERATOR.current_screen].open_screen()
        GENERATOR.change_screen_flag = False

    MANAGER.draw_ui(WINDOW)
    pygame.display.update()

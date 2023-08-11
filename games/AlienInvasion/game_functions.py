import sys

import pygame


def check_events():
    """Respond to key presses and mouse evens."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(ai_settings, screen, ship):
    """Update the screen during each loop"""
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # Make the most recently event visible by refreshing.
    pygame.display.flip()

import pygame
import sys

from settings import Settings
from ship import Ship 
import game_functions as gf


def run_game():
    #initialize pygame, settings and screen objects
    pygame.init()
    settings = Settings()

    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Monopoly")

    # Make the Ship
    # ship = Ship(screen)
    # Start the main loop for the game
    while True:

        # Watch keyboard and mouse events
        gf.check_events()
        gf.update_screen(settings, screen)


run_game()

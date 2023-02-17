import pygame
from settings import Settings
from ship import Ship 
import game_functions as gf 

def run_game():

    # Initialize game and create screen object.
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(
        (settings.scren_width, settings.scren_height))
    pygame.display.set_caption("Alien Invasion")

    # Make the ship
    ship = Ship(screen)

    # Start the main loop for the game 
    while True:

        gf.check_events()
        gf.update_screen()


run_game()
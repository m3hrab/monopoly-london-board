import sys 
import pygame 
from settings import Settings  
from board import Board
from button import Button
import game_functions as gf

def run_game():
    # Initialize the game and create screen objects
    pygame.init()
    settings = Settings()

    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Monopoly")

    # Make a board
    board = Board(screen)

    # Add the buttons
    roll_btn = Button(board)
    
    # Start the main loop for the game 
    while True:

        gf.check_events()
        gf.update_screen(settings, screen, board, roll_btn)

run_game()
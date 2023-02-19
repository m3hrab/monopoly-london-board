import sys 
import pygame 
from settings import Settings  
from board import Board
from button import Button
from dice import Dice
import game_functions as gf
from start_window import TextInput

def run_game():

    # Initialize the game and create screen objects
    pygame.init()
    settings = Settings()

    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))

    # Set a the game title 
    pygame.display.set_caption("Monopoly")

    # Make a board
    board = Board(screen)

    # Add the buttons
    roll_btn = Button(board)
    
    # Make two dice 
    position1 = (board.rect.centerx+30, board.rect.centery+80)
    position2 = (board.rect.centerx-30, board.rect.centery+80)

    dice = Dice(position1, position2, screen)
    
    new_game = True
    text_input = TextInput(screen)
                        
    # Start the main loop for the game 
    while True:
        gf.check_events(dice, new_game, text_input)
        gf.update_screen(settings, screen, board, roll_btn,
                        dice, new_game, text_input)
        
        

run_game()
import pygame,sys 
from settings import Settings  
from board import Board
from button import Button
from dice import Dice
import game_functions as gf
from start_window import TextInput
from player import MonopolyPlayer

def run_game():

    # Initialize the game and create screen objects
    pygame.init()
    settings = Settings()

    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))

    # Set a the game title 
    pygame.display.set_caption("Monopoly")

    # ----------------------Start Window---------------------

    text_input = TextInput(screen)
    while text_input.collect_assets != True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            text_input.handle_event(event)
        
        text_input.draw()

    #-----------------------Close Opening Window -----------------

    # Make a board
    board = Board(screen, text_input)

    # Add the buttons
    roll_btn = Button(board)
    
    # Make two dice 
    position1 = (board.rect.centerx+30, board.rect.centery+80)
    position2 = (board.rect.centerx-30, board.rect.centery+80)

    dice = Dice(position1, position2, screen)

    # Create Players list from the list of players that added in the start window
    players = []
    for i in range(len(text_input.select_tokens)):
        x = board.rect.right - 30
        y = board.rect.bottom - 30 
        player = MonopolyPlayer(text_input.players[i], text_input.select_tokens[i], x,y)
        players.append(player)

    # Start the main loop for the game 
    while True:
        gf.check_events(dice, roll_btn, players)
        gf.update_screen(settings, screen, board, roll_btn, dice, players)
        
        
run_game()
import sys
import pygame 

def check_events(dice, roll_btn):
    # Watch keyboard and mouse events

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:

            if roll_btn.roll_btn_rect.collidepoint(event.pos):
                dice.roll()
            

def update_screen(settings, screen, board, roll_btn, dice):

    # Redraw the screen during each pass through the loop
    screen.fill(settings.bg_color)
    board.draw()
    roll_btn.draw(screen)
    dice.draw()
    
    # Make the recently drawn screen visible 
    pygame.display.flip()

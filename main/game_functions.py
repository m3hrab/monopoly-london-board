import sys
import pygame 

def check_events(dice1):
    # Watch keyboard and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dice1.roll()
                # dice2.roll()

def update_screen(settings, screen, board, roll_btn, dice1):

    # Redraw the screen during each pass through the loop
    screen.fill(settings.bg_color)
    board.draw()
    roll_btn.draw(screen)
    dice1.draw()
    # dice2.draw()

    # Make the recently drawn screen visible 
    pygame.display.flip()

import sys
import pygame 

def check_events():
    # Watch keyboard and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(settings, screen, board, roll_btn):
    # Redraw the screen during each pass through the loop
    screen.fill(settings.bg_color)
    board.draw()
    roll_btn.draw(screen)
    # Make the recently drawn screen visible 
    pygame.display.flip()

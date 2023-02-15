import sys
import pygame

def check_events():
    """Responds to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()



def update_screen(settings, screen):
    """Update images on the screen and flip to the new screen"""

    # Redraw teh screen during each pass through the loop
    screen.fill(settings.bg_color)
    
    # make the recently drawn screen visible.   
    pygame.display.flip()

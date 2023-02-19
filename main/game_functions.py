import sys
import pygame 

pygame.init()
# New game window
base_font = pygame.font.Font(None, 32)
user_text = 'Mehrab'
input_rect = pygame.Rect(100,100,140,32)
color_active = (230,230,230)
color_passive = (30,30,30)

color = color_passive
active = False

def check_events(dice, text_input):
    # Watch keyboard and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if text_input.collect_assets != True: 
            text_input.handle_event(event)

def update_screen(settings, screen, board, roll_btn, dice, text_input):

    # Redraw the screen during each pass through the loop
    if text_input.collect_assets != True:
        text_input.draw()

    else:
        screen.fill(settings.bg_color)
        board.draw()
        roll_btn.draw(screen)
        dice.draw()
        # Make the recently drawn screen visible 
        pygame.display.flip()

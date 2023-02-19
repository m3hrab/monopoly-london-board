import pygame
import sys 
from start_window import TextInput
# Initialize Pygame
pygame.init()

# Set up the window
window_size = (400, 300)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Text Input Demo')

# Create a text input box
text_input = TextInput(50, 50, 300, 40)

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # If the user closes the window, exit the program.
            pygame.quit()
            sys.exit()
        else:
            # Otherwise, handle the event with the text input box.
            text_input.handle_event(event)
    
    # Draw the text input box
    screen.fill((0, 0, 0))
    text_input.draw(screen)
    pygame.display.update()

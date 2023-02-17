import pygame

pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

# Set the caption
pygame.display.set_caption("Animated Button")

# Define the font and text
font = pygame.font.Font(None, 36)
text = font.render("Click Me", True, WHITE)

# Define the button rect and initial color
button_rect = pygame.Rect(250, 200, 200, 50)
button_color = GRAY

# Define the animation variables
animation_speed = 5
animation_direction = 1
animation_offset = 0

# Main loop
done = False
while not done:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                print("Button clicked!")
    
    # Clear the screen
    screen.fill(BLACK)
    
    # Update the button color and animation variables
    if button_rect.collidepoint(pygame.mouse.get_pos()):
        button_color = WHITE
        animation_offset += animation_direction * animation_speed
        if animation_offset > 10:
            animation_direction = -1
        elif animation_offset < 0:
            animation_direction = 1
    else:
        button_color = GRAY
        animation_offset = 0
    
    # Draw the button
    pygame.draw.rect(screen, button_color, button_rect)
    button_text_rect = text.get_rect(center=button_rect.center)
    button_text_rect.move_ip(0, animation_offset)
    screen.blit(text, button_text_rect)
    
    # Update the screen
    pygame.display.flip()

# Quit pygame
pygame.quit()

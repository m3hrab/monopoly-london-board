import pygame

pygame.init()

# Set up the screen
screen = pygame.display.set_mode((800, 600))

# Set up the cursor
hand_cursor = (
    "    XX        ",
    "   X..X       ",
    "  X....X      ",
    " X......X     ",
    "X........X    ",
    "X........X    ",
    "X........X    ",
    "X........X    ",
    "X........X    ",
    " X......X     ",
    "  X....X      ",
    "   X..X       ",
    "    XX        ",
    "              ",
    "              ",
    "              "
)
pygame.mouse.set_cursor((16, 16), (5, 1), *pygame.cursors.compile(hand_cursor))

# Run the game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Draw the screen
    screen.fill((255, 255, 255))
    pygame.display.update()

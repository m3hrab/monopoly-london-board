import pygame

class Button:

    def __init__(self, board):

        self.roll_btn = pygame.image.load('main/Assets/images/buttons/roll.png')
        self.build_btn = pygame.image.load('main/Assets/images/buttons/build.png')
        self.sell_btn = pygame.image.load('main/Assets/images/buttons/sell.png')
        self.trade_btn = pygame.image.load('main/Assets/images/buttons/trade.png')

        #Get the buttons rects
        self.roll_btn_rect = self.roll_btn.get_rect()
        self.build_btn_rect = self.build_btn.get_rect()
        self.sell_btn_rect = self.sell_btn.get_rect()
        self.trade_btn_rect = self.trade_btn.get_rect()


        # set the buttons rect 
        # roll btn 
        self.roll_btn_rect.centerx = board.rect.centerx 
        self.roll_btn_rect.centery = board.rect.centery + 140

        # build button
        self.build_btn_rect.right = self.roll_btn_rect.left - 10
        self.build_btn_rect.top = self.roll_btn_rect.bottom + 12

        # sell button
        self.sell_btn_rect.centerx = self.roll_btn_rect.centerx
        self.sell_btn_rect.top = self.roll_btn_rect.bottom + 10

        # trade btn
        self.trade_btn_rect.left = self.roll_btn_rect.right + 10
        self.trade_btn_rect.top = self.roll_btn_rect.bottom + 10

    # def handle_events(self, event):
    #     if self.roll_btn_rect.collidepoint(event.pos):
    #         dice roll

        
    def draw(self, screen):
        screen.blit(self.roll_btn, self.roll_btn_rect)
        screen.blit(self.build_btn, self.build_btn_rect)
        screen.blit(self.sell_btn, self.sell_btn_rect)
        screen.blit(self.trade_btn, self.trade_btn_rect)

    
    # def clicked(self, event):
    #     return self.rect.collidepoint(event.pos)
    



# pygame.init()

# # Set the width and height of the screen [width, height]
# size = (700, 500)
# screen = pygame.display.set_mode(size)

# # Set the caption
# pygame.display.set_caption("Custom Button Class")

# # Load the button image and create the button object
# button_image = pygame.image.load('button_image.png')
# button = Button(button_image, (size[0] // 2, size[1] // 2))

# # Main loop
# done = False
# while not done:
#     # Event handling
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             if button.clicked(event):
#                 print("Button clicked!")
    
#     # Clear the screen
#     screen.fill((255, 255, 255))
    
#     # Draw the button
#     button.draw(screen)
    
#     # Update the screen
#     pygame.display.flip()

# # Quit pygame
# pygame.quit()

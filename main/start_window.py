import pygame

class TextInput():

    def __init__(self, screen, font_size=32,):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.rect = pygame.Rect(self.screen_rect.centerx-150, self.screen_rect.centery+50, 200,40)
        self.color = pygame.Color('gray')
        self.text = ''
        self.font = pygame.font.Font(None, font_size)
        self.active = False
        self.players = []

        # Load images and sets it's position
        self.img = pygame.image.load("main/Assets/images/Board/img.png")
        self.img_rect = self.img.get_rect()
        self.img_rect.centerx = self.screen_rect.centerx 
        self.img_rect.centery = self.screen_rect.centery - 100

        # Load the buttons
        self.add_btn = pygame.image.load("main/Assets/images/buttons/add.png")
        self.add_btn2 = pygame.image.load("main/Assets/images/buttons/add_clicked.png")
        self.done_btn = pygame.image.load("main/Assets/images/buttons/done.png")
        self.done_btn2 = pygame.image.load("main/Assets/images/buttons/done_clicked.png")

        # Get the buttons position
        self.add_btn_rect = self.add_btn.get_rect()
        self.done_btn_rect = self.done_btn.get_rect()

        # Set the buttons positons 
        self.add_btn_rect.centerx = self.screen_rect.centerx - 50
        self.add_btn_rect.centery = self.rect.bottom + 30

        self.done_btn_rect.centerx = self.screen_rect.centerx + 50
        self.done_btn_rect.centery = self.rect.bottom + 30


    def handle_event(self, event):
        
        if event.type == pygame.MOUSEBUTTONDOWN:

            # If the user clicks on the text input box, activate it.
            if self.rect.collidepoint(event.pos):
                self.active = True
                self.color = pygame.Color('white')
            else:
                self.active = False
                self.color = pygame.Color('gray')

            if self.add_btn_rect.collidepoint(event.pos) and self.text != '':
                # If the user presses enter, finish input and clear the text box.
                self.players.append(self.text)
                print(self.players)
                self.text = ''                

        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN and self.text != '':
                # If the user presses enter, finish input and clear the text box.
                self.players.append(self.text)
                print(self.players)
                self.text = ''
            elif event.key == pygame.K_BACKSPACE:
                # If the user presses backspace, remove the last character from the text box.
                self.text = self.text[:-1]
            else:
                # Otherwise, add the character to the text box.
                self.text += event.unicode

    
    def draw(self):
        # Draw the text input box and the text inside it.
        self.screen.fill((92, 225, 230))
        self.screen.blit(self.img, self.img_rect)

        pygame.draw.rect(self.screen, self.color, self.rect, 2)
        text_surface = self.font.render(self.text, True, self.color)
        self.screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))
        
        self.screen.blit(self.add_btn, self.add_btn_rect)
        self.screen.blit(self.done_btn, self.done_btn_rect)

        
        pygame.display.flip()
        self.rect.w = max(300, text_surface.get_width() + 10)

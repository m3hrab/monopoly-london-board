import pygame

class TextInput():

    def __init__(self, screen, font_size=28):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.rect = pygame.Rect(self.screen_rect.centerx-150, self.screen_rect.centery, 200,30)
        self.color = pygame.Color('gray')
        self.text = ''
        self.font = pygame.font.Font(None, font_size)
        self.active = False
        self.players = []
        self.tokens = []
        self.select_tokens = []
        self.select_tokens_rect = []
        self.token_flag = False
        self.tokens_rect = []
        self.collect_assets = False
        self.add_is_click = False
        self.done_is_click = False
        self.t_flag = True


        # Load images and sets it's position
        self.img = pygame.image.load("main/Assets/images/Board/img.png")
        self.img_rect = self.img.get_rect()
        self.img_rect.centerx = self.screen_rect.centerx 
        self.img_rect.centery = self.screen_rect.centery - 130


        # Load all the tokens and get their positions
        for i in range(8):
            self.tokens.append(pygame.image.load(f"main/Assets/images/tokens/{(i+1)}.png"))
            self.tokens_rect.append(self.tokens[i].get_rect())


        # Sets tokens position 
        space = 10
        for rect in self.tokens_rect:
            rect.centerx = self.screen_rect.centerx - 170 + space 
            rect.centery = self.rect.bottom + 30
            space += 50

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
        self.add_btn_rect.centery = self.tokens_rect[0].bottom + 30

        self.done_btn_rect.centerx = self.screen_rect.centerx + 50
        self.done_btn_rect.centery = self.tokens_rect[0].bottom + 30


    def handle_event(self, event):
        
        if event.type == pygame.MOUSEBUTTONDOWN:

            # If the user clicks on the text input box, activate it.
            if self.rect.collidepoint(event.pos):
                self.active = True
                self.color = pygame.Color('white')
            else:
                self.active = False
                self.color = pygame.Color('gray')

            if self.text != '':
                # Check players tokens selected
                if len(self.select_tokens)==len(self.players):
                    for i in range(len(self.tokens_rect)):
                        if self.tokens_rect[i].collidepoint(event.pos):
                            self.token_flag = True
                            self.select_tokens.append(self.tokens[i])
                            break


                if self.token_flag and self.add_btn_rect.collidepoint(event.pos):
                    # If the user presses enter, finish input and clear the text box.
                    self.add_is_click = True
                    self.players.append(self.text)
                    # print(self.players)
                    self.text = ''
                    self.token_flag = False
                                    

            if self.done_btn_rect.collidepoint(event.pos) and len(self.players)>1:
                # Go to the main game
                self.collect_assets = True
                self.done_is_click = True


        if event.type == pygame.KEYDOWN and self.active:
            # if event.key == pygame.K_RETURN and self.text != '':
            #     # If the user presses enter, finish input and clear the text box.
            #     self.players.append(self.text)
            #     print(self.players)
            #     self.text = ''
            if event.key == pygame.K_BACKSPACE:
                # If the user presses backspace, remove the last character from the text box.
                self.text = self.text[:-1]
            else:
                # Otherwise, add the character to the text box.
                self.text += event.unicode

    
    def draw(self):
        # Draw the text input box and the text inside it.
        self.screen.fill((168, 218, 220)) #(92, 225, 230))
        self.screen.blit(self.img, self.img_rect)

        pygame.draw.rect(self.screen, self.color, self.rect, 2)
        text_surface = self.font.render(self.text, True, self.color)
        self.screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))

        # Show the available tokens
        for i in range(len(self.tokens)):
            if self.tokens[i] not in self.select_tokens:
                self.screen.blit(self.tokens[i], self.tokens_rect[i])
        
        if self.add_is_click:
            self.screen.blit(self.add_btn2, self.add_btn_rect)
            self.add_is_click = False
        else:
            self.screen.blit(self.add_btn, self.add_btn_rect)

        if self.done_is_click:
            self.screen.blit(self.done_btn2, self.done_btn_rect)
            self.done_is_click = False
        else:
            self.screen.blit(self.done_btn, self.done_btn_rect)

        gap = 25
        text_color = pygame.Color('White')

        for i in range(len(self.players)):
            text = str(i+1) + ". " + self.players[i]
            text_surface2 = self.font.render(text, True, text_color)
            self.screen.blit(text_surface2, (self.add_btn_rect.centerx , self.add_btn_rect.bottom + gap))

            # Display the token with player 
            self.screen.blit(self.select_tokens[i], (self.add_btn_rect.right + 50 , self.add_btn_rect.bottom + gap-10))
            gap += 40
        
        pygame.display.flip()
        self.rect.w = max(300, text_surface.get_width() + 10)

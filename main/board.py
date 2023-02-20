# import pygame

# class Board():
#     BOARD_X_OFFSET = 130

#     def __init__(self, screen, players):
#         """Initialize the board and set its starting position"""

#         self.screen = screen 
#         self.image = pygame.image.load("main/Assets/images/Board/3.png")
#         self.rect = self.image.get_rect()
#         self.screen_rect = screen.get_rect()

#         # Initialize player names
#         self.players = players

#         # Sets the board position
#         self.rect.centerx = self.screen_rect.centerx - self.BOARD_X_OFFSET
#         self.rect.centery = self.screen_rect.centery 

#         # Player statistics 
#         self.image2 = pygame.image.load("main/Assets/images/Board/player-statistics.png")
#         self.rect2 = self.image2.get_rect()

#         # Sets the players statistic card position
#         self.rect2.left = self.rect.right + 20
#         self.rect2.top = self.screen_rect.top + 2

#         # Property statistics 
#         self.image3 = pygame.image.load("main/Assets/images/Board/property-statistics.png")
#         self.rect3 = self.image3.get_rect()

#         # Sets the players statistic card position
#         self.rect3.left = self.rect.right + 20
#         self.rect3.top = self.rect2.bottom + 8

#     def draw_board(self):
#         """Draw the board"""
#         self.screen.blit(self.image, self.rect)

#     def draw_player_inputs(self):
#         """Draw the player inputs"""
#         self.screen.blit(self.image2, self.rect2)
#         gap = 25
#         text_color = pygame.Color('White')

#         for i in range(len(self.players.players)):
#             text = str(i+1) + ". " + self.players.players[i]
#             text_surface2 = self.players.font.render(text, True, text_color)
#             self.screen.blit(text_surface2, (self.rect2.left + 30 , self.rect2.top + 30 + gap))

#             # Display the token with player 
#             self.screen.blit(self.players.select_tokens[i],(self.rect2.left + 120 , self.rect2.top + 25 + gap))
#             gap += 25

#     def draw_properties(self):
#         self.screen.blit(self.image3, self.rect3)

#     def draw(self):
#         """Redraw the board and player inputs"""
#         self.draw_board()
#         self.draw_player_inputs()
#         self.draw_properties()



#######################################
import os
import pygame

# Set the current working directory to the directory of the script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Board():

    def __init__(self, screen, text_inputs):
        """Initialize the board and set its starting position"""

        self.screen = screen 
        self.image = pygame.image.load("Assets/images/Board/3.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Initialize text inputs
        self.text_inputs = text_inputs

        # Sets the board position
        self.rect.centerx = self.screen_rect.centerx - 130
        self.rect.centery = self.screen_rect.centery 

        # Player statistics 
        self.image2 = pygame.image.load("Assets/images/Board/player-statistics.png")
        self.rect2 = self.image2.get_rect()

        # Sets the players statistic card position
        self.rect2.left = self.rect.right + 20
        self.rect2.top = self.screen_rect.top + 2

        # Property statistics 
        self.image3 = pygame.image.load("Assets/images/Board/property-statistics.png")
        self.rect3 = self.image3.get_rect()

        # Sets the players statistic card position
        self.rect3.left = self.rect.right + 20
        self.rect3.top = self.rect2.bottom + 8

    def draw(self):
        """Redraw the board"""
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.image2, self.rect2)
        self.screen.blit(self.image3, self.rect3)

        # Draw the players inputs
        gap = 25
        text_color = pygame.Color('White')

        for i in range(len(self.text_inputs.players)):
            text = str(i+1) + ". " + self.text_inputs.players[i]
            text_surface2 = self.text_inputs.font.render(text, True, text_color)
            self.screen.blit(text_surface2, (self.rect2.left + 30 , self.rect2.top + 30 + gap))

            # Display the token with player 
            self.screen.blit(self.text_inputs.select_tokens[i],(self.rect2.left + 120 , self.rect2.top + 25 + gap))
            gap += 25

    def draw_player_inputs(self, players, select_tokens):
        """Draws the input box for each player and allows player to choose a token"""

        self.text_inputs.players = players
        self.text_inputs.select_tokens = select_tokens

        # Set the position for player name and token input
        gap = 25
        input_gap = 40

        for i in range(len(players)):
            # Draw the player name input box
            player_name_rect = pygame.Rect(self.rect2.left + 10, self.rect2.top + input_gap + gap, 200, 20)
            pygame.draw.rect(self.screen, pygame.Color('White'), player_name_rect)

            # Draw the token selection box
            token_rect = pygame.Rect(self.rect2.left + 110, self.rect2.top + input_gap + gap, 30, 30)
            pygame.draw.rect(self.screen, pygame.Color('White'), token_rect)

            gap += 25

    def detect_collision(self, mouse_pos):
        """Detect if a mouse click is within a player name input box"""

        for i in range(len(self.text_inputs.players)):
            player_name_rect = pygame.Rect(self.rect2.left + 10, self.rect2.top + 70 + (25 * i), 200, 20)

            if player_name_rect.collidepoint(mouse_pos):
                return i


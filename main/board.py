import pygame 

class Board():

    def __init__(self, screen):
        """Initialize the ship and set its starting position"""

        self.screen = screen 
        self.image = pygame.image.load("main/images/3.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Sets the board positon
        self.rect.centerx = self.screen_rect.centerx - 130
        self.rect.centery = self.screen_rect.centery 

        # Player statistics 
        self.image2 = pygame.image.load("main/images/player-statistics.png")
        self.rect2 = self.image2.get_rect()

        # Sets the players statistic card position
        self.rect2.left = self.rect.right + 20
        self.rect2.top = self.screen_rect.top + 2

        # Property statistics 
        self.image3 = pygame.image.load("main/images/property-statistics.png")
        self.rect3 = self.image3.get_rect()

        # Sets the players statistic card position
        self.rect3.left = self.rect.right + 20
        self.rect3.top = self.rect2.bottom + 8

    def blitme(self):
        """Redraw the board"""
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.image2, self.rect2)
        self.screen.blit(self.image3, self.rect3)

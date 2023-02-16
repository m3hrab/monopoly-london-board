import pygame 

class Board():

    def __init__(self, screen):
        """Initialize the ship and set its starting position"""

        self.screen = screen 
        self.image = pygame.image.load("main/images/board.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Sets the board positon
        self.rect.centerx = self.screen_rect.centerx - 100
        self.rect.centery = self.screen_rect.centery 

    def blitme(self):
        """Redraw the board"""
        self.screen.blit(self.image, self.rect)

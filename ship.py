import pygame

class Ship():

    def __init__(self, screen):
        """Initialzie the ship and set its starting position."""
        self.screen = screen 

        # Load the ship and set its starting position
        self.image = pygame.image.load("bg.jpg")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Start the screen at the bottom center of the screen
        self.rect.x = self.screen_rect.top
        self.rect.y = self.screen_rect.y 

    def blitme(self):
        """Draw the ship at its current location""" 
        self.screen.blit(self.image, self.rect)
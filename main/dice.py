import pygame
import random

class Dice(pygame.sprite.Sprite):
    def __init__(self, position, position2, screen):

        super().__init__()
        self.images = []
        for i in range(1,7):
            img = pygame.image.load(f'main/Assets/images/dice/{i}.png')
            self.images.append(img)

        self.image = self.images[0]
        self.image2 = self.images[0]
        self.rect = self.image.get_rect(center=position)
        self.rect2 = self.image2.get_rect(center=position2)

        self.sound = pygame.mixer.Sound('main/Assets/audio/dice_roll.wav')
        self.sound.set_volume(0.5)
        self.number = None
        self.screen = screen
        
    def roll(self):

        self.sound.play()
        for img in self.images:
            self.image = img
            self.image2 = img
            self.draw()
            pygame.display.flip()
            pygame.time.wait(50)
        self.number = random.randint(1, 6)
        self.image = self.images[self.number - 1]

        self.number2 = random.randint(1, 6)
        self.image2 = self.images[self.number2 - 1]
        self.draw()

    def update(self):
        self.draw()
        
    def draw(self):
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.image2, self.rect2)

        

import pygame
import random

class Dice(pygame.sprite.Sprite):
    def __init__(self, images, position, surface):
        super().__init__()
        self.images = images
        self.image = self.images[0]
        self.rect = self.image.get_rect(center=position)
        self.roll_animation = RollAnimation(self.images, self.rect.center)
        self.number = None
        self.surface = surface
        
    def roll(self):
        self.roll_animation.start()
        self.number = random.randint(1, 6)
        self.image = self.images[self.number-1]
        self.roll_animation.stop()
        self.draw()
        
    def update(self):
        self.roll_animation.update()
        self.draw()
        
    def draw(self):
        self.surface.blit(self.image, self.rect)
        
class RollAnimation(pygame.sprite.Sprite):
    def __init__(self, images, position):
        super().__init__()
        self.images = images
        self.image_index = 0
        self.image = self.images[self.image_index]
        self.rect = self.image.get_rect(center=position)
        self.animation_speed = 8
        self.animation_counter = 0
        self.animation_on = False
        
    def start(self):
        self.animation_on = True
        self.image_index = 0
        self.image = self.images[self.image_index]
        self.animation_counter = 0
        
    def stop(self):
        self.animation_on = False
        self.image_index = 0
        self.image = self.images[self.image_index]
        self.animation_counter = 0
        
    def update(self):
        if self.animation_on:
            self.animation_counter += 1
            if self.animation_counter % self.animation_speed == 0:
                self.image_index += 1
                if self.image_index >= len(self.images):
                    self.image_index = 0
                self.image = self.images[self.image_index]

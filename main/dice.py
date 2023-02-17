import pygame
import random

class Dice(pygame.sprite.Sprite):
    def __init__(self, position, screen):

        super().__init__()
        self.images = []
        for i in range(1,19):
            img = pygame.image.load(f'main/Assets/images/dice/{i}.png')
            self.images.append(img)

        self.image = self.images[0]
        self.rect = self.image.get_rect(center=position)
        self.roll_animation = RollAnimation(self.images, self.rect.center)
        self.sound = pygame.mixer.Sound('main/Assets/audio/dice_roll.wav')
        self.sound.set_volume(0.5)
        self.number = None
        self.screen = screen
        
    def roll(self):

        self.sound.play()
        self.roll_animation.start()
        for img in self.images:
            self.image = img
            self.draw()
            pygame.time.wait(50)
            
        self.roll_animation.stop()
        self.number = random.randint(1, 6)
        self.image = self.images[self.number - 1]
        self.draw()

    def update(self):
        self.roll_animation.update()
        self.draw()
        
    def draw(self):
        self.screen.blit(self.image, self.rect)
        
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


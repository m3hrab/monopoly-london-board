import pygame
import random

class Die(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        super().__init__()
        self.images = []
        for i in range(1, 7):
            image = pygame.image.load(f'main/images/{i}.png').convert_alpha()
            image = pygame.transform.scale(image, (size, size))
            self.images.append(image)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.value = 1
        self.rolling = False
        self.roll_speed = 8
        self.roll_frames = 16
        self.roll_count = 0
        self.roll_sound = pygame.mixer.Sound('dice_roll.wav')

    def roll(self):
        self.value = random.randint(1, 6)
        self.rolling = True
        self.roll_count = 0
        self.roll_sound.play()

    def update(self):
        if self.rolling:
            self.roll_count += 1
            if self.roll_count > self.roll_frames:
                self.rolling = False
                self.image = self.images[self.value - 1]
            else:
                index = self.roll_count // self.roll_speed
                self.image = self.images[index % 6]

class Dice(pygame.sprite.Group):
    def __init__(self, x, y, size):
        super().__init__()
        self.add(Die(x, y, size))
        self.add(Die(x + size + 20, y, size))

    def roll(self):
        for die in self.sprites():
            die.roll()

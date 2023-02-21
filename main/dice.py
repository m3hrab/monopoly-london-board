import pygame
import random


class Dice(pygame.sprite.Sprite):
    """A class that manage the dices"""

    # Define the constructor method for the Dice class
    def __init__(self, position, position2, screen):

        # Call the constructor of the parent class
        super().__init__()

        # Load the images for the dice from disk and store them in a list
        self.images = []
        for i in range(1,7):
            img = pygame.image.load(f'main/Assets/images/dice/{i}.png')
            self.images.append(img)

        # Set the initial image for the dice sprite
        self.image = self.images[0]
        self.image2 = self.images[0]

        # Set the position of the dice sprite
        self.rect = self.image.get_rect(center=position)
        self.rect2 = self.image2.get_rect(center=position2)

        # Load the sound effect for the dice roll
        self.sound = pygame.mixer.Sound('main/Assets/audio/dice_roll.wav')
        self.sound.set_volume(0.5)

        # Set the initial number on the dice to None
        self.number = None
        self.screen = screen
        
    # Define a method to simulate a dice roll
    def roll(self):
        # Play the dice roll sound effect
        self.sound.play()

        # Loop through the images of the dice to simulate rolling
        for img in self.images:
            self.image = img
            self.image2 = img

            # Draw the updated sprite on the screen
            self.draw()
            pygame.display.flip()

            # Wait for a short amount of time before updating the sprite again
            pygame.time.wait(50)

        # Select a random number between 1 and 6 for the dice roll
        self.number = random.randint(1, 6)
        self.image = self.images[self.number - 1]

        self.number2 = random.randint(1, 6)
        self.image2 = self.images[self.number2 - 1]

        # Draw the updated sprite on the screen
        self.draw()

    # Define a method to update the sprite on the screen
    def update(self):
        self.draw()
        
    # Define a method to draw the sprite on the screen
    def draw(self):
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.image2, self.rect2)

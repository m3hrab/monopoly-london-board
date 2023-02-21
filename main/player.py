import pygame

class MonopolyPlayer():

    def __init__(self, name, image, x, y):
        # Initialize the properties of a player
        self.name = name
        self.money = 1500
        self.properties = []
        self.in_jail = False
        self.jail_turns = 0
        self.token_image = image  
        self.token_rect = self.token_image.get_rect()
        self.current_player = 0

        # Set the position of the token on the board
        self.token_rect.right = x 
        self.token_rect.bottom = y

    # Define a function to draw the token on the screen 
    def draw(self):
        self.screen.blit(self.token_image, self.token_rect)

    # Define a function to move the token on the board
    def move(self, dice_roll):
        pass

    # Define a function to move the token on the board with an animation
    def move_token_animation(self, surface, x, y, speed=5):
        # Calculate the destination position for the token
        dest_x, dest_y = self.get_token_position()

        # Determine the direction of movement
        dx = 1 if dest_x > x else -1
        dy = 1 if dest_y > y else -1

        # Animate the movement of the token
        while x != dest_x or y != dest_y:
            x += dx * speed
            y += dy * speed
            surface.blit(self.token_image, (x, y))
            pygame.display.update()
            pygame.time.wait(50)

    # Define a function to get the current position of the token on the board
    def get_token_position(self):
        row, col = self.get_row_col(self.position)

        if row == 0:
            return (90 + col * 65, 560)
        elif row == 1:
            return (810, 90 + col * 65)
        elif row == 2:
            return (710 - col * 65, 40)
        elif row == 3:
            return (90, 690 - col * 65)

    # Define a function to get the row and column of a cell based on its position on the board
    def get_row_col(self, position):
        if position < 10:
            return (0, position)
        elif position < 20:
            return (1, position - 10)
        elif position < 30:
            return (2, position - 20)
        else:
            return (3, position - 30)
        
    # Define a function to subtract rent from player's money
    def pay_rent(self, rent):
        self.money -= rent

    # Define a function to add a property to the player's list of properties and subtract the price from their money
    def buy_property(self, property):
        self.properties.append(property)
        self.money -= property.price

    # Define a function to remove a property from the player's list of properties and add the price to their money
    def sell_property(self, property):
        self.properties.remove(property)
        self.money += property.price

    # Define a function to calculate the total value of the player's assets
    def get_assets_value(self):
        assets_value = self.money
        for property in self.properties:
            assets_value += property.price
            if property.is_mortgaged:
                assets_value -= property.mortgage_value
        return assets_value

    




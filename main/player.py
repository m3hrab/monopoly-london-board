import pygame

class MonopolyPlayer():

    def __init__(self, name, image, position):
        self.name = name
        self.money = 1500
        self.properties = []
        self.in_jail = False
        self.jail_turns = 0
        self.position = position
        self.token_image = image  
        self.token_rect = self.token_image.get_rect()

    def draw(self):
        self.screen.blit(self.token_image, self.token_rect)

    def move(self, dice_roll):
        pass

    def move_token_animation(self, surface, x, y, speed=5):
        dest_x, dest_y = self.get_token_position()
        dx = 1 if dest_x > x else -1
        dy = 1 if dest_y > y else -1

        while x != dest_x or y != dest_y:
            x += dx * speed
            y += dy * speed
            surface.blit(self.token_image, (x, y))
            pygame.display.update()
            pygame.time.wait(50)

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

    def get_row_col(self, position):
        if position < 10:
            return (0, position)
        elif position < 20:
            return (1, position - 10)
        elif position < 30:
            return (2, position - 20)
        else:
            return (3, position - 30)
        


    def pay_rent(self, rent):
        self.money -= rent

    def buy_property(self, property):
        self.properties.append(property)
        self.money -= property.price

    def sell_property(self, property):
        self.properties.remove(property)
        self.money += property.price

    def get_assets_value(self):
        assets_value = self.money
        for property in self.properties:
            assets_value += property.price
            if property.is_mortgaged:
                assets_value -= property.mortgage_value
        return assets_value

  




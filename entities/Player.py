# from entities.Entity import Entity
from .Entity import Entity
from settings.keyboard_layout import keybinds_player1, keybinds_player2
import pygame

class Player(Entity):
    def __init__(self, x, y, main, keybinds):
        super().__init__(x, y, 15 , 25, solid=True)
        self.__main = main
        self.__texture = pygame.image.load("assets/textures/entities/player/eyes_open.png").convert_alpha()
        # Nick - movement + physics
        self.velocity_y = 0
        self.on_ground = True
        self.gravity = 1
        self.speed = 5
        if keybinds == 1:
            self.controls = keybinds_player1()
        else:
            self.controls = keybinds_player2()
    def get_texture(self):
        return self.__texture
    
    def move(self, keys):
        if keys[self.controls["left"]]:
            self.set_x(self.get_x() - self.speed)
        if keys[self.controls["right"]]:
            self.set_x(self.get_x() + self.speed)   

    def jump(self):
        if self.on_ground:
            self.velocity_y = -20
            self.on_ground = False

    def apply_gravity(self):
        self.velocity_y += self.gravity
        self.set_y(self.get_y() + self.velocity_y)

    def game_loop(self, delta_time, events):
        # Continue acties (elke frame)
        keys = pygame.key.get_pressed()
        self.move(keys)
        self.apply_gravity()

        # Eenmalige acties (per event)
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == self.controls["jump"]:
                    self.jump()

    def run_with_delay(self):
        print("value")
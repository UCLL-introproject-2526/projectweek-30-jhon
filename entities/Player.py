from entities.Entity import Entity
import pygame

class Player(Entity):
    def __init__(self, x, y, main):
        super().__init__(x, y, 15 , 25, solid=True)
        self.__main = main
        self.__texture = pygame.image.load("assets/textures/entities/player/eyes_open.png").convert_alpha()
        # Nick - movement + physics
        self.velocity_y = 0
        self.on_ground = False
        
        self.gravity = 1
    def get_texture(self):
        return self.__texture

    def game_loop(self):
        pass
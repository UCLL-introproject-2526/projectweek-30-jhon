from entities.Entity import Entity
import pygame

class Player(Entity):
    def __init__(self, x, y, main):
        super().__init__(x, y, 15 , 25, solid=True)
        self.__main = main
        self.__texture = pygame.image.load("assets/textures/entities/player/eyes_open.png").convert_alpha()

    def get_texture(self):
        return self.__texture

    def game_loop(self, past_time):
        print("Player game loop...")
        self.__main.add_later_task(self.run_with_delay, 10)
        pass

    def run_with_delay(self):
        print("value")

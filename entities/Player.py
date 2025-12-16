from entities.Entity import Entity
import pygame

class Player(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, 15 , 25, solid=True)
        self.__texture = pygame.image.load("assets/textures/entities/player/eyes_open.png").convert_alpha()
        # Nick - movement + physics
        self.velocity_y = 0
        self.on_ground = False
        
        self.gravity = 1
    def get_texture(self):
        return self.__texture

    # def game_loop(self):
    #     pass


    # Nick -movement + physics

    def move(self, keys):
        if keys[self.controls["left"]]:
            self.rect.x -= self.speed
        if keys[self.controls["right"]]:
            self.rect.x += self.speed

    def jump(self):
        if self.on_ground:
            self.velocity_y = -25
            self.on_ground = False

    def apply_gravity(self):
        self.velocity_y += self.gravity
        # wij gebruiken geen rect hier, maar de x en y van de entity
        # self.rect.y += self.velocity_y
        self.set_y(self.get_y() + self.velocity_y) 


    def game_loop(self, keys):
        self.move(keys)
        self.apply_gravity()
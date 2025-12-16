import pygame

from tools.importer import image

class Entity:
    def __init__(self, x, y, width, height, main, solid=True, texture=None, gravitation = False, weight = 10, bounce = 0):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.__solid = solid
        self.__texture = texture
        self.__gravitation = gravitation
        self.__bounce = bounce
        self.__speed_x = 0
        self.__speed_y = 0
        self.__main = main
        if texture:
            self.set_texture(texture)

    def is_solid(self):
        return self.__solid

    def set_solid(self, solid):
        self.__solid = solid

    def set_height(self, height):
        self.__height = height

    def get_texture(self):
        return self.__texture
    
    def set_texture(self, texture):
        self.__texture = image(f"assets/textures/entities/{texture}")

    def get_render_data(self):
        return self.__x, self.__y, self.__width, self.__height
    
    def get_x(self):
        return self.__x
    
    def set_x(self, x):
        self.__x = x

    def get_y(self):
        return self.__y
    
    def set_y(self, y):
        self.__y = y

    def collision(self, other):
        x1, y1, w1, h1 = self.get_render_data()
        x2, y2, w2, h2 = other.get_render_data()

        return (
            x1 < x2 + w2 and
            x1 + w1 > x2 and
            y1 < y2 + h2 and
            y1 + h1 > y2
        )

    def moveee(self, delta_time):
        if self.__gravitation:
            self.__speed_y += self.__width * delta_time
        self.__y += self.__speed_y
        self.__x += self.__speed_x

        for other in self.__main.get_current_map().get_entities():
            if other is self or not other.is_solid():
                continue

            if self.collision(other):
                ex, ey, ew, eh = other.get_render_data()

                if self.__speed_x > 0:
                    # Von links kommend
                    self.__x = ex - self.__width
                elif self.__speed_x < 0:
                    # Von rechts kommend
                    self.__x = ex + ew

                self.__speed_x *= -self.__bounce

        self.__y += self.__speed_y * delta_time

        for entity in self.__main.get_current_map().get_entities():
            if entity is self or not entity.is_solid():
                continue

            if self.collision(entity):
                ex, ey, ew, eh = entity.get_render_data()

                if self.__speed_y > 0:
                    self.__y = ey - self.__height
                elif self.__speed_y < 0:
                    self.__y = ey + eh

                self.__speed_y *= -self.__bounce


    def game_loop(self, past_time, events):
        print("Entiry game loop...")
        pass
    



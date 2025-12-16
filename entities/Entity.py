import pygame

from tools.importer import image

class Entity:
    def __init__(self, x, y, width, height, main, solid=True, texture=None, gravitation = False, weight = 10):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.__solid = solid
        self.__texture = texture
        self.__gravitation = gravitation
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

    def colishion(self, other):
        pass

    def move(self, other, delta_time):
        if self.__gravitation:
            self.__speed_y -= self.__width * delta_time
        self.__y += self.__speed_y
        self.__x += self.__speed_x

    def game_loop(self, past_time, events):
        print("Entiry game loop...")
        pass
    



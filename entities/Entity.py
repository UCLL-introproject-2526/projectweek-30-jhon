import pygame

class Entity:
    def __init__(self, x, y, width, height, solid=True, texture=None):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.__solid = solid
        self.__texture = texture
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
        self.__texture = pygame.image.load(f"assets/textures/entities/{texture}").convert_alpha()

    def get_render_data(self):
        return self.__x, self.__y, self.__width, self.__height

    def game_loop(self):
        pass
import pygame

from tools.importer import image


class TextureLibrary:
    def __init__(self):
        self.textures = []


class Texture:
    def __init__(self, name, texture):
        self.__name = name
        self.__texture = texture

    def read_texture(self, texture):
        self.__texture = image(f'entities/{texture}')

    def get_texture(self):
        return self.__texture

    def get_name(self):
        return self.__name
import pygame

class Map:
    def __init__(self, name, width, height):
        self.__width = width
        self.__height = height
        self.image = pygame.image.load(f"assets/textures/background/{name}.png").convert_alpha()
        self.entities = []


    def add_entity(self, entity):
        if entity not in self.entities:
            self.entities.append(entity)

    def remove_entity(self, entity):
        if entity in self.entities:
            self.entities.remove(entity)

    def get_range(self):
        return self.__width, self.__height
    
    def get_image(self):
        return self.image
    
    def get_entities(self):
        return self.entities

    def get_height(self):
        return self.__height

    def get_width(self):
        return self.__width

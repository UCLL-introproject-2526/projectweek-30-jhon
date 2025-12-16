import pygame

class Map:
    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height
        self.image = pygame.image.load(f"assets/textures/background/{name}.png").convert_alpha()
        self.entities = []


    def add_entity(self, entity):
        if entity not in self.entities:
            self.entities.append(entity)

    def remove_entity(self, entity):
        if entity in self.entities:
            self.entities.remove(entity)

    def get_range(self):
        return (self.width, self.height)
    
    def get_image(self):
        return self.image
    
    def get_entities(self):
        return self.entities

import pygame
from entities.Entity import Entity

class TextEntity(Entity):
    def __init__(self, x, y, text, main, color=(255, 255, 255), size=36, bounce=False, fade=False, center=False):
        super().__init__(x, y, 0, 0, main)
        self.text = text
        self.color = color
        self.size = size
        self.__center = center
        self.__base_x = x
        self.__create_texture()
        
    def __create_texture(self):
        font = pygame.font.Font(None, self.size)
        self.__render_surface = font.render(self.text, True, self.color)
        self.width = self.__render_surface.get_width()
        self.height = self.__render_surface.get_height()
        
        if self.__center:
            self.x = self.__base_x - (self.width // 2)
    
    def get_texture(self):
        return self.__render_surface

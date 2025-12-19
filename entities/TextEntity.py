import pygame
from entities.Entity import Entity
from tools.ImageLibary import image_library


class TextEntity(Entity):
    def __init__(self, x, y, main, text, color, id=None, has_bg=False):
        super().__init__(x, y, 120 , 20, main, id=id)
        self.text = text
        self.color = color
        self.main = main
        self.__img = 'entities/button/long_button.png' if has_bg else 'entities/text/long_button.png'

    def get_texture(self):
        font = pygame.font.SysFont('Arial', 100)
        surface = image_library.get_image(self.__img).copy()
        text_surface = font.render(self.text, True, self.color)
        text_rect = text_surface.get_rect(center=surface.get_rect().center)
        surface.blit(text_surface, text_rect)
        return surface

    def set_text(self, text):
        self.text = text

    def set_color(self, color):
        self.color = color
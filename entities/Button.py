import pygame
from entities.Entity import Entity
from tools.Loop_controller import Loop_controller
from tools.importer import image


class Button(Entity):
    def __init__(self, x, y, main, texture, text, color, bg_color, id=None):
        super().__init__(x, y, 100, 30, main, texture=texture, id=id)
        self.text = text
        self.color = color
        self.main = main
        self.bg_color = bg_color
        self.__clicked = False
        self.bg_img = image('entities/button/mylongbutton.png')

    def is_clicked(self):
        mouse_pos = self.main.get_mouse_pos()
        if mouse_pos is None:
            return False
        if (self.x <= mouse_pos[0] <= self.x + self.width and
            self.y <= mouse_pos[1] <= self.y + self.height) and self.__clicked == False:
            if pygame.mouse.get_pressed()[0]:
                self.__clicked = True
                return True
        if not pygame.mouse.get_pressed()[0]:
            self.__clicked = False
        return False


    def reset_click(self):
        self.__clicked = False

    def get_texture(self):
        font = pygame.font.SysFont('Arial', 160, bold=True)
        surface = self.bg_img.copy()
        text_surface = font.render(self.text, True, (74, 39, 10))
        text_rect = text_surface.get_rect(center=surface.get_rect().center)
        surface.blit(text_surface, text_rect)
        return surface
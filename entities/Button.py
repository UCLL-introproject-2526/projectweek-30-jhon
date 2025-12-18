import pygame
from entities.Entity import Entity
from tools.Loop_controller import Loop_controller
from tools.importer import image


class Button(Entity):
    def __init__(self, x, y, main, text, color = (74, 39, 10), id=None, is_big=True):
        super().__init__(x, y, 120 if is_big else 38, 24, main, id=id)
        self.__save_x = x
        self.__save_y = y
        self.text = text
        self.color = color
        self.main = main
        self.bg_color = bg_color
        self.__clicked = False
        self.__is_big = is_big
        self.imagessssiooo = [
            image('entities/button/long_button.png'),
            image('entities/button/small_button.png')
        ]

    def is_clicked(self):
        mouse_pos = self.main.get_mouse_pos()
        if mouse_pos is None:
            return False
        if (self.x + 3 < mouse_pos[0] < self.x + self.width - 3 and
            self.y + 3 < mouse_pos[1] < self.y + self.height - 3) and self.__clicked == False:
            self.y = self.__save_y - 2
            self.x = self.__save_x - 9
            self.width =  138 if self.__is_big else 44
            self.height = 28

            if pygame.mouse.get_pressed()[0]:
                self.__clicked = True
                return True
        else:
            self.y = self.__save_y
            self.x = self.__save_x
            self.width =  120 if self.__is_big else 38
            self.height = 24
        if not pygame.mouse.get_pressed()[0]:
            self.__clicked = False
        return False


    def reset_click(self):
        self.__clicked = False

    def get_img(self):
        return  self.imagessssiooo[0] if self.__is_big else self.imagessssiooo[1]

    def get_texture(self):
        font = pygame.font.SysFont('Arial', 130, bold=True)
        surface = self.get_img().copy()
        text_surface = font.render(self.text, True, self.color)
        text_rect = text_surface.get_rect(center=surface.get_rect().center)
        surface.blit(text_surface, text_rect)
        return surface
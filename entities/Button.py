import pygame
from entities.Entity import Entity
from tools.Loop_controller import Loop_controller

class Button(Entity):
    def __init__(self, x, y, width, height, main, texture, text, color, bg_color):
        super().__init__(x, y, width, height, main, texture=texture)
        self.text = text
        self.color = color
        self.main = main
        self.bg_color = bg_color

    def is_clicked(self):
        mouse_pos = self.main.get_mouse_pos()
        if (self.x <= mouse_pos[0] <= self.x + self.width and
            self.y <= mouse_pos[1] <= self.y + self.height):
            if pygame.mouse.get_pressed()[0]:
                return True
        return False

    def get_texture(self):
        font = pygame.font.SysFont('Arial', 30)
        return font.render(self.text, True, self.color, self.bg_color)

    def game_loop(self, past_time, events):
        mouse_pos = self.main.get_mouse_pos()
        if self.is_clicked():
            print('TTEEEESSST')
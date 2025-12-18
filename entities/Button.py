import pygame
from entities.Entity import Entity
from tools.Loop_controller import Loop_controller

class Button(Entity):
    def __init__(self, x, y, width, height, main, texture, text, color):
        super().__init__(x, y, width, height, main, texture=texture)
        self.text = text
        self.color = color

    def __get_screen_area(self, map_obj):
        window_width = 600
        window_height = 260
        current_map_width, current_map_height = map_obj.get_range()

        window_aspect_ratio = window_width / window_height
        map_aspect_ratio = current_map_width / current_map_height

        offset_x = 0
        offset_y = 0
        if window_aspect_ratio > map_aspect_ratio:
            screen_height = window_height
            screen_width = int(map_aspect_ratio * screen_height)
            offset_x = (window_width - screen_width) // 2
        else:
            screen_width = window_width
            screen_height = int(screen_width / map_aspect_ratio)
            offset_y = (window_height - screen_height) // 2
        return offset_x, offset_y, screen_width, screen_height
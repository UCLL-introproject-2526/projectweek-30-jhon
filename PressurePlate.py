import pygame
from entities.Entity import Entity

class PressurePlate(Entity):
    def __init__ (self, x, y, main):
        super().__init__(x, y, 20, 20, main,solid=True,texture="block_models/platform.png")
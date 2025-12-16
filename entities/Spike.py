import pygame
from entities.Entity import Entity

class Spike(Entity):
    def __init__ (self, x, y, main):
        super().__init__(x, y, 20, 20, main,solid=False,texture="block_models/Spike_model.png")
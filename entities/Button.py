import pygame
from entities.Entity import Entity
class Button(Entity):
    def __init__(self, x, y, width, height, texture=None):
        super().__init__(x, y, width, height, solid=False, texture=texture)
    
    
    


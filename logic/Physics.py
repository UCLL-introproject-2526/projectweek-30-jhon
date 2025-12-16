import pygame
from entities.Entity import Entity

class Physics:
    def __init__(self, gravity=1):
        self.gravity = gravity

    def apply_gravity(self, entity):
        x, y, width, height = entity.get_render_data()
        entity.set_height(height + self.gravity)
    
    def get_gravity(self):
        return self.gravity
import pygame
from entities.Entity import Entity
from entities.Player import Player

class Spike(Entity):
    def __init__ (self, x, y, main):
        super().__init__(x, y, 20, 20, main,solid=False,texture="block_models/Spike_model.png", name="Spike")
        self._main = main
        self._active = True
    
    def set_active(self, active: bool):
        self._active = bool(active)

    def is_active(self):
        return self._active

    def get_texture(self):
        # Hide texture when inactive so render skips it
        if not self._active:
            return None
        return super().get_texture()

    def game_loop(self, delta_time, events):

        """Check collision with players (instant death -> restart level)"""
        if not self._active:
            return

        sx, sy, sw, sh = self.get_render_data()
        
        for entity in self._main.get_current_map().get_entities():
            if hasattr(entity, '__class__') and entity.__class__.__name__ == 'Player':
                px, py, pw, ph = entity.get_render_data()
                if (px < sx + sw and px + pw > sx and py < sy + sh and py + ph > sy):
                    self._main.restart_map()
                    return
            
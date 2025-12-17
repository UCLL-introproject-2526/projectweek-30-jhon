import pygame
from entities.Entity import Entity
from tools.importer import image

class PressurePlate(Entity):
    def __init__(self, x, y, main, width=20, height=10):
        """PressurePlate uses a fixed unpressed texture 'block_models/pressureplate_in.png'.
        The activated texture is always 'assets/textures/pressureplate_out.png'.
        """
        super().__init__(x, y, width, height, main, solid=False, texture=None)
        self.main_ref = main
        self.activated = False
        self.unpressed_texture_path = "block_models/pressureplate_in.png"
        # Always use this activated texture (entity-relative path)
        self.activated_texture_path = "block_models/pressureplate_out.png"

        # set initial unpressed texture (may raise if missing)
        self.set_texture(self.unpressed_texture_path)

    def activate(self):
        if self.activated:
            return
        self.activated = True
        # change texture to the fixed activated texture (entity-relative)
        self.set_texture(self.activated_texture_path)

        # remove all spikes from current map
        current_entities = list(self.main_ref.get_current_map().get_entities())
        spikes = [e for e in current_entities if hasattr(e, '__class__') and e.__class__.__name__ == 'Spike']
        for s in spikes:
            self.main_ref.get_current_map().remove_entity(s)

    def game_loop(self, delta_time, events):
        if self.activated:
            return
        # Check if any player is on the plate
        for e in self.main_ref.get_current_map().get_entities():
            if hasattr(e, '__class__') and e.__class__.__name__ == 'Player':
                if self.collision(e):
                    self.activate()
                    return

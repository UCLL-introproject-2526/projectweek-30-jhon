import pygame
from entities.Entity import Entity

class PressurePlate(Entity):
    def __init__(self, x, y, main, width=20, height=10):
        """PressurePlate uses a fixed unpressed texture 'block_models/pressureplate_in.png'.
        The activated texture is always 'block_models/pressureplate_out.png'.
        Plate deactivates again when no player stands on it.
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

        # deactivate all spikes on the current map
        for e in list(self.main_ref.get_current_map().get_entities()):
            if hasattr(e, '__class__') and e.__class__.__name__ == 'Spike' and hasattr(e, 'set_active'):
                e.set_active(False)

    def deactivate(self):
        if not self.activated:
            return
        self.activated = False
        # restore unpressed texture
        self.set_texture(self.unpressed_texture_path)

        # reactivate all spikes on the current map
        for e in list(self.main_ref.get_current_map().get_entities()):
            if hasattr(e, '__class__') and e.__class__.__name__ == 'Spike' and hasattr(e, 'set_active'):
                e.set_active(True)

    def game_loop(self, delta_time, events):
        # check whether any player is currently standing on the plate
        player_on_plate = False
        for e in self.main_ref.get_current_map().get_entities():
            if hasattr(e, '__class__') and e.__class__.__name__ == 'Player':
                if self.collision(e):
                    player_on_plate = True
                    break

        if player_on_plate:
            self.activate()
        else:
            self.deactivate()

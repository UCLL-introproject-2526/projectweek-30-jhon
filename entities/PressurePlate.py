import pygame
from entities.Entity import Entity

class PressurePlate(Entity):
    def __init__(self, x, y, main, width=20, height=10, remove_target=None):
        """PressurePlate uses a fixed unpressed texture 'block_models/pressureplate_in.png'.
        The activated texture is always 'block_models/pressureplate_out.png'.
        Plate deactivates again when no player stands on it.
        """
        super().__init__(x, y, width, height, main, solid=False, texture=None, name="PressurePlate")
        self.main_ref = main
        self.activated = False
        # Optional: remove a specific entity (e.g., a Wall) on first activation
        self.remove_target = remove_target
        self._removed_done = False
        self.unpressed_texture_path = "block_models/pressureplate_out.png"
        # Always use this activated texture (entity-relative path)
        self.activated_texture_path = "block_models/pressureplate_in.png"

        # set initial unpressed texture (may raise if missing)
        self.set_texture(self.unpressed_texture_path)

    def activate(self):
        if self.activated:
            return
        self.activated = True
        # change texture to the fixed activated texture (entity-relative)
        self.set_texture(self.activated_texture_path)

        # Remove only spikes explicitly marked as removable
        for e in list(self.main_ref.get_current_map().get_entities()):
            if hasattr(e, '__class__') and e.__class__.__name__ == 'Spike':
                # check explicit removable flag
                if hasattr(e, 'is_removable') and e.is_removable():
                    self.main_ref.get_current_map().remove_entity(e)

        # One-shot removal of the configured target (e.g., a Wall)
        if self.remove_target is not None and not self._removed_done:
            self.main_ref.get_current_map().remove_entity(self.remove_target)
            self._removed_done = True

    def deactivate(self):
        if not self.activated:
            return
        self.activated = False
        # restore unpressed texture
        self.set_texture(self.unpressed_texture_path)
        # No spike reactivation: non-removable spikes were untouched; removable ones were removed

        # If we previously removed the target wall, add it back when the plate is released
        if self.remove_target is not None and self._removed_done:
            current_map = self.main_ref.get_current_map()
            # Only add back if it's not already present
            if self.remove_target not in current_map.get_entities():
                current_map.add_entity(self.remove_target)
            self._removed_done = False

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

import pygame
from entities.Entity import Entity

class PressurePlate(Entity):
    def __init__(self, x, y, main, width=20, height=10, remove_target=None, add_target=None, remove_spikes=False):
        """PressurePlate uses a fixed unpressed texture 'block_models/pressureplate_in.png'.
        The activated texture is always 'block_models/pressureplate_out.png'.
        Plate deactivates again when no player stands on it.
        """
        super().__init__(x, y, width, height, main, solid=False, texture=None, name="PressurePlate")
        self.main_ref = main
        self.activated = False
        # Optional: remove a specific entity (e.g., a Wall) on first activation
        # Store position for dynamic lookup to survive map rebuilds
        self.remove_target = remove_target
        self._removed_done = False
        # Optional: add a wall when activated
        self.add_target = add_target
        self._added_done = False
        # Only remove spikes if explicitly enabled
        self.remove_spikes = remove_spikes
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

        # Remove only spikes explicitly marked as removable (only if this plate is configured to remove spikes)
        if self.remove_spikes:
            for e in list(self.main_ref.get_current_map().get_entities()):
                if hasattr(e, '__class__') and e.__class__.__name__ == 'Spike':
                    # check explicit removable flag
                    if hasattr(e, 'is_removable') and e.is_removable():
                        self.main_ref.get_current_map().remove_entity(e)

        # One-shot removal of the configured target (e.g., a Wall)
        # Search by position to handle map rebuilds where the object reference changes
        if self.remove_target is not None and not self._removed_done:
            target_x = self.remove_target.get_x()
            target_y = self.remove_target.get_y()
            for e in list(self.main_ref.get_current_map().get_entities()):
                if hasattr(e, '__class__') and e.__class__.__name__ == 'Wall':
                    if e.get_x() == target_x and e.get_y() == target_y:
                        self.main_ref.get_current_map().remove_entity(e)
                        self._removed_done = True
                        break

        # Add a wall when activated
        if self.add_target is not None and not self._added_done:
            target_x, target_y, target_w, target_h = self.add_target.get_render_data()
            current_map = self.main_ref.get_current_map()
            # Check if wall at that position already exists
            wall_exists = False
            for e in current_map.get_entities():
                if hasattr(e, '__class__') and e.__class__.__name__ == 'Wall':
                    if e.get_x() == target_x and e.get_y() == target_y:
                        wall_exists = True
                        break
            if not wall_exists:
                # Add the wall
                from entities.Wall import Wall
                new_wall = Wall(target_x, target_y, target_w, target_h, self.main_ref)
                current_map.add_entity(new_wall)
                self.add_target = new_wall
                self._added_done = True

    def deactivate(self):
        if not self.activated:
            return
        self.activated = False
        # restore unpressed texture
        self.set_texture(self.unpressed_texture_path)
        # No spike reactivation: non-removable spikes were untouched; removable ones were removed

        # If we previously removed the target wall, add it back when the plate is released
        if self.remove_target is not None and self._removed_done:
            target_x, target_y, target_w, target_h = self.remove_target.get_render_data()
            current_map = self.main_ref.get_current_map()
            # Check if wall at that position exists; if not, recreate it
            wall_exists = False
            for e in current_map.get_entities():
                if hasattr(e, '__class__') and e.__class__.__name__ == 'Wall':
                    if e.get_x() == target_x and e.get_y() == target_y:
                        wall_exists = True
                        break
            if not wall_exists:
                # Recreate the wall at the same position
                from entities.Wall import Wall
                new_wall = Wall(target_x, target_y, target_w, target_h, self.main_ref)
                current_map.add_entity(new_wall)
                # Update reference for next cycle
                self.remove_target = new_wall
            self._removed_done = False

        # If we previously added the target wall, remove it when the plate is released
        if self.add_target is not None and self._added_done:
            target_x, target_y, target_w, target_h = self.add_target.get_render_data()
            current_map = self.main_ref.get_current_map()
            # Find and remove the wall at that position
            for e in list(current_map.get_entities()):
                if hasattr(e, '__class__') and e.__class__.__name__ == 'Wall':
                    if e.get_x() == target_x and e.get_y() == target_y:
                        current_map.remove_entity(e)
                        break
            self._added_done = False

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

from entities.Entity import Entity

class PressurePlate(Entity):
    # 1. Voeg 'permanent=False' toe aan de parameters hieronder
    def __init__(self, x, y, main, width=20, height=10, remove_target=None, add_target=None, remove_spikes=False, permanent=False):
        super().__init__(x, y, width, height, main, solid=False, texture=None, name="PressurePlate")
        self.main_ref = main
        self.activated = False
        
        self.remove_target = remove_target
        self._removed_done = False
        self.add_target = add_target
        self._added_done = False
        self.remove_spikes = remove_spikes
        
        # 2. Sla de instelling op
        self.permanent = permanent

        self.unpressed_texture_path = "block_models/pressureplate_out.png"
        self.activated_texture_path = "block_models/pressureplate_in.png"
        self.set_texture(self.unpressed_texture_path)

    def activate(self):
        if self.activated:
            return
        self.activated = True
        self.set_texture(self.activated_texture_path)

        # Remove Spikes
        if self.remove_spikes:
            for e in list(self.main_ref.get_current_map().get_entities()):
                if hasattr(e, '__class__') and e.__class__.__name__ == 'Spike':
                    if hasattr(e, 'is_removable') and e.is_removable():
                        self.main_ref.get_current_map().remove_entity(e)

        # Remove Target Wall
        if self.remove_target is not None and not self._removed_done:
            target_x = self.remove_target.get_x()
            target_y = self.remove_target.get_y()
            for e in list(self.main_ref.get_current_map().get_entities()):
                if hasattr(e, '__class__') and e.__class__.__name__ == 'Wall':
                    if e.get_x() == target_x and e.get_y() == target_y:
                        self.main_ref.get_current_map().remove_entity(e)
                        self._removed_done = True
                        break

        # Add Target Wall
        if self.add_target is not None and not self._added_done:
            target_x, target_y, target_w, target_h = self.add_target.get_render_data()
            current_map = self.main_ref.get_current_map()
            wall_exists = False
            for e in current_map.get_entities():
                if hasattr(e, '__class__') and e.__class__.__name__ == 'Wall':
                    if e.get_x() == target_x and e.get_y() == target_y:
                        wall_exists = True
                        break
            if not wall_exists:
                from entities.Wall import Wall
                new_wall = Wall(target_x, target_y, target_w, target_h, self.main_ref)
                current_map.add_entity(new_wall)
                self.add_target = new_wall
                self._added_done = True

    def deactivate(self):
        if not self.activated:
            return
        self.activated = False
        self.set_texture(self.unpressed_texture_path)

        # 3. HIER IS DE LOGICA:
        if self.remove_target is not None and self._removed_done and not self.permanent:
            target_x, target_y, target_w, target_h = self.remove_target.get_render_data()
            current_map = self.main_ref.get_current_map()
            wall_exists = False
            for e in current_map.get_entities():
                if hasattr(e, '__class__') and e.__class__.__name__ == 'Wall':
                    if e.get_x() == target_x and e.get_y() == target_y:
                        wall_exists = True
                        break
            if not wall_exists:
                from entities.Wall import Wall
                new_wall = Wall(target_x, target_y, target_w, target_h, self.main_ref)
                current_map.add_entity(new_wall)
                self.remove_target = new_wall
            self._removed_done = False

        if self.add_target is not None and self._added_done:
            target_x, target_y, target_w, target_h = self.add_target.get_render_data()
            current_map = self.main_ref.get_current_map()
            for e in list(current_map.get_entities()):
                if hasattr(e, '__class__') and e.__class__.__name__ == 'Wall':
                    if e.get_x() == target_x and e.get_y() == target_y:
                        current_map.remove_entity(e)
                        break
            self._added_done = False

    def game_loop(self, delta_time, events):
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
import pygame
from entities.Entity import Entity

class PlayerMerge(Entity):
    """Detects when both players touch anywhere and merges them"""
    def __init__(self, main, next_level_callback):
        super().__init__(0, 0, 0, 0, main, solid=False, name="PlayerMerge")
        self._main = main
        self.next_level_callback = next_level_callback
        self.merge_triggered = False
        self.merge_timer = 0.5
    
    def get_texture(self):
        return None
    
    def game_loop(self, delta_time, events):
        """Check if players are touching"""
        if self.merge_triggered:
            self.merge_timer -= delta_time
            if self.merge_timer <= 0:
                self.next_level_callback()
            return
        
        players = []
        
        # Find all players
        for entity in self._main.get_current_map().get_entities():
            if hasattr(entity, '__class__') and entity.__class__.__name__ == 'Player':
                players.append(entity)
        
        # If both players exist, check if they're touching
        if len(players) >= 2:
            p1_x, p1_y, p1_w, p1_h = players[0].get_render_data()
            p2_x, p2_y, p2_w, p2_h = players[1].get_render_data()
            
            # AABB collision
            if (p1_x < p2_x + p2_w and
                p1_x + p1_w > p2_x and
                p1_y < p2_y + p2_h and
                p1_y + p1_h > p2_y):
                
                print("🎉 MERGE! Players touched!")
                self.merge_triggered = True

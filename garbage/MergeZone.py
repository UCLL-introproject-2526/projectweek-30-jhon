import pygame
from entities.Entity import Entity

class MergeZone(Entity):
    """Merges both players when they touch"""
    def __init__(self, x, y, width, height, main, next_level_callback):
        super().__init__(x, y, width, height, main, solid=False)
        self.next_level_callback = next_level_callback
        self.merge_triggered = False
        self.merge_timer = 0
        self.merge_duration = 0.5
        self._main = main
    
    def get_texture(self):
        """Pulsing merge zone"""
        x, y, width, height = self.get_render_data()
        surface = pygame.Surface((width, height))
        
        # Pulsing effect
        pulse = int(128 + 100 * abs(pygame.time.get_ticks() % 1000 - 500) / 500)
        surface.fill((100, 200, 255))
        surface.set_alpha(pulse)
        return surface
    
    def game_loop(self, delta_time, events):
        """Check if both players are in merge zone"""
        if self.merge_triggered:
            self.merge_timer -= delta_time
            if self.merge_timer <= 0:
                self.next_level_callback()
            return
        
        zone_x, zone_y, zone_width, zone_height = self.get_render_data()
        players = []
        
        # Find all players
        for entity in self._main.get_current_map().get_entities():
            if hasattr(entity, '__class__') and entity.__class__.__name__ == 'Player':
                player_x, player_y, player_width, player_height = entity.get_render_data()
                
                # Check if player is in merge zone
                if (zone_x < player_x + player_width and
                    zone_x + zone_width > player_x and
                    zone_y < player_y + player_height and
                    zone_y + zone_height > player_y):
                    players.append(entity)
        
        # If both players are in zone, merge!
        if len(players) >= 2:
            print("🎉 MERGE! Both players combined!")
            self.merge_triggered = True
            self.merge_timer = self.merge_duration

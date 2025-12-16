import pygame
from entities.Entity import Entity

class GoalArea(Entity):
    def __init__(self, x, y, width, height, main, next_level_callback):
        super().__init__(x, y, width, height, main, solid=False)
        self.next_level_callback = next_level_callback
        self.triggered = False
        self._main = main
    
    def get_texture(self):
        """Green glowing goal area"""
        surface = pygame.Surface((self.get_render_data()[2], self.get_render_data()[3]))
        surface.fill((0, 255, 100))
        surface.set_alpha(128)  # Semi-transparent
        return surface
    
    def game_loop(self, delta_time, events):
        """Check if any player reached the goal"""
        if self.triggered:
            return
        
        goal_x, goal_y, goal_width, goal_height = self.get_render_data()
        
        for entity in self._main.get_current_map().get_entities():
            if hasattr(entity, '__class__') and entity.__class__.__name__ == 'Player':
                player_x, player_y, player_width, player_height = entity.get_render_data()
                
                # Check collision with goal area
                if (goal_x < player_x + player_width and
                    goal_x + goal_width > player_x and
                    goal_y < player_y + player_height and
                    goal_y + goal_height > player_y):
                    
                    print("🎉 GOAL REACHED! Moving to next level...")
                    self.triggered = True
                    self.next_level_callback()
                    break

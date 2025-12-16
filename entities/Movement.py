import pygame

class Movement:
    """Standalone movement system for players"""
    
    @staticmethod
    def handle_movement(player, keys):
        """Handle left/right movement"""
        if keys[player.controls["left"]]:
            player.set_x(player.get_x() - player.speed)
        if keys[player.controls["right"]]:
            player.set_x(player.get_x() + player.speed)
    
    @staticmethod
    def handle_gravity(player):
        """Apply gravity to player"""
        player.velocity_y += player.gravity
        if player.velocity_y > 10:
            player.velocity_y = 10  # Terminal velocity
        player.set_y(player.get_y() + player.velocity_y)
    
    @staticmethod
    def handle_jump(player):
        """Jump if on ground"""
        if player.on_ground:
            player.velocity_y = -15
            player.on_ground = False
    
    @staticmethod
    def check_wall_collisions(player, main):
        """Check collision with walls"""
        player.on_ground = False
        player_x, player_y, player_width, player_height = player.get_render_data()
        
        for entity in main.get_current_map().get_entities():
            if hasattr(entity, '__class__') and entity.__class__.__name__ == 'Wall':
                wall_x, wall_y, wall_width, wall_height = entity.get_render_data()
                
                # AABB collision
                if (player_x < wall_x + wall_width and
                    player_x + player_width > wall_x and
                    player_y < wall_y + wall_height and
                    player_y + player_height > wall_y):
                    
                    # Landing on platform (from above)
                    if player.velocity_y > 0 and player_y + player_height - player.velocity_y <= wall_y + 2:
                        player.set_y(wall_y - player_height)
                        player.velocity_y = 0
                        player.on_ground = True
                    # Hit head on ceiling
                    elif player.velocity_y < 0:
                        player.set_y(wall_y + wall_height)
                        player.velocity_y = 0
                    # Side collision
                    elif player_x < wall_x:
                        player.set_x(wall_x - player_width)
                    else:
                        player.set_x(wall_x + wall_width)

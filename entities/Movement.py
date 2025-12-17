import pygame


def handle_movement(player, keys):
    """Handle left/right movement"""
    moving_left = keys[player.controls["left"]]
    moving_right = keys[player.controls["right"]]

    if moving_left and not moving_right:
        player.set_x(player.get_x() - player.speed)
        if hasattr(player, 'set_direction'):
            player.set_direction('left')
    elif moving_right and not moving_left:
        player.set_x(player.get_x() + player.speed)
        if hasattr(player, 'set_direction'):
            player.set_direction('right')
    else:
        # No horizontal input (or conflicting inputs) → show front/idle
        if hasattr(player, 'set_direction'):
            player.set_direction('idle')


def handle_gravity(player):
    """Apply gravity to player"""
    player.velocity_y += player.gravity
    if player.velocity_y > 10:
        player.velocity_y = 10  # Terminal velocity
    player.set_y(player.get_y() + player.velocity_y)


def handle_jump(player):
    """Jump if on ground"""
    if player.on_ground:
        player.velocity_y = -13
        player.on_ground = False


def check_wall_collisions(player, main):
    """Check collision with walls using axis-separated (swept) resolution to avoid tunneling."""
    player.on_ground = False

    px, py, pw, ph = player.get_render_data()
    prev_x = getattr(player, 'prev_x', px)
    prev_y = getattr(player, 'prev_y', py)

    dx = px - prev_x
    dy = py - prev_y

    # --- Horizontal sweep/resolution
    if dx != 0:
        for entity in main.get_current_map().get_entities():
            if hasattr(entity, '__class__') and entity.__class__.__name__ == 'Wall':
                wx, wy, ww, wh = entity.get_render_data()

                # Check vertical overlap during horizontal movement (use either prev or current y)
                if (prev_y < wy + wh and prev_y + ph > wy) or (py < wy + wh and py + ph > wy):
                    if dx > 0:
                        # moving right
                        if prev_x + pw <= wx and px + pw > wx:
                            player.set_x(wx - pw)
                            px = player.get_x()
                            dx = px - prev_x
                    else:
                        # moving left
                        if prev_x >= wx + ww and px < wx + ww:
                            player.set_x(wx + ww)
                            px = player.get_x()
                            dx = px - prev_x

    # --- Vertical sweep/resolution ---
    if dy != 0:
        for entity in main.get_current_map().get_entities():
            if hasattr(entity, '__class__') and entity.__class__.__name__ == 'Wall':
                wx, wy, ww, wh = entity.get_render_data()

                # Ensure there is horizontal overlap at the time of vertical movement
                if (px < wx + ww and px + pw > wx):
                    if dy > 0:
                        # moving down
                        if prev_y + ph <= wy and py + ph > wy:
                            player.set_y(wy - ph)
                            player.velocity_y = 0
                            player.on_ground = True
                            py = player.get_y()
                            dy = py - prev_y
                    else:
                        # moving up
                        if prev_y >= wy + wh and py < wy + wh:
                            player.set_y(wy + wh)
                            player.velocity_y = 0
                            py = player.get_y()
                            dy = py - prev_y

    # Clamp to map bounds (x-axis)
    map_width, map_height = main.get_current_map().get_range()
    if player.get_x() < 0:
        player.set_x(0)
    elif player.get_x() + pw > map_width:
        player.set_x(map_width - pw)
    if player.get_y() > map_height + 50:
        main.restart_map()
        return


class Movement:
    handle_movement = staticmethod(handle_movement)
    handle_gravity = staticmethod(handle_gravity)
    handle_jump = staticmethod(handle_jump)
    check_wall_collisions = staticmethod(check_wall_collisions)

# python
# Datei: `entities/Moving_Element.py`
from entities.Entity import Entity
from entities.Player import Player


class Moving_Element(Entity):
    def __init__(self, x, y, width, height, main, id=None, speed=5, texture=None):
        super().__init__(x, y, width, height, main, id=id, solid=True, texture=texture)
        self.destination_y = y
        self.destination_x = x
        self.speed = speed

    def game_loop(self, past_time, events):
        max_move = self.speed * past_time

        dy = self.destination_y - self.y
        if dy > 0:
            move_y = min(dy, max_move)
        elif dy < 0:
            move_y = -min(abs(dy), max_move)
        else:
            move_y = 0

        dx = self.destination_x - self.x
        if dx > 0:
            move_x = min(dx, max_move)
        elif dx < 0:
            move_x = -min(abs(dx), max_move)
        else:
            move_x = 0

        if move_x != 0 or move_y != 0:
            self.x += move_x
            self.y += move_y

            for entity in self.get_colliding_objects():
                if isinstance(entity, Player):
                    entity.move(move_x, move_y)

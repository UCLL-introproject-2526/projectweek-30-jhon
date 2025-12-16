from entities.Entity import Entity
class Wall(Entity):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, solid=True , texture="player/eyes_open.png")
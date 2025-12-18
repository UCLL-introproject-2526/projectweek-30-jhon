from entities.Entity import Entity
class Wall(Entity):
    def __init__(self, x, y, width, height, main):
        super().__init__(x, y, width, height, main, solid=True)
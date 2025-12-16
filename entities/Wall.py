import Hitbox

class Wall(Hitbox):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, solid=True)
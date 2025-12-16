from entities.Entity import Entity

class Box(Entity):
    def __init__ (self, x, y, main):
        super().__init__(x, y, 20, 20, main,solid=True,texture="player/eyes_open.png")

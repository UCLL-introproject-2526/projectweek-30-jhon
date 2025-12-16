from entities.Entity import Entity

class Box(Entity):
    def __init__ (self, x, y,):
        super().__init__(x, y, 20, 20,solid=True,texture="player/eyes_open.png")

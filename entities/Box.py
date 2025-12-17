from entities.Entity import Entity

class Box(Entity):
    def __init__ (self, x, y, main):
        super().__init__(x, y, 20, 20, main, name="box",solid=True,texture="block_models/platform.png")

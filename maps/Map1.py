from maps.Map import Map
from entities.Wall import Wall

class Map1(Map):
    def __init__(self, main):
        super().__init__('map1', 400, 250, 40, 130, 335, 130)
        self.setup(main)

    def setup(self, main):

        # bottom
        self.add_entity(Wall(0, 240, 400, 10, main))

        # walls
        self.add_entity(Wall(0, 0, 10, 250, main))
        self.add_entity(Wall(390, 0, 10, 250, main))


        self.add_entity(Wall(90, 180, 40, 70, main))
        self.add_entity(Wall(180, 110, 40, 140, main))
        self.add_entity(Wall(270, 180, 40, 70, main))


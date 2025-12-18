from maps.Map import Map
from entities.Wall import Wall
from entities.Button import Button

class Map1(Map):
    def __init__(self, main):
        super().__init__('map1', 400, 250, 20, 180, 360, 180)
        self.setup(main)

    def setup(self, main):
        self.add_entity(Wall(0, 247, 400, 3, main))
        self.add_entity(Wall(0, 0, 12, 250, main))
        self.add_entity(Wall(388, 0, 12, 250, main))

        self.add_entity(Wall(12, 224, 16, 23, main))
        self.add_entity(Wall(372, 224, 16, 23, main))


        self.add_entity(Wall(99, 180, 30, 67, main))
        self.add_entity(Wall(184, 160, 42, 87, main))
        self.add_entity(Wall(279, 180, 30, 67, main))
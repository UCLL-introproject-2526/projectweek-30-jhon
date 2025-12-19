from maps.Map import Map
from entities.Wall2 import Wall2  # Import aangepast naar Wall2
from entities.Button import Button

class Map1(Map):
    def __init__(self, main):
        super().__init__(main, 'map1', 400, 250, 30, 180, 355, 180)
        self.setup(main)

    def setup(self, main):
        # Alle Walls vervangen door Wall2
        self.add_entity(Wall2(0, 247, 400, 3, main))

        self.add_entity(Wall2(0, 0, 12, 250, main))
        self.add_entity(Wall2(388, 0, 12, 250, main))

        self.add_entity(Wall2(100, 180, 30, 67, main))
        self.add_entity(Wall2(184, 160, 42, 87, main))
        self.add_entity(Wall2(280, 180, 30, 67, main))
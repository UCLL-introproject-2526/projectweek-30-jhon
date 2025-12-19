from entities.Wall import Wall
from maps.Map import Map
from entities.Wall2 import Wall2  # Import aangepast naar Wall2

class Map6(Map):
    def __init__(self, main):
        # super(main, naam, width, height, p1_x, p1_y, p2_x, p2_y)
        super().__init__(main, 'map6', 589, 288, 2, 170, 560, 100)
        self.setup(main)

    def setup(self, main):


        self.add_entity(Wall(0, 224, 29, 64, main))



        self.add_entity(Wall(82, 188, 19, 99, main))
        self.add_entity(Wall(58, 187, 65, 14, main))
        self.add_entity(Wall(58, 259, 65, 14, main))

        self.add_entity(Wall(82, 188, 19, 99, main))
        self.add_entity(Wall(146, 149, 65, 14, main))

        self.add_entity(Wall(171, 153, 17, 135, main))
        self.add_entity(Wall(58, 187, 65, 14, main))

        self.add_entity(Wall(235, 111, 120, 14, main))
        self.add_entity(Wall(281, 118, 30, 170, main))

        self.add_entity(Wall(382, 149, 65, 14, main))
        self.add_entity(Wall(405, 162, 17, 135, main))

        self.add_entity(Wall(492, 188, 19, 99, main))
        self.add_entity(Wall(468, 187, 65, 14, main))
        self.add_entity(Wall(468, 259, 65, 14, main))

        self.add_entity(Wall(560, 224, 29, 64, main))
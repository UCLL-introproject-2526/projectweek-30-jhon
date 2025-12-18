from maps.Map import Map
from entities.Wall import Wall

class Map2(Map):
    def __init__(self, main):
        super().__init__('map2', 400, 250, 10, 180, 365, 200)
        self.setup(main)

    def setup(self, main):
        # bottom
        self.add_entity(Wall(0, 240, 30, 10, main))
        self.add_entity(Wall(100, 240, 30, 10, main))
        self.add_entity(Wall(300, 240, 30, 10, main))
        self.add_entity(Wall(360, 240, 30, 10, main))

        # walls
        self.add_entity(Wall(0, 0, 10, 250, main))
        self.add_entity(Wall(390, 0, 10, 250, main))

        self.add_entity(Wall(30, 190, 30, 8, main))
        self.add_entity(Wall(90, 180, 25, 8, main))
        self.add_entity(Wall(145, 165, 30, 8, main))
        self.add_entity(Wall(200, 150, 40, 8, main))
        self.add_entity(Wall(270, 130, 35, 8, main))
        self.add_entity(Wall(330, 170, 30, 8, main))
from maps.Map import Map
from entities.Wall import Wall

class Map1(Map):
    def __init__(self, main):
        super().__init__('map1', 400, 250, 20, 180, 360, 180)
        self.setup(main)

    def setup(self, main):
        self.add_entity(Wall(0, 240, 400, 30, main))
        self.add_entity(Wall(-20, 0, 30, 250, main)) 
        self.add_entity(Wall(400, 0, 30, 250, main)) 
        self.add_entity(Wall(100, 180, 30, 60, main)) 
        self.add_entity(Wall(190, 160, 30, 90, main)) 
        self.add_entity(Wall(280, 180, 30, 60, main))



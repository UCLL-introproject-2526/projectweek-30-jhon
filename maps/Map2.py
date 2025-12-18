from maps.Map import Map
from entities.Wall import Wall

class Map2(Map):
    def __init__(self, main):
        super().__init__('map2', 400, 250, 25, 200, 370, 200)
        self.setup(main)

    def setup(self, main):
        self.add_entity(Wall(0, 240, 60, 20, main))
        self.add_entity(Wall(250, 240, 50, 20, main))
        self.add_entity(Wall(340, 240, 60, 20, main))

        #middle wall
        self.add_entity(Wall(180,62,40,188,main))
        self.add_entity(Wall(180,0,40,25,main))

        #right platforms
        self.add_entity(Wall(250,190,50,10, main))

        #left platform
        self.add_entity(Wall(100,190,50,10, main))

        #Side U Right
        self.add_entity(Wall(250,140,50,10, main))
        self.add_entity(Wall(290,150,10,50, main))

        #Side U Left
        self.add_entity(Wall(100,140,50,10, main))
        self.add_entity(Wall(140,150,10,40, main))


        #Right top 2 platforms
        self.add_entity(Wall(285,60,60,10, main))
        self.add_entity(Wall(330,135,45,10, main))

        # + wall
        self.add_entity(Wall(285,50,10,10, main))

        # lil platform
        self.add_entity(Wall(345,70,20,10,main))


        #top wall
        self.add_entity(Wall(0,0,400,1, main))

        #EASIER
        self.add_entity(Wall(190,62,20,10,main))
        self.add_entity(Wall(220,62,20,10,main))


        #LEFT rest
        self.add_entity(Wall(0,110,50,16, main))
        self.add_entity(Wall(0,54,55,16, main))
        self.add_entity(Wall(140,90,10,50, main))
        self.add_entity(Wall(100,90,40,10, main))
        self.add_entity(Wall(100,60,10,30, main))










        #borders
        self.add_entity(Wall(0, 0, 10, 250, main))
        self.add_entity(Wall(390, 0, 10, 250, main))
        #
        # self.add_entity(Wall(30, 190, 30, 8, main))
        # self.add_entity(Wall(90, 180, 25, 8, main))
        # self.add_entity(Wall(145, 165, 30, 8, main))
        # self.add_entity(Wall(200, 150, 40, 8, main))
        # self.add_entity(Wall(270, 130, 35, 8, main))
        # self.add_entity(Wall(330, 170, 30, 8, main))
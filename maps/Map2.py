from maps.Map import Map
from entities.Wall import Wall

class Map2(Map):
    def __init__(self, main):
        super().__init__('map2', 400, 250, 10, 200, 370, 200)
        self.setup(main)

    def setup(self, main):
        self.add_entity(Wall(0, 230, 80, 20, main))      
        self.add_entity(Wall(120, 230, 60, 20, main))    
        self.add_entity(Wall(220, 230, 80, 20, main))    
        self.add_entity(Wall(340, 230, 60, 20, main))    

        self.add_entity(Wall(0, 0, 10, 250, main))       
        self.add_entity(Wall(390, 0, 10, 250, main))     

        self.add_entity(Wall(30, 190, 30, 8, main))      
        self.add_entity(Wall(90, 180, 25, 8, main))      
        self.add_entity(Wall(145, 165, 30, 8, main))     
        self.add_entity(Wall(200, 150, 40, 8, main))     
        self.add_entity(Wall(270, 130, 35, 8, main))     
        self.add_entity(Wall(330, 170, 30, 8, main))     
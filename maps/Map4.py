from maps.Map import Map
from entities.Wall import Wall
from entities.Spike import Spike

class Map4(Map):
    def __init__(self, main):

        super().__init__(main, 'map4', 400, 250, 20, 180, 350, 50)
        self.setup(main)

    def setup(self, main):
        # --- Ground and boundaries ---
        self.add_entity(Wall(0, 243, 400, 30, main))     # Ground floor
        self.add_entity(Wall(-20, 0, 30, 250, main))     # Left boundary
        self.add_entity(Wall(370, 0, 30, 250, main))     # Right boundary

        # --- Platform layout ---
        self.add_entity(Wall(0, 145, 250, 19, main))     # Lower left platform
        self.add_entity(Wall(350, 193, 50, 15, main))    # Right mid platform
        self.add_entity(Wall(60, 75, 330, 15, main))     # Upper long platform

        # --- Spikes ---
        self.add_entity(Spike(150, 59, main))            # Top spike 1
        self.add_entity(Spike(200, 59, main))            # Top spike 2
        self.add_entity(Spike(300, 227, main))           # Bottom spike 1
        self.add_entity(Spike(100, 227, main))           # Bottom spike 2
        self.add_entity(Spike(150, 227, main))           # Bottom spike 3
        self.add_entity(Spike(260, 227, main))           # Bottom spike 4
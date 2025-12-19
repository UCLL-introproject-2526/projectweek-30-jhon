from maps.Map import Map
from entities.Wall import Wall

class Map6(Map):
    def __init__(self, main):
        # super(main, naam, width, height, p1_x, p1_y, p2_x, p2_y)
        # P1 start op (10, 200), P2 start op (370, 200)
        super().__init__(main, 'map6', 400, 250, 10, 200, 370, 200)
        self.setup(main)

    def setup(self, main):
        # --- Ground floor (Verschillende segmenten) ---
        self.add_entity(Wall(0, 230, 80, 20, main))      # Left segment
        self.add_entity(Wall(120, 230, 60, 20, main))    # Center-left segment
        self.add_entity(Wall(220, 230, 80, 20, main))    # Center-right segment
        self.add_entity(Wall(340, 230, 60, 20, main))    # Right segment

        # --- Boundary walls ---
        self.add_entity(Wall(0, 0, 10, 250, main))       # Left boundary
        self.add_entity(Wall(390, 0, 10, 250, main))     # Right boundary

        # --- Challenging platforms ---
        self.add_entity(Wall(30, 190, 30, 8, main))      # Step 1
        self.add_entity(Wall(90, 180, 25, 8, main))      # Step 2 (higher)
        self.add_entity(Wall(145, 165, 30, 8, main))     # Step 3 (higher)
        self.add_entity(Wall(200, 150, 40, 8, main))     # Step 4 (highest)
        self.add_entity(Wall(270, 130, 35, 8, main))     # Step 5 (peak)
        self.add_entity(Wall(330, 170, 30, 8, main))     # Step 6 (descending)
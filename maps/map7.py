from maps.Map import Map
from entities.Wall2 import Wall2  # Import aangepast naar Wall2
from entities.Spike import Spike
from entities.Pressure_plate import Pressure_plate
from entities.Moving_Element import Moving_Element


class Map7(Map):
    def __init__(self, main):
        # Breedte 1000, Hoogte 750
        super().__init__(main, 'map7', 1000, 750, 150, 659, 850, 659)
        self.setup(main)

    def setup(self, main):
        # --- Base structure (Nu Wall2) ---
        self.add_entity(Wall2(0, 730, 1000, 50, main))  # Ground floor
        self.add_entity(Wall2(490, 200, 20, 730, main))  # Center Wall

        # --- Spikes (Loop) ---
        for x in range(0, 1000, 20):
            self.add_entity(Spike(x, 711, main))

        # --- Left side - Player 1 Platforms (Nu Wall2) ---
        self.add_entity(Wall2(100, 685, 100, 20, main))
        self.add_entity(Wall2(250, 620, 100, 20, main))
        self.add_entity(Wall2(400, 555, 100, 20, main))
        self.add_entity(Wall2(250, 500, 100, 20, main))
        self.add_entity(Wall2(100, 445, 100, 20, main))
        self.add_entity(Wall2(20, 390, 20, 20, main))
        self.add_entity(Wall2(100, 325, 100, 20, main))
        self.add_entity(Wall2(250, 260, 100, 20, main))
        self.add_entity(Wall2(400, 195, 100, 20, main))

        # --- Right side - Player 2 Platforms (Nu Wall2) ---
        self.add_entity(Wall2(800, 685, 100, 20, main))
        self.add_entity(Wall2(650, 620, 100, 20, main))
        self.add_entity(Wall2(500, 555, 100, 20, main))
        self.add_entity(Wall2(650, 500, 100, 20, main))
        self.add_entity(Wall2(800, 445, 100, 20, main))
        self.add_entity(Wall2(960, 390, 20, 20, main))
        self.add_entity(Wall2(800, 325, 100, 20, main))
        self.add_entity(Wall2(650, 260, 100, 20, main))
        self.add_entity(Wall2(500, 195, 100, 20, main))

        # --- INTERACTIVE WALLS (Moving Elements) ---
        # Deze blijven Moving_Element (want Wall2 kan niet bewegen)

        # Muur voor rechterkant (exit right)
        self.add_entity(Moving_Element(495, 100, 20, 100, main, "wall_exit_right", texture='wall/platform', speed=50))

        # Muur voor linkerkant (exit left)
        self.add_entity(Moving_Element(485, 100, 20, 100, main, "wall_exit_left", texture='wall/platform', speed=50))

        # --- PRESSURE PLATES ---
        self.add_entity(Pressure_plate(520, 185, main, "plate_right"))
        self.add_entity(Pressure_plate(465, 185, main, "plate_left"))

    def update(self, past_time, events):
        # --- Logica: Permanent openen ---

        # 1. Rechterkant
        plate_right = self.get_entity_by_id("plate_right")
        wall_right = self.get_entity_by_id("wall_exit_right")

        if plate_right and wall_right:
            if plate_right.get_pressure():
                wall_right.destination_y = -1000  # Wegschuiven

        # 2. Linkerkant
        plate_left = self.get_entity_by_id("plate_left")
        wall_left = self.get_entity_by_id("wall_exit_left")

        if plate_left and wall_left:
            if plate_left.get_pressure():
                wall_left.destination_y = -1000  # Wegschuiven
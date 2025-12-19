from entities.Wall import Wall
from maps.Map import Map
from entities.Wall2 import Wall2  # Import aangepast naar Wall2
from entities.Spike import Spike
from entities.Pressure_plate import Pressure_plate
from entities.Moving_Element import Moving_Element


class Map7(Map):
    def __init__(self, main):
        # Breedte 1000, Hoogte 750
        super().__init__(main, 'map7', 1024, 765, 308, 565, 715, 563)
        self.setup(main)
        self.__left = False
        self.__right = False

    def setup(self, main):


        self.add_entity(Wall(0, 760, 1024, 10, main))
        self.add_entity(Wall(412, 197, 206, 26, main))
        self.add_entity(Wall(495, 220, 40, 542, main))
        self.add_entity(Wall(412, 567, 205, 26, main))
        self.add_entity(Wall(256, 265, 106, 16, main))
        self.add_entity(Wall(103, 334, 108, 23, main))
        self.add_entity(Wall(0, 445, 217, 22, main))
        self.add_entity(Wall(256, 511, 104, 24, main))
        self.add_entity(Wall(256, 634, 106, 25, main))
        self.add_entity(Wall(668, 267, 105, 13, main))
        self.add_entity(Wall(668, 267, 105, 13, main))
        self.add_entity(Wall(818, 334, 107, 23, main))
        self.add_entity(Wall(813, 455, 211, 22, main))
        self.add_entity(Wall(666, 511, 106, 23, main))
        self.add_entity(Wall(665, 636, 106, 23, main))
        self.add_entity(Wall(932, 392, 92, 70, main))
        self.add_entity(Wall(977, 347, 47, 50, main))
        self.add_entity(Wall(0, 395, 91, 80, main))
        self.add_entity(Wall(0, 346, 49, 52, main))


        self.add_entity(Moving_Element(495, 100, 39, 95, main, "pillar", texture='wall/pillar_1', speed=50))
        self.add_entity(Pressure_plate(557, 185, main, "plate_right"))
        self.add_entity(Pressure_plate(450, 185, main, "plate_left"))


        # spikes
        for i in range(0, 51):
            self.add_entity(Spike(20 * i, 753, main))


    def restart(self):
        self.__left = False
        self.__right = False

    def update(self, past_time, events):
        if self.get_entity_by_id('plate_right').get_pressure():
            self.__right = True

        if self.get_entity_by_id('plate_left').get_pressure():
            self.__left = True

        if self.__left and self.__right:
            self.get_entity_by_id('pillar').destination_y = 150

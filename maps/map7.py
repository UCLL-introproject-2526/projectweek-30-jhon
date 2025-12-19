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

        self.add_entity(Spike(0, 753, main))
        self.add_entity(Spike(20, 753, main))
        self.add_entity(Spike(40, 753, main))
        self.add_entity(Spike(60, 753, main))
        self.add_entity(Spike(80, 753, main))
        self.add_entity(Spike(100, 753, main))
        self.add_entity(Spike(120, 753, main))
        self.add_entity(Spike(140, 753, main))
        self.add_entity(Spike(160, 753, main))
        self.add_entity(Spike(180, 753, main))
        self.add_entity(Spike(200, 753, main))
        self.add_entity(Spike(220, 753, main))
        self.add_entity(Spike(240, 753, main))
        self.add_entity(Spike(260, 753, main))
        self.add_entity(Spike(280, 753, main))
        self.add_entity(Spike(300, 753, main))
        self.add_entity(Spike(320, 753, main))
        self.add_entity(Spike(340, 753, main))
        self.add_entity(Spike(360, 753, main))
        self.add_entity(Spike(380, 753, main))
        self.add_entity(Spike(300, 753, main))
        self.add_entity(Spike(320, 753, main))
        self.add_entity(Spike(340, 753, main))
        self.add_entity(Spike(360, 753, main))
        self.add_entity(Spike(380, 753, main))
        self.add_entity(Spike(400, 753, main))
        self.add_entity(Spike(420, 753, main))
        self.add_entity(Spike(440, 753, main))
        self.add_entity(Spike(460, 753, main))
        self.add_entity(Spike(480, 753, main))
        self.add_entity(Spike(500, 753, main))
        self.add_entity(Spike(520, 753, main))
        self.add_entity(Spike(540, 753, main))
        self.add_entity(Spike(560, 753, main))
        self.add_entity(Spike(580, 753, main))
        self.add_entity(Spike(600, 753, main))
        self.add_entity(Spike(620, 753, main))
        self.add_entity(Spike(640, 753, main))
        self.add_entity(Spike(660, 753, main))
        self.add_entity(Spike(680, 753, main))
        self.add_entity(Spike(700, 753, main))
        self.add_entity(Spike(720, 753, main))
        self.add_entity(Spike(740, 753, main))
        self.add_entity(Spike(760, 753, main))
        self.add_entity(Spike(780, 753, main))
        self.add_entity(Spike(800, 753, main))
        self.add_entity(Spike(820, 753, main))
        self.add_entity(Spike(840, 753, main))
        self.add_entity(Spike(860, 753, main))
        self.add_entity(Spike(880, 753, main))
        self.add_entity(Spike(900, 753, main))
        self.add_entity(Spike(920, 753, main))
        self.add_entity(Spike(940, 753, main))
        self.add_entity(Spike(960, 753, main))
        self.add_entity(Spike(980, 753, main))
        self.add_entity(Spike(1000, 753, main))
        self.add_entity(Spike(1220, 753, main))


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




        pass
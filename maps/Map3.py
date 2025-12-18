from entities.Moving_Element import Moving_Element
from entities.Spike import Spike
from maps.Map import Map
from entities.Wall import Wall
from entities.Pressure_plate import Pressure_plate


class Map3(Map):
    def __init__(self, main):
        super().__init__('map3', 400, 250, 10, 180, 360, 0)
        self.setup(main)

    def setup(self, main):
        # bottom
        self.add_entity(Wall(0, 247, 400, 3, main))
        self.add_entity(Wall(0, 169, 314, 16, main))
        self.add_entity(Wall(79, 63, 321, 16, main))
        self.add_entity(Wall(0, 0, 400, 5, main))


        # walls
        self.add_entity(Wall(0, 0, 10, 250, main))
        self.add_entity(Wall(390, 0, 10, 250, main))

        # pressure_plates
        self.add_entity(Pressure_plate(80, 236, main, "activator"))

        # spike
        self.add_entity(Spike(100, 231, main))

        # moving element
        self.add_entity(Moving_Element(140, 220, 10, 10, main, "mover", texture='wall/platform', speed=40))

    def update(self, past_time, events):
        if self.get_entity_by_id('activator').get_pressure():
            self.get_entity_by_id('mover').destination_y = 180
            for entity in self.entities:
                if isinstance(entity, Spike):
                    entity.disable()
        else:
            self.get_entity_by_id('mover').destination_y = 220
            for entity in self.entities:
                if isinstance(entity, Spike):
                    entity.enable()

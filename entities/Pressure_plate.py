from entities.Entity import Entity
from entities.Player import Player
from tools.importer import image


class Pressure_plate(Entity):
    def __init__(self, x, y, main, id):
        super().__init__(x, y, 16, 16, main, id=id)
        self.__pressure = False
        self.textures = [
            image("entities/pressure_plate/in.png"),
            image("entities/pressure_plate/out.png")
        ]

    def get_texture(self):
        return self.textures[0] if self.__pressure else self.textures[1]

    def get_pressure(self):
        return self.__pressure

    def game_loop(self, past_time, events):
        for entity in self.get_colliding_objects():
            if isinstance(entity, Player):
                self.__pressure = True
                return
        self.__pressure = False
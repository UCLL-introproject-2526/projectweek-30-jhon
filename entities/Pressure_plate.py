from entities.Entity import Entity
from entities.Player import Player
from tools.ImageLibary import image_library


class Pressure_plate(Entity):
    def __init__(self, x, y, main, id):
        super().__init__(x, y, 16, 16, main, id=id)
        self.__pressure = False

    def get_texture(self):
        return image_library.get_image("entities/pressure_plate/in.png") if self.__pressure else image_library.get_image("entities/pressure_plate/out.png")

    def get_pressure(self):
        return self.__pressure

    def game_loop(self, past_time, events):
        for entity in self.get_colliding_objects():
            if isinstance(entity, Player):
                self.__pressure = True
                return
        self.__pressure = False
from config import build_maps
from entities.Player import Player

class MapManager:
    def __init__(self, main):
        self.__current_map = 0
        self.__maps = build_maps(main)
        self.__player1 = Player(0, 0, main, "p1")
        self.__player2 = Player(1, 0, main, "p2")
        self.get_current_map().add_entity(self.__player1)
        self.get_current_map().add_entity(self.__player2)


    def select_map(self, name):
        self.__current_map = name

    def get_current_map(self):
        return self.__maps[self.__current_map]

    def next_map(self):
        self.get_current_map().remove_entity(self.__player1)
        self.get_current_map().remove_entity(self.__player2)
        self.__current_map += 1
        if self.__current_map >= len(self.__maps):
            self.__current_map = 0
        self.get_current_map().add_entity(self.__player1)
        self.get_current_map().add_entity(self.__player2)
        self.__player1.reset_movement()
        self.__player2.reset_movement()

    def reset_map(self):
        self.get_current_map().restart_map()

    def get_map_by_entity(self, entity):
        for map in self.__maps:
            for e in map.get_entities():
                if e is entity:
                    return map
        return None

    def transfer(self, entity, map):
        self.get_map_by_entity(entity)
        map.add_entity(entity)


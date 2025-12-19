from config import build_maps
from entities.Player import Player

class MapManager:
    def __init__(self, main):
        self.__current_map = 3
        self.__previous_map = 0
        self.__maps = build_maps(main)
        self.__player1 = Player(0, 0, main, "p1")
        self.__player2 = Player(1, 0, main, "p2")
        self.get_current_map().add_entity(self.__player1)
        self.get_current_map().add_entity(self.__player2)


    def select_map(self, number):
        self.__current_map = number
        self.get_current_map().remove_entity(self.__player1)
        self.get_current_map().remove_entity(self.__player2)

        self.__current_map = number
        self.get_current_map().add_entity(self.__player1)
        self.get_current_map().add_entity(self.__player2)
        self.__player1.reset_movement()
        self.__player2.reset_movement()

    def get_current_map(self):
        return self.__maps[self.__current_map]

    def next_map(self):
        new_map = self.__current_map + 1
        if new_map >= len(self.__maps):
            new_map = 0
        self.select_map(new_map)

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

    def settings(self):
        self.__previous_map = self.__current_map
        self.select_map(len(self.__maps) - 1)
    
    def back_from_settings(self):
        self.select_map(self.__previous_map)

    def get_p1(self):
        return self.__player1

    def get_p2(self):
        return self.__player2




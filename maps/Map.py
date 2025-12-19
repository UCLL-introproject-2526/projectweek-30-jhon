import pygame

from entities.Player import Player
from tools.ImageLibary import image_library

class Map:
    def __init__(self, main, name, width, height, start_pos1_x, start_pos1_y, start_pos2_x, start_pos2_y, no_player=False):
        self.__width = width
        self.__height = height
        self.__start_pos1_x = start_pos1_x
        self.__start_pos1_y = start_pos1_y
        self.__start_pos2_x = start_pos2_x
        self.__start_pos2_y = start_pos2_y
        self.bg = f"background/{name}.png"
        self.fg = f"frontground/{name}.png"
        self.__disable_players = no_player
        self.main = main
        self.entities = []

    def get_no_player(self):
        return self.__disable_players

    def add_entity(self, entity):
        if entity not in self.entities:
            self.entities.append(entity)
            self.place_player(entity)

    def remove_entity(self, entity):
        if entity in self.entities:
            self.entities.remove(entity)

    def get_range(self):
        return self.__width, self.__height

    def get_bg(self):
        return image_library.get_image(self.bg)

    def get_fg(self):
        return image_library.get_image(self.fg)

    def get_entities(self):
        return self.entities

    def get_height(self):
        return self.__height

    def get_width(self):
        return self.__width

    def get_entity_by_id(self, id):
        for entity in self.entities:
            if entity.get_id() == id:
                return entity

    def update_map(self, past_time, events):
        self.update(past_time, events)
        for entity in self.entities:
            entity.game_loop(past_time, events)

    def update(self, past_time, events):
        pass

    def place_player(self, player):
        if isinstance(player, Player):
            if player.get_player_name() == "p1":
                player.y = self.__start_pos1_y
                player.x = self.__start_pos1_x
            else:
                player.y = self.__start_pos2_y
                player.x = self.__start_pos2_x

    def restart_map(self):
        for entity in self.entities:
            self.place_player(entity)

    def restart(self):
        pass
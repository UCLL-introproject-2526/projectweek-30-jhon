from Map import Map
from entities.Player import Player
from logic.Loop_controller import Loop_controller
from logic.Logic_runner import LogicManager
from entities.Box import Box
from entities.Wall import Wall
from settings.keyboard_layout import keybinds_player1, keybinds_player2

def build_maps(main):
    maps = []
    map1 = Map("map1", 400, 250)
    map1.add_entity(Player(50, 50, main, 1))
    map1.add_entity(Player(100, 50, main, 2))
    map1.add_entity(Box(200, 200, ))
    map1.add_entity(Wall(-2, 200, 400, 20))
    maps.append(map1)
    

    return maps

class Main:
    def __init__(self):
        self.__loop_controller = Loop_controller(self, "Projectweek Jhon")
        self.__maps = build_maps(self)
        self.__selected_map = 0

        self.__loop_controller.start()
    def get_current_map(self):
        return self.__maps[self.__selected_map]

    def add_later_task(self, task, delay):
        self.__loop_controller.add_later_task(task, delay)
    

main = Main()



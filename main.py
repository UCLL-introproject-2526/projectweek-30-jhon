from Map import Map
from entities.Player import Player
from logic.Loop_controller import Loop_controller
from logic.Logic_runner import LogicManager
from entities.Box import Box
from entities.Wall import Wall
from entities.MenuController import MenuController
from settings.keyboard_layout import keybinds_player1, keybinds_player2

def build_maps(main):
    maps = []
    map0 = Map("map0", 400, 250)
    
    def play_game():
        print("Starting game!")
        main.select_map(1)
    
    def settings():
        print("Settings clicked")
    
    def quit_game():
        import sys
        print("Quitting...")
        sys.exit()
    

    map0.add_entity(MenuController(play_game, settings, quit_game))
    maps.append(map0)
    map1 = Map("map1", 400, 250)
    map1.add_entity(Player(50, 50, main, 1))
    map1.add_entity(Player(100, 50, main, 2))
    map1.add_entity(Box(200, 200, main))
    map1.add_entity(Wall(-2, 200, 400, 20, main))
    maps.append(map1)
    
    

    return maps

class Main:
    def __init__(self):
        self.__loop_controller = Loop_controller(self, "Merge Conflict")
        self.__maps = build_maps(self)
        self.__selected_map = 0

        self.__loop_controller.start()
    def get_current_map(self):
        return self.__maps[self.__selected_map]
    
    def select_map(self, index):
        if 0 <= index < len(self.__maps):
            self.__selected_map = index

    def add_later_task(self, task, delay):
        self.__loop_controller.add_later_task(task, delay)
    

main = Main()

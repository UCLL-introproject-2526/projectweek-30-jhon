from Map import Map
from entities.Player import Player
from logic.Loop_controller import Loop_controller
from logic.Logic_runner import LogicManager
from entities.Box import Box
from entities.Wall import Wall
from entities.MenuController import MenuController
from entities.SettingsMap import SettingsMap
from settings.keyboard_layout import keybinds_player1, keybinds_player2
from entities.Spike import Spike
from entities.PlayerMerge import PlayerMerge

def build_maps(main):
    maps = []
    map0 = Map("start_menu", 400, 250)
    
    def play_game():
        print("Starting game!")
        main.select_map(1)
    
    def settings():
        print("Settings clicked")
        main.select_map(3)
    
    def quit_game():
        import sys
        print("Quitting...")
        sys.exit()
    

    map0.add_entity(MenuController(play_game, settings, quit_game))
    maps.append(map0)
    
    # Map 1: Level 1 - Platform Challenge
    map1 = Map("background", 400, 250)

    # Players start at OPPOSITE sides
    map1.add_entity(Player(20, 180, main, 1))  # Left side
    map1.add_entity(Player(360, 180, main, 2))  # Right side
    
    # Ground floor
    map1.add_entity(Wall(0, 220, 400, 30, main))
    
    # Middle platforms to cross
    map1.add_entity(Wall(100, 180, 30, 10, main))
    map1.add_entity(Wall(190, 160, 30, 10, main))
    map1.add_entity(Wall(280, 180, 30, 10, main))
    
    # Merge detector - triggers when players touch ANYWHERE
    map1.add_entity(PlayerMerge(main, lambda: main.select_map(2)))
    
    maps.append(map1)
    
    # Map 2: Level 2 - Advanced Challenge (HARDER!)
    map2 = Map("map1", 400, 250)
    
    # Players start at opposite ends AGAIN
    map2.add_entity(Player(10, 200, main, 1))  # Far left
    map2.add_entity(Player(370, 200, main, 2))  # Far right
    
    # Ground floor - multiple gaps!
    map2.add_entity(Wall(0, 230, 80, 20, main))
    map2.add_entity(Wall(120, 230, 60, 20, main))
    map2.add_entity(Wall(220, 230, 80, 20, main))
    map2.add_entity(Wall(340, 230, 60, 20, main))
    
    # Challenging platforms to cross
    map2.add_entity(Wall(30, 190, 30, 8, main))
    map2.add_entity(Wall(90, 180, 25, 8, main))
    map2.add_entity(Wall(145, 165, 30, 8, main))
    map2.add_entity(Wall(200, 150, 40, 8, main))
    map2.add_entity(Wall(270, 130, 35, 8, main))
    map2.add_entity(Wall(330, 170, 30, 8, main))
    
    # Merge detector for level 2
    map2.add_entity(PlayerMerge(main, lambda: main.select_map(0)))  # Back to menu after level 2
    
    maps.append(map2)

    # Map 3: Settings
    map3 = Map("settings", 400, 250)
    SettingsMap(main, map3)
    maps.append(map3)
    
    

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

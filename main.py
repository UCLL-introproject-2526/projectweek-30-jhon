from Map import Map
from entities.Player import Player
from logic.Loop_controller import Loop_controller
from logic.Logic_runner import LogicManager
from entities.Box import Box
from entities.Wall import Wall
from entities.MenuController import MenuController
from entities.SettingsMap import SettingsMap
from entities.GoalArea import GoalArea
from settings.keyboard_layout import keybinds_player1, keybinds_player2

def build_maps(main):
    maps = []
    map0 = Map("map0", 400, 250)
    
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
    map1 = Map("map1", 400, 250)
    
    # Players start position
    map1.add_entity(Player(20, 180, main, 1))
    map1.add_entity(Player(40, 180, main, 2))
    
    # Ground floor
    map1.add_entity(Wall(0, 220, 400, 30, main))
    
    # Left side platforms
    map1.add_entity(Wall(0, 180, 60, 10, main))
    map1.add_entity(Wall(20, 140, 50, 10, main))
    
    # Middle platforms (gaps to jump across)
    map1.add_entity(Wall(100, 200, 50, 10, main))
    map1.add_entity(Wall(170, 170, 50, 10, main))
    map1.add_entity(Wall(240, 140, 50, 10, main))
    
    # Right side platforms
    map1.add_entity(Wall(310, 110, 60, 10, main))
    map1.add_entity(Wall(340, 70, 60, 10, main))
    
    # Obstacles - boxes to push/avoid
    map1.add_entity(Box(130, 190, main))
    map1.add_entity(Box(200, 160, main))
    map1.add_entity(Box(270, 130, main))
    
    # Top platform - goal area
    map1.add_entity(Wall(350, 40, 50, 10, main))
    map1.add_entity(GoalArea(350, 20, 50, 20, main, lambda: main.select_map(2)))
    
    maps.append(map1)
    
    # Map 2: Level 2 - Advanced Challenge (HARDER!)
    map2 = Map("map1", 400, 250)
    
    # Players start at bottom left
    map2.add_entity(Player(10, 200, main, 1))
    map2.add_entity(Player(30, 200, main, 2))
    
    # Ground floor - multiple gaps!
    map2.add_entity(Wall(0, 230, 80, 20, main))
    map2.add_entity(Wall(120, 230, 60, 20, main))
    map2.add_entity(Wall(220, 230, 80, 20, main))
    map2.add_entity(Wall(340, 230, 60, 20, main))
    
    # Lower platforms - narrow jumps
    map2.add_entity(Wall(30, 190, 30, 8, main))
    map2.add_entity(Wall(90, 180, 25, 8, main))
    map2.add_entity(Wall(145, 165, 30, 8, main))
    
    # Middle section - zigzag pattern
    map2.add_entity(Wall(50, 140, 35, 8, main))
    map2.add_entity(Wall(115, 120, 30, 8, main))
    map2.add_entity(Wall(70, 100, 35, 8, main))
    map2.add_entity(Wall(135, 80, 30, 8, main))
    
    # Right section - tall climb
    map2.add_entity(Wall(200, 150, 40, 8, main))
    map2.add_entity(Wall(270, 130, 35, 8, main))
    map2.add_entity(Wall(230, 100, 40, 8, main))
    map2.add_entity(Wall(300, 70, 35, 8, main))
    
    # More obstacles - strategic box placement
    map2.add_entity(Box(60, 180, main))
    map2.add_entity(Box(120, 175, main))
    map2.add_entity(Box(155, 155, main))
    map2.add_entity(Box(80, 130, main))
    map2.add_entity(Box(210, 140, main))
    map2.add_entity(Box(280, 120, main))
    
    # Final platform and goal at top right
    map2.add_entity(Wall(340, 40, 60, 10, main))
    map2.add_entity(GoalArea(340, 15, 60, 25, main, lambda: main.select_map(0)))  # Back to menu
    
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

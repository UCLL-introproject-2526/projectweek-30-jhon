from Map import Map
from entities.Spike import Spike
from entities.Wall import Wall
from entities.Player import Player
from entities.MenuController import MenuController
from entities.PressurePlate import PressurePlate
from entities.SettingsMap import SettingsMap
from entities.EndingScreen import EndingScreen


def build_maps(main):
    maps = []
    map0 = Map("start_menu", 400, 250)

    def play_game():
        print("Starting game!")
        main.next_map()

    def settings():
        print("Settings clicked")
        # Settings map sits after level 3
        main.select_map(101)

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
    map1.add_entity(Wall(0, 240, 400, 30, main))

    # Left & right boundary walls to prevent players from falling off the sides
    map1.add_entity(Wall(-20, 0, 30, 250, main))  # Left wall
    map1.add_entity(Wall(400, 0, 30, 250, main))  # Right wall

    # Middle platforms to cross
    map1.add_entity(Wall(100, 180, 30, 60, main))
    map1.add_entity(Wall(190, 160, 30, 90, main))
    map1.add_entity(Wall(280, 180, 30, 60, main))

    # Merge detector - triggers when players touch ANYWHERE
    maps.append(map1)

    # Map 2: Level 2 - Advanced Challenge (HARDER!)
    map2 = Map("background", 400, 250)

    # Players start at opposite ends AGAIN
    map2.add_entity(Player(10, 200, main, 1))  # Far left
    map2.add_entity(Player(370, 200, main, 2))  # Far right

    # Ground floor - multiple gaps!
    map2.add_entity(Wall(0, 230, 80, 20, main))
    map2.add_entity(Wall(120, 230, 60, 20, main))
    map2.add_entity(Wall(220, 230, 80, 20, main))
    map2.add_entity(Wall(340, 230, 60, 20, main))

    # Left & right boundary walls to prevent players from falling off the sides
    map2.add_entity(Wall(0, 0, 10, 250, main))  # Left wall
    map2.add_entity(Wall(390, 0, 10, 250, main))  # Right wall

    # Challenging platforms to cross
    map2.add_entity(Wall(30, 190, 30, 8, main))
    map2.add_entity(Wall(90, 180, 25, 8, main))
    map2.add_entity(Wall(145, 165, 30, 8, main))
    map2.add_entity(Wall(200, 150, 40, 8, main))
    map2.add_entity(Wall(270, 130, 35, 8, main))
    map2.add_entity(Wall(330, 170, 30, 8, main))

    # Merge detector for level 2 -> proceed to level 3
    maps.append(map2)

    # Map 3: Level 3 - Spikes and Platforms
    map3 = Map("map3", 400, 250)

    # Players
    map3.add_entity(Player(20, 180, main, 1))
    map3.add_entity(Player(380, 50, main, 2))

    # Ground and boundaries
    map3.add_entity(Wall(0, 240, 400, 30, main))
    map3.add_entity(Wall(-20, 0, 30, 250, main))
    map3.add_entity(Wall(400, 0, 30, 250, main))

    # Platforms layout
    map3.add_entity(Wall(0, 150, 250, 10, main))
    map3.add_entity(Wall(350, 200, 50, 10, main))
    map3.add_entity(Wall(50, 75, 350, 10, main))

    # spike top
    map3.add_entity(Spike(150, 55, main))
    map3.add_entity(Spike(200, 55, main))
    # spike bottom
    map3.add_entity(Spike(300, 221, main))
    map3.add_entity(Spike(150, 221, main))
    # Add a Pressure Plate at the bottom left (unpressed is always 'block_models/pressureplate_in.png')
    # map3.add_entity(PressurePlate(60, 233, main))


    # Merge to return to menu
    maps.append(map3)

     # map 4
    map4 = Map("map4", 400, 250)
    map4.add_entity(Player(20, 180, main, 1))
    map4.add_entity(Player(380, 50, main, 2))

    map4.add_entity(Wall(0, 240, 400, 30, main))
    map4.add_entity(Wall(-20, 0, 30, 250, main))
    map4.add_entity(Wall(400, 0, 30, 250, main))
    map4.add_entity(Wall(0, 0, 10, 250, main))

    # Platforms layout
    map4.add_entity(Wall(250, 75, 150, 10, main))
    map4.add_entity(Wall(0, 200, 200, 10, main))
    map4.add_entity(Wall(250, 35, 10, 50, main))
    map4.add_entity(Wall(200, 0, 10, 50, main))
    map4.add_entity(Wall(210, 110, 40, 10, main))

    # removable wall (will be removed by the pressure plate)
    removable_wall = Wall(325, 0, 10, 80, main)
    map4.add_entity(removable_wall)

    # wall that will be spawned by append_wall_plate (not added to map initially)
    spawnable_wall = Wall(170, 75, 90, 10, main)

    #Spikes
    map4.add_entity(Spike(280, 55, main))
    map4.add_entity(Spike(70, 220, main, removable=True))
    map4.add_entity(Spike(120, 220, main, removable=True))
    map4.add_entity(Spike(150, 180, main))
    map4.add_entity(Spike(125, 180, main))
    map4.add_entity(Spike(210, 90, main))
    map4.add_entity(Spike(230, 90, main))
    
    # pressure plate that removes the wall on activation
    map4.add_entity(PressurePlate(50, 233, main, remove_target=removable_wall))

    # pressure plate that spawns a new wall when activated
    append_wall_plate = PressurePlate(170, 193, main, add_target=spawnable_wall)
    map4.add_entity(append_wall_plate)

    # pressure plate that removes spikes
    map4.add_entity(PressurePlate(260, 68, main, remove_spikes=True))


    maps.append(map4)



<<<<<<< Updated upstream
=======















    # Map 5: New level (added)
    map5 = Map("map5", 1000, 750)

# 1. SPELERS
    map5.add_entity(Player(50, 700, main, 1))
    map5.add_entity(Player(900, 700, main, 2))

    # 2. BASIS (Grond en Middenmuur)
    map5.add_entity(Wall(0, 730, 1000, 50, main))
    map5.add_entity(Wall(490, 0, 20, 730, main)) # Middenmuur

    # 3. LINKER KANT (Speler 1)
    # De sprongen zijn nu max 45 pixels hoog
    map5.add_entity(Wall(10, 685, 100, 20, main))
    map5.add_entity(Wall(120, 640, 100, 20, main))
    map5.add_entity(Wall(230, 595, 100, 20, main)) # Dicht bij midden
    map5.add_entity(Wall(120, 550, 100, 20, main)) # Terug naar links
    map5.add_entity(Wall(10, 505, 100, 20, main))
    map5.add_entity(Wall(120, 460, 100, 20, main))
    map5.add_entity(Wall(230, 415, 100, 20, main))
    map5.add_entity(Wall(120, 370, 100, 20, main))
    # Finish Links
    map5.add_entity(Wall(50, 300, 200, 20, main))

    # 4. RECHTER KANT (Speler 2 - Gespiegeld)
    map5.add_entity(Wall(890, 685, 100, 20, main))
    map5.add_entity(Wall(780, 640, 100, 20, main))
    map5.add_entity(Wall(670, 595, 100, 20, main)) # Dicht bij midden
    map5.add_entity(Wall(780, 550, 100, 20, main)) # Terug naar rechts
    map5.add_entity(Wall(890, 505, 100, 20, main))
    map5.add_entity(Wall(780, 460, 100, 20, main))
    map5.add_entity(Wall(670, 415, 100, 20, main))
    map5.add_entity(Wall(780, 370, 100, 20, main))
    # Finish Rechts
    map5.add_entity(Wall(750, 300, 200, 20, main))


    # removable wall (will be removed by the pressure plate)

    # A spike to increase challenge

    # pressure plate that removes the wall on activation

    maps.append(map5)


>>>>>>> Stashed changes
    # map 100 - Ending screen
    map100 = Map("ending", 400, 250)
    map100.add_entity(EndingScreen(
        lambda: main.select_map(1),  # Replay: go back to level 1
        lambda: main.select_map(0),  # Menu: go to main menu
        lambda: __import__('sys').exit()  # Quit
    ))
    maps.append(map100)
    # Map 101: Settings
    map101 = Map("settings", 400, 250)
    SettingsMap(main, map101)
    maps.append(map101)

    return maps
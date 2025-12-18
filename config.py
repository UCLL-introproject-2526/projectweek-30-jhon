
# ============================================================================
# IMPORTS
# ============================================================================
from Map import Map
from entities.Spike import Spike
from entities.Wall import Wall
from entities.Player import Player
from entities.MenuController import MenuController
from entities.Button import Button
from entities.PressurePlate import PressurePlate
from entities.SettingsMap import SettingsMap
from entities.EndingScreen import EndingScreen


# ============================================================================
# MAIN MAP BUILDER
# ============================================================================
def build_maps(main):
    maps = []
    # ========================================================================
    # MAP 0: MAIN MENU
    # ========================================================================
    map0 = Map("map0", 400, 250)

    # Menu button callbacks
    def play_game():
        """Start the game from level 1"""
        print("Starting game!")
        main.next_map()

    def settings():
        """Open settings screen (settings)"""
        print("Settings clicked")
        main.select_map("settings")

    def quit_game():
        """Exit the game"""
        import sys
        print("Quitting...")
        sys.exit()

    # Add menu controller with keyboard shortcuts
    map0.add_entity(MenuController(play_game, settings, quit_game))
    maps.append(map0)

    # ========================================================================
    # MAP 1: LEVEL 1 - Platform Challenge
    # ========================================================================
    map1 = Map("map1", 400, 250)

    map1.add_entity(Player(20, 180, main, 1))
    map1.add_entity(Player(360, 180, main, 2))

    # Ground floor
    map1.add_entity(Wall(0, 240, 400, 30, main))

    # Boundary walls (prevent falling off edges)
    map1.add_entity(Wall(-20, 0, 30, 250, main))   # Left boundary
    map1.add_entity(Wall(400, 0, 30, 250, main))   # Right boundary

    # Middle platforms
    map1.add_entity(Wall(100, 180, 30, 60, main))  # Left platform
    map1.add_entity(Wall(190, 160, 30, 90, main))  # Center platform (higher)
    map1.add_entity(Wall(280, 180, 30, 60, main))  # Right platform

    maps.append(map1)

    # ========================================================================
    # MAP 2: LEVEL 2 - Advanced Challenge
    # ========================================================================
    map2 = Map("background", 400, 250)

    # Players (starting at far opposite ends)
    map2.add_entity(Player(10, 200, main, 1))
    map2.add_entity(Player(370, 200, main, 2))

    # Ground floor
    map2.add_entity(Wall(0, 230, 80, 20, main))      # Left segment
    map2.add_entity(Wall(120, 230, 60, 20, main))    # Center-left segment
    map2.add_entity(Wall(220, 230, 80, 20, main))    # Center-right segment
    map2.add_entity(Wall(340, 230, 60, 20, main))    # Right segment

    # Boundary walls
    map2.add_entity(Wall(0, 0, 10, 250, main))       # Left boundary
    map2.add_entity(Wall(390, 0, 10, 250, main))     # Right boundary

    # Challenging platforms
    map2.add_entity(Wall(30, 190, 30, 8, main))      # Step 1
    map2.add_entity(Wall(90, 180, 25, 8, main))      # Step 2 (higher)
    map2.add_entity(Wall(145, 165, 30, 8, main))     # Step 3 (higher)
    map2.add_entity(Wall(200, 150, 40, 8, main))     # Step 4 (highest)
    map2.add_entity(Wall(270, 130, 35, 8, main))     # Step 5 (peak)
    map2.add_entity(Wall(330, 170, 30, 8, main))     # Step 6 (descending)

    maps.append(map2)

    # ========================================================================
    # MAP 3: LEVEL 3 - Spikes and Platforms
    # ========================================================================
    map3 = Map("map3", 400, 250)

    # Players (different starting heights)
    map3.add_entity(Player(20, 180, main, 1))
    map3.add_entity(Player(380, 50, main, 2))

    # Ground and boundaries
    map3.add_entity(Wall(0, 240, 400, 30, main))     # Ground floor
    map3.add_entity(Wall(-20, 0, 30, 250, main))     # Left boundary
    map3.add_entity(Wall(400, 0, 30, 250, main))     # Right boundary

    # Platform layout
    map3.add_entity(Wall(0, 150, 250, 10, main))     # Lower left platform
    map3.add_entity(Wall(350, 200, 50, 10, main))    # Right mid platform
    map3.add_entity(Wall(50, 75, 350, 10, main))     # Upper long platform

    # Spikes
    map3.add_entity(Spike(150, 55, main))            # Top spike 1
    map3.add_entity(Spike(200, 55, main))            # Top spike 2
    map3.add_entity(Spike(300, 221, main))           # Bottom spike 1
    map3.add_entity(Spike(150, 221, main))           # Bottom spike 2

    maps.append(map3)

    # ========================================================================
    # MAP 4: LEVEL 4 - Pressure Plates and Puzzles
    # ========================================================================
    map4 = Map("map4", 400, 250)

    # Players
    map4.add_entity(Player(20, 180, main, 1))
    map4.add_entity(Player(380, 50, main, 2))

    # Ground and boundaries
    map4.add_entity(Wall(0, 240, 400, 30, main))     # Ground floor
    map4.add_entity(Wall(-20, 0, 30, 250, main))     # Left outer boundary
    map4.add_entity(Wall(400, 0, 30, 250, main))     # Right boundary
    map4.add_entity(Wall(0, 0, 10, 250, main))       # Left inner boundary

    # Static platforms
    map4.add_entity(Wall(250, 75, 150, 10, main))    # Upper right platform
    map4.add_entity(Wall(0, 200, 200, 10, main))     # Left mid platform
    map4.add_entity(Wall(250, 35, 10, 50, main))     # Vertical wall right
    map4.add_entity(Wall(200, 0, 10, 50, main))      # Vertical wall center
    map4.add_entity(Wall(210, 110, 40, 10, main))    # Small center platform

    # Interactive walls
    removable_wall = Wall(325, 0, 10, 80, main)      # Will be removed by pressure plate
    map4.add_entity(removable_wall)
    
    spawnable_wall = Wall(170, 75, 90, 10, main)     # Will appear when plate activated

    # Spikes (some removable)
    map4.add_entity(Spike(280, 55, main))                    # Top spike (permanent)
    map4.add_entity(Spike(70, 220, main, removable=True))    # Bottom spike 1 (removable)
    map4.add_entity(Spike(120, 220, main, removable=True))   # Bottom spike 2 (removable)
    map4.add_entity(Spike(150, 180, main))                   # Mid spike 1 (permanent)
    map4.add_entity(Spike(125, 180, main))                   # Mid spike 2 (permanent)
    map4.add_entity(Spike(210, 90, main))                    # Center spike 1 (permanent)
    map4.add_entity(Spike(230, 90, main))                    # Center spike 2 (permanent)
    
    # Pressure plates
    map4.add_entity(PressurePlate(50, 233, main, remove_target=removable_wall))  # Removes wall
    map4.add_entity(PressurePlate(170, 193, main, add_target=spawnable_wall))    # Spawns platform
    map4.add_entity(PressurePlate(260, 68, main, remove_spikes=True))            # Removes spikes

    maps.append(map4)



    # ========================================================================
    # MAP 5: LEVEL 5 - Mirrored Towers
    # ========================================================================

    map5 = Map("map5", 1000, 750)

    # Left player
    map5.add_entity(Player(150, 659, main, 1))
    # Right player
    map5.add_entity(Player(850, 659, main, 2))

    # Base structure
    map5.add_entity(Wall(0, 730, 1000, 50, main))      # Ground floor
    for x in range(0, 1000, 20):
        map5.add_entity(Spike(x, 711, main))
    map5.add_entity(Wall(490, 200, 20, 730, main))       

    # Left side - Player 1
    map5.add_entity(Wall(100, 685, 100, 20, main))
    map5.add_entity(Wall(250, 620, 100, 20, main))
    map5.add_entity(Wall(400, 555, 100, 20, main)) 
    map5.add_entity(Wall(250, 500, 100, 20, main)) 
    map5.add_entity(Wall(100, 445, 100, 20, main))
    map5.add_entity(Wall(20, 390, 20, 20, main))
    map5.add_entity(Wall(100, 325, 100, 20, main))
    map5.add_entity(Wall(250, 260, 100, 20, main))
    map5.add_entity(Wall(400, 195, 100, 20, main))

    # Right side - Player 2
    map5.add_entity(Wall(800, 685, 100, 20, main))   
    map5.add_entity(Wall(650, 620, 100, 20, main))   
    map5.add_entity(Wall(500, 555, 100, 20, main))   
    map5.add_entity(Wall(650, 500, 100, 20, main))   
    map5.add_entity(Wall(800, 445, 100, 20, main))   
    map5.add_entity(Wall(960, 390, 20, 20, main))    
    map5.add_entity(Wall(800, 325, 100, 20, main))
    map5.add_entity(Wall(650, 260, 100, 20, main))
    map5.add_entity(Wall(500, 195, 100, 20, main))



    maps.append(map5)


    # ========================================================================
    # MAP 100: ENDING SCREEN
    # ========================================================================
    map100 = Map("ending", 400, 250)
    map100.add_entity(EndingScreen(
        lambda: main.select_map(1),              # Replay button: restart from level 1
        lambda: main.select_map(0),              # Menu button: return to main menu
        lambda: __import__('sys').exit()         # Quit button: exit game
    ))
    maps.append(map100)

    # ========================================================================
    # MAP 101: SETTINGS SCREEN
    # ========================================================================
    map101 = Map("settings", 400, 250)
    SettingsMap(main, map101)
    maps.append(map101)

    return maps
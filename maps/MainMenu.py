from maps.Map import Map
from entities.Wall import Wall
from entities.TextEntity import TextEntity

class MainMenu(Map):
    def __init__(self, main):
        super().__init__("MainMenu", 400, 250, 40, 130, 335, 130)
        self.setup(main)

    def setup(self, main):
        self.add_entity(Wall(0, 240, 400, 10, main))
        
        # Title
        self.add_entity(TextEntity(200, 30, "MERGE CONFLICT", main, (255, 255, 255), 52, center=True))
        
        # Subtitle
        self.add_entity(TextEntity(200, 70, "A Two-Player Cooperative Platformer", main, (200, 200, 200), 22, center=True))
        
        # Menu options
        self.add_entity(TextEntity(200, 110, "[P] Play Game", main, (255, 255, 100), 32, center=True))
        self.add_entity(TextEntity(200, 145, "[S] Settings", main, (100, 200, 255), 32, center=True))
        self.add_entity(TextEntity(200, 180, "[Q] Quit", main, (255, 150, 150), 32, center=True))
        
        # Instructions
        self.add_entity(TextEntity(200, 220, "Press key to select", main, (180, 180, 180), 18, center=True))
        
        # Version
        self.add_entity(TextEntity(365, 233, "v1.0", main, (100, 100, 100), 16))



from maps.Map import Map
from entities.Wall import Wall
from entities.TextEntity import TextEntity
from entities.Button import Button

class Settings(Map):
    def __init__(self, main):
        super().__init__("settings", 500, 250, 40, 130, 335, 130, no_player=True)
        self.setup(main)

    def setup(self, main):
        self.add_entity(Wall(0, 240, 400, 10, main))



        # player 1
        self.add_entity(Button(35, 20, main, "Back", is_big=False))
        self.add_entity(TextEntity(35, 110, main, 'Player 1', (200, 200, 200), has_bg=True))
        self.add_entity(TextEntity(0, 140, main, 'Jump', (255, 255, 255)))
        self.add_entity(TextEntity(0, 170, main, 'Left', (255, 255, 255)))
        self.add_entity(TextEntity(0, 200, main, 'Right', (255, 255, 255)))
        self.add_entity(Button(110, 140, main, "W", (200, 200, 200), is_big=False))
        self.add_entity(Button(110, 170, main, "A", (200, 200, 200), is_big=False))
        self.add_entity(Button(110, 200, main, "S", (200, 200, 200), is_big=False))


        # player 2
        self.add_entity(TextEntity(345, 110, main, 'Player 2', (200, 200, 200), has_bg=True))
        self.add_entity(TextEntity(310, 140, main, 'Jump', (255, 255, 255)))
        self.add_entity(TextEntity(310, 170, main, 'Left', (255, 255, 255)))
        self.add_entity(TextEntity(310, 200, main, 'Right', (255, 255, 255)))
        self.add_entity(Button(420, 140, main, "UP_ARROW", (200, 200, 200), is_big=False))
        self.add_entity(Button(420, 170, main, "L_ARROW", (200, 200, 200), is_big=False))
        self.add_entity(Button(420, 200, main, "R_ARROW", (200, 200, 200), is_big=False))


        # fps
        self.add_entity(TextEntity(195, 110, main, "FPS", (200, 200, 200), has_bg=True))
        self.add_entity(Button(195, 135, main, "-", (255, 255, 255), is_big=False))
        self.add_entity(Button(235, 135, main, "60", (200, 200, 200), is_big=False))
        self.add_entity(Button(275, 135, main, "+", (255, 255, 255), is_big=False))

        # volume
        self.add_entity(TextEntity(195, 175, main, "Volume", (200, 200, 200), has_bg=True))
        self.add_entity(Button(195, 200, main, "-", (255, 255, 255), is_big=False))
        self.add_entity(Button(235, 200, main, "100%", (200, 200, 200), is_big=False))
        self.add_entity(Button(275, 200, main, "+", (255, 255, 255), is_big=False))

        # full screen
        self.add_entity(Button(340, 30, main, "Full Screen", (200, 200, 200)))





    def update_map(self, past_time, events):



        pass
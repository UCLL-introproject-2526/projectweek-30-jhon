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

        self.add_entity(Button(200, 120, main, None, "Play", (0, 255, 0), (0, 0, 0), "start", is_big=False))



        # self.add_entity(Button(200, 110, main, None, "Play", (0, 255, 0), (0, 0, 0), "start"))
        # self.add_entity(Button(200, 140, main, None, "Quit", (0, 255, 0), (0, 0, 0), "quit"))

    def update_map(self, past_time, events):
        pass
        # if self.get_entity_by_id('start').is_clicked():
        #     self.get_entity_by_id('start').main.next_map()
        #
        # if self.get_entity_by_id('quit').is_clicked():
        #     self.get_entity_by_id('quit').main.quit()


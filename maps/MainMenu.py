from maps.Map import Map
from entities.Wall import Wall
from entities.TextEntity import TextEntity
from entities.Button import Button

class MainMenu(Map):
    def __init__(self, main):
        super().__init__("MainMenu", 500, 250, 40, 130, 335, 130, no_player=True)
        self.setup(main)

    def setup(self, main):
        self.add_entity(Wall(0, 240, 400, 10, main))

        self.add_entity(Button(200, 120, main, "Play", id="start"))
        self.add_entity(Button(200, 160, main, "Settings", id="settings"),)
        self.add_entity(Button(200, 200, main, "Quit", id="quit"))

    def update_map(self, past_time, events):
        if self.get_entity_by_id('start').is_clicked():
            self.get_entity_by_id('start').main.next_map()

        if self.get_entity_by_id('quit').is_clicked():
            self.get_entity_by_id('quit').main.quit()

        if self.get_entity_by_id('settings').is_clicked():
            self.get_entity_by_id('settings').main.settings()


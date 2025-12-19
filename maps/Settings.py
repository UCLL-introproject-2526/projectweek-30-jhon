import pygame.key

from maps.Map import Map
from entities.Wall import Wall
from entities.TextEntity import TextEntity
from entities.Button import Button
from tools.SoundLibrary import musik, sound_library


class Settings(Map):
    def __init__(self, main):
        super().__init__(main, "settings", 500, 250, 40, 130, 335, 130, no_player=True)
        self.setup(main)
        self.__keymap_p1 = None
        self.__keymap_p2 = None
        self.__selected_key = None

    def setup(self, main):
        self.add_entity(Wall(0, 240, 400, 10, main))

        # player 1
        self.add_entity(Button(35, 20, main, "Back", is_big=False, id="back"))
        self.add_entity(TextEntity(35, 110, main, 'Player 1', (200, 200, 200), has_bg=True))
        self.add_entity(TextEntity(0, 140, main, 'Jump', (255, 255, 255)))
        self.add_entity(TextEntity(0, 170, main, 'Left', (255, 255, 255)))
        self.add_entity(TextEntity(0, 200, main, 'Right', (255, 255, 255)))
        self.add_entity(Button(110, 140, main, "W", (200, 200, 200), is_big=False, id='p1j', callback=lambda: self.select_key(0, 'jump')))
        self.add_entity(Button(110, 170, main, "A", (200, 200, 200), is_big=False, id='p1l', callback=lambda: self.select_key(0, 'left')))
        self.add_entity(Button(110, 200, main, "S", (200, 200, 200), is_big=False, id='p1r', callback=lambda: self.select_key(0, 'right')))


        # player 2
        self.add_entity(TextEntity(345, 110, main, 'Player 2', (200, 200, 200), has_bg=True))
        self.add_entity(TextEntity(310, 140, main, 'Jump', (255, 255, 255)))
        self.add_entity(TextEntity(310, 170, main, 'Left', (255, 255, 255)))
        self.add_entity(TextEntity(310, 200, main, 'Right', (255, 255, 255)))
        self.add_entity(Button(420, 140, main, "UP_ARROW", (200, 200, 200), is_big=False, id='p2j', callback=lambda: self.select_key(1, 'jump')))
        self.add_entity(Button(420, 170, main, "L_ARROW", (200, 200, 200), is_big=False, id='p2l', callback=lambda: self.select_key(1, 'left')))
        self.add_entity(Button(420, 200, main, "R_ARROW", (200, 200, 200), is_big=False, id='p2r', callback=lambda: self.select_key(1, 'right')))


        # fps
        self.add_entity(TextEntity(195, 110, main, "FPS", (200, 200, 200), has_bg=True))
        self.add_entity(Button(195, 135, main, "-", (255, 255, 255), is_big=False, callback=self.reduce_fps))
        self.add_entity(Button(235, 135, main, "60", (200, 200, 200), is_big=False, id="fps", is_animated=False))
        self.add_entity(Button(275, 135, main, "+", (255, 255, 255), is_big=False, callback=self.increase_fps))

        # volume
        self.add_entity(TextEntity(195, 175, main, "Volume", (200, 200, 200), has_bg=True))
        self.add_entity(Button(195, 200, main, "-", (255, 255, 255), is_big=False, callback=self.reduce_volume))
        self.add_entity(Button(235, 200, main, "100%", (200, 200, 200), is_big=False, is_animated=False, id='volume'))
        self.add_entity(Button(275, 200, main, "+", (255, 255, 255), is_big=False, callback=self.increase_volume))

        # full screen
        self.add_entity(Button(340, 30, main, "Full Screen", (200, 200, 200)))

    def select_key(self, player, key):
        self.__selected_key = (player, key)

    def key_already_selected(self, key):
        keys = [
            self.__keymap_p1.jump,
            self.__keymap_p1.left,
            self.__keymap_p1.right,
            self.__keymap_p2.jump,
            self.__keymap_p2.left,
            self.__keymap_p2.right
        ]
        return key in keys

    def enter_key(self, key):
        if self.__selected_key is not None and not self.key_already_selected(key):
            key_map = self.__keymap_p1 if self.__selected_key[0] == 0 else self.__keymap_p2
            if self.__selected_key[1] == 'left':
                key_map.left = key
            elif self.__selected_key[1] == 'right':
                key_map.right = key
            elif self.__selected_key[1] == 'jump':
                key_map.jump = key
        self.__selected_key = (key, key)

    def reduce_fps(self):
        print("Reducing FPS")
        self.main.set_fps(self.main.get_fps() - 5)

    def increase_fps(self):
        print("Increasing FPS")
        self.main.set_fps(self.main.get_fps() + 5)

    def reduce_volume(self):
        musik.set_volume(musik.get_volume() - 5)
        sound_library.set_volume(musik.get_volume() - 5)

    def increase_volume(self):
        musik.set_volume(musik.get_volume() + 5)
        sound_library.set_volume(musik.get_volume() + 5)

    def update(self, past_time, events):
        if self.__keymap_p1 is None or self.__keymap_p2 is None:
            self.__keymap_p1 = self.main.get_p1().controls
            self.__keymap_p2 = self.main.get_p2().controls
        for event in events:
            if event.type == pygame.KEYDOWN:
                self.enter_key(event.key)

        self.get_entity_by_id('fps').set_text(str(self.main.get_fps()))
        if self.get_entity_by_id('back').is_clicked():
            self.main.map(0)

        self.get_entity_by_id('p1j').set_text(pygame.key.name(self.__keymap_p1.jump))
        self.get_entity_by_id('p1j').set_color((255, 255, 255) if self.__selected_key == (0, 'jump') else (200, 200, 200))
        self.get_entity_by_id('p1l').set_text(pygame.key.name(self.__keymap_p1.left))
        self.get_entity_by_id('p1l').set_color((255, 255, 255) if self.__selected_key == (0, 'left') else (200, 200, 200))
        self.get_entity_by_id('p1r').set_text(pygame.key.name(self.__keymap_p1.right))
        self.get_entity_by_id('p1r').set_color((255, 255, 255) if self.__selected_key == (0, 'right') else (200, 200, 200))
        self.get_entity_by_id('p2j').set_text(pygame.key.name(self.__keymap_p2.jump))
        self.get_entity_by_id('p2j').set_color((255, 255, 255) if self.__selected_key == (1, 'jump') else (200, 200, 200))
        self.get_entity_by_id('p2l').set_text(pygame.key.name(self.__keymap_p2.left))
        self.get_entity_by_id('p2l').set_color((255, 255, 255) if self.__selected_key == (1, 'left') else (200, 200, 200))
        self.get_entity_by_id('p2r').set_text(pygame.key.name(self.__keymap_p2.right))
        self.get_entity_by_id('p2r').set_color((255, 255, 255) if self.__selected_key == (1, 'right') else (200, 200, 200))

        self.get_entity_by_id('volume').set_text(str(musik.get_volume()))

    def restart(self):
        self.__selected_key = None


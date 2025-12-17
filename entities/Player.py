# from entities.Entity import Entity
from entities.Entity import Entity
import tools.importer

# temporary movement to test maps (movement.py)
from garbage.Movement import Movement
# -----------------------------
from settings.keyboard_layout import keybinds_player1, keybinds_player2
import pygame

from SoundLibrary import SoundLibrary

class Player(Entity):
    def __init__(self, x, y, main, keybinds):
        super().__init__(x, y, 15 , 25, main, solid=False, gravitation=1, name="Player")
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.__sound_library = SoundLibrary()
        self.__footstep_cooldown = 0
        self.__footstep_delay = 0.3

        self.__textures = []
        if keybinds == 1:
            self.controls = keybinds_player1()
            self.__textures.append(tools.importer.image("assets/textures/entities/Player/Player_01.png"))
            self.__textures.append(tools.importer.image("assets/textures/entities/Player/Player_01_Left.png"))
            self.__textures.append(tools.importer.image("assets/textures/entities/Player/Player_01_Right.png"))
        else:
            self.controls = keybinds_player2()
            self.__textures.append(tools.importer.image("assets/textures/entities/Player/Player_02.png"))
            self.__textures.append(tools.importer.image("assets/textures/entities/Player/Player_02_Left.png"))
            self.__textures.append(tools.importer.image("assets/textures/entities/Player/Player_02_Right.png"))

    def get_texture(self):
        if not self.moving_right and not self.moving_left or (self.moving_right and self.moving_left):
            return self.__textures[0]
        elif self.moving_right:
            self.speed_x = 3
            return self.__textures[2]
        elif self.moving_left:
            self.speed_x = -3
            return self.__textures[1]
        return self.__textures[0]

    def game_loop(self, delta_time, events):
        self.calc_movement(delta_time)
        self.keyboard_input(events)

        if self.on_floor and self.moving_up:
            self.speed_y = -10
            self.__sound_library.play('jump')
        if not self.moving_right and not self.moving_left or (self.moving_right and self.moving_left):
            self.speed_x = 0
        elif self.moving_right:
            self.speed_x = 3
        elif self.moving_left:
            self.speed_x = -3
        # Walking sound
        if self.on_floor and (self.moving_right or self.moving_left):
            if self.__footstep_cooldown <= 0:
                self.__sound_library.play('footstep')
                self.__footstep_cooldown = self.__footstep_delay
        self.__footstep_cooldown -= delta_time

        if self.get_y() > self.main.get_current_map().get_height() + self.get_height():
            self.__sound_library.play('willhelm')
            self.player_death()

    def player_death(self):
        self.main.restart_map()

    def keyboard_input(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == self.controls["jump"]:
                    self.moving_up = True
                if event.key == self.controls["left"]:
                    self.moving_left = True
                if event.key == self.controls["right"]:
                    self.moving_right = True
            if event.type == pygame.KEYUP:
                if event.key == self.controls["left"]:
                    self.moving_left = False
                if event.key == self.controls["right"]:
                    self.moving_right = False
                if event.key == self.controls["jump"]:
                    self.moving_up = False

    def detect_merge(self):
        for entity in self.main.get_current_map().get_entities():
            if entity.get_name() == "Player" and entity is not self:
                print("MERGEEEEE")


    def run_with_delay(self):
        print("value")
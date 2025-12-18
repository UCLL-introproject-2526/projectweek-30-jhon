import pygame
from entities.Entity import Entity
from tools.SoundLibrary import SoundLibrary
import tools.importer
from settings import keyboard_layout


class Player(Entity):
    def __init__(self,x ,y ,main, player_name):
        super().__init__(x,y,15,25, main, solid=False, gravitation=1)
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.player_name = player_name
        self.__sound_library = SoundLibrary()
        self.__footstep_cooldown = 0
        self.__footstep_delay = 0.3
        self.__textures = []

        if player_name == "p1":
            self.controls = Key_map(pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d)
            self.__textures.append(tools.importer.image("entities/player/Player_01.png"))
            self.__textures.append(tools.importer.image("entities/player/Player_01_left.png"))
            self.__textures.append(tools.importer.image("entities/player/Player_01_right.png"))
        else:
            self.controls = Key_map(pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT)
            self.__textures.append(tools.importer.image("entities/player/Player_02.png"))
            self.__textures.append(tools.importer.image("entities/player/Player_02_right.png"))
            self.__textures.append(tools.importer.image("entities/player/Player_02_left.png"))

    def player_death(self):
        self.main.restart_map()

    def get_player_name(self):
        return self.player_name


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
        self.detect_merge()
        self.calc_movement(delta_time)
        self.keyboard_input(events)


        # keyboard input
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

        if self.y > self.main.get_current_map().get_height() + self.height:
            self.__sound_library.play('willhelm')
            self.player_death()

    def keyboard_input(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == self.controls.jump:
                    self.moving_up = True
                if event.key == self.controls.left:
                    self.moving_left = True
                if event.key == self.controls.right:
                    self.moving_right = True
            if event.type == pygame.KEYUP:
                if event.key == self.controls.left:
                    self.moving_left = False
                if event.key == self.controls.right:
                    self.moving_right = False
                if event.key == self.controls.jump:
                    self.moving_up = False

    def detect_merge(self):
        for entity in self.main.get_current_map().get_entities():
            if isinstance(entity, Player) and entity is not self:
                if self.collision(entity):
                    self.__sound_library.play('merge')
                    self.main.next_map()

    def reset_movement(self):
        self.moving_right = False
        self.moving_left = False


class Key_map:
    def __init__(self, jump, sneak, left, right):
        self.jump = jump
        self.sneak = sneak
        self.left = left
        self.right = right

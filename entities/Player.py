# from entities.Entity import Entity
from entities.Entity import Entity
import tools.importer

# temporary movement to test maps (movement.py)
from entities.Movement import Movement
# -----------------------------
from settings.keyboard_layout import keybinds_player1, keybinds_player2
import pygame

from SoundLibrary import SoundLibrary

class Player(Entity):
    def __init__(self, x, y, main, keybinds):
        super().__init__(x, y, 15 , 25, main, solid=True, gravitation=1)
        self.__main = main
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.__sound_library = SoundLibrary()
        self.__footstep_cooldown = 0
        self.__footstep_delay = 0.3




        self.velocity_y = 0
        self.on_ground = True
        self.gravity = 1
        self.speed = 3
        if keybinds == 1:
            self.controls = keybinds_player1()
            texture_path = "assets/textures/entities/Player/Player_01.png"
        else:
            self.controls = keybinds_player2()
            texture_path = "assets/textures/entities/Player/Player_02.png"
        self.__texture = pygame.image.load(texture_path).convert_alpha()



        self.__textures = [
            tools.importer.image("assets/textures/entities/Player/Player_01.png"),
            tools.importer.image("assets/textures/entities/Player/Player_01_Left.png"),
            tools.importer.image("assets/textures/entities/Player/Player_01_Right.png"),
        ]
        # Track previous position for collision resolution; updated at start of each game loop
        self.prev_x = self.get_x()
        self.prev_y = self.get_y()
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
    
 #    def move(self, keys):
 #        if keys[self.controls["left"]]:
 #            self.set_x(self.get_x() - self.speed)
 #        if keys[self.controls["right"]]:
 #            self.set_x(self.get_x() + self.speed)
 #
 #    def jump(self):
 #        self.__speed_y -= 120
 #        print("evenEJKKNKNNK")
 # #        if self.on_ground:
 # #            self.velocity_y = -20
 # #            self.on_ground = False

    # def apply_gravity(self):
    #     self.velocity_y += self.gravity
    #     self.set_y(self.get_y() + self.velocity_y)
    #
    # def save_prev_position(self):
    #     self.prev_x = self.get_x()
    #     self.prev_y = self.get_y()

    def game_loop(self, delta_time, events):
        self.calc_movement(delta_time)
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
        print(f"aktivated: {self.moving_left}, {self.moving_right}, {self.moving_up}")
        if self.on_floor and self.moving_up:
            self.speed_y = -10
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



        # # Save previous position for collision resolution
        # self.save_prev_position()
        # # Get input and handle movement
        # keys = pygame.key.get_pressed()
        # Movement.handle_movement(self, keys)
        #
        # # Apply gravity
        # Movement.handle_gravity(self)
        #
        # # Check collisions with walls
        # Movement.check_wall_collisions(self, self.__main)
        #
        # # Handle jump input
        # for event in events:
        #     if event.type == pygame.KEYDOWN:
        #         if event.key == self.controls["jump"]:
        #             Movement.handle_jump(self)

    def run_with_delay(self):
        print("value")
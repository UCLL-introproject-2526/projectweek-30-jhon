# from entities.Entity import Entity
from entities.Entity import Entity

# temporary movement to test maps (movement.py)
from entities.Movement import Movement
# -----------------------------
from settings.keyboard_layout import keybinds_player1, keybinds_player2
import pygame
from tools.importer import image as import_image

class Player(Entity):
    def __init__(self, x, y, main, keybinds):
        super().__init__(x, y, 15 , 25, main, solid=True, gravitation=1)
        self.__main = main
        self.velocity_y = 0
        self.on_ground = True
        self.gravity = 1
        self.speed = 3
        self.direction = 'right'
        self.__textures = {}
        if keybinds == 1:
            self.controls = keybinds_player1()
            base = "assets/textures/entities/player/Player_01.png"
            left = "assets/textures/entities/player/Player_01_Left.png"
            right = "assets/textures/entities/player/Player_01_Right.png"
        else:
            self.controls = keybinds_player2()
            base = "assets/textures/entities/player/Player_02.png"
            left = "assets/textures/entities/player/Player_02_Left.png"
            right = "assets/textures/entities/player/Player_02_Right.png"

        # Load textures (fallback if directional files are missing)
        base_img = import_image(base, True)
        left_img = import_image(left, True) if pygame.image.get_extended() else base_img
        right_img = import_image(right, True) if pygame.image.get_extended() else base_img

        self.__textures = {
            'idle': base_img,
            'left': left_img,
            'right': right_img
        }
        self.__texture = self.__textures.get(self.direction, base_img)
        # Track previous position for collision resolution; updated at start of each game loop
        self.prev_x = self.get_x()
        self.prev_y = self.get_y()
    def get_texture(self):
        # Return texture based on current facing direction
        return self.__textures.get(self.direction, self.__textures['idle'])

    def set_direction(self, direction):
        if direction in ('left', 'right', 'idle'):
            self.direction = direction
    
    def move(self, keys):
        if keys[self.controls["left"]]:
            self.set_x(self.get_x() - self.speed)
            self.set_direction('left')
        if keys[self.controls["right"]]:
            self.set_x(self.get_x() + self.speed)
            self.set_direction('right')   

    def jump(self):
        self.__speed_y -= 120
        print("evenEJKKNKNNK")
 #        if self.on_ground:
 #            self.velocity_y = -20
 #            self.on_ground = False

    def apply_gravity(self):
        self.velocity_y += self.gravity
        self.set_y(self.get_y() + self.velocity_y)

    def save_prev_position(self):
        self.prev_x = self.get_x()
        self.prev_y = self.get_y()

    def game_loop(self, delta_time, events):
        # Save previous position for collision resolution
        self.save_prev_position()
        # Get input and handle movement
        keys = pygame.key.get_pressed()
        Movement.handle_movement(self, keys)
        
        # Apply gravity
        Movement.handle_gravity(self)
        
        # Check collisions with walls
        Movement.check_wall_collisions(self, self.__main)
        
        # Handle jump input
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == self.controls["jump"]:
                    Movement.handle_jump(self)

    def run_with_delay(self):
        print("value")
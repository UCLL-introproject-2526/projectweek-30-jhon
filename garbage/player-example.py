import pygame
import sys

pygame.init()

# Window settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("JHON")
clock = pygame.time.Clock()

# --- PHYSICS ---
# class Physics:
#     def __init__(self, gravity=1):
#         self.gravity = gravity

#     def apply_gravity(self, entity):
#         x, y, width, height = entity.get_render_data()
#         entity.set_height(height + self.gravity)
    
#     def get_gravity(self):
#         return self.gravity



# ----- BLOCK CLASS -----
class Block:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def collide(self, player):
        # Horizontal collision
        if player.rect.colliderect(self.rect):
            if player.rect.right > self.rect.left and player.rect.left < self.rect.left:
                player.rect.right = self.rect.left
            elif player.rect.left < self.rect.right and player.rect.right > self.rect.right:
                player.rect.left = self.rect.right

        # Vertical collision
        if player.rect.colliderect(self.rect):
            if player.velocity_y > 0 and player.rect.bottom >= self.rect.top:
                player.rect.bottom = self.rect.top
                player.velocity_y = 0
                player.on_ground = True
            elif player.velocity_y < 0 and player.rect.top <= self.rect.bottom:
                player.rect.top = self.rect.bottom
                player.velocity_y = 0

class Player:
    def __init__(self, x, y, color, controls):
        self.rect = pygame.Rect(x, y, 40, 40)
        self.color = color
        self.controls = controls
        self.speed = 4

        self.velocity_y = 0
        self.on_ground = False
        self.gravity = 1


    def move(self, keys):
        if keys[self.controls["left"]]:
            self.rect.x -= self.speed
        if keys[self.controls["right"]]:
            self.rect.x += self.speed


    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def dont_go_outside(self):
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
            self.velocity_y = 0
            self.on_ground = True

    def jump(self):
        if self.on_ground:
            self.velocity_y = -25
            self.on_ground = False

    def apply_gravity(self):
        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y

    
    



def collide_all_blocks(player, blocks):
    for block in blocks:
        block.collide(player)

# ----- CREATE BLOCKS -----
block1 = Block(200, 500, 400, 20, (100, 100, 100))
block2 = Block(0, 300, 300, 20, (100, 100, 100))
blocks = [block1, block2]

# ----- CREATE PLAYERS -----
fire = Player(
    100, 400,
    (255, 100, 0),
    {"left": pygame.K_LEFT, "right": pygame.K_RIGHT, "up": pygame.K_UP, "down": pygame.K_DOWN}
)

water = Player(
    600, 400,
    (0, 150, 255),
    {"left": pygame.K_a, "right": pygame.K_d, "up": pygame.K_w, "down": pygame.K_s}
)

# Merge zone
merge_zone = pygame.Rect(360, 520, 80, 40)

# ----- GAME LOOP -----
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == fire.controls["up"]:
                fire.jump()
            if event.key == water.controls["up"]:
                water.jump()
        

    keys = pygame.key.get_pressed()

    # Move players
    fire.move(keys)
    water.move(keys)

    fire.apply_gravity()
    water.apply_gravity()

    fire.dont_go_outside()
    water.dont_go_outside()

    # Collision with blocks
    collide_all_blocks(fire, blocks)
    collide_all_blocks(water, blocks)

    # Draw
    screen.fill((30, 30, 30))
    pygame.draw.rect(screen, (0, 255, 0), merge_zone)

    for block in blocks:
        block.draw(screen)

    fire.draw(screen)
    water.draw(screen)

    # Merge check
    if fire.rect.colliderect(merge_zone) and water.rect.colliderect(merge_zone):
        print("LEVEL COMPLETE!")
        running = False

    pygame.display.flip()

pygame.quit()
sys.exit()

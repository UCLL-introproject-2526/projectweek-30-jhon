import pygame
import sys

pygame.init()

# Window settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("JHON")
clock = pygame.time.Clock()

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
            if player.rect.bottom > self.rect.top and player.rect.top < self.rect.top:
                player.rect.bottom = self.rect.top
            elif player.rect.top < self.rect.bottom and player.rect.bottom > self.rect.bottom:
                player.rect.top = self.rect.bottom

class Player:
    def __init__(self, x, y, color, controls):
        self.rect = pygame.Rect(x, y, 40, 40)
        self.color = color
        self.controls = controls
        self.speed = 4

    def move(self, keys):
        # Horizontal movement
        if keys[self.controls["left"]] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[self.controls["right"]] and self.rect.x < WIDTH - self.rect.width:
            self.rect.x += self.speed
        # Vertical movement
        if keys[self.controls["up"]] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[self.controls["down"]] and self.rect.y < HEIGHT - self.rect.height:
            self.rect.y += self.speed

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

def collide_all_blocks(player, blocks):
    for block in blocks:
        block.collide(player)

# ----- CREATE BLOCKS -----aaaaa
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

    keys = pygame.key.get_pressed()

    # Move players
    fire.move(keys)
    water.move(keys)

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
    if fire.rect.colliderect(merge_zone) and water.rect.colliderect(merge_zone) and abs(fire.rect.centerx - water.rect.centerx) < 40:
        print("LEVEL COMPLETE!")
        running = False

    pygame.display.flip()

pygame.quit()
sys.exit()

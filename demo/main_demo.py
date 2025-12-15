import pygame
import sys

from settings import *
from player import Player
from block import Block

def collide_all_blocks(player, blocks):
    for block in blocks:
        block.collide(player)

# ----- CREATE BLOCKS -----
blocks = [
    Block(200, 500, 400, 20, BLOCK_COLOR),
    Block(0, 300, 300, 20, BLOCK_COLOR)
]

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

merge_zone = pygame.Rect(360, 520, 80, 40)

# ----- GAME LOOP -----
running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    fire.move(keys)
    water.move(keys)

    collide_all_blocks(fire, blocks)
    collide_all_blocks(water, blocks)

    screen.fill(DARK_BG)
    pygame.draw.rect(screen, (0, 255, 0), merge_zone)

    for block in blocks:
        block.draw(screen)

    fire.draw(screen)
    water.draw(screen)

    if fire.rect.colliderect(merge_zone) and water.rect.colliderect(merge_zone):
        print("LEVEL COMPLETE!")
        running = False

    pygame.display.flip()

pygame.quit()
sys.exit()

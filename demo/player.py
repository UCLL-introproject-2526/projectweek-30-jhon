import pygame
from settings import WIDTH, HEIGHT

class Player:
    def __init__(self, x, y, color, controls):
        self.rect = pygame.Rect(x, y, 40, 40)
        self.color = color
        self.controls = controls
        self.speed = 4

    def move(self, keys):
        if keys[self.controls["left"]] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[self.controls["right"]] and self.rect.right < WIDTH:
            self.rect.x += self.speed
        if keys[self.controls["up"]] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[self.controls["down"]] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

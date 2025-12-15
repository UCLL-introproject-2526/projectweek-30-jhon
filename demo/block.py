import pygame

class Block:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def collide(self, player):
        if player.rect.colliderect(self.rect):
            # Horizontal
            if player.rect.right > self.rect.left and player.rect.left < self.rect.left:
                player.rect.right = self.rect.left
            elif player.rect.left < self.rect.right and player.rect.right > self.rect.right:
                player.rect.left = self.rect.right

            # Vertical
            if player.rect.bottom > self.rect.top and player.rect.top < self.rect.top:
                player.rect.bottom = self.rect.top
            elif player.rect.top < self.rect.bottom and player.rect.bottom > self.rect.bottom:
                player.rect.top = self.rect.bottom

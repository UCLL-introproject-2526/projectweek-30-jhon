# ------------ class block ----------------------------------------
import pygame

class Block:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def collide(self, entity):
        if not entity.rect.colliderect(self.rect):
            return

        overlap_left = entity.rect.right - self.rect.left
        overlap_right = self.rect.right - entity.rect.left
        overlap_top = entity.rect.bottom - self.rect.top
        overlap_bottom = self.rect.bottom - entity.rect.top

        min_overlap = min(overlap_left, overlap_right, overlap_top, overlap_bottom)

        if min_overlap == overlap_left:
            entity.rect.right = self.rect.left
        elif min_overlap == overlap_right:
            entity.rect.left = self.rect.right
        elif min_overlap == overlap_top:
            entity.rect.bottom = self.rect.top
        elif min_overlap == overlap_bottom:
            entity.rect.top = self.rect.bottom

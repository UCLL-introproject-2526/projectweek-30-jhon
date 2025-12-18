import pygame

def image(path, is_alpha = True):
    if is_alpha:
        return pygame.image.load(f"assets/textures/{path}").convert_alpha()
    return pygame.image.load(f"assets/textures/{path}").convert()

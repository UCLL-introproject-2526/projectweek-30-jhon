import pygame

keyboard_layout = {
    "p1": {
        "azerty": {
            "up" : pygame.K_z,
            "down" : pygame.K_s,
            "left" : pygame.K_q,
            "right" : pygame.K_d
        },
        "query": {
            "up" : pygame.K_w,
            "down" : pygame.K_s,
            "left" : pygame.K_a,
            "right" : pygame.K_d
        }
    },
    "p2": {
        "azerty": {
            "up" : pygame.K_UP,
            "down" : pygame.K_DOWN,
            "left" : pygame.K_LEFT,
            "right" : pygame.K_RIGHT
        },
        "query": {
            "up" : pygame.K_UP,
            "down" : pygame.K_DOWN,
            "left" : pygame.K_LEFT,
            "right" : pygame.K_RIGHT
        }
    }
}
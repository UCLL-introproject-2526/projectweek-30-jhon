import pygame
keyboard_layout = "querty"
def keybinds_player1():
    if keyboard_layout == "azerty":
        return {"left": pygame.K_q, "right": pygame.K_d, "jump": pygame.K_z}
    elif keyboard_layout == "qwerty":
        return {"left": pygame.K_a, "right": pygame.K_d, "jump": pygame.K_w}
def keybinds_player2():
    return {"left": pygame.K_LEFT, "right": pygame.K_RIGHT, "jump": pygame.K_UP}
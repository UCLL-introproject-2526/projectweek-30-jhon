import pygame

# def play_sound(sound):
#     sfx = pygame.mixer.Sound(f'assets/audio/{sound}')
#     pygame.mixer.Sound.play()

class SoundLibrary:
    def __init__(self):
        self.sfx = {
            'footstep': 'sfx/footstep.wav',
        }
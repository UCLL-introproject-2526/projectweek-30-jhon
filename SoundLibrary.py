import pygame

class SoundLibrary:
    def __init__(self):
        self.sfx = {
            'footstep': 'sfx/footstep.wav',
        }
        self.__load_sounds()


    def __load_sounds(self):
        self.loaded_sfx = {}
        for key, path in self.sfx.items():
            self.loaded_sfx[key] = pygame.mixer.Sound(f'assets/audio/{path}')
            

    def play(self, sfx_name):
        if sfx_name in self.loaded_sfx:
            pygame.mixer.Sound.play(self.loaded_sfx[sfx_name])

    def sound_loop(self, past_time):
        pass


import pygame

class SoundLibrary:
    def __init__(self):
        self.sfx = {
            'footstep': 'footstep.wav',
        }
        self.tracks = {
            'background1': 'soft-background-music-409193.mp3'
        }
        self.loaded_sfx = {}
        self.current_track = None
        self.__load_sounds()


    def __load_sounds(self):
        for key, path in self.sfx.items():
            self.loaded_sfx[key] = pygame.mixer.Sound(f'assets/audio/sfx/{path}')

    def play(self, name):
        if name in self.loaded_sfx:
            pygame.mixer.Sound.play(self.loaded_sfx[name])
            return
        
        if name in self.tracks:
            if not pygame.mixer.music.get_busy() or self.current_track != name:
                pygame.mixer.music.load(f'assets/audio/music/{self.tracks[name]}')
                pygame.mixer.music.play()
                self.current_track = name

    def sound_loop(self, past_time):
        self.play('background1')
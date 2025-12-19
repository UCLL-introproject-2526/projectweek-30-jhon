import pygame
from pygame.examples.music_drop_fade import volume


class SoundLibrary:
    def __init__(self):
<<<<<<< Updated upstream
        self.sfx = {
            'footstep': 'footstep.wav',
            'jump': 'boink.wav',
            'willhelm': 'willhelm.wav',
            'spikestab': 'spikedeath.wav',
            'merge': 'slimeysfx.wav',
            'spikeretract': 'swordsheathing.wav',
            'wallmove': 'stoneslide.wav',
        }
        self.tracks = {
            'background1': 'soft-background-music-409193.mp3',
            'backgroundmain': 'please-calm-my-mind-125566.mp3',
        }
        self.loaded_sfx = {}
        self.current_track = None
        self.total_time = 0
        self.__load_sounds()
=======
        self.__sounds = []
        self.__volume = 100

    def play(self, path):
        for sound in self.__sounds:
            if sound.name == path:
                pygame.mixer.Sound.play(sound.sound)
                return
        sound = Sound(path)
        self.__sounds.append(sound)
        sound.sound.set_volume(sound.sound.base_volume * self.__volume / 100)

    def set_volume(self, volume):
        self.__volume = max(0, min(150, volume))
        for sound in self.__sounds:
            sound.sound.set_volume(sound.sound.base_volume * self.__volume / 100)

    def get_volume(self):
        return self.__volume

class Sound:
    def __init__(self, sound_name):
        self.name = sound_name
        self.sound = pygame.mixer.Sound(f'assets/audio/sfx/{sound_name}')
        pygame.mixer.Sound.play(self.sound)






class Musik:
    def __init__(self):
        self.__is_playing = None
        self.total_time = 0
        self.__volume = 100

    def set_volume(self, volume):
        self.__volume = min(150, max(0, volume))
        pygame.mixer.music.set_volume(volume / 100)


    def get_volume(self):
        return self.__volume
>>>>>>> Stashed changes

    def __load_sounds(self):
        for key, path in self.sfx.items():
            self.loaded_sfx[key] = pygame.mixer.Sound(f'assets/audio/sfx/{path}')

    def play(self, name):
        if name in self.loaded_sfx:
            pygame.mixer.Sound.play(self.loaded_sfx[name])
            return

        elif name in self.tracks:
            if not pygame.mixer.music.get_busy() or self.current_track != name:
                pygame.mixer.music.load(f'assets/audio/music/{self.tracks[name]}')
                pygame.mixer.music.play()
                self.current_track = name
        else:
            print("Unknown sound player name")

    def stop(self):
        pygame.mixer.music.stop()

    def pause(self):
        pygame.mixer.music.pause()

    def unpause(self):
        pygame.mixer.music.unpause()

    def sound_loop(self, past_time):
        self.total_time += past_time
        self.play('backgroundmain')
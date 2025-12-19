import pygame

class SoundLibrary:
    def __init__(self):
        self.__sounds = []
        self.current_volume = 1.0

    def play(self, path):
        for sound in self.__sounds:
            if sound.name == path:
                sound.sound.set_volume(self.current_volume)
                pygame.mixer.Sound.play(sound.sound)
                return
        self.__sounds.append(Sound(path, self.current_volume))

    def volume(self, volume):
        self.current_volume = volume / 100
        for sound in self.__sounds:
            sound.sound.set_volume(self.current_volume)
        print("setting sound volume to", volume)


class Sound:
    def __init__(self, sound_name, volume=1.0):
        self.name = sound_name
        self.sound = pygame.mixer.Sound(f'assets/audio/sfx/{sound_name}')
        self.sound.set_volume(volume)
        pygame.mixer.Sound.play(self.sound)


class Musik:
    def __init__(self):
        self.__is_playing = None
        self.total_time = 0
        self.__volume = 100

    def play(self, path):
        if not pygame.mixer.music.get_busy() and self.__is_playing != path:
            print("musik playing")
            pygame.mixer.music.load(f'assets/audio/music/{path}')
            pygame.mixer.music.play()
            self.__is_playing = path

    def get_volume(self):
        return self.__volume

    def pause(self):
        pygame.mixer.music.pause()

    def unpause(self):
        pygame.mixer.music.unpause()

    def set_volume(self, volume):
        self.__volume = max(min(volume, 100), 0)
        # lol
        pygame.mixer.music.set_volume(volume / 100)
        sound_library.volume(self.__volume)

    def sound_loop(self, past_time):
        self.total_time += past_time
        self.play('soft-background-music-409193.mp3')


sound_library = SoundLibrary()
musik = Musik()
import pygame


class SoundLibrary:
    def __init__(self):
        self.__sounds = []

    def play(self, path):
        for sound in self.__sounds:
            if sound.name == path:
                pygame.mixer.Sound.play(sound.sound)
                return
        self.__sounds.append(Sound(path))

    def volume(self, volume):
        for sound in self.__sounds:
            sound.set_volume(sound.base_volume * volume)


class Sound:
    def __init__(self, sound_name):
        self.name = sound_name
        self.sound = pygame.mixer.Sound(f'assets/audio/sfx/{sound_name}')
        pygame.mixer.Sound.play(self.sound)






class Musik:
    def __init__(self):
        self.__is_playing = None
        self.total_time = 0

    def play(self, path):
        if not pygame.mixer.music.get_busy() and self.__is_playing != path:
            print("musik playing")
            pygame.mixer.music.load(f'assets/audio/music/{path}')
            pygame.mixer.music.play()
            self.__is_playing = path

    def pause(self):
        pygame.mixer.music.pause()

    def unpause(self):
        pygame.mixer.music.unpause()

    def set_volume(self, volume):
        pygame.mixer.music.set_volume(volume)

    def sound_loop(self, past_time):
        self.total_time += past_time
        self.play('soft-background-music-409193.mp3')




sound_library = SoundLibrary()
musik = Musik()
from entities.Entity import Entity
from entities.Player import Player
from tools.ImageLibary import image_library
from tools.SoundLibrary import sound_library


class Spike(Entity):
    def __init__(self, x, y, main):
        super().__init__(x, y, 16, 16, main)
        self.__has_blood = False
        self.textures = [
            'entities/spikes/Spike_model.png',
            'entities/spikes/Spike_model_blood.png',
        ]
        self.__active = True

    def get_texture(self):
        if self.__has_blood:
            return image_library.get_image(self.textures[1])
        return image_library.get_image(self.textures[0])

    def game_loop(self, past_time, events):
        if self.__active:
            for entity in self.main.get_current_map().get_entities():
                if self.collision(entity):
                    if isinstance(entity, Player):
                        entity.player_death()
                        self.__has_blood = True
                        self.play('swordsheathing.wav')


        pass

    def disable(self):
        if self.__active:
            self.__active = False
            self.height = 4
            self.move(0, 12)
            sound_library.play('spikedeath.wav')

    def enable(self):
        if not self.__active:
            self.__active = True
            self.height = 16
            self.move(0, -12)
            sound_library.play('spikedeath.wav')

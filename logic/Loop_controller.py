import pygame
from time import time
from logic.Render import Render
from SoundLibrary import SoundLibrary
from logic.Logic_runner import LogicManager

class Loop_controller:
    def __init__(self, main, name):
        self.fps = 1
        self.main = main
        self.__renderer = Render(name, 600, 260)
        self.__logic_manager = LogicManager(main)
        self.__sound_library = SoundLibrary()
        self.__time = time()

    def start(self):
        pygame.init()
        clock = pygame.time.Clock()

        while True:
            past_time = time() - self.__time
            print("past time:", past_time)
            self.__time = time()
            events = pygame.event.get()
            self.__sound_library.sound_loop(past_time)
            for event in events:
                if event.type == pygame.QUIT:
                    self.__renderer.quit()
                if event.type == pygame.FULLSCREEN:
                    self.__renderer.toggle_fullscreen()
            self.__logic_manager.execute_loop(past_time, events)

            self.__renderer.update(self.main)
            clock.tick(self.fps)

    def add_later_task(self, task, delay):
        self.__logic_manager.add_later_taks(task, delay)

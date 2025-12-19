import pygame
from time import time

from tools.Logic_runner import LogicManager
from tools.Render import Render
from tools.SoundLibrary import musik


class Loop_controller:
    def __init__(self, main):
        self.__fps = 60
        self.main = main
        pygame.init()
        self.__renderer = Render("Merge Conflict", 1200, 750)
        self.__logic_manager = LogicManager(main)
        self.__time = time()

    def get_fps(self):
        return self.__fps

    def set_fps(self, fps):
        self.__fps = max(10, min(fps, 120))

    def start(self):
        clock = pygame.time.Clock()

        while True:
            self.game_loop()
            clock.tick(self.__fps)

    def add_later_task(self, task, delay):
        self.__logic_manager.add_later_taks(task, delay)

    def quit(self):
        self.__renderer.quit()

    def game_loop(self):

        # runtime
        past_time = time() - self.__time
        self.__time = time()

        # events
        events = pygame.event.get()



        # loops

        # run sound loop
        musik.sound_loop(past_time)


        # listen to quit event
        for event in events:
            if event.type == pygame.QUIT:
                self.__renderer.quit()
            if event.type == pygame.FULLSCREEN:
                self.__renderer.toggle_fullscreen()
        self.__logic_manager.execute_loop(past_time, events)

        self.__renderer.update(self.main)

    def get_current_mouse_pos(self):
        return self.__renderer.get_cursor_position(self.main)
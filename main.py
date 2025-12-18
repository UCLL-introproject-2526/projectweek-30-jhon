from maps.MapManager import MapManager
from tools.Render import Render
from tools.Loop_controller import Loop_controller


class Main:
    def __init__(self):
        self.__loop_controller = Loop_controller(self)
        self.__map_manager = MapManager(self)
        self.__loop_controller.start()


    def get_current_map(self):
        return self.__map_manager.get_current_map()

    def add_delayed_task(self, task, delay):
        self.__loop_controller.add_later_task(task, delay)

    def next_map(self):
        self.__map_manager.next_map()

    def restart_map(self):
        self.__map_manager.reset_map()

    def open_settings(self):
        self.__map_manager.settings()

    def get_mouse_pos(self):
        return self.__loop_controller.get_current_mouse_pos()

    def quit(self):
        self.__loop_controller.quit()

    def settings(self):
        self.__map_manager.settings()
Main()
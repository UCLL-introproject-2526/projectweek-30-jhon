import asyncio
from maps.MapManager import MapManager
from tools.Render import Render
from tools.Loop_controller import Loop_controller


class Main:
    def __init__(self):
        self.__loop_controller = Loop_controller(self)
        self.__map_manager = MapManager(self)
        asyncio.create_task(self.__loop_controller.start())


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
    
    def back_from_settings(self):
        self.__map_manager.back_from_settings()

    def map(self, number):
        self.__map_manager.select_map(0)

    def get_fps(self):
        return self.__loop_controller.get_fps()

    def set_fps(self, fps):
        self.__loop_controller.set_fps(fps)

    def get_p1(self):
        return self.__map_manager.get_p1()

    def get_p2(self):
        return self.__map_manager.get_p2()

async def main():
    game = Main()
    await asyncio.sleep(0)
    while True:
        await asyncio.sleep(0)

asyncio.run(main())
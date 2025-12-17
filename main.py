from logic.Loop_controller import Loop_controller
from config import build_maps

class Main:
    def __init__(self):
        self.__loop_controller = Loop_controller(self, "Merge Conflict")
        self.__maps = build_maps(self)
        self.__selected_map = 0
        self.__loop_controller.start()
    def get_current_map(self):
        return self.__maps[self.__selected_map]
    
    def select_map(self, index):
        if 0 <= index < len(self.__maps):
            self.__selected_map = index

    def next_map(self):
        self.__selected_map += 1
        if self.__selected_map >= len(self.__maps):
            self.__selected_map = 0

    def add_later_task(self, task, delay):
        self.__loop_controller.add_later_task(task, delay)

    def restart_map(self):
        # Rebuild maps to reset all entity state and ensure pressure plates work again
        print(f"selectedMap: {self.__selected_map}, {len(self.__maps)}")
        current_map_index = self.__selected_map  # Save current map before rebuild
        self.__maps = build_maps(self)
        self.__selected_map = current_map_index  # Restore position on same map
        print(f"Now selectedMap: {self.__selected_map}, {len(self.__maps)}")


main = Main()

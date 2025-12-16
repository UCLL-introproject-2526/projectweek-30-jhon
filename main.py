import Map
from entities.Player import Player
from logic.Loop_controller import Loop_controller
from logic.Logic_runner import LogicManager
from entities.Box import Box

def build_maps(main):
    maps = []
    map1 = Map.Map("map1", 400, 250)
    map1.add_entity(Player(50, 50))
    map1.add_entity(Box(100,100))

    maps.append(map1)
    

    return maps

class Main:
    def __init__(self):
        self.__loop_controller = Loop_controller(self, "Projectweek Jhon")
<<<<<<< HEAD
        self.__maps = build_maps(self)
=======
        map1 = Map.Map("map1", 400, 250)
        map1.add_entity(Player(50, 50, self))
        self.__maps = [map1]
>>>>>>> 50f1c13ff837f10eebf899df3c0dfdc069f775d8
        self.__selected_map = 0

        self.__loop_controller.start()
    def get_current_map(self):
        return self.__maps[self.__selected_map]

    def add_later_task(self, task, delay):
        self.__loop_controller.add_later_task(task, delay)
    

main = Main()



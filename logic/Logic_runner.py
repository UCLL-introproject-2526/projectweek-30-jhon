class LogicManager:
    def __init__(self, main):
        self.__opentasks = []
        self.__main = main


    def execute_loop(self, delta_time):
        for entity in self.__main.get_current_map().get_entities():
            entity.game_loop(delta_time)

        for task in self.__opentasks:
            if task.check_and_run(delta_time):
                self.__opentasks.remove(task)

    def add_later_taks(self, task, time):
        self.__opentasks.append(LaterTask(task, time))

class LaterTask:
    def __init__(self, task, delay):
        self.__time = delay
        self.__task = task

    def check_and_run(self, delta_time):
        self.__time -= delta_time
        if self.__time < 0:
            self.__task()
            return True
        return False

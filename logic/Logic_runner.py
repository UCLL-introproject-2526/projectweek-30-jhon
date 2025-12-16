class LogicManager:
    def __init__(self, main):
        self.__opentasks = []
        self.__main = main


    def execute_loop(self, delta_time):
        for task in self.__opentasks:
            task.check_and_run(delta_time)


class LaterTask:
    def __init__(self, delay, task):
        self.__time = delay
        self.__task = task

    def check_and_run(self, delta_time):
        self.__time -= delta_time
        if self.__time < 0:
            self.__task()
            return True
        return False

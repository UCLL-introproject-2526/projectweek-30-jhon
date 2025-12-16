class LogicManager:
    def __init__(self):
        self.__opentasks = []


    def execute_loop(self, time):
        pass


class LaterTask:
    def __init__(self, delay, task):
        self.__time = delay
        self.__task = task

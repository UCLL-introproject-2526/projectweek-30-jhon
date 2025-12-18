class LogicManager:
    def __init__(self, main):
        self.__open_tasks = []
        self.__main = main


    def execute_loop(self, delta_time, events):
        self.__main.get_current_map().update_map(delta_time, events)

        for task in self.__open_tasks:
            if task.check_and_run(delta_time):
                self.__open_tasks.remove(task)

    def add_later_taks(self, task, time):
        self.__open_tasks.append(LaterTask(task, time))

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

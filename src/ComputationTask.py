"""Holds a task that requires computation."""
import Memento
import itertools
from HelperFunctions import cantor_pair

counter = itertools.count()


class ComputationTask:

    def __init__(self, parent_class_string, function_string):
        """parent_class_string is used to find the function, and must match the class containing the function to be called.
        Function_string is the function that needs to be called.
        """
        self.class_string = parent_class_string
        self.function_string = function_string
        self.execute_after_string = None
        self.data = None
        self.delay = 0
        self.priority = 5
        self.repeat = 0
        self.time_created = Game.time
        count = next(counter)
        try:
            self.uid = cantor_pair(Game.time, count)
        except Exception as e:
            # If game can not be found, we must be running tests, go off of strict count
            self.uid = count

    def execute(self, callback_function):
        return callback_function(self.data)

    def execute_after(self, register_task_function, call_after_function):
        if self.repeat > 0:
            self.delay = self.repeat
            self.time_created = Game.time
            count = next(counter)
            self.uid = cantor_pair(Game.time, count)
            register_task_function(self)
        if call_after_function is not None:
            call_after_function(self)

    def get_memento(self):
        memento_dict = {
            "class_string": self.class_string,
            "function_string": self.function_string,
            "data": self.data,
            "delay": self.delay,
            "priority": self.priority,
            "time_created": self.time_created,
            "repeat": self.repeat,
            "execute_after_string": self.execute_after_string,
            "uid": self.uid,
        }
        return memento_dict


def new_from_memento(memento):
    new_task = ComputationTask(None, None)
    new_task.uid = memento.uid
    new_task.class_string = memento.class_string
    new_task.function_string = memento.function_string
    new_task.data = memento.data
    new_task.delay = memento.delay
    new_task.priority = memento.priority
    new_task.time_created = memento.time_created
    new_task.repeat = memento.repeat
    new_task.execute_after_string = memento.execute_after_string
    return new_task

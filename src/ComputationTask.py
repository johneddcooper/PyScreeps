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
        self.data = None
        self.delay = 0
        self.priority = 5
        self.time_created = Game.time
        count = next(counter)
        try:
            self.uid = cantor_pair(Game.time, count)
        except Exception as e:
            # If game can not be found, we must be running tests, go off of strict count
            self.uid = count

    def execute(self, callback_function):
        return callback_function(self.data)

    def get_memento(self):
        memento_dict = {
            "class_string": self.class_string,
            "function_string": self.function_string,
            "data": self.data,
            "delay": self.delay,
            "priority": self.priority,
            "time_created": self.time_created
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
    return new_task

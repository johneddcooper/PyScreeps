"""Holds a task that requires computation."""
import Memento


class ComputationTask:

    def __init__(self, parent_class_string, function_string):
        """parent_class_string is used to find the function, and must match the class containing the function to be called.
        Function_string is the function that needs to be called.
        """
        self.class_string = parent_class_string
        self.function_string = function_string
        self.data = None
        self.tick_delay_to_run = 0
        self.priority = 5

    def execute(self):
        print("execute", self.class_string, self.function_string)
        print(eval(self.class_string))

        getattr(eval(self.class_string), self.function_string)(self.data)

    def get_memento(self):
        memento_dict = {
            "class_string": self.class_string,
            "function_string": self.function_string,
            "data": self.data,
            "tick_delay_to_run": self.tick_delay_to_run,
            "priority": self.priority,
        }
        return Memento.Memento("ComputationTask", memento_dict)


def new_from_memento(serialized_memento):
    memento = Memento.deserialize(serialized_memento)
    new_task = ComputationTask(None, None)
    new_task.class_string = memento.data_dict["class_string"]
    new_task.function_string = memento.data_dict["function_string"]
    new_task.data = memento.data_dict["data"]
    new_task.tick_delay_to_run = memento.data_dict["tick_delay_to_run"]
    new_task.priority = memento.data_dict["priority"]
    return new_task

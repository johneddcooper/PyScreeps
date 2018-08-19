import Memento


class ComputationTask:

    def __init__(self, parent_class_string, function_string):
        self.class_string = parent_class_string
        self.function_string = function_string
        self.data = None
        self.tick_delay_to_run = 0
        self.priority = 5

    def execute(self):
        getattr(exec(self.class_string), self.function_string)(self.data)

    def get_memento(self):
        memento_dict = {
            "class_string": self.class_string,
            "function_string": self.function_string,
            "data": self.data,
            "tick_delay_to_run": self.tick_delay_to_run,
            "priority": self.priority,
        }
        print("self Dict", memento_dict)
        return Memento.Memento("ComputationTask", memento_dict)


def new_from_memento(serialized_memento):
    memento = Memento.deserialize(serialized_memento)
    print("new from")
    print(memento.class_name)
    print(str(memento.data_dict))
    new_task = ComputationTask(None, None)
    new_task.class_string = memento.data_dict["class_string"]
    new_task.function_string = memento.data_dict["function_string"]
    new_task.data = memento.data_dict["data"]
    new_task.tick_delay_to_run = memento.data_dict["tick_delay_to_run"]
    new_task.priority = memento.data_dict["priority"]
    print("new task")
    print(new_task.class_string)
    print(new_task.function_string)
    print(new_task.data)
    print(new_task.tick_delay_to_run)
    print(new_task.priority)
    print('/new task')
    return new_task

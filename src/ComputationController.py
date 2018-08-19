# Controlles the execution of compuational tasks
import MemoryHelper
import ComputationTask


class ComputaionController:

    def __init__(self):
        self.memory_helper = MemoryHelper.MemoryHelper("ComputationController")
        # self.computation_list = Queue.PriorityQueue()

    def test_function(data):
        print("Incomming Data: {}".format(data))


memory_helper = MemoryHelper.MemoryHelper("mementoTest")
a = ComputationTask.ComputationTask("ComputationController", "test_function")
a.data = {"a1": "Test Data1", "a2": {"Test Data2": [1, 2, 3, 4]}}
print("a.data.a1", a.data.a1)
memento = a.get_memento()
serialized_memento = memento.serialize()
print("ser memento:")
print(str(serialized_memento))
print('4 key')

memory_helper.set_class_memory(serialized_memento)
task_list2 = memory_helper.get_class_memory()
print("gotten2")
print(str(task_list2))
for key, values in _.pairs(task_list2):
    print(key, values)
print("done kv iiter")
task = ComputationTask.new_from_memento(task_list2)
print('task fun string', task.function_string)
print('task.data', task.data)

# Controlles the execution of compuational tasks
import MemoryHelper
import ComputationTask
from ComputationTaskPriorityQueue import ComputationTaskPriorityQueue

"""
1. Get all tasks from memory @ put them into some kind of container
2. Main queries every class for
2. Classes register computation functions (that are called by computation tasks) with a unique string and a function to be called.
"""


# computation_task_list =

memory_helper = MemoryHelper.MemoryHelper("ComputationController")
# self.computation_list = Queue.PriorityQueue()


def register_computation_task(computation_task):
    pass


def test_function(data):
    print("Incomming Data: {}".format(data))


# memory_helper = MemoryHelper.MemoryHelper("mementoTest")
a = ComputationTask.ComputationTask("ComputationController", "test_function")
a.data = {"a1": "Test Data1"}
b = ComputationTask.ComputationTask("ComputationController", "test_function")
b.data = {"b1": "Test Data1"}
b.priority = 7
c = ComputationTask.ComputationTask("ComputationController", "test_function")
c.data = {"c1": "Test Data1"}
c.priority = 3
d = ComputationTask.ComputationTask("ComputationController", "test_function")
d.data = {"d1": "Test Data1"}
e = ComputationTask.ComputationTask("ComputationController", "test_function")
e.data = {"e1": "Test Data1"}
e.priority = 3
# memento = Memento.serialize(a.get_memento())

task_queue = ComputationTaskPriorityQueue()
task_queue.push(a)
task_queue.push(b)
task_queue.push(c)
task_queue.push(d)
task_queue.push(e)

t = task_queue.pop()
print(t.priority, str(t.data))
t = task_queue.pop()
print(t.priority, str(t.data))
t = task_queue.pop()
print(t.priority, str(t.data))
t = task_queue.pop()
print(t.priority, str(t.data))
t = task_queue.pop()
print(t.priority, str(t.data))


# memory_helper.set_class_memory(memento)
# task_list2 = memory_helper.get_class_memory()
# for key, values in _.pairs(task_list2):
#     print(key, values)
# task = ComputationTask.new_from_memento(task_list2)

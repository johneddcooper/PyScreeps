# Controlles the execution of compuational tasks
import MemoryHelper
import ComputationTask
from ComputationTaskPriorityQueue import ComputationTaskPriorityQueue

"""
1. Get all tasks from memory @ put them into some kind of container
2. Main queries every class for
2. Classes register computation functions (that are called by computation tasks) with a unique string and a function to be called.
"""
COMPUTATION_TASK_GARBAGE_COLLECTION_TIME = 100  # mostly for testing or errors, used by garbage collection func to remove tasks older then X ticks

callback_functions = {}
memory_instance = None
task_queue = None


def init():
    print("initted")
    global memory_instance
    global task_queue
    memory_instance = MemoryHelper.MemoryHelper("test_memory")
    if task_queue is None:
        retrive_tasks_from_memory()
    register_callback_function("ComputationController", "computation_task_cleanup", computation_task_cleanup)
    computation_task_cleanup_task = ComputationTask.ComputationTask("ComputationController", "computation_task_cleanup")
    computation_task_cleanup_task.repeat = 15
    computation_task_cleanup_task.delay = 15
    print(len(task_queue))
    if not task_queue.__contains__(computation_task_cleanup_task):
        print("not in")
        register_computation_task(computation_task_cleanup_task)
    else:
        print("In")


def register_callback_function(class_string, function_string, call_function):
    if class_string not in callback_functions:
        callback_functions[class_string] = {}
    callback_functions[class_string][function_string] = call_function


def get_callback_function(class_string, function_string):
    return callback_functions[class_string][function_string] if callback_functions[class_string][function_string] != None else None


def register_computation_task(computation_task):
    global task_queue
    global memory_instance
    print("registering comp task")
    if task_queue is None:
        retrive_tasks_from_memory()
    if computation_task.class_string not in callback_functions or computation_task.function_string not in callback_functions[computation_task.class_string]:
        print("Callback function for added computation_task not registered")
        return
    task_queue.push(computation_task)
    memory_instance.set_item_at_path("task_queue_mem.{}".format(computation_task.uid), computation_task)
    print("pushed on to queue now of len ", len(task_queue))


def retrive_tasks_from_memory():
    global task_queue
    if task_queue is None:
        task_queue = ComputationTaskPriorityQueue()
    for uid, task in _.pairs(memory_instance.get_item_at_path("task_queue_mem")):
        task_queue.push(task)


def execute_tasks():
    global task_queue
    if task_queue is None:
        retrive_tasks_from_memory()
    time = Game.time
    while not task_queue.empty():
        task = ComputationTask.new_from_memento(task_queue.head())
        if task.delay + task.time_created <= time:
            task.execute(get_callback_function(task.class_string, task.function_string))
            task.execute_after(register_computation_task, get_callback_function(task.class_string, task.execute_after_string))
            task_queue.pop()
            memory_instance.remove_item_at_path("task_queue_mem.{}".format(task.uid))
            print("exe queue size", len(task_queue))
        else:
            break


def computation_task_cleanup():
    print("Running garbage collection")
    time = Game.time - COMPUTATION_TASK_GARBAGE_COLLECTION_TIME
    for uid, task in _.pairs(memory_instance.get_item_at_path("task_queue_mem")):
        if task.time_created < time:
            print("Deleting task ", task.uid)
            del(memory_instance.get_item_at_path("task_queue_mem")[uid])


def test_function1(data):
    print("Incomming Data1: {}".format(data))


def test_function2(data):
    print("Incomming Data2: {}".format(data))


# task_list2 = memory_helper.get_class_memory()
# for key, values in _.pairs(task_list2):
#     print(key, values)
# task = ComputationTask.new_from_memento(task_list2)

# register_callback_function("ComputationTask", "test_function1", test_function1)
# register_callback_function("ComputationTask", "test_function2", test_function2)
# task_a = ComputationTask.ComputationTask("ComputationTask", "test_function1")
# task_a.data = [1, 2, 3]
# task_a.delay = 2
# task_b = ComputationTask.ComputationTask("ComputationTask", "test_function1")
# task_c = ComputationTask.ComputationTask("ComputationTask", "test_function2")
# task_b.data = {"b1": [4, 5, 6]}
# task_b.delay = 5
# task_c.priority = 3
# task_c.data = 5
# task_c.delay = 10
# # register_computation_task(task_a)
# register_computation_task(task_b)
# register_computation_task(task_c)

# for k, v in ._pairs(task_queue):


# computation_task_cleanup()

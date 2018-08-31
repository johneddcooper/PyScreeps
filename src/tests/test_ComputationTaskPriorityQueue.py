import os
import sys
import random
import copy
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import ComputationTaskPriorityQueue

NUM_ITEMS_TO_TEST_GENERATE = 50


class ItemClass:
    def __init__(self, priority, time_created, data):
        self.priority = priority
        self.data = data
        self.time_created = time_created
        self.delay = 0
        self.task = self

    def __eq__(self, other):
        return self.priority == other.priority and self.data == other.data and self.time_created == other.time_created and self.delay == other.delay


proof_list = []
task_queue = ComputationTaskPriorityQueue.ComputationTaskPriorityQueue()

for i in range(NUM_ITEMS_TO_TEST_GENERATE):
    test_object = ItemClass(random.randint(0, 10), i, random.randint(0, 100))
    proof_list.append(test_object)
    task_queue.push(test_object)

sorted_proof_list = sorted(proof_list, key=lambda item: (item.time_created + item.delay, item.priority))


def test_priority_queue_start_empty():
    task_queue = ComputationTaskPriorityQueue.ComputationTaskPriorityQueue()
    assert(len(task_queue) == 0)


def test_priority_queue_head():
    assert sorted_proof_list[0] == task_queue.head()


def test_priority_queue_pop():
    queue = copy.deepcopy(task_queue)
    pre_length = len(queue)
    item = queue.pop()
    post_length = len(queue)
    assert pre_length - post_length == 1
    print(item.data)
    print(sorted_proof_list[0].data)
    assert item == sorted_proof_list[0]


def test_priority_queue_order_correct():
    queue = copy.deepcopy(task_queue)
    return_list = []
    while True:
        t = queue.pop()
        if t is None:
            break
        return_list.append(t)

    sorted_proof_list = sorted(proof_list, key=lambda item: (item.time_created + item.delay, item.priority))
    assert sorted_proof_list == return_list


def test_priority_queue_return_none_when_empty():
    task_queue = ComputationTaskPriorityQueue.ComputationTaskPriorityQueue()
    assert(task_queue.pop() is None)
    assert(task_queue.head() is None)


def test_priority_queue_contains_when_empty():
    task_queue = ComputationTaskPriorityQueue.ComputationTaskPriorityQueue()
    assert ("x" in task_queue) is False


def test_priority_queue_contains_when_populated():
    contains = True
    for i in range(len(proof_list)):
        contains = contains and proof_list[i] in task_queue
    assert contains is True


def test_queue_item_compatitors():
    t1 = ComputationTaskPriorityQueue.ComputationTaskPriorityQueue.PriorityQueueItem(1, 1, 0)
    t2 = ComputationTaskPriorityQueue.ComputationTaskPriorityQueue.PriorityQueueItem(1, 2, 0)
    t3 = ComputationTaskPriorityQueue.ComputationTaskPriorityQueue.PriorityQueueItem(2, 1, 2)
    t4 = ComputationTaskPriorityQueue.ComputationTaskPriorityQueue.PriorityQueueItem(2, 2, 3)
    t5 = ComputationTaskPriorityQueue.ComputationTaskPriorityQueue.PriorityQueueItem(2, 2, 4)
    assert t1 < t2 < t3 < t4
    assert not t1 > t2
    assert t1 <= t2
    assert not t1 >= t2
    assert t4 > t3 > t2 > t1
    assert not t4 < t5
    assert not t4 > t5
    assert t4 <= t5
    assert t4 >= t5
    assert t1 == t2
    assert not t1 == t3

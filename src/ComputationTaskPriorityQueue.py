import itertools


class ComputationTaskPriorityQueue:

    class PriorityQueueItem:

        def __init__(self, runtime, priority, task):
            self.runtime = runtime
            self.priority = priority
            self.task = task

        def __lt__(self, other):
            return self.runtime < other.runtime or self.runtime == other.runtime and self.priority < other.priority

        def __gt__(self, other):
            return self.runtime > other.runtime or self.runtime == other.runtime and self.priority > other.priority

        def __le__(self, other):
            return self.runtime <= other.runtime or self.runtime == other.runtime and self.priority <= other.priority

        def __ge__(self, other):
            return self.runtime >= other.runtime or self.runtime == other.runtime and self.priority >= other.priority

        def __eq__(self, other):
            # override eq operator to test for tasks that perform the same function
            # assumes other is a task, for checking if a task is in the priority queue
            if not other.task:
                return self.task.class_string == other.class_string and self.task.function_string == other.function_string
            else:
                return self.task.class_string == other.task.class_string and self.task.function_string == other.task.function_string

    def __init__(self):
        self.priority_queue = []
        self.counter = itertools.count()

    def pop(self):
        # return the actual computation_task from the constructed (priority, count, computation_task) tuple
        return heappop(self.priority_queue).task

    def push(self, computation_task):
        heappush(self.priority_queue, ComputationTaskPriorityQueue.PriorityQueueItem(computation_task.time_created + computation_task.delay, computation_task.priority, computation_task))

    def head(self):
        return self.priority_queue[0].task

    def empty(self):
        return len(self.priority_queue) <= 0

    def __len__(self):
        return len(self.priority_queue)

    def __str__(self):
        for item in self.priority_queue:
            print(item.task)

    def __contains__(self, item):
        # will only compare a passed items class string and function string (expecting that the item is a computation task), making the "in" operator only useful for checking for "one-only" computation tasks
        for queue_item in self.priority_queue:
            if queue_item.__eq__(item):
                return True
        return False


def heappush(heap, val):
    cur = len(heap)
    heap.append(val)
    while cur > 0:
        parent = (cur - 1) // 2
        # JS tries to conduct comparison on all three elements in the (pri, order, computation_task) tuple, leading to string errors.
        # If priority of child is smaller then parent, or if priority is equal but order is smaller, break and leave as it. Ya, its hacky. W/E.

        if heap[parent].__le__(heap[cur]):
            break

        heap[cur], heap[parent] = heap[parent], heap[cur]
        cur = parent


def heappop(heap):
    ret = heap[0]
    last = heap.pop()
    size = len(heap)
    if size == 0:
        return ret
    heap[0] = last
    cur = 0
    while True:
        ch1 = 2 * cur + 1
        if ch1 >= size:
            return ret
        ch2 = ch1 + 1
        child = ch2 if ch2 < size and heap[ch2].__lt__(heap[ch1]) else ch1
        if heap[cur].__le__(heap[child]):
            return ret
        heap[child], heap[cur] = heap[cur], heap[child]
        cur = child

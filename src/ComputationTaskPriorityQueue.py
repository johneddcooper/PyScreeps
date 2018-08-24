import itertools


class ComputationTaskPriorityQueue:

    def __init__(self):
        self.priority_queue = []
        self.counter = itertools.count()

    def pop(self):
        # return the actual computation_task from the constructed (priority, count, computation_task) tuple
        return heappop(self.priority_queue)[2]

    def push(self, computation_task):
        heappush(self.priority_queue, (computation_task.time_created + computation_task.delay, computation_task.priority, computation_task))

    def head(self):
        return self.priority_queue[0][2]

    def empty(self):
        return len(self.priority_queue) <= 0

    def __len__(self):
        return len(self.priority_queue)

    def __str__(self):
        for item in self.priority_queue:
            print(item[2])


def heappush(heap, val):
    cur = len(heap)
    heap.append(val)
    while cur > 0:
        parent = (cur - 1) // 2
        # JS tries to conduct comparison on all three elements in the (pri, order, computation_task) tuple, leading to string errors.
        # If priority of child is smaller then parent, or if priority is equal but order is smaller, break and leave as it. Ya, its hacky. W/E.
        if (heap[parent][0], heap[parent][1]) <= (heap[cur][0], heap[cur][1]):
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
        child = ch2 if ch2 < size and (heap[ch2][0], heap[ch2][1]) < (heap[ch1][0], heap[ch1][1]) else ch1
        if (heap[cur][0], heap[cur][1]) <= (heap[child][0], heap[child][1]):
            return ret
        heap[child], heap[cur] = heap[cur], heap[child]
        cur = child

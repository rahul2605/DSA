from collections import deque


class Queue:
    def __init__(self, capacity):
        self.q = deque(maxlen=capacity)
        self.capacity = capacity

    def __str__(self):
        return str(self.q)

    def is_empty(self):
        return len(self.q) == 0

    def is_full(self):
        return len(self.q) == self.capacity

    def enqueue(self, val):
        self.q.append(val)

    def dequeue(self):
        if self.is_empty():
            return 'The Queue is Empty.'

        return self.q.popleft()


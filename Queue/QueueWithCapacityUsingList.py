class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.Q = ['None'] * capacity
        self.start = -1
        self.end = -1

    def __str__(self):
        if self.start == -1:
            return 'The Queue is Empty.'
        start = self.start
        end = self.end
        vals = []
        while start != end:
            vals.append(str(self.Q[start]))
            start = (start + 1) % self.capacity
        vals.append(str(self.Q[start]))
        return ' <- '.join(vals)

    def is_empty(self):
        if self.start == -1:
            return True
        return False

    def is_full(self):
        return (self.end + 1) % self.capacity == self.start

    def enqueue(self, val):
        if self.is_full():
            return 'The Queue is Full.'

        if self.is_empty():
            self.start = 0
        self.end = (self.end + 1) % self.capacity
        self.Q[self.end] = val
        return True

    def dequeue(self):
        if self.is_empty():
            return 'The Queue is Empty.'

        val = self.Q[self.start]
        self.start = (self.start + 1) % self.capacity

        if self.is_full():
            self.start = -1
            self.end = -1
        return val

    def peek(self):
        if self.is_empty():
            return 'The Queue is Empty.'

        return self.Q[self.start]

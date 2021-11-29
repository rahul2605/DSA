from LinkedList.LinkedList import LinkedList


class Queue:
    def __init__(self):
        self.ll = LinkedList()

    def __str__(self):
        return str(self.ll).replace('->', '<-')

    def __iter__(self):
        return self.ll.__iter__()

    def is_empty(self):
        return self.ll.head is None

    def enqueue(self, val):
        self.ll.append(val)

    def dequeue(self):
        if self.is_empty():
            return 'The Queue is Empty.'

        val = self.ll.head.value
        self.ll.head = self.ll.head.next
        if self.ll.head is None:
            self.ll.tail = None
        return val

    def peek(self):
        if self.is_empty():
            return 'The Queue is Empty.'

        return self.ll.head.value

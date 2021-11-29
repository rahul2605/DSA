from LinkedList.LinkedList import LinkedList

class Stack:
    def __init__(self):
        self.ll = LinkedList()

    def __str__(self):
        return str(self.ll)

    def __iter__(self):
        return self.ll.__iter__()

    def is_empty(self):
        return self.ll.head is None

    def push(self, val):
        self.ll.prepend(val)

    def pop(self):
        if self.is_empty():
            return 'The Stack is empty.'

        val = self.ll.head.value
        self.ll.head = self.ll.head.next
        return val

    def peek(self):
        if self.is_empty():
            return 'The Stack is empty.'
        return self.ll.head.value

from random import randint


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None

    def __iter__(self):
        curr = self.head
        while curr:
            yield curr
            curr = curr.next

    def __str__(self):
        values = [str(node.value) for node in self]
        return ' -> '.join(values)

    def __len__(self):
        length = 0
        curr = self.head
        while curr:
            length += 1
            curr = curr.next
        return length

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def generate(self, num_of_vals=10, min_range=0, max_range=99):
        self.head = None
        self.tail = None
        for i in range(num_of_vals):
            self.append(randint(min_range, max_range))
        return self

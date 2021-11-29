from Queue.QueueUsingLinkedList import Queue


class BinaryTree:
    def __init__(self, size):
        self.max_size = size + 1
        self.tree = [None] * self.max_size
        self.last_index = 0

    def add_node(self, data):
        if self.last_index + 1 == self.max_size:
            return 'The tree is full'
        self.last_index += 1
        self.tree[self.last_index] = data

    def preorder_traversal(self, index=1, level=0):
        if level == 0:
            print('Pre Order Traversal:')
        if index > self.last_index:
            return

        print(' ' * level + self.tree[index])
        self.preorder_traversal(2*index, level=level + 1)
        self.preorder_traversal(2*index+1, level=level + 1)

    def inorder_traversal(self, index=1, level=0):
        if level == 0:
            print('In Order Traversal:')
        if index > self.last_index:
            return

        self.inorder_traversal(2*index, level=level + 1)
        print(' ' * level + self.tree[index])
        self.inorder_traversal(2*index+1, level=level + 1)

    def postorder_traversal(self, index=1, level=0):
        if level == 0:
            print('Post Order Traversal:')
        if index > self.last_index:
            return

        self.postorder_traversal(2 * index, level=level + 1)
        self.postorder_traversal(2*index+1, level=level + 1)
        print(' ' * level + self.tree[index])

    def level_order_traversal(self):
        print('Level Order Traversal:')
        for i in range(1, self.last_index+1):
            print(self.tree[i])

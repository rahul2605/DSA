from random import randint
from Queue.QueueUsingLinkedList import Queue


class BSTNode:
    def __init__(self, data=None):
        self.data = data
        self.left_child = None
        self.right_child = None


def insert_node(bst_node: BSTNode, value):
    if bst_node.data is None:
        bst_node.data = value
        return

    if value <= bst_node.data:
        if bst_node.left_child is None:
            bst_node.left_child = BSTNode(value)
            return
        else:
            insert_node(bst_node.left_child, value)
    elif value > bst_node.data:
        if bst_node.right_child is None:
            bst_node.right_child = BSTNode(value)
            return
        else:
            insert_node(bst_node.right_child, value)


def level_order_traversal(root_node: BSTNode):
    if not root_node:
        return

    buffer_q = Queue()
    buffer_q.enqueue(root_node)

    while not buffer_q.is_empty():
        node = buffer_q.dequeue()
        print(node.data)
        if node.left_child is not None:
            buffer_q.enqueue(node.left_child)
        if node.right_child is not None:
            buffer_q.enqueue(node.right_child)


def search_node(root_node: BSTNode, node_value):
    if root_node is None:
        print('Not found!')

    if root_node.data == node_value:
        print('Found!')
    elif node_value < root_node.data:
        search_node(root_node.left_child, node_value)
    elif node_value > root_node.data:
        search_node(root_node.right_child, node_value)


def min_value_node(node: BSTNode):
    while node.left_child is not None:
        node = node.left_child
    return node


def delete_node(root_node: BSTNode, node_value):
    if root_node is None:
        return
    elif root_node.data > node_value:
        root_node.left_child = delete_node(root_node.left_child, node_value)
    elif root_node.data < node_value:
        root_node.right_child = delete_node(root_node.right_child, node_value)
    elif root_node.data == node_value:
        if root_node.left_child is None and root_node.right_child is None:
            root_node = None
        elif root_node.left_child is None:
            root_node = root_node.right_child
        elif root_node.right_child is None:
            root_node = root_node.left_child
        elif root_node.right_child is not None and root_node.left_child is not None:
            min_val_node = min_value_node(root_node.right_child)
            root_node.data = min_val_node.data
            root_node.right_child = delete_node(root_node.right_child, min_val_node.data)
    return root_node

newBST = BSTNode()
vals = [70, 50, 90, 30, 60, 80, 100, 20, 40, 10, 75, 85, 45]
for val in vals:
    insert_node(newBST, val)

level_order_traversal(newBST)
delete_node(newBST, 40)
print('---------------------------')
level_order_traversal(newBST)

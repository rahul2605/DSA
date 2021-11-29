from BinaryTreeUsingLL import TreeNode
from Queue.QueueUsingLinkedList import Queue
from BinaryTreeUsingList import BinaryTree


def preorder_traversal(root_node: TreeNode, level=0):
    if not root_node:
        return

    print(' '*level + root_node.data)
    preorder_traversal(root_node.left_child, level=level+1)
    preorder_traversal(root_node.right_child, level=level+1)


def inorder_traversal(root_node: TreeNode, level=0):
    if not root_node:
        return
    inorder_traversal(root_node.left_child, level=level+1)
    print(' '*level + root_node.data)
    inorder_traversal(root_node.right_child, level=level + 1)


def postorder_traversal(root_node: TreeNode, level=0):
    if not root_node:
        return
    postorder_traversal(root_node.left_child, level=level+1)
    postorder_traversal(root_node.right_child, level=level+1)
    print(' '*level + root_node.data)


def level_order_traversal(root_node: TreeNode):
    print('Level Order Traversal')
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


def get_deepest_node(root_node: TreeNode):
    if not root_node:
        return

    buffer_q = Queue()
    buffer_q.enqueue(root_node)

    while not buffer_q.is_empty():
        node = buffer_q.dequeue()
        if node.left_child is not None:
            buffer_q.enqueue(node.left_child)
        if node.right_child is not None:
            buffer_q.enqueue(node.right_child)
    print(f'Deepest node is {node.data}')
    return node.data


def delete_deepest_node(root_node: TreeNode, deepest_node_value):
    if not root_node:
        return

    buffer_q = Queue()
    buffer_q.enqueue(root_node)

    node = None
    while not buffer_q.is_empty():
        node = buffer_q.dequeue()
        if node.data == deepest_node_value:
            node.data = None
            return
        if node.left_child is not None:
            if node.left_child.data == deepest_node_value:
                node.left_child = None
                return
            buffer_q.enqueue(node.left_child)
        if node.right_child is not None:
            if node.right_child.data == deepest_node_value:
                node.right_child = None
                return
            buffer_q.enqueue(node.right_child)


def delete_node(root_node: TreeNode, val_to_delete):
    if not root_node:
        return

    buffer_q = Queue()
    buffer_q.enqueue(root_node)

    while not buffer_q.is_empty():
        node = buffer_q.dequeue()
        if node.data == val_to_delete:
            deepest_node = get_deepest_node(root_node)
            delete_deepest_node(root_node, deepest_node)
            node.data = deepest_node
            return

        if node.left_child is not None:
            buffer_q.enqueue(node.left_child)
        if node.right_child is not None:
            buffer_q.enqueue(node.right_child)



drinks_node = TreeNode("Drinks")
hot_node = TreeNode("Hot")
cold_node = TreeNode("Cold")
tea_node = TreeNode("Tea")
coffee_node = TreeNode("Coffee")

drinks_node.left_child = hot_node
drinks_node.right_child = cold_node

hot_node.left_child = tea_node
hot_node.right_child = coffee_node

level_order_traversal(drinks_node)
delete_node(drinks_node, "Hot")
level_order_traversal(drinks_node)


# nodes = ['Drinks', 'Hot', 'Cold', 'Tea', 'Coffee']
# bt = BinaryTree(10)
# for node in nodes:
#     bt.add_node(node)
# delete_deepest_node(bt)
# bt.level_order_traversal()
# print('-------------------------------')
# bt.preorder_traversal()
# print('-------------------------------')
# bt.postorder_traversal()
# print('-------------------------------')
# bt.inorder_traversal()

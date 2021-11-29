from Queue.QueueUsingLinkedList import Queue


class AVLNode:
    def __init__(self, data=None):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.height = 1


def preorder_traversal(root_node: AVLNode, level=0):
    if not root_node:
        return

    print(' '*level + root_node.data)
    preorder_traversal(root_node.left_child, level=level+1)
    preorder_traversal(root_node.right_child, level=level+1)


def inorder_traversal(root_node: AVLNode, level=0):
    if not root_node:
        return
    inorder_traversal(root_node.left_child, level=level+1)
    print(' '*level + root_node.data)
    inorder_traversal(root_node.right_child, level=level + 1)


def postorder_traversal(root_node: AVLNode, level=0):
    if not root_node:
        return
    postorder_traversal(root_node.left_child, level=level + 1)
    postorder_traversal(root_node.right_child, level=level+1)
    print(' '*level + root_node.data)


def level_order_traversal(root_node: AVLNode):
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


def search_node(root_node: AVLNode, node_value):
    if root_node is None:
        print('Not found!')
    print(root_node.data, node_value)
    if root_node.data == node_value:
        print('Found!')
    elif node_value < root_node.data:
        search_node(root_node.left_child, node_value)
    elif node_value > root_node.data:
        search_node(root_node.right_child, node_value)


def get_height(node: AVLNode):
    if not node:
        return 0
    return node.height


def rotate_right(unbalanced_node: AVLNode):
    new_root = unbalanced_node.left_child
    unbalanced_node.left_child = unbalanced_node.left_child.right_child
    new_root.right_child = unbalanced_node
    unbalanced_node.height = 1 + max(get_height(unbalanced_node.left_child), get_height(unbalanced_node.right_child))
    new_root.height = 1 + max(get_height(new_root.left_child), get_height(new_root.right_child))
    return new_root


def rotate_left(unbalanced_node: AVLNode):
    new_root = unbalanced_node.right_child
    unbalanced_node.right_child = unbalanced_node.right_child.left_child
    new_root.left_child = unbalanced_node
    unbalanced_node.height = 1 + max(get_height(unbalanced_node.left_child), get_height(unbalanced_node.right_child))
    new_root.height = 1 + max(get_height(new_root.left_child), get_height(new_root.right_child))
    return new_root


def get_balance(node: AVLNode):
    """
    Returns the height difference between the left and right subtrees of the node.
    returns < 0: Left subtree is higher
    returns > 0: Right subtree is higher
    """
    if not node:
        return 0
    return get_height(node.left_child) - get_height(node.right_child)


def insert_node(root_node: AVLNode, node_value):
    # This is just at the leaf, where the node is actually added
    if not root_node:
        return AVLNode(node_value)

    # This is the code that propagates towards the leaf where the node will be added
    if node_value <= root_node.data:
        root_node.left_child = insert_node(root_node.left_child, node_value)
    elif node_value > root_node.data:
        root_node.right_child = insert_node(root_node.right_child, node_value)

    # The rest of this happens at every level going back up from the leaf
    root_node.height = 1 + max(get_height(root_node.left_child), get_height(root_node.right_child))
    balance = get_balance(root_node)
    if balance > 1:                                     # Left
        if node_value <= root_node.left_child.data:     # Left
            root_node = rotate_right(root_node)
        elif node_value > root_node.left_child.data:    # Right
            root_node.left_child = rotate_left(root_node.left_child)
            root_node = rotate_right(root_node)
    elif balance < -1:                                  # Right
        if node_value <= root_node.right_child.data:     # Left
            root_node.right_child = rotate_right(root_node.right_child)
            root_node = rotate_left(root_node)
        elif node_value > root_node.right_child.data:    # Right
            root_node = rotate_left(root_node)

    return root_node


def min_value_node(node: AVLNode):
    while node.left_child is not None:
        node = node.left_child
    return node


def delete_node(root_node: AVLNode, node_value):
    if not root_node:
        return root_node

    if node_value < root_node.data:
        root_node.left_child = delete_node(root_node.left_child, node_value)
    elif node_value > root_node.data:
        root_node.right_child = delete_node(root_node.right_child, node_value)
    elif node_value == root_node.data:
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

    if root_node:
        root_node.height = 1 + max(get_height(root_node.left_child), get_height(root_node.right_child))
    balance = get_balance(root_node)
    if balance > 1:  # Left
        if node_value <= root_node.left_child.data:  # Left
            root_node = rotate_right(root_node)
        elif node_value > root_node.left_child.data:  # Right
            root_node.left_child = rotate_left(root_node.left_child)
            root_node = rotate_right(root_node)
    elif balance < -1:  # Right
        if node_value <= root_node.right_child.data:  # Left
            root_node.right_child = rotate_right(root_node.right_child)
            root_node = rotate_left(root_node)
        elif node_value > root_node.right_child.data:  # Right
            root_node = rotate_left(root_node)
    return root_node


avl_tree = AVLNode(10)
for i in range(20, 100, 10):
    avl_tree = insert_node(avl_tree, i)
print('Level Order Traversal:')
level_order_traversal(avl_tree)
print('-----------------------')

delete_node(avl_tree, 80)
print('Level Order Traversal:')
level_order_traversal(avl_tree)
print('-----------------------')
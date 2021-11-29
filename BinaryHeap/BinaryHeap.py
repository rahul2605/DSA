class Heap:
    def __init__(self, size: int, heap_type: str):
        self.max_size = size + 1
        self.custom_list = [None] * self.max_size
        self.heap_size = 0
        self.heap_type = heap_type.lower()

    def __del__(self):
        self.custom_list = None

    def peek(self):
        if self.heap_size == 0:
            return None
        return self.custom_list[1]

    def size(self):
        return self.heap_size

    def level_order_traversal(self):
        print('Level Order Traversal.')
        for i in range(1, self.heap_size+1):
            print(self.custom_list[i])

    def heapify_for_insert(self, index):
        if index <= 1:
            return

        parent = int(index/2)
        if self.heap_type == 'min':
            if self.custom_list[index] < self.custom_list[parent]:
                temp = self.custom_list[index]
                self.custom_list[index] = self.custom_list[parent]
                self.custom_list[parent] = temp
        elif self.heap_type == 'max':
            if self.custom_list[index] > self.custom_list[parent]:
                temp = self.custom_list[index]
                self.custom_list[index] = self.custom_list[parent]
                self.custom_list[parent] = temp
        self.heapify_for_insert(parent)

    def insert_node(self, val):
        if self.heap_size + 1 == self.max_size:
            return 'The Heap is full.'
        self.heap_size += 1
        self.custom_list[self.heap_size] = val
        self.heapify_for_insert(self.heap_size)

    def heapify_for_delete(self, index):
        left_child_index = 2 * index
        right_child_index = 2 * index + 1

        if index >= self.heap_size or left_child_index > self.heap_size or right_child_index > self.heap_size:
            return

        if self.heap_type == 'min':
            if self.custom_list[left_child_index] < self.custom_list[right_child_index]:
                swap_child_index = left_child_index
            else:
                swap_child_index = right_child_index
            if self.custom_list[index] > self.custom_list[swap_child_index]:
                temp = self.custom_list[index]
                self.custom_list[index] = self.custom_list[swap_child_index]
                self.custom_list[swap_child_index] = temp
        elif self.heap_type == 'max':
            if self.custom_list[left_child_index] > self.custom_list[right_child_index]:
                swap_child_index = left_child_index
            else:
                swap_child_index = right_child_index
            if self.custom_list[index] < self.custom_list[swap_child_index]:
                temp = self.custom_list[index]
                self.custom_list[index] = self.custom_list[swap_child_index]
                self.custom_list[swap_child_index] = temp
        self.heapify_for_delete(swap_child_index)

    def delete_node(self):
        if self.heap_size == 0:
            return 'The Heap is empty.'
        data = self.custom_list[1]
        self.custom_list[1] = self.custom_list[self.heap_size]
        self.custom_list[self.heap_size] = None
        self.heap_size -= 1
        self.heapify_for_delete(1)
        return data

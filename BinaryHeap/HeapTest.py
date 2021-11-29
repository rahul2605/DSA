from BinaryHeap import Heap
from random import randint

heap_size = 10
heap = Heap(heap_size, 'max')

for i in range(7):
    rand_val = randint(0, 100)
    print(f'Inserting {rand_val} in the Heap.')
    heap.insert_node(rand_val)

heap.level_order_traversal()

print('Deleting a value.')
deleted_val = heap.delete_node()
print(f'{deleted_val} deleted.')
heap.level_order_traversal()


from LinkedList import LinkedList
from random import randint

def remove_dups(ll):
    print('Removing Duplicates..')
    ll_vals = set([ll.head.value])
    for node in ll:
        if node.next is not None:
            if node.next.value not in ll_vals:
                ll_vals.append(node.next.value)
            else:
                node.next = node.next.next
    return ll

def remove_dups_without_set(ll):
    print('Removing Duplicates..')
    curr_node = ll.head
    while curr_node:
        runner = curr_node
        while runner:
            if runner.next is not None:
                if runner.next.value == curr_node.value:
                    runner.next = runner.next.next
            runner = runner.next
        curr_node = curr_node.next
    return ll


def k_to_last_using_buffer(k, ll):
    k_to_last_buffer = []
    for node in ll:
        k_to_last_buffer.append(node.value)
        k_to_last_buffer = k_to_last_buffer[-k-1:]
    if len(k_to_last_buffer) < k+1 or len(k_to_last_buffer) == 0:
        return None
    return k_to_last_buffer[0]

def k_to_last(k, ll):
    ptr1 = ll.head
    ptr2 = ll.head

    for i in range(k+1):
        if ptr2 is None:
            return None
        ptr2 = ptr2.next

    while ptr2:
        ptr2 = ptr2.next
        if ptr2 is None:
            if ptr1.next != None:
                ptr1 = ptr1.next
        else:
            ptr1 = ptr1.next
    return ptr1.value


def partition(val, ll):
    print(f'Partitioning linked-list at {val}.')
    new_ll = LinkedList()
    for node in ll:
        if node.value is not None:
            if node.value < val:
                new_ll.prepend(node.value)
            else:
                new_ll.append(node.value)
    return new_ll


ll = LinkedList()
ll.generate(num_of_vals=30)
print(ll)
partition_val = randint(0, 99)
partitioned_ll = partition(partition_val, ll)
print(partitioned_ll)

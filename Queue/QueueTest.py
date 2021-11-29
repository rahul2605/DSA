from QueueUsingCollections import Queue

qq = Queue(10)
print(f'Queue is Empty: {qq.is_empty()}')

for i in range(15):
    qq.enqueue(i)
    print(qq)

print(f'Queue is Full: {qq.is_full()}')
print(f'Queue is Empty: {qq.is_empty()}')

for i in range(6):
    print(qq.dequeue())
print(qq)

for i in range(2):
    qq.enqueue(i)
print(qq)

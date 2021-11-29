from Stack import Stack

st = Stack()

for i in range(2):
    st.push(i)
print(st)
print(f'Stack is empty: {st.is_empty()}')

for i in range(3):
    print(st.pop())
print(st)
print(f'Stack is empty: {st.is_empty()}')
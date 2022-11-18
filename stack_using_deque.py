from collections import deque

stack = deque()

stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)
stack.append(6)
print(type(stack))
# print(list(stack))
print(stack)

print('Pop:', stack.pop())
# print('Pop:', stack.pop())
# print('Pop:', stack.pop())
print(stack)

stack.appendleft(0)
stack.remove(1)
stack.insert(5, 10) # position / index, value
stack.insert(5, 10) 
stack.insert(5, 10)

print(stack)
print(stack.count(10))
stack.extend()
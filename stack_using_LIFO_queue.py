from queue import LifoQueue

stack = LifoQueue(maxsize=10)

stack.put(10)
# print(stack.get_nowait()) # raise error if stack is empty
print(stack.get()) # wait untill an item is available
stack.put(1) # if stack is full, it will wait untill a space available
stack.put_nowait(33) # raise error if stack is full
stack.put(2)
stack.put(3)
stack.put(4)

print(stack)

print('size:', stack.qsize())
print('pop:', stack.get())
print('size:', stack.qsize())
print(stack.all_tasks_done)
print(stack.empty())
print(stack.full())
print(stack.task_done())
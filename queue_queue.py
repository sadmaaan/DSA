from queue import Queue

queue = Queue(maxsize=0) # infinite queue

queue.put(1)
queue.put(2)
queue.put(3)
queue.put(4)
queue.put(5)

print(queue)

print(queue.empty())
print(queue.qsize())

print(queue.get())
print(queue.get())
print(queue.get())
print(queue.get())
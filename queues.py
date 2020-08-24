
"""
First In First out
Lists is not a recommended queue
"""
from collections import deque

q = deque()

q.appendleft(1)
q.appendleft(2)
q.appendleft(3)
q.appendleft(4)

print(q.pop())




class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.bugger) == 0

    def size(self):
        return len(self.buffer)


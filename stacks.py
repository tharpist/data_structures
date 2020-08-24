"""
Queue: First in First Out
Stack: Last in First out
"""
class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    
    def get_stack(self):
        return self.items



s = Stack()
s.push("A")
s.push("B")
s.push("C")
s.push("D")
#s.pop()
s.peek()

print(s.get_stack())
#print(s.items)
print(s.peek())

#s.get_stack()
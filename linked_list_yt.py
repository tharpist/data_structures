"""
Taken from
"""
class Node():
    def __init__(self, data):
        self.data = data

def countNodes(head):
    count = 1
    current = head
    while current.next != null:
        current = current.next
        count += 1





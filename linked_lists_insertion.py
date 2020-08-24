"""
Singly linked list
Has a node of daata
2 components data component and next
NExt is a pointer that points to the next node in the list
Linked lists are terminated by Null saying it's the end of the list

Arrays  are contiguous
Linked Lists are not

Sometimes I will have to  choose between linked list and arrays based on memory


"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next 

    def append(self, data):
        new_node = Node(data)
    
        if self.head is None:
            self.head = new_node
            return 
    
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node 
    
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert(self, prev_node, data):
        if not prev_node:
            print("Previous node is not there")
            return
        new_node = Node(data)    
        new_node.next = prev_node.next
        prev_node.next = new_node


llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
#llist.insert(llist.head.next, "E")
llist.append("D")
llist.insert(llist.head.next, "E")
llist.print_list()



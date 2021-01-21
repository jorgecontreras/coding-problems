# linked list node remove

# Given a linked list and an integer k, remove the k-th node from the end of the list and return the head of the list.

# k is guaranteed to be smaller than the length of the list.

# Do this in one pass.

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def show(self):
        node = self.head
        while node:
            print(node.val)
            node = node.next

    def insert_node(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node

    def append_node(self, val):
        node = Node(val)
        #if list is empty append node at head
        if self.head is None:
            self.head = node
            return
        
        #if list it not empty, traverse all the way to the last
        last = self.head 
        while last.next:
            last = last.next

        last.next = node

    def remove_node(self, k):
        node = self.head
        prev = None
        while k > 0:
            prev = node
            node = node.next
            k -= 1

        if prev:
            prev.next = node.next
        else:
            self.head = node.next

        node = None 
        
# test
# create linked list

myList = LinkedList()
myList.append_node(1)
myList.append_node(2)
myList.append_node(3)
myList.append_node(4)
myList.append_node(5)
myList.show()
print()
myList.remove_node(0)
myList.show()
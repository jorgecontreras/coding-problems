# reverse linked list
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def reverse_linked_list(node):
    prev = None 
    while node:
        node.next, node, prev = prev, node.next, node
    return prev

def show_linked_list(head):
    node = head
    while node:
        print(node.val)
        node = node.next


n = Node(2)
n.next = Node(3)
n.next.next = Node (4)

r = reverse_linked_list(n)
show_linked_list(r)

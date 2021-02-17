# REVERSE LINKED LIST - RECURSIVE
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def reverse(head):
    #base case
    if not head or not head.next:
        return head

    reversed_list = reverse(head.next)

    head.next.next, head.next = head, None

    return reversed_list

node = Node(1)
node.next = Node(2)
node.next.next = Node(3)
node.next.next.next = Node(4)
node.next.next.next.next = Node(5)

reversed_list = reverse(node)

assert reversed_list.val == 5
assert reversed_list.next.val == 4
assert reversed_list.next.next.val == 3
assert reversed_list.next.next.next.val == 2
assert reversed_list.next.next.next.next.val == 1

print("all tests passed.")
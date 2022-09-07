# BREADTH FIRST VALUES
"""
Write a function, breadth_first_values, that takes in the root of a binary tree. 
The function should return a list containing all values of the tree in breadth-first order.
"""

from collections import deque

class Node:
   def __init__(self, val):
     self.val = val
     self.left = None
     self.right = None

def bfs(root):
    queue = deque([root])

    values = []
    while queue:
        node = queue.popleft()
        values.append(node.val)
    
        if node.left:
          queue.append(node.left)

        if node.right:
          queue.append(node.right)

    return values

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
#    /       \
#   g         h

t1 = bfs(a)

assert t1 == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

print("All tests passed!")
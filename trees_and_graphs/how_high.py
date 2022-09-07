# HOW HIGH
"""
Write a function, how_high, that takes in the root of a binary tree. 
The function should return a number representing the height of the tree.

The height of a binary tree is defined as the maximal number of edges from the root node to any leaf node.

If the tree is empty, return -1.
"""
from collections import deque

class Node:
   def __init__(self, val):
     self.val = val
     self.left = None
     self.right = None

def how_high_dfs(root):
    if not root:
        return -1

    return 1 + max(how_high_dfs(root.left), how_high_dfs(root.right))

def how_high(root):
    if not root: 
        return -1

    queue = deque([root])

    h = -1
    while queue:
        size = len(queue)
        for _ in range(size):
            node = queue.popleft()

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        h += 1

    return h

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

assert how_high(a) == 2
assert how_high_dfs(a) == 2

a = Node('a')

assert how_high(a) == 0
assert how_high(None) == -1

assert how_high_dfs(a) == 0
assert how_high_dfs(None) == -1

print("All tests passed!")
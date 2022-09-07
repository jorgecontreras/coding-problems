# DEPTH FIRST VALUES
"""
Write a function, depth_first_values, that takes in the root of a binary tree. 
The function should return a list containing all values of the tree in depth-first order.
"""

class Node:
   def __init__(self, val):
     self.val = val
     self.left = None
     self.right = None


def dfs_values(root):
    values = []
    return dfs(root, values)

def dfs(root, values):
    if not root:
        return

    values.append(root.val)

    dfs(root.left, values)
    dfs(root.right, values)

    return values

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

assert dfs_values(a) == ['a', 'b', 'd', 'e', 'c', 'f']

print("All tests passed!")
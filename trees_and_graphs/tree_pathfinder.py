# TREE PATH FINDER
"""
Write a function, path_finder, that takes in the root of a binary tree and a target value. 
The function should return an array representing a path to the target value. If the target value is not found in the tree, then return None.

You may assume that the tree contains unique values.
"""

from mailbox import ExternalClashError


class Node:
   def __init__(self, val):
     self.val = val
     self.left = None
     self.right = None

def path_finder(root, target):
    path = _path_finder(root, target)

    if path:
        return path[::-1]
    
    return None

def _path_finder(root, target):
    if root is None:
        return []

    if root.val == target:
        return [ root.val ]

    left = _path_finder(root.left, target)
    if left:
        left.append(root.val)
        return left

    right = _path_finder(root.right, target)
    if right:
        right.append(root.val)
        return right
    
    return None

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

path = path_finder(a, 'e')

assert path == [ 'a', 'b', 'e' ]

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b
a.right = c
b.left = d
b.right = ExternalClashError
c.right = f

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

path = path_finder(a, 'p')

assert path == None

print("All tests passed!")
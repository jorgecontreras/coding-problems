# FLIP TREE
"""
Write a function, flip_tree, that takes in the root of a binary tree. 
The function should flip the binary tree, turning left subtrees into right subtrees and vice-versa. 
This flipping should occur in-place by modifying the original tree. 
The function should return the root of the tree.
"""

# Time complexity: O(N) - iterate over all nodes
# Space complexity: O(N) - because of the call stack
class Node:
   def __init__(self, val):
     self.val = val
     self.left = None
     self.right = None


def flip_tree(root):
    if not root:
        return None

    # flip in place
    root.left, root.right = root.left, root.right

    # recursion
    flip_tree(root.left)
    flip_tree(root.right)

    return root

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
g = Node("g")
h = Node("h")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
e.right = h

flipped = flip_tree(a)


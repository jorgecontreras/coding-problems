# TREE VALUE COUNT
"""
Write a function, tree_value_count, that takes in the root of a binary tree and a target value. 
The function should return the number of times that the target occurs in the tree.
"""

# Time: O(N) - check every node
# Space: O(N) - call stack
class Node:
   def __init__(self, val):
     self.val = val
     self.left = None
     self.right = None

def tree_value_count(root, target):
    if root is None:
        return 0

    left_count = tree_value_count(root.left, target)
    right_count = tree_value_count(root.right, target)

    match = 1 if root.val == target else 0

    return match + left_count + right_count

a = Node(12)
b = Node(6)
c = Node(6)
d = Node(4)
e = Node(6)
f = Node(12)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      12
#    /   \
#   6     6
#  / \     \
# 4   6     12

t1 = tree_value_count(a,  6)

assert t1 == 3

print("All tests passed!")
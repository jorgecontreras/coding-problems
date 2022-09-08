# BINARY TREE INCLUDES
"""
Write a function, binary_search_tree_includes, that takes in the root of a binary search tree containing numbers and a target value. 
The function should return a boolean indicating whether or not the target is found within the tree.

A Binary Search Tree is a binary tree where all values within a node's left subtree are smaller than the node's value 
and all values in a node's right subtree are greater than or equal to the node's value.

Your solution should have a best case runtime of O(log(n)).
"""
class Node:
   def __init__(self, val):
     self.val = val
     self.left = None
     self.right = None

def binary_search_tree_includes(root, target):
    # base case
    if not root:
        return False

    # target was found
    if root.val == target:
        return True

    # keep searching. compare value to decide if we should go left or right
    if target < root.val:
        return binary_search_tree_includes(root.left, target)
    else:
        return binary_search_tree_includes(root.right, target)


a = Node(12)
b = Node(5)
c = Node(18)
d = Node(3)
e = Node(9)
f = Node(19)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      12
#    /   \
#   5     18
#  / \     \
# 3   9     19

assert binary_search_tree_includes(a, 9) == True
assert binary_search_tree_includes(a, 15) == False

print("All tests passed!")
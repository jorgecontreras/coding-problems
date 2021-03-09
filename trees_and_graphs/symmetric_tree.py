# SYMMETRIC TREE

# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
#
# Time complexity: O(n), because we traverse the tree once
# Space complexity: O(n), for the call stack, being the worst case a linear tree.

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def is_symmetric(root):
    if not root:
        return True
    
    return is_mirror(root.left, root.right)

def is_mirror(left, right):
    if left and right:
        return left.val == right.val and is_mirror(left.left, right.right) and is_mirror(left.right, right.left)
    
    return left is right

# tests
n = Node(3)
n.left = Node(4)
n.right = Node(4)
n.left.left = Node(7)
n.left.right = Node(1)
n.right.left = Node(1)
n.right.right = Node(7)

assert is_symmetric(n) == True

n = Node(3)
n.left = Node(4)
n.right = Node(4)
n.left.left = Node(7)
n.left.right = Node(8)
n.right.left = Node(1)
n.right.right = Node(7)

assert is_symmetric(n) == False

n = Node(3)

assert is_symmetric(n) == True

print("all tests passed.")
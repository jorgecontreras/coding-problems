class Node:
   def __init__(self, val):
     self.val = val
     self.left = None
     self.right = None


# TREE INCLUDES
"""
Write a function, tree_includes, that takes in the root of a binary tree and a target value. The function should return a boolean indicating whether or not the value is contained in the tree.
"""

def tree_includes(root, target):
    return dfs(root, target)

def dfs(root, target):
    if root is None:
        return False

    if root.val == target:
        return True

    left = dfs(root.left, target)
    right = dfs(root.right, target)

    return left or right

#sample tree
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

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

# tests:
assert tree_includes(a, "e") == True
assert tree_includes(a, "n") == False
assert tree_includes(a, "f") == True
assert tree_includes(a, "p") == False
assert tree_includes(None, "b") == False

print("All tests passed!")

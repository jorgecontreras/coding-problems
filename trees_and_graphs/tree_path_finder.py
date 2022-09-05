# TREE PATH FINDER
"""
Write a function, path_finder, that takes in the root of a binary tree and a target value. 
The function should return an array representing a path to the target value. 
If the target value is not found in the tree, then return None.

You may assume that the tree contains unique values.
"""

# Time complexity: O(N)
# Space complexity: O(N)

class Node:
   def __init__(self, val):
     self.val = val
     self.left = None
     self.right = None

def path_finder(root, target):
    path = dfs(root, target)

    # If path was found, reverse it and then return
    if path:
        return path[::-1]

    # if path was not found return None
    return None

def dfs(root, target):
    if root is None:
        return None

    if root.val == target:
        return [ root.val ]

    left = dfs(root.left, target)
    if left:
        left.append(root.val)
        return left

    right = dfs(root.right, target)
    if right:
        right.append(root.val)
        return right

    return None


# TEST 01
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
assert path_finder(a, "c") == ['a', 'c']

# TEST 02:
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
f.right = h

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
#    /       \
#   g         h

assert path_finder(a, "h") == ['a', 'c', 'f', 'h']

print("All tests passed!")
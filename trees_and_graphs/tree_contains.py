# TREE CONTAINS
"""
Write a function, tree_contains, that takes in the root of a binary tree and a target value. 
The function should return a boolean indicating whether or not the value is contained in the tree.
"""
from collections import deque

class Node:
   def __init__(self, val):
     self.val = val
     self.left = None
     self.right = None

def tree_contains_dfs(root, target):
    if root is None:
        return False

    return root.val == target or tree_contains_dfs(root.left, target) or tree_contains_dfs(root.right, target)

def tree_contains_bfs(root, target):
    queue = deque([root])

    while queue:
        node = queue.popleft()

        if node.val == target:
            return True

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return False

# tests
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

assert tree_contains_dfs(a, "a") == True
assert tree_contains_bfs(a, "a") == True

print("All tests passed!")
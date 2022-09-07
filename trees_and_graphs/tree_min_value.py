# TREE MIN VALUE
"""
Write a function, tree_min_value, that takes in the root of a binary tree that contains number values. 
The function should return the minimum value within the tree.

You may assume that the input tree is non-empty.
"""
class Node:
   def __init__(self, val):
     self.val = val
     self.left = None
     self.right = None

# Time complexity: O(N)
# Space complexity: O(N)

from collections import deque

def tree_min_value_bfs(root):
    smallest = float("inf")

    queue = deque([root])

    while queue:
        node = queue.popleft()
        smallest = min(smallest, node.val)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return smallest

def tree_min_value_dfs(root):
    if root is None:
        return float("inf")

    left = tree_min_value_dfs(root.left)
    right =tree_min_value_dfs(root.right)
    
    return min(root.val, left, right)

a = Node(5)
b = Node(11)
c = Node(3)
d = Node(4)
e = Node(14)
f = Node(12)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#       5
#    /    \
#   11     3
#  / \      \
# 4   14     12

assert tree_min_value_bfs(a) == 3
assert tree_min_value_dfs(a) == 3

print("All tests passed!")
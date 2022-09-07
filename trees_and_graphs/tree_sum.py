# TREE SUM
"""
Write a function, tree_sum, that takes in the root of a binary tree that contains number values. 
The function should return the total sum of all values in the tree.
"""

# Time complexity: O(N)
# Space complexity: O(N)

class Node:
   def __init__(self, val):
     self.val = val
     self.left = None
     self.right = None

from collections import deque

def tree_sum_bfs(root):

    queue = deque([root])
    sum = 0

    while queue:
        node = queue.popleft()
        sum += node.val

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return sum


def tree_sum_dfs(root):
    if root is None:
        return 0

    return root.val + tree_sum_dfs(root.left) + tree_sum_dfs(root.right)


a = Node(1)
b = Node(6)
c = Node(0)
d = Node(3)
e = Node(-6)
f = Node(2)
g = Node(2)
h = Node(2)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h

assert tree_sum_bfs(a) == 10
assert tree_sum_dfs(a) == 10

print("All tests passed!")
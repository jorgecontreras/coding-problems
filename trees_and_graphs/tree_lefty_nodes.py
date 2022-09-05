# LEFTY NODES
"""
Write a function, lefty_nodes, that takes in the root of a binary tree. 
The function should return a list containing the left-most value on every level of the tree. 
The list must be ordered in a top-down fashion where the root is the first item.

Note that the left-most node on a level may not necessarily be a left child.
"""

class Node:
   def __init__(self, val):
     self.val = val
     self.left = None
     self.right = None

# Time complexity : O(N) - traversing all nodes of the tree
# Space complexity: O(N)  - storing all nodes in the call stack(DFS) or queue(BFS)

from collections import deque
# BFS
def lefty_nodes_bfs(root):
    queue = deque([root])
    output = []
    while queue:
        size = len(queue)
        for i in range(size):
            node = queue.popleft()
            if i == 0:
                output.append(node.val)
            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

    return output


# DFS
def lefty_nodes_dfs(root, level = 0, output = []):
    # base case
    if not root:
        return
    
    if level == len(output):
        output.append(root.val)

    lefty_nodes_dfs(root.left, level + 1, output)
    lefty_nodes_dfs(root.right, level + 1, output)

    return output
    
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
e.right 


assert lefty_nodes_dfs(a) == [ 'a', 'b', 'd', 'g' ]
assert lefty_nodes_bfs(a) == [ 'a', 'b', 'd', 'g' ]

print("All tests passed!")
# Binary tree right side view
#
# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
#
# Approach: Breadth First Search
#
# Time complexity: O(N)
# Space complexity: O(N)

from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def right_view(root):

    def dfs(node, level):
        if level == len(result):
            result.append(node.val)

        # do right side first - right side view
        if node.right:
            dfs(node.right, level + 1)

        # do left after
        if node.left:
            dfs(node.left, level + 1)

    if not root:
        return []
    
    result = []

    dfs(root, 0)

    return result        

# tests
n = Node(3)
n.left = Node(9)
n.right = Node(4)
n.left.left = Node(7)
n.left.right = Node(1)
n.right.left = Node(1)
n.right.right = Node(7)
assert right_view(n) == [3,4,7]

n = Node(3)
assert right_view(n) == [3]

n = Node(3)
n.left = Node(4)
n.right = Node(4)
n.left.left = Node(7)
n.left.right = Node(1)
n.right.left = Node(1)
n.right.right = Node(7)
n.left.right.left = Node(0)

assert right_view(n) == [3,4,7,0]

print("all tests passed.")
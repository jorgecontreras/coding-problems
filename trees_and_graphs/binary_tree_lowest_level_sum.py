# Given a binary tree, return the level of the tree with minimum sum.
#
# Time complexity: O(NlogN)
# Space complexity: O(N)
# ===================================================================

from collections import deque
import math 

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    

def smallest_level(root):
    if not root:
        return None

    min_level = math.inf

    queue = deque([root])

    while queue:
        level_size = len(queue)
        level_sum = 0

        for i in range(level_size):
            node = queue.popleft()
            level_sum += node.val

            if i == level_size - 1:
                min_level = min(min_level, level_sum)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

    return min_level

# build tree
# level 1: 
root = Node(8) # level sum = 8

# level 2
root.left = Node(1) 
root.right = Node(4) # level sum = 5

# level 3
root.left.left = Node(1)
root.left.right = Node(5)
root.right.left = Node(4) 
root.right.right = Node(2) # level sum: 12

# test
assert smallest_level(root) == 5

print("all tests passed.")
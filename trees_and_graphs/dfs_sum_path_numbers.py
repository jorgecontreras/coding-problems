# ALL PATHS SUM
#
# Depth First Search
# 
# Given a binary tree where each node can only have a digit (0-9) value, each root-to-leaf path will represent a number. 
# Find the total sum of all the numbers represented by all paths.
#
# Time complexity: O(N)
# Space complexity: O(N)

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def dfs(node, total, path):
    if not node:
        return

    path.append(str(node.val))

    if not node.left and not node.right: #end of path
        total.append(int("".join(path)))

    else:
        dfs(node.left, total, path)
        dfs(node.right, total, path)

    #backtracking
    del path[-1]

def sum_path_numbers(node):
    total = []
    dfs(node, total, [])
    return sum(total)

n1 = Node(1)
n1.left = Node(7)
n1.right = Node(9)
n1.right.left = Node(2)
n1.right.right = Node(9)

assert sum_path_numbers(n1) == 408

print("all tests passed.")
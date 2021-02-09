# ALL PATHS FOR A SUM
#
# Depth First Search

# Given a binary tree and a number ‘S’, find all paths from root-to-leaf such that the sum of all the node values of each path equals ‘S’.

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    def dfs(self, node, s, path=[]):

        if not node:
            return 

        # continue on same path
        path.append(node.val)

        # decrease the target sum as we approach
        s -= node.val

        # leaf node reached. "s" should be 0 to meet the criteria
        if not node.left and not node.right and s == 0:
                self.paths.append(list(path))

        # keep searching in left and right branches
        else:
            self.dfs(node.left, s, path)
            self.dfs(node.right, s, path)

        # backtracking
        del path[-1]

    def paths_sum(self, node, s):
        self.paths = []
        self.dfs(node, s)
        return self.paths

solution = Solution()

# test 1
n1 = Node(1)
n1.left = Node(7)
n1.right = Node(9)
n1.left.left = Node(4)
n1.left.right = Node(5)
n1.right.left = Node(2)
n1.right.right = Node(7)
s1 = 12

# test 2
n2 = Node(12)
n2.left = Node(7)
n2.right = Node(1)
n2.left.left = Node(4)
n2.right.left = Node(10)
n2.right.right = Node(5)
s2 = 23

assert solution.paths_sum(n1, s1) == [[1,7,4],[1,9,2]]
assert solution.paths_sum(n2, s2) == [[12,7,4],[12,1,10]]

print("all tests passed.")
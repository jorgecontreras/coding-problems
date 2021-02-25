# Binary tree diameter
#
# Time complexity: O(N)
# Space complexity: O(N)

class Node:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None

class Solution:
    def diameter(self, root):
        #diameter is the depth of left + depth of right branches
        def depth(root):
            if not root:
                return 0

            left = depth(root.left)
            right = depth(root.right)

            self.diameter = max(self.diameter, left + right)

            return max(left, right) + 1

        self.diameter = 0
        depth(root)
        return self.diameter

# tests
s = Solution()

n = Node(2)
n.left = Node(5)
n.left.left = Node(7)
n.left.right = Node(1)
n.left.left.left = Node(6)
n.left.left.left.left = Node(3)
n.left.left.left.left.left = Node(8)
n.left.left.left.left.left.left = Node (4)

n.left.right.left = Node(9)
n.left.right.right = Node(0)

assert s.diameter(n) == 7

print("all tests passed.")
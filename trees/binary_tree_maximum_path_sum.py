# binary tree maximum path sum

import math
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    def binary_tree_max_sum(self, root):

        def max_gain(node):
            if not node:
                return 0

            left_gain = max(0, max_gain(node.left))
            right_gain = max(0, max_gain(node.right))
            subtree_sum = node.val + left_gain + right_gain
            self.max_sum = max(self.max_sum, subtree_sum)

            return node.val + max(left_gain, right_gain)

        self.max_sum = -math.inf
        max_gain(root)
        
        return self.max_sum


"""

                    *5*

            *2*             *3*

        4       *8*               *9*
"""

n = Node(5)
n.left = Node(2)
n.right = Node(3)

n.left.left = Node(4)
n.left.right = Node(8)
n.right.right = Node(9)

# should be 17
s = Solution()
assert s.binary_tree_max_sum(n) == 27
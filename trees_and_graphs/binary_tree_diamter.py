# binary tree diameter

class Solution:
    class Node:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None

    def diameter(root):
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
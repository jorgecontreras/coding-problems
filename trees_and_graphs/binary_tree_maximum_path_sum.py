# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import math

class Solution(object):
    
    def max_gain(self, node):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not node:
            return 0
        
        left_gain = max(self.max_gain(node.left), 0)
        right_gain = max(self.max_gain(node.right), 0)
        
        subtree_sum = node.val + left_gain + right_gain
        self.max_sum = max(self.max_sum, subtree_sum)
        
        return node.val + max(left_gain, right_gain) 
        
    def maxPathSum(self, root):
        self.max_sum = -math.inf
        self.max_gain(root)
        
        return self.max_sum
    
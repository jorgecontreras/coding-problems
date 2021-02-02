# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        #in order traversal
        def traverse(root):
            
            if not root: 
                return True
            
            #left
            if not traverse(root.left):
                return False
            
            #node
            if root.val <= self.prev:
                return False
            
            #right
            self.prev = root.val
            return traverse(root.right)
        
        self.prev = -math.inf
        return traverse(root)
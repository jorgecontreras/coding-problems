import math

# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Node) -> bool:
        
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

s = Solution()

n = Node(2)
n.left = Node(1)
n.right = Node(3)

assert s.isValidBST(n) == True

n = Node(5)
n.left = Node(1)
n.right = Node(4)
n.right.left = Node(3)
n.right.right = Node(6)

assert s.isValidBST(n) == False

print("all tests passed.")
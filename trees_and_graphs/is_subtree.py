"""
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
 

Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
"""

# Time complexity: O(m*n)
# Space complexity: O(n), for the depth of the recursion 

class Solution:

    def isSubtree(self, s, t):
        # base case
        if not s:
            return False
        # if subtree found
        if self.isEqual(s, t):
            return True

        # recurse left and right
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isEqual(self, p, q):
        if p and q:
            return p.val == q.val and self.isEqual(p.left, q.left) and self.isEqual(p.right, q.right)
        
        return p is q
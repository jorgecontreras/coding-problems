"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class BinaryTreeToDll(object):
    def convert(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        self.last = None
        self.first = None
        
        #in-order traverse
        # left -> node -> right    
        def traverse(node):
            
            if node:
                #left
                traverse(node.left)
                
                #node
                if self.last:
                    # create link
                    self.last.right = node
                    node.left = self.last
                else:
                    # save first
                    self.first = node

                self.last = node

                #right
                traverse(node.right)

        if not root:
            return None
        
        # trigger the process
        traverse(root)
        
        #close the dll
        self.last.right = self.first
        self.first.left = self.last
        
        return self.first
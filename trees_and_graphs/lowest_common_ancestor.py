# lowest common ancestor
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    def lowest_common_ancestor(root, p, q):

        def dfs(node):
            if not node:
                return False

            #left
            left = dfs(node.left)

            #right
            right = dfs(node.right)

            #parent
            parent = node == p or node == q

            if left + right + parent >= 2:
                self.lca = node 

            return parent or left or right 

        self.lca = None
        dfs(root)
        return self.lca





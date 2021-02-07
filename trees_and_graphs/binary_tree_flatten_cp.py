# flatten binary tree


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
class Solution:
    def flatten_r(self, node):

        if not node:
            return None

        if not node.left and not node.right: #leaf node
            return node

        left_tail = self.flatten_r(node.left) 
        right_tail = self.flatten_r(node.right) 

        if left_tail: #4
            # shuffle links
            left_tail.right = node.right
            node.right = node.left
            node.left = None

        return right_tail if right_tail else left_tail



    def flatten(self, root):
        self.flatten_r(root)


n = Node(5)
n.left = Node(8)
n.right = Node(3)
n.left.left = Node(4)
n.left.right = Node(1)
n.right.left = Node(3)
n.right.right = Node(6)

s = Solution()

s.flatten(n)

while n:
    print(n.val)
    n = n.right
# binary tree flatten to linked list
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    def flatten_r(self, node):

        if not node:
            return None 

        if not node.right and not node.left:
            return node

        left_tail = self.flatten_r(node.left)
        right_tail = self.flatten_r(node.right)

        # shuffle pointers
        if left_tail:
            left_tail.right = node.right 
            node.right = node.left
            node.left = None

        return right_tail if right_tail else left_tail

    def show(self, node):

        print(node.val)
        while node.right:
            print(node.left)
            print(node.right.val)
            node = node.right
            

    def flatten(self, root):
        self.flatten_r(root)


n = Node(1)
n.left = Node(2)
n.right = Node(5)
n.left.left = Node(3)
n.left.right = Node(4)
n.right.right = Node(6)

s = Solution()

s.flatten(n)
s.show(n)

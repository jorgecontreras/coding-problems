# find max sum of path in  a binary tree
# root to leaf

class Node:
    def __init__(self, val):
        self.val = val 
        self.left = None
        self.right = None

class Solution:
    def max_path_sum(self, root):

        def traverse(node, path_sum=0):
            if not node:
                return 0

            path_sum += node.val
            
            if not node.left and not node.right:
                self.biggest_sum = max(self.biggest_sum, path_sum)
            
            if node.left:
                traverse(node.left, path_sum)

            if node.right:
                traverse(node.right, path_sum)
    
        self.biggest_sum = 0
        traverse(root)
        return self.biggest_sum

s = Solution()

n = Node(6)
n.left = Node(3)
n.right = Node(5)

print(s.max_path_sum(n))
# expected = 6->5 = 11

n.left.left = Node(2)
n.left.right = Node(4)
n.right.left = Node(8)
n.right.right = Node(1)

print(s.max_path_sum(n))
# expected = 6-> 5 -> 8 = 19

n.left.left.left = Node(33)
print(s.max_path_sum(n))
# expected = 6->3->2->33 = 44
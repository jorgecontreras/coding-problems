# binary tree right view

from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    
class Solution:

    def right_view(self, root):

        if not root:
            return []

        queue = deque()
        queue.append(root)
        result = []

        while queue:
            level_size = len(queue)

            for i in range(level_size):
                node = queue.popleft()
                if i+1 == level_size:
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result
                



n = Node(5)
n.left = Node(6)
n.right = Node(2)
n.left.left = Node(1)
n.left.right = Node(7)
n.right.left = Node(9)
n.right.right = Node(10)
n.left.left.right = Node(1)

# expected
output = [5, 2, 10, 1]
s = Solution()

print(s.right_view(n))
assert (s.right_view(n)) == output
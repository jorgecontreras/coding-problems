# binary tree right side view
from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def right_view(root):

    if not root:
        return []
    
    queue = deque([root])
    result = []

    while queue:
        level_size = len(queue)
        rightmost = queue[level_size - 1]
        result.append(rightmost.val)
        
        for _ in range(level_size):
            node = queue.popleft()

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

    return result        

# tests
n = Node(3)
n.left = Node(4)
n.right = Node(4)
n.left.left = Node(7)
n.left.right = Node(1)
n.right.left = Node(1)
n.right.right = Node(7)
assert right_view(n) == [3,4,7]

n = Node(3)
assert right_view(n) == [3]

n = Node(3)
n.left = Node(4)
n.right = Node(4)
n.left.left = Node(7)
n.left.right = Node(1)
n.right.left = Node(1)
n.right.right = Node(7)
n.left.right.left = Node(0)

assert right_view(n) == [3,4,7,0]

print("all tests passed.")
# LEVEL AVERAGES
from collections import deque

# Time: O(N) --> traverse all nodes in the tree
# Space: O(N) --> store values in the queue

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def level_averages(root):
    queue = deque([root])

    output = []

    while queue:
        size = len(queue)
        sum = 0
        for _ in range(size):
            node = queue.popleft()
            sum += node.val

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        avg = sum / size
        output.append(avg)

    return output

# sample tree
a = Node(3)
b = Node(5)
c = Node(2)
d = Node(7)
e = Node(4)
f = Node(3)


#       a          3
#      / \
#     b   c        3.5
#    / \   \
#   d   e   f      4.x

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

ans = level_averages(a)

print(ans)
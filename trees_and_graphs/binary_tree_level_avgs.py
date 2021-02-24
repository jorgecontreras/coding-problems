from collections import deque

class Node:
   def __init__(self, val):
       self.val = val
       self.left = None
       self.right = None

def traverse(node):

    if not node:
        return 0
        
    queue = deque()
    queue.append(node)
    results = []

    while queue:
        levelSize = len(queue)
        total = 0

        for i in range(levelSize):
            node = queue.popleft()
            total += node.val

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        levelAverage = total / levelSize
        results.append(levelAverage)

    return results

n = Node(5) # 5

n.left = Node(3) #3.5
n.right = Node(4)

n.left.left = Node(4) #7
n.left.right = Node(6)
n.right.left = Node(8)
n.right.right = Node(10)

print(traverse(n))
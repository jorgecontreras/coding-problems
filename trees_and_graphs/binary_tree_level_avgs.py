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

        while levelSize > 0:
            node = queue.popleft()
            levelSize -= 1
            total += node.val

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        levelAverage = total / levelSize
        results.append(levelAverage)

    return results


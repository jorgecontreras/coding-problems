# binary tree right side view

from collections import deque

def right_view(root):

    if not root:
        return []
    
    queue = deque()
    queue.append(root)
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

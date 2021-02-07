# level averages binary tree

# Given a binary tree, populate an array to represent the averages of all of its levels.

from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def level_avg(root):

    result = []
    queue = deque()
    queue.append(root)

    while len(queue) > 0:
        level_size = len(queue)
        current_sum = 0 

        for _ in range(level_size):
            node = queue.popleft()
            current_sum += node.val

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        result.append(current_sum / level_size)

    return result

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  root.right.left.left = TreeNode(20)
  root.right.left.right = TreeNode(17)
  print("Level averages: " + str(level_avg(root)))


main()
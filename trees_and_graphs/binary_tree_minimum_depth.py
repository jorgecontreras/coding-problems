# BINARY TREE MINIMUM DEPTH
#
# Time complexity: O(N)
# Space complecity: O(N)
#
# Find the minimum depth of a binary tree. 
# The minimum depth is the number of nodes along the shortest 
# path from the root node to the nearest leaf node.

from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def find_minimum_depth(root):
    
    level = 0
    queue = deque([root])
    
    while queue:
        level += 1
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.popleft()
            if not node.left and not node.right:
                return level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return 0

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  assert find_minimum_depth(root) == 2
  root.left.left = TreeNode(9)
  root.right.left.left = TreeNode(11)
  assert find_minimum_depth(root) == 3
  print("all tests passed.")

main()
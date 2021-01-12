# Binay Tree Level Order Traversal

from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def traverse(root):
  result = []
  
  queue = deque()
  queue.append(root)
  
  while len(queue) > 0:
      levelSize = len(queue)
      currentLevel = []
      
      while levelSize > 0:
          node = queue.popleft()
          currentLevel.append(node.val)
          levelSize -= 1
          
          if node.left:
              queue.append(node.left)
          if node.right:
              queue.append(node.right)
      
      result.append(currentLevel)
      
  return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level order traversal: " + str(traverse(root)))


main()
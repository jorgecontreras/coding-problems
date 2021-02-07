# reverse-level-traversal

# Binay Tree Level Order Traversal

# Given a binary tree, populate an array to represent its 
# level-by-level traversal in reverse order, 
# i.e., the lowest level comes first. 
# You should populate the values of all nodes in 
# each level from left to right in separate sub-arrays.

from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def traverse(root):
  
  result = deque()
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
      
      result.appendleft(currentLevel)
      
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
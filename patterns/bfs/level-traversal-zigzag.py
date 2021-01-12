# level traversal zigzag

# reverse-level-traversal

# Binay Tree Level Order Traversal

# Given a binary tree, populate an array to represent its 
# zigzag level order traversal. 
# You should populate the values of all nodes of the 
# first level from left to right, 
# then right to left for the next level and keep 
# alternating in the same manner for the following levels.

from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def traverse(root):
  
  result = deque()
  queue = deque()
  queue.append(root)
  leftToRight = True

  while len(queue) > 0:
      levelSize = len(queue)
      currentLevel = deque()
      
      while levelSize > 0:
          node = queue.popleft()
          
          if leftToRight:
              currentLevel.append(node.val)
          else:
              currentLevel.appendleft(node.val)

          levelSize -= 1
          
          if node.left:
              queue.append(node.left)
          if node.right:
              queue.append(node.right)
      
      result.append(currentLevel)
      leftToRight = not leftToRight

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
  print("Zigzag traversal: " + str(traverse(root)))


main()
# BINARY TREE - LEVEL ORDER SUCCESSOR
#
# Tree Breadth First Search
# Time complexity: O(N)
# Space complexity: O(N)
#
# Given a binary tree and a node, find the level order successor of the given node in the tree. 
# The level order successor is the node that appears right after the given node in the level order traversal.

from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def find_successor(root, key):

    queue = deque([root])

    while queue:
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.popleft()

            
            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

            # found the predecessor. 
            # next element in the queue is the successor we look for
            if node.val == key:
                return queue[0] if queue else None

    return -1

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  result = find_successor(root, 12)
  if result:
    assert result.val == 7
  result = find_successor(root, 9)
  if result:
    assert result.val == 10

  print("all tests passed.")

main()
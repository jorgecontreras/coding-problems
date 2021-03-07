# Binary tree flatten to linked list
#
# LeetCode 114 https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
#
# Given the root of a binary tree, flatten the tree into a "linked list":
#
# The "linked list" should use the same TreeNode class where the right child pointer points 
# to the next node in the list and the left child pointer is always null.
# 
# The "linked list" should be in the same order as a pre-order traversal of the binary tree.
#

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    def flatten_recursive(self, node):

        if not node:
            return None 

        if not node.right and not node.left:
            return node

        left_tail = self.flatten_recursive(node.left)
        right_tail = self.flatten_recursive(node.right)

        # shuffle pointers: this is the flatten
        if left_tail:
            left_tail.right = node.right 
            node.right = node.left
            node.left = None

        return right_tail if right_tail else left_tail

    def check(self, node):
        result = []

        result.append(node.val)
        while node.right:
            result.append(node.right.val)
            node = node.right

        return result
            

    def flatten(self, root):
        self.flatten_recursive(root)


n = Node(1)
n.left = Node(2)
n.right = Node(5)
n.left.left = Node(3)
n.left.right = Node(4)
n.right.right = Node(6)

s = Solution()

s.flatten(n)
assert s.check(n) == [1,2,3,4,5,6]

print("all tests passed.")

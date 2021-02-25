# twosum Binary Search Trees
# Given the roots of two binary search trees, root1 and root2, return true if and only if there is a node in the first tree and a node in the second tree whose values sum up to a given integer target.
#
# Time complexity: O(N)
# Space complexity: O(N)

from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def two_sum_bst(root1, root2, target):
    complements = set()

    #traverse tree 1 and store the complements in a set
    queue = deque([root1])

    while queue:
        size = len(queue)
        for _ in range(size):
            node = queue.popleft()
            complement = target - node.val 
            complements.add(complement)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

    # traverse tree 2 and look for each value in the complement set
    queue = deque([root2])

    while queue:
        size = len(queue)
        for _ in range(size):
            node = queue.popleft()
            if node.val in complements:
                return True
            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)
    
    return False

# tests
n1 = Node(2)
n1.left = Node(1)
n1.right = Node(4)

n2 = Node(1)
n2.left = Node(0)
n2.right = Node(3)

assert two_sum_bst(n1, n2, 5) == True

n1 = Node(0)
n1.left = Node(-10)
n1.right = Node(10)

n2 = Node(5)
n2.left = Node(1)
n2.right = Node(7)
n2.left.left = Node(0)
n2.left.right = Node(2)

assert two_sum_bst(n1, n2, 18) == False

print("all tests passed.")
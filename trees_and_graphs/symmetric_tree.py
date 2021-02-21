# SYMMETRIC TREE

# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
#
# Time complexity: O(n), because we traverse the tree once
# Space complexity: O(n), for the call stack, being the worst case a linear tree.

def is_symmetric(root):
    if not root:
        return True
    
    return is_mirror(root.left, root.right)

def is_mirror(left, right):
    if left and right:
        return left.val == right.val and is_mirror(left.left, right.right) and is_mirror(left.right, right.left)
    
    return left is right
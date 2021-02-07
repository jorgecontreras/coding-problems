# binary tree path sum

# Given a binary tree and an integer k, return whether there exists a root-to-leaf path that sums up to k.

# For example, given k = 18 and the following binary tree:

#     8
#    / \
#   4   13
#  / \   \
# 2   6   19
# Return True since the path 8 -> 4 -> 6 sums to 18.
#

def path_sum_exists(root, k):
    if not root:
        return False

    k -= root.val
    if root.left is None and root.right is None: # leaf node found
        return k == 0

    return path_sum_exists(root.left, k) or path_sum_exists(root.right, k)
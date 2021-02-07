# binary tree path sum

def binary_path_sum(node, k):

    if not node:
        return False

    k -= node.val
    if node.left is None and node.right is None: #leaf found 
        return k == 0

    return binary_path_sum(node.left, k) or binary_path_sum(node.right, k)


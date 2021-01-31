# binary tree path sum
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def binary_tree_path_sum(root, k):
    
    if not root:
        return False

    k -= root.val
    if root.left is None and root.right is None:
        return k == 0

    return binary_tree_path_sum(root.left, k) or binary_tree_path_sum(root.right, k)


n = Node(5)
n.left = Node(2)
n.right = Node(3)

n.left.left = Node(4)
n.left.right = Node(8)
n.right.right = Node(9)

k = 17

print(binary_tree_path_sum(n, k))

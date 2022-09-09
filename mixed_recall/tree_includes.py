# TREE INCLUDES

def tree_includes(root, target):
    if not root:
        return False

    if root.val == target:
        return True

    return tree_includes(root.left, target) or tree_includes(root.right, target)
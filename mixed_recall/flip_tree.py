# FLIP TREE

def flip_tree(root):
    if not root:
        return

    root.left, root.right = root.right, root.left
    flip_tree(root.left)
    flip_tree(root.right)

    return root
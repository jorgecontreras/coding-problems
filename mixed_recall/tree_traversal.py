# TREE TRAVERSALS

# left, self, right
def inorder(root, values=[]):
    if not root:
        return 

    inorder(root.left, values)
    values.append(root.val)
    inorder(root.right, values)
    


# self, left, right
def preorder(root, values=[]):
    if not root:
        return 

    values.append(root.val)
    inorder(root.left, values)
    inorder(root.right, values)
    


# left, right, self
def postorder(root, values=[]):
    if not root:
        return 

    inorder(root.left, values)
    inorder(root.right, values)
    values.append(root.val)
    



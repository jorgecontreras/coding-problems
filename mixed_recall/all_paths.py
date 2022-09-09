# ALL PATHS FROM ROOT TO LEAVES

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def all_paths(root):
    paths = []
    _paths(root, paths, [])
    return paths

def _paths(root, paths, path):
    if not root:
        return []

    path.append(root.val)
    # leaf found
    if not root.left and not root.right:
        paths.append(list(path))

    _paths(root.left, paths, path)
    _paths(root.right, paths, path)

    # backtrack
    del path[-1]


# sample tree
a = Node(3)
b = Node(5)
c = Node(2)
d = Node(7)
e = Node(4)
f = Node(3)


#       a          3
#      / \
#     b   c        3.5
#    / \   \
#   d   e   f      4.x

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

ans = all_paths(a)

print(ans)
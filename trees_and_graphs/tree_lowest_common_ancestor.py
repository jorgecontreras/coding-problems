# TREE LOWEST COMMON ANCESTOR
"""
Write a function, lowest_common_ancestor, that takes in the root of a binary tree and two values. 
The function should return the value of the lowest common ancestor of the two values in the tree.

You may assume that the tree values are unique and the tree is non-empty.

Note that a node may be considered an ancestor of itself.
"""
class Node:
   def __init__(self, val):
     self.val = val
     self.left = None
     self.right = None

def lca(root, val1, val2):

    #find path to val1
    path1 = set(path(root, val1))

    #find path to val2
    path2 = path(root, val2)
    if not path1 or not path2:
        return None

    # locate the first path element that overlaps
    for node in path2:
        if node in path1:
            return node 
    
    return None

def path(root, target):
    if not root:
        return None

    if root.val == target:
        return [ root.val ]

    left = path(root.left, target)
    if left:
        left.append(root.val)
        return left

    right = path(root.right, target)
    if right:
        right.append(root.val)
        return right 

    return None 

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
e.right = h

#      a
#    /    \
#   b      c
#  / \      \
# d   e      f
#    / \
#    g  h

assert lca(a, 'd', 'h') == 'b'
assert lca(a, 'd', 'g') == 'b' 
assert lca(a, 'g', 'c') == 'a'
assert lca(a, 'b', 'g') == 'b'
assert lca(a, 'f', 'x') == None
print("All tests passed!")
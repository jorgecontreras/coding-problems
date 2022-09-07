# LOWEST COMMON ANCESTOR
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def lca(root, nodeA, nodeB):
    # find route from root to nodeA
    # [ 'a', 'b', 'f', 'x', 'y']
    routeA = route(root, nodeA)

    # find route from root to nodeB
    # [ 'a', 'b', 'g', 'h', 'z']
    routeB = route(root, nodeB)

    # find the first element that overlaps
    routeA = set(routeA)
    for node in routeB:
        if node in routeA:
            return node

def route(root, target):
    if not root:
        return []

    if root.val == target:
        return [ root.val ]

    left = route(root.left, target)
    if left:
        left.append(root.val)
        return left

    right = route(root.right, target)
    if right:
        right.append(root.val)
        return right

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

t1 = lca(a, 'd', 'h')

assert t1 == 'b'

l = Node('l')
m = Node('m')
n = Node('n')
o = Node('o')
p = Node('p')
q = Node('q')
r = Node('r')
s = Node('s')
t = Node('t')

l.left = m
l.right = n
n.left = o
n.right = p
o.left = q
o.right = r
p.left = s
p.right = t

#        l
#     /     \
#    m       n
#         /    \
#         o     p
#        / \   / \
#       q   r s   t

assert lca(l, 'r', 'p') == 'n'

print("All tests passed!")
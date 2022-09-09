# SUBTREE of ANOTHER TREE
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# empty tree is subtree of another tree? YES
# empty tree is subtree of empty tree? NO
def is_subtree(s, t):
    # edge cases
    if s is None:
        return False
    
    if t is None:
        return True

    # both trees are the same, by definition t is subtree of s
    if same_tree(s, t):
        return True

    left = is_subtree(s.left, t)
    right = is_subtree(s.right, t)

    return left or right

    
def same_tree(r, v):
    if r is None and v is None:
        return True

    if r and v:
        return r.val == v.val and same_tree(r.left, v.left) and same_tree(r.right, v.right)

    return False
    







# small tree
t = Node('t')
u = Node('u')
s = Node('s')
s.left = t
s.right = u

# large tree
a = Node('a')
b = Node('b')
c = Node('c')
a.left = b
a.right = c
c.left = s

ans = is_subtree(a, s)

print(ans)
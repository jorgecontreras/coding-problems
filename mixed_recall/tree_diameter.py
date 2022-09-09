# TREE DIAMETER: The longest path between any two nodes

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Diameter:
    def tree_diameter(self, root):
        self.diameter = 0
        self.longest_path(root)
        return self.diameter
        

    def longest_path(self, root):
        if not root:
            return 0

        left = self.longest_path(root.left)
        right = self.longest_path(root.right)

        self.diameter = max(self.diameter, left + right)

        return 1 + max(left, right)


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

d = Diameter()
ans = d.tree_diameter(a)

print(ans)
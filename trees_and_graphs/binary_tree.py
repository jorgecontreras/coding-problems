# Create a binary tree

class Node:
    def __init__(self, x):
        self.val = x 
        self.left = None
        self.right = None

    def insert(self, x):
        if self.val:
            if x <= self.val:
                if self.left is None:
                    self.left = Node(x)
                else:
                    self.left.insert(x)
            elif x > self.val:
                if self.right is None:
                    self.right = Node(x)
                else:
                    self.right.insert(x)
        else:
            self.val = x
        
    def printTree(self):
        # print left
        if self.left:
            self.left.printTree()
        # print node
        print(self.val)
        # print right
        if self.right:
            self.right.printTree()

# create the tree
root = Node(5)
root.insert(11)
root.insert(13)
root.insert(2)
root.insert(7)
root.insert(1)
root.insert(8)
root.insert(4)
root.insert(4)

root.printTree()
    
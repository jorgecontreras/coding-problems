# sorted array to BST
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def sorted_array_to_bst(nums):

    def helper(start, end):
        if start > end:
            return None

        p = start + (end-start) // 2

        root = Node(nums[p])
        root.left = helper(start, p-1)
        root.right = helper(p+1, end)

        return root

    return helper(0, len(nums) - 1)


t1 = [-10, -3, 0, 5, 9]

root = sorted_array_to_bst(t1)

print(root.val)
print(root.left.val)
print(root.right.val)
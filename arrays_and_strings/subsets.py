# subsets

# Problem Statement #
# Given a set with distinct elements, find all of its distinct subsets.

# Example 1:

# Input: [1, 3]
# Output: [], [1], [3], [1,3]
# Example 2:

# Input: [1, 5, 3]
# Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3]

# time complexity:
# O(2^N)
# 
# space complexity:
# O(N 2^N)
#
def subsets(nums):
    subsets = [[]]

    for n in nums:
        create = []
        for s in subsets:
            create += [s + [n]]
        subsets += create

    return subsets

t1 = [1, 5, 3]

print(subsets(t1))
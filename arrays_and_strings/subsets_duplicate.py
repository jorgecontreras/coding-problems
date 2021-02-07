# subsets with duplicate

# Problem Statement #
# Given a set of numbers that might contain duplicates, find all of its distinct subsets.

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
    nums.sort()
    subsets = [[]]
    prev = None

    for n in nums:
        if n != prev: 
            create = []
            for s in subsets:
                create += [s + [n]]
            subsets += create
        else:
            new = []
            for c in create:
                new += [c + [n]]
            subsets += new
        prev = n


    return subsets

t1 = [1, 5, 3, 3]

print(subsets(t1))
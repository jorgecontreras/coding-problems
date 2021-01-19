# remove duplicates

# Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; after removing the duplicates in-place return the length of the subarray that has no duplicate in it.

# Example 1:

# Input: [2, 3, 3, 3, 6, 9, 9]
# Output: 4
# Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].
# Example 2:

# Input: [2, 2, 2, 11]
# Output: 2
# Explanation: The first two elements after removing the duplicates will be [2, 11].

def remove_duplicates(nums):
    p1 = 0
    for p2 in range(1, len(nums)):
        if nums[p2] != nums[p1]:
            p1 += 1
        nums[p1] = nums[p2]

    return p1+1

        
t1 = [2, 3, 3, 3, 6, 9, 9]
t2 = [2, 2, 2, 11]

assert remove_duplicates(t1) == 4
assert remove_duplicates(t2) == 2
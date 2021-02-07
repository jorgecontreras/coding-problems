# find smallest positive number

"""
Given an unsorted array containing numbers, find the smallest missing positive number in it.

Example 1:

Input: [-3, 1, 5, 4, 2]
Output: 3
Explanation: The smallest missing positive number is '3'
Example 2:

Input: [3, -2, 0, 1, 2]
Output: 4
Example 3:

Input: [3, 2, 5, 1]
Output: 4
"""

# the key is to ignore out of range numbers: negative and larger than array size
# sort the good ones using cyclic sort
# finally, traverse the array to find the smallest missing

def find_smallest_positive(nums):
    i = 0
    while i < len(nums):
        # ignore out of bound nums
        if nums[i] < 0 or nums[i] > len(nums):
            i += 1
            continue

        # sort the good ones
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]

        else:
            i += 1

    # traverse the array until we find a mismatch
    for i in range(len(nums)):
        if nums[i] != i + 1:
            return i + 1

    return len(nums) + 1

t1 = [-3, 1, 5, 4, 2]
t2 = [3, -2, 0, 1, 2]
t3 = [3, 2, 5, 1]

assert find_smallest_positive(t1) == 3
assert find_smallest_positive(t2) == 4
assert find_smallest_positive(t3) == 4

print("all tests passed.")
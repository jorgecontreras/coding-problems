"""
Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

Example 1:

Input: nums = [2,2,3,2]
Output: 3
Example 2:

Input: nums = [0,1,0,1,0,1,99]
Output: 99
"""

def seen_once(nums):
    once = twice = 0

    for n in nums:
        once = ~twice & (once ^ n)
        twice = ~once & (twice ^ n)

    return once

t1 = [2,2,3,2]
t2 = [0,1,0,1,0,1,99]

assert seen_once(t1) == 3
assert seen_once(t2) == 99

print("all tests passed.")
"""
Problem Statement #
Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.

Example 1:

Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].
Example 2:

Input: [2, 3, 4, 1, 5], k=2 
Output: 7
Explanation: Subarray with maximum sum is [3, 4].
"""

def max_sum_subarray(nums, k):
    start = 0
    _sum = 0
    max_sum = 0

    for i in range(len(nums)):
        _sum += nums[i]
        if i-start >= k - 1:
            max_sum = max(max_sum, _sum)
            _sum -= nums[start]
            start += 1
    
    return max_sum
    

t1 = [2, 1, 5, 1, 3, 2]
k1 = 3

t2 = [2, 3, 4, 1, 5]
k2 = 2
o1 = max_sum_subarray(t1, k1)
o2 = max_sum_subarray(t2, k2)

assert o1 == 9
assert o2 == 7
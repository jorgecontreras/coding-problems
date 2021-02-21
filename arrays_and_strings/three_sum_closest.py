# 3 sum closest
#
# Time complexity: O(n^2logN): nested array traversal + sort
# Space complexity: O(n)
"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
 
"""
def three_sum_closest(nums, target):
    diff = float('inf')
    #sort
    nums.sort()

    for i in range(len(nums)):
        lo, hi = i+1, len(nums) - 1
        while (lo < hi):
            _sum = nums[i] + nums[lo] + nums[hi]
            if abs(target - _sum) < abs(diff):
                diff = target - _sum
            if _sum < target:
                lo += 1
            else:
                hi -= 1
        
        if diff == 0:
            break
    return target - diff

nums1 = [2,4,8,11,20]
target1 = 15

nums2 = [-1,2,1,-4]
target2 = 1

assert three_sum_closest(nums1, target1) == 14
assert three_sum_closest(nums2, target2) == 2

print("all tests passed.")
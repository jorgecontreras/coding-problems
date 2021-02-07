"""
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107


"""

# note: sliding window pattern could not be applier here because the input can contain negative numbers


class Solution:
    def subarraySum(self, nums, k) -> int:
        count = 0
        _sum = 0
        sums = {0: 1}

        for i in range(len(nums)):
            _sum += nums[i]

            if (_sum - k) in sums:
                count += sums[_sum-k]
            sums[_sum] = sums.get(_sum, 0) + 1
        
        return count


s = Solution()

print(s.subarraySum([-1,-1,1], 0))
print(s.subarraySum([1], 0))
print(s.subarraySum([1,2,3], 3))
print(s.subarraySum([1,1,1], 2))
print(s.subarraySum([1,-1,0], 0))

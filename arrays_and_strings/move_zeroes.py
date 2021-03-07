# move zeroes
#
# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Example:

# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Note:

# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
#
# Solution: in reality, we are moving non-zeroes to the left, resulting in all zeroes on the right

from collections import deque

class Solution:
    def goodMove(self, nums):
        anchor = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[anchor], nums[i] = nums[i], nums[anchor]
                anchor += 1
        
        print(nums)

t1 = [0,1,0,3,12]
s = Solution()
ans = s.goodMove(t1)

assert t1 == [1, 3, 12, 0, 0]
print("all tests passed.")
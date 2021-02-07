# move zeroes

# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.


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
print(s.goodMove(t1))
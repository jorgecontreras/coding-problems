# Rank Transform of an array

# Given an array of integers arr, replace each element with its rank.

# The rank represents how large the element is. The rank has the following rules:

# Rank is an integer starting from 1.
# The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
# Rank should be as small as possible.

from heapq import * 

class Solution:
    def arrayRankTransform(self, arr):
        nums = arr.copy()
        nums.sort()
        r = 1
        ranks = {}
        for n in nums:
            if n not in ranks:
                ranks[n] = r
                r += 1

        result = []
        for n in arr:
            result.append(ranks[n])
        
        return result
            

        
s = Solution()

t2 = [40,10,20,30]

print(s.arrayRankTransform(t2))
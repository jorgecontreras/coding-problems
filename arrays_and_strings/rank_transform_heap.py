# Rank Transform of an array

# Given an array of integers arr, replace each element with its rank.

# The rank represents how large the element is. The rank has the following rules:

# Rank is an integer starting from 1.
# The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
# Rank should be as small as possible.

from heapq import * 

class Solution:
    def arrayRankTransform(self, arr):
        heap = []
        
        #insert them into the heap
        for i, n in enumerate(arr):
            heappush(heap, (n, i))

        # pop elements and assign them a rank
        rank = 0
        prev = float('-inf')
        while len(heap) > 0:
            e = heappop(heap)
            if e[0] > prev:
                rank += 1
            prev = e[0]
            arr[e[1]] = rank
            
        return arr
        
s = Solution()

t2 = [-1,0,1,-1,-1,-1,-1,0,0,3,4,5,6,-1]

print(s.arrayRankTransform(t2))
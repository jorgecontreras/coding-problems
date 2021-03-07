# median number stream

# Design a class to calculate the median of a number stream. The class should have the following two methods:

# 1. insert. store the number in the class.
# 2. median. returns the median of all numbers inserted in the class.
#
# If the count of numbers inserted in the class is even, the median will be the average of the middle two numbers.
#
# Use two heaps approach. [ maxHeap ][median][ minHeap ]
#
# time complexity: O(logN) due to heap insertion
#
# space complecity: O(N). we keep a list of all numbers at all times
#
from heapq import *

class MedianOfStream:

    def __init__(self):
        self.above = [] #maxHeap
        self.below = [] #minHeap

    def insert(self, num):
        if not self.above or num <= -self.above[0]:
            heappush(self.above, -num)
        else:
            heappush(self.below, num)

        #re-balance
        if len(self.above) > len(self.below):
            heappush(self.below, -heappop(self.above))
        elif len(self.above) < len(self.below):
            heappush(self.above, -heappop(self.below))
        
    def median(self):
        if len(self.above) > len(self.below):
            return -self.above[0] 

        if len(self.above) == len(self.below):
            return (-self.above[0] + self.below[0]) / 2

        else:
            return self.below[0]

# Tests

ms = MedianOfStream()

ms.insert(2)
assert ms.median() == 2

ms.insert(4)
assert ms.median() == 3

ms.insert(7)
assert ms.median() == 4

ms.insert(1)
assert ms.median() == 3

ms.insert(5)
assert ms.median() == 4

ms.insert(3)
assert ms.median() == 3.5

print("all tests passed.")
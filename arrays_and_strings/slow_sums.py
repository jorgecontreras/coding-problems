"""
Suppose we have a list of N numbers, and repeat the following operation until we're left with only a single number: 
Choose any two numbers and replace them with their sum. Moreover, we associate a penalty with each operation equal 
to the value of the new number, and call the penalty for the entire list as the sum of the penalties of each operation.

For example, given the list [1, 2, 3, 4, 5], we could choose 2 and 3 for the first operation, 
which would transform the list into [1, 5, 4, 5] and incur a penalty of 5. The goal in this problem 
is to find the worst possible penalty for a given input.

Example

arr = [4, 2, 1, 3]
output = 26
First, add 4 + 3 for a penalty of 7. Now the array is [7, 2, 1]
Add 7 + 2 for a penalty of 9. Now the array is [9, 1]
Add 9 + 1 for a penalty of 10. The penalties sum to 26.
"""

# Solution: Max Heap
#
# Store the numbers in a max heap so we can easily get the largest every time.
# Perform the sum and push it back to the max heap, keeping track of the total.
#
# Time complexity: O(NlogN)
# Space complexity: O(N)

from heapq import *

def getTotalTime(arr):
  max_heap = []
  total_sum = 0
  
  for n in arr:
    heappush(max_heap, -n)
    
  while len(max_heap) > 1:
    _sum = heappop(max_heap) + heappop(max_heap)
    total_sum += -_sum
    heappush(max_heap, _sum)
  
  return total_sum

assert getTotalTime([4,2,1,3]) == 26

print("all tests passed.")
# k smallest numbers

from heapq import *

def find_k_smallest_numbers(nums, k):
    minHeap = []

    for i in range(len(nums)):
        heappush(minHeap, nums[i])

    return list(minHeap)

nums = [3,1,5,12,11, -1, 33, 12, 90, 0]

print(find_k_smallest_numbers(nums, 3))
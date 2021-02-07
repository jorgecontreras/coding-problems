# K largest numbers

from heapq import *

def find_k_largest_numbers(nums, k):
    minHeap = []
    # insert k numbers in the minheap
    for i in range(k):
        heappush(minHeap, nums[i])

    for i in range(k, len(nums)):
        if minHeap[0] < nums[i]:
            heappop(minHeap)
            heappush(minHeap, nums[i])

    return list(minHeap)

nums = [3,1,5,12,11, -1, 33, 12, 90, 0]

print(find_k_largest_numbers(nums, 3))
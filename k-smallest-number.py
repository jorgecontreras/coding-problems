# k-smallest number

from heapq import *

def find_kth_smallest(nums, k):
    minHeap = []

    for i in range(len(nums)):
        heappush(minHeap, nums[i])

    while k > 0:
        k -= 1
        n = heappop(minHeap)

    return n

print(find_kth_smallest([1,5,3,8,5,6,5,0,1,4,-2], 5))
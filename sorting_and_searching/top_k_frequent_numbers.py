"""
Problem Statement:
Given an unsorted array of numbers, find the top ‘K’ frequently occurring numbers in it.

Example 1:

Input: [1, 3, 5, 12, 11, 12, 11], K = 2
Output: [12, 11]
Explanation: Both '11' and '12' apeared twice.
Example 2:

Input: [5, 12, 11, 3, 11], K = 2
Output: [11, 5] or [11, 12] or [11, 3]
Explanation: Only '11' appeared twice, all other numbers appeared once.

"""

# Time complexity: O(NlogK)
# Space complexity: O(N)

from heapq import *

def top_k_frequent(nums, k):
    top = []
    freq = {}
    heap = []

    for n in nums:
        freq[n] = freq.get(n, 0) + 1

    for n,f in freq.items():
        heappush(heap, (f,n))
        if len(heap) > k:
            heappop(heap)

    while len(heap) > 0:
        top.append(heappop(heap)[1])

    return top

assert top_k_frequent([1, 3, 5, 12, 11, 12, 11], 2) == [11, 12]

print("all tests passed.")
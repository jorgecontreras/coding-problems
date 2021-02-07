# array peak

"""
A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
"""

#linear scan
def array_peak_linear(nums):
    for i in range(len(nums) - 1):
        if nums[i] > nums[i+1]:
            return i 

    return len(nums) - 1


def array_peak_binary_search(nums):
    start, end = 0, len(nums) - 1

    while start < end:
        mid = start + (end-start) // 2
        
        if nums[mid] < nums[mid+1]:
            start = mid + 1
        else:
            end = mid

    return start


t1 = [1,2,1,3,5,6,4]
t2 = [7,6,5,4,3,2,1]
t3 = [0,0,0,1,1,1]
t4 = [0,2,3,1]
t5 = [2,2]
t6 = [1]
t7 = [0]
t8 = [-10,-5,-3,-1, 5, 6, 7, 4, 3, 8]

print(array_peak_linear(t1))
print(array_peak_linear(t2))
print(array_peak_linear(t3))
print(array_peak_linear(t4))
print(array_peak_linear(t5))
print(array_peak_linear(t6))
print(array_peak_linear(t7))
print(array_peak_linear(t8))

print("")
print(array_peak_binary_search(t1))
print(array_peak_binary_search(t2))
print(array_peak_binary_search(t3))
print(array_peak_binary_search(t4))
print(array_peak_binary_search(t5))
print(array_peak_binary_search(t6))
print(array_peak_binary_search(t7))
print(array_peak_binary_search(t8))


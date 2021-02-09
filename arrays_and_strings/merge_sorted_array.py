# MERGE SORTED ARRAY

# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
#
# Three pointers
# 
# Time complexity: O(m+n)
# Space complexity : O(m)
#
# Example 1:
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
#
# Example 2:
# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]

def merge(nums1, m, nums2, n):
    i = len(nums1) - 1

    while m > 0 and n > 0:
        if nums1[m-1] >= nums2[n-1]:
            nums1[i] = nums1[m-1]
            m -= 1
        else:
            nums1[i] = nums2[n-1]
            n -= 1
        i -= 1

    while n > 0:
        nums1[i] = nums2[n-1]
        i -= 1
        n -= 1
    
    return nums1

assert merge([1], 1, [], 0) == [1]
assert merge([1,2,3,0,0,0], 3, [2,5,6], 3) == [1, 2, 2, 3, 5, 6]
assert merge([0], 0, [1], 1) == [1]

print("all tests passed.")
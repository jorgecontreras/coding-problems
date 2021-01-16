# merge sorted array

# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]

# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]

def merge(nums1, m, nums2, n):
    pointer = len(nums1) - 1
        
    while m > 0 and n > 0:
        if nums1[m-1] >= nums2[n-1]:
            nums1[pointer] = nums1[m-1]
            m -= 1
        else:
            nums1[pointer] = nums2[n-1]
            n -= 1
        pointer -= 1
        
    while n > 0:
        nums1[pointer] = nums2[n-1]
        n -= 1
        pointer -= 1
    return nums1

    
    



print(merge([1], 1, [], 0))
print(merge([1,2,3,0,0,0], 3, [2,5,6], 3))
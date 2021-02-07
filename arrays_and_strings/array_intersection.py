# Array intersection two arrays, unsorted
# time complexity: O(N + M)
# space complexity: O(N + M)
"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]

Input nums1 = [2, 3, 6, 9]
Input nums2 = [4, 5, 6, 9]
"""

def intersection(nums1, nums2):
    s1 = set(nums1)
    s2 = set(nums2)

    return [n for n in s1 if n in s2]
    
    
nums1 = [2, 3, 6, 9]
nums2 = [4, 5, 6, 9]
nums3 = [4,9,5]
nums4 = [9,4,9,8,4]
nums5 = [1,2,2,1]
nums6 = [2,2]

print(intersection(nums1, nums2))
print(intersection(nums3, nums4))
print(intersection(nums5, nums6))

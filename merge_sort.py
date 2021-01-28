# merge sort

# O(n log n): cuts the input by two every time and then it takes n time to merge each

def merge(left, right):
    merged = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged += left[i:]
    merged += right[j:]

    return merged

def merge_sort(nums):

    # base case 
    if len(nums) <= 1:
        return nums
    
    mid = len(nums) // 2

    left = nums[:mid]
    right = nums[mid:]

    left = merge_sort(left)
    right = merge_sort(right)
        
    return merge(left, right)


nums1 = [2,5,7,2,7,8,2,8,2,74,14,5,4,3,33,6,8,8]
nums2 = [5,1,8,23,6,8,2,6,1,6,1,89,4]

assert sorted(nums1) == merge_sort(nums1)
assert sorted(nums2) == merge_sort(nums2)
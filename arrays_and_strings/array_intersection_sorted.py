# array intersection two sorted arrays O(N) time O(1) space

def intersection(nums1, nums2):
    i = j = 0

    result = set()
    
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            result.add(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1

    return list(result)

nums1 = [2,3,3,4,5,6,8,9]
nums2 = [1,3,5,7,8,9,10,11]
ans1 = [3,5,8,9]

nums3 = [8,9,10,11,12]
nums4 = [11,12,13]
ans2 = [11,12]

print(intersection(nums1, nums2))
print(intersection(nums3, nums4))


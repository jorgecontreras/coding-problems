# find duplicates

# sort the array using cyclic sort

# traverse the sorted array
# elements not in its correct position are duplicates

def cyclic_sort(nums):
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[j], nums[i] = nums[i], nums[j]
        else:
            i += 1
    
    dups = []
    for i in range(len(nums)):
        if nums[i] != i + 1:
            dups.append(nums[i])

    return dups

t1 = [4,5,2,2,3,5]
print(cyclic_sort(t1))

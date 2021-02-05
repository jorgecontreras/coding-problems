# cyclic_sort

# start the iterations
# swap each number encountered to its correct position
# only increase i when the current number is already at its correct position
#
# i: current position
# j: correct position

def cyclic_sort(nums):
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[j], nums[i] = nums[i], nums[j]
        else:
            i += 1
    return nums

t1 = [4,6,2,1,3,5]
print(cyclic_sort(t1))
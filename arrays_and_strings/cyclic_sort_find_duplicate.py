# find the duplicate number

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
        if nums[i] != i + 1:
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                return nums[i]
        else:
            i += 1

t1 = [1,6,2,6,3,5]
print(cyclic_sort(t1))

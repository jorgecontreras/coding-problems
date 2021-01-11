# cyclic-sort

# You are given an unsorted array containing numbers from the range 1 to n. 
# The array can have duplicates, which means that some numbers will be missing. 
# Find all the missing numbers.

def cyclic_sort(nums):
    for i in range(len(nums)):
        while nums[i] != i+1:
            swp = nums[i]
            nums[i] = nums[nums[i] - 1]
            nums[swp - 1] = swp

    return nums

arr = [3,1,5,4,2]

answer = cyclic_sort(arr)
print(answer)
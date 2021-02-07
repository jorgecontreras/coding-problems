# cyclic sort - find the missing number

def find_missing(nums):
    i, n = 0, len(nums)

    while i < n:
        j = nums[i]
        if nums[i] < n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i in range(len(nums)):
        if nums[i] != i:
            return i

t1 = [4, 0, 3, 1]
t2 = [8, 3, 5, 2, 4, 6, 0, 1]
t3 = [4, 3, 1, 2, 0]

assert find_missing(t1) == 2
assert find_missing(t2) == 7
assert find_missing(t3) == None

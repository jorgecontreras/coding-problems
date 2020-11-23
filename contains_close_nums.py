def containsCloseNums(nums, k):
    r = {}
    
    for i, num in enumerate(nums):
        if num in r:
            if i - r[num] <= k:
                return True
        r[num] = i
    return False

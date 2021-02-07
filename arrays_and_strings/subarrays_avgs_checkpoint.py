def find_averages_of_subarrays(k, nums):
    
    _sum = 0
    start = 0
    result = []

    for i in range(len(nums)):
        _sum += nums[i]
        if i-start >= k - 1:
            result.append(_sum / k)
            _sum -= nums[start]
            start += 1
    return result




# TESTS
arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 5

slide = find_averages_of_subarrays(k, arr)

print(slide)
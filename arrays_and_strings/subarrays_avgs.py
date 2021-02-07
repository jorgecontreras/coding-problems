# PROBLEM
# Given an array, find the average of all contiguous subarrays of size K in it

# SOLUTIONS
#
# brute force  O(N * K)
def find_averages_of_subarrays(k, arr):
    r = []
    for i in range(len(arr)-k+1):
        sub = arr[i:i+k]
        t = 0
        for n in sub:
            t += n
        avg = t/k
        r.append(avg)
    return r


# sliding window O(N)
def find_averages_of_subarrays_sliding(k, arr):
    r = []
    t = 0
    start = 0
    for end in range(len(arr)):
        t += arr[end]
        if end >= k - 1:
            r.append(t/k)
            t -= arr[start]
            start += 1
    return r




# TESTS
arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 5

bf = find_averages_of_subarrays(k, arr)
slide = find_averages_of_subarrays_sliding(k, arr)

print(bf)
print(slide)
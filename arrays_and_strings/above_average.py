
"""
Above Average subarrays:

You are given an array A containing N integers. 
Find all subarrays whose average sum is greater than 
the average sum of the remaining array elements. 
You must return the start and end index of each subarray in sorted order.

"""

# find all subarrays of arr
def find_subarrays(arr, start, end, result):
    #base case
    if end == len(arr):
        return result

    # window has closed, reset and increase window size by 1
    elif start > end:
        return find_subarrays(arr, 0, end+1, result)

    # keep closing the window
    else:
        _sum = sum(arr[start:end+1])
        average_sum = _sum / (end-start + 1)
        size = end - start + 1
        subarray = ([start+1, end+1], _sum, average_sum, size)
        result.append(subarray)
        return find_subarrays(arr, start + 1, end, result)

def above_avg(arr):
    total = sum(arr)
    
    subs = find_subarrays(arr, 0, 0, [])

    ans = []
    
    for sub in subs:
        outside_size = len(arr) - sub[3]
        if outside_size > 0:
            outside_avg = (total - sub[1]) / outside_size
        else:
            outside_avg = 0
        
        if sub[2] > outside_avg:
            ans.append(sub[0])

    return ans


arr = [3,4,2]

print(above_avg(arr))
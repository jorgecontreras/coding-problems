
# find all subarrays of arr
def find_subarrays(arr, start, end):
    #base case
    if end == len(arr):
        return

    # window has closed, reset and increase window size by 1
    elif start > end:
        return find_subarrays(arr, 0, end+1)

    # keep closing the window
    else:
        print(arr[start:end+1])
        return find_subarrays(arr, start + 1, end)


arr = [3,4,2]
find_subarrays(arr, 0, 0)
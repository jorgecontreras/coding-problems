
# O(N^2)
def duplicateZeros(arr):
    """
    Do not return anything, modify arr in-place instead.
    """
    i = 0 
    while i < len(arr):
        if arr[i] == 0:
            for j in range(len(arr) - 1, i, -1):
                arr[j] = arr[j-1]
            if i+1 < len(arr):
                arr[i+1] = 0
                i += 1
        i += 1

t1 = [1,0,2,3,0,4,5,0]
duplicateZeros(t1)
assert t1 == [1,0,0,2,3,0,0,4]

print("all tests passed.")
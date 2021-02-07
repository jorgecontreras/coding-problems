def findMinArray(arr, k):
    
    for i in range(len(arr)):
        pos = i
        for j in range(i+1, len(arr)):
            if j-i > k:
                break

            if arr[j] < arr[pos]:
                pos = j

        for j in range(pos, i, -1):
            arr[j], arr[j-1] = arr[j-1], arr[j]

        k -= pos - i

    return arr


t1 = [8, 9, 10, 12, 11]
k1 = 1

t2 = [6, 7, 8, 9, 3, 4, 2]
k2 = 4

t3 = [6, 7, 8, 9, 3, 4, 2]
k3 = 7

assert findMinArray(t1, k1) == [8, 9, 10, 11, 12]
assert findMinArray(t2, k2) == [3, 6, 7, 8, 9, 4, 2]
assert findMinArray(t3, k3) == [2, 6, 7, 8, 3, 9, 4]

print("all test passed.")


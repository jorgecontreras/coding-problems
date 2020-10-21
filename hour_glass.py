
# Complete the hourglassSum function below.
def hourglassSum(arr):
    highest = None
    for row in range(4):
        for col in range(4):
            this_clock = 0
            this_clock += arr[row][col] + arr[row][col+1] + arr[row][col+2] + arr[row+1][col+1] + arr[row+2][col] + arr[row+2][col+1] + arr[row+2][col+2]
            if highest is None or this_clock > highest:
                highest = this_clock

    return highest

arr = []

for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

print(arr)

#result = hourglassSum(arr)

#print(result)

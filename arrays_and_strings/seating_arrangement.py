def minOverallAwkwardness1(arr):
    arr.sort()
    
    seats = zip(arr,arr[2:])

    return max(abs(a-b) for a,b in seats)

print(minOverallAwkwardness1([2,4,2,4,2,4,14]))


# CONTAINER WITH MOST WATER
# 
# Two pointers
#
# Use two pointers, calculate volume at each pair. 
# then choose to increase left or decrease right depending on which is higher
#
# Time complexity: O(N)
# Space complexity: O(1)

def max_water(arr):
    left = 0
    right = len(arr) - 1
    max_volume = 0

    while left < right:
        volume = min(arr[left], arr[right]) * (right-left)
        max_volume = max(max_volume, volume)

        if arr[left] > arr[right]:
            right -= 1

        else:
            left += 1

    return max_volume

t1 = [1,8,6,2,5,4,8,3,7]
t2 = [1,1]
t3 = [4,3,2,1,4]
t4 = [1,2,1]
t5 = [2,3,4,5,18,17,6]
t6 = [1,3,2,5,25,24,5]

assert max_water(t1) == 49
assert max_water(t2) == 1
assert max_water(t3) == 16
assert max_water(t4) == 2
assert max_water(t5) == 17
assert max_water(t6) == 24

print("all tests passed.")
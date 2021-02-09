# CONTAINER WITH MOST WATER
# 
# Time Limit Exceeded!
#
# Time complexity: O(N^2): The process of finding all subarrays is time consuming and is not necessary. 
# Space complexity: O(1)
#  

def max_water(arr):
    
    max_volume = 0
    start = 0
    end = 0

    while end < len(arr):
        
        volume = min(arr[start], arr[end]) * (end-start)
        max_volume = max(max_volume, volume)
        
        if start >= end:
            start = 0
            end += 1
        else:
            start += 1

    return max_volume

t1 = [1,8,6,2,5,4,8,3,7]
t2 = [1,1]
t3 = [4,3,2,1,4]
t4 = [1,2,1]
t5 = [2,3,4,5,18,17,6]
t6 = [1,3,2,5,25,24,5]

print(max_water(t1))
print(max_water(t2))
print(max_water(t3))
print(max_water(t4))
print(max_water(t5))
print(max_water(t6))
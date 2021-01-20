# squaring sorted array
from heapq import *

def make_squares(nums):
    result = []

    p1 = 0
    p2 = len(nums) - 1

    while p1 <= p2:
        l = nums[p1] * nums[p1]
        r = nums[p2] * nums[p2]

        if l >= r:
            result.append(l)
            p1 += 1
        else:
            result.append(r)
            p2 -= 1

    return result[::-1]


print(make_squares([-2, -1, 0, 2, 3]))
print(make_squares([-3, -1, 0, 1, 2]))
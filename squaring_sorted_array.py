# squaring sorted array

# Given a sorted array, create a new array containing squares of all the numbers of the input array in the sorted order.

# Example 1:
#
# Input: [-2, -1, 0, 2, 3]
# Output: [0, 1, 4, 4, 9]
#
#
# Example 2:
#
# Input: [-3, -1, 0, 1, 2]
# Output: [0, 1, 1, 4, 9]

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
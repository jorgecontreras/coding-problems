# find unique number
#
# XOR trick:
#
# 2 ^ 2 = 0
# 1 ^ 1 = 0
# 3 ^ 0 = 3
# a number XOR with itself resuts in zero
# we can use this property as a bit mask to discover the number that does not "cancel" itself.

def find_unique(nums):
    a = 0
    for i in nums:
        a ^= i

    return a

t1 = [2,1,2,3,5,1,6,5,6]

assert find_unique(t1) == 3

print("all tests passed.")
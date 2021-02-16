"""
Given an array of integers in which two elements appear exactly once and all other elements appear exactly twice, find the two elements that appear only once.

For example, given the array [2, 4, 6, 8, 10, 2, 6, 10], return 4 and 8. The order does not matter.

Follow-up: Can you do this in linear time and constant space?
"""

# time complexity: O(N)
# space complexity: O(N)
def solution_hashmap(nums):
    seen = set()
    for n in nums:
        if n not in seen:
            seen.add(n)
        else:
            seen.remove(n)

    return list(seen)

# hint: if we XOR a number with itself odd number of times the result is the number itself, otherwise it's 0
# time complexity: O(N)
# space complexity: O(1)
def solution_bitmask(nums):
    #find the numbers that appear odd number of times (like once)
    a = 0
    for n in nums:
        a ^= n 

    # now separate those two numbers
    diff = a & -(a)

    b = 0
    for n in nums:
        if n & diff:
            b ^= n

    return [b, a^b]

t1 = [2, 4, 6, 8, 10, 2, 6, 10]
assert solution_hashmap(t1) == [4,8]
assert solution_bitmask(t1) == [4,8]

print("all tests passed.")
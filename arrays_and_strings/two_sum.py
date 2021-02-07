# two sum in O(n) time

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

def two_sum(nums, target):
    
    seen = dict()

    for i, n in enumerate(nums):
        diff = target - n

        if diff in seen:
            return [seen[diff], i]
        else:
            seen[n] = i

t1 = [-1, -2, -3, -4, -5]
t2 = [2,7,11,15]
t3 = [3,2,4]
t4 = [3,3]

assert two_sum(t1, -8) == [2, 4]
assert two_sum(t2, 9) == [0, 1]
assert two_sum(t3, 6) == [1, 2]
assert two_sum(t4, 6) == [0, 1]
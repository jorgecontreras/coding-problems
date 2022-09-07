# MAX INCREASING SUBSEQ
"""
Write a function, max_increasing_subseq, that takes in a list of numbers as an argument. 
The function should return the length of the longest subsequence of strictly increasing numbers.

A subsequence of a list can be created by deleting any items of the list, while maintaining the relative order of items.
"""
# dynamic programming YES
# exhaustive recursion? NO
# two pointers? NO

# Time complexity: O(n^2)
# Space complexity: O(n^2)
def max_increasing_subseq(nums):
    start = 0
    previous = float("-inf")
    dp = {}
    return _max_increasing(nums, start, previous, dp)

def _max_increasing(nums, i, prev, dp):
    key = (i, prev)
    if key in dp:
        return dp[key]

    if len(nums) == i:
        return 0

    # binary decision: take or not take
    exclude = _max_increasing(nums, i+1, prev, dp)
    include = float('-inf')
    # only include if the current number is larger than the previous
    if nums[i] > prev:
        include = 1 + _max_increasing(nums, i+1, nums[i], dp)

    dp[key] = max(include, exclude)
    return dp[key]

# tests
t1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]

assert max_increasing_subseq(t1) == 21
assert max_increasing_subseq([12, 9, 2, 5, 4, 32, 90, 20]) == 4
assert max_increasing_subseq([42, 50, 51, 60, 55, 70, 4, 5, 70]) == 5

print("All tests passed!")
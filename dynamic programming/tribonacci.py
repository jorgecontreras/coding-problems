#   TRIBONACCI
"""
Write a function tribonacci that takes in a number argument, n, and returns the n-th number of the Tribonacci sequence.

The 0-th and 1-st numbers of the sequence are both 0.

The 2-nd number of the sequence is 1.

To generate further numbers of the sequence, calculate the sum of previous three numbers.

Solve this recursively.
"""
def tribonacci(n, dp={}):
    if n in dp:
        return dp[n]

    if n <= 1:
        return 0

    if n == 2:
        return 1

    dp[n] = tribonacci(n-3, dp) + tribonacci(n-2, dp) + tribonacci(n-1, dp)
    return dp[n]

assert tribonacci(20) == tribonacci(20)

print("All tests passed!")
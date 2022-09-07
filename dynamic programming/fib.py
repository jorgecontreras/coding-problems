# FIB
"""
Write a function fib that takes in a number argument, n, and returns the n-th number of the Fibonacci sequence.
The 0-th number of the sequence is 0.
The 1-st number of the sequence is 1.
To generate further numbers of the sequence, calculate the sum of previous two numbers.
Solve this recursively.
"""

def fib(n, dp={}):
    if n in dp:
        return dp[n]

    if n <= 2:
        return 1

    dp[n] = fib(n-2, dp) + fib(n-1, dp)
    return dp[n]

assert fib(5) == 5
assert fib(35) == 9227465

print("All tests passed!")
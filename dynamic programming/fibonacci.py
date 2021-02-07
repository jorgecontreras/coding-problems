
def fib(n, dp):

    if n in dp:
        return dp[n]

    if n <= 1:
        return n

    ans = fib(n-1, dp) + fib(n-2, dp)
    dp[n] = ans
    return dp[n]

dp = {}
print(fib(80, dp))
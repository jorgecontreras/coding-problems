# COIN CHANGE
#
# Dynamic Programming - Bottom Up
#

def coin_change(coins, amount):
    # initialize dp with higher value (amount + 1)
    dp = [0] + [amount + 1] * amount

    # compute each amount, bottom up:
    # dp[0], dp[1], dp[2], dp[3] ... dp[amount]
    for a in range(1, amount + 1):
        for c in coins:
            if a - c >= 0: # check the coin does not exceed the required amount
                dp[a] = min(1 + dp[a - c], dp[a])

    return dp[amount] if dp[amount] != amount + 1 else -1

t1 = [1,2,5]
a1 = 11

t2 = [2]
a2 = 3

assert coin_change(t1, a1) == 3
assert coin_change(t2, a2) == -1

print("all tests passed.")
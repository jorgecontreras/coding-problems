def solve_knapsack(profits, weights, capacity):
    #initialize cache
    dp = [[-1 for x in range(capacity + 1)] for y in range(len(profits))]

    return knapsack(dp, profits, weights, capacity, 0)

def knapsack(dp, profits, weights, capacity, index):

    # base case
    if index >= len(weights) or capacity <= 0:
        return 0

    # query cache
    if dp[index][capacity] != -1:
        return dp[index][capacity]

    # include item
    p1 = 0
    if capacity - weights[index] >= 0:
        p1 = profits[index] + knapsack(dp, profits, weights, capacity - weights[index], index + 1)

    # dont include item
    p0 = knapsack(dp, profits, weights, capacity, index + 1)

    #pick best profit and store in cache
    dp[index][capacity] = max(p0, p1)
    return dp[index][capacity]

def main():
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))


main()    
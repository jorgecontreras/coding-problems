# Knapsack 
#
# Recursion
#
# Time complexity: 2^n, where n is the number of items
# Space complexity: O(n). space to store the recursion stack

def solve_knapsack(profits, weights, capacity):
    return knapsack(profits, weights, capacity, 0)

def knapsack(profits, weights, capacity, index):

    # base case
    if index >= len(weights) or capacity <= 0:
        return 0

    # include item
    p1 = 0
    if capacity - weights[index] >= 0:
        p1 = profits[index] + knapsack(profits, weights, capacity - weights[index], index + 1)

    # dont include item
    p0 = knapsack(profits, weights, capacity, index + 1)

    #pick best profit
    return max(p0, p1)

def main():
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))


main()    
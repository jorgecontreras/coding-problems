# max stock gain

from heapq import *

def max_stock_gain(prices, k):

    own = False
    gains = []

    for i in range(len(prices) - 1):
        if prices[i] < prices[i+1]:
            if not own:
                bought_at = prices[i]
                own = True
        else:
            if own:
                sold_at = prices[i]
                own = False
                gain = sold_at - bought_at
                heappush(gains, -gain)
    
    if own and prices[-1] > prices[-2]:
        sold_at = prices[len(prices)-1]
        own = False
        gain = sold_at - bought_at
        heappush(gains, -gain)

    max_gain = 0
    while gains and k > 0:
        gain = -heappop(gains)
        max_gain += gain
        k -= 1

    return max_gain


prices = [5, 2, 4, 0, 1]
k = 2

print(max_stock_gain(prices, k))

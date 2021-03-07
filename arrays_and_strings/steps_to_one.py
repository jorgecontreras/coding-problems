# STEPS TO ONE

# Given a positive integer N, find the smallest number of steps it will take to reach 1.

# There are two kinds of permitted steps:

# You may decrement N to N - 1.
# If a * b = N, you may decrement N to the larger of a and b.
# For example, given 100, you can reach 1 in five steps with the following route: 100 -> 10 -> 9 -> 3 -> 2 -> 1.
from math import sqrt

def steps(n):
    sequence = [n]
    while n > 1:
        
        # find divisors of n
        divs = []
        for i in range(1, n):
            d = n / i
            if d % 1 == 0:
                divs.append([d, i])
                
        mid = len(divs) // 2
        b = max(divs[mid])
        if b < n:
            n = int(b)
        else:
            n -= 1
        sequence.append(n)

    return sequence

print(steps(100)) 
print(steps(30))
print(steps(28))


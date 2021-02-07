# PROBLEM STATEMENT: 
# Given an integer n, find the next biggest integer with the same number of 1-bits on. For example, given the number 6 (0110 in binary), return 9 (1001)

def count_bits(n):
    c = 0
    while n:
        n &= n-1
        c += 1
    return c

def next_biggest(n):
    a = count_bits(n)
    x = n+1
    while count_bits(x) != a:
        x += 1

    return x

n1 = 6 # 1001
n2 = 5 # 0110
n3 = 8 # 10000
n4 = 1 # 0010
n5 = 3 # 0101

assert next_biggest(n1) == 9
assert next_biggest(n2) == 6
assert next_biggest(n3) == 16
assert next_biggest(n4) == 2
assert next_biggest(n5) == 5
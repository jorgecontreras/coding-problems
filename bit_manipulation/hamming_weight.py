# hamming weight

def hammingWeight(n):
    ones = 0

    while n:
        n &= n-1
        ones += 1
    return ones

data = 0b00000000010000000000000000001011
print(hammingWeight(data))
# count bits (Hamming weight)

def count_bits(n):
    c = 0
    while n:
        n &= n - 1
        c += 1
    return c

assert count_bits(0b11001100) == 4
assert count_bits(0b00000000000000000000000000001011) == 3
assert count_bits(0b00000000000000000000000010000000) == 1
assert count_bits(0b11111111111111111111111111111101) == 31

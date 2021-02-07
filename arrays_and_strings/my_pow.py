def myPow(x: float, n: int) -> float:
    # base condition
    if n == 0:
        return 1
 
    # calculate sub-problem recursively
    pow = myPow(x, n // 2)
 
    if n & 1:  # if y is odd
        return x * pow * pow
 
    # else y is even
    return pow * pow

print(myPow(2, -2))
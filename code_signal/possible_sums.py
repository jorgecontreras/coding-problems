def possibleSums(coins, quantity):
    
    sums = set()
    
    for c,q in zip(coins, quantity):
        prev = sums.copy()
        for n in range(1, q+1):
            v = n*c
            sums.add(v)
            for p in prev:
                sums.add(p+v)    
    
    return len(sums)

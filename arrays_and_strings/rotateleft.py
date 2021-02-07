def rotLeft(a, d):
    d = d % len(a)
    
    result = []
    p = d
        
    for _ in range(len(a)):
        result.append(a[p])
        if p >= len(a) - 1:
            p = 0
        else:
            p += 1

    return result
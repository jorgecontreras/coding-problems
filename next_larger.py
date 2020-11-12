def nextLarger(a):
    for i, n in enumerate(a):
        swap = False
        for j in range(i+1, len(a)):
            if a[j] > a[i]:
                a[i] = a[j]
                swap = True
                break
                
        if not swap:
            a[i] = -1
    
    a[len(a) - 1] = -1
    return a

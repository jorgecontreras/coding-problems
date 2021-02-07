# Rotate elements of array a, by a number of d positions t

def rotLeft(a, d):
    d = d % len(a) #d=2
    
    result = []
    p = d #p=2
        
    for _ in range(len(a)):
        result.append(a[p]) #[24,5,36]
        if p >= len(a) - 1:
            p = 0
        else:
            p += 1 #p=5

    return result

t1 = [1,3,24,5,36,0,8]
k1 = 2

print(rotLeft(t1, k1))
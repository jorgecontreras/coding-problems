
# brute-froce solution O(n^2)

def nextLargerSlow(a):
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


# using stack O(n)

def nextLarger(a):
    n = len(a)
    ans = [-1 for _ in range(n)]
    stack = []
    stack.append(0)

    for i in range(1, n):
        while stack and a[stack[-1]] < a[i]:
            ans[stack[-1]] = a[i]
            stack.pop()
        stack.append(i)
    
    return ans

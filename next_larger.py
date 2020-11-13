
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

class Stack():
    def __init__(self):
        self.size = 0
        self.items = []

    def push(self, value):
        self.items.append(value)
        self.size += 1

    def pop(self):
        if self.size > 0:
            item = self.items.pop()
            self.size -= 1
            return item
        return None

    def peek(self):
        if self.size > 0:
            return self.items[self.size - 1]
        return None


def nextLargerFast(a):
    n = len(a)
    ans = [-1 for _ in range(n)]
    stack = Stack()
    stack.push(0)

    for i in range(1, n):
        while stack.size > 0 and a[stack.peek()] < a[i]:
            ans[stack.peek()] = a[i]
            stack.pop()
        stack.push(i)
    
    return ans

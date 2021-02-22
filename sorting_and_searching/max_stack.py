# Max Stack
# Design a stack that supports push, pop, top, and retrieving the maximum element in constant time.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# largest() -- Retrieve the maximum element in the stack.
 

class MaxStack:
    def __init__(self):
        self.stack = []
        self.max = []

    def push(self, x):
        self.stack.append(x)
        if not self.max or x > self.max[-1]:
            self.max.append(x)

    def pop(self):
        if self.stack[-1] == self.max[-1]:
            self.max.pop()
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def largest(self):
        return self.max[-1]

# tests
ms = MaxStack()

ms.push(5)
ms.push(7)    
assert ms.largest() == 7
ms.push(9)
assert ms.largest() == 9
ms.pop()
assert ms.top() == 7
ms.pop()
assert ms.largest() == 5

print("all tests passed.")
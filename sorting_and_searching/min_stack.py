# Min Stack
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
 
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x):
        self.stack.append(x)
        if not self.min_stack or x < self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        if self.min_stack[-1] == self.stack[-1]:
            self.min_stack.pop()

        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]

# tests
ms = MinStack()

ms.push(9)
ms.push(4)

assert ms.getMin() == 4
ms.push(1)
assert ms.top() == 1
assert ms.getMin() == 1
ms.push(12)
ms.push(2)
ms.pop()
assert ms.top() == 12
assert ms.getMin() == 1

print("all tests passed.")
def decodeString(s):
    stack = []
    for c in s:
        if c == ']':
            sub = stack.pop()
            while sub[0] != '[':
                sub = stack.pop() + sub
            n = stack.pop()
            while stack and stack[-1].isnumeric():
                n = stack.pop() + n
            stack.extend(sub[1:] * int(n))
        else:
            stack.append(c)
        
    return ''.join(stack)

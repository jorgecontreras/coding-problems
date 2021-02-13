def valid_parentheses(s):
    matches = {
        ")": "(",
        "}": "{",
        "]": "["
    }
    stack = []
    for c in s:
        if c not in matches:
            stack.append(c)
        else:
            if not stack or stack[-1] != matches[c]:
                return False
            stack.pop()

    return len(stack) == 0


assert valid_parentheses("{[]}") ==  True
assert valid_parentheses("([)]") == False
assert valid_parentheses("(]") == False 
assert valid_parentheses("()[]{}") == True
assert valid_parentheses("()") == True

print("all tests passed.")
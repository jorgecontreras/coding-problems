"""
VALID PARENTHESIS - BALANCED BRACKETS

A bracket is considered to be any one of the following characters: (, ), {, }, [, or ].
We consider two brackets to be matching if the first element is an open-bracket, e.g., (, {, or [, and the second bracket is a close-bracket of the same type, e.g., ( and ), [ and ], and { and } are the only pairs of matching brackets.
Furthermore, a sequence of brackets is said to be balanced if the following conditions are met:

    - The sequence is empty, or
    - The sequence is composed of two, non-empty, sequences both of which are balanced, or
    - The first and last brackets of the sequence are matching, and the portion of the sequence without the first and last elements is balanced.

You are given a string of brackets. Your task is to determine whether each sequence of brackets is balanced. If a string is balanced, return true, otherwise, return false
"""

# Solution: 
#
# Use a stack. Add opening brackets to the stack. When a closing bracket is found, the top of the stack must be the matching bracket.
#
# Time complexity: O(N). Iterate the string one character at a time, for the length of the string.
# Space complexity: O(N). To store the brackets in a stack, worst case would be that we have only opening brackets.

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
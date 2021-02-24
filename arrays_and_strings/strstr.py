"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Example 3:

Input: haystack = "", needle = ""
Output: 0

"""
def strStr(haystack, needle):
        
    left, right = 0, 0
    sub = ""
    
    while right < len(haystack):
        while right-left < len(needle) and right-left < len(haystack):
            sub += haystack[right]
            if sub == needle:
                return left
            right += 1
        left += 1
        sub = sub[1:]
        
    return -1

assert strStr("hello", "ll") == 2
assert strStr("aaa", "aaaa") == -1

print("all tests passed.")
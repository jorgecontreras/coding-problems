# Given a string s, find the length of the longest substring without repeating characters.
#
# Time complexity: O(N)
# Space complexity: O(N)

def longest_no_repeat(s):
    left = 0
    max_size = 0
    window = {}
    
    for i in range(len(s)):
        window[s[i]] = window.get(s[i], 0) + 1
        
        while window[s[i]] > 1:
            window[s[left]] -= 1
            left += 1
            
        max_size = max(max_size, i-left+1)
    return max_size

t1 = "pwwkew"
t2 = "abcabcbb"
t3 = "bbbbbb"
t4 = ""
t5 = " "
t6 = "x"
t7 = "abcdefg"
t8 = " c"

print(longest_no_repeat(t1))
print(longest_no_repeat(t2))
print(longest_no_repeat(t3))
print(longest_no_repeat(t4))
print(longest_no_repeat(t5))
print(longest_no_repeat(t6))
print(longest_no_repeat(t7))
print(longest_no_repeat(t8))